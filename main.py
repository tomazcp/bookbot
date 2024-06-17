def main():
    book_path = "./books/frankenstein.txt"
    text = book_text(book_path)
    print(text)
    word_count = count_words(text)
    print(f"The book has {word_count} words.")
    
    char_count = char_repeat(text)
    print(char_count)
    report_res = report({"path": book_path, 
                         "word_count": word_count,
                         "sort_fn": sort_on,
                         "char_dict": char_count})
    print_report(report_res)

def book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_repeat(text):
    char_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count

def report(opts_dict):
    rows = []
    char_dict = opts_dict["char_dict"]
    for k in char_dict:
        if k.isalpha():
            row = {"char": k, "num": char_dict[k]}
            rows.append(row)

    rows.sort(reverse=True, key=opts_dict["sort_fn"])

    report = []
    report.append(f"--- Begin report of {opts_dict['path']} ---") 
    report.append(f"{opts_dict['word_count']} found in the document")
    report.append("\n")
    
    for r in rows:
        report.append(f"The '{r['char']}' was found {r['num']} times")
    
    report.append("--- End report ---")
    return report

def print_report(report):
    for line in report:
        print(line)

def sort_on(dict):
    return dict["num"]


main()