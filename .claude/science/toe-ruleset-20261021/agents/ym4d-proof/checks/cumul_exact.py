#!/usr/bin/env python3
"""Serial exact finite checks; see cumul_criteria.md for prior criteria."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import os
import resource
import sys

HERE = Path(__file__).resolve().parent
PAIRS = list(combinations(range(4), 2))
CENTRES = [(F(t, 2), F(0), F(0), F(0)) for t in (-3, -1, 1, 3)]
CYCLES = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
RECORDS = []


def check(name, passed, **details):
    RECORDS.append(dict(name=name, passed=bool(passed), **details))


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def mul(a, b):
    out = {}
    for k, v in a.items():
        for l, w in b.items():
            key = tuple(sorted(k+l))
            out[key] = out.get(key, F(0)) + v*w
    return {k: v for k, v in out.items() if v}


def symbol(s):
    return {(s,): F(1)}


def partitions(items):
    if not items:
        yield []
        return
    for rest in partitions(items[1:]):
        yield [(items[0],)] + rest
        for j in range(len(rest)):
            yield rest[:j] + [(items[0],)+rest[j]] + rest[j+1:]


def gaussian_moment(items):
    if not items:
        return {(): F(1)}
    i, *rest = items
    out = mul(symbol(f'mu{i}'), gaussian_moment(rest))
    for k, j in enumerate(rest):
        out = add(out, mul(symbol(f'C{min(i,j)}{max(i,j)}'),
                           gaussian_moment(rest[:k]+rest[k+1:])))
    return out


def cumulant(items, moment):
    out = {}
    for p in partitions(tuple(items)):
        term = {(): F((-1)**(len(p)-1)*factorial(len(p)-1))}
        for block in p:
            term = mul(term, moment(tuple(sorted(block))))
        out = add(out, term)
    return out


def matrix_product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def delta(i, j):
    return int(i == j)


def curvature_derivative(z):
    s = sum(x*x for x in z)
    h = [[-F(delta(i,j), 2)/s**2 + 2*z[i]*z[j]/s**3
          for j in range(4)] for i in range(4)]
    return [[-delta(n,sig)*h[m][r] + delta(n,r)*h[m][sig]
             + delta(m,sig)*h[n][r] - delta(m,r)*h[n][sig]
             for r,sig in PAIRS] for m,n in PAIRS]


def curvature_wedge(z):
    s = sum(x*x for x in z)
    h = [[delta(i,j)-2*z[i]*z[j]/s for j in range(4)] for i in range(4)]
    return [[(h[m][r]*h[n][s2]-h[m][s2]*h[n][r])/s**2
             for r,s2 in PAIRS] for m,n in PAIRS]


def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))


STAR = [[parity(a+b) if len(set(a+b)) == 4 else 0 for b in PAIRS] for a in PAIRS]


def covariances(points):
    return {(i,j): curvature_derivative(tuple(x-y for x,y in zip(points[i],points[j])))
            for i in range(len(points)) for j in range(len(points)) if i != j}


def cycle_trace(covs, cycle):
    mat = covs[(cycle[0], cycle[1])]
    for k in range(1, len(cycle)):
        mat = matrix_product(mat, covs[(cycle[k], cycle[(k+1) % len(cycle)])])
    return trace(mat)


def pairings(legs):
    if not legs:
        yield []
        return
    i = legs[0]
    for k in range(1, len(legs)):
        j = legs[k]
        for tail in pairings(legs[1:k]+legs[k+1:]):
            yield [(i,j)]+tail


def connected_pairings(n):
    out = []
    for p in pairings(list(range(2*n))):
        edges = [(i//2, j//2) for i,j in p]
        if any(i == j for i,j in edges):
            continue
        reached = {0}
        for _ in range(n):
            for i,j in edges:
                if i in reached or j in reached:
                    reached.update((i,j))
        if len(reached) == n:
            out.append(edges)
    return out


def direct_wick(points):
    covs = covariances(points)
    total = F(0)
    matchings = connected_pairings(len(points))
    for edges in matchings:
        for components in product(range(6), repeat=len(points)):
            value = F(1)
            for i,j in edges:
                value *= covs[(i,j)][components[i]][components[j]]
                if not value:
                    break
            total += value
    return total, matchings


class Interval:
    """Closed rational intervals, every operation encloses its exact image."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, other):
        b = self.coerce(other)
        return Interval(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        b = self.coerce(other)
        vals = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = self.coerce(other)
        assert not b.lo <= 0 <= b.hi
        return self * Interval(1/b.hi, 1/b.lo)

    def __rtruediv__(self, other):
        return self.coerce(other)/self

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return Interval(low, max(self.lo**2, self.hi**2))

    def __pow__(self, n):
        assert n >= 0
        if n == 0:
            return Interval(1)
        if n == 2:
            return self.square()
        if n % 2 == 0:
            return (self**(n//2)).square()
        return self*(self**(n-1))

    def rational(self):
        return [str(self.lo), str(self.hi)]


def main():
    assert os.environ.get('CUMUL_GUARDED') == '1', 'use cumul_run.py'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    for n in (3,4):
        p = cumulant(range(n), gaussian_moment)
        check(f'formal affine Gaussian cumulant {n}', not p, terms=len(p))
    gaussian_mutant = mul(symbol('C01'), symbol('C23'))
    check('control omitted Gaussian subtraction detected', bool(gaussian_mutant))

    for z0 in ((1,0,0,0),(1,2,3,4),(2,-1,0,3)):
        z = tuple(map(F,z0))
        d, w = curvature_derivative(z), curvature_wedge(z)
        anticomm = [[x+y for x,y in zip(a,b)] for a,b in
                    zip(matrix_product(STAR,d),matrix_product(d,STAR))]
        norm = sum(x*x for row in d for x in row)
        check(f'curvature identities {z0}', d == w and
              norm == 6/sum(x*x for x in z)**4 and
              all(x == 0 for row in anticomm for x in row), norm=str(norm))

    covs = covariances(CENTRES)
    two, p2 = direct_wick(CENTRES[1:3])
    three, p3 = direct_wick(CENTRES[:3])
    four, p4 = direct_wick(CENTRES)
    traces = [cycle_trace(covs,c) for c in CYCLES]
    four_cycle = 16*sum(traces)
    edge_classes = {}
    for p in p4:
        edges = tuple(sorted(tuple(sorted(e)) for e in p))
        edge_classes[edges] = edge_classes.get(edges,0)+1
    check('connected pairing counts', (len(p2),len(p3),len(p4)) == (2,8,48)
          and sorted(edge_classes.values()) == [16,16,16],
          counts=[len(p2),len(p3),len(p4)], cycle_multiplicities=list(edge_classes.values()))
    check('two-point independent check', two == 12 == 2*cycle_trace(covs,(1,2)), value=str(two))
    check('three-point collinear cancellation', three == 0 == 8*cycle_trace(covs,(0,1,2)), value=str(three))
    triangle = [tuple(map(F,p)) for p in ((0,0,0,0),(1,0,0,0),(0,1,1,0))]
    three_other, _ = direct_wick(triangle)
    check('three-point noncollinear cancellation', three_other == 0 ==
          8*cycle_trace(covariances(triangle),(0,1,2)), value=str(three_other))
    check('four-point exact independent contraction', four == four_cycle == F(169,108),
          value=str(four), cycle_traces=[str(t) for t in traces])
    check('point quotient', four/two**2 == F(169,15552), value_per_inverse_colour=str(four/two**2))
    check('control wrong cycle factor detected', four != 8*sum(traces))
    check('control omitted cycle detected', all(four != 16*(sum(traces)-t) for t in traces))

    eps = F(1,10000)
    icovs = {(i,j): curvature_derivative(tuple(Interval(x-y-2*eps,x-y+2*eps)
              for x,y in zip(CENTRES[i],CENTRES[j])))
              for i in range(4) for j in range(4) if i != j}
    a4 = 16*sum(cycle_trace(icovs,c) for c in CYCLES)
    b2 = 2*cycle_trace(icovs,(1,2))
    ratio = a4/(b2**2)
    check('smooth four-point positive interval', F(3,2) < a4.lo <= a4.hi < F(5,3),
          interval=a4.rational(), certified_outer=['3/2','5/3'])
    check('smooth two-point positive interval', 11 < b2.lo <= b2.hi < 13,
          interval=b2.rational(), certified_outer=['11','13'])
    check('smooth ratio interval', F(3,338) < ratio.lo <= ratio.hi < F(5,363),
          interval=ratio.rational(), certified_outer_per_inverse_colour=['3/338','5/363'])

    def original_moment(items):
        return symbol('m'+''.join(map(str,items))) if items else {(): F(1)}

    for a in (F(-3,2),F(2,3)):
        b = F(7,5)
        def affine_moment(items):
            out = {}
            for k in range(len(items)+1):
                for chosen in combinations(items,k):
                    out = add(out,scale(original_moment(chosen),a**k*b**(len(items)-k)))
            return out
        for n in (2,3,4):
            check(f'affine cumulant scaling n={n} a={a}',
                  cumulant(range(n),affine_moment) == scale(cumulant(range(n),original_moment),a**n))
        check(f'ratio rescaling a={a}', a**4*four/(a**2*two)**2 == four/two**2)

    result = dict(kind='finite exact algebra and rational interval certificate; no YM estimate',
                  criteria_sha256=hashlib.sha256((HERE/'cumul_criteria.md').read_bytes()).hexdigest(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  arithmetic='fractions.Fraction; interval endpoints exact rationals',
                  tests=RECORDS, passed=all(r['passed'] for r in RECORDS),
                  rejected_candidate={'nonzero free scalar F2 third cumulant':
                                      'FAILED: exact coefficient is zero'},
                  nice=os.getpriority(os.PRIO_PROCESS,0),
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(result,indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
