from homework_6.compare_n_iterative.timeit import timeit


@timeit
def makeheap_n_log_n(arr):
    #  работает за n * O(_siftup) = n log h
    for idx in range(len(arr)):
        arr = _sift_up(arr, 0, idx)
    return arr


@timeit
def makeheap(arr):
    #  работает быстро за счет того, что проходит снизу вверх
    length = len(arr)
    start_idx = (length // 2) - 1
    for idx in range(start_idx, -1, -1):
        _sift_down(arr, idx, length - 1)
    return arr


#  работает за O(h)
def _sift_up(heap, start_idx, end_idx):
    idx = end_idx
    while idx > start_idx:
        parent_idx = (idx - 1) // 2
        if heap[parent_idx] > heap[idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        else:
            return heap
        idx = parent_idx
    return heap


#  работает за O(h)
def _sift_down(heap, start_idx, end_idx):
    idx = start_idx
    while True:
        child_idx = 2 * idx + 1
        if child_idx > end_idx:
            return heap

        if child_idx + 1 <= end_idx and heap[child_idx + 1] < heap[child_idx]:
            child_idx += 1

        if heap[idx] <= heap[child_idx]:
            return heap
        heap[idx], heap[child_idx] = heap[child_idx], heap[idx]
        idx = child_idx
