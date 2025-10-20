numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("X" * number)

# OR

for number in numbers:
    output = ''
    for item in range(number):
        output += 'X'
    print(output)