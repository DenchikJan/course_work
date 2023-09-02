import pytest
from pathlib import Path
from src.func import read_file

path = Path("files", "test_file.json")


@pytest.fixture
def array_fixture_1():
    return [{"first_name": "Denis", "last_name": "Volchkov"},
            {"first_name": "Vladimir", "last_name": "Ivanov"},
            {"first_name": "Ksenia", "last_name": "Petrova"},
            {"first_name": "Daria", "last_name": "Mayorova"},
            {"first_name": "Anton", "last_name": "Sidorov"}
            ]


def test_read_file(array_fixture_1):
    assert read_file(path) == array_fixture_1
