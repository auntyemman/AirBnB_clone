#!/usr/bin/python3
#!/usr/bin/python3
"""Import the class BaseModel from model.base_model
create a class Amenity that inherits from the BaseModel"""

from model.base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
