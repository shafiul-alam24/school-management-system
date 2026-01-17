from student import Student
from course import Course
from file_handler import save_student, show_all_students


# Create courses
math = Course("Mathematics")
science = Course("Science")

# Create students
s1 = Student("Rahim", 1, "rahim123")
s2 = Student("Karim", 2, "karim456")

# Enroll & save
s1.enroll_course(math.course_name)
save_student(s1.name, s1.roll, math.course_name)

s2.enroll_course(science.course_name)
save_student(s2.name, s2.roll, science.course_name)

# Encapsulation test
print("Rahim Password:", s1.get_password())

# Read file data
show_all_students()
