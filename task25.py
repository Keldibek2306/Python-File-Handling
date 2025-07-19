with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

talabalar = []
for i in students:
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        if grade == 5:
            talabalar.append(name)
        
with open("Output/output25.txt","w") as javob:
    javob.write("5 baho olgan talabalar: " + ",".join(talabalar))