# 2.2.1. Напечатайте все перестановки чисел 1..n
# (то есть последовательности длины n, в которые каждое
# из этих чисел входит по одному разу).

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
#
# 4 3 2 1


def swap(a, i1, i2):
    tmp = a[i1]
    a[i1] = a[i2]
    a[i2] = tmp


def generateSetSwaps(n):
    swaps = []
    setSwap = [i for i in range(1, n+1)]
    lastSwap = list(reversed(setSwap))
    while True:
        swaps.append(list(setSwap))
        if setSwap == lastSwap:
            break

        for i in reversed(range(n-1)):
            if setSwap[i] < setSwap[i+1]:
                minInd = i+1
                for g in range(i+2, n):
                    if setSwap[i] < setSwap[g] < setSwap[minInd]:
                        minInd = g
                swap(setSwap, i, minInd)
                setSwap = setSwap[:i+1] + list(reversed(setSwap[i+1:]))
                break
    return swaps


print(generateSetSwaps(3))
