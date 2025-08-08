from stats import (char_frequency, count_characters, count_words,
                   get_book_text, sorted_char_frequency)


def main():
    # Read the book text from file.
    text = get_book_text('books/frankenstein.txt')
    
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
    print("Analyzing book found at books/frankenstein.txt...")
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