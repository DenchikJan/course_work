from src.func import read_file, formatting_date, print_description
from src.class_list import ListMod

cnt = 0
print_from = ""
print_to = ""

array = read_file("../files/operations.json")
operations = ListMod(array)
operations.filter_list("state", "EXECUTED")
operations.sort_list("date", True)
operations.slise_list(0, 5)

for element in operations.array:
    cnt += 1
    print(f"---{cnt}---")
    print(formatting_date(element['date']), element['description'])
    print_from = print_description(element, "from")
    print_to = print_description(element, "to")
    print(f"{print_from} -> {print_to}")
    print(element["operationAmount"]["amount"], element["operationAmount"]["currency"]["name"])
