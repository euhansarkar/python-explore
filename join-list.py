list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

list3 = list1 + list2

# list1.extend(list2)

# print(list3)


for x in list2:
    list1.append(x)

print(list1)

