import json


def read_file(file_name) -> list:
    """
    Читает файл file_name
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
    return content


def filter_list(array: list, key_name, filter_name) -> list:
    new_list = []
    for elements in array:
        if type(elements) == dict:
            if key_name in elements.keys():
                if elements[key_name] == filter_name:
                    new_list.append(elements)
    return new_list


def sort_list(array: list, key_sort, reverse=False) -> list:
    array.sort(key=lambda dictionary: dictionary[key_sort], reverse=reverse)
    return array


def slise_list(array: list, start=0, end=5) -> list:
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
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return ""


def cart_number_mask(cart_number: str) -> str:
    if len(cart_number) == 16:
        return f"{cart_number[:4]} {cart_number[4:6]}** **** {cart_number[-4:]}"
    else:
        return ""
