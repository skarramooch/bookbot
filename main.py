import sys
from stats import get_book_text, counter, charcount, sorted_chars

def main():
    sys_arg_len = len(sys.argv)
    print(f"sys_arg_len: {sys_arg_len}")
    if sys_arg_len < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = counter(text)
    characters = charcount(text)
    items = sorted_chars(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {str(sys.argv[1])}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in items:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
