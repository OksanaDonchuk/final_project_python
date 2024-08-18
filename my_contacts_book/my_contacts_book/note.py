class Note(Field):
    """
    Class to represent a note field.

    Attributes:
        title (str): The title of the note.
        text (str): The text content of the note.
        tag (str): The tag associated with the note.
    """

    def __init__(self, title: str, text: str, tag: str):
        """
        Initializes a Note instance.

        Args:
            title (str): The title of the note.
            text (str): The text content of the note.
            tag (str): The tag associated with the note.
        """
        super().__init__(title)
        self.title = title
        self.text = text
        self.tag = tag


    def __str__(self):
        return f"Note(title='{self.title}', text='{self.text}', tag='{self.tag}')"