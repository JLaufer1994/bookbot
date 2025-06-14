from stats import get_book_text, count_words, count_characters, char_frequency

def main():
    # Read the book text from file.
    text = get_book_text('books/frankenstein.txt')
    
    # Count the number of words.
    num_words = count_words(text)
    
    # Count the number of characters.
    num_characters = count_characters(text)
    
    # Get the frequency of each character.
    frequency = char_frequency(text)
    
    # Output all results.
    print(f"{num_words} words found in the document")
    print(f"{num_characters} characters found in the document")
    print("Character frequency:")
    for char, count in frequency.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()