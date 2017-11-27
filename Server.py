from flask import Flask, jsonify
import requests
import os

app= Flask(__name__)

import time
start_time=time.time()
canvas_api=os.environ['CANVAS_KEY']
while True:
    @app.route('/')
    def index():

        base_url='https://canvas.moravian.edu/api/v1/users/self/courses/5519/assignments'
        headers = {"Authorization": "Bearer " + canvas_api}
        r= requests.get(base_url,headers=headers)
        data= r.json()

        return jsonify(data)


    if __name__=='__main__':

        app.run(debug=True)

    time.sleep(60.0 - ((time.time() - start_time) % 60.0))




