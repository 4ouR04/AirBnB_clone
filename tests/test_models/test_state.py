#!/usr/bin/python3
"""
    Test Case for state Model
"""
from models import BaseModel
from models import State
import unittest
import models


class Teststate(unittest.TestCase):
    """
        unitesst for state class
    """
    def issub_class(self):
        """
            test if state class is sub class of base model
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "update_at"))

    def test_name_attr(self):
        """
            Test that State has attribute name
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
