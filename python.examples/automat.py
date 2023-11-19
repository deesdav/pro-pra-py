user = int(input("Enter your count of money "))

MONEY = (5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
print(f"{user}Kč")
print("===============")
for item in MONEY:
    count = user // item 
    if count == 0:
        continue
    else: 
        print(f"{item}Kč")
        print(f"{count}x")
        user = user % item
        print(f"zbyde {user}")
    



