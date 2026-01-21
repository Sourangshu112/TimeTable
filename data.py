batches: dict = {
    #id: [course, yr, dept, room, interdept GROUP]
    1 : ["btech", 1, "ME", "A"],
    2 : ["btech", 1, "CEE", "A"],
    3 : ["btech", 1, "FET", "A"],
    4 : ["btech", 1, "EE", "A"],
    5 : ["btech", 1, "EE", "B"],
    6 : ["btech", 1, "CSE", "A"],
    7 : ["btech", 1, "CSE", "B"],

    8 : ["btech", 2, "ME", "A"],
    9 : ["btech", 2, "ME", "B"],
    10: ["btech", 2, "CEE", "A"],
    11: ["btech", 2, "CEE", "B"],
    12: ["btech", 2, "FET", "A"],
    13: ["btech", 2, "EE", "A"],
    14: ["btech", 2, "EE", "B"],
    15: ["btech", 2, "CSE", "A"],
    16: ["btech", 2, "CSE", "B"],

    17: ["btech", 3, "ME", "A"],
    18: ["btech", 3, "ME", "B"],
    19: ["btech", 3, "CEE", "A"],
    20: ["btech", 3, "CEE", "B"],
    21: ["btech", 3, "FET", "A"],
    22: ["btech", 3, "EE", "A"],
    23: ["btech", 3, "EE", "B"],
    24: ["btech", 3, "CSE", "A"],

    25: ["btech", 4, "ME", "A"],
    26: ["btech", 4, "FET", "A"],
    27: ["btech", 4, "EE", "A"],
    28: ["btech", 4, "EE", "B"],

    29: ["diploma", 1, "EE+ME+FPT", "A"],
    30: ["diploma", 1, "EE+ME+FPT" ,"B"],
    31: ["diploma", 1, "CST+CE", "A"],
    32: ["diploma", 1, "CST+CE", "B"],

    33: ["diploma", 2, "ME", "A"],
    34: ["diploma", 2, "CE", "A"],
    35: ["diploma", 2, "FET", "A"],
    36: ["diploma", 2, "EE", "A"],
    37: ["diploma", 2, "CST", "A"],

    38: ["diploma", 3, "ME", "A"],
    39: ["diploma", 3, "CE", "A"],
    40: ["diploma", 3, "FET", "A"],
    41: ["diploma", 3, "EE", "A"],
    42: ["diploma", 3, "CST", "A"],
}


rooms: list = ['C39', 'A39', 'D39', 'B203', 'C25', 'D25', 'A24', 'C38', 'B112', 'C26', 
         'D23', 'A12', 'C37', 'B110', 'D22', 'A13', 'D38', 'C24', 'B204', 'C22', 
         'D12', 'A35', 'D26', 'B202', 'C23', 'D24', 'A36', 'D37']


rooms_mapped: dict = {
    #room : [list of batches together in the room]
    'C39' : [1,2,3],
    'A39' : [4,5],
    'D39' : [6,7],
    'B203': [8,9],
    'C25' : [10,11],
    'D25' : [12],
    'A24' : [13,14],
    'C38' : [15,16],
    'B112': [17,18],
    'C26' : [19,20],
    'D23' : [21],
    'A12' : [22,23],
    'C37' : [24],
    'B110': [25],
    'D22' : [26],
    'A13' : [27,28],
    'D38' : [29,30],
    'C24' : [31,32],
    'B204': [33],
    'C22' : [34],
    'D12' : [35],
    'A35' : [36],
    'D26' : [37],
    'B202': [38],
    'C23' : [39],
    'D24' : [40],
    'A36' : [41],
    'D37' : [42],
}

