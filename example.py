from timer import stop_watch


# decorate function you want to measure elapsed time.
@stop_watch
def example_func(num):
    res = 0

    for i in range(num):
        res += i
    return res


if __name__ == "__main__":
    """
    example of timer decorater
    """
    summ = example_func(100)
    print(summ)
