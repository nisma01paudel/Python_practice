books = ["Deep Work", 4.5, "Atomic Habits", 4.8, "The Pragmatic Programmer", 5]

print(books)

books.append("Power of subconscious mind")

print(books)
#lno=list numbers
lno =[1,4,7,2,5,3,9]
lno.sort()
print("Sorted numbers:" +str(lno))
lno.insert(6,8)
print("Inserted 8 in list :"+str(lno))
lno.pop(3)
print("pop out 4 in list :"+str(lno))
#print(lno.pop(4)) - function in print
#value = lno.pop(3) - another method
#print(value)
#print(lno)
lno.reverse()
print("Reversed numbers :"+str(lno))
lno.remove(3)
print("Removed 3 from list  :"+str(lno))