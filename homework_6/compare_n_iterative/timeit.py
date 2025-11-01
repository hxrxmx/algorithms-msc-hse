import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} was executed in {end - start:.6f}.")
        return res

    return wrapper
