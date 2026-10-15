def sort_on(count: tuple[str, int]) -> int:
   return count[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    count_characters =[]
    for char in char_counts:
       count_characters.append((char, char_counts[char]))
    sorted_count_characters = sorted(count_characters, key=sort_on, reverse=True)
    return  sorted_count_characters


def count(text):
    words = text.split()
    return len(words)
def count_characters(text):
    text = text.lower()
    counts = {}

    for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts
