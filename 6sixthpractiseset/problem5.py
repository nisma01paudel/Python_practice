# Write a program which finds out whether a given name is present in a list or not.

list = ["Ram", "Rita", "Shyam", "Radha", "Krishna"]

name = input("Enter a name: ")

if( name in list):
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")