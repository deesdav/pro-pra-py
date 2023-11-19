def prep_counter(words, index):
    counter = {}
    for word in words:
        char = word[index]
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
    return counter
# "olovo", "osel", "lok", "kolo", "oko", "olusk", "koks" , "slon", "nos"
# "kolo", "ostružina", "ananas", "slon", "nůžky", "yacht", "hora", "auto", "oko", "osud"
# "ahoj", "ok", "joj"
firstLetterCount = prep_counter(["ahoj", "ok", "jo"], 0)
lastLetterCount = prep_counter(["ahoj", "ok", "jo"], -1)

inter = set(firstLetterCount.keys()).intersection(set(lastLetterCount.keys()))

for i in inter:
    value = firstLetterCount[i]
    firstLetterCount[i] -= value
    lastLetterCount[i] -= value
    if firstLetterCount[i] == 0:
        del firstLetterCount[i] 
    if lastLetterCount[i] == 0:
        del lastLetterCount[i]     


if len(firstLetterCount) == 1 and len(lastLetterCount) == 1:
    first_letter, firstV = list(firstLetterCount.items())[0]
    last_letter, lastV = list(lastLetterCount.items())[0]
    
    if firstV > 0 and lastV > 0:
        print("You can play")
    else:
        print("You cannot play")
else:
    print("You cannot play")
