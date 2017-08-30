import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

def sum_pairs(ints, s):

    ind = 1
    sol = []

    for i in ints:

        for n in ints[ind:]:

            if i + n == s:

                sol.append([i,n, ints[ind:].index(n) + ind])

        ind += 1

    if not sol:

        return None

    else:

        return sorted(sol, key=lambda x: x[2])[0][:-1]

@timeit
def funct():

    num_lists = [[[1, 4, 8, 7, 3, 15], 8],
                 [[1, -2, 3, 0, -6, 1], -6],
                 [[20, -13, 40], -7],
                 [[1, 2, 3, 4, 1, 0], 2],
                 [[10, 5, 2, 3, 7, 5], 10],
                 [[4, -2, 3, 3, 4], 8],
                 [[0, 2, 0], 0],
                 [[5, 9, 13, -3], 10]]

    for i in num_lists:

        print(sum_pairs(i[0], i[1]))

funct()
