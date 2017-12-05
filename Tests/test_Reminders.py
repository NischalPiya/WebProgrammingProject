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
        r = create_test_db()
        self.assertEqual(0, len(r.get_product_list()))

    def test_new_inventory_one_element(self):
        r = create_test_db()
        r.new_canvas_reminder("5522", "27201")
        self.assertEqual(1, len(r.get_product_list()))

    def test_new_inventory_multiple_elements(self):
        r = create_test_db()
        r.new_canvas_reminder("5522", "27201")
        r.new_canvas_reminder("5522", "25628")
        self.assertEqual(2, len(r.get_product_list()))

    def test_delete_inventory(self):
        r = create_test_db()
        r.new_canvas_reminder('5522', '27201')
        r.delete_canvas_reminder('5522', '27201')
        self.assertEqual(0, len(r.get_product_list()))

    def test_same_reminder_no_duplicates(self):
        r = create_test_db()
        r.new_canvas_reminder('5522', '27201')
        r.new_canvas_reminder('5522', '27201')
        self.assertEqual(1, len(r.get_product_list()))

    def test_list_reminders(self):
        return 0

    def test_delete_empty_reminder(self):
        r=create_test_db()
        r.delete_canvas_reminder('5522','27201')
        self.assertEqual([],r.list_reminders(),'You have no reminders to delete')