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