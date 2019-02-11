# Randomized algorithms

# Worst sort function
import random
def shuffle(n):
    # create a list
    A = random.sample(list(range(0, 2*n)), n)
    # where the sorted list will be
    B = [0 for i in range(n)]
    check = False
    while check == False:
        # randomize the orders of elements in the list
        P = random.sample(list(range(0, n)), n)
        for i in range(n):
            B[P[i]] = A[i]
        # count how many "pairs" are in their relative orders
        count = 0
        for i in range(n-1):
            if B[i+1] >= B[i]:
                count += 1
        # shuffle until the list is sorted
        if count == n-1:
            check == True
            break
    return A, B

print(shuffle(2))
print(shuffle(3))
print(shuffle(4))
print(shuffle(5))
print(shuffle(6))
print(shuffle(7))
print(shuffle(8))
print(shuffle(9))

# Median finder
import random
import math
import numpy as np
def median_finder(n, q):
    # create a list
    A = random.sample(list(range(0, 2*n)), n)
    # sort the list
    A.sort()
    # get the index for the percentile
    low = round((50-q/2)/100*n)
    high = round((50+q/2)/100*n)
    # get random elements in the list 3*n times
    B = np.random.randint(0,n,3*n)
    count = 0
    for i in B:
        median = A[i]
        check = False
        count += 1
        # check if it's the median
        if median >= A[low] and median <= A[high]:
            check = True
            break
    # return the median if found
    if check == True:
        return A, A[low], A[high], median, count
    # return failed if not found
    else:
        return A, A[low], A[high], "failed", count
print(median_finder(10, 0.5))
print(median_finder(20, 0.3))
print(median_finder(30, 0.2))
