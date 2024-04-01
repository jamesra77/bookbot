def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    char_count_pairs = dict_to_list_sorted(char_counts)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words were found in document")
    for pair in char_count_pairs:
        print(f"The '{pair["char"]}' character was found {pair["count"]} times")
    print("--- End report ---")



def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in char_counts:
            char_counts[lower_char] = 1
        else:
            char_counts[lower_char] += 1

    return char_counts

def dict_to_list_sorted(dct):
    lst = []
    for key in dct:
        if key.isalpha():
            pair = {"char": key, "count": dct[key]}
            lst.append(pair)

    lst.sort(reverse=True, key=sort_on)
    return lst

def sort_on(dct):
    return dct["count"]



main()
