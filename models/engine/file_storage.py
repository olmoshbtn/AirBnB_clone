#!/usr/bin/python3
""""This module contains 'FilesStorage',
the class which serializes/deserializes to/from JSON"""

import models
import json


class FileStorage:
	"""This class serializes instances to a JSON file
	and deserializes a JSON file to instances"""

Private class attributes
__file_path = string con el path al archivo json
__objects = dictionary con objetos de formato [classname.id]

Public instance methods
all(self) = retorna __objects
new(self, obj) = setea en __objects el obj [classname.id]
save(self) = serialize __objects al archivo json
reload(self) = deserializa el archivo json a __objects (solo si el path de jason existe)

