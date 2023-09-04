class ListMod:

    def __init__(self, array):
        self.array = array

    def filter_list(self, key_name, filter_name) -> list:
        """
        И выдает список из словарей в которых есть заданый фильтр.
        :param key_name: ключ для фильтра
        :param filter_name: фильтр
        :return: список
        """
        new_list = []
        for elements in self.array:
            if type(elements) == dict:
                if key_name in elements.keys():
                    if elements[key_name] == filter_name:
                        new_list.append(elements)
        self.array = new_list
        return self.array

    def sort_list(self, key_sort, reverse=False) -> list:
        """
        Сорует список на основе элемента словоря по заданному ключу
        :param key_sort: ключ для сортировки
        :param reverse: по возростанию при reverse=False и по убыванию при reverse=True
        :return: список
        """
        self.array.sort(key=lambda dictionary: dictionary[key_sort], reverse=reverse)
        return self.array

    def slise_list(self, start=0, end=5) -> list:
        """
        Возвращает новый массив, содержащий копию части исходного массива.
        :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
        start = 0, если индекс больше длинны списк, start = длинна списка - 1. По умолчанию равен нулю.
        :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
        Если индекс отрицательный, start = 0, если индекс больше длинны списк, start = длинна списка.
        По умолчанию равен пяти.
        start должен быть меньше end.
        Если start = end, то end = end + 1.
        :return: список
        """
        if start > end:
            start_tmp = start
            start = end
            end = start_tmp

        if start < 0:
            start_point = 0
        elif start >= len(self.array):
            start_point = len(self.array) - 1
        else:
            start_point = start

        if end < 0:
            end_point = 0
        elif end > len(self.array):
            end_point = len(self.array)
        else:
            end_point = end

        if start_point == end_point:
            end_point += 1
            self.array = self.array[start_point:end_point]
            return self.array
        else:
            self.array = self.array[start_point:end_point]
            return self.array
