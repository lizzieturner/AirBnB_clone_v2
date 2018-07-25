#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        '''
            Returns all cities in a State
        '''
        return [city for city in State.cities if city.state_id == self.id]
