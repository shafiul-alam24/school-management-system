class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.courses = []
        self.__password = password

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def get_password(self):
        return self.__password
