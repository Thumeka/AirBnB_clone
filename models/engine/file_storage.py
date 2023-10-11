#!/usr/bin/python3
"""a class FileStorage that serializes instances to a JSON file,
and deserializes JSON file to instances"""
import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Serialize and deserialize json files"""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if odj is not None:
            key = '{}.{}'.format(obj.__obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path"""

        new_dict = {}

        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                load_data = json.load(f)
                for key, obj in load_data.items():
                    obj = eval(obj_data["__class__"])(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
