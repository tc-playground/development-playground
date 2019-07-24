# Generates N prime numbers in which sum of digits is even.

import sys

# Inefficient prime calculator.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Return the sum of the digits in n.
def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# Generates N prime numbers in which sum of digits is even.
def get_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate) and sum_of_digits(candidate) % 2 == 0:
            primes.append(candidate)
        candidate += 1
    return primes

# Main Method

def main():
    n = int(sys.argv[1])
    primes = get_primes(n)
    print("Even Sum of Digit Primes: ", primes)
    return 0

if __name__ == '__main__':
    main()