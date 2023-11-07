"""Testing the functions defined in dictionary.py."""
from dictionary import invert, count, favorite_color, alphabetizer, update_attendance
import pytest
__author__ = "730711765"

def test__invert_duplicates() -> None:
    """Testing the invert function for a dictionary that has identical values for multiple keys."""
    with pytest.raises(KeyError):
        dict_a: dict[str, str] = {'a': 'b', 'c': 'b'}
        invert(dict_a)


def test__invert_usecase1() -> None:
    """Testing the invert function for a normal use case."""
    dict_a: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert(invert(dict_a)) == {'b': 'a', 'd': 'c'}


def test__invert_usecase2() -> None:
    """Testing the invert function for another normal use case."""
    dict_a: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert(invert(dict_a)) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test__count_emptylist() -> None:
    """Testing the count function for an empty list."""
    list_a: list[str] = []
    assert count(list_a) == {}


def test__count_usecase1() -> None:
    """Testing the count function for a normal use case."""
    list_a: list[str] = ['a']
    assert count(list_a) == {'a': 1}


def test__count_usecase2() -> None:
    """Testing the count function for another normal use case."""
    list_a: list[str] = ['a', 'b', 'a']
    assert count(list_a) == {'a': 2, 'b': 1}


def test__favoritecolor_emptylist() -> None:
    """Testing the favoritecolor function for an empty list."""
    colordict_a: dict[str, str] = {}
    assert favorite_color(colordict_a) == ""


def test__favoritecolor_usecase1() -> None:
    """Testing the favoritecolor function for a normal use case."""
    favcolordict_a: dict[str, str] = {'Harshil': 'blue', 'Jash': 'blue'}
    assert favorite_color(favcolordict_a) == "blue"


def test__favoritecolor_usecase2() -> None:
    """Testing the favoritecolor function for another normal use case."""
    favcolordict_b: dict[str, str] = {'Harshil': 'blue', 'Jash': 'yellow', 'Aras': 'yellow'}
    assert favorite_color(favcolordict_b) == "yellow"


def test__alphabetizer_emptylist() -> None:
    """Testing the alphabetizer function for an empty list."""
    inputlist: list[str] = []
    assert alphabetizer(inputlist) == {}


def test__alphabetizer_usecase1() -> None:
    """Testing the alphabetizer function for a normal use case."""
    inputlist: list[str] = ['apple', 'banana']
    assert alphabetizer(inputlist) == {'a': ['apple'], 'b': ['banana']}


def test__alphabetizer_usecase1() -> None:
    """Testing the alphabetizer function for another normal use case."""
    inputlist: list[str] = ['apple', 'banana', 'Agave']
    assert alphabetizer(inputlist) == {'a': ['apple', 'Agave'], 'b': ['banana']}


def test__update_attendance_emptydict() -> None:
    """Testing the update_attendance function for an empty input dictionary, day and student."""
    testdict: dict[str, list[str]] = {}
    testday: str = ""
    testname: str = ""
    assert update_attendance(testdict, testday, testname) == {}


def test__update_attendance_usecase1() -> None:
    """Testing the update_attendance function for a normal use case."""
    testdict: dict[str, list[str]] = {'Monday': ['Alice']}
    testday: str = "Monday"
    testname: str = "Bob"
    assert update_attendance(testdict, testday, testname) == {'Monday': ['Alice', 'Bob']}


def test__update_attendance_usecase1() -> None:
    """Testing the update_attendance function for a normal use case."""
    testdict: dict[str, list[str]] = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Alice']}  
    testday: str = "Tuesday"
    testname: str = "Cindy"
    assert update_attendance(testdict, testday, testname) == {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Alice', 'Cindy']}