with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output06.txt", 'w') as file:
    for i in numbers:
        if i % 2 == 1:
            file.write(f"{i} ")