teachers: dict = {
    #id : [name,dept]
    101 : ['AM','Abhijit Mandal','Chemistry'],
    102 : ['BKT','Bikarna Tarafdar','Mathmatics'],
    103 : ['SSC','Shib Sankar Chowdhury','Humanities'],
    104 : ['RD','Rakesh Das','Physics'],
    105 : ['CD','Chandita Das','Humanities'],
    106 : ['AK','Amiungshu Karmakar','Electrical'],
    107 : ['RRK','Raja Ram Kumar','Electrical'],
    108 : ['RK','Rajeev Kumar','Electrical'],
    109 : ['TkD','Tapas Kumar Das','Electrical'],
    110 : ['SA','Smita Anand','Electrical'],
    111 : ['AbK','Abhinav Kumar','Mechanical'],
    112 : ['HbM','Habib Masum','Mechanical'],
    113 : ['TrD','Tribid Ranjan Das','Mechanical'],
    114 : ['NM','Nitesh Mandal','Mechanical'],
    115 : ['RR','Raktim Roy','Mechanical'],
    116 : ['SKD','Sudip Kumar Das','Food'],
    117 : ['JA','Md. Jagar Ali','Food'],
    118 : ['SC','Sourav Chakraborty','Food'],
    119 : ['VK','Vivek Kumar','Food'],
    120 : ['SUD','Siraj Ud Doulah','Computer Science'],
    121 : ['IW','Imayanmosha Wahlang','Computer Science'],
    122 : ['TKO','Tryambak Kumar Ojha','Computer Science'],
    123 : ['SDM','Sukhen Das Mondal','Computer Science'],
    124 : ['DR','Debadrita Roy','Computer Science'],
    125 : ['PY','Poojari Yogendar','Civil'],
    126 : ['SB','Soumi Bhattacharyya','Civil'],
    127 : ['HR','Habibur Rahaman','Civil'],
    128 : ['HS','Haradhan Sarkar','Civil'],
    129 : ['KY','Kiran Yarakula','Civil'],
    130 : ['SM','Sankar Mukherjee','Electrical'],
    131 : ['PM','Pranab Mandal','Electrical'],
    132 : ['AR','Amarjit Roy','Electrical'],
    133 : ['AnP','Anisha Paul','Mechanical'],
    134 : ['ABD','Amit Baran Das','Food'],
    135 : ['MAM','Musadir Ahamad Malik','Food'],
    136 : ['SR','Subrata Roy','Computer Science'],
    137 : ['BPT','Babul Prasad Tewari','Computer Science'],
    138 : ['KP','Kaushik Paul','Civil'],
    139 : ['RKN','Raj Kumar Nayak','Mathematics'],
    140 : ['SSD','Suranjan Sikdar','Chemistry'],
    141 : ['HbR','Hasibur Raheman','Mechanics'],
    142 : ['GH','Goutam Haldar','Mathamatics'],
    143 : ['SkD','Santosh Kumar Dash','Mechanical'],
    144 : ['AP','Apsari Pravin','Physics'],
    145 : ['CS','Chiranjit Saini','Electrical'],
    146 : ['TnS','Tonmoy Sarkar','Mechanical'],
    147 : ['GG','Goutam Ghorai','Electrical'],
    148 : ['Guest','Guest','Biology'],
    149 : ['AS','Anirban Saha','Humanities'],
    150 : ['PS','Priyanka Saha','Humanities'],
    151 : ['DD','Dharmesher Dash','Mechanical'],
    152 : ['DG','Debasish Ghorui','Mathametics'],
    153 : ['SN','Soutick Nandi','Chemistry'],
    154 : ['SnC','Sandip Chandra','Electrical'],
    156 : ['MJK','Mohan Jagadesh Kumar', 'Mechanical'],
    157 : ['KKD','Kishod Kumar Dash','Food'],
    158 : ['DS','Dalbir Singh','Mechanical'],
    159 : ['SrC','Surajit Chottopadhai','Electrical'],
    160 : ['AnS','Anwesha Sarkar','Food'],
    161 : ['SuB', 'Soumik Bhoumik','Computer Science'],
    162 : ['SS','Shuvra Saha','Civil']
}

