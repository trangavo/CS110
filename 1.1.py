# 2-way merge-sort algorithm
import math
def Two_Merge(L,R,A):
    l = len(L)
    r = len(R)
    n = len(A)
    # append an infinity value to the sublists
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    # for each position in the list, compare the smaller of the two smallest elements in two sublists
    for k in range(n):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
def Two_MergeSort(A):
    n = len(A)
    # if list only has 1 element, it is sorted
    if n == 1:
        return A
    else:
        # divide the list into 2
        L = []
        R = []
        for x in range(n//2):
            L.append(A[x])
        for y in range(n//2,n):
            R.append(A[y])
        # recursively divide the list into 2
        Two_MergeSort(L)
        Two_MergeSort(R)
        # merge two sublists
        Two_Merge(L,R,A)
        return A
