def validate(func):
    def wrapper(a, b):
        if type(a) not in (int, float) or type(b) not in (int, float):
            raise ValueError('Values must be int or float')

        return func(a, b)

    return wrapper

@validate
def add_values(a, b):
    return a + b


def sub_values(a, b):
    return a - b

print(add_values('5', 6))
