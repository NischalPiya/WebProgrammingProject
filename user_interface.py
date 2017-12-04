from Reminders import Reminders
from Server import list_courses, list_assignment

print("Canvas Reminders Application")
print("What would you like to do?")
print("1. List all of your courses")

user_response = input("Print the number of the action you would like to perform: ")

if user_response == "1":
    print(list_courses())