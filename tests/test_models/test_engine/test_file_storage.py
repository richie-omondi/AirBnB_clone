#!/usr/bin/env python
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_docs
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
from models.engine.file_storage import FileStorage
import models
from uuid import UUID
from datetime import datetime


class TestFileStorage_docs(unittest.TestCase):
    """ Unit tests for testing documentation in class FileStorage"""

    def test_moduleDocs(self):
        """ Test whether the module has documentation"""
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """ Test whether the class has documentation"""
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        """ Test whether the save() method has documentation"""
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)
    
    def test_methodDocsAll(self):
        """ Test whether the all() method has documentation"""
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.all.__doc__)
        self.assertGreater(len(methodDoc), 0)
    
    def test_methodDocsNew(self):
        """ Test whether the new() method has documentation"""
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.new.__doc__)
        self.assertGreater(len(methodDoc), 0)
    
    def test_methodDocsReload(self):
        """ Test whether the reload() method has documentation"""
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.reload.__doc__)
        self.assertGreater(len(methodDoc), 0)

class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_with_no_arguments(self):
        """ Test whether the class FileStorage is instantiated with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arguments(self):
        """ Test whether the class FileStorage is  instantiated with arguments"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """ Test whether __file_path is a private string"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """ Test whether the __objects dictionary is private"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class """

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

if __name__ == "__main__":
    unittest.main()