import pandas as pd
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
import re
import os
import copy

# --- CONFIGURATION ---
INPUT_FILE = 'timetable.csv'
TEMPLATE_FILE = 'template_1.docx' # Must contain a table with 9 columns (Day + 8 slots)
OUTPUT_DIR = 'Merged_Timetables'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_cell_content(row, slot_col):
    """Parses the CSV cell to extract clean text."""
    val = str(row[slot_col])
    if not val or val == 'nan' or 'lunch' in val.lower():
        return ""
    return val.strip()

def merge_cells_logic(table_row, data_row):
    """
    Fills a row and merges cells if consecutive slots have identical content.
    """
    # 1. Fill the "Day" column (Column 0)
    cell_day = table_row.cells[0]
    cell_day.text = data_row['Day']
    cell_day.paragraphs[0].runs[0].font.bold = True

    # 2. Iterate through slots (S1 to S8) -> Columns 1 to 8
    # We maintain a 'start_index' to know where the current merge block began
    start_col_idx = 1 
    previous_content = get_cell_content(data_row, 'S1')
    
    # We loop from S2 (col 2) up to S8 (col 8) + 1 extra iteration to finish the last block
    slot_cols = [f'S{i}' for i in range(1, 9)]
    
    for i in range(1, len(slot_cols)):
        current_slot = slot_cols[i]
        current_col_idx = i + 1 # Column index in Word table
        
        current_content = get_cell_content(data_row, current_slot)

        # CHECK: Is this slot different from the previous one?
        if current_content != previous_content:
            # A block has ended. Process the *previous* block.
            
            # Get the range of cells to merge: [start_col_idx ... current_col_idx - 1]
            first_cell = table_row.cells[start_col_idx]
            last_cell = table_row.cells[current_col_idx - 1]
            
            # Merge if the block spans more than 1 cell
            if first_cell != last_cell:
                first_cell.merge(last_cell)
            
            # Write the text into the (now merged) first cell
            first_cell.text = previous_content
            
            # Style the cell (Center text)
            if previous_content:
                for paragraph in first_cell.paragraphs:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            # Reset for the new block
            start_col_idx = current_col_idx
            previous_content = current_content

    # 3. Handle the final block (The last slot, S8)
    first_cell = table_row.cells[start_col_idx]
    last_cell = table_row.cells[8] # The last column
    
    if first_cell != last_cell:
        first_cell.merge(last_cell)
        
    first_cell.text = previous_content
    if previous_content:
        for paragraph in first_cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

def generate_classwise(df):
    """Generates one docx per room using the template."""
    print("Generating Class-wise Timetables...")
    
    grouped = df.groupby('Room')
    
    for room, group in grouped:
        # Load the clean template for every room
        doc = Document(TEMPLATE_FILE)
        
        # Find the table (Assuming it's the first table in the doc)
        if not doc.tables:
            print("Error: No table found in template.docx")
            return
        table = doc.tables[0]
        
        # Set Title (Optional: Finds a paragraph "{{ title }}" and replaces it)
        for p in doc.paragraphs:
            if "{{ title }}" in p.text:
                p.text = p.text.replace("{{ title }}", f"Class Timetable - Room {room}")

        # Sort Days
        day_order = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5}
        group['day_num'] = group['Day'].map(day_order)
        group = group.sort_values('day_num')

        # Add Rows and Merge
        for _, row in group.iterrows():
            new_row = table.add_row()
            merge_cells_logic(new_row, row)
            
        output_path = os.path.join(OUTPUT_DIR, f"Class_{room}.docx")
        doc.save(output_path)
        print(f"Saved: {output_path}")

def generate_teacherwise(df):
    """Generates one docx per teacher using the template."""
    print("Generating Teacher-wise Timetables...")
    
    # 1. Pivot Logic to reconstruct teacher rows
    records = []
    slot_cols = [f'S{i}' for i in range(1, 9)]
    
    for _, row in df.iterrows():
        room = row['Room']
        day = row['Day']
        for slot in slot_cols:
            val = str(row[slot])
            if not val or val == 'nan' or 'lunch' in val.lower():
                continue
            
            match = re.search(r'(.*)\s+\(([^)]+)\)$', val)
            if match:
                subject = match.group(1).strip()
                teacher = match.group(2).strip()
                records.append({
                    'Teacher': teacher,
                    'Day': day,
                    'Slot': slot,
                    'Content': f"{subject}\n({room})"
                })
    
    if not records: return
    t_df = pd.DataFrame(records)
    
    unique_teachers = sorted(t_df['Teacher'].unique())
    days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    for teacher in unique_teachers:
        doc = Document(TEMPLATE_FILE)
        table = doc.tables[0]
        
        # Set Title
        for p in doc.paragraphs:
            if "{{ title }}" in p.text:
                p.text = p.text.replace("{{ title }}", f"Teacher Timetable: {teacher}")

        # Filter data for this teacher
        t_data = t_df[t_df['Teacher'] == teacher]
        
        for day in days_order:
            # Construct a row object similar to the dataframe row
            row_data = {'Day': day}
            day_records = t_data[t_data['Day'] == day]
            
            for slot in slot_cols:
                # Find if teacher has class in this slot
                slot_record = day_records[day_records['Slot'] == slot]
                if not slot_record.empty:
                    row_data[slot] = slot_record.iloc[0]['Content']
                else:
                    row_data[slot] = "" # Free period
            
            new_row = table.add_row()
            merge_cells_logic(new_row, row_data)

        output_path = os.path.join(OUTPUT_DIR, f"Teacher_{teacher}.docx")
        doc.save(output_path)
        print(f"Saved: {output_path}")

# --- MAIN ---
if __name__ == "__main__":
    if os.path.exists(INPUT_FILE) and os.path.exists(TEMPLATE_FILE):
        df = pd.read_csv(INPUT_FILE)
        generate_classwise(df)
        generate_teacherwise(df)
        print("\nAll merged timetables generated!")
    else:
        print(f"Error: Ensure {INPUT_FILE} and {TEMPLATE_FILE} are present.")