#|Maddison Montijo  Assignment 8.2 

import json
from os import path

studentfile = 'Student.json'
student_list = []

#Check if file exists
if path.isfile(studentfile) is False:
    raise Exception("File does not exist")

#Read JSON file
with open(studentfile) as sf:
    student_list = json.load(sf)

    for student in student_list:
        print(student['F_Name'], student['L_Name'], student['Student_ID'], student['Email'])
    else:
        print("This is the original student list.")    

# Verifying existing List
print(student_list)
print(type(student_list))

student_list.append({
    "F_Name": "Maddison",
    "L_Name": "Montijo",
    "Student_ID": 45714,
    "Email": "mmontijo@gmail.com"
    
})

#Verifying new List
print(student_list)
print(type(student_list))

#Write JSON file
with open(studentfile, 'w') as sf:
    json.dump(student_list, sf)

print("This is the new student list.")

