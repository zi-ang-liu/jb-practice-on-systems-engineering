# bracket
# Given a function and distinct initial points, search in the downhill direction (as defined by the initial points) and return three points that bracket the minimum of the function.


def f(x):
    return x**2


def bracket(f, x1, x2, x3):
    if f(x1) > f(x2) and f(x2) > f(x3):
        return x1, x2, x3
    elif f(x1) < f(x2) and f(x2) < f(x3):
        return x3, x2, x1
    else:
        print("Initial points do not bracket the minimum")
