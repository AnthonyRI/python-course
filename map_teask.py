def map_rq(func, dat):
    if hasattr(dat, "__iter__"):
        return [map_rq(func, item) for item in dat]
    else:
        return func(dat)

def map_yield(func, dat):
    for each in dat:
        yield func(each)
        map_yield(func, each)


dat = [1, 2, 3, 4, 5, 6, 7, 8]


print map_rq(lambda x: x*2, dat)
print map_yield(lambda x: x*2, dat)

