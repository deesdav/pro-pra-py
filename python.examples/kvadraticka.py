import math
a = int(input("Put a number "))
b = int(input("Put a second number "))
c = int(input("Put a third number "))
  
D = b**2 - 4*a*c
print("Diskriminant:", D)
if D > 0:
    print("Rovnice má 2 řešení")
    x1 = (-b-(math.sqrt(D)))/(2*a)
    x2 = (-b+(math.sqrt(D)))/(2*a)
    print(x1, x2)

elif D < 0:
    print("Rovnice nemá řešení")
    print("Tady je vzorec který si vypočítej sám")
    if b>0:
        print(f"(-{b} - ({-D})^(1/2) * i ) / ({a*2})")
        print(f"(-{b} + ({-D})^(1/2) * i ) / ({a*2})")
    else:
        print(f"({b} - ({-D})^(1/2) * i ) / ({a*2})")
        print(f"({b} + ({-D})^(1/2) * i ) / ({a*2})")
else:
    print("Rovnice má 1 řešení")
    x = (-b)/(2*a)
    print(x)