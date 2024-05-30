#!/usr/bin/python3
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary containing all serialized objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: Instance of a class to be serialized.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)."""
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, "r") as file:
            json_objects = json.load(file)
            for key, obj_dict in json_objects.items():
                class_name = obj_dict["__class__"]
                module_name = "models.user"  # Update to the correct module name
                module = __import__(module_name, fromlist=[class_name])
                class_ = getattr(module, class_name)
                self.__objects[key] = class_(**obj_dict)
