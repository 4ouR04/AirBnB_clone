#!/usr/bin/python3
"""Test File Storage"""
import unittest
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """unit test"""
    def test_doc1(self):
        """test docstring for module"""
        res = "Module has no documentation"
        self.assertIsNotNone(models.engine.file_storage.__doc__, res)

    def test_doc2(self):
        """test docstring for class"""
        res = "Class has no documentation"
        doc = FileStorage.__doc__
        self.assertIsNotNone(doc, res)

    def test_doc3(self):
        """test documentation for methods"""
        res = "all method has no documentation"
        func = FileStorage.all.__doc__
        self.assertIsNotNone(func, res)

        res = "new method has no documentation"
        function = FileStorage.new.__doc__
        self.assertIsNotNone(function, res)

        res = "save method has no documentation"
        function = FileStorage.save.__doc__
        self.assertIsNotNone(function, res)

        res = "reload method has no documentation"
        function = FileStorage.reload.__doc__
        self.assertIsNotNone(function, res)

    def test_file4(self):
        """test the file permissions"""
        path = 'tests/test_models/test_engine/test_file_storage.py'
        is_readable = os.access(path, os.R_OK)
        self.assertTrue(is_readable)

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable)

        is_writable = os.access(path, os.W_OK)
        self.assertTrue(is_writable)

    def test_file5(self):
        """test the file permissions"""
        path = 'models/engine/file_storage.py'
        is_readable = os.access(path, os.R_OK)
        self.assertTrue(is_readable)

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable)

        is_writable = os.access(path, os.W_OK)
        self.assertTrue(is_writable)

    def test_instance1(self):
        """test instance"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    @classmethod
    def setUps(s):
        """set up for test"""
        s.user = User()
        s.user.first_name = "Yos"
        s.user.last_name = "Kal"
        s.user.email = "yoo@gmail.com"
        s.storage = FileStorage()
        s.path = "file.json"


if __name__ == "__main__":
    unittest.main()
