#!/usr/bin/python3
from models.base_model import BaseModel
"""This module supplies the Place class.
"""


class Place(BaseModel):
    """Represents a Place entity.

    Attributes:
        city_id (str): The ID of the City this
        place belongs to (empty string by default).
        user_id (str): The ID of the User who owns the
        place (empty string by default).
        name (str): The name of the place (empty string by default).
        description (str): A description of the place (empty string
        by default).
        number_rooms (int): The number of rooms in the place (0 by default).
        number_bathrooms (int): The number of bathrooms in the place
        (0 by default).
        max_guest (int): The maximum number of guests allowed
        in the place (0 by default).
        price_by_night (int): The price per night for the
        place (0 by default).
        latitude (float): The latitude coordinate of the
        place (0.0 by default).
        longitude (float): The longitude coordinate of the
        place (0.0 by default).
        amenity_ids (list[str]): A list of Amenity IDs associated
        with the place (empty list by default).
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list[str] = []
