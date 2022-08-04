#!/usr/bin/python3
"""This module serves as a base class for other classses"""

from datetime import datetime
from uuid import uuid4
from json import JSONEncoder
from models.engine.file_storage import models



date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """Base class"""

    def __init__(self, *args, **kwargs):
        """This class method initializes the class instances for id and date"""
        
        for key in kwargs:
            if key != '__class__':
                if key == 'created_at':
                    date = datetime.strptime(kwargs[created_at], date_format)
                    self.created_at = date
                elif key == 'updated_at':
                    date = datetime.strptime(kwargs[updated_at], date_format)
                    self.updated_at = date
                else:
                    setattr(self, key, kwargs[key])

        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new

    def __str__(self):
        """Return the 'magic' representation of the instance attributes"""

        return " [{}] ({}) {} ".format(self.__class__.__name__, self.id, self.__dir__)

    def save(self):
        """Updates the public instance attribute"""
        
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns dictionary"""

        to_dictionary = self.__dict__.copy
        to_dictionary['__class__'] = self.__class__.__name__
        to_dictionary['created_at'] = created_at.isoformat()
        to_dictionary['updated_at'] = updated_at.isoformat()
        
        return to_dictionary


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, o):
        """ default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
