# Write a program to accept marks of 6 students and display them in a sorted manner.
# Write a program to store seven fruits in a list entered by the user.
marks = []

l1 = int(input("Enter marks here:"))
marks.append(l1)
l2 = int(input("Enter marks here:"))
marks.append(l2)
l3 = int(input("Enter marks here:"))
marks.append(l3)
l4 = int(input("Enter marks here:"))
marks.append(l4)
l5 = int(input("Enter marks here:"))
marks.append(l5)
l6 = int(input("Enter marks here:"))
marks.append(l6)
marks.sort()
print(marks)