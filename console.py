#!/usr/bin/python3
"""Console Module to implement command interpreter"""

import cmd
import json

#import models
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

#storage system in the model init file
from models import storage


class HBNBCOMMAND(cmd.Cmd):
    """Implement quit and EOF, create, destroy etc."""

    classes = [Amenity, BaseModel, City, Place, Review, State, User]
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exits console"""
        return True

    def do_EOF(self, arg):
        """Exits console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
