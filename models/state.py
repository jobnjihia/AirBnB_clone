#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    All attrbutes should be empty
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes State
        """
        super().__init__(*args, **kwargs)
