# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
# Program to determine whether a student has passed or failed
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Calculate total percentage
total_percentage = (marks1 + marks2 + marks3) / 3

# Check pass/fail conditions
if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print(f"Congratulations! You have passed with a total percentage of {total_percentage:.2f}%.")
else:
    print(f"Sorry, you failed. Your total percentage is {total_percentage:.2f}%. Better luck next year!")
