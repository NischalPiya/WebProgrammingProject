import redis
import os
canvas_api = os.environ['CANVAS_KEY']
from RemindersApi import get_assign_name, get_due_date

class Reminders():

    def __init__(self,existing_reminders):
        self.r = redis.Redis()

    def new_canvas_reminder(self,course_code,assign_id):
        if len(course_code) == 4 and course_code.isdigit():
            if len(assign_id) == 5 and assign_id.isdigit():
                if(get_assign_name(course_code,assign_id))!= 0:
                    if self.r.exists(get_assign_name(course_code,assign_id)) == 0:
                        self.r.set(get_assign_name(course_code,assign_id), get_due_date(course_code,assign_id))
                        return 1
                    else:
                        print("This assignment already has a reminder.")

                return 0
            else:
                print("Enter a valid assignment id")
        else:
            print("Enter a valid course code.")

    def delete_canvas_reminder(self,course_code,assign_id):
        if len(course_code) == 4 and course_code.isdigit():
            if len(assign_id) == 5 and assign_id.isdigit():
                if (get_assign_name(course_code, assign_id)) != 0:
                    if self.r.exists(get_assign_name(course_code,assign_id)) == 1:
                        self.r.delete(get_assign_name(course_code,assign_id))
                        return 1
                    else:
                        print('This assignment currently has no reminder')
                        return 0
            else:
                print("Enter a valid assignment id")
        else:
            print("Enter a valid course code.")

    def list_reminders(self):
        list = []
        for assign in self.r.keys():
            real_assign = assign.decode()
            list.append(real_assign+" "+str(self.r.get(real_assign))[2:12])
        return list


    def get_product_list(self):
        return self.r.keys()

    def delete_all_reminders(self):
        self.r.flushdb()

r = Reminders({})


