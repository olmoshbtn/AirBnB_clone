#!/usr/bin/python3
"""This module contains 'FilesStorage',
the class which serializes/deserializes to/from JSON"""

import JSON
import models


class FileStorage:
	"""serializes instances to a JSON file, deserializes 
		the JSON file into instances
	"""

    	# string - path to the JSON file
    	__file_path = "file.json"
    	# dictionary - empty but will store all objects by <class name>.id
    	__objects = {}

    	def all(self):
        	"""returns the dictionary __objects
        	"""
        	return self.__objects

	def new(self, obj):
        	"""Sets in __objects the obj with key <obj class name>.id
        	"""
        	key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        	self.__class__.__objects[key] = obj

	def save(self):
        	"""serializes __objects to the JSON file (path: __file_path)
        	"""
        	with open(self.__class__.__file_path, 'w') as ob_file:
        	objects = {key: val.to_dict() for
        			key. val in self.__class__.__objects.items()}
			dump(objects, ob_file)

	def reload(self):
		"""Deserializes the JSON file to __objects (model instance)
		"""
		try:
			with open(self.__file_path, 'r') as in_file:
				objects = load(in_file)
				for key, val in objects.items():
					cls = models.getmodel(key.split(".")[0])
					if cls:
						self.__class__.__objects[key] = cls (**val)
		except FileNotFoundError:
			pass
