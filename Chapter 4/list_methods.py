#In strings, if we change something, a new string is returned, he original one remains unchanged,
#But if we do the same with lists, the original one gets modified

list1 = ['Apple', 'Ravleen', 'Shorthills', 500, True]
print(list1)
list1.append("Generative AI")
print(list1)


l1 = [1,34,64,2,56,353,88]
l1.sort()
#l1.reverse()
print(l1)
l1.insert(3,27)
print(l1)

print("normal",l1.pop(3))
val = l1.sort()
print("v",val)
value = l1.pop(3)
print("val",value)