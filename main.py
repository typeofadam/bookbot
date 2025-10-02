from stats import get_word_count, get_char_counts

def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    frankenstein_path = "./books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    num_words = get_word_count(frankenstein_text)
    print(f"Found {num_words} total words")
    print(get_char_counts(frankenstein_text))

main()