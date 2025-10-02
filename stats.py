def get_word_count(string_to_count):
    word_list = string_to_count.split()
    return len(word_list)

def get_char_counts(string_to_count):
    string_to_count = string_to_count.lower()
    char_counts = {}
    char_set = set(string_to_count)
    for char in char_set:
        char_counts[char] = string_to_count.count(char)
    return char_counts