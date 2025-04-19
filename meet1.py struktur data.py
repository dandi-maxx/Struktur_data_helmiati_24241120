# operasi Logika
# or and xor not

x = Truex = False

z = not x
print("nilai dari z =", z)

print("********** and ***********")
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)

x = True
y = False
z = x and y
print(x, 'and', y, '=', z)

x = False
y = True
z = x and y
print(x, 'and', y, '=', z)

y = False
z = x and y
print(x, 'and', y, '=', z)

x = True
y = False
z = x or y
print(x, 'or', y, '=', z)

x = False
y = True
z = x or y
print(x, 'or', y, '=', z)

x = False
y = False
z = x or y
print(x, 'or', y, '=', z)
