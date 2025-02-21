import sys
from stats import *


def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_everything(text)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    sorted_char_list = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char_list:
        if char.isalpha():
            print(f"{char}: {count}")  
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()
