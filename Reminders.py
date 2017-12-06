import redis
from Server import get_due_date,get_assign_name,list_assignment,get_course_id_assign_id_with_name


class Reminders():

    def __init__(self,existing_reminders):
        self.r = redis.Redis()

    def new_canvas_reminder(self,course_code,assign_id):
        if len(course_code) == 4 & course_code.isdigit():
            if len(assign_id) == 5 & assign_id.isdigit():
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
        self.r.delete(get_assign_name(course_code,assign_id))
        if r.list_reminders()==[]:
            print('You have no reminders to delete')

    def list_reminders(self):
        list = []
        for assign in self.r.keys():

            real_assign = assign.decode()

            list.append(real_assign+str(self.r.get(real_assign)))

        return list


    def get_product_list(self):
        return self.r.keys()

    def delete_all_reminders(self):
        self.r.flushdb()




r=Reminders({})




