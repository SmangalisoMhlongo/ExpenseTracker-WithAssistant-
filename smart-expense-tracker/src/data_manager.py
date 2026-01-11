import pandas as pd
import os

#path where all expenses will be stored and loaded from
FILE_PATH = "data/expenses.csv"

#colums that will be in our expenses file
COLUMNS = ["date", "description", "amount", "category"]

#to load the expenses csv file
def load_expenses():
    
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        return pd.DataFrame(columns=COLUMNS)

    return pd.read_csv(FILE_PATH)

#adding an expense as a test
def add_expense(date, description, amount, category="unknown"):

    df = load_expenses()

    new_expense = {
        "date": date,
        "description": description,
        "amount": float(amount),
        "category": category
    }

    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

#to get all expenses
def get_all_expenses():
    return load_expenses()

