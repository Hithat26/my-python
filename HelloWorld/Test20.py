numbers = [4, 10, 7, 4, 2, 2]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)