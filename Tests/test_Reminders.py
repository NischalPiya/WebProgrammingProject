import unittest
from unittest import TestCase
import Reminders

class TestListAssignments(TestCase):
    def test_new_empty_inventory(self):
        r = Reminders({})
        self.assertEqual(0, len(r.get_product_list()))
