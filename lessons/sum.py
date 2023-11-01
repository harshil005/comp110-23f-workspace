"""Summing the elements of a list using different loops."""
__author__ = "730711765"


def w_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of the elements."""
    sum: float = 0.0
    counter: int = 0
    while counter < len(vals):
        sum += vals[counter]
        counter += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of the elements."""
    sum: float = 0.0
    for element in vals:
        sum += element
    
    return sum 


def f_range_sum(vals: list[float]) -> float:
    """Takes a list of floats and returns the sum of the elements."""
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum