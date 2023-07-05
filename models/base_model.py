#!/usr/bin/python3
"""Class BaseModel that defines all common
attributes/methods for other classes"""


import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel."""

    def __init__(self):
        """Public instance attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ returns the string representation of the obj """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all instance attributes and their
        values, including the attributes created_at and updated_at attributes
        converted to ISO format"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
