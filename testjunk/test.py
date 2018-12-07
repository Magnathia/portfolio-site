import math



def devation(list):
    base = 0
    for value in list:
        base += value
    return base / len(list)

def population_devation(list):
    base = devation(list)
    # print('The base is: ', base)
    devation_squared = []
    sum_squared = 0
    for value in list:
        # print("working value is:", value - base)
        squared = (value - base)**2
        devation_squared.append(squared)
    # print(devation_squared)
    for value in devation_squared:
        sum_squared += value
    # print('The squared total is: ', sum_squared)
    final = math.sqrt(sum_squared / len(list))
    return final


def percentile(list, percent):
    ascending_list = sorted(list)
    pos = math.ceil(len(ascending_list) * (percent/100))
    return(ascending_list[pos-1])


def porabola(modifier):
    for x in range(-2, 3):
        y = x**2 + 1
        print(x, '', y)


from math import sqrt
from fractions import Fraction, gcd

def factorize_quadratic(a, b, c):
    """Factorize the quadratic expression ax^2 + bx + c over the
    rational numbers and print the factorization. If this is not
    possible, raise ValueError.

        >>> factorize_quadratic(1, 3, 2)
        (x + 1)(x + 2)
        >>> factorize_quadratic(1, 3, 0)
        x(x + 3)
        >>> factorize_quadratic(2, -9, -5)
        (2x + 1)(x - 5)
        >>> factorize_quadratic(4, -12, 8)
        4(x - 1)(x - 2)
        >>> factorize_quadratic(1, -2, 1)
        (x - 1)^2
        >>> factorize_quadratic(5, 0, 0)
        5x^2
        >>> factorize_quadratic(1, 3, 1)
        Traceback (most recent call last):
          ...
        ValueError: No factorization over the rationals.

    """
    # Extract common factor, if any.
    f = abs(gcd(gcd(a, b), c))
    a, b, c = a // f, b // f, c // f

    # Is the discriminant a perfect square?
    discriminant = b * b - 4 * a * c
    root = int(sqrt(discriminant))
    if root * root != discriminant:
        raise ValueError("No factorization over the rationals.")

    # The two roots of the quadratic equation.
    r, s = Fraction(-b - root, 2 * a), Fraction(-b + root, 2 * a)

    # Sort the roots by absolute value. (This step is purely for
    # the readability of the printed output: the intention is that
    # we get "x(x + 1)" instead of "(x + 1)x", and "(x + 1)(x + 2)"
    # instead of "(x + 2)(x + 1)".)
    r, s = sorted((r, s), key=abs)

    # Self-test: check that the factorization is correct.
    assert(r.denominator * s.denominator == a)
    assert(r.denominator * s.numerator + r.numerator * s.denominator == -b)
    assert(r.numerator * s.numerator == c)

    def maybe(x):
        if x == -1: return '-'
        if x == 1: return ''
        return x

    def factor(r):
        if r == 0: return "x"
        n, d = r.numerator, r.denominator
        return "({}x {} {})".format(maybe(d), '-+'[n < 0], abs(n))

    if r == s:
        print("{}{}^2".format(maybe(f), factor(r)))
    else:
        print("{}{}{}".format(maybe(f), factor(r), factor(s)))


factorize_quadratic(3, 30, -72)
