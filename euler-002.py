# Even Fibonacci numbers https://projecteuler.net/problem=2


def fib(previous, current, accumulator=0):
    # limit set by the problem
    if current > 4000000:
        print(str(accumulator))
        exit()
    if current % 2 == 0:
        accumulator += current
    # The right-hand side is evaluated first, this way we don't need to set a third variable
    previous, current = current, previous+current
    return fib(previous, current, accumulator)

# We start with 1 and 2 as the problem says
fib(1, 2)
