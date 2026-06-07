import pandas as pd
import os

EXCEL_FILE = "people_data.xlsx"

# Initialize the Excel file if it doesn't exist
def initialize_file():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=["ID", "Name"])
        df.to_excel(EXCEL_FILE, index=False)
        print("Excel file initialized.")

# Load Excel file
def load_data():
    return pd.read_excel(EXCEL_FILE)

# Save data to Excel file
def save_data(df):
    df.to_excel(EXCEL_FILE, index=False)

# Add entry
def add_entry():
    df = load_data()
    new_id = input("Enter ID: ").strip()
    if new_id in df['ID'].astype(str).values:
        print("This ID already exists.")
        return
    name = input("Enter Name: ").strip()
    new_row = pd.DataFrame([{"ID": new_id, "Name": name}])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    print("Entry added.")

# Delete entry
def delete_entry():
    df = load_data()
    search = input("Enter ID or Name to delete: ").strip()
    initial_len = len(df)
    df = df[(df['ID'].astype(str) != search) & (df['Name'].str.lower() != search.lower())]
    if len(df) < initial_len:
        save_data(df)
        print("Entry deleted.")
    else:
        print("No matching entry found.")

# Search by ID
def search_by_id():
    df = load_data()
    search_id = input("Enter ID to search: ").strip()
    result = df[df['ID'].astype(str) == search_id]
    if not result.empty:
        print(result.to_string(index=False))
    else:
        print("No entry found for this ID.")

# Search by Name
def search_by_name():
    df = load_data()
    name = input("Enter Name to search: ").strip().lower()
    result = df[df['Name'].str.lower() == name]
    if not result.empty:
        print(result.to_string(index=False))
    else:
        print("No entry found for this name.")

# Main menu
def main():
    initialize_file()
    while True:
        print("\n----- ID-Name Excel Handler -----")
        print("1. Add Entry")
        print("2. Delete Entry")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. View All")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            delete_entry()
        elif choice == "3":
            search_by_id()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            df = load_data()
            print(df.to_string(index=False))
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
