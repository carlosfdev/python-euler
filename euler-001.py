#  Multiples of 3 and 5 https://projecteuler.net/problem=1
accumulator = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        accumulator += i
print(str(accumulator))
