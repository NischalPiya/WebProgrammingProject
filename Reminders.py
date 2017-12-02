import redis
import threading
from Server import get_due_date,get_assign_name

class Reminders():

    def __init__(self,product_db):
        self.r = redis.Redis()
        self.r.flushdb()

    def new_canvas_reminder(self,course_code,assign_id):
        self.r.set(get_assign_name(course_code,assign_id), get_due_date(course_code,assign_id))

    def new_user_reminder(self,assignment_name,class_name,due_date):
        self.r.set(assignment_name,due_date)


    def delete_canvas_reminder(self,course_code,assign_id):
        self.r.delete(get_assign_name(course_code,assign_id))


    def list_reminders(self):
        print(self.r.keys())

    def get_product_list(self):
        return self.r.keys()