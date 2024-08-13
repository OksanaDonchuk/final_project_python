from functools import wraps
from typing import List
from address_book import AddressBook
from birthday import Birthday
from record import Record
from colorama import Fore, Style
from prettytable import PrettyTable

def input_error(func):
    """
    Decorator to handle input errors and return error messages.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"{Fore.YELLOW}Error: {str(e)}{Style.RESET_ALL}"
    return inner


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    """
    Adds a contact to the address book.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) < 2:
        raise ValueError("Error: Give me name and phone please.")
    
    name, phone, *optional_args = args
    name = name.capitalize()
    birthday = optional_args[0] if optional_args else None
    
    existing_record = book.find(name)
    if existing_record and any(phone == p.value for p in existing_record.phones):
        return f"{Fore.YELLOW}Contact with this name and phone number already exists.{Style.RESET_ALL}"
    
    if existing_record:
        existing_record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        if birthday:
            record.add_birthday(birthday)
        book.add_record(record)
        return f"{Fore.GREEN}Contact added.{Style.RESET_ALL}"

    return f"{Fore.GREEN}Contact updated.{Style.RESET_ALL}"

@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    """
    Changes a phone number for an existing contact or removes a phone number if only two arguments are provided.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) == 3:
        name, old_phone, new_phone = args
        name = name.capitalize()
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            return f"{Fore.GREEN}Phone number updated.{Style.RESET_ALL}"
        return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"
    
    elif len(args) == 2:
        name, phone_to_remove = args
        name = name.capitalize()
        record = book.find(name)
        if record:
            if record.find_phone(phone_to_remove):
                record.remove_phone(phone_to_remove)
                return f"{Fore.GREEN}Phone number removed.{Style.RESET_ALL}"
            else:
                return f"{Fore.YELLOW}Phone number not found in the contact.{Style.RESET_ALL}"
        return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"
    
    else:
        raise ValueError("Error: Give me name, old phone and new phone please or name and phone to remove.")

@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    """
    Shows the phone number for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Error: Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Phones"]
        phones = ", ".join([str(phone) for phone in record.phones])
        table.add_row([name, phones])
        return f"{Fore.BLUE}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"

@input_error
def show_all(book: AddressBook) -> str:
    """
    Shows all contacts in the address book.

    Args:
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if not book:
        return f"{Fore.YELLOW}The address book is empty.{Style.RESET_ALL}"
    
    table = PrettyTable()
    table.field_names = ["Name", "Phones", "Birthday"]
    for record in book.values():
        phones = ", ".join([str(phone) for phone in record.phones])
        birthday = str(record.birthday) if record.birthday else ""
        table.add_row([record.name, phones, birthday])
    return f"{Fore.BLUE}{table}{Style.RESET_ALL}"

@input_error
def delete_contact(args: List[str], book: AddressBook) -> str:
    """
    Deletes a contact from the address book.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Error: Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        book.delete(name)
        return f"{Fore.GREEN}Contact deleted.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"

@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    """
    Adds a birthday to the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 2:
        raise ValueError("Error: Give me name and birthday please.")
    
    name, birthday = args
    name = name.capitalize()
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"{Fore.GREEN}Birthday added.{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    """
    Shows the birthday for the specified contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 1:
        raise ValueError("Error: Give me name, please.")
    
    name = args[0].capitalize()
    record = book.find(name)
    if record:
        table = PrettyTable()
        table.field_names = ["Name", "Birthday"]
        birthday = str(record.birthday) if record.birthday else "No birthday set"
        table.add_row([name, birthday])
        return f"{Fore.BLUE}{table}{Style.RESET_ALL}"
    return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"

@input_error
def change_birthday(args: List[str], book: AddressBook) -> str:
    """
    Changes the birthday for an existing contact.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    if len(args) != 2:
        raise ValueError("Error: Give me the name of the contact and the new birthday please.")

    name, new_birthday = args
    name = name.capitalize()
    record = book.find(name)

    if record:
        if record.birthday:
            record.birthday = Birthday(new_birthday)
            return f"{Fore.GREEN}Birthday updated.{Style.RESET_ALL}" 
        else:
            return f"{Fore.YELLOW}Contact has no existing birthday to update.{Style.RESET_ALL}" 
    return f"{Fore.YELLOW}Contact not found.{Style.RESET_ALL}"

@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    """
    Shows upcoming birthdays within the next 7 days.

    Args:
        args (List[str]): The arguments for the command.
        book (AddressBook): The address book instance.

    Returns:
        str: The response message.
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return f"{Fore.YELLOW}No birthdays in the next 7 days.{Style.RESET_ALL}"
    table = PrettyTable()
    table.field_names = ["Name", "Birthday", "Phones"]
    for record in upcoming_birthdays:
        phones = ", ".join([str(phone) for phone in record.phones])
        table.add_row([record.name, record.birthday, phones])
    return f"{Fore.BLUE}{table}{Style.RESET_ALL}"