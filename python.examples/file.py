#file = open("./test_write.txt", mode="a")
#file.write("Hello world\n")
#file.flush()
#file.close()
#while True:
#    pass

with open("./maj.txt", mode="r", encoding="UTF-8") as file:
    for line in file:
        line.replace(";", " ")
        line.replace(",", " ")
        line.replace(".", " ")
        line.replace(":", " ")
        line.replace("–", " ")

        for word in line.split(" "):
            word.replace(";", " ")
            word.replace(",", " ")
            word.replace(".", " ")
            word.replace(":", " ")
            word.replace("–", " ")
            print(word)

