## množiny
my_set = set()

my_set.add("asdf")
my_set.add("asdf")
my_set.add(1)
my_set.add(1.0)
my_set.add(True)

my_second_set = set()
my_second_set.add("asdf")
my_second_set.add(2)

print(my_set)
print(my_second_set)

print(my_set.intersection(my_second_set)) # průnik
print(my_set.union(my_second_set)) # sjednocení
print(my_set.difference(my_second_set)) # rozdil

my_set_copy = my_set.copy()

print(my_set.clear())
print(my_set_copy)
print(my_set)
print(my_set.pop()) # vezme jeden prvek a smaže ho
print(my_set)

for item in my_second_set:
    print(item)