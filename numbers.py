a = 100
b = 200
total_sum = 0

list1 = range(a, b + 1)
for number in list1:
    if number % 2 == 1:
        total_sum += 1

print(total_sum)
