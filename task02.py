with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output02.txt", 'w') as file:
    file.write(f"{sum(numbers)}")
