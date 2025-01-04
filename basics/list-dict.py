def contact_management():
    contacts = {}  

    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter the contact name: ")
            numbers = input("Enter the phone numbers (comma-separated): ")
            contacts[name] = numbers.split(',') 
            print(f"Contact '{name}' added with numbers: {numbers}.")

        elif choice == '2':
            if not contacts:
                print("No contacts found.")
            else:
                print("\nContacts:")
                for name, numbers in contacts.items():
                    print(f"Name: {name}, Numbers: {', '.join(numbers)}")

        elif choice == '3':
            name = input("Enter the contact name to remove: ")
            if name in contacts:
                del contacts[name]  
                print(f"Contact '{name}' removed.")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '4':
            print("Exiting the contact.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    contact_management()
