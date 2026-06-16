contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")

    elif choice == "3":
        search_name = input("Enter name to search: ")

        if search_name in contacts:
            print(f"Phone Number: {contacts[search_name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")

        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")