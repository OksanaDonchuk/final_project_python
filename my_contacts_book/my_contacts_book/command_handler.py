from address_book import AddressBook
from handlers import (
    add_contact, change_birthday, change_contact, change_name, delete_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays, add_email, delete_email, change_email, add_address, delete_address, change_address, show_contact
)
from colorama import Fore, Style  

class CommandHandler:
    def __init__(self):
        """
        Initializes the CommandHandler with a set of commands that can be executed.
        Each command is associated with a specific method that handles its logic.
        """
        self.commands = {
            "hello": self.hello,
            "add": self.add_contact,
            "change": self.change_contact,
            "change-name": self.change_name,
            "phone": self.show_phone,
            "contact": self.show_contact,
            "all": self.show_all,
            "add-birthday": self.add_birthday,
            "show-birthday": self.show_birthday,
            "birthdays": self.birthdays,
            "change-birthday": self.change_birthday,
            "add-email": self.add_email,
            "delete-email": self.delete_email,
            "change-email": self.change_email,
            "add-address": self.add_address,
            "delete-address": self.delete_address,
            "change-address": self.change_address,
            "delete": self.delete_contact,
            "help": self.print_help,
            "close": self.goodbye,
            "exit": self.goodbye,
            "bye": self.goodbye
        }

    def execute_command(self, action: str, args: list[str], book: AddressBook) -> str:
        """Executes a command based on the action provided.

        Args:
            action (str): The command action to execute.
            args (list[str]): The arguments to pass to the command function.
            book (AddressBook): The book object to be used for command operations.

        Returns:
            str: The result of the command execution or an error message if the command is invalid.
        """
        command = self.commands.get(action)
        if command:
            return command(args, book)
        else:
            return "Invalid command. The available commands are described in the help: command – help"

    def hello(self, args: list[str], book: AddressBook) -> str:
        """Returns a greeting message to the user."""
        return "How can I help you?"

    def add_contact(self, args: list[str], book: AddressBook) -> str:
        """Adds a new contact to the book using the provided arguments."""
        return add_contact(args, book)

    def change_contact(self, args: list[str], book: AddressBook) -> str:
        """Updates an existing contact in the book based on the provided arguments."""
        return change_contact(args, book)

    def change_name(self, args: list[str], book: AddressBook) -> str:
        """Updates the name of a specified contact in the book."""
        return change_name(args, book)

    def show_phone(self, args: list[str], book: AddressBook) -> str:
        """Retrieves and displays the phone number of a specified contact."""
        return show_phone(args, book)

    def show_contact(self, args: list[str], book: AddressBook) -> str:
        """Retrieves and displays the details of a specified contact."""
        return show_contact(args, book)

    def show_all(self, args: list[str], book: AddressBook) -> str:
        """Displays all contacts currently stored in the book."""
        return show_all(book)

    def add_birthday(self, args: list[str], book: AddressBook) -> str:
        """Adds a birthday for a specified contact in the book."""
        return add_birthday(args, book)

    def show_birthday(self, args: list[str], book: AddressBook) -> str:
        """Retrieves and displays the birthday of a specified contact."""
        return show_birthday(args, book)

    def birthdays(self, args: list[str], book: AddressBook) -> str:
        """Displays all birthdays of contacts stored in the book."""
        return birthdays(args, book)

    def change_birthday(self, args: list[str], book: AddressBook) -> str:
        """Updates the birthday of a specified contact in the book."""
        return change_birthday(args, book)

    def add_email(self, args: list[str], book: AddressBook) -> str:
        """Adds an email address for a specified contact in the book."""
        return add_email(args, book)

    def delete_email(self, args: list[str], book: AddressBook) -> str:
        """Deletes an email address associated with a specified contact."""
        return delete_email(args, book)

    def change_email(self, args: list[str], book: AddressBook) -> str:
        """Updates the email address of a specified contact in the book."""
        return change_email(args, book)

    def add_address(self, args: list[str], book: AddressBook) -> str:
        """Adds a physical address for a specified contact in the book."""
        return add_address(args, book)

    def delete_address(self, args: list[str], book: AddressBook) -> str:
        """Deletes a physical address associated with a specified contact."""
        return delete_address(args, book)

    def change_address(self, args: list[str], book: AddressBook) -> str:
        """Updates the physical address of a specified contact in the book."""
        return change_address(args, book)

    def delete_contact(self, args: list[str], book: AddressBook) -> str:
        """Removes a specified contact from the book."""
        return delete_contact(args, book)

    def print_help(self, args: list[str], book: AddressBook) -> str:
        """Provides help information regarding available commands and their usage."""
        return self.generate_help_message()

    def generate_help_message(self) -> str:
        """
        Returns a help message listing available commands and their usage.

        Returns:
            str: The help message string.
        """
        help_message = f"""
        {Fore.CYAN}Available commands:
        - hello: Displays a greeting message.
        - help: Shows this help message.
        - add <name> <phone>: Adds a new contact with the specified name and phone number.
                              If the contact already exists but with a different number, the contact will be updated.
        - change <name> <old_phone> <new_phone>: Changes the phone number for an existing contact.
                                                 If only the name and the existing number are provided, the number will be removed.
        - change-name <old_name> <new_name>: Changes the name of an existing contact.
        - phone <name>: Shows the phone number for the specified contact.
        - contact <name>: Shows the specified contact.
        - all: Shows all contacts with their phone numbers.
        - add-birthday <name> <birthday>: Adds a birthday to the specified contact.
        - show-birthday <name>: Shows the birthday for the specified contact.
        - birthdays: Shows upcoming birthdays within the next 7 days.
        - change-birthday <name> <new_birthday>: Changes the birthday for an existing contact.
        - add-email <name> <email>: Add an email to the specified contact.
        - delete-email <name> <email>: Delete an email from the specified contact.
        - change-email <name> <new_email>: Change an email for the specified contact.
        - add-address <name> <address>: Adds an address to the specified contact.
        - delete-address <name>: Deletes an address from the specified contact.
        - change-address <name> <new_address>: Changes an address for the specified contact.
        - delete <name>: Deletes a contact from the address book.
        - add-note
        - change-note
        - delete-note
        - show-all-notes
        - close / exit / bye: Exits the program.{Style.RESET_ALL}
        """
        return help_message

    def goodbye(self, args: list[str], book: AddressBook) -> str:
        """Returns a farewell message to the user."""
        return "Good bye!"

