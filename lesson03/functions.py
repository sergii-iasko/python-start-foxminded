# def say_hello(text):
#     print(text)
#
# say_hello('Hello')

# ======================================

# def some_numbers(a: float, b: float) -> float:
#     return a + b
#
# print(some_numbers(4, 5))
# ==========================================

def some_numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    return


some_numbers(4, 5, 6, name='John', surname='Doe')
