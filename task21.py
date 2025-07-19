with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

max_grade = -1
talabalar = []
for i in students:
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        if grade > max_grade:
            max_grade = grade
            talabalar = [name]
        elif grade == max_grade:
            talabalar.append(name)
        
with open("Output/output21.txt","w") as javob:
    javob.write(f"max baho {max_grade},olgan talabalar: {', '.join(talabalar)}")