class expenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

    def store_to_csv(self):
        with open("examplefile.csv" , "a+") as file:
            for item in self.expenseDict['income']:
                file.write(str(item)+"\n")
            for item in self.expenseDict['expense']:
                file.write(str(item)+"\n")

# define a menu that will let users to enter expense, view expenses
# or income, get totals in each and exit from the program


def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details




myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Store the details to a csv file.")
    print("6. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        myexpense.store_to_csv()
    elif choice == 6:
        exit()
    else:
        print("In valid choice")

# create a method in the class
# to export the details in the from of csv
# add export details to a file in the menu options