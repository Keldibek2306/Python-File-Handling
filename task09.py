dic = {}

with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
    for num in numbers:
        count = 0
        i = num
        while i != 0:
            count += 1
            i = i // 10
        dic.update({num: count})

with open("Output/output09.txt", 'w') as file:
    for key, natija in dic.items():
        file.write(f"{key} - {natija}xonali\n") # 34 - 2xonali