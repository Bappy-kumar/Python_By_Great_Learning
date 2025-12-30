class Student:
    collegename = "GL"

    def __init__(self, studId, department, subs):
        self.studId = studId
        self.department = department
        self.subs = subs
        self.cgpa = sum(self.subs) / len(self.subs)

    def __str__(self):
        return f"{self.studId}:{self.department}:{self.cgpa}:{Student.collegename}"


stds = []

while True:
    print("\n1. Register a new student")
    print("2. Update the student details")
    print("3. Remove the student details")
    print("4. Search for the student")
    print("5. Display all the student details")
    print("0. Exit")

    ch = int(input("Enter choice: "))

    # 1. Register
    if ch == 1:
        id1 = int(input("Enter student ID: "))
        dept = input("Enter department: ")
        m1 = int(input("Enter marks for subject 1: "))
        m2 = int(input("Enter marks for subject 2: "))
        m3 = int(input("Enter marks for subject 3: "))
        stds.append(Student(id1, dept, [m1, m2, m3]))
        print("Student registered successfully")

    # 2. Update
    elif ch == 2:
        id1 = int(input("Enter student ID to update: "))
        for s in stds:
            if s.studId == id1:
                s.department = input("Enter new department: ")
                s.subs = [
                    int(input("Enter new marks for subject 1: ")),
                    int(input("Enter new marks for subject 2: ")),
                    int(input("Enter new marks for subject 3: "))
                ]
                s.cgpa = sum(s.subs) / len(s.subs)
                print("Student updated successfully")
                break
        else:
            print("Student not found")

    # 3. Remove
    elif ch == 3:
        id1 = int(input("Enter student ID to remove: "))
        stds = [s for s in stds if s.studId != id1]
        print("Student removed if existed")

    # 4. Search
    elif ch == 4:
        id1 = int(input("Enter student ID to search: "))
        for s in stds:
            if s.studId == id1:
                print(s)
                break
        else:
            print("Student not found")

    # 5. Display all
    elif ch == 5:
        if not stds:
            print("No students available")
        for s in stds:
            print(s)

    # Exit
    elif ch == 0:
        print("Exiting program...")
        break

    else:
        print("Wrong choice")
