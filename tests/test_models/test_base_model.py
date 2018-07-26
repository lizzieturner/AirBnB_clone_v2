#!/usr/bin/python3

'''
    All the test for the base_model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime
import os


class TestBase(unittest.TestCase):
    '''
        Testing the base class model.
    '''

    def test_class_doc(self):
        '''
            Test class documentation
        '''
        self.assertTrue(len(BaseModel.__doc__) > 0)

    @classmethod
    def setUpClass(cls):
        '''
            Initializing instance.
        '''
        cls.bsmdl = BaseModel()
        cls.bsmdl.name = "Lizzie"

    def test_ids_differ(self):
        '''
            Checks that the ids between two instances are different.
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.bsmdl.id)

    def test_name(self):
        '''
            Checks that an attribute can be added.
        '''
        self.assertEqual("Lizzie", self.bsmdl.name)

    def test_a_updated_created_equal(self):
        '''
            Checks that both dates are equal.
        '''
        self.assertEqual(self.bsmdl.updated_at.year,
                         self.bsmdl.created_at.year)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "db no good :(")
    def test_save(self):
        '''
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        '''
        self.bsmdl.name = "Not Lizzie"
        self.bsmdl.save()
        self.assertNotEqual(self.bsmdl.created_at, self.bsmdl.updated_at)

    def test_to_dict(self):
        '''
            Checks the to_dict method
        '''
        dict1 = self.bsmdl.to_dict()
        self.assertEqual("<class 'dict'>", str(type(dict1)))

    def test_to_dict_class(self):
        '''
            Checks that the __class__ key exists.
        '''
        newmodel = BaseModel()
        self.assertEqual("BaseModel", (newmodel.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        '''
            Checks the type of the value of updated_at.
        '''
        newmodel = BaseModel()
        self.assertEqual("<class 'str'>",
                         str(type((newmodel.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        '''
            Checks the type of the value of created_at.
        '''
        newmodel = BaseModel()
        tmp = newmodel.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        '''
            Test that an instance is created using the
            key value pair.
        '''
        new_dict = self.bsmdl.to_dict()
        new_model = BaseModel(**new_dict)
        self.assertEqual(new_model.id, self.bsmdl.id)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at
            data type is datetime.
        '''
        bsmdl_dict = self.bsmdl.to_dict()
        new_model = BaseModel(bsmdl_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            Test that the new_model's created_at
            data type is datetime.
        '''
        bsmdl_dict = self.bsmdl.to_dict()
        new_model = BaseModel(bsmdl_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        '''
            Test that the new_model's and bsmdl's
            dictionary values are same.
        '''
        model2 = BaseModel()
        dict2 = model2.to_dict()
        new_model = BaseModel(**dict2)
        new_dict = new_model.to_dict()
        self.assertEqual(dict2, new_dict)

    def test_instance_diff(self):
        '''
            Test that the bsmdl and new_model are
            not the same instance.
        '''
        bsmdl_dict = self.bsmdl.to_dict()
        new_model = BaseModel(bsmdl_dict)
        self.assertNotEqual(self.bsmdl, new_model)

    @classmethod
    def tearDownClass(cls):
        '''
            Remove instance
        '''
        del cls.bsmdl
