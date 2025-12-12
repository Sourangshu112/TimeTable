batches: dict = {
    #id: [course, yr, dept, room,[interdept split]]

    1 : ["btech", 1, "ME", "C39", ["A"]],
    2 : ["btech", 1, "CEE", "C39", ["A"]],
    3 : ["btech", 1, "FET", "C39", ["A"]],
    4 : ["btech", 1, "EE", "A39", ["A","B"]],
    5 : ["btech", 1, "CSE", "D39", ["A","B"]],

    6 : ["btech", 2, "ME", "B203", ["A","B"]],
    7 : ["btech", 2, "CEE", "C25", ["A","B"]],
    8 : ["btech", 2, "FET", "D25", ["A"]],
    9 : ["btech", 2, "EE", "A24", ["A","B"]],
    10: ["btech", 2, "CSE", "C38", ["A","B"]],

    11: ["btech", 3, "ME", "B112", ["A","B"]],
    12: ["btech", 3, "CEE", "C26", ["A","B"]],
    13: ["btech", 3, "FET", "D23", ["A"]],
    14: ["btech", 3, "EE", "A12", ["A","B"]],
    15: ["btech", 3, "CSE", "C37", ["A"]],

    16: ["btech", 4, "ME", "B110", ["A"]],
    17: ["btech", 4, "FET", "D22", ["A"]],
    18: ["btech", 4, "EE", "A13", ["A","B"]],

    19: ["diploma", 1, "EE+ME+FPT", "D38", ["A","B"]],
    20: ["diploma", 1, "CST+CE", "C24", ["A","B"]],

    21: ["diploma", 2, "ME", "B204", ["A"]],
    22: ["diploma", 2, "CE", "C22", ["A"]],
    23: ["diploma", 2, "FET", "D12", ["A"]],
    24: ["diploma", 2, "EE", "A35", ["A"]],
    25: ["diploma", 2, "CST", "D26", ["A"]],

    26: ["diploma", 3, "ME", "B202", ["A"]],
    27: ["diploma", 3, "CE", "C23", ["A"]],
    28: ["diploma", 3, "FET", "D24", ["A"]],
    29: ["diploma", 3, "EE", "A36", ["A"]],
    30: ["diploma", 3, "CST", "D37", ["A"]],
}

batches2: dict = {
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
    10 : ["btech", 2, "CEE", "A"],
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

    38: ["diploma", 3, "CE", "A"],
    39: ["diploma", 3, "ME", "A"],
    40: ["diploma", 3, "FET", "A"],
    41: ["diploma", 3, "EE", "A"],
    42: ["diploma", 3, "CST", "A"],
}


rooms: list = ['C39', 'A39', 'D39', 'B203', 'C25', 'D25', 'A24', 'C38', 'B112', 'C26', 
         'D23', 'A12', 'C37', 'B110', 'D22', 'A13', 'D38', 'C24', 'B204', 'C22', 
         'D12', 'A35', 'D26', 'B202', 'C23', 'D24', 'A36', 'D37']


rooms_mapped: dict = {
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

theory: dict = {
    #id: [batch,subject,hr/week,teacherid]
    1: ['D38',"Applied Chemistry",3,id]
    2: ['D38',],
    3: ['D38',],
    4: ['D38',],
}

practical: dict = {

}