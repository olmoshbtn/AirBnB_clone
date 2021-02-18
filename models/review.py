#!/usr/bin/python3
"""This module writes a class review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class creation"""

    # Public class attributes
    place_id = ""
    user_id = ""
    text = ""
