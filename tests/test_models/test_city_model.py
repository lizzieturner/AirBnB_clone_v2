#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''
    def test_class_docs(self):
        '''
           Test class documentation
        '''
        self.assertTrue(len(City.__doc__) > 0)

    @classmethod
    def setUpClass(cls):
        '''
            Initializing testing instance
        '''
        cls.new_city = City()
        cls.new_city.state_id = "5"
        cls.new_city.name = "San Francisco"

    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_User_attributes(self):
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name" in self.new_city.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "state_id")
        self.assertIsInstance(name, str)
