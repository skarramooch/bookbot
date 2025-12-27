def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def counter(file_contents):
    words = 0
    for word in file_contents.split():
        words += 1
    return words
