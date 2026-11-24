from p4 import *

students = {
    "Ali": [20, 15, 17, 18],
    "Sara": [9, 8, 12, 7],
}

name = input("Enter student name: ")

if name in students:
    grades = students[name]
    average = avg(grades)

    print("student:", name)
    print("Avg =", average)
    print("max =", max_grade(grades))
    print("status =", check_status(average))
else:
    print("Student not found!")