#!/usr/bin/python3
"""
file_storage
serializes python objects into json objects
deserializes json objects to python objects
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    FileStorage class:
    attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - store all objects by <class name>.id

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets new object (obj) into __objects
        the obj with key <obj class name>.id
        Variables:       
        key [str] -- key format generated.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).
        Variables:
        ----------
        nw_dct [dict] -- keys and values to build JSON.
        """
        nw_dct = {}
        for key, value in FileStorage.__objects.items():
            nw_dct[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(nw_dct, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                nw_dct = json.load(my_file)

            for key, value in nw_dct.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
