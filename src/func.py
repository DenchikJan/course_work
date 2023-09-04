import json
import maya
import datetime

def read_file(file_name) -> list:
    """
    Читает файл file_name json
    :param file_name: путь к файлу
    :return: список
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
    return content


def filter_list(array: list, key_name, filter_name) -> list:
    """
    И выдает список из словарей в которых есть заданый фильтр.
    :param array: исходный список.
    :param key_name: ключ для фильтра
    :param filter_name: фильтр
    :return: список
    """
    new_list = []
    for elements in array:
        if type(elements) == dict:
            if key_name in elements.keys():
                if elements[key_name] == filter_name:
                    new_list.append(elements)
    return new_list


def sort_list(array: list, key_sort, reverse=False) -> list:
    """
    Сорует список на основе элемента словоря по заданному ключу
    :param array: исходный список.
    :param key_name: ключ для сортировки
    :param filter_name: по возростанию при reverse=False и по убыванию при reverse=True
    :return: список
    """
    array.sort(key=lambda dictionary: dictionary[key_sort], reverse=reverse)
    return array


def slise_list(array: list, start=0, end=5) -> list:
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param array: исходный список.
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
    elif start >= len(array):
        start_point = len(array) - 1
    else:
        start_point = start

    if end < 0:
        end_point = 0
    elif end > len(array):
        end_point = len(array)
    else:
        end_point = end

    if start_point == end_point:
        end_point += 1
        return array[start_point:end_point]
    else:
        return array[start_point:end_point]


def account_number_mask(account_number: str) -> str:
    """
    Заменяет в строке все элементы кроме последних 4 символов на "**"
    если в исходной строке не 20 символов выводит ""
    :param account_number: исходная строка
    :return: строка
    """
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return ""


def cart_number_mask(cart_number: str) -> str:
    """
    Преобразует строку к формату XXXX XX** **** XXXX
    если и сиходной строке не 16 символов выводит ""
    :param cart_number: исходная строка
    :return: строка
    """
    if len(cart_number) == 16:
        return f"{cart_number[:4]} {cart_number[4:6]}** **** {cart_number[-4:]}"
    else:
        return ""


def formatting_date(str_date: str) -> datetime:
    """
    Преобразует дату к вормату число.месяц.год
    :param str_date: исходная строка
    :return: строка
    """
    dt = maya.parse(str_date).datetime()
    return dt.strftime("%d.%m.%Y")


def print_description(array: dict, key) -> str:
    """
    Выводит название карты и маска ее номера или счет и маска его номера
    При отсустствие ключа выводит Not date 
    При длинне строке не 16 или 20 выводит ERROR
    :param array: исходный словарь
    :param key: ключь 
    :return: строка
    """
    if key in array.keys():
        from_ = array[key].split()
        if len(from_[-1]) == 16:
            return f'{" ".join(from_[:-1])} {cart_number_mask(from_[-1])}'
        elif len(from_[-1]) == 20:
            return f'{" ".join(from_[:-1])} {account_number_mask(from_[-1])}'
        else:
            return "ERROR"
    else:
        return "Not date"
