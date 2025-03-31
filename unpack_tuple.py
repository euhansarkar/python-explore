# like the javascript destructure we can unpack tuples here

tuple_a = ("apple", "banana", "cherry")

(red, yellow, green) =  tuple_a

# print(type(red))

# print(type(yellow))

# print(type(green))




# like the javascript when you need to take the rest (...) then it you should use asteriks (*) sign to take the rest. (*) sign should not use multile times, it just use only 1 time. otherwise it will give an error.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "hello", "world")


(green, *yellow, pk, red) = fruits


print(green)

print(yellow)

print(pk)

print(red)