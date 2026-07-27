class Student:

    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")

s = Student()

del s