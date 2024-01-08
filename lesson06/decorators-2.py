def validate(func):
    def wrapper(*args, **kwargs):
        values = args + tuple(kwargs.values())
        for value in values:
            if type(value) not in (int, float):
                raise ValueError('Values must be int or float')

        return func(*args, **kwargs)

    return wrapper

@validate
def add_values(*args, **kwargs):
    print(kwargs)
    return sum(args + tuple(kwargs.values()))


print(add_values(5, 6, c=6))
