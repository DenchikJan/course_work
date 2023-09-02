import pytest
from pathlib import Path
from src.func import read_file, filter_list

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


def test_read_file(array_fixture_1):
    assert read_file(path) == array_fixture_1


def test_filter_dict(array_fixture_1, array_fixture_2, array_fixture_3):
    assert filter_list(array_fixture_1, 'first_name', 'Denis') == array_fixture_3
    assert filter_list(array_fixture_1, 'fame', 'Denis') == []
    assert filter_list(array_fixture_2, 'first_name', 'Denis') == array_fixture_3
    assert filter_list([], 'first_name', 'Denis') == []
