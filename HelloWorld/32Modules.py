def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


# to use find_max use:
# import 32Modules or
# from 32Modules import find_max