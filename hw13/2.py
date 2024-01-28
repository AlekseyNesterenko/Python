from queue import Empty
from typing import Union

class InvalidNumberError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Invalid number: {self.value}. Number should be a positive integer or float.'
    
class InvalidTextError(Exception):
    def __init__(self, value):
        self.value = value
        pass
    def __str__(self):
        return f'Invalid text: {self.value}. Text should be a non-empty string.'

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not text or not isinstance(text, str):
            raise InvalidTextError(text)
        if number <= 0 or not isinstance(number, float):
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

archive_instance = Archive("Sample text", 42.5)
print(archive_instance)