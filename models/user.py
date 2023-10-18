#!/usr/bin/python3
"""Class user that inherints from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User: manages user object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
