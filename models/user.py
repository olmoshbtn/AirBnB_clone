#!/usr/bin/python3
"""This module writes a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class creation"""

    # Public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
