ism = input("ism kiriting:").title()

with open("Input/students.txt") as student:
    students = student.read()
    
    if ism in students:
        natija = f"{ism} ismi mavjud."
    else:
        natija = f"{ism} ismi mavjud emas"
        
with open("Output/output18.txt","w") as javobi:
    javobi.write(f"{natija}")