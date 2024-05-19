class Student:
    def __init__(self, name, marks):
        self.name = name
        if len(marks) != 5:
            raise ValueError("Marks should be of length 5")
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def ShowResult(self):
        percentage = sum(self.marks) / 5
        if percentage >= 90:
            print("Grade: A")
        elif percentage >= 80:
            print("Grade: B")
        elif percentage >= 70:
            print("Grade: C")
        elif percentage >= 60:
            print("Grade: D")
        else:
            print("Grade: F")

        print(f"Percentage: {percentage}%")


if __name__ == '__main__':
    NumOfStudents = int(input("Enter the number of students: "))
    students = []
    sublist = ['Physics', 'Chemistry', 'Maths', 'Biology', 'Computer']
    for i in range(NumOfStudents):
        name = input("Enter the name of the student: ")
        marks = []
        for subject in sublist:
            marks.append(int(input(f"Enter the marks of {subject}: ")))
        students.append(Student(name, marks))

    for student in students:
            student.display_info()
            student.ShowResult()
            print()
