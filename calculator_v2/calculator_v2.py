import os
from datetime import datetime

origin_path = "Files/"


def print_all_files(path, exclude):
    general_expenses = []
    for file in os.listdir(path):
        if not file in exclude:
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


def check_action():
    while True:
        check = input("Sure you want to do this? Y/N")
        if check == 'Y' or check == 'y':
            return True
        elif check == 'N' or check == 'n':
            return False


def option_one():
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    directories.sort(key=lambda date: datetime.strptime(date, "%b.%Y"))
    for i in directories:
        print(i + "\n")
        print_all_files(origin_path + i, "")
        print("---------------")


def option_two():
    while True:
        while True:
            directory = input("Directory to read: ")
            path = origin_path + directory
            if os.path.exists(path):
                break
        print_all_files(path, "")
        if not continue_asking():
            break


def option_three():
    files = open('files_preset', 'r').read().split('\n')
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


def option_five():
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    final_sum = 0
    for directory in directories:
        path = os.path.join(origin_path, directory)
        file_path = os.path.join(path, "bekommeich.txt")
        if os.path.exists(file_path):
            sum_expenses = process_input(file_path)
            final_sum += sum_expenses
            print(f"{directory}: {sum_expenses}€")
    print(f"Sum of currently open payments: {final_sum}€\n")


def option_six():
    if not check_action():
        return
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    for directory in directories:
        try:
            file_path = os.path.join(origin_path, directory)
            if os.path.exists(file_path + "/bekommeich.txt"):
                os.rename(file_path + "/bekommeich.txt", file_path + "/bekommeich_payed.txt")
        except ValueError:
            continue
        except FileNotFoundError:
            continue


def option_seven():
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    directories.sort(key=lambda date: datetime.strptime(date, "%b.%Y"))
    for i in directories:
        print(i + "\n")
        print_all_files(origin_path + i, "investments.txt")
        print("---------------")


def option_eight():
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    directories.sort(key=lambda date: datetime.strptime(date, "%b.%Y"))
    for i in directories:
        print(i + "\n")
        general_expenses = []
        for file in os.listdir(origin_path + i):
            if file == "investments.txt":
                sum_expenses = process_input(origin_path + i + "/" + file)
                print(f"{file}: {sum_expenses}€")
                general_expenses.append(sum_expenses)
        print(f"General: {round(sum(general_expenses), 2)}€")
        print("---------------")


def option_nine():
    directories = os.listdir(origin_path)
    directories.remove(".gitkeep")
    directories.sort(key=lambda date: datetime.strptime(date, "%b.%Y"))
    for i in directories:
        print(i + "\n")
        print_all_files(origin_path + i, ["investments.txt", "bekommeich.txt", "bekommeich_payed.txt"])
        print("---------------")


def execute_options():
    option = input(
        f'Type 1 2 3 4 5 6 7 8 9\n'
        f'Option 1: List all Expenses\n'
        f'Option 2: Show specific File\n'
        f'Option 3: Add new File\n'
        f'Option 4: Mark payed\n'
        f'Option 5: Calculate open payments\n'
        f'Option 6: Mark all payed\n'
        f'Option 7: List all expenses without investments\n'
        f'Option 8: List all investments\n'
        f'Option 9: List all expenses without investments and without money back\n')
    if option == '1':
        option_one()
    elif option == '2':
        option_two()
    elif option == '3':
        option_three()
    elif option == '4':
        option_four()
    elif option == '5':
        option_five()
    elif option == '6':
        option_six()
    elif option == '7':
        option_seven()
    elif option == '8':
        option_eight()
    elif option == '9':
        option_nine()


def main():
    try:
        while True:
            execute_options()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
