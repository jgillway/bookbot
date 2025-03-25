import sys
from stats import get_word_count, get_number_of_characters, get_sorted_characters

def get_file_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def print_report(file_location, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} words")
    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if (char.isalpha()):
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_location = sys.argv[1]
    file_text = get_file_text(file_location)
    num_words = get_word_count(file_text)
    char_dict = get_number_of_characters(file_text)
    sorted_char_list = get_sorted_characters(char_dict)

    print_report(file_location, num_words, sorted_char_list)

main()
