#!/usr/bin/python3

"""
Module: BaseModel
Contains the class BaseModel of the AirBnB Clone
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Represents the base class of the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of the BaseModel instance
        _*args: list of arguements
        _*kwargs: dict of key-value arguements
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of Basemodel Instance
        """
        return "[{}] ({}) {}"
        format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        nw_dct = self.__dict__.copy()
        nw_dct['__class__'] = self.__class__.__name__
        nw_dct['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        nw_dct['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (nw_dct)
