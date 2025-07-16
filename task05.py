with open('Input/numbers.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
    natija = sum(numbers) / len(numbers)
    
    
with open("Output/output05.txt", 'w') as file:
    file.write(f"{natija}")

    