dict_a = {
    "name": "euhan",
    "age": 20,
    "year": 2024,
    "isActive": True 
}

dict_a["age"] = 30

# print(dict_a)

# print(dict_a.values())
# print(dict_a.keys())
# print(dict_a.items())

# print(dict_a.get("age"))

dict_a.update({"year": 1950})
dict_a.update({"hello": "world"})
dict_a.update({"what": "are you there?"})
dict_a.update({"may": "may i comein sir?"})

# dict_a.popitem()
# dict_a.popitem()
# dict_a.popitem()
# dict_a.popitem()
# dict_a.pop("year")

# dict_a.clear()

# print("name" not in dict_a)


dict_b = dict_a.copy()

dict_b["name"] = "sarkar"

print(dict_a)
print(dict_b)
