#!/usr/bin/python3
from models.base_model import BaseModel
"""This module supplies the Review class.
"""


class Review(BaseModel):
    """Represents a Review entity.

    Attributes:
    place_id (str): The ID of the Place the review is
    for (empty string by default).
    user_id (str): The ID of the User who wrote the review
    (empty string by default).
    text (str): The text content of the review
    (empty string by default).
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
