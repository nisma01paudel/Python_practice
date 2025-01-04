#  Attempt problem 1 using while loop. 

#  Write a program to print multiplication table of a given number using for loop.

n=int(input("Enter the number you wish to multiply:"))

i=1

while (i<11):
    print(f"{n} x {i} = {n*i}")
    i+=1