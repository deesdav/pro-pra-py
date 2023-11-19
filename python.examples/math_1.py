def sum (a, b):
    return a + b
  
a = int(input("Put a number: "))
f1 = float(input("Put a float number: "))
print(type(a))
print(type(f1))
b = 3
print(type(b))
c = sum(a, b)
print(type(c))
print(c)

if a > 0:
    print(a)
elif a < 0:
    print(b)
else:
    print(c)