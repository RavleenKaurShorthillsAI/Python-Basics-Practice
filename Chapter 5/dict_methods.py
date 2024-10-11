marks = { "Ravleen": 100, "John": 88, "Jake": 67}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Ravleen": 99, "Sia": 89})
print(marks)
print(marks.get("Ravleenkaur")) #Returns None
print(marks["Ravleenkaur"]) #returns an error