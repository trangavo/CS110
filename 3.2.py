# Create a heap

# max-heapify
def max_heapify(A,i):
    # get the left child's index
    l = 2*i
    # get the right child's index
    r = 2*i+1
    # get heap size
    heap_size = 
    # find the largest among key node, left child, right child
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    # Switch the largest and key node
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # call the function again for the next layer to keep pushing the key node down
        max_heapify(A, largest)
# build-max-heap
def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A)//2,0,-1):
        max_heapify(A,i)
