def get_num_words(text):
    return len(text.split())

def get_characters_count(book_text):
    characters_count = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in characters_count:
            characters_count[lower_char] = 1
        else:
            characters_count[lower_char] += 1

    return characters_count

def sort_on_count(char_dict):
    return char_dict["count"]

def get_ordered_characters_count_list(characters_count):
    characters_count_list = []
    for k, v in characters_count.items():
        if k.isalpha():
            characters_count_list.append(dict(char=k, count=v))
    characters_count_list.sort(reverse=True, key=sort_on_count)
    return characters_count_list
