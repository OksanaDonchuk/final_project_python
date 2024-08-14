from my_contacts_book.comments import Title, Content, Tags

class Note:
    def __init__(self, title: str, content: str = None, tags: list = None):
        if not title:
            raise ValueError("Title cannot be empty.")
        self.title = Title(title)
        self.content = Content(content) if content else Content("") 
        self.tags = tags if tags else [] 

    def __str__(self) -> str:
        
        title_str = f"Title: {self.title.value}"
        content_str = f"Content: {self.content.value}" if self.content.value else ""
        tags_str = f"Tags: {', '.join(self.tags)}" if self.tags else ""
        return "\n".join(filter(None, [title_str, content_str, tags_str]))

    # def add_tags(self, note, new_tags):
    #     if not new_tags:
    #         return
    #     note.tags = [str(tag).strip() for tag in note.tags.split(",")]
    #     for tag in new_tags.split(","):
    #         if tag not in note.tags:
    #             note.tags.append(tag)
    #     return f"Tags added to note with title: '{note.title.value}'."
    def add_tags(self, new_tags: str) -> str:
        if not new_tags:
            return "No tags provided."
        new_tags = [tag.strip() for tag in new_tags.split(",")]
        self.tags.extend(tag for tag in new_tags if tag not in self.tags)
        return f"Tags added to note with title: '{self.title.value}'."

class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, content: str = None, tags: str = None) -> str:
        if self.find_note_by_title(title):
            return f"Note with title: '{title}' already exists."
        note = Note(title, content, tags.split(",") if tags else [])
        self.notes.append(note)
        return f"Note with title: '{title}' successfully added."
    
    def delete_note(self, title: str) -> str:
        note = self.find_note_by_title(title)
        if note:
            self.notes.remove(note)
            return f"Note with title: '{title}' successfully deleted."
        else:
            return f"Note with title: '{title}' not found."

    def change_note(self, title: str, new_content: str = None, new_tags: str = None) -> str:
        note = self.find_note_by_title(title)
        if note:
            if new_content:
                note.content = Content(new_content)
            if new_tags:
                note.tags = [tag.strip() for tag in new_tags.split(",")]
            return f"Note with title: '{title}' successfully edited."
        else:
            return f"Note with title: '{title}' not found."

    def find_note_by_title(self, title: str) -> Note:
        if not title:
            raise ValueError("Title is required")
        for note in self.notes:
            if note.title.value.lower() == title.lower():
                return note
        return None

    def find_note_by_tag(self, tag: str) -> list:
        if not tag:
            raise ValueError("Tag is required")
        return [note for note in self.notes if tag.lower() in [t.lower() for t in note.tags]]

    def show_all_notes(self):
        if not self.notes:
            return "There are no notes available."

        divider_str = "*" * 40
        notes_str = "\n\n".join(f"{divider_str}\n{note}\n{divider_str}" for note in self.notes)
        return notes_str