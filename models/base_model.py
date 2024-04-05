#!/usr/bin/python3
"""This module supplies the base class for all classes."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class

    Attributes:
        id (str): a unique identifier for each BaseModel instance.
        created_at (datetime): timestamp of when the object was created.
        updated_at (datetime): timestamp of when the object was updated.

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, dt)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns the string representation of a BaseModel instance.

        Returns:
            str: The string representaion of a BaseModel instance.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates `updated_at` with the datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance.

        Returns:
            dict: A dictionary containing all keys/values of the instance.

        """
        inst_dict = {
            '__class__': self.__class__.__name__,
            **self.__dict__,
            'created_at': datetime.isoformat(self.created_at),
            'updated_at': datetime.isoformat(self.updated_at),
        }

        return inst_dict
