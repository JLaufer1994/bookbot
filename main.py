from stats import get_book_text

def get_book_word_number(path):
    book_text = get_book_text(path)
    return len(book_text.split())

def main():
    num_words = get_book_word_number('books/frankenstein.txt')
    print(str(num_words) + " words found in the document")

main()