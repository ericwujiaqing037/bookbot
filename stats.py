def get_book_text(file_path):
      with open(file_path) as f:
        file_contents = f.read()
        return file_contents
      

def get_book_words(book):
    num_words = len(book.split())
    return num_words


def count_characters(book):
    charDict = {}
    book_lower_case = book.lower()
    for c in book_lower_case: 
        if c not in charDict:
            charDict[c] = 0
        charDict[c] += 1
    
    return charDict