"""`list` Utility Functions."""
__author__ = "730711765"


def all(check_list: list[int], check_int: int) -> bool:
    """Checks if a list is made up of all of a certain integer."""
    count = 0
    if len(check_list) == 0:
        return False
    else:
        while count < len(check_list):
            if check_list[count] != check_int:
                return False
            count += 1
        return True


def max(input_list: list[int]) -> int:
    """Finds the maximum value of a given list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    loop_count = 1
    max: int = input_list[0]
    while loop_count < len(input_list):
        if input_list[loop_count] > max:
            max = input_list[loop_count]
        loop_count += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are exactly the same at every index."""
    if len(list1) != len(list2):
        return False
    
    check_count = 0 
    while check_count < len(list1):
        if list1[check_count] != list2[check_count]:
            return False
        check_count += 1
    return True

print(max([]))