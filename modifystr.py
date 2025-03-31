a = """    hellow : wWorldD             """

b = a.upper()

c = b.lower()

e = c.strip()

f = e.replace("w", "EEE")

g = f.split(":")

h = (a + b + c + e + f).split()

print(h)