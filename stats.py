def word_count(full_text):
    return len(full_text.split())

def char_count(full_text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict = {}
    
    for char in alphabet: 
        count = full_text.count(char)
        dict[char] = count
        
    return dict

def sort_on(items):
    return items["num"]
    
def sorted_list(char_dict):
    list = []
    for char in char_dict:
        dict = {}
        
        dict["num"] = char_dict[char]
        dict["char"] = char
        
        list.append(dict)
        
    list.sort(reverse=True, key=sort_on)
    
    return list


