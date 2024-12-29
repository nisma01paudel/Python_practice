d={} # empty dictionary.
marks = {
       "Harry":100,
       "Subham": 56,
       "Rohan":23,
       0:"Harry"
}
# to comment: ctrl+/
# print(marks, type(marks))
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99,"Renuka":100})
# print(marks)

print(marks.get("Harry")) #prints none if something is not found in dictionary.
print(marks["Harry" ]) #prints error if something is not found in dictionary.