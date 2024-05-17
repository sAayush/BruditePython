class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


if __name__ == '__main__':
    emp1 = Employee("Aayush Soni", 20, 20000)
    emp2 = Employee("Bhinsar", 21, 30000)
    emp1.display_info()
    emp2.display_info()
