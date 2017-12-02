import unittest
from unittest import TestCase
import redis

from Server import list_assignment

class TestListAssignments(TestCase):

    def test_assignments_valid_class_code(self):
        assign = list_assignment("5522")
        self.assertEqual(4,len(assign))

    def test_assignments_unauth_class_code(self):
        assign = list_assignment("5511")
        self.assertEqual(None,assign)



if __name__ == '__main__':
    unittest.main()