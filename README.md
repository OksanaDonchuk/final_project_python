# My Contacts Book Bot

`my_contacts_book_bot` is a command-line tool for managing your contacts. This bot allows you to add, change, delete, and view contacts, as well as manage birthdays. The tool is designed to be simple and easy to use, with the added benefit of storing your data persistently between sessions.

## Installation

To install the package, you can use pip:

```sh
pip install my_contacts_book_bot

Usage
Once installed, you can run the bot using the following command:

my_contacts_book

Commands
hello: Displays a greeting message.
help: Shows a list of available commands and their usage.
add <name> <phone>: Adds a new contact with the specified name and phone number.
change <name> <old_phone> <new_phone>: Changes the phone number for an existing contact.
phone <name>: Displays the phone number for the specified contact.
all: Shows all contacts with their phone numbers.
add-birthday <name> <birthday>: Adds a birthday to the specified contact.
show-birthday <name>: Shows the birthday for the specified contact.
birthdays: Shows upcoming birthdays within the next 7 days.
change-birthday <name> <new_birthday>: Changes the birthday for an existing contact.
delete <name>: Deletes a contact from the address book.
close / exit / bye: Exits the program.

Example Usage

$ my_contacts_book
Welcome to the assistant bot!
Available commands:
- hello: Displays a greeting message.
- help: Shows this help message.
- add <name> <phone>: Adds a new contact with the specified name and phone number.
...
Enter a command:
```

## Persistent Storage

The bot automatically saves your address book to disk when you exit the program and restores it when you start the program again. This means you won't lose your contacts between sessions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

Oksana Donchuk
ksunya.donchuk@gmail.com

```

```
