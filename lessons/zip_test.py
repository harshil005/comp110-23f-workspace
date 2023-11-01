"""Testing the zip function from the zip.py code."""
__author__ = "730711765"

from lessons.zip import zip


def test_combine_empty_lists() -> None:
    """Testing zip for 2 empty lists."""
    assert zip([], []) == {}


def test_usecase1() -> None:
    """Testing zip for a use case."""
    list_a: list[str] = ["Monday", "Tuesday"]
    list_b: list[int] = [1, 2]
    assert zip(list_a, list_b) == {"Monday": 1, "Tuesday": 2}


def test_usecase2() -> None:
    """Testing zip for another use case."""
    list_1: list[str] = ["Monday", "Tuesday", "Wednesday"]
    list_2: list[int] = [1, 2, 3]
    assert zip(list_1, list_2) == {"Monday": 1, "Tuesday": 2, "Wednesday": 3}