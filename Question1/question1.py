def manage_student_club():
    activities = {}  # Dictionary to store activities and corresponding student names
    
    while True:
        # Get student details
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        activity = input("Enter the activity (e.g., Music, Sports, Art): ")
        
        # Add the student to the corresponding activity in the dictionary
        if activity not in activities:
            activities[activity] = []  # Create a new list for the activity
        activities[activity].append(name)
        
        # Ask if the user wants to add another member
        continue_input = input("Do you want to add another member? (yes/no): ").strip().lower()
        if continue_input == "no":
            break
    print(activities.keys())
    print(activity)

    # Display unique activities
    print("\nUnique Activities:")
    for activity in activities.keys():
        print(activity)
    
    # Count and display the number of students in each activity
    print("\nActivity Enrollment Counts:")
    for activity, students in activities.items():
        print(f"{activity}: {len(students)} students")
    
    # Display names of students grouped by activity
    print("\nStudents Grouped by Activity:")
    for activity, students in activities.items():
        print(f"{activity}: {', '.join(students)}")

# Run the program
manage_student_club()
