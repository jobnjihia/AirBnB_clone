#!/usr/bin/python3

"""
Module: BaseModel
Contains the class BaseModel of the AirBnB Clone
"""
from datetime import datetime
import uuid


def BaseModel:
    """
    Represents the base class of the AirBnB project
    """
    def __init__(self, *args, *kwargs):
        """
        initialization of the BaseModel instance
        _*args: list of arguements
        _*kwargs: dict of key-value arguements
        """

    def __str__(self):
        """
        Return a string representation of Basemodel Instance
        """
        return "[{}] ({}) {}".
        format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        nw_dct = self.__dict__.copy()
        nw_dct['__class__'] = self.__class__.__name__
        nw_dct['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        nw_dct['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (nw_dct)
