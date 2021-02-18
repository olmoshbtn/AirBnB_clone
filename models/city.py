#!/usr/bin/python3
"""This module writes a class city that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class creation"""

    # Public class attributes
    state_id = ""
    name = ""
