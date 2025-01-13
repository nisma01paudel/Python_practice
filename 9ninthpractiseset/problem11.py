# 11. Write a python program to rename a file to “renamed_by_ python.txt

# import os

# os.rename("original_file.txt", "renamed_by_python.txt")

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)