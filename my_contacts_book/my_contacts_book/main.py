import pickle
from transliteration import suggest_command, transliterate
from address_book import AddressBook
from handlers import (
    add_contact, change_birthday, change_contact, delete_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays
)
from colorama import init, Fore, Style

init(autoreset=True)

def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """
    Saves the address book to a file.

    Args:
        book (AddressBook): The address book instance to save.
        filename (str): The filename to save the address book to.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """
    Loads the address book from a file.

    Args:
        filename (str): The filename to load the address book from.

    Returns:
        AddressBook: The loaded address book instance.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def print_message(message: str, is_error: bool = False) -> None:
    """
    Prints a message in color based on whether it's an error or not.
    
    Args:
        message (str): The message to print.
        is_error (bool): Flag indicating if the message is an error.
    """
    if is_error:
        print(Fore.YELLOW + message + Style.RESET_ALL)
    else:
        print(Fore.GREEN + message + Style.RESET_ALL)

def handle_action(action: str, args: list[str], book: AddressBook) -> str:
    """
    Handles the action by calling the appropriate function using match...case.

    Args:
        action (str): The command to execute.
        args (list[str]): The arguments for the action.
        book (AddressBook): The address book instance.

    Returns:
        str: The response string after executing the command.
    """
    match action:
        case "hello":
            return "How can I help you?"
        case "add":
            return add_contact(args, book)
        case "change":
            return change_contact(args, book)
        case "phone":
            return show_phone(args, book)
        case "all":
            return show_all(book)
        case "add-birthday":
            return add_birthday(args, book)
        case "show-birthday":
            return show_birthday(args, book)
        case "birthdays":
            return birthdays(args, book)
        case "change-birthday":
            return change_birthday(args, book)
        case "delete":
            return delete_contact(args, book)
        case "help":
            return print_help()
        case "close" | "exit" | "bye":
            return "Good bye!"
        case _:
            return "Invalid command. Available commands are: hello, add, change, phone, all, add-birthday, show-birthday, birthdays, change-birthday, delete, close, exit, bye."

def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses the input string into a command and arguments.

    Args:
        user_input (str): Input string from the user.

    Returns:
        tuple[str, list[str]]: A tuple containing the command and a list of arguments.
    """
    action, *args = user_input.split()
    action = action.strip().lower()
    return action, args

def print_help() -> str:
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
    - phone <name>: Shows the phone number for the specified contact.
    - all: Shows all contacts with their phone numbers.
    - add-birthday <name> <birthday>: Adds a birthday to the specified contact.
    - show-birthday <name>: Shows the birthday for the specified contact.
    - birthdays: Shows upcoming birthdays within the next 7 days.
    - change-birthday <name> <new_birthday>: Changes the birthday for an existing contact.
    - delete <name>: Deletes a contact from the address book.
    - close / exit / bye: Exits the program.{Style.RESET_ALL}
    """
    return help_message

def main() -> None:
    """
    Main function to run the assistant bot.
    """
    book = load_data() 
    print(f"{Fore.BLUE}Welcome to the assistant bot!{Style.RESET_ALL}")
    print(print_help()) 
    while True:
        user_input = input("Enter a command:\n").strip().lower()
        if not user_input:
            continue

        action, args = parse_input(user_input)

        suggested_command = suggest_command(action, ["hello", "add", "change", "phone", "all", "add-birthday", "show-birthday", "birthdays", "change-birthday", "delete", "help", "close", "exit", "bye"])
        if suggested_command and suggested_command != action:
            confirm = input(f"Do you mean '{suggested_command}'? (y/n): ").strip().lower()
            if confirm == 'y':
                action = suggested_command

        response = handle_action(action, args, book)
        print(response)
        if action in ["close", "exit", "bye"]:
            save_data(book)
            break

if __name__ == "__main__":
    main()
