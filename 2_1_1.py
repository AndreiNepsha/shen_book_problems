# 2_1_1
# Напечатайте все последовательности длины k из чисел 1..n
def generateSequence(n, k):
    endSequence = [n] * k
    sequence = [1] * k
    result = [list(sequence)]
    while sequence != endSequence:
        for i in reversed(range(len(sequence))):
            if sequence[i] == n:
                sequence[i] = 1
                continue
            else:
                sequence[i] += 1
                break
        result.append(list(sequence))
    return result


sequences = generateSequence(3, 3)
print(sequences)
