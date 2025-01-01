#  Write a program to find out whether a given post is talking about “Sita ” or not.

post = input("Enter the post: ")

if("Sita" in post.lower()):
    print("This post is talking about sita")

else:
    print("This post is not talking about sita")