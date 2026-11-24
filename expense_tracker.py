expenses = []

while True:
    print("\n1. Add Expense\n2. View Total Expense\n3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        item = input("Enter item name: ")
        amount = float(input("Enter amount (in Rs): "))
        expenses.append((item, amount))
        print("Expense added successfully!")
    elif choice == '2':
        total = sum(amount for item, amount in expenses)
        print(f"\nTotal Expense: Rs. {total}")
        for item, amount in expenses:
            print(f"- {item}: Rs. {amount}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
