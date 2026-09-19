# Simple Attendance Program using List Concept

students = [] 	#Starting with the empty list
def attendance():
    while True:
        print("\n\nWelcome to Attendance System:")
        print("-----------------------------")
        print("1. Add student")
        print("2. View students")
        print("e. Exit")

        choice = input("\nSelect your choice: ")

        if choice == '1':
            while True:
                data = str(input("Enter student name: "))
                students.append(data)
                print("\nNew student added successfully.")

                more = input("\nDo you want to add another student? (y/n): ").lower()
                if more == 'y':
                    continue
                elif more == 'n':
                    break   
                else:
                    print("\nInvalid input. Please enter 'y' or 'n'.")
                    break 

        elif choice == '2':
            if len(students) == 0:
                print("\nNo students in the list.")
            else:
                print("\n\nList of students:")
                for student in students:
                    print(student)

        elif choice == 'e':
            print("\nExiting Attendance System. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please try again.")

attendance()
