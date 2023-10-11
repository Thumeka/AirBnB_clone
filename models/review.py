#!/usr/bin/python3
"""Class that inherit from BaseModel"""
from models.base_models import BaseModel


class Review(BaseModel):
    """Review class"""

    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
