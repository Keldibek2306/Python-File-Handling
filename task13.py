
with open('Input/students.txt') as file:
    names = file.readlines()
    natija = sorted(names)

   
    
with open("Output/output13.txt", 'w') as file:
    file.writelines(natija)
