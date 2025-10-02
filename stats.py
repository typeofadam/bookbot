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

def sort_on(items):
    return items["num"]

def get_char_sorted_dict_list(char_dict):
    char_dict_list = []
    for key, value in char_dict.items():
        char_dict_list.append({"char": key, "num": value})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list