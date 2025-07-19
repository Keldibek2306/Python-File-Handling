
with open("Input/grades.csv") as name_grade:
    names = name_grade.read().splitlines()
    names.pop(0)
    
jami = 0
soni = 0

for i in names:
    if i.strip():
        name, grade = i.split(",")
        jami += int(grade)
        soni += 1

with open("Output/output20.txt","w") as javob:
    if soni > 0:
        ortacha = jami / soni
        javob.write(f"O'rtacha baho: {round(ortacha,2)}")
    else:
        javob.write("Talaba baho olmagan.")