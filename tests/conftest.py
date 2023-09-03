import pytest


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