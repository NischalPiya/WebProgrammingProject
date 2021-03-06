from Reminders import r
from RemindersApi import list_courses,list_assignment
import time

import time
import datetime

print ("                                              Current date and time: " , datetime.datetime.now())
print("")
print("      *** Canvas Reminders Application ***")

user_response = " "
while True:

    while(user_response != "7"):
        print("\nWhat would you like to do?")
        print("1. List all of your courses")
        print("2. List all assignments for a specific course")
        print("3. Add a new reminder")
        print("4. Remove a reminder")
        print("5. List all my reminders")
        print("6. Delete all my reminders")
        print("7. Quit")
        print("")
        user_response = input("Print the number of the action you would like to perform: ")

        if user_response == "1":
            list_courses()
        elif user_response == "2":
            course_code = input("\nEnter the course code for the class: ")
            list_assignment(course_code)
        elif user_response == "3":
            new_list=[]
            checker = 0
            course_code = input("\nEnter the course code for the class: ")
            assign_id = input("\nEnter the assignment code for the class: ")
            checker = r.new_canvas_reminder(course_code,assign_id)
            if checker == 1:
                print("->"+str(r.list_reminders()).strip('[]'))

        elif user_response=="4":
            new_list = []
            course_code = input("\nEnter the course code for the class: ")
            assign_id = input("\nEnter the assignment code for the class: ")
            checker = 0
            checker = r.delete_canvas_reminder(course_code, assign_id)
            if checker == 1:
                print("->"+str(r.list_reminders()).strip('[]'))

        elif user_response == "5":
            new_list = []
            r.list_reminders()
            print("->" + str(r.list_reminders()).strip('[]'))

        elif user_response == "6":
            confirm=input("\nAre you sure you want to remove(Y/N)?")
            if(confirm=="y" or confirm=="Y"):
                r.delete_all_reminders()
            else:
                r.list_reminders()

                print("->" + str(r.list_reminders()).strip('[]'))

        elif user_response=="7":
            break
        else:
            print("Enter a valid number")
        time.sleep(1.0)

    break