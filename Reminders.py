import redis
import requests
import json
import os
import datetime
canvas_api = os.environ['CANVAS_KEY']


class Reminders():

    def __init__(self,existing_reminders):
        self.r = redis.Redis()



    def new_canvas_reminder(self,course_code,assign_id):
        if len(course_code) == 4 and course_code.isdigit():
            if len(assign_id) == 5 and assign_id.isdigit():
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
            list.append(real_assign+" "+str(self.r.get(real_assign))[2:12])

        return list


    def get_product_list(self):
        return self.r.keys()

    def delete_all_reminders(self):
        self.r.flushdb()


def get_due_date(course_code, assign_id):
    base_url = 'https://canvas.moravian.edu/api/v1/courses/' + course_code + '/assignments/' + assign_id
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return (data['due_at'])

def get_assign_name(course_code, assign_id):
    base_url = 'https://canvas.moravian.edu/api/v1/courses/' + course_code + '/assignments/' + assign_id
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return (data['name'])

def list_courses():
    base_url = 'https://canvas.moravian.edu/api/v1/courses/?per_page=200'
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    curr_date = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d')
    print("Current course as of " + str(curr_date) + "\n")
    for courses in data:
        end_date = datetime.datetime.strptime(courses['end_at'][0:10], '%Y-%m-%d')
        if end_date > curr_date:
            print(courses['name'],courses['id'])

def list_assignment(course_code):
    base_url = 'https://canvas.moravian.edu/api/v1/users/self/courses/' + course_code + '/assignments/?per_page=200'
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    # curr_date = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d')
    if response.status_code == 404:
        print("Please enter a valid 4-digit class code")
    elif response.status_code == 401:
        print("Status code entered is not a class you are authorized to access")
    else:
        response.raise_for_status()
        data = json.loads(response.text)
        for homework in data:
            if homework['due_at'] != None:
                # end_date = datetime.datetime.strptime(homework['due_at'][0:10], '%Y-%m-%d')
                # if  end_date > curr_date:
                print(homework['name'], homework['id'], homework['due_at'])
        return data
r = Reminders({})



