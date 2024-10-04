def bracket(f, x1=0, s=1e-2, k=2.0):
    """
    bracket function: find a bracket of the minimum

    Parameters
    ----------
    f : function
        The function to minimize
    x1 : float
        Initial guess
    s : float
        Step size
    k : float
        Expansion factor

    Returns
    -------
    tuple
        A tuple of the form (x1, x2, x3, f1, f2, f3)
        where x1>x2>x3 and f1>f2<f3
    """
    f1 = f(x1)
    x2 = x1 + s
    f2 = f(x2)
    if f2 > f1:
        x1, x2 = x2, x1
        f1, f2 = f2, f1
        s = -s
    while True:
        x3 = x2 + s
        f3 = f(x3)
        if f3 > f2:
            return x1, x2, x3, f1, f2, f3
        x1, x2, x3 = x2, x3, x3 + s
        f1, f2, f3 = f2, f3, f(x3)
        s *= k


def f(x):
    return x**2


x1, x2, x3, f1, f2, f3 = bracket(f, -1)
print(f"x1={x1}, x2={x2}, x3={x3}, f1={f1}, f2={f2}, f3={f3}")


def bisection(f, a, b, tol=1e-6):
    """
    Bisection method: root finding algorithm

    Parameters
    ----------
    f : function
        The function to find the root of
    a : float
        Lower bound of the interval
    b : float
        Upper bound of the interval
    tol : float
        Tolerance

    Returns
    -------
    tuple
        A tuple of the form (a, b)
        where f(a) and f(b) have opposite signs
    """

    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if f(a) == 0:
        return a, a
    if f(b) == 0:
        return b, b

    while b - a > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m, m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return a, b


def f(x):
    return x**2 - 4


a, b = bisection(f, 0, 3)
print(f"a={a}, b={b}")
