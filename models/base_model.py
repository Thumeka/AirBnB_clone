#!/usr/bin/python3
"""Define BaseModel Class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represents BaseModel of AirBnB Clone"""

    def __init__(self, *args, **kwargs):
        """Initializes instance of BaseModel"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], tformat)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return f"[{clsname}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the instance update_at attribute"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/values of
        __dict__ of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
