#!/usr/bin/python3
"""This module supplies the storage engine.

"""
import json
import os


class FileStorage:
    """Represents the storage engine.

    __file_path (str): path to the JSON file
    __objects (dict): dictionary to store all objects.

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all objects in dictionary."""
        return self.__objects

    def new(self, obj):
        """Adds new entry to __objects."""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {}
            for key, obj in self.__objects.items():
                json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects only if
        the JSON file exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    self.__objects = json.load(file)
                except json.JSONDecodeError:
                    self.__objects = {}