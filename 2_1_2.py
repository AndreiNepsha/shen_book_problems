# 2_1_2
# В предложенном алгоритме используется сравнение двух массивов (x <> last).
# Устраните его, добавив булевскую переменную l
# и включив в инвариант соотношение
# l ⇔ последовательность x | последняя.
def generateSequence(n, k):
    sequences = []
    allSequencesGenerated = False
    sequence = [1] * k
    while not allSequencesGenerated:
        sequences.append(list(sequence))
        for i in reversed(range(k)):
            if sequence[i] == n:
                sequence[i] = 1
                if i == 0:
                    allSequencesGenerated = True
            else:
                sequence[i] += 1
                break
    return sequences


print(generateSequence(3, 3))
