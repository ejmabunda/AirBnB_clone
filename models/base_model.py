#!/usr/bin/python3
"""This module supplies the base class.
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """"Represents the base model.

    Attributes:
        id (str): Unique identifier of a model instance.
        created_at (datetime): Date instance was created.
        updated_at (datetime): Date instance was updated.

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of '__dict__'
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = datetime.isoformat(self.created_at)
        my_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return my_dict
