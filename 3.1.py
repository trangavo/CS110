# To find maximum subarray

import math
inf = -math.inf

def max_crossing(A, low, mid, high):
    left_sum = inf
    tot = 0
    for i in range(mid, low-1, -1):
        tot += A[i]
        if tot > left_sum:
            left_sum = tot
            max_left = i
    right_sum = inf
    tot2 = 0
    for j in range(mid+1, high+1):
        tot2 = tot2 + A[j]
        if tot2 > right_sum:
            right_sum = tot
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low+high) // 2
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
#A = [2,3,4,5,7]   
#n = len(A)
#max_subarray(A, 0, n-1)

def max_increment(A, current_max):
    new_sum = 0
    for i in range(-1,-len(A)-1,-1):
        new_sum += A[i]
        if new_sum > current_max:
            current_max = new_sum
    return current_max 
A = [2,3,4,5,7,-2]
print(max_subarray(A[0:-1], 0, len(A)-2)[2])
print(max_increment(A, max_subarray(A[0:-1], 0, len(A)-2)[2]))
