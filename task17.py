with open("Input/students.txt") as hariflar ,open("Output/output17.txt" , "w") as harif :
    oqilgan = hariflar.readlines()
    natija = filter(lambda harf : harf.lower().startswith("a"),oqilgan) 
    
    harif.writelines(natija)
    
    print("fayilga yozildi ")