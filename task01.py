with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    
with open("Output/output01.txt", 'w') as file:
    file.write(" ".join(map(str, numbers)))