import unittest
from unittest import TestCase
from Reminders import Reminders

class TestListAssignments(TestCase):
    def test_new_empty_inventory(self):
        r = Reminders({})
        self.assertEqual(0, len(r.get_product_list()))

    def test_new_inventory_one_element(self):
        r = Reminders({})
        r.new_canvas_reminder("5522","27201")
        self.assertEqual(1, len(r.get_product_list()))

    def test_new_inventory_multiple_elements(self):
        r = Reminders({})
        r.new_canvas_reminder("5522","27201")
        r.new_canvas_reminder("5522","25628")
        self.assertEqual(2, len(r.get_product_list()))

    def test_delete_inventory(self):
        r=Reminders({})
        r.new_canvas_reminder('5522','27201')
        r.delete_canvas_reminder('5522','27201')
        self.assertEqual(0,len(r.get_product_list()))