#!/usr/bin/python3
"""Class that inherit from BaseModel"""
from models.base_models import BaseModel


class City(BaseModel):
    """City class"""

    """Public class attributes"""
    state_id = ""
    name = ""
