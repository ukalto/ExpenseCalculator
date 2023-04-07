expenses = []


def proceed_input(curr_expense):
    if "," in curr_expense:
        expenses.append(float(curr_expense.replace(",", ".")))
    else:
        expenses.append(float(curr_expense))


def main():
    while True:
        curr_expense = input()
        if curr_expense == "":
            print(sum(expenses).__round__(2))
            break
        proceed_input(curr_expense)


if __name__ == "__main__":
    main()
