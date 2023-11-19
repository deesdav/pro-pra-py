
"""class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
"""
##udělat sázku na červenou a černou
import random
print("WELCOME IN CASINO!")
start = 1000
generator = random.randint(1,37)
if generator >=1 and generator <=18:
    print("RED")
elif generator >=19 and generator <=36:
    print("BLACK") 
if generator == 37:
    print("GREEN") 

while start > 0:
   
    color_choice = str(input("ENTER COLOR: "))
    vallet = int(input("ENTER YOUR MONEY: "))
    if color_choice == "red" and generator >=1 and generator <=18:
        vallet = vallet + 200
        print(vallet)
    else:
        vallet = vallet - 200
    print(vallet)
    if color_choice == "black" and generator >=19 and generator <=36:
        vallet = vallet + 200
        print(vallet)
    else:
        vallet = vallet - 200
        print(vallet)
    if color_choice == "green":
        
        print("You cant enter green")
    else:
        vallet = vallet - 200
        print(vallet)
    



