class User:

    def __init__(self, first_name, last_name):
        self.Firstname = first_name
        self.Lastname = last_name

    def firstname(self):
        print("Имя ", self.Firstname)

    def lastname(self):
        print("Фамилия ", self.Lastname)

    def full_name(self):
        print("Имя Фамилия ",  f"{self.Firstname} {self.Lastname}")