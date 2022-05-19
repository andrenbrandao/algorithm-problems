import sys
from random import randint

if __name__ == "__main__":
    n = int(sys.argv[1])

    inputs = []
    for i in range(n):
        inputs.append(str(i))

    print(" ".join(inputs))
