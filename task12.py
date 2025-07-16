
with open('Input/students.txt') as file:
    names = file.readlines()

    natija = len(names)
   
    
with open("Output/output12.txt", 'w') as file1:
    file1.writelines(names)
    file1.write(f"ismlar soni {natija}")