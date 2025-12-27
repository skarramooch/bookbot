from stats import get_book_text, counter

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = counter(text)
    print(f"Found {num_words} total words")

main()
