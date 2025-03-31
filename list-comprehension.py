fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newFruits = []

for x in fruits:
    if "n" in x:
        newFruits.append(x)

newlist = [x for x in fruits if "a" not in x]
list1 = [y for y in fruits if "e" not in y]
list2 = [z for z in fruits if "i" in z]

# print(newlist)

# print(list1)

# print(list2)

list3 = [a for a in fruits if a != "apple"]

# print(list3)


list4 = [k for k in fruits]


list5 = [g for g in range(10) if g < 7]

# print(list4)

# print(list5)

list6 = [x.upper() for x in fruits]

list7 = ["hello" for p in fruits]

# print(list6)

# print(list7)

list8 = [x if x != "banana" else "orange" for x in fruits]


print(list8)

