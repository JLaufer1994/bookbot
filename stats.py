def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def char_frequency(text):
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq

def sorted_char_frequency(text):
    char = char_frequency(text)
    sorted_list_of_dicts = []
    for item in char.items():
        sorted_list_of_dicts.append({"char":item[0], "num":item[1]})
    sorted_list_of_dicts.sort(key=lambda x: x['num'], reverse=True)
    return sorted_list_of_dicts