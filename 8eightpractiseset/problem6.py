# Write a python function which converts inches to cms. 

def inch_to_cm(inch):
    return inch*2.54

inch = int(input("Enter inch to convert: "))
cm=inch_to_cm(inch)
print(f"The corresponding value in cms is : {cm} cm")