def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_counts = get_char_counts(text)
        sorted_list = chars_dict_to_sorted_list(char_counts)
        print_report(book_path, num_words, sorted_list)


def print_report(book_path, num_words, sorted_list):
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in this document")
        for cc in sorted_list:
            print(f"The ''{cc['letter']}'' character was found {cc['num']} times")
        print("--- End of report ---")


def chars_dict_to_sorted_list(char_counts):
    ccdict = []
    for c in char_counts:
        if c.isalpha():
            ccdict.append({"letter": c, "num": char_counts[c]})
    ccdict.sort(reverse=True, key=num_sort)
    return ccdict

def num_sort(dict):
     return dict["num"]

def get_book_text(path):
    with open(path)  as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts =  {}
    for c in text:
        lower = c.lower()
        if lower in char_counts:
            char_counts[lower] += 1
        else:
            char_counts[lower] = 1
    return char_counts

main()
