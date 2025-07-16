with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    numbers.sort()
    
with open("Output/output10.txt", 'w') as file:
    file.write(" ".join(map(str, numbers)))