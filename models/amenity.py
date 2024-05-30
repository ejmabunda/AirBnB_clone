#!/usr/bin/python3
from models.base_model import BaseModel
"""This module supplies the Amenity class.
"""


class Amenity(BaseModel):
    """Represents an Amenity entity.

    Attributes:
    name (str): The name of the amenity (empty string by default).
    """

    name: str = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
