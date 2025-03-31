thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "apple"]


thislist.sort()

# print(thislist)

list1 = [9238, 8293, 82, 829,  8, 892, 81, 183, 284]

list1.sort(reverse = True)

# print(list1)

def myFunction(n):
    return abs(n - 50)


list2 = [100, 500, 50, 3, 458]

list2.sort(key = myFunction)

# print(list2)

list3 = ["banana", "Orange", "Kiwi", "cherry"]

list3.sort(key = str.upper)

list3.reverse()

print(list3)




