#!/usr/bin/python3
"""Module containing the BaseModel class."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class for creating instances with common attributes/methods.

    Public instance attributes:
    - id: string - assign with a uuid when an instance is created
    - created_at: datetime - assign with the current datetime when
    an instance is created
    - updated_at: datetime - assign with the current datetime when
    an instance is created and updated when modified

    Public instance methods:
    - save(self): updates the public instance attribute updated_at
    with the current datetime
    - to_dict(self): returns a dictionary containing all keys/values
    of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
        - *args: Not used
        - **kwargs: Dictionary of attributes to initialize the instance with.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

#        if kwargs:
#           dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
#            for key, value in kwargs.items():
#                if key == '__class__':
#                    continue
#                elif key == 'created_at':
#                    self.created_at = datetime.strptime(
#                        kwargs['created_at'], dtime_format)
#                elif key == 'updated_at':
#                    self.updated_at = datetime.strptime(
#                        kwargs['updated_at'], dtime_format)
#                else:
#                    setattr(self, key, value)
#        else:
#            self.id = str(uuid.uuid4())
#            self.created_at = datetime.now()
#            self.updated_at = datetime.now()
#           models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
