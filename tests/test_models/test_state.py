#!/bin/usr/python3
"""Test State"""

import unittest
from models.base_model import BaseModel
from models.state import State
from pep8 import StyleGuide


class TestState(unittest.TestCase):
    """Test state"""

    def test_class(self):
        """Test class"""
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """Test instance"""
        my_state = State()
        self.assertEqual(my_state.name, "")
        self.assertTrue(isinstance(my_state, BaseModel))
