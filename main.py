def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    frankenstein_path = "./books/frankenstein.txt"
    print(get_book_text(frankenstein_path))

main()