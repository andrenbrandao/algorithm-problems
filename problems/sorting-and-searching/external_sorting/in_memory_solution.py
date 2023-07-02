result = []

with open('large_file.txt', 'r') as file:
    for line in file:
        value = int(line.strip('\n'))
        result.append(value)

result.sort()

with open('result_in_memory.txt', 'w') as file:
    for value in result:
        file.write(f"{value}\n")
