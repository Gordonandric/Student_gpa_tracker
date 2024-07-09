# GPA Calculator
# Purpose: To calculate the unweighted or weighted GPA based on class grades
# Target Audience: Students in high school with the 4 point grading scale


# Functions

# Function to add a class-grade pair to list_of_pairs
def add_pair(class_name, grade):
    # Append class_name and grade to list_of_pairs
    list_of_pairs.append((class_name, grade))

# Function to remove a class-grade pair from list_of_pairs
def remove_pair(class_name):
    # Create and assign found_item's value to False
    found_item = False
    # Iterate through each pair in list_of_pairs
    for pair in list_of_pairs:
        # If class name matches the inputted class
        if class_name == pair[0]:
            # Remove that class-grade pair from pair list
            list_of_pairs.remove(pair)
            # If the class-grade pair is successfully removed change found_item's value to True
            found_item = True
            # Break the loop
            break
    # If found_item's value is True
    if(found_item == True):
        # Display to user that the pair was succesfully removed
        print("\nSuccessfully removed class-grade pair:",(pair))
    # Else if found_item's value is False 
    else:
        # Display to user the class-grade pair was not found
        print("\nClass-Grade pair was not found.")

# Function to calculate unweighted or weighted gpa based off class grades
def calculate_gpa(weighted):
    # Create total_gpa variable to store total_gpa value
    total_gpa = 0
    # Create total_grades variable to store total amount of grades
    total_grades = 0
    # If user inputs U for unweighted GPA
    if weighted == "U":
        # Iterate through each pair in list_of_pairs
        for pair in list_of_pairs:
            # Get class_name value from the first item in list_of_pairs
            class_name = pair[0]
            # Get grade value for corresponding class from the second item in list_of_pairs
            grade = pair[1]
            # If grade is in the lettergrade dictionary
            if grade in lettergrade:
                # gpa equals the corresponding value of the lettergrade
                gpa = lettergrade[grade]
                # Add gpa value to total_gpa
                total_gpa += gpa
                # Increase the total amount of grades by 1
                total_grades += 1
        
        # If the total amount of grades is greater than 0    
        if total_grades > 0:
            # The average unweighted gpa is equal to the total gpa divided by the total amount of grades
            average_gpa = total_gpa / total_grades
            # Round the unweighted gpa to two decimal points
            average_gpa = round(average_gpa, 2)
            # Display unweighted gpa
            print("\nYour Unweighted GPA:",average_gpa)
        # Else if total amount of grades is not greater than 0
        else:
            # Display to user that they have not added any class-grade pairs and instructions on how to
            print("\nSorry no class-grade pairs have been added yet try option 1")
    
    # Else if the user inputs W for weighted GPA            
    elif weighted == "W":
        # Iterate through each pair in list_of_pairs
        for pair in list_of_pairs:
            # Get class_name value from the first item in list_of_pairs
            class_name = pair[0]
            # Get grade value for corresponding class from the second item in list_of_pairs
            grade = pair[1]
            # If class_name contains 'AP'
            if "AP" in class_name:
                # If grade is in the lettergrade dictionary
                if grade in lettergrade:
                    # gpa equals the corresponding value of the lettergrade
                    gpa = lettergrade[grade]
                    # Add gpa value to total_gpa and add 1 because its a AP class
                    total_gpa += gpa + 1
                    # Increase the total amount of grades by 1
                    total_grades += 1
                    
            # Else if class_name does not contain 'AP'
            else:
                # If grade is in the lettergrade dictionary
                if grade in lettergrade:
                    # gpa equals the corresponding value of the lettergrade
                    gpa = lettergrade[grade]
                    # Add gpa value to total_gpa
                    total_gpa += gpa
                    # Increase the total amount of grades by 1
                    total_grades += 1
                    
        # If the total amount of grades is greater than 0       
        if total_grades > 0:
            # The average unweighted gpa is equal to the total gpa divided by the total amount of grades
            average_gpa = total_gpa / total_grades
            # Round the weighted gpa to two decimal points
            average_gpa = round(average_gpa, 2)
            # Display unweighted gpa
            print("\nYour weighted GPA:",average_gpa)
        # Else if total amount of grades is not greater than 0
        else:
            # Display to user that they have not added any class-grade pairs and instructions on how to
            print("\nSorry no class-grade pairs have been added yet try option 1.")

# Function to show all class-grade pairs
def show_all():
    # Checks if list_of_pairs is empty
    if list_of_pairs:
        # If list is not empty print heading for the pairs
        print("\nClass-Grade Pairs:")
        # Iterate through each pair in list_of_pairs
        for pair in list_of_pairs:
            # Print the class name and according grade
            print("\nClass:", pair[0], " Grade:", pair[1])
    # Else if the list is empty
    else:
        # Tell user that they have not added any class-grade pairs
        print("\nNo class-grade pairs added yet try option 1.")
    

# Create choice variable
choice = None

# List containing class-grade pairs
list_of_pairs = []

# Dictionary with each letter grade value
lettergrade = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
    "I": 0.0
}


# Welcome user to app
print("Welcome to the Student GPA Tracker app.")

# While user does not choose choice 0
while choice != "0":
    # Display user options
    print("""
        Options:
    
        0 - Quit
        1 - Add a class-grade pair
        2 - Remove a class-grade pair
        3 - Calculate GPA based off class grades
        4 - Show all class-grade pairs
    """)
    
    # Prompt user to enter their choice
    choice = input("Enter your choice: ")
    
    # If user selects choice 0
    if choice == "0":
        # Greet the user off the program
        print("\nThank you for using the Student GPA Tracker. Goodbye!")
        # Break the loop to end program
        break
    
    # If user selects choice 1
    elif choice == "1":
        # Prompt user to enter name of a class and if its a AP or Honors class
        class_name = input("\nEnter the name of a class (prefix AP for a AP class): ").upper()
        # Prompt user to enter grade of that class
        grade = input("\nEnter class letter grade (A,B,C,D,F,I): ").upper()
        # Call add_pair function to add class-grade pair to list
        add_pair(class_name, grade)
    
    # If user chooses choice 2
    elif choice == "2":
        # Prompt user to enter class name to delete corresponding grade
        class_name = input("\nEnter the name of the class whose grade you want to delete: ").upper()
        # Call remove_pair function to remove the class-grade pair
        remove_pair(class_name)
    
    # If user chooses choice 3
    elif choice == "3":
        # Prompt user to enter if they want unweighted or weighted GPA calculated
        weighted = input("\nEnter U for unweighted GPA or W for weighted GPA): ").upper()
        # Call calculate_gpa function to calculate gpa
        calculate_gpa(weighted)
    
    # If user chooses choice 4
    elif choice == "4":
        # Call show_all function to show all class-grade pairs
        show_all()
    
# Prompt user to press enter key to exit program
input("\n\nPress the enter key to exit")