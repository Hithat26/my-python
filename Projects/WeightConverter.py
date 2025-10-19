weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "l" or unit == "L":
    weight *= 0.45
    print(f"You are {weight} kilograms")
else:
    weight /= 0.45
    print(f"You are {weight} pounds")

