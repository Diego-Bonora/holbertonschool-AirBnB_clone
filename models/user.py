#!/usr/bin/python3
""" Class User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User with 4 public instances"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
