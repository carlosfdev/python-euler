# Largest palindrome product  https://projecteuler.net/problem=4


def is_palindrome(num):
    return str(num) == str(num)[::-1]

biggest_palindrome = biggest_a = biggest_b = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        product = a * b
        if is_palindrome(product):
            if product > biggest_palindrome:
                biggest_palindrome = product
                biggest_a = a
                biggest_b = b

print(str(biggest_a) + ' * ' + str(biggest_b))
print(biggest_palindrome)
