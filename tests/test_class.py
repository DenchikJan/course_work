from src.class_list import ListMod


class TestListMod:

    def test_filter_list(self, array_fixture_1, array_fixture_2 ,array_fixture_3):
        list_1 = ListMod(array_fixture_1)
        list_2 = ListMod(array_fixture_2)
        list_3 = ListMod([])
        assert list_1.filter_list('first_name', 'Denis') == array_fixture_3
        assert list_1.filter_list('fame', 'Denis') == []
        assert list_2.filter_list('first_name', 'Denis') == array_fixture_3
        assert list_3.filter_list('first_name', 'Denis') == []

    def test_sort_list(self, array_fixture_1, array_fixture_4):
        list_1 = ListMod(array_fixture_1)
        assert list_1.sort_list('first_name', True) == array_fixture_4

    def test_slise_list(self, array_fixture_1, array_fixture_5, array_fixture_6, array_fixture_7, array_fixture_3):
        list_1 = ListMod(array_fixture_1)
        list_2 = ListMod(array_fixture_1)
        list_3 = ListMod(array_fixture_1)
        list_4 = ListMod(array_fixture_1)
        list_5 = ListMod(array_fixture_1)
        list_6 = ListMod(array_fixture_1)
        list_7 = ListMod(array_fixture_1)
        assert list_1.slise_list(0, 2) == array_fixture_5
        assert list_2.slise_list(-5, 2) == array_fixture_5
        assert list_3.slise_list(5, 2) == array_fixture_6
        assert list_4.slise_list(9, 20) == array_fixture_7
        assert list_5.slise_list(0, 20) == array_fixture_1
        assert list_6.slise_list(-5, -2) == array_fixture_3
        assert list_7.slise_list(4, 4) == array_fixture_7
