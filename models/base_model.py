#!/usr/bin/python3
"""This module provides 'BaseModel' as base class
from which all other models will be created"""

from datetime import datetime
import json
import models
from uuid import uuid4


class BaseModel:
    """Common definition for all models (attributes/methods)"""

    def __init__(self, *args, **kwargs):
        """Initialization method which defines attributes"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__,
            )

    def save(self):
        """This method saves the instance and updates the updated_at time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary containing
        all keys/values of __dict__ of the instance"""

        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
