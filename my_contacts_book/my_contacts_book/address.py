from field import Field

class Address(Field):
    """
    Class to represent an address field.

    Attributes:
        value (str): The address value as a string.
    """

    def __init__(self, value: str):
        """
        Initializes an Address instance.

        Args:
            value (str): The address value as a string.
        """
        self.value = value