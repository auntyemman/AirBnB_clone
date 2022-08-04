#!/usr/bin/python3
"""Import the class BaseModel from model.base_model
create a class State that inherits from the BaseModel"""

from model.base_model import BaseModel
class State(BaseModel):
    """state class inherited from BaseModel"""
    
    name = ""
