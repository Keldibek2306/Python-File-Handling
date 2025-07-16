with open('Input/students.txt') as file:
    names = file.readlines()
    for i in names:
        i = i.strip()
        sanash = len(i)
        natija = (f"isim {i} => {sanash} ta")
        print(natija)




with open("Output/output15.txt", 'w') as file:
    file.write(natija)
