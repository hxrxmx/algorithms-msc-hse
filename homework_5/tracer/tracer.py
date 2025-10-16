def tracer(fun):
    def wrapper(*args, **kwargs):
        print(f"function '{fun.__name__}' called with args: {args}, {kwargs}")
        res = fun(*args, **kwargs)
        print(f"function '{fun.__name__}' returned {res}")
        return res

    return wrapper
