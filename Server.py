from flask import Flask, jsonify
import requests
import os
import json
import time


app= Flask(__name__)


canvas_api=os.environ['CANVAS_KEY']

@app.route('/')
def index():

        base_url='https://canvas.moravian.edu/api/v1/users/self/courses/5522/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        r= requests.get(base_url,headers=headers)
        data= r.json()

        return jsonify(data)


if __name__=='__main__':

    app.run(debug=True)




def list_assignment(course_code):
        base_url = 'https://canvas.moravian.edu/api/v1/users/self/courses/'+course_code+'/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        response = requests.get(base_url, headers=headers)

        if response.status_code == 404:
            print("Please enter a valid 4-digit class code")
        elif response.status_code == 401:
            print("Status code entered is not a class you are authorized to access")
        else:
            response.raise_for_status()
            data= json.loads(response.text)
            for homework in data :
                if homework['due_at']!='None':
                    print(homework['name'],homework['id'],homework['due_at'])
            return data

def get_due_date(course_code,assign_id):
    base_url = 'https://canvas.moravian.edu/api/v1/courses/' + course_code + '/assignments/' + assign_id
    headers = {"Authorization": "Bearer " + canvas_api}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return (data['due_at'])


def add_assignment(assign_id):
    return 0

list_assignment('5522')
