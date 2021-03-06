#!/usr/bin/python3
"""Test City"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test City"""

    def test_class(self):
        """Test class"""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """Test instance"""
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")
        self.assertTrue(isinstance(my_city, BaseModel))
