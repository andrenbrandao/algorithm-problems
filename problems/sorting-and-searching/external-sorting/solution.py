LINES_PER_CHUNK = 1000000

from heapq import heapify, heappush, heappop

def sort_chunk(number):
    numbers = []
    filename = f"chunk_{number}.txt"

    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip('\n')))


    numbers.sort()

    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")


with open('large_file.txt', 'r') as file:
    chunk_number = 0
    count_lines = 0

    line = file.readline()
    while line:
        with open(f"chunk_{chunk_number}.txt", 'w') as chunk_file:
            while line and count_lines <= LINES_PER_CHUNK:
                chunk_file.write(line)
                count_lines += 1
                line = file.readline()

        count_lines = 0
        chunk_number += 1


for i in range(chunk_number):
    sort_chunk(i)

chunk_files = []
for i in range(chunk_number):
    f = open(f"chunk_{i}.txt", 'r')
    chunk_files.append(f)

minheap = []

for i, file in enumerate(chunk_files):
    line = file.readline()

    if line:
        value = int(line.strip('\n'))
        heappush(minheap, (value, i))

with open("result.txt", "w") as file:
    while minheap:
        value, chunk_pos = heappop(minheap)

        file.write(f"{value}\n")

        line = chunk_files[chunk_pos].readline()
        if line:
            new_value = int(line.strip('\n'))
            heappush(minheap, (new_value, chunk_pos))

for chunk_file in chunk_files:
    chunk_file.close()

