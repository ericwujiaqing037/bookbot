from stats import get_book_text, get_book_words, count_characters

def main():
    file_path_to_book = "books/frankenstein.txt"
    book = get_book_text(file_path_to_book)
    num_words = get_book_words(book)
    charDict = count_characters(book)
    print(f"Found {num_words} total words")
    print(charDict)
    
if __name__ == "__main__":
    main()

