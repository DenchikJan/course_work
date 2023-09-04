from pathlib import Path
from src.func import (read_file, account_number_mask, cart_number_mask, formatting_date, print_description)

path = Path("files", "test_file.json")
correct_cart_number = "1596837868705199"
correct_account_number = "64686473678894779589"
account_mask = "**9589"
no_correct_cart_number = "15968378687051"
no_correct_correct_account_number = "6468647367889477958900"
cart_mask = "1596 83** **** 5199"
str_date = "2019-07-03T18:35:29.512364"
format_date = "03.07.2019"


def test_read_file(array_fixture_1):
    assert read_file(path) == array_fixture_1


def test_account_number_mask():
    assert account_number_mask(correct_account_number) == account_mask
    assert account_number_mask(no_correct_correct_account_number) == ""


def test_cart_number_mask():
    assert cart_number_mask(correct_cart_number) == cart_mask
    assert cart_number_mask(no_correct_cart_number) == ""


def test_formatting_date():
    assert formatting_date(str_date) == format_date


def test_print_description(array_fixture_8, array_fixture_9):
    assert print_description(array_fixture_8, "from") == "Maestro 1596 83** **** 5199"
    assert print_description(array_fixture_8, "to") == "Счет **9589"
    assert print_description(array_fixture_9, "from") == "Not date"
    assert print_description(array_fixture_9, "to") == "ERROR"
