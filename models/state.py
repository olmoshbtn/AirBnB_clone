#!/usr/bin/python3
"""This module writes a class state that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class creation"""

    # Public class attributes
    name = ""
