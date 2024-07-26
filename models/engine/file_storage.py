#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone.
"""
import json


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    @property
    def cities(self):
        """
        Prints the cities in the state.
        """

    def delete(self, obj=None):
        """
        Compares eachvalue of key with
        cls arguments with its object.
        """
        if obj:
            id = obj.to_dict()["id"]
            clsName = obj.to_dict()["__class__"]
            keyName = clsName+"."+id
            if keyName in FileStorage.__objects:
                del (FileStorage.__objects[keyName])
                self.save()

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        print_dict = {}
        if cls:
            clsName = cls.__name__
            for a, b in FileStorage.__objects.items():
                if a.split('.')[0] == clsName:
                    print_dict[a] = b
            return print_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary.
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        Saves storage dictionary to file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """
        Loads storage dictionary from file.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Closes the storage.
        """
        self.reload()
