from functools import wraps

def val_checker(Check_func):
    def val_checker_(func):
        @wraps(func)
        def wrapper(x):
            if Check_func(x):
                return func(x)
            else:
                raise ValueError
        return wrapper
    return val_checker_

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
