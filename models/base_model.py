#!/usr/bin/python3
"""Define BaseModel Class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel of AirBnB Clone"""

    def __init__(self):
        """Initializes instance of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return f"[{clsname} ({self.id}) {self.__dict__}]"

    def save(self):
        """Updates the instance update_at attricbute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of
        __dict__ of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()
        return obj_dict
