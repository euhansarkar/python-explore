thislist = ["apple", "banana", "cherry"]

list1 = thislist.copy()

list1[0] = "hello"

# print(thislist)

# print(list1)

# another way to copy a list here

list2 = list(thislist)

list2[0] = "world"

# print(thislist)

# print(list2)


# another way to make a copy of list

list3 = thislist[:]

list3[0] = "another"

print(thislist)

print(list3)