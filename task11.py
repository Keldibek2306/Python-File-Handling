with open('Input/students.txt') as file:
    names = file.read()
   
    
with open("Output/output11.txt", 'w') as file:
     file.write(" ".join(map(str, names.split())))


