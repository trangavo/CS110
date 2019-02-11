# Heap functions

# 6.5 - 1
import math
# Max heapify
def max_heapify(A, i):
    heap_size = len(A) - 2
    l = 2*i
    r = 2*i+1
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
# Heap-extract-max
def extract_max(A):
    A.insert(0, math.inf)
    heap_size = len(A) - 1
    max = A[1]
    A[1] = A[heap_size]
    heap_size = heap_size - 1
    max_heapify(A, 1)
    A = A[1:]
    return max, A
A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
extract_max(A)

# 6.5 - 2
import math
def increase_key(A, i, key):
    if key < A[i]:
        return False
    A[i] = key
    while i > 1 and A[i//2] < A[i]:
        A[i], A[i//2] = A[i//2], A[i]
        i = i//2
def heap_insert(A,key):
    A.insert(0, math.inf)
    heap_size = len(A) - 1
    A.append(-math.inf)
    heap_size = heap_size + 1
    increase_key(A,heap_size,key)
    A = A[1:]
    return A
A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
heap_insert(A,10)

#heapq
def heappush(heap, item):
    heap.append(item)
    _siftup(heap, len(heap)-1, item)
def heappop(heap, item):
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftdown(heap, 0)
    else:
        returnitem = lastelt
    return returnitem
def heapify(x):
    n = len(x) - 1
    for i in range((n-1)//2,0,-1):
        _siftdown(x, i)

def _siftup(heap, startpos, item):
    while startpos > 0 and A[(startpos-1)//2] < A[startpos]:
        A[startpos], A[(startpos-1)//2] = A[(startpos-1)//2], A[startpos]
        startpos = (startpos-1) // 2
def _siftdown(heap, i):
    l = 2*i + 1
    r = 2*i + 1
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _siftdown(heap, largest)
