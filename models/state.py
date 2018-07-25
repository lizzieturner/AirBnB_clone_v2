#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel):
    '''
        Implementation for the State.
    '''
    _tablename_ = 'states'
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        '''
            Returns all cities in a State
        '''
        city_list = models.storage.all("City").values()
        return [city for city in city_list if city.state_id == self.id]
