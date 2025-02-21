

def get_num_words(text):
    words = text.split()
    return len(words)

def get_everything(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict
