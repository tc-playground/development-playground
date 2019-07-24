# Profile the generation of N prime numbers in which sum of digits is even.
# Deterministically profile the time taken to invoke each method. 

import sys
import time

# Profile method decorator

# A python `decorator` to time individual functions.
# NB: The time taken to print the results 
def profile(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Function %s run time is %f s" % (
            func.__name__, time.time() - start_time))
        return result
    return wrapper 

# Code to profile.

# Inefficient prime calculator.
@profile
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Return the sum of the digits in n.
@profile
def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# Generates N prime numbers in which sum of digits is even.
@profile
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
    start_time = time.time()
    primes = get_primes(n)
    total_time = time.time() - start_time
    print("Even Sum of Digit Primes: ", primes)
    print("Total time is %f s" % total_time)
    return 0

if __name__ == '__main__':
    main()

