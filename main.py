from stats import get_word_count

def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    frankenstein_path = "./books/frankenstein.txt"
    num_words = get_word_count(get_book_text(frankenstein_path))
    print(f"Found {num_words} total words")

main()