from src.func import (read_file, filter_list, sort_list, slise_list, formatting_date, print_description)

cnt = 0
print_from = ""
print_to = ""
array = read_file("../files/operations.json")
array = filter_list(array, "state", "EXECUTED")
array = sort_list(array, "date", True)
array = slise_list(array)

for element in array:
    cnt += 1
    print(f"---{cnt}---")
    print(formatting_date(element['date']), element['description'])
    print_from = print_description(element, "from")
    print_to = print_description(element, "to")
    print(f"{print_from} -> {print_to}")
    print(element["operationAmount"]["amount"], element["operationAmount"]["currency"]["name"])
