from homework_5.tracer.tracer import tracer


@tracer
def permutations(arr):
    if len(arr) <= 1:
        return [arr]

    all_permutations = []
    for i, elem in enumerate(arr):
        residue = arr[:i] + arr[i + 1 :]
        for permutation in permutations(residue):
            all_permutations.append([elem] + permutation)

    return all_permutations
