def get_book_word_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    return word_count

def get_num_chars(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
    char_nums = dict()
    for c in file_contents:
        char_nums[c] = char_nums.setdefault(c, 0) + 1
    return char_nums

def sort_char_nums(num_chars):
    result = list()
    for d in num_chars:
        if d.isalpha():
            char_dict = {"char": d, "num": num_chars[d]}
            result.append(char_dict)
    result.sort(key=lambda d: d["num"], reverse=True)
    return result