import random

with open('large_file.txt', 'w') as file:
    for i in range(5*10**7):
        n = random.randint(1, 10**10)
        file.write(f"{n}\n")
