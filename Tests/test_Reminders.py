import unittest
from unittest import TestCase
from Reminders import Reminders

class TestListAssignments(TestCase):
    def test_new_empty_inventory(self):
        r = Reminders({})
        self.assertEqual(0, len(r.get_product_list()))

    def test_new_nonempty_inventory(self):
        r = Reminders({})
        r.new_canvas_reminder("5522","27201")

        self.assertEqual(1, len(r.get_product_list()))
