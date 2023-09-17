"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730711765"

search_word = input("Enter a 5-character word: ")

if len(search_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

search_char = input("Enter a single character: ")


print(f'Searching for {search_char} in {search_word}')
char_count = 0

if search_word[0] == search_char:
    print(search_char +" found at index 0")
    char_count +=1
if search_word[1] == search_char:
    print(search_char +" found at index 1")
    char_count +=1
if search_word[2] == search_char:
    print(search_char +" found at index 2")
    char_count +=1
if search_word[3] == search_char:
    print(search_char +" found at index 3")
    char_count +=1
if search_word[4] == search_char:
    print(search_char +" found at index 4")
    char_count +=1

if char_count == 0:
    print(f"No instances of {search_char} found in {search_word}")
else:
    if char_count == 1:
        print(f"1 instance of {search_char} found in {search_word}")   
    else:
        print(f'{char_count} instances of {search_char} found in {search_word}')