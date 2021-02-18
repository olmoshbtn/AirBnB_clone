#!/usr/bin/python3
"""This module writes a class amenity that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class creation"""

    # Public class attributes
    name = ""
