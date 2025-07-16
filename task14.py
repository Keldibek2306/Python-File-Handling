with open('Input/students.txt') as file:
    names = file.readlines()
    natija = sorted(names,reverse = True)

   
    
with open("Output/output14.txt", 'w') as file:
    file.writelines(natija)
