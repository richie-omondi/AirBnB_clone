#!/usr/bin/env python
"""Defines the FileStorage class"""

import json

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
        """Return the __objects dictionary"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class_name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict_1 = FileStorage.__objects
        obj_dict_2 = {obj: obj_dict_1[obj].to_dict() for obj in obj_dict_1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict_2, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects dictionary, if the file path exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return