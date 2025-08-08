from stats import (char_frequency, count_characters, count_words,
                   get_book_text, sorted_char_frequency)
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book text from command line arguments.
    book_name = sys.argv[1]

    # Read the book text from file.
    text = get_book_text(book_name)
    
    # Count the number of words.
    num_words = count_words(text)
    
    # Count the number of characters.
    num_characters = count_characters(text)
    
    # Get the frequency of each character.
    frequency = char_frequency(text)

    # Sort the character frequency.
    sorted_frequency = sorted_char_frequency(text)
    
    # Output all results.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("-------- Character Count -------")
    for item in sorted_frequency:
          character = item['char']
          count = item['num']

          if character.isalpha():
               print(f"{character}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    main()