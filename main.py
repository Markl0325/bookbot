def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_list = get_everything(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(char_dict):
    return char_dict["num"]
    

def get_everything(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    return char_list

        



main()

