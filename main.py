from stats import (
    chars_dict_to_sorted_list,
    get_book_text,
    get_character_counts,
    get_word_count,
)


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(file_contents)
    print(f"Found {word_count} total words.")
    character_counts = get_character_counts(file_contents)
    sorted_chars_count = chars_dict_to_sorted_list(character_counts)
    print(sorted_chars_count)

main()
