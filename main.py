def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

main()