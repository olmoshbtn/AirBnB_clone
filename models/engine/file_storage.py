#!/usr/bin/python3
""""This module contains 'FileStorage',
the class which serializes/deserializes to/from JSON"""

import json
import models


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes a JSON file to instances"""

    # Private class attributes
    __file_path = "file.json"  # string which is path to the JSON file
    __objects = {}  # empty dictionary to store all objects by <class.name>.id

    # Public instance methods
    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        new__objects = {}
        for key in self.__objects:
            new__objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="UTF8") as file:
            file.write(json.dumps(new__objects))

    def reload(self):
        """deserializes JSON file to __objects"""

        try:
            with open(self.__file_path, "r") as file:
                __objects = json.load(file)
            for key, value in __objects.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass
