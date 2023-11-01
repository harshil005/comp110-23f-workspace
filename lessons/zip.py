"""Combining two lists into a dictionary."""
__author__ = "730711765"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Combines two lists to create and return a dictionary."""
    list_index = 0
    list_to_dict: dict[str, int] = dict()
    if len(list_1) == len(list_2):
        while list_index < len(list_1):
            list_to_dict[list_1[list_index]] = list_2[list_index]
            list_index += 1
    else:
        return list_to_dict
    return list_to_dict