numbers = [3, 5, 3, 2, 2, 2, 50, 59, 1]
max = 1
result = 0
for i in range(1, len(numbers)):
    n = numbers.count(numbers[i])
    if n > max:
        max = n
        result = i
