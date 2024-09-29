def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors from 2 to sqrt(num)
        if num % i == 0:  # If num is divisible by i, it is not prime
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):  # Check if i + 1 is prime
        print(i + 1, end=" ")  # Print prime numbers on the same line
print()
