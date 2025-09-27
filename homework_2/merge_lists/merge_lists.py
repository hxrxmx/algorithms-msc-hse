def merge(list_1, list_2):
    merged = []
    while list_1 and list_2:
        if list_1[0] < list_2[0]:
            merged.append(list_1.pop(0))
        else:
            merged.append(list_2.pop(0))

    merged += list_1 + list_2

    return merged
