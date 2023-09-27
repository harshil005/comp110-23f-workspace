__author__ = "730711765"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word = "python"
tries = 0
this_char = 0
word_check = ""

guess = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")



while this_char < len(secret_word):
    if guess[this_char] == secret_word[this_char]:
        word_check += GREEN_BOX
    else:
        char_in_word = False
        char_count = 0
        while char_in_word != True and char_count != len(secret_word):
            if guess[this_char] == secret_word[char_count]:
                char_in_word = True
            else:
                char_count += 1
        
        if char_in_word == True:
            word_check += YELLOW_BOX
        else:
            word_check += WHITE_BOX
         
    this_char += 1

print(word_check)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
