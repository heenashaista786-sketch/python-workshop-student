# Day 1 - Python Fundamentals

def input_student():
    student_name = input("enter student name:")
    marks_python = float(input("enter marks for python:"))
    marks_math = float(input("enter marks for mathematics"))
    marks_comm = float(input("enter marks for communication:"))
    dict_student_info = {
        "name":student_name,
        "python_marks":marks_python,
        "math_marks":marks_math,
        "comm_marks":marks_comm,
    }
    #return student_name,marks_pythyon,marks_math,marks_comm
    return dict_student_info
#TODO:
def calculate_percentage(marks_python,marks_math,marks_comm):
    total = (marks_comm+marks_math+marks_python)
    prcentage = (total/300)*100
    return percentage

if __name__ == "__main__":
    print("\n == result --")
    # name,python-m,math_m,comm_m = input_student()
    student_info = input_student()
    print(student_info)
    print("student:",student_info["name"])
    print("percentage", calculate_percentage(
    student_info["python_marks"],
student_info["math_marks"],
student_info["comm_marks"]))

