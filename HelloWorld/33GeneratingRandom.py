import random

for i in range(3):
    print(random.randint(1,100))

members = ['John', 'Bob', 'Mary', 'Mosh']
leader = random.choice(members)
print(leader)