theory: dict = {
    1   : ['D38', 'Applied Chemistry', 3, 101],
    2   : ['D38', 'Mathematics-I', 3, 102],
    3   : ['D38', 'Communication Skill in English', 2, 103],
    4   : ['D38', 'Applied Physics', 3, 104],
    5   : ['C24', 'Applied Chemistry', 3, 101],
    6   : ['C24', 'Mathematics-I', 3, 102],
    7   : ['C24', 'Communication Skill in English', 2, 103],
    8   : ['C24', 'Applied Physics', 3, 104],
    9   : ['A35', 'Introduction to Electric Generation System', 3, 106],
    10  : ['A35', 'DC Machines and Transformers', 3, 107],
    11  : ['A35', 'Electrical Circuits', 3, 108],
    12  : ['A35', 'Analog and Digital Electronics', 3, 109],
    13  : ['A35', 'Electrical and Electronics Measurment', 3, 110],
    14  : ['B204', 'Manufactoring Process 1', 3, 111],
    15  : ['B204', 'Mech Eng Drawing', 2, 112],
    16  : ['B204', 'Strength of Material', 3, 113],
    17  : ['B204', 'Thermal Engineering', 3, 114],
    18  : ['B204', 'Mech. Eng. Materials', 3, 115],
    19  : ['D12', 'Fundamental Chemistry', 2, 116],
    20  : ['D12', 'Technology in Food Preservation', 2, 117],
    21  : ['D12', 'Food Microbiology', 2, 117],
    22  : ['D12', 'Engg. Thermodynamics & Chem Kinetics', 2, 118],
    23  : ['D12', 'Unit Operation of Chemical Engineering - I', 3, 119],
    24  : ['D12', 'Chemistry of Food', 2, 116],
    25  : ['D26', 'Computer Programming', 2, 120],
    26  : ['D26', 'Scripting Languages', 2, 121],
    27  : ['D26', 'Data Structure', 3, 122],
    28  : ['D26', 'Computer System Organization', 4, 123],
    29  : ['D26', 'Algorithms', 3, 124],
    30  : ['C22', 'Transotation Engg.', 2, 125],
    31  : ['C22', 'Buliding Construction', 2, 126],
    32  : ['C22', 'Basic Surveying', 3, 127],
    33  : ['C22', 'Mechanics of Material', 3, 126],
    34  : ['C22', 'CE Planning and Drawing', 1, 128],
    35  : ['C22', 'Construction of Materials', 2, 129],
    36  : ['C22', 'Concrete Technology', 2, 128],
    37  : ['A36', 'Industrial Automation & Control ', 3, 110],
    38  : ['A36', 'Building Electrification', 3, 131],
    39  : ['A36', 'Microcontroller and its Application', 3, 132],
    40  : ['A36', 'Solar Power Technologies', 3, 106],
    41  : ['B202', 'Fluid Mechanis and Machinery', 3, 130],
    42  : ['B202', 'Advance Manufactoring Process', 3, 111],
    43  : ['B202', 'Power Engineering', 3, 130],
    44  : ['B202', 'Elective-Automobile Engineering', 2, 113],
    45  : ['B202', 'Elective-Material Handling System', 2, 133],
    46  : ['D24', 'Dairy Technology', 3, 118],
    47  : ['D24', 'Food Biotechnology', 2, 117],
    48  : ['D24', 'Technology of Food IV', 2, 134],
    49  : ['D24', 'Bakery Technology', 3, 117],
    50  : ['D24', 'Food Engineering', 2, 119],
    51  : ['D24', 'Food Safety and Quality Management', 2, 135],
    52  : ['D37', 'Microcontroller and Microprocessor', 3, 136],
    53  : ['D37', 'IOT', 4, 137],
    54  : ['D37', 'Advanced Computer Network', 4, 124],
    55  : ['D37', 'Theory of Automata', 4, 123],
    56  : ['D37', 'Computer Ghraphics', 4, 122],
    57  : ['C23', 'Water Resource Engg.', 2, 129],
    58  : ['C23', 'Traffic Engg Elective', 3, 128],
    59  : ['C23', 'Building Maintenance', 3, 125],
    60  : ['C23', 'Estimate costing and Valuation', 3, 138],
    61  : ['C23', 'Safety Engg and Management in Construction Sector', 2, 129],
    62  : ['A39','Basic Electrical Engineering',4,109],
    63  : ['A39','Mathematics IB',4,139],
    64  : ['A39','Chemistry I',4,140],
    65  : ['A39','Engineering Grapics',1,141],
    66  : ['D39','Mathematics IA',4,142],
    67  : ['D39','Applied Physics I',4,104],
    68  : ['D39','Basic Electrical Engineering',4,109],
    69  : ['D39','Workshop',1,143],
    70  : ['C39','Mathematics IA',4,139],
    71  : ['C39','Applied Physics I',4,144],
    72  : ['C39','Basic Electrical Engineering',4,145],
    73  : ['C39','Workshop',1,133],
    74  : ['A24','Electric Circuit Theory',3,108],
    75  : ['A24','Engineering Mechanics',3,146],
    76  : ['A24','Mathematics-III',3,102],
    77  : ['A24','Electromagnetic Field Theory',3,147],
    78  : ['A24','Analog Electronics',3,132],
    79  : ['A24','Biology for Engineers',3,148],
    80  : ['A24','Indian Contitution',3,149],
    81  : ['C38','Analog & Digital Electronics',3,159],
    82  : ['C38','DSA',3,121],
    83  : ['C38','Computer Organisation',3,136],
    84  : ['C38','Linear Algebra',2,142],
    85  : ['C38','Economics',3,150],
    86  : ['B203','Biology ',3,148],
    87  : ['B203','Manufacturing Process',4,151],
    88  : ['B203','Matematics-III',4,152],
    89  : ['B203','Thermodynamics',4,143],
    90  : ['B203','Basic Electronics Engineering',3,159],
    91  : ['B203','Engineering Mechanics',4,112],
    92  : ['D25','Chemistry II',3,101],
    93  : ['D25','Chemistry for Food',4,135],
    94  : ['D25','Food Microbiology',4,160],
    95  : ['D25','Unit Operation I',4,119],
    96  : ['D25','Engineering Thermodynamics',3,116],
    97  : ['D25','Biology for Engineers',3,148],
    98  : ['D25','Chemistry for Food Lab ',3,135],
    99  : ['C25','Values & Ethics in Profession',3,149],
    100 : ['C25','Chemistry II',5,153],
    101 : ['C25','Basic Env Engg and Ele Bio',3,138],
    102 : ['C25','Thermodynamics & kinetics',2,118],
    103 : ['C25','Surveying',3,125],
    104 : ['C25','Building Material & Construction',5,128],
    105 : ['A12','Power Electronics',3,154],
    106 : ['A12','Control System',3,107],
    107 : ['A12','Electrical Machine II',3,147],
    108 : ['A12','DSA',3,161],
    109 : ['A12','Power System I',3,159],
    110 : ['A12','Renewable & NC Energy',3,110],
    111 : ['C37','Probability & Statistics',3,152],
    112 : ['C37','Operating System',3,123],
    113 : ['C37','Object Oriented Programming',3,120],
    114 : ['C37','Intro to Machine Learning',3,121],
    115 : ['C37','Intro to industrial management',3,146],
    116 : ['B112','Heat Transfer',4,156],
    117 : ['B112','Effe. Technical Communication',3,105],
    118 : ['B112','Solid Mechanics',4,156],
    119 : ['B112','Kinematics & TOM',4,141],
    120 : ['B112','Essence of Indian Knowledge Tradition',2,149],
    121 : ['D23','Food Processing Technology I',4,135],
    122 : ['D23','Food Processing Technology II',3,116],
    123 : ['D23','Renewable Energy',3,134],
    124 : ['D23','Fermentation Technology',3,160],
    125 : ['D23','Food Process Engineering',3,157],
    126 : ['D23','Constitution',3,149],
    127 : ['D23','Economics',2,150],
    128 : ['C26','Economics',1,150],
    129 : ['C26','Unit Operation II',3,118],
    130 : ['C26','Design of RC Structures A',3,126],
    131 : ['C26','Design of RC Structures B',3,162],
    132 : ['C26','Engineering geology-A',3,126],
    133 : ['C26','Engineering geology-B',3,127],
    134 : ['C26','Concrete Technology A',3,162],
    135 : ['C26','Concrete Technology B',3,127],
    136 : ['A13','Artificial Intelligence',3,161],
    137 : ['A13','Power Generation Economics',3,154],
    138 : ['A13','Electric Drive',3,145],
    139 : ['A13','Principles of Management',3,150],
    140 : ['A13','Digital Image Processing',3,132],
    141 : ['D22','Entrepreuneurship for Food Tech',3,160],
    142 : ['D22','Nanoscience in Food Science',3,157],
    143 : ['D22','Modelling and Sim. of Food Process',3,118],
    144 : ['D22','Project Engg & Food Plant Layout',3,134],
    145 : ['D22','Food Saftey & Quality Management',3,119],
    146 : ['D22','Food Packaging Technology',3,118],
    147 : ['B110','Non-Conventional Energy',3,143],
    148 : ['B110','Industrial Engineering',3,133],
    149 : ['B110','Advanced Weilding technolog',3,146],
    150 : ['B110','Mechanical Vibration',3,158],
    151 : ['B110','Advance Manufacturing Technology',3,151],
    152 : ['B110','Automobile Engineering',3,114],
    153 : ['B110','CAD-CAM',3,112],
    154 : ['B110','Economics',3,150],
}


