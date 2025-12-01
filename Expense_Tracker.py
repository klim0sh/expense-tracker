from utils import (
    stats,
    load_expenses,
    save_expenses
)
def add_expense(expenses):
    while True:
        category = input("Enter a category(food, transport, entertainment, etc.):")
        name = input("Enter a name(or type 'stop' to finish): ").strip()
        if name.lower() == "stop": 
            break
        if name in expenses:
            print(f"{name} is already added.")
            continue
        try:
            amount = float(input("Enter an amount: "))
            expenses[name] = (amount, category)
        except ValueError:
            print("Enter a value. ")
            continue

def remove_expense(expenses):
    name = input("Enter the name of expense to delete: ").strip()
    if name in expenses:
        del expenses[name]
        print(f"{name} has been removed.")
    else:
        print(f"{name} is not found")

def show_expenses(expenses):
    for name, amount, category in expenses.items():
        print(f"  - {name:<15} {amount:10.2f} {category:>12}")
        
def edit_expense(expenses):
    name = input("Enter the name of expense to edit: ").strip()
    if name in expenses:
        try:
            new_amount = float(input("Enter a new amount: "))
            expenses[name] = new_amount
            print(f"{name} updated to {new_amount:.2f}")
        except ValueError:
            print("Enter a number.")
        
    else:
        print(f"{name} is not found.")


def program():
    expenses = load_expenses()
    while True:
        action = input(f"\nChoose action: [add/show/remove/edit/stats/exit] ").lower().strip()
        if action == "add":
            add_expense(expenses)
        elif action == "show":
            if not expenses:
                print("No expense to show or stats are empty")
                continue
            show_expenses(expenses)
        elif action == "remove":
            remove_expense(expenses)
        elif action == "edit":
            edit_expense(expenses)
        elif action == "stats":
            if not expenses:
                print("No expense to show or stats are empty")
                continue
            result = stats(expenses)
            print(f"Total expenses: {result['total']:.2f}")
            print(f"Average expenses: {result['average']:.2f}")
            print(f"Most expensive: {', '.join(result['max'][0])} ({result['max'][1]:.2f})")
            print(f"Cheapest: {', '.join(result['min'][0])} ({result['min'][1]:.2f})")
        elif action == "exit":
            save_expenses(expenses)
            break
        else:
            print("Invalid command")
program()