import redis
import threading
from Server import get_due_date

class Reminders():

    def __init__(self,product_db):
        self.r = redis.Redis()
        self.r.flushdb()

    def new_canvas_reminder(self,course_code,assign_id):
        self.r.set(assign_id, get_due_date(course_code,assign_id))

    def new_user_reminder(self,assignment_name,class_name,due_date):
        self.r.set(assignment_name,due_date)

    def get_product_list(self):
        print(self.r.keys())
        return self.r.keys()