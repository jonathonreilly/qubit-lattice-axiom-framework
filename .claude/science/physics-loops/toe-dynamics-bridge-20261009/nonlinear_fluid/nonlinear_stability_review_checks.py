#!/usr/bin/env python3
"""Independent finite algebra for a source-bound nonlinear-stability review.

No repository imports or author-runner code. Four-element subsets and their
three pairings enumerate collisions. Rational full-space solves determine heat
and off-diagonal responses; a computed Krylov plane determines the diagonal
response. These checks do not prove the infinite-dimensional energy estimate.
"""
from fractions import Fraction as F
from itertools import product, combinations
from functools import reduce
from math import gcd, lcm

V = list(product((-1, 0, 1), repeat=3))
n = len(V)
energy = [sum(t*t for t in v) for v in V]
M = [F(2, 3)**(3-e)*F(1, 6)**e for e in energy]
zero = lambda: [F(0)]*n
one = [F(1)]*n


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(c, a):
    return [c*x for x in a]


def inner(a, b):
    return sum((w*x*y for w, x, y in zip(M, a, b)), F(0))


def pp(a):
    r = inner(one, a)
    ee = inner(energy, a)
    jj = [inner([v[d] for v in V], a) for d in range(3)]
    return [r*F(5-3*e, 2)+3*sum(j*x for j, x in zip(jj, v))
            +F(3, 2)*ee*(e-1) for v, e in zip(V, energy)]


def moments(a):
    return [inner(one, a)]+[inner([v[d] for v in V], a) for d in range(3)]+[inner(energy, a)]


def key(pair):
    i, j = pair
    return tuple(V[i][d]+V[j][d] for d in range(3))+(energy[i]+energy[j],)


def axis(pair):
    i, j = pair
    dif = [abs(V[i][d]-V[j][d]) for d in range(3)]
    return dif.index(2) if sorted(dif) == [0, 0, 2] else None


reactions = []
for a, b, c, d in combinations(range(n), 4):
    for inp, out in [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]:
        if key(inp) != key(out):
            continue
        i, j = inp
        k, ell = out
        ia, oa = axis(inp), axis(out)
        axial = ia is not None and oa is not None and ia != oa
        nu = zero()
        for ix, s in [(i, -1), (j, -1), (k, 1), (ell, 1)]:
            nu[ix] = F(s)
        assert moments([x/w for x, w in zip(nu, M)]) == [0]*5
        assert M[i]*M[j] == M[k]*M[ell]
        reactions.append((i, j, k, ell, axial, nu, M[i]*M[j]))
assert len(reactions) == 288
assert sum(r[4] for r in reactions) == 9


def bb(x, which="unit"):
    out = zero()
    for i, j, k, ell, axial, nu, q in reactions:
        if which == "base" and axial or which == "axial" and not axial:
            continue
        coeff = q*(x[k]+x[ell]-x[i]-x[j])
        if not coeff:
            continue
        out = add(out, [coeff*z/w for z, w in zip(nu, M)])
    return out


def gamma(x, y):
    out = zero()
    for i, j, k, ell, axial, nu, q in reactions:
        coeff = q*F(1, 2)*(x[i]*y[j]+x[j]*y[i]-x[k]*y[ell]-x[ell]*y[k])
        if not coeff:
            continue
        out = add(out, [coeff*z/w for z, w in zip(nu, M)])
    return out


def solve(a, b):
    a = [list(row)+[rhs] for row, rhs in zip(a, b)]
    for c in range(len(b)):
        pivot = next(r for r in range(c, len(b)) if a[r][c])
        a[c], a[pivot] = a[pivot], a[c]
        piv = a[c][c]
        a[c] = [x/piv for x in a[c]]
        for r in range(len(b)):
            if r == c or not a[r][c]:
                continue
            q = a[r][c]
            a[r] = [x-q*y for x, y in zip(a[r], a[c])]
    return [row[-1] for row in a]


basis = [one]+[[F(v[d]) for v in V] for d in range(3)]+[list(map(F, energy))]
for i, j in combinations(range(5), 2):
    assert gamma(basis[i], basis[j]) == bb([x*y/2 for x, y in zip(basis[i], basis[j])])
for x in basis:
    assert bb(x) == zero()
    assert gamma(x, x) == bb([t*t/2 for t in x])
for i in range(n):
    x = zero()
    x[i] = F(1)
    assert pp(pp(x)) == pp(x)
    assert moments(x) == moments(pp(x))
    for j in range(n):
        y = zero()
        y[j] = F(1)
        assert moments(gamma(x, y)) == [0]*5

slow = [[F(5-3*e, 2) for e in energy]]+[[F(3*v[d]) for v in V] for d in range(3)]
checked_coeffs = 0
for a in range(4):
    for b in range(a, 4):
        h = [x*y/(2 if a == b else 1) for x, y in zip(slow[a], slow[b])]
        h = add(h, scale(-1, pp(h)))
        assert moments(h) == [0]*5
        for i in range(3):
            heat = inner([e*v[i] for e, v in zip(energy, V)], h)
            target = -F(2, 3) if a == 0 and b == i+1 else 0
            assert heat == target
            for j in range(3):
                stress = inner([v[i]*v[j] for v in V], h)
                target = F(0)
                if a and b:
                    if a == b:
                        target = F(int(i == j == a-1))-F(int(i == j), 3)
                    else:
                        target = F(int((i, j) in [(a-1, b-1), (b-1, a-1)]))
                assert stress == target
        checked_coeffs += 1

