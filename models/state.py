#!/usr/bin/python3
from models.base_model import BaseModel
"""This module supplies the State class.
"""


class State(BaseModel):
    """
    Represents a State entity.

    Attributes:
        name (str): The name of the state
        (empty string by default).
    """

    name: str = ""
