ism = input("Ism kiriting: ").strip()

with open("Input/students.txt", "r") as fayl:
    ismlar = [qator.strip() for qator in fayl.readlines()]

if ism in ismlar:
   s = (f"{ism} faylda mavjud.")
   print(s)
else:
    s = (f"{ism} faylda mavjud emas.")
    print(s)
with open("Output/output18.txt" , "w") as fayil2 :
    fayil2.write(f"{s}" )