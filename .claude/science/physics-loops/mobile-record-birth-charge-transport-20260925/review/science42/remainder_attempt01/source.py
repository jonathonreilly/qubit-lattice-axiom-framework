#!/usr/bin/env python3
"""Fresh rational Taylor-interval checks; no historical/author runtime imports."""
from fractions import Fraction as Q
from itertools import product
from math import factorial
import json


def cos_interval(x):
    polynomial = sum(((-1)**n)*x**(2*n)/factorial(2*n) for n in range(6))
    radius = abs(x)**12/factorial(12)
    return polynomial-radius, polynomial+radius


def exact(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, (list,tuple)):
        return [exact(v) for v in x]
    if isinstance(x, dict):
        return {k:exact(v) for k,v in x.items()}
    return x


def main():
    rows = []
    for r, direction in product((Q(1,32), Q(1,8), Q(1,2), Q(1)),
                                ((1,0,0),(1,1,0),(1,1,1),(1,2,Q(-1,2)))):
        k = tuple(r*v for v in direction)
        intervals = [cos_interval(x) for x in k]
        lower = Q(4,3)*sum(1-hi for lo,hi in intervals)
        upper = Q(4,3)*sum(1-lo for lo,hi in intervals)
        quadratic = Q(2,3)*sum(x*x for x in k)
        quartic = Q(1,18)*sum(x**4 for x in k)
        sixth = Q(1,540)*sum(abs(x)**6 for x in k)
        assert quadratic-quartic <= lower <= upper <= quadratic
        assert quadratic-quartic-sixth <= lower <= upper <= quadratic-quartic+sixth
        rows.append(dict(k=k, rigorous_second_moment_interval=[lower,upper],
                         quadratic=quadratic, quartic_correction=quartic,
                         sixth_error_bound=sixth,
                         quadratic_error_interval=[quadratic-upper,quadratic-lower],
                         all_interval_inclusions=True))
    print(json.dumps(exact(dict(status='all rational interval assertions passed',
                                cosine_truncation_degree=10,cosine_error_degree=12,
                                rows=rows,group_count=len(rows))),indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
