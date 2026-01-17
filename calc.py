# Program: Marks Calculator
# Author: Bhavya Sharma

# Marks Calculator for Exam Result

# Student Details
name = input("Enter Name: ")
student_class = int(input("Enter Class: "))
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
print("\n----- RESULT -----")
print(f"Name: {name}")
print(f"Class: {student_class}")
print(f"Section: {section}")
print(f"Total Marks: {total_obtained}/{total_max}")
print(f"Percentage: {percentage:.2f}%")