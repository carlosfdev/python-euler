# Largest prime factor https://projecteuler.net/problem=3


objective = 600851475143
divider = 2
max_prime_factor = 1

while objective > 1:
    while objective % divider == 0:
        objective /= divider
        max_prime_factor = divider
    divider += 1

print(max_prime_factor)
