class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


if __name__ == '__main__':
    car1 = Car("Toyota", "Corolla", 2019)
    car2 = Car("Honda", "Civic", 2020)
    car1.display_info()
    car2.display_info()