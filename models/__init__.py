#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import models.engine.db_storage
from os import getenv

StorageType = getenv('HBNB_TYPE_STORAGE')
if StorageType == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
