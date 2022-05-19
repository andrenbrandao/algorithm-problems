import sys
import os

tests = int(sys.argv[1])

for i in range(tests):
    print(f"Test #{str(i)}")

    os.system(f"python3 gen.py {str(i)} > input.txt")

    os.system(f"python3 ../quicksort-naive.py < input.txt > model.txt")
    os.system(f"python3 ../quicksort-randomized.py < input.txt > main.txt")

    with open("input.txt") as f:
        input_data = f.read()
        print("Input:")
        print(input_data)

    with open("model.txt") as f:
        model = f.read()
        print("Model:", model)

    with open("main.txt") as f:
        main = f.read()
        print("Main:", main)

    if model != main:
        break
