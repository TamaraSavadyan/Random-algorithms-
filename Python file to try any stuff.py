pass

def pyramid(num):
    pyramid = dict()
    g = 1
    pyramid.setdefault(1, g)
    for i in range(2, num + 2):
        pyramid.setdefault(i, g * 4 * i)
