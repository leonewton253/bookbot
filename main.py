with open("books/frankenstein.txt") as f:
    file_contents = f.read()

print("""
======================================================================================
                                    BOOK REPORT
======================================================================================
                                frankenstein.txt
======================================================================================
""")

def word_count(file_contents):
    book = file_contents.split()
    count = 0
    for text in book:
        count+=1
    print(f"There are {count} words in the book")

word_count(file_contents)
print("--------------------------------------------------------------------------------")

def count_letters(file_contents):
    letter_count = {}
    file_lower = file_contents.lower()
    for char in file_lower:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{letter}' character appears {count} times")

count_letters(file_contents)
