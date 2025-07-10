#student grade checker
# use tuple to store Name and Roll NO.
# use list to store multiple student detail
# use three subject and accept the grade
# print all the student with their grade
#     Note: >=80%=1st divistion
#     >=60%&<80%=2nd division

# Student Grade Checker

# List to store all student details
students = []

# Function to calculate percentage and division
def get_division(percentage):
    if percentage >= 80:
        return "1st Division"
    elif percentage >= 60:
        return "2nd Division"
    elif percentage >= 40:
        return "3rd Division"
    else:
        return "Fail"

# Number of students to enter
num = int(input("Enter number of students: "))

for i in range(num):
    print(f"\nEnter details for Student {i+1}")
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    
    # Accepting marks for 3 subjects
    sub1 = float(input("Enter marks for Python: "))
    sub2 = float(input("Enter marks for System Analysis and Datastructure: "))
    sub3 = float(input("Enter marks for Compiler: "))
    
    # Calculate total and percentage
    total = sub1 + sub2 + sub3
    percentage = total / 3
    
    # Get division
    division = get_division(percentage)
    
    # Store data as (Name, Roll No, Percentage, Division)
    student = (name, roll, round(percentage, 2), division)
    students.append(student)

# Print all student details
print("\n--- Student Grade Report ---")
print("Name\t\tRoll No\t\t% Marks\t\tDivision")
for student in students:
    print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}%\t\t{student[3]}")