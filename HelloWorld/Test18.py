numbers = [10, 8, 4, 7, 11, 1, 12]
largest_number = numbers[0]
for number in numbers[1:]:
    if number > largest_number:
        largest_number = number
print(f"Largest number: {largest_number}")