x = ("apple", "banana", "cay")

y = list(x)

y[0] = "hello"

z = tuple(y)

# print(x)

# print(y)

# print(type(z))

# tuple is immutable that means unchanable. but if we need to add some values in tuple then we should convert the tuple to the list first. then add values by using list methods. then convert it back into tuple.

tuple1 = ("apple", "banana", "cherry")

a = list(tuple1)

a.append("euhan")

tuple2 = tuple(a)

# print(tuple2)


# to add a tuple into another tuple we should sum it.

tuple_x = ("hello", "world")

tuple_y = ("i'm", "euhan")

tuple_x += tuple_y

# print("see tuple x", tuple_x)

# the same way we added elements in a tuple, with the same way we can remove tuple elements from the tuple.



