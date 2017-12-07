import unittest
from unittest import TestCase
from Reminders import Reminders
import redis

def create_test_db():
    test = redis.Redis()
    test.flushdb()
    return Reminders(test)

class TestReminders(TestCase):
    def test_new_empty_inventory(self):
        test = create_test_db()
        self.assertEqual(0, len(test.get_product_list()))

    def test_new_inventory_one_element(self):
        test = create_test_db()
        test.new_canvas_reminder("5522", "27201")
        self.assertEqual(1, len(test.get_product_list()))

    def test_new_inventory_multiple_elements(self):
        test = create_test_db()
        test.new_canvas_reminder("5522", "27201")
        test.new_canvas_reminder("5522", "25628")
        self.assertEqual(2, len(test.get_product_list()))

    def test_delete_inventory(self):
        test = create_test_db()
        test.new_canvas_reminder('5522', '27201')
        test.delete_canvas_reminder('5522', '27201')
        self.assertEqual(0, len(test.get_product_list()))

    def test_same_reminder_no_duplicates(self):
        test = create_test_db()
        test.new_canvas_reminder('5522', '27201')
        test.new_canvas_reminder('5522', '27201')
        self.assertEqual(1, len(test.get_product_list()))

    def test_list_reminders(self):
        test = create_test_db()
        test.new_canvas_reminder("5522", "27201")
        test.new_canvas_reminder("5522", "25628")
        self.assertEqual(len(test.list_reminders()),2)

    def test_delete_empty_reminder(self):
        test=create_test_db()
        test.delete_canvas_reminder('5522','27201')
        self.assertEqual([],test.list_reminders(),'You have no reminders to delete')