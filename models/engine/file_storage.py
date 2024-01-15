#!/usr/bin/python3
"""Module contain the FileStorage class for serialization/deserialization."""

import json
import os


class FileStorage:
    """
    The FileStorage class for serializing instances to a JSON file
    and deserializing from a JSON file.

    Private class attributes:
    - __file_path: string - path to the JSON file (ex: file.json)
    - __objects: dictionary - empty but will store objects by <class name>.id

    Public instance methods:
    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    - reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        if obj.id in self.__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        save_dict = {
                key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(save_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
