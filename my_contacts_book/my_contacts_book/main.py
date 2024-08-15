import pickle
from transliteration import suggest_command, transliterate
from address_book import AddressBook
# from notes import Notes
from handlers import (
    add_contact, change_birthday, change_contact, change_name, delete_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays, add_email, delete_email, change_email, add_address, delete_address, change_address, show_contact)
from command_handler import CommandHandler


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


# def save_notes(notes: Notes, filename: str = "notes.pkl") -> None:
#     with open(filename, "rb") as file:
#         data = pickle.load(file)
#         data["notes"] = notes
#         with open(filename, "wb") as file:
#             pickle.dump(data, file)
            
# def load_notes(filename: str = "notes.pkl") -> Notes:
#     try:
#         with open(filename, "rb") as file:
#             data = pickle.load(file)
#             return data.get("notes", Notes())
#     except FileNotFoundError:
#         return Notes()
    
# def sort_by_tag(self, tag: str) -> list:
#         if not tag:
#             raise ValueError("Tag is required")
#         filtered_notes = self.find_note_by_tag(tag)
#         return sorted(filtered_notes, key=lambda note: note.title.value)    
    
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

def main() -> None:
    """
    Main function to run the assistant bot.
    """
    book = load_data() 
    command_handler = CommandHandler()
    # notes = load_notes()
    print(f"{Fore.BLUE}Welcome to the assistant bot!{Style.RESET_ALL}")
    print(command_handler.generate_help_message()) 
    while True:
        user_input = input("Enter a command:\n").strip().lower()
        if not user_input:
            continue

        action, args = parse_input(user_input)

        COMMANDS = list(command_handler.commands.keys())
        suggested_command = suggest_command(action, COMMANDS)

        if suggested_command and suggested_command != action:
            confirm = input(f"Do you mean '{suggested_command}'? (y/n): ").strip().lower()
            if confirm == 'y':
                action = suggested_command

        response = command_handler.execute_command(action, args, book)
        print(response)
        if action in ["close", "exit", "bye"]:
            save_data(book)
            # save_notes(notes)
            break

if __name__ == "__main__":
    main()
