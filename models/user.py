#!/usr/bin/python3
"""User class it inherits from the Basemodel"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """The class"""

    """Attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
