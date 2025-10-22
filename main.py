from stats import get_book_text, get_book_words, count_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path_to_book = sys.argv[1] 
    book = get_book_text(file_path_to_book)
    num_words = get_book_words(book)
    charDict = count_characters(book)
    sorted_word_counts = sorted(charDict.items(), key = lambda x: x[1], reverse= True)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(sorted_word_counts)
    for key, value in sorted_word_counts:
        if(key.isalpha()):
            print(f"{key}: {value}")

    
if __name__ == "__main__":
    main()

