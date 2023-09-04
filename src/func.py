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
