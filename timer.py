from functools import wraps
import time


def stop_watch(func):
    """
    this is decorator for function you want to measure elapsed time.
    this is declared as follows,

    @stop_watch
    def brabra():
        pass

    then, if you call above function, print elapsed time, as follows,

    brabra()
    >>> 0.000011111 ms in brabra
    """
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print("{} ms in {}".format(elapsed_time * 1000, func.__name__))
        return result
    return wrapper
