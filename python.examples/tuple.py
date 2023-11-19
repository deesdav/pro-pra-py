def qudratic(a, b, c):
    D = b**2 + 4 * a * c
    x1 = (-b + (D)**(1/2)) / (2 * a)
    x2 = (-b - (D)**(1/2)) / (2 * a)
    return x1, x2

_, b = qudratic(1, -2 , 1)
print(b)