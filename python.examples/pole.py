## Napsat program kde uživatel může psát čísal, ale když zadá -1 tak vypíše prumer sumu max min


array = []
user = 0

while user != -1:  
    user = int(input("Piš čísla: "))
    if user != -1:   
       array.append(user)
    if user == -1:
        print(max(array))
        print(min(array))
        print(sum(array))
        print(sum(array) / len(array))
        break

   

