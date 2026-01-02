def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def counter(file_contents):
    words = 0
    for word in file_contents.split():
        words += 1
    return words

def charcount(file_contents):
    chars = {}
    for char in file_contents.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sorted_chars(characters):
    char_list = []
    for char in characters:
        if char.isalpha():
            num = int(characters[char])
            char_dict = {'char': char, 'num': num}
            char_list.append(char_dict)

    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list
