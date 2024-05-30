#!/usr/bin/python3
from models.base_model import BaseModel
"""This module supplies the City class.
"""


class City(BaseModel):
    """Represents a City entity.

    Attributes:
    state_id (str): The ID of the State this city
    belongs to (empty string by default).
    name (str): The name of the city (empty string by default).
    """

    state_id: str = ""
    name: str = ""
