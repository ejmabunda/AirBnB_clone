#!/usr/bin/python3
"""This module supplies the base class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """"Represents the base model.

    Attributes:
        id (str): Unique identifier of a model instance.
        created_at (datetime): Date instance was created.
        updated_at (datetime): Date instance was updated.

    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of '__dict__'
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = datetime.isoformat(self.created_at)
        my_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return my_dict
