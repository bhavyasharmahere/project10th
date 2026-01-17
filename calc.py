# Program: Marks Calculator
# Author: Bhavya Sharma

# Marks Calculator for Exam Result

# Student Details
name = input("Enter Name: ")
student_class = int(input("Enter Class: "))

if student_class >= 8:
    section = input("Enter Section: ")
    print("\nEnter Maximum Marks for each subject:")
    max_comp = int(float(input("Computer: ")))
    max_maths = int(float(input("Maths: ")))
    max_science = int(float(input("Science: ")))
    max_sst = int(float(input("SST: ")))
    max_english = int(float(input("English: ")))
    max_s = int(float(input("Sanskrit: ")))
    max_h =  int(float(input("Hindi: ")))
    
    print("\nEnter Marks You Obtained:")
    c = int(float(input("comp: ")))
    maths = int(float(input("Maths: ")))
    science = int(float(input("Science: ")))
    sst = int(float(input("SST: ")))
    english = int(float(input("English: ")))
    s= int(float(input("Sanskrit: ")))
    h=  int(float(input("Hindi: ")))
    
    # Net Calculations
    total_max = max_comp + max_maths + max_science + max_sst + max_english + max_s + max_h
    total_obtained = c + maths + science + sst + english + s + h
    percentage = (total_obtained / total_max) * 100
    
    # Final Output
    print(f"Name: {name}")
    print(f"Class: {student_class}")
    print(f"Section: {section}")
    print(f"Total Marks: {total_obtained}/{total_max}")
    print(f"Percentage: {percentage:.2f}%")

    print('ENDS')


else:
    section = input("Enter Section: ")
    print("\nEnter Maximum Marks for each subject:")
    max_ai = int(float(input("AI: ")))
    max_maths = int(float(input("Maths: ")))
    max_science = int(float(input("Science: ")))
    max_sst = int(float(input("SST: ")))
    max_english = int(float(input("English: ")))
    max_lang = int(float(input("Sanskrit/Hindi: ")))
    
    print("\nEnter Marks Obtained:")
    ai = int(float(input("AI: ")))
    maths = int(float(input("Maths: ")))
    science = int(float(input("Science: ")))
    sst = int(float(input("SST: ")))
    english = int(float(input("English: ")))
    lang = int(float(input("Sanskrit/Hindi: ")))
    
    # Calculations
    total_max = max_ai + max_maths + max_science + max_sst + max_english + max_lang
    total_obtained = ai + maths + science + sst + english + lang
    percentage = (total_obtained / total_max) * 100
    # Output
    
    print(f"Name: {name}")
    print(f"Class: {student_class}")
    print(f"Section: {section}")
    print(f"Total Marks: {total_obtained}/{total_max}")
    print(f"Percentage: {percentage:.2f}%")
