output_file = []

with open('lib/input.txt', 'r') as f:
    output_file = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]

print(output_file)

with open('out.txt', 'w') as f:
    f.write(''.join(line for line in output_file))
