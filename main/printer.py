import util as u

top_list:list = ["Title", "ToDo", "Info", "Due" , "Status"  ]
max_size:list = [25     , 20    , 20    , 24    , 12        ]

def print_top():
    pass

def get_info_sizes(d:dict):
    longest_word:int = 0
    for lists in d:
        for i, element in enumerate(lists):
            lenght:int = u.count_string_length(max_size[i])
            if lenght > longest_word: #if current word is longer than last longest word
                longest_word = lenght
            #rausfinden in welchem block der liste (links nach rechts) man ich gerade bewegt

def print_gui(d:dict):
    print_top()
    