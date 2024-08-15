from notes import Notes
from functools import wraps
from typing import List
from address_book import AddressBook
from birthday import Birthday
from email import Email
from notes import Notes
from colorama import Fore, Style


# def input_error(handler):
#     @wraps(handler)
#     def wrapper(*args, **kwargs):
#         try:
#             return handler(*args, **kwargs)
#         except (KeyError, ValueError, IndexError) as e:
#             return str(e)
#
#     return wrapper

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except IndexError:
            return "Error: Missing argument."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return wrapper


@input_error
def add_note(args: List[str], notes: Notes) -> str:
    title = input("Enter a title: ")
    if notes.find_note_by_title(title):
        return f"Note with title '{title}' already exists."
    text = input("Enter a text: ")
    tags = input("Enter tags (comma separated): ")
    try:
        notes.add_note(title, text, tags)
        return f"Note with title: '{title}' successfully added."
    except ValueError as e:
        return str(e)


@input_error
def delete_note(notes: Notes):
    title = input("Enter a title: ")
    note = notes.find_note_by_title(title)
    if note:
        notes.notes.remove(note)
        if notes.find_note_by_title(title):
            return f"Note with title: '{title}' not found."
        else:
            return f"Note with title: '{title}' successfully deleted."
    else:
        return f"Note with title: '{title}' not found."


@input_error
def change_note(notes: Notes):
    title = input("Enter a title: ")
    new_content = input("Enter new content: ")
    new_tags = input("Enter new tags: ")

    note = notes.find_note_by_title(title)

    if note:
        if new_content:
            note.content = new_content

        if new_tags:
            note.tags = [tag.strip() for tag in new_tags.split(",")]

        return f"Note with title '{title}' successfully edited."
    else:
        return f"Note with title '{title}' not found."


@input_error
def find_note_by_title(notes: Notes) -> str:
    title = input("Enter the title to search for: ")
    note = notes.find_note_by_title(title)
    if note:
        return str(note)
    else:
        return f"Note with title '{title}' not found."


@input_error
def find_note_by_tag(notes: Notes, tag: str) -> str:
    tag = input("Enter the tag to search for: ")
    notes_with_tag = notes.find_note_by_tag(tag)
    if notes_with_tag:
        return "\n".join(str(note) for note in notes_with_tag)
    else:
        return f"No notes found with tag '{tag}'."


@input_error
def show_all_notes(notes: Notes):
    return notes.show_all_notes()
