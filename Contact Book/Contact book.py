contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact Added Successfully!")

def view_contacts():
    print("\n--- Contact List ---")

    if not contacts:
        print("No Contacts Found!")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter Name or Phone Number: ")

    found = False

    for contact in contacts:
        if (search.lower() == contact['name'].lower() or
                search == contact['phone']):
            print("\nContact Found:")
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            found = True
            break

    if not found:
        print("Contact Not Found!")

def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter Phone Number of Contact to Update: ")

    for contact in contacts:
        if contact['phone'] == phone:
            print("Enter New Details")

            contact['name'] = input("New Name: ")
            contact['phone'] = input("New Phone Number: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")

            print("Contact Updated Successfully!")
            return

    print("Contact Not Found!")

def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter Phone Number of Contact to Delete: ")

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            return

    print("Contact Not Found!")

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Your Choice (1-6): ")

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_contact()

    elif choice == '4':
        update_contact()

    elif choice == '5':
        delete_contact()

    elif choice == '6':
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
        