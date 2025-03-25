def get_word_count(file_text):
    return len(file_text.split())

def get_number_of_characters(file_text):
    character_dict = {}
    file_text = file_text.lower()

    for char in file_text:
        character_dict[char] = character_dict.get(char, 0) + 1
    
    return character_dict

def get_sorted_characters(character_dict):
    return sorted(character_dict.items(), key=lambda item: item[1], reverse=True)