# ['B.Tech', '1st', 'EE', 'Basic Electrical Engineering', '4', 'Theory', 'TkD', '', '', '']
# ['B.Tech', '1st', 'EE', 'Mathematics IB', '4', 'Theory', 'RKN', '', '', '']
# ['B.Tech', '1st', 'EE', 'Chemistry I', '1', 'Theory', 'SSD', '', '', '']
# ['B.Tech', '1st', 'EE', 'Engineering Grapics', '4', 'Theory', 'HbR', '', '', '']
# ['B.Tech', '1st', 'CSE(AI/ML)', 'Mathematics IA', '4', 'Theory', 'GH', '', '', '']
# ['B.Tech', '1st', 'CSE(AI/ML)', 'Applied Physics I', '4', 'Theory', 'RD', '', '', '']
# ['B.Tech', '1st', 'CSE(AI/ML)', 'Basic Electrical Engineering', '4', 'Theory', 'TkD', '', '', '']
# ['B.Tech', '1st', 'CSE(AI/ML)', 'Workshop', '1', 'Theory', 'SkD', '', '', '']
# ['B.Tech', '1st', 'ME', 'Mathematics IA', '4', 'Theory', 'RKN', '', '', '']
# ['B.Tech', '1st', 'ME', 'Applied Physics I', '4', 'Theory', 'AP', '', '', '']
# ['B.Tech', '1st', 'ME', 'Basic Electrical Engineering', '4', 'Theory', 'CS', '', '', '']
# ['B.Tech', '1st', 'ME', 'Workshop', '1', 'Theory', 'AnP', '', '', '']
# ['B.Tech', '1st', 'FET', 'Mathematics IA', '4', 'Theory', 'RKN', '', '', '']
# ['B.Tech', '1st', 'FET', 'Applied Physics I', '4', 'Theory', 'AP', '', '', '']
# ['B.Tech', '1st', 'FET', 'Basic Electrical Engineering', '4', 'Theory', 'CS', '', '', '']
# ['B.Tech', '1st', 'FET', 'Workshop', '1', 'Theory', 'AnP', '', '', '']
# ['B.Tech', '1st', 'C&EE', 'Mathematics IA', '4', 'Theory', 'RKN', '', '', '']
# ['B.Tech', '1st', 'C&EE', 'Applied Physics I', '4', 'Theory', 'AP', '', '', '']
# ['B.Tech', '1st', 'C&EE', 'Basic Electrical Engineering', '4', 'Theory', 'CS', '', '', '']
# ['B.Tech', '1st', 'C&EE', 'Workshop', '1', 'Theory', 'AnP', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Electric Circuit Theory', '3', 'Theory', 'RK', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Engineering Mechanics', '3', 'Theory', 'TnS', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Mathematics-III', '3', 'Theory', 'BKT', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Electromagnetic Field Theory', '3', 'Theory', 'GG', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Analog Electronics', '3', 'Theory', 'AR', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Biology for Engineers', '3', 'Theory', 'Guest', '', '', '']
# ['B.Tech', '2nd', 'EE', 'Indian Contitution', '3', 'Theory', 'AS', '', '', '']
# ['B.Tech', '2nd', 'CSE(AI/ML)', 'Analog & Digital Electronics', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '2nd', 'CSE(AI/ML)', 'DSA', '3', 'Theory', 'IW', '', '', '']
# ['B.Tech', '2nd', 'CSE(AI/ML)', 'Computer Organisation', '3', 'Theory', 'SR', '', '', '']
# ['B.Tech', '2nd', 'CSE(AI/ML)', 'Linear Algebra', '2', 'Theory', 'GH', '', '', '']
# ['B.Tech', '2nd', 'CSE(AI/ML)', 'Economics', '3', 'Theory', 'PS', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Biology ', '3', 'Theory', 'Guest', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Manufacturing Process', '4', 'Theory', 'DD', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Matematics-III', '4', 'Theory', 'DG', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Thermodynamics', '4', 'Theory', 'SKD', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Basic Electronics Engineering', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '2nd', 'ME', 'Engineering Mechanics', '4', 'Theory', 'HM', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Chemistry II', '3', 'Theory', 'AM', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Chemistry for Food', '4', 'Theory', 'MAM', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Food Microbiology', '4', 'Theory', 'AS', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Unit Operation I', '4', 'Theory', 'VK', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Engineering Thermodynamics', '3', 'Theory', 'SKD', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Biology for Engineers', '3', 'Theory', 'Guest', '', '', '']
# ['B.Tech', '2nd', 'FET', 'Chemistry for Food Lab ', '3', 'Theory', 'MAM', 'N/A', '', '']
# ['B.Tech', '2nd', 'C&EE', 'Values & Ethics in Profession', '3', 'Theory', 'AS', '', '', '']
# ['B.Tech', '2nd', 'C&EE', 'Chemistry II', '5', 'Theory', 'KP', '', '', '']
# ['B.Tech', '2nd', 'C&EE', 'En.&Biology', '3', 'Theory', 'SS', '', '', '']
# ['B.Tech', '2nd', 'C&EE', 'Thermodynamics & kinetics', '2', 'Theory', 'HS', '', '', '']
# ['B.Tech', '2nd', 'C&EE', 'Surveying', '3', 'Theory', 'PY', '', '', '']
# ['B.Tech', '2nd', 'C&EE', 'Building Material & Construction', '5', 'Theory', 'HS', '', '', '']
# ['B.Tech', '3rd', 'EE', 'Power Electronics', '3', 'Theory', 'SnC', '', '', '']
# ['B.Tech', '3rd', 'EE', 'Control System', '3', 'Theory', 'RRK', '', '', '']
# ['B.Tech', '3rd', 'EE', 'Electrical Machine II', '3', 'Theory', 'GG', '', '', '']
# ['B.Tech', '3rd', 'EE', 'DSA', '3', 'Theory', 'SB', '', '', '']
# ['B.Tech', '3rd', 'EE', 'Power System I', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '3rd', 'EE', 'Renewable & Non-conventional Energy', '3', 'Theory', 'SA', '', '', '']
# ['B.Tech', '3rd', 'CSE(AI/ML)', 'Probability & Statistics', '3', 'Theory', 'DG', '', '', '']
# ['B.Tech', '3rd', 'CSE(AI/ML)', 'Operating System', '3', 'Theory', 'SDM', '', '', '']
# ['B.Tech', '3rd', 'CSE(AI/ML)', 'Object Oriented Programming', '3', 'Theory', 'SUD', '', '', '']
# ['B.Tech', '3rd', 'CSE(AI/ML)', 'Intro to Machine Learning', '3', 'Theory', 'IW', '', '', '']
# ['B.Tech', '3rd', 'CSE(AI/ML)', 'Intro to industrial management', '3', 'Theory', 'TS', '', '', '']
# ['B.Tech', '3rd', 'ME', 'Heat Transfer', '4', 'Theory', 'MJK', '', '', '']
# ['B.Tech', '3rd', 'ME', 'Effective Technical Communication', '3', 'Theory', 'CD', '', '', '']
# ['B.Tech', '3rd', 'ME', 'Solid Mechanics', '4', 'Theory', 'MJK', '', '', '']
# ['B.Tech', '3rd', 'ME', 'Kinematics & TOM', '4', 'Theory', 'HbR', '', '', '']
# ['B.Tech', '3rd', 'ME', 'Essence of Indian Knowledge Tradition', '2', 'Theory', 'AS', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Food Processing Technology I', '4', 'Theory', 'MAM', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Food Processing Technology II', '3', 'Theory', 'SKD', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Renewable Energy', '3', 'Theory', 'ABD', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Fermentation Technology', '3', 'Theory', 'AS', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Food Process Engineering', '3', 'Theory', 'KKD', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Constitution', '3', 'Theory', 'AS', '', '', '']
# ['B.Tech', '3rd', 'FET', 'Economics', '2', 'Theory', 'PS', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Economics', '1', 'Theory', 'PS', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Unit Operation II', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Design of RC Structures A', '3', 'Theory', 'SB', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Design of RC Structures B', '3', 'Theory', 'SS', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Engineering geology-A', '3', 'Theory', 'SB', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Engineering geology-B', '3', 'Theory', 'HbR', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Concrete Technology A', '3', 'Theory', 'SS', '', '', '']
# ['B.Tech', '3rd', 'C&EE', 'Concrete Technology B', '3', 'Theory', 'HbR', '', '', '']
# ['B.Tech', '4th', 'EE', 'Artificial Intelligence', '3', 'Theory', 'SB', '', '', '']
# ['B.Tech', '4th', 'EE', 'Power Generation Economics', '3', 'Theory', 'SnC', '', '', '']
# ['B.Tech', '4th', 'EE', 'Electric Drive', '3', 'Theory', 'CS', '', '', '']
# ['B.Tech', '4th', 'EE', 'Principles of Management', '3', 'Theory', 'PS', '', '', '']
# ['B.Tech', '4th', 'EE', 'Digital Image Processing', '3', 'Theory', 'AR', '', '', '']
# ['B.Tech', '4th', 'FET', 'Entrepreuneurship for Food Tech', '3', 'Theory', 'AS', '', '', '']
# ['B.Tech', '4th', 'FET', 'Nanoscience in Food Science', '3', 'Theory', 'KKD', '', '', '']
# ['B.Tech', '4th', 'FET', 'Modelling and Simulation of Food Process', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '4th', 'FET', 'Project Engineering & Food Plant Layout', '3', 'Theory', 'ABD', '', '', '']
# ['B.Tech', '4th', 'FET', 'Food Saftey & Quality Management', '3', 'Theory', 'VK', '', '', '']
# ['B.Tech', '4th', 'FET', 'Food Packaging Technology', '3', 'Theory', 'SC', '', '', '']
# ['B.Tech', '4th', 'ME', 'Non-Conventional Energy', '3', 'Theory', 'SKD', '', '', '']
# ['B.Tech', '4th', 'ME', 'Industrial Engineering', '3', 'Theory', 'AnP', '', '', '']
# ['B.Tech', '4th', 'ME', 'Advanced Weilding technolog', '3', 'Theory', 'TS', '', '', '']
# ['B.Tech', '4th', 'ME', 'Mechanical Vibration', '3', 'Theory', 'DS', '', '', '']
# ['B.Tech', '4th', 'ME', 'Advance Manufacturing Technology', '3', 'Theory', 'DD', '', '', '']
# ['B.Tech', '4th', 'ME', 'Automobile Engineering', '3', 'Theory', 'NM', '', '', '']
# ['B.Tech', '4th', 'ME', 'CAD-CAM', '3', 'Theory', 'HM', '', '', '']
# ['B.Tech', '4th', 'ME', 'Economics', '3', 'Theory', 'PS', '', '', '']





