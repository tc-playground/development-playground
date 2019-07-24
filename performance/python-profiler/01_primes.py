# Generates N prime numbers.

import sys

# Inefficient prime calculator.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Calculate the specified number of primes.
def get_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

# Main Method

def main():
    n = int(sys.argv[1])
    primes = get_primes(n)
    print("Primes: ", primes)
    return 0

if __name__ == '__main__':
    main()
