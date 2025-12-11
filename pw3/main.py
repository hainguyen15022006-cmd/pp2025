import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.sid = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  
        self.gpa = 0
    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark
class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
def input_student():
    n= int(input("Number of students: "))
    students=[]

    for _ in range(n):
        sid=input("Student id: ")
        name=input("Student name: ")
        dob= input("Date of birth: ")
        students.append(Student(sid,name,dob))
    return students

def input_course():
    c= int(input("Enter courses: "))
    courses=[]
    for _ in range(c):
        cid= input("Course id: ")
        name= input("Name course: ")
        cre= input("Credit: ")
        courses.append(Course(cid,name,cre))
    return courses

def input_marks(students,courses):
    course_id= input("Course id: ")
    course_ids = [c.course_id for c in courses]
    if course_id not in course_ids:
        print("Please try again\n ")
        return
    else:
        print(f"Please enter mark for course {course_id}")

    for st in students:
        raw = float(input(f"Mark for {st.name}: "))
        mark = math.floor(raw * 10) / 10
        st.add_mark(course_id, mark)
def calculateGPA(students, courses):
    for st in students:
        marks = []
        weights = []
        for c in courses:
            if c.course_id in st.marks:     
                marks.append(st.marks[c.course_id])
                weights.append(c.credits)
        if len(marks) == 0:
            st.gpa = 0
            continue
        marks = np.array(marks)
        weights = np.array(weights)
        st.gpa = round(np.average(marks, weights=weights), 2)

def sort_students_by_gpa(students):
    students.sort(key=lambda s: s.gpa, reverse=True)

def show_students(students):
    print("--Student List--")
    for st in students:
        print(f"{st.student_id} - {st.name} - {st.dob}")
def show_courses(courses):
    print("\n--Course List--")
    for c in courses:
        print(f"{c.course_id} - {c.name} ({c.cre} credits)")
def show_gpa(students):
    print("\n---Student GPA---")
    for st in students:
        print(f"{st.name}: GPA = {st.gpa}")

def main():
    students =[]
    courses =[]
    while True:
        print("-Menu-")
        print("1.Input students")
        print("2.Input courses")
        print("3.Input marks")
        print("4.Calculate GPA")
        print("5.Sort by GPA")
        print("6.Show students")
        print("7.Show courses")
        print("8.Show GPA")
        print("0.Exit")
        choice = input("Choose: ")
        if choice == "1":
            students=input_student()
        elif choice== "2":
            courses = input_course()
        elif choice =="3":
            input_marks(students, courses)
        elif choice =="4":
            calculateGPA(students, courses)
        elif choice=="5":
            sort_students_by_gpa(students)
        elif choice== "6":
            show_students(students)
        elif choice =="7":
            show_courses(courses)
        elif choice=="8":
            show_gpa(students)
        elif choice=="0":
            print("End")
            break
        else:
            print("Invalid")








