#  Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

f = open("poems.txt")

# Read the entire file into a single string
content = f.read()
if("Twinkle" in content):
    print("The word 'Twinkle' is present in the file.")
else:
    print("The word 'Twinkle' is not present in the file.")
f.close()