from crud.create_table import create_user_table
from crud.insert_table import insert_data
from crud.read_table import read_user_table
from crud.update_data import update_user_table
from crud.delete_data import delete_user

while True:

    print("\n===== USER MANAGEMENT SYSTEM =====")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_user_table()

    elif choice == '2':
        insert_data()

    elif choice == '3':
        read_user_table()

    elif choice == '4':
        update_user_table()

    elif choice == '5':
        delete_user()

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice")