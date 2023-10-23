#!/usr/bin/python3
"""__City Module__"""

from models.base_model import BaseModel

class City(BaseModel):
    """__class City__"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
