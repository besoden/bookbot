def get_book_word_count(file_path):
    #print("in get_book_word_count")
    with open(file_path) as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    return word_count

def get_num_chars(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
    char_nums = dict()
    for c in file_contents:
        #print(f"I'm here and my value is {c}")
        char_nums[c] = char_nums.setdefault(c, 0) + 1
    #print(char_nums)
    return char_nums
    