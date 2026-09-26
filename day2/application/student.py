class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())
        print("Grade:",self.calculate_grade())

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 85:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 45:
            grade = "C"
        else:
            grade = "D"  
        return grade



if __name__ == "__main__":
    student_obj1 = Student("harry",42,56,23,45)
    student_obj1.display()
    student_obj2 = Student("bhagya",23,34,56,78)
    student_obj2.display()
    student_obj3 = Student("apeksha",12,22,33,55)
    student_obj3.display()
    student_obj4 = Student("ram",22,55,88,77)
    student_obj4.display()
    student_obj5 = Student("lucky",22,77,55,44)
    student_obj5.display()
    
