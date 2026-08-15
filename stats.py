def get_book_text(file_path: str) -> str:
    with open(f"{file_path}") as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book_text: str) -> int:
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_character_counts(book_text: str) -> dict[str, int]:
    char_counts = {}
    lower_text = book_text.lower()
    for c in lower_text:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1
    return char_counts

def sort_on(char_and_count: tuple[str, int]) -> int:
    return char_and_count[1]

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    output = []
    for c, count in char_count.items():
        output.append((c, count))
    sorted_output = sorted(output, reverse=True, key=sort_on)
    return sorted_output
