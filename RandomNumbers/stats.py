# критерий монотонности
def mono_test(arr):
    n = len(arr) - 1
    h = 0
    l = 0

    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) > 0:
            h += 1
        else:
            l += 1

    h /= n
    l /= n

    return abs(h - l)

# тест на частоту знаков
def num_freq_test(arr):
    n = len(arr)
    C = [0]*10

    for i in range(n):
        t = str(i)
        for j in t:
            C[int(j)] += 1

    for i in C:
        i -= 0.1
        i /= sum(C)

    return max(C) + abs(min(C))

def freq_test(arr):

    m = 1/2  #мат ожидание массива (идеальный случай)

    l = 0
    r = 0

    for i in arr:
        if i < m:
            l += 1
        else:
            r += 1

    l /= len(arr)
    r /= len(arr)

    # насколько слева чисел больше чем справа
    return abs(l - r)
