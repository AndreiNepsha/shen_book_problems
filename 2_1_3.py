# 2.1.3.
# Напечатайте все подмножества множества {1..k}


def generateSequences(n, k):
    sequences = []
    allSequencesGenerated = False
    sequence = [0] * k
    while not allSequencesGenerated:
        sequences.append(list(sequence))
        for i in reversed(range(k)):
            if sequence[i] == n - 1:
                sequence[i] = 0
                if i == 0:
                    allSequencesGenerated = True
            else:
                sequence[i] += 1
                break
    return sequences


def generateSubsets(k):
    set = range(1, k+1)
    subsets = []
    for sq in generateSequences(2, k):
        subsets.append([set[i] for i in range(0, k) if sq[i] != 0])
    return subsets


print(generateSubsets(3))