cols = []
for i in range(n):
    x = zero()
    x[i] = F(1)
    cols.append(add(bb(x), pp(x)))
bp = [[cols[j][i] for j in range(n)] for i in range(n)]
heat_source = [F(v[0])*(e-F(5, 3)) for v, e in zip(V, energy)]
off_source = [F(v[0]*v[1]) for v in V]
responses = []
for source in (heat_source, off_source):
    sol = solve(bp, source)
    assert pp(sol) == zero()
    assert bb(sol) == source
    assert bb(sol, "axial") == zero()
    responses.append(inner(source, sol))
chi, muo = responses
assert chi == F(40, 441) and muo == F(67, 1083)

diag_source = [F(v[0]**2-v[1]**2, 2) for v in V]
krylov = [diag_source, bb(diag_source, "base")]
ii, jj = next((i, j) for i, j in combinations(range(n), 2)
              if krylov[0][i]*krylov[1][j] != krylov[0][j]*krylov[1][i])


def coords(x):
    coeff = solve([[krylov[k][r] for k in range(2)] for r in (ii, jj)], [x[ii], x[jj]])
    assert x == add(scale(coeff[0], krylov[0]), scale(coeff[1], krylov[1]))
    return coeff


dc = {}
for which in ("base", "axial"):
    columns = [coords(bb(x, which)) for x in krylov]
    dc[which] = [[columns[j][i] for j in range(2)] for i in range(2)]
d = [[[dc["base"][i][j], dc["axial"][i][j]] for j in range(2)] for i in range(2)]


def mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def sub(p, q):
    return [(p[i] if i < len(p) else 0)-(q[i] if i < len(q) else 0) for i in range(max(len(p), len(q)))]


det = sub(mul(d[0][0], d[1][1]), mul(d[0][1], d[1][0]))
s00, s01 = [inner(diag_source, x) for x in krylov]
num = sub([s00*x for x in d[1][1]], [s01*x for x in d[1][0]])
iso = sub(num, [muo*x for x in det])
den = lcm(*(x.denominator for x in iso))
ints = [int(x*den) for x in iso]
divisor = reduce(gcd, ints)
ints = [x//divisor for x in ints]
if ints[-1] < 0:
    ints = [-x for x in ints]
assert ints == [-22183, 4579, 536]
assert sum(num)/sum(det) != muo  # Unit-rate isotropy must be rejected.
vx = [F(v[0]) for v in V]
evx = [e*x for e, x in zip(energy, vx)]
nu = muo/inner(vx, vx)
energy_flux_per_j = inner(evx, slow[1])
thermal_stream = [x*a for x, a in zip(vx, slow[0])]
heat_source_factor = inner(heat_source, thermal_stream)/inner(heat_source, heat_source)
assert thermal_stream == scale(heat_source_factor, heat_source)
thermal_diffusion = -heat_source_factor*chi/energy_flux_per_j
quadratic_cross = [x*y for x, y in zip(slow[0], slow[1])]
quadratic_cross = add(quadratic_cross, scale(-1, pp(quadratic_cross)))
thermal_advection = -inner(evx, quadratic_cross)/energy_flux_per_j
assert nu == F(67, 361) and thermal_diffusion == F(4, 49)
assert thermal_advection == F(2, 5)

# A periodic shear j=(sin(y)+cos(y),0,0), evaluated at y=0, has
# partial_y |j|^2=2. Omitting |j|^2 from E1 leaves a y-momentum residual.
shear_u = slow[1]
shear_uy = slow[1]
quadratic_derivative = [x*y for x, y in zip(shear_u, shear_uy)]
quadratic_derivative = add(quadratic_derivative, scale(-1, pp(quadratic_derivative)))
wrong_pressure_residual = inner([F(v[1]**2) for v in V], quadratic_derivative)
corrected_pressure_residual = wrong_pressure_residual+2*inner(vx, shear_u)*inner(vx, shear_uy)/3
assert wrong_pressure_residual != 0 and corrected_pressure_residual == 0
test_u = [sum(x) for x in zip(*slow)]
assert gamma(test_u, test_u) != scale(-1, bb([x*x/2 for x in test_u]))

print('four-distinct-velocity enumeration:', len(reactions), 'reactions;', sum(r[4] for r in reactions), 'axial')
print('complete bilinear conservation:', n*n, 'coordinate-basis pairs; equilibrium polarization: all 15 kernel pairs')
print('slow quadratic moment coefficients:', checked_coeffs, 'complete coefficients, all stress and heat components')
print('full 27-dimensional rational solves: chi =', chi, '; mu_off =', muo)
print('independently computed Krylov isotropy polynomial:', ints, '(ascending coefficients)')
print('viscosity =', nu, '; density diffusion =', thermal_diffusion, '; thermal advection =', thermal_advection)
print('wrong controls rejected: unit-rate isotropy, reversed quadratic collision sign, missing pressure correction', wrong_pressure_residual)
print('scope: exact finite velocity algebra only; no analytic Sobolev, continuation, or convergence proof is executed')
