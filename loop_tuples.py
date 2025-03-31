tuple_a = ("apple", "banana", "cherry")

# by using for loop
# for x in tuple_a:
#     print(x)


# by using range(len)

# for x in range(len(tuple_a)):
#     print(f"x is {x}",tuple_a[x])


# by using while loop
x = 0
while x < len(tuple_a):
    print(f"x is {x} {tuple_a[x]}")
    x += 1