
from file_methods import reading, validate_arguments

def sort_on(dict):
    return dict[1]

def stats():
    args = validate_arguments()
    file_content = reading(args[1])
    words = file_content.split()
    num_words = len(words)
    character_dict = {} 

    lowered_content= ""
    for char in file_content:
        lowered_content += char.lower()
    
    for char in lowered_content:
        if not char.isspace():           
            if char in character_dict:
                character_dict[char] += 1 
            else:
                character_dict[char] = 1

    dict_to_sort = list(character_dict.items())
    dict_to_sort.sort(reverse=True, key=sort_on) 
    head_output = f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
    '''
    character_output = f""""""

    for i in dict_to_sort:
        i[0].split()
        if i[0] != "": 
            character = i[0]
            value = i[1]
            character_output += "\n" + f"{character}" + ": " + f"{value}" + "\n"




    end_output = """============= END ==============="""
    formatted_output = head_output + "\n" + character_output + "\n" + end_output + "\n"

    return print(formatted_output) 


