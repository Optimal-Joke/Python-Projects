import multiprocessing as mp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import time


def is_prime(n):
    """Checks if the number passed as input is prime.
    """
    m = np.absolute(n)
    if m == 1:
        return False
    elif m < 4:
        return True
    elif m % 2 == 0:
        return False
    elif m < 9:
        return True
    elif m % 3 == 0:
        return False
    else:
        r = np.floor(np.sqrt(m))
        f = 5
        while f <= r:
            if m % f == 0:
                return False
            if m % (f+2) == 0:
                return False
            f += 6
        return True


def sumPrimes(start, stop):
    """For summing primes under ~6500. Above this point, bigPrimeSum is more efficient.
    """
    sum_primes = 0
    for x in range(start, stop):
        if is_prime(x):
            sum_primes += x
    return sum_primes


def chunk(start, stop):
    """Splits a range of numbers into a number of smaller ranges, that number being the number of CPU threads available. 
    """
    threads = mp.cpu_count()
    num_samples = threads + 1

    array = np.linspace(start, stop, num=num_samples)
    mins_maxes = [int(np.floor(num)) for num in array]

    ranges = [(mins_maxes[idx], mins_maxes[idx+1])
              for idx, value in list(enumerate(mins_maxes))[:-1]]
    return ranges


def bigPrimeSum(start, stop):
    """For summing primes over ~6500. Above this point, this method is more efficient than sumPrimes.
    """
    ranges = chunk(start, stop)
    p = mp.Pool()
    sums = p.starmap(sumPrimes, ranges)
    totalsum = sum(sums)
    return totalsum


def benchmark(maxn=1000000, thread_count="multi"):

    tic = time.perf_counter()
    if thread_count == "multi":
        print(bigPrimeSum(1, maxn))
    elif thread_count == "single":
        print(sumPrimes(1, maxn))
    else:
        print("Please pass either \"single\" or \"multi\" as input.")
        return
    toc = time.perf_counter()
    duration = toc-tic

    if thread_count == "multi":
        message = f"Using all {mp.cpu_count()} available threads, a summation of primes up to {maxn} took {duration} seconds."
    elif thread_count == "single":
        message = f"Using a single thread, a summation of primes up to {maxn} took {duration} seconds."
    print(message)
    return maxn, duration


# Set minimum and maximum thresholds for the summation
mini = int(input("Lower bound of summation [1]: "))
maxi = int(input("Upper bound of summation [1000000]: "))
n_vals = int(input(
    "Number of intermediary bounds [100] (higher means more precise graph, but more time to complete): "))


# Set singlethread start time
single_tic = time.perf_counter()

# Sums primes up to 10000000 by speading the work over all available threads
single_maxnums = []
single_durations = []
for x in np.linspace(mini, maxi, num=n_vals):
    # if x != 1:
    maxn, duration = benchmark(maxn=int(x), thread_count="single")
    single_maxnums.append(maxn)
    single_durations.append(duration)
    print("")

# Set singlethread end time and calculate total time for execution
single_toc = time.perf_counter()
single_dur = single_toc-single_tic


# Set multithread start time
multi_tic = time.perf_counter()

# Sums primes up to 10000000 on a single thread
multi_maxnums = []
multi_durations = []
for x in np.linspace(mini, maxi, num=n_vals):
    # if x != 1:
    maxn, duration = benchmark(maxn=int(x), thread_count="multi")
    multi_maxnums.append(maxn)
    multi_durations.append(duration)
    print("")

# Set multithread end time and calculate total time for execution
multi_toc = time.perf_counter()
multi_dur = multi_toc-multi_tic


# Display single/multithread execution times
print(f"Singlethread diagnostic completed in {single_dur} seconds.")
print(
    f"Multithread ({mp.cpu_count()} threads) diagnostic completed in {multi_dur} seconds.")


# Set plot parameters
single_plot = plt.plot(single_maxnums, single_durations, "r")
multi_plot = plt.plot(multi_maxnums, multi_durations, "g")

plt.title("Execution Time of Prime Summation: Single vs Multithread")
plt.xlabel("Number under which all primes have been summed")
plt.ylabel("Duration of summation [s]")

red_patch = mpatches.Patch(color='red', label="Singlethread")
green_patch = mpatches.Patch(color='green', label="Multithread")
plt.legend(handles=[red_patch, green_patch])

# Display plot
plt.show()
