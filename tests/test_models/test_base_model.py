#!/usr/bin/python3

'''
    All the test for the base_model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestDocsAndStyle(unittest.TestCase):
    '''
        Test documentation and formatting
    '''
    def test_class_doc(self):
        '''
            Check documentation
        '''
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_pep8(self):
        '''
           Test pep8 conformity
        '''
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    '''
        Testing the base class model.
    '''

    def setUp(self):
        '''
            Initialize instance
        '''
        self.my_model = BaseModel
        self.my_model.name = "Test Model"

    @classmethod
    def setUpClass(cls):
        '''
            Initializing instance.
        '''
        cls.base1 = BaseModel
        cls.base1.name = "Lizzie"
        cls.base1.id = 5

    def test_id_type(self):
        '''
            Checks that the type of the id is string.
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        '''
            Checks that the ids between two instances are different.
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        '''
            Checks that an attribute can be added.
        '''
        self.assertEqual("Test Model", self.my_model.name)

    def test_a_updated_created_equal(self):
        '''
            Checks that both dates are equal.
        '''
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db")
    def test_save(self):
        '''
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        '''
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_str_overide(self):
        '''
            Checks that the right message gets printed.
        '''
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict(self):
        '''
            Checks the to_dict method
        '''
        dict1 = self.base1.todict()
        self.assertEqual("<class 'dict'>", str(type(dict1)))
        self.assertIsInstance(dict1['created at'], str)

    def test_to_dict_class(self):
        '''
            Checks that the __class__ key exists.
        '''

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        '''
            Checks the type of the value of updated_at.
        '''
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        '''
            Checks the type of the value of created_at.
        '''
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        '''
            Test that an instance is created using the
            key value pair.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            Test that the new_model's created_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        '''
            Test that the new_model's and my_model's
            dictionary values are same.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance_diff(self):
        '''
            Test that the my_model and new_model are
            not the same instance.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)

    @classmethod
    def tearDownClass(cls):
        '''
            Remove instance
        '''
        del cls.base1
