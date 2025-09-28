def sum_ids(arr, sum):
    seen = {}
    for i, num in enumerate(arr):
        target = sum - num
        if target in seen:
            return seen[target], i
        seen[num] = i
    return None
