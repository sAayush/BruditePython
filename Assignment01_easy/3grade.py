class Student:
    def __init__(self, name, marks):
        self.name = name
        if len(marks) != 5:
            raise ValueError("Marks should be of length 5")
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def calculate_grade(self):
        percentage = sum(self.marks) / 5
        grade = "F"
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        return grade, percentage

    def show_result(self):  # Use lowercase for consistency
        grade, percentage = self.calculate_grade()
        print(f"Grade: {grade}")
        print(f"Percentage: {percentage}%")


if __name__ == '__main__':
    num_students = int(input("Enter the number of students: "))
    students = []
    subjects = ['Physics', 'Chemistry', 'Maths', 'Biology', 'Computer']

    for i in range(num_students):
        name = input("Enter the name of the student: ")
        marks = []
        for subject in subjects:
            marks.append(int(input(f"Enter the marks of {subject}: ")))
        print()
        students.append(Student(name, marks))
        print(students)
    for student in students:
        student.display_info()
        student.show_result()
        print()
