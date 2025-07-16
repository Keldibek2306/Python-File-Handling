with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output03.txt", 'w') as file:
    file.write(f"{max(numbers)}")
