#!/usr/bin/env python3
"""Independent sparse Laurent-polynomial checks of the cutoff/alias argument.

No author runner or repository code is imported. Exact rational convolution
and integer residue maps are used instead of a complex-valued spatial DFT.
The interpolation check integrates an actual one-dimensional cell field;
the all-grid analytic estimate is supplied separately in the review.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict
from math import cos, sin, pi, sqrt

V = list(product((-1, 0, 1), repeat=3))
ev = [sum(x*x for x in v) for v in V]
M = [F(2, 3)**(3-e)*F(1, 6)**e for e in ev]
R = []
for a, b, c, d in combinations(range(27), 4):
    for i, j, k, l in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):
        if ev[i]+ev[j] == ev[k]+ev[l] and all(V[i][s]+V[j][s] == V[k][s]+V[l][s] for s in range(3)):
            R.append((i, j, k, l))
assert len(R) == 288

def reaction_key(i, j, k, l):
    return tuple(sorted((tuple(sorted((i, j))), tuple(sorted((k, l))))))

axial = set()
for c in range(3):
    a, b = [d for d in range(3) if d != c]
    for shift in (-1, 0, 1):
        ids = []
        for d in (a, b):
            for sign in (-1, 1):
                v = [0, 0, 0]
                v[c], v[d] = shift, sign
                ids.append(V.index(tuple(v)))
        axial.add(reaction_key(*ids))
assert len(axial) == 9
assert axial <= {reaction_key(*r) for r in R}
trace_coeff, sum_coeff = [F(0), F(0)], [F(0), F(0)]
for r in R:
    i, j, k, l = r
    index = int(reaction_key(*r) in axial)
    q = M[i]*M[j]
    sum_coeff[index] += q
    trace_coeff[index] += q*sum(F(1)/M[t] for t in r)
assert trace_coeff == [F(124, 3), F(4, 3)]
assert sum_coeff == [F(97, 432), F(1, 54)]

def gamma(a, b):
    out = [F(0) for _ in V]
    for i, j, k, l in R:
        c = M[i]*M[j]*(a[i]*b[j]+a[j]*b[i]-a[k]*b[l]-a[l]*b[k])/2
        for t, sign in ((i, -1), (j, -1), (k, 1), (l, 1)):
            out[t] += sign*c/M[t]
    return out

def fold(k, m):
    a = (m-1)//2
    return tuple((x+a) % m-a for x in k)

def weight(k, s):
    return (1+sum(x*x for x in k))**s

def norm2(poly, s):
    return sum((weight(k, s)*sum(M[v]*x*x for v, x in enumerate(a)) for k, a in poly.items()), F(0))

geometry = []
for m in (3, 5, 7, 9):
    a = (m-1)//2
    fibers = defaultdict(list)
    for q in product(range(-2*a, 2*a+1), repeat=3):
        k = fold(q, m)
        assert all(abs(kd) <= abs(qd) for kd, qd in zip(k, q))
        if q != k:
            fibers[k].append(q)
            assert max(abs(x) for x in q) >= (m+1)//2
    maximum = max(map(len, fibers.values()))
    assert maximum == 7
    geometry.append((m, maximum))

# A real principal Fourier polynomial with two different invariant-valued
# amplitudes. Its quadratic collision output contains several aliased modes.
m = 3
p, q = (1, 1, 1), (-1, 1, -1)
A = [F(5-3*e, 2) for e in ev]
a = [(A[t]+3*v[0])/2 for t, v in enumerate(V)]
b = [(2*A[t]+3*v[1])/2 for t, v in enumerate(V)]
H = {p: a, tuple(-x for x in p): a, q: b, tuple(-x for x in q): b}
poly = defaultdict(lambda: [F(0) for _ in V])
for k, ak in H.items():
    for l, bl in H.items():
        out = gamma(ak, bl)
        kl = tuple(x+y for x, y in zip(k, l))
        for v in range(27):
            poly[kl][v] += out[v]
tail = {k: a for k, a in poly.items() if fold(k, m) != k}
alias = defaultdict(lambda: [F(0) for _ in V])
for k, ak in tail.items():
    for v in range(27):
        alias[fold(k, m)][v] += ak[v]
alias2, tail4, full6 = norm2(alias, 4), norm2(tail, 4), norm2(poly, 6)
sigma = F(1, 1+((m+1)//2)**2)
assert alias2 > 0 and tail4 > 0  # dropping the alias term changes the grid product
assert alias2 <= 7*tail4 <= 26*tail4
assert tail4 <= sigma*sigma*full6
invariants = [[F(1) for v in V], *[[F(v[d]) for v in V] for d in range(3)], list(map(F, ev))]
for ak in alias.values():
    for inv in invariants:
        assert sum(M[v]*inv[v]*ak[v] for v in range(27)) == 0

# Exact mass of the cutoff initial law: all nonzero principal Fourier modes
# have zero finite-grid mean. Aliased continuum mass is excluded by cutoff.
# These equalities test the velocity part of the coefficient 27 independently.
assert sum(A) == F(-27, 2)
assert sum(M[t]*A[t] for t in range(27)) == 1
assert all(sum(v[d] for v in V) == 0 for d in range(3))

# Actual centered-cell midpoint quadrature of I_m g-J_m g, using a real scalar
# polynomial with distinct principal frequencies. No phase average is used
# in the quadrature itself. The exact integral is then evaluated separately.
mi = 5
ell = 2*pi/mi
def field(x):
    return cos(x)+0.5*sin(2*x)
def quad(nodes):
    total = 0.0
    for z in range(mi):
        center = ell*z
        const = field(center)
        for j in range(nodes):
            y = ell*((j+0.5)/nodes-0.5)
            total += (const-field(center+y))**2
    return total/(mi*nodes)
def sinc(x):
    return sin(x)/x
phase_integral = (1-sinc(ell/2))+F(1, 4)*(1-sinc(ell))
q1, q2 = quad(2000), quad(4000)
assert abs(q2-phase_integral) < abs(q1-phase_integral)/3.9
assert abs(q2-phase_integral) < 1e-8
h1_square = F(2, 2)+F(5, 8)  # cos(x) and 0.5 sin(2x)
assert phase_integral <= 3*ell*ell*float(h1_square)

print('integer alias fibers (m,max noncentral):', geometry)
print('geometric axial count:', len(axial), '; C_R and S coefficients of (1,alpha):', trace_coeff, sum_coeff)
print('exact nonzero quadratic alias H4 energy:', alias2)
print('exact alias/tail H4 energy ratio:', alias2/tail4)
print('tail H4 and sigma^2 H6 bounds agree; all five aliased collision moments vanish')
print('cutoff preparation velocity sums:', sum(A), sum(M[t]*A[t] for t in range(27)))
print('actual cell interpolation quadrature:', format(q2, '.16g'))
print('separate integrated phase expression:', format(float(phase_integral), '.16g'))
print('absolute quadrature discrepancy:', format(abs(q2-phase_integral), '.3g'))
print('scope: finite exact alias witnesses and scalar quadrature; analytic all-grid bounds require the written proof')
