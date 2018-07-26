#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Intializes testing instance
        '''
        cls.rev = Review()
        cls.rev.place_id = "3"
        cls.rev.user_id = "10"
        cls.rev.text = "text text text"

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.rev, BaseModel)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        self.assertTrue("place_id" in self.rev.__dir__())
        self.assertTrue("user_id" in self.rev.__dir__())
        self.assertTrue("text" in self.rev.__dir__())

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        place_id = getattr(self.rev, "place_id")
        user_id = getattr(self.rev, "user_id")
        text = getattr(self.rev, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
