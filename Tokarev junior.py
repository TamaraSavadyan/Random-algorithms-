import copy

k = 0


def flip(d, a):
    #  initialBoxes = copy.deepcopy(a)
    if d == 'R':
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                delta = a[i + 1] - a[i]
                a[i] -= delta
                a[i + 1] += delta
                print(k, "processing", i)
            else:
                print(k, "processing", i)
            '''
    else:
        for i in range(n + 1):
            if i != n and a[n - i] < a[n - (i + 1)]:
                a[i + 1] += a[i + 1] - a[i]
            '''
            '''
    if a != initialBoxes:
        k += 1
        flip(d, a)
    else:
    '''
        return a


print(flip('R', [3, 2, 1, 2]))  # [1, 2, 2, 3]

# print(flip('L', [1, 4, 5, 3, 5]))  # [5, 5, 4, 3, 1]
