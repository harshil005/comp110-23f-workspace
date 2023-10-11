"""Creating a Structured Wordle."""
__author__ = "730711765"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_string: str, search_char: str) -> bool:
    """Checks if a certain character is present anywhere in a certain string."""
    char_found = False
    assert len(search_char) == 1
    n = 0 
    while n < len(search_string) and char_found is False:
        if search_string[n] == search_char:
            return True
        n += 1
    return False


def emojified(guess_str: str, secret_str: str) -> str:
    """Returns an indication of how close the guess word is to the secret word with emoji indicators."""
    assert len(guess_str) == len(secret_str)
    this_char = 0
    guess_check = ""
    while this_char < len(secret_str):
        if guess_str[this_char] == secret_str[this_char]:
            guess_check += GREEN_BOX
        else:
            if contains_char(secret_str, guess_str[this_char]) is True:
                guess_check += YELLOW_BOX
            else:
                guess_check += WHITE_BOX
         
        this_char += 1
    return guess_check


def input_guess(exp_length: int) -> str:
    """Returns a guess of the correct number of characters."""
    guess = input(f"Enter a {exp_length} character word: ")
    while len(guess) != exp_length:
        guess = input(f"That wasn't {exp_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns_taken = 0
    secret_word = "codes"
    won = False

    while turns_taken < 6 and won is False:
        print(f"=== Turn {turns_taken+1}/6 ===")
        user_guess = input_guess(len(secret_word))
        turns_taken += 1
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {turns_taken}/6 turns!")
            won = True

    if won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()