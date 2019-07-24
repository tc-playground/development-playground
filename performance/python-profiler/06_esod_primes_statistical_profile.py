# Profile the generation of N prime numbers in which sum of digits is even.
# Deterministically profile and aggregated the time taken to invoke each method. 

from collections import defaultdict
import signal
import sys
import time

# Profile method decorator

# A global dictionary to store and aggregate the stats.
stats = defaultdict(int)
SAMPLE_INTERVAL = 0.001 # seconds

# Everytime the sample interupt is called sample the `stack`.
# Store what stack frame is currently being executed and rest the timer 
# for the next interupt.
def sample_stack(signum, frame):
    stack = []
    while frame:
        stack.append(frame.f_code.co_name)
        frame = frame.f_back
    stack_name = '-'.join(reversed(stack))
    stats[stack_name] += 1
    signal.setitimer(signal.ITIMER_PROF, SAMPLE_INTERVAL)

# Setup a signal timer and attach it to the `sample_stack` function.
signal.signal(signal.SIGPROF, sample_stack)
signal.setitimer(signal.ITIMER_PROF, SAMPLE_INTERVAL)

def print_summary(stats, total_time):
    total_samples = sum(stats.values())
    print('Total time: %f s' % total_time)
    print('Total samples: %s' % total_samples)

    for curr_stack, sample_count in stats.items():
        num_samples = sample_count
        children = [
            stack for stack in stats
            if len(stack) > len(curr_stack) and curr_stack in stack]
        # Number of samples for function is number of samples caught by
        # the function plus sum of samples of children.
        if children:
            num_samples += sum(stats[child] for child in children)
        sample_percent= 100.0 * num_samples / total_samples
        print('Function: %s, sample count: %d, percentage: %f %%' % (
            curr_stack, num_samples, sample_percent))

# Code to profile.

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
    start_time = time.time()
    primes = get_primes(n)
    total_time = time.time() - start_time
    print("Even Sum of Digit Primes: ", primes)
    print_summary(stats, total_time)
    print("Total time is %f s" % total_time)
    return 0

if __name__ == '__main__':
    main()