labs: dict = {
    101 : "Ghraphics Labs",
    102 : "Workshop",
    103 : "Chemistry Lab",
    104 : "Physics Labs",
    105 : "English Labs",
    106 : ""
}



practical: dict = {
    #id: [batch,labroom,subject,[hr_needed_continuous],[teachers]]
    1 : ['Engineering Ghraphics', 3],
    2 : ['Engineering Workshop Practics', 3],
    3 : ['Applied Chemistry Lab', 2],
    4 : ['Applied Physics Lab', 2],
    5 : ['Communication Skill in English Lab', 2],
    6 : ['Engineering Ghraphics', 3],
    7 : ['Engineering Workshop Practics', 3],
    8 : ['Applied Chemistry Lab', 2],
    9 : ['Applied Physics Lab', 2],
    10: ['Communication Skill in English Lab', 2],
    11: ['Introduction to Electric Generation System Labs', 2],
    12: ['DC Machines and Transformers Labs', 2],
    13: ['Elecrical Cicuits Labs', 2],
    14: ['Analog and Digital Electronics Labs', 2],
    15: ['Electircal and Electronics Measurment Labs', 2],
    16: ['Manufactoring Process 1 Practice Lab', [2,2]],
    17: ['Thermal Engineering Lab', 2],
    18: ['Mech. Eng. Drawing Practice', [2,2]],
    19: ['Material Testing Lab', 2],
    20: ['Food Preservation Lab', [2,2]],
    21: ['Chemistry of Food Lab', [2,2]],
    22: ['Food Microbiology lab', 3],
    23: ['Unit Operation of Chemical Engineering - I Lab', 2],
    24: ['Computer Programming Lab', [2,2]],
    25: ['Scripting Languages Lab', [2,2]],
    26: ['Data Structure Lab', 2],
    27: ['CE Planning and Drawing Lab', [2,2]],
    28: ['Transotation Engg. Lab', 2],
    29: ['Construction of Materials lLab', 2],
    30: ['Mechanics of Material Lab', 2],
    31: ['Concrete Technology Lab', 2],
    32: ['Solar Power Technologies Lab', 2],
    33: ['Building Electrification Lab', 2],
    34: ['Mircrocontroller and its Application Lab', 2],
    35: ['Industrial Automation and Control Lab', 2],
    36: ['Power Engineering Lab', 2],
    37: ['Fluid Mechanis Lab', 2],
    38: ['Advance Manufactoring Process Lab', 2],
    39: ['Automobile Engineering Lab', 2],
    40: ['Dairy Technology Lab', '2,2'],
    41: ['Bakery and Confect Tech Lab', '2,2'],
    42: ['Food Analylis & QC Lab', 3],
    43: ['Microprocessor and Microcontroller Lab using simulator', 2],
    44: ['Estimate costing and Valuation Practices', 2],
    45: ['Water Resource Engg. Lab', 2],
    46: ['Design of RCC and Steel Structure Practices', 2],
}