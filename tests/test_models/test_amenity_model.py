#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityDocs(unittest.TestCase):
    '''
        Check for documentation
    '''
    def test_class_doc(self):
        '''
          Check class documentation
        '''
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Initializes testing instance
        '''
        cls.amen = Amenity()
        cls.amen.name = "Wifi"

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        self.assertIsInstance(self.amen, BaseModel)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        self.assertTrue("name" in self.amen.__dir__())

    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        name_value = getattr(self.amen, "name")
        self.assertIsInstance(name_value, str)
