#!/usr/bin/python3
"""unique FileStorage instance"""

from models.engine import file_storage

storage = FileStorage()
storage.reload()