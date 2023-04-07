import os
from datetime import datetime

origin_path = "Files/"


def print_all_files(path):
    general_expenses = []
    for file in os.listdir(path):
        sum_expenses = process_input(path + "/" + file)
        print(f"{file}: {sum_expenses}€")
        general_expenses.append(sum_expenses)
    print(f"General: {round(sum(general_expenses), 2)}€")


def process_input(path):
    expenses = []
    for curr_expense in open(path).read().split("\n"):
        if curr_expense.replace('.', '').replace(',', '').isdigit():
            if "," in curr_expense:
                expenses.append(float(curr_expense.replace(",", ".")))
            else:
                expenses.append(float(curr_expense))
    return round(sum(expenses), 2)


def continue_asking():
    while True:
        check = input("Continue? Y/N")
        if check == 'Y' or check == 'y':
            return True
        elif check == 'N' or check == 'n':
            return False


def option_one():
    directories = os.listdir(origin_path)
    directories.sort(key=lambda date: datetime.strptime(date, "%b.%Y"))
    for i in directories:
        print(i + "\n")
        print_all_files(origin_path + i)
        print("---------------")


def option_two():
    while True:
        while True:
            directory = input("Directory to read: ")
            path = origin_path + directory
            if os.path.exists(path):
                break
        print_all_files(path)
        if not continue_asking():
            break


def option_three():
    files = ["auto.txt", "bekommeich.txt", "bestellen.txt", "e-scooter.txt", "einkauf.txt", "essen.txt", "selber.txt"]
    while True:
        directory_name = input("Directory-Name-Format: Mon.YYYY\n")
        try:
            if directory_name == datetime.strptime(directory_name, "%b.%Y").strftime('%b.%Y'):
                full_path = origin_path + directory_name
                os.mkdir(full_path)
                [open(full_path + "/" + i, 'x') for i in files]
                if not continue_asking():
                    break
        except ValueError:
            continue
        except FileNotFoundError:
            continue


def option_four():
    while True:
        directory_name = input("Which directory should be marked as payed back? Mon.YYYY\n")
        try:
            if directory_name == datetime.strptime(directory_name, "%b.%Y").strftime('%b.%Y'):
                full_path = origin_path + directory_name
                os.rename(full_path + "/bekommeich.txt", full_path + "/bekommeich_payed.txt")
                if not continue_asking():
                    break
        except ValueError:
            continue
        except FileNotFoundError:
            continue


def execute_options():
    option = input(f'Type 1 2 3 4\nOption 1: List all Expenses\nOption 2: Show specific File\nOption 3: Add new File\nOption 4: Mark payed\n')
    if option == '1':
        option_one()
    elif option == '2':
        option_two()
    elif option == '3':
        option_three()
    elif option == '4':
        option_four()


def main():
    try:
        while True:
            execute_options()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
