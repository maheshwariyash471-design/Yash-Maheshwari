students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll] = name
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for roll, name in students.items():
                print("Roll No:", roll, " Name:", name)
        else:
            print("No Records Found!")

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")
        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")