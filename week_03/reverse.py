numbers = [3,4,5,6,7]
print(numbers)
numbers[0], numbers[4] = numbers[4],numbers[0]
numbers[1], numbers[3] = numbers[3],numbers[1]

print(numbers)