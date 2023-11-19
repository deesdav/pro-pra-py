# slvoník
a = dict() # prazdný slovník
a = {} # prazdný slovník

a = {
    "ahoj": 5,
    "cus": 2,
    "list": [],
    1 : "ahoj"    
}
a["nevim"] = 5
print(a[1])

print(a.keys())
print(a.values())

del a["list"] # maže hodnotu která je pod klíčem list

if "nevim" in a.keys():
    print("'nevim' exists in the dictionary")

print(len(a))

for key , value in a.items():
    if "ahoj" in a.keys():
        print(f"{key} -> {value}")
    