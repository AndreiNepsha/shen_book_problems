# 2.1.4.
# Напечатайте все последовательности положительных целых
# чисел длины k, у которых i-й член не превосходит i.


def generateSequences(k):
    sequences = []
    allSequencesGenerated = False
    sequence = [1] * k
    while not allSequencesGenerated:
        sequences.append(list(sequence))
        for i in reversed(range(k)):
            if sequence[i] == i + 1:
                sequence[i] = 1
                if i == 1:
                    allSequencesGenerated = True
            else:
                sequence[i] += 1
                break
    return sequences


print(generateSequences(4))
