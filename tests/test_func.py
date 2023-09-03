import pytest
from pathlib import Path
from src.func import read_file, filter_list, sort_list, slise_list, account_number_mask, cart_number_mask

path = Path("files", "test_file.json")


@pytest.fixture
def array_fixture_1():
    return [{"first_name": "Denis", "last_name": "Volchkov"},
            {"first_name": "Vladimir", "last_name": "Ivanov"},
            {"first_name": "Ksenia", "last_name": "Petrova"},
            {"first_name": "Daria", "last_name": "Mayorova"},
            {"first_name": "Anton", "last_name": "Sidorov"}
            ]


@pytest.fixture
def array_fixture_2():
    return [{"first_name": "Denis", "last_name": "Volchkov"},
            {"first_name": "Vladimir", "last_name": "Ivanov"},
            {"first_name": "Ksenia", "last_name": "Petrova"},
            {"first_name": "Daria", "last_name": "Mayorova"},
            {"first_name": "Anton", "last_name": "Sidorov"},
            6
            ]


@pytest.fixture
def array_fixture_3():
    return [{"first_name": "Denis", "last_name": "Volchkov"}]


@pytest.fixture
def array_fixture_4():
    return [{'first_name': 'Vladimir', 'last_name': 'Ivanov'},
            {'first_name': 'Ksenia', 'last_name': 'Petrova'},
            {'first_name': 'Denis', 'last_name': 'Volchkov'},
            {'first_name': 'Daria', 'last_name': 'Mayorova'},
            {'first_name': 'Anton', 'last_name': 'Sidorov'}
            ]


@pytest.fixture
def array_fixture_5():
    return [{"first_name": "Denis", "last_name": "Volchkov"},
            {"first_name": "Vladimir", "last_name": "Ivanov"}
            ]


@pytest.fixture
def array_fixture_6():
    return [{"first_name": "Ksenia", "last_name": "Petrova"},
            {"first_name": "Daria", "last_name": "Mayorova"},
            {"first_name": "Anton", "last_name": "Sidorov"}
            ]


@pytest.fixture
def array_fixture_7():
    return [{"first_name": "Anton", "last_name": "Sidorov"}]


correct_cart_number = "1596837868705199"
correct_account_number = "64686473678894779589"
account_mask = "**9589"
no_correct_cart_number = "15968378687051"
no_correct_correct_account_number = "6468647367889477958900"
cart_mask = "1596 83** **** 5199"


def test_read_file(array_fixture_1):
    assert read_file(path) == array_fixture_1


def test_filter_list(array_fixture_1, array_fixture_2, array_fixture_3):
    assert filter_list(array_fixture_1, 'first_name', 'Denis') == array_fixture_3
    assert filter_list(array_fixture_1, 'fame', 'Denis') == []
    assert filter_list(array_fixture_2, 'first_name', 'Denis') == array_fixture_3
    assert filter_list([], 'first_name', 'Denis') == []


def test_sort_list(array_fixture_1, array_fixture_4):
    assert sort_list(array_fixture_1, 'first_name', True) == array_fixture_4


def test_slise_list(array_fixture_1, array_fixture_5, array_fixture_6, array_fixture_7, array_fixture_3):
    assert slise_list(array_fixture_1, 0, 2) == array_fixture_5
    assert slise_list(array_fixture_1, -5, 2) == array_fixture_5
    assert slise_list(array_fixture_1, 5, 2) == array_fixture_6
    assert slise_list(array_fixture_1, 9, 20) == array_fixture_7
    assert slise_list(array_fixture_1, 0, 20) == array_fixture_1
    assert slise_list(array_fixture_1, -5, -2) == array_fixture_3
    assert slise_list(array_fixture_1, 4, 4) == array_fixture_7


def test_account_number_mask():
    assert account_number_mask(correct_account_number) == account_mask
    assert account_number_mask(no_correct_correct_account_number) == ""


def test_cart_number_mask():
    assert cart_number_mask(correct_cart_number) == cart_mask
    assert cart_number_mask(no_correct_cart_number) == ""
