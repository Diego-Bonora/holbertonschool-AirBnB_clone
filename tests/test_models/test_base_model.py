#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests for BaseModel Class"""

    def test_create_class(self):
        """ Tests if the class was created correctly """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_id_instance(self):
        """ Tests if id is str """
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_created_at_instance(self):
        """ Tests if created_at is datetime"""
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    def test_updated_at_instance(self):
        """ Tests if updated_at is datetime"""
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)

    def test_save(self):
        """ Test save method """
        b1 = BaseModel()
        old_datetime = b1.updated_at
        b1.save()
        new_datetime = b1.updated_at
        self.assertNotEqual(old_datetime, new_datetime)

    def test_to_dict(self):
        """ Test to_dict method """
        b1 = BaseModel()
        new_dict = b1.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        """ Test to_dict returns all correct """
        b1 = BaseModel()
        result = b1.to_dict()
        self.assertIn("id", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)

    def test_str(self):
        """ Test the str representation """
        b1 = BaseModel()
        str_rep = str(b1)
        self.assertIn(b1.__class__.__name__, str_rep)
        self.assertIn(b1.id, str_rep)


if __name__ == "__main__":
    unittest.main()
