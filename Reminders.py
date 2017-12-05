import redis
import threading
from Server import get_due_date,get_assign_name

class Reminders():

    def __init__(self,product_db):
        self.r = redis.Redis()

    def new_canvas_reminder(self,course_code,assign_id):
        if self.r.get(assign_id)== None:
            print("Please enter a valid 4-digit class code")
        elif self.r.get(assign_id)== None:
            print("Status code entered is not a class you are authorized to access")
        elif self.r.get(course_code)== None:
            print("Please enter a valid 4-digit class code")
        elif self.r.get(course_code)== None:
            print("Status code entered is not a class you are authorized to access")
        else:
            if self.r.get(assign_id) != self.r.keys():
                self.r.set(get_assign_name(course_code,assign_id), get_due_date(course_code,assign_id))
            else:
                print("This assignment already has a reminder.")

    def new_user_reminder(self,assignment_name,class_name,due_date):
        self.r.set(assignment_name,due_date)

    def delete_canvas_reminder(self,course_code,assign_id):
        self.r.delete(get_assign_name(course_code,assign_id))

    def list_reminders(self):
        list = []
        for ass in self.r.keys():
            real_ass = ass.decode()
            list.append(real_ass)
        return list

    def get_product_list(self):
        return self.r.keys()

    def delete_all_reminders(self):
        self.r.flushdb()

r = Reminders({})
