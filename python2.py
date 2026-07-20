def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Fibonacci sequence (first 10 numbers):")
fib_seq = fibonacci(10)
print(fib_seq)

print("\nPrime numbers in the sequence:")
primes = [x for x in fib_seq if is_prime(x)]
print(primes)
