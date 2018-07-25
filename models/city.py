#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    _tablename_ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
