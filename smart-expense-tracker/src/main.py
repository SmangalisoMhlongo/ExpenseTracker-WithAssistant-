from data_manager import add_expense, get_all_expenses
from classifier import predict_category

def show_menu():
    print("\n=== Smart Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Exit")

def handle_add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    # Predict category using ML
    category = predict_category(description)

    # Save expense with predicted category
    add_expense(date, description, amount, category)

    print(f"Expense added under category: {category}")

def handle_view_expenses():
    expenses = get_all_expenses()

    if expenses.empty:
        print("No expenses found.")
    else:
        print("\nYour expenses:")
        print(expenses)
#main loop to keep everything running smoothly, I used different funcstions to keep things clean
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
