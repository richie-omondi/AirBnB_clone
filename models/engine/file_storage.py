#!/usr/bin/env python
"""Defines the FileStorage class"""

import json
from json import loads, dumps
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file
        and deserializes a JSON file to an instance

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class_name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict = {
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        json_string = dumps(dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects dictionary, 
        if the file path exists
        """
        allowed_classes = ["BaseModel", "User", "State",
                           "City", "Place", "Amenity", "Review"]
        file_name = FileStorage.__file_path
        if isfile(file_name):
            with open(file_name, "r") as f:
                json_string = f.read()
                json_load = loads(json_string)
            for key, value in json_load.items():
                class_name, obj_id = key.split(".")
                if class_name in allowed_classes:
                    eval("self.new({}(**value))".format(class_name))