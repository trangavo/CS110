# Implementations of different sorting algorithms

# Insertion sort
import time
start = time.time()
def insertion_sort(A):
    for j in range(1, len(A)):
      key = A[j]
      i = j-1
      while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
      A[i+1] = key
    return(A)
print(insertion_sort([112,110,156,99]))
end = time.time()
duration = end - start
print(duration)

# Bubble sort
import time
start = time.time()
def bubble_sort(A):
    for j in range(len(A)-1):
        for i in range(0, len(A)-1):
            key = A[i]
            if A[i+1] < A[i]:
                A[i] = A[i+1]
                A[i+1] = key
    return(A)
print(bubble_sort([112,110,156,99]))
end = time.time()
duration = end - start
print(duration)      

# Selection sort
import time
start = time.time()
def selection_sort(A):
    for i in range(0, len(A)-1):
        key = A[i]
        position_min = i
        for j in range(i+1, len(A)):
            if A[j] < A[position_min]:
                position_min = j
        A[i] = A[position_min]
        A[position_min] = key
    return(A)
print(selection_sort([112,110,156,99]))
end = time.time()
duration = end - start
print(duration)
