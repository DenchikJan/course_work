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
