def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def get_word_count(string_to_count):
    word_list = string_to_count.split()
    return len(word_list)

def main():
    frankenstein_path = "./books/frankenstein.txt"
    print(get_word_count(get_book_text(frankenstein_path)))

main()