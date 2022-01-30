#!/usr/bin/python3
"""
    Unit Testing For BaseModel class
"""
from models import BaseModel
import unittest
from unittest import mock
import inspect
import time
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    """ Testing the Base Class """
    def test_doc1(self):
        """test documentation for module"""
        res = "Module has no documenation"
        self.assertIsNotNone(models.base_model.__doc__, res)

    def test_doc2(self):
        """test documentation for class"""
        res = "Module has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__doc__, res)

    def test_doc3(self):
        """testing for methods"""
        res = "method init has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__init__.__doc__, res)
        res1 = "method __str__ has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__, res1)
        res2 = "method save has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__, res2)
        res3 = "method to_dict has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__, res3)

    def test_str(self):
        """
            test str method
        """
        instance = BaseModel()
        correct_str = "[BaseModel] ({}) {}".format(
                                                    instance.id,
                                                    instance.__dict__
                                                        )
        self.assertEqual(correct_str, str(instance))

    def to_dict_value(self):
        """
            test return value of dict
        """
        ti = "%Y-%m-%dT%H:%M:%S.%f"
        inst = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
        self.assertEqual(type(dict_base["created_at"]), str)
        self.assertEqual(type(dict_base["updated_at"]), str)
        self.assertEqual(
                            dict_base["created_at"],
                            inst.created_at.strftime(ti)
                                    )
        self.assertEqual(
                            dict_base["updated_at"],
                            inst.updated_at.strftime(ti)
                                    )

    def test_to_dict(self):
        """
            test to dic method
        """
        inst = BaseModel()
        inst.name = "kal"
        dict_inst = inst.to_dict()
        attr = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"]
        self.assertCountEqual(dict_inst.keys(), attr)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')
        self.assertEqual(dict_inst['name'], "kal")

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """
            test save and update
        """
        instance = BaseModel()
        old_value_created = instance.created_at
        old_value_update = instance.updated_at
        instance.save()
        new_value_created = instance.created_at
        new_value_updated = instance.updated_at
        self.assertNotEqual(old_value_update, new_value_updated)
        self.assertEqual(old_value_created, new_value_created)
        self.assertTrue(mock_storage.save.called)
