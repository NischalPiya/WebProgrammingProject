import redis
import threading
from Server import get_due_date
class reminders:

    def __init__(self, inventory):
        r = redis.Redis()
        self.lock = threading.RLock()

    def new_canvas_reminder(self,course_code,assign_id):
        self.r.set(assign_id, get_due_date(course_code,assign_id))

    def new_user_reminder(self,assignment_name,class_name,due_date):
        self.r.set(assignment_name,class_name,due_date)

    r = redis.Redis()
    r.new_canvas_reminder('5522','25628')
