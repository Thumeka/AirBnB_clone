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


class FileStorage:
    """Serialize and deserialize json files"""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path"""

        new_dict = {}

        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    load_data = json.load(f)
                    for key, obj_data in load_data.items():
                        class_name = obj_data.get("__class__")
                        if class_name in globals():
                            obj_class = globals()[class_name]
                            obj = obj_class(**obj_data)
                            FileStorage.__objects[key] = obj
                except Exception:
                    pass
