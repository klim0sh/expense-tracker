import os
def stats(expenses):
    total = sum(expenses.values())
    average = total/len(expenses)
    max_amount = max(expenses.values())
    min_amount = min(expenses.values())
    max_items = [name for name, val in expenses.items() if val == max_amount]
    min_items = [name for name, val in expenses.items() if val == min_amount]
    return {
        "total": total,
        "average": average,
        "max": (max_items, max_amount),
        "min": (min_items, min_amount),
    }

def load_expenses():
    if not os.path.exists("expenses.txt"):
        return {}
    expenses = {}
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.split(",")
            expenses[parts[0]] = float(parts[1].strip())
    return expenses

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for name, amount in expenses.items():
            file.write(f"{name},{amount:.2f}\n")
    