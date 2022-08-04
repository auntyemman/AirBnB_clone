#!/usr/bin/pythom3
"""Import the class BaseModel from model.base_model
create a class Place that inherits from the BaseModel"""

from model.base_model import BaseModel
class Place(BaseModel):
    """create a public class attribute from the class above"""
    
    city_id = ""
    user_id = ""
    name = = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
