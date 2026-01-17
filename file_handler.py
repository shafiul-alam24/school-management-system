def save_student(name, roll, course):
    with open("students.txt", "a") as file:
        file.write(f"Name: {name}, Roll: {roll}, Course: {course}\n")


def show_all_students():
    try:
        with open("students.txt", "r") as file:
            print("\nStudent List:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No data found")
