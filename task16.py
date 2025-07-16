with open('Input/students.txt') as file:
    names = file.readlines()
    natija = []
    for i in names:
        i = i.strip()
        if len(i) > 5:
            natija.append(i)
        

with open("Output/output16.txt", 'w') as file:
    file.writelines(f"{natija} ")
