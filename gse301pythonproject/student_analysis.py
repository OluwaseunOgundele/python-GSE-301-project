# Student Academic Performance System
# GSE301 Python Project

department_info = ("Religion Department", "Faculty of Technology", 2025)

students = [
    {
        "name": "Rasheed Fatia",
        "matric": "23/60AC389",
        "age": 21,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["Python", "Statistics"],
        "outstanding": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric": "23/70JC093",
        "age": 22,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Algorithms"],
        "outstanding": 0
    },
    {
        "name": "Moses Oyedele",
        "matric": "23/50BC112",
        "age": 24,
        "cgpa": 2.90,
        "is_active": True,
        "courses": ["Networking"],
        "outstanding": 1
    }
]

courses_offered = {"Python", "Statistics", "Algorithms", "Networking"}


def get_grade(score):
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    match grade:
        case "A":
            print("Excellent")
        case "B":
            print("Very good")
        case "C":
            print("Good")
        case "D":
            print("Fair")
        case "E":
            print("Poor")
        case "F":
            print("Fail")

    return grade


scores = [45, 78, 90, 67, 88, 92, 54, 60, 73, 85]

print("Top 3 scores:", scores[:3])
print("Last 5 scores:", scores[-5:])
print("Alternate scores:", scores[::2])

passed_python = {"Rasheed Fatia", "Yusuf Adeoye"}
high_cgpa = {"Rasheed Fatia"}

print("Passed and merit:", passed_python & high_cgpa)
print("All students:", passed_python | high_cgpa)
print("Passed not merit:", passed_python - high_cgpa)

while True:
    print("\n1. View students")
    print("2. Add student")
    print("3. Check graduation eligibility")
    print("4. Exit")

    choice = input("Choose option: ")

    match choice:
        case "1":
            for student in students:
                print(student["name"])

        case "2":
            name = input("Name: ")
            matric = input("Matric: ")

            try:
                age = int(input("Age: "))
                cgpa = float(input("CGPA: "))
            except ValueError:
                print("Invalid input")
                continue

            active = input("Is active (yes/no): ").lower() == "yes"
            course_input = input("Courses (comma separated): ").split(",")

            students.append({
                "name": name,
                "matric": matric,
                "age": age,
                "cgpa": cgpa,
                "is_active": active,
                "courses": course_input,
                "outstanding": 0
            })

            print("Student added")

        case "3":
            name = input("Enter student name: ")

            for s in students:
                if s["name"].lower() == name.lower():
                    if s["cgpa"] >= 2.5 and s["outstanding"] == 0 and s["is_active"]:
                        print(s["name"], "is eligible for graduation")
                    else:
                        print(s["name"], "is NOT eligible for graduation")
                    break
            else:
                print("Student not found")

        case "4":
            print("Goodbye")
            break

        case _:
            print("Invalid choice")
