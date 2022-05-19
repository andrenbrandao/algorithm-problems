import sys
import os
import time

tests = int(sys.argv[1])

avg1 = []
avg2 = []

for i in range(tests, tests + 1):
    print(f"Test #{str(i)}")

    os.system(f"python3 gen.py {str(i)} > input.txt")

    start = time.time()
    os.system(f"python3 ../quicksort-naive.py < input.txt")
    time1 = time.time() - start
    avg1.append(time1)

    start = time.time()
    os.system(f"python3 ../quicksort-randomized.py < input.txt")
    time2 = time.time() - start
    avg2.append(time2)

    print(f"Execution 1: {time1}")
    print(f"Execution 2: {time2}")

print(f"Avg Quicksort: {sum(avg1)/len(avg1)}")
print(f"Avg Quicksort Randomized: {sum(avg2)/len(avg2)}")
