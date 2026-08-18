import sys

from stats import (
    chars_dict_to_sorted_list,
    get_book_text,
    get_character_counts,
    get_word_count,
)


def print_report(book_path: str, word_count: int, sorted_char_counts: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_char_counts:
        if pair[0].isalpha():
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    word_count = get_word_count(file_contents)
    character_counts = get_character_counts(file_contents)
    sorted_chars_counts = chars_dict_to_sorted_list(character_counts)
    print_report(book_path, word_count, sorted_chars_counts)

main()
