# 1.1.30. Даны натуральные числа n и k, n > 1.
# Напечатайте k десятичных знаков числа 1/n.
# (При наличии двух десятичных разложений выбирается то из них,
# которое не содержит девятки в периоде.)
# Программа должна использовать только целые переменные.


def printDecimalPlaces(n, k):
    print("0,", end="")
    dividend = 10
    while k > 0:
        while dividend != 0 and dividend // n == 0:
            dividend *= 10
            print(0, end="")
            k -= 1
        print(dividend // n, end="")
        k -= 1
        dividend = (dividend % n) * 10


printDecimalPlaces(19, 30)
