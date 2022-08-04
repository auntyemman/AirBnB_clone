#!/usr/bin/python3
"""Import the class BaseModel from model.base_model
create a class Review that inherits from the BaseModel"""

from model.base_model import BaseModel
class Review(BaseModel):
    """assign attributes to the class above"""
    
    place_id = ""
    user_id = ""
    text = ""
