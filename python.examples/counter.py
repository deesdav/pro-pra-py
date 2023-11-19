def counter(text): #funkce
    dict = {} # slovník prazdny    
    for i in text: # cyklus prochazim 
        if i in dict.keys(): # pokud se jeden znak textu vyskytuje ve slovníku, prida to kolikrat tam je
            dict[i] += 1 
        else: # pokud ne zalozi ho
            dict[i] = 1

    return dict # vracim slovnik

print(counter("aaaahoj"))