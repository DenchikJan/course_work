from src.func import read_file, filter_list, sort_list, slise_list, account_number_mask, cart_number_mask,formatting_date

cnt = 0
print_from = ""
print_to = ""
array = read_file("../files/operations.json")
array = filter_list(array, "state", "EXECUTED")
array = sort_list(array, "date", True)
array = slise_list(array)
print(array)

for element in array:
    cnt += 1
    print(f"---{cnt}---")
    print(formatting_date(element['date']), element['description'])
    if "from" in element.keys():
        from_ = element["from"].split()
        if len(from_[-1]) == 16:
            print_from = f'{" ".join(from_[:-1])} {cart_number_mask(from_[-1])}'
        elif len(from_[-1]) == 20:
            print_from = f'{" ".join(from_[:-1])} {account_number_mask(from_[-1])}'
        else:
            print_from = "ERROR"
    else:
        print_from = "Not date"

    if "to" in element.keys():
        to_ = element["to"].split()
        if len(to_[-1]) == 16:
            print_to = f'{" ".join(to_[:-1])} {cart_number_mask(to_[-1])}'
        elif len(to_[-1]) == 20:
            print_to = f'{" ".join(to_[:-1])} {account_number_mask(to_[-1])}'
        else:
            print_to = "ERROR"

    else:
        print_to = "Not date"

    print(f"{print_from} -> {print_to}")
    print(element["operationAmount"]["amount"], element["operationAmount"]["currency"]["name"])
