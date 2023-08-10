numbers = []

for i in range(3):
    numbers.append(float(input()))
    
squares = []
for num in numbers:
    squares.append(num**2)
    
print(squares)