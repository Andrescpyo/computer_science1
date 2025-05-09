import math

#This file is to test whether the merge sort and bubble sort algorithms are functions proportional to their complexity O(n log n) and O(n^2) respectively and therefore determine whether or not they comply with it.

merge_data = {
    #These are the average data for the number of steps it took for the algorithm to sort the files with 'n' amounts of data.
    #n: steps

    50: 505,
    100: 1209,
    500: 8338.6667,
    1000: 18697.333,
    5000: 117029,
    10000: 254055,
    50000: 1552615,
    100000: 3305278,
    500000: 18813550,
    1000000: 39625246
}

bubble_data = {
    50: 1884,
    100: 7560.3333,
    500: 187889.67,
    1000: 749843.33,
    5000: 18775408,
    10000: 75203782
}

print("Merge Sort Verification:")
for n, steps in merge_data.items():
    n_log_n = n * math.log2(n)
    ratio = steps / n_log_n
    print(f"n={n}, steps={steps}, n*log2(n)={n_log_n:.2f}, ratio={ratio:.2f}")

print("\nBubble Sort Verification:")
for n, steps in bubble_data.items():
    n_squared = n ** 2
    ratio = steps / n_squared
    print(f"n={n}, steps={steps}, n^2={n_squared}, ratio={ratio:.2f}")