#!/usr/bin/env python
""" Defines unitests for models/base_model.py

UnitTest classes:
    TestBaseModel

"""
import unittest
from models.base_model import BaseModel
import datetime
from uuid import UUID
from time import sleep

class TestBaseModel(unittest.TestCase):

    def test_moduleDocs(self):
        moduleDoc = __import__("models.base_model").base_model.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        classDoc = __import__("models.base_model").base_model.BaseModel.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_saveDocs(self):
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_to_dictDocs(self):
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.to_dict.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test__str__Docs(self):
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.__str__.__doc__)
        self.assertGreater(len(methodDoc), 0)
 
    def test_str(self):
        obj1 = BaseModel()
        obj1_str = obj1.__str__
        expect_str = "[BaseModel] ({}) {}".format(obj1.id, obj1.__dict__)
        self.assertEqual(expect_str, obj1_str)
    
    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))
    
    def test_validId(self):
        obj1 = BaseModel()
        value = UUID(obj1.id)
        self.assertIs(type(value), UUID)
    
    def test_uniqueId(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        
    def test_created_at_type(self):
        obj1 = BaseModel()
        self.assertIs(type(obj1.created_at), datetime)

    def test_updated_at_type(self):
        obj1 = BaseModel()
        self.assertIs(type(obj1.updated_at), datetime)

    def test_created_at_time_difference_not_equal(self):
        obj1 = BaseModel()
        sleep(5)
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)
    
    def test_updated_at_time_difference_not_equal(self):
        obj1 = BaseModel()
        sleep(5)
        obj2 = BaseModel()
        self.assertLess(obj1.updated_at, obj2.updated_at)
    
    def test_save(self):
        obj1 = BaseModel()
        sleep(5)
        first_update = obj1.updated_at
        obj1.save()
        self.assertLess(first_update, obj1.updated_at)
    
    def test_dict_type(self):
        obj1 = BaseModel()
        self.assertTrue(dict, type(obj1.to_dict()))

    def test_dict_has_keys(self):
        obj1 = BaseModel()
        self.assertIn("id", obj1.to_dict())
        self.asssetIn("created_at", obj1.to_dict())
        self.assertIn("updated_at", obj1.to_dict())
        self.assertIn("__class__", obj1.to_dict())
    
    def test_dict_attributes(self):
        datetime_obj = datetime.today()
        obj1 = BaseModel()
        obj1.id = "789456"
        obj1.created_at = obj1.updated_at = datetime_obj
        test_dict = {
            'id': '789456',
            '__class__': 'BaseModel',
            'created_at': datetime_obj.isoformat(),
            'updated_at': datetime_obj.isoformat()
        }
        self.assertDictEqual(obj1.to_dict(), test_dict)
        
    def test_with_kwargs(self):
        obj1 = BaseModel()
        test_dict = obj1.to_dict()

        created_at = datetime.fromisoformat(test_dict["created_at"])
        updated_at = datetime.fromisoformat(test_dict["updated_at"])

        self.assertIn("created_at", test_dict)
        self.assertIn("updated_at", test_dict)
        self.assertIn("id", test_dict)

        self.assertIs(type(test_dict["created_at"]), str)
        self.assertIs(type(test_dict["updated_at"]), str)
        self.assertIs(type(test_dict["id"]), str)

        self.assertEqual(test_dict["created_at"], created_at.isoformat())
        self.assertEqual(test_dict["updated_at"], updated_at.isoformat())
        