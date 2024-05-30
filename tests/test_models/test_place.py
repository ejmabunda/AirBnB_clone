#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_default_attributes(self):
        # Create an instance of Place with default attributes
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_attributes(self):
        # Create an instance of Place with custom attributes
        custom_city_id = "123"
        custom_user_id = "456"
        custom_name = "Cozy Cabin"
        custom_description = "A charming retreat"
        custom_rooms = 3
        custom_bathrooms = 2
        custom_guests = 6
        custom_price = 150
        custom_latitude = 40.7128
        custom_longitude = -74.0060
        custom_amenities = ["wifi", "pool"]

        place = Place(city_id=custom_city_id, user_id=custom_user_id,
                      name=custom_name, description=custom_description,
                      number_rooms=custom_rooms, number_bathrooms=custom_bathrooms,
                      max_guest=custom_guests, price_by_night=custom_price,
                      latitude=custom_latitude, longitude=custom_longitude,
                      amenity_ids=custom_amenities)

        self.assertEqual(place.city_id, custom_city_id)
        self.assertEqual(place.user_id, custom_user_id)
        self.assertEqual(place.name, custom_name)
        self.assertEqual(place.description, custom_description)
        self.assertEqual(place.number_rooms, custom_rooms)
        self.assertEqual(place.number_bathrooms, custom_bathrooms)
        self.assertEqual(place.max_guest, custom_guests)
        self.assertEqual(place.price_by_night, custom_price)
        self.assertEqual(place.latitude, custom_latitude)
        self.assertEqual(place.longitude, custom_longitude)
        self.assertEqual(place.amenity_ids, custom_amenities)

    def test_attribute_types(self):
        # Ensure that attribute types are correct
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

if __name__ == "__main__":
    unittest.main()
