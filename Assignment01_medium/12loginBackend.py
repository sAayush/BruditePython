class User:
    def __init__(self,):
        self.username = ''
        self.password = ''
        self.confirm_password = ''

    def login(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        attempts = 3
        while attempts > 0:
            confirm_password = input("Confirm password: ")
            if self.password == confirm_password:
                print("Login successful")
                break
            else:
                attempts -= 1
                print(f"Password doesn't match. {attempts} attempts left")


if __name__ == '__main__':
    user = User()
    user.login()
