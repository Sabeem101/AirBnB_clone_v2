#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

        @property
        def cities(self):
            """
            Gets the city class attributes.
            """
            from models import storage
            C_List = []
            C_All = storage.all(city)
            for city in C_All.values():
                if city.state_id == self.id:
                    C_List.append(city)
            return C_List


class State(BaseModel, Base):
    """
    State class.
    """
    __tablename__ = 'states'
    if storage_type = "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""
        # FileStorage DONE: gets city attributes that returns
        # the list of city instances with THE State id.
