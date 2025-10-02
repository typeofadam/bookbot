from stats import get_word_count, get_char_counts, get_char_sorted_dict_list

def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    num_words = get_word_count(frankenstein_text)
    char_counts = get_char_counts(frankenstein_text)
    char_dict_list = get_char_sorted_dict_list(char_counts)
    
    print(char_counts, char_dict_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in char_dict_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")


main()