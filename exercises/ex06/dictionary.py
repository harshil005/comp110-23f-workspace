"""Creating a variety of dictionary functions."""
__author__ = "730711765"


def invert(inp_dict: dict[str, str]) -> dict[str, str]: 
    """Takes a dictionary and returns one with the keys and the values swapped."""
    newdict: dict[str, str] = {}
    for key in inp_dict:
        if inp_dict[key] in newdict:
            raise KeyError("dict cannot be inverted! try again with a set of unique values.")
        newdict[inp_dict[key]] = key
    
    return newdict


def favorite_color(dict_in: dict[str, str]) -> str:
    """Returns the color in a given dict which occurs the most frequently."""
    counter_dict: dict[str, int] = {}
    for elem in dict_in:
        if dict_in[elem] not in counter_dict:
            counter_dict[dict_in[elem]] = 1
        else:
            counter_dict[dict_in[elem]] += 1
    
    max_found: int = 0
    max_color: str = ""
    for key in counter_dict:
        if counter_dict[key] > max_found:
            max_found = counter_dict[key]
            max_color = key
    return max_color


def count(valuelist: list[str]) -> dict[str, int]:
    """Counts how many times each value occurs in a list and returns a list with the frequencies."""
    count_dict: dict[str, int] = {}
    for value in valuelist:
        if value not in count_dict:
            count_dict[value] = 1
        else:
            count_dict[value] += 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Counts how many words in a list start with each letter and returns a dict with their frequencies."""
    wordcount_dict: dict[str, list[str]] = {}
    for word in word_list:
        if word[0].lower() not in wordcount_dict:
            wordcount_dict[word[0].lower()] = [word]
            
        else:
            wordcount_dict[word[0].lower()].append(word)
    return wordcount_dict


def update_attendance(update_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Takes a dict and updates it a specified key by adding a given value to it."""
    if day not in update_dict:
        update_dict[day] = [student]
    else:
        if student not in update_dict[day]:
            update_dict[day].append(student)
    return (update_dict)