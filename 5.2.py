# Quicksort
def partition(A,start,end):
    pivot = end
    i = start-1
    for j in range(start, end):
        if A[j] <= A[pivot]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[pivot] = A[pivot], A[i+1]
    return i+1
def quicksort(A,start,end):
    if start >= end:
        return A[end]
    else:
        i = partition(A,start,end) - 1
        quicksort(A,start,i)
        quicksort(A,i+2,end)
    return A
# A = [3,2,1,7,0,9,11,-22,-10,2,3,1,8,7,3]
# quicksort(A,0,len(A)-1)

import random, time
random.seed(123)
lst1 = [random.random() for a in range(100)]
lst2 = [i for i in range(100)]

starttime2 = time.time()
N = quicksort(lst2,0,len(lst2)-1)
endtime2 = time.time()
duration2 = endtime2-starttime2

starttime = time.time()
M = quicksort(lst1,0,len(lst1)-1)
endtime = time.time()
duration = endtime-starttime

print("unsorted list", duration)
print("sorted list", duration2)

# Fibonacci
import time
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
each_time = 0
for i in range(10):
    start = time.time()
    fib(100)
    end = time.time()
    duration = end-start
    each_time += duration
average = each_time/10
print(average)
