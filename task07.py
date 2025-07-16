with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output07.txt", 'w') as file:
    for i in numbers:
        file.write(f"{i ** 2} ")