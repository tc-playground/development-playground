# Profile the generation of N prime numbers in which sum of digits is even.
# Deterministically profile and aggregated the time taken to invoke each method. 

from collections import defaultdict
import sys
import time

# Profile method decorator

# A global dictionary to store and aggregate the stats.
stats = defaultdict(lambda: defaultdict(float))

# A python `decorator` to time individual functions.
# NB: The time taken to print the results 
def profile_stats(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_name = func.__name__
        # We need this small hack to keep things simple.
        caller_name = sys._getframe(1).f_code.co_name
        result = func(*args, **kwargs)
        stats[func_name][caller_name] += time.time() - start_time
        return result
    return wrapper

def print_summary(stats, total_time):
    print('Total time: %f s' % total_time)
    for f_name in stats:
        func_time = 0
        for caller in stats[f_name]:
            func_time += stats[f_name][caller]
            percentage = float(func_time) / total_time
        print('Function: %s, caller: %s, function run time: %f s, percentage: %f %%' % (
            f_name, caller, func_time, 100 * percentage))

# Code to profile.

# Inefficient prime calculator.
@profile_stats
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Return the sum of the digits in n.
@profile_stats
def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# Generates N prime numbers in which sum of digits is even.
@profile_stats
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
    print_summary(stats, total_time)
    print("Total time is %f s" % total_time)
    return 0

if __name__ == '__main__':
    main()

