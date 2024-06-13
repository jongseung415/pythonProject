a = [1,2,3]
a[2] = 4
print(a)

x = ["adam", "john", "casey"]
y = x
print(x)
print(y)
y[2] = "ben"
print(x)
print(y)

del a[0]
print(a)
