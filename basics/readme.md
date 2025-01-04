# Basics

## Calculator

### Explaination:
This Python code defines a function `result()` that performs arithmetic operations based on the input operator. The function takes three parameters: `a`, `op`, and `b`, where `a` and `b` are integers and `op` is a string representing the operator. It uses a `match` statement to determine which operation to perform based on the operator provided (`+`, `-`, `*`, `/`, `%`). If the division operator (`/`) is chosen and `b` is zero, it returns an error message for division by zero. The script then takes user input for two numbers and an operator, calls the `result()` function with these inputs, and prints the result.

## class

### Explaination:
This Python program defines a `Car` class with attributes for `company`, `model`, `color`, and `year`, and a method `display_info()` that prints these details in a formatted way. In the `main()` function, a simple menu system is implemented to allow the user to interact with the program. The options include adding a car (which prompts the user for details), viewing the list of added cars (which prints the details of each car using `display_info()`), or exiting the program. The `cars` list is used to store instances of the `Car` class, and the program will continue running until the user chooses to exit.

## Function

### Explaination:
This Python program defines a function `is_even()` that checks if a number is even by using the modulus operator (`%`) to determine if the number divided by 2 has a remainder of 0. The function `check_number()` prompts the user to input a number, then calls `is_even()` to determine if the number is even or odd, and prints the corresponding message. If the number is even, it prints that the number is even; otherwise, it prints that the number is odd. The program is executed when the script is run, invoking `check_number()`.

## list-dict

### Explaination:
This Python program implements a basic contact management system using a dictionary to store contacts, where the contact name is the key and the phone numbers are stored as a list of strings. The `contact_management()` function presents a menu with options to add a contact, view contacts, remove a contact, or exit the program. 

- **Adding a contact**: The user is prompted to enter a name and phone numbers, and the contact is stored in the `contacts` dictionary.
- **Viewing contacts**: The program displays all contacts, showing each contact's name and associated phone numbers.
- **Removing a contact**: The user can remove a contact by name. If the contact exists, it is deleted from the dictionary.
- **Exiting the program**: The loop terminates when the user selects option 4.

The system continues to prompt the user for input until they choose to exit.
