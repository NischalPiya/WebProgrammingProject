from flask import Flask, jsonify
import requests
import os
import json
import datetime
import redis

app= Flask(__name__)


canvas_api=os.environ['CANVAS_KEY']

@app.route('/')
def index():
    return("hello")

@app.route('/courses')
def list_courses():
    base_url = 'https://canvas.moravian.edu/api/v1/courses/?per_page=50'
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


@app.route('/list/<course_code>')
def list_assignment(course_code):
        base_url = 'https://canvas.moravian.edu/api/v1/users/self/courses/'+course_code+'/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        response = requests.get(base_url, headers=headers)
        curr_date = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d')
        if response.status_code == 404:
            print("Please enter a valid 4-digit class code")
        elif response.status_code == 401:
            print("Status code entered is not a class you are authorized to access")
        else:
            response.raise_for_status()
            data= json.loads(response.text)
            for homework in data :
                if homework['due_at'] != None:
                    end_date = datetime.datetime.strptime(homework['due_at'][0:10], '%Y-%m-%d')
                    if  end_date > curr_date:
                        print(homework['name'],homework['id'],homework['due_at'])
            return data


def get_due_date(course_code,assign_id):
    base_url = 'https://canvas.moravian.edu/api/v1/courses/' + course_code + '/assignments/' + assign_id
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return (data['due_at'])

def get_assign_name(course_code,assign_id):
    base_url = 'https://canvas.moravian.edu/api/v1/courses/' + course_code + '/assignments/' + assign_id
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return (data['name'])

def add_assignment(assign_id):
    return 0

if __name__=='__main__':
    app.run(debug=True)

