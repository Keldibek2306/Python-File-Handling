with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output08.txt", 'w') as file:
    for i in numbers:
        if i % 5 == 0:
            file.write(f"{i} ")