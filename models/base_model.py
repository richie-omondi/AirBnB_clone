#!usr/bin/env python
""" Defines the BaseModel class"""

from datetime import datetime
import uuid

class BaseModel:
    """ Represents the BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """ Initializes an object """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def save(self):
        """ Update updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return the dictionary format of the BaseModel instance"""
        dict = self.__dict__.copy()
        dict["__created_at__"] = self.created_at.isoformat
        dict["__updated_at__"] = self.updated_at.isoformat
        dict["__class__"] = type(self).__name__

        return dict 

    def __str__(self):
        """ Returns or Prints an official string representation of the class"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
