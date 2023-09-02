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
