#  Write a program to wipe out the content of a file using python.

with open("file.txt", "w") as f:
    # f.truncate(0)
    f.write("")