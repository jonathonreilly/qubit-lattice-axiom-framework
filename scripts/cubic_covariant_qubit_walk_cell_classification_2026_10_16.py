#!/usr/bin/env python3
"""Exact classification of covariant one-qubit unitary walks on the 27-point cell.

A walk is U(k) = sum_n A_n exp(i k.n) on l2(Z^3) (x) C^2 with n in {-1,0,1}^3.
Soldered covariance under a rotation group H <= O means
A_{Rn} = D(R) A_n D(R)^dagger with D the spin-1/2 lift. For H without a nonzero
fixed vector, det U is constant and U is a constant phase times
V = f + i g.sigma with f H-invariant, g H-equivariant real trig polynomials and
f^2 + |g|^2 = 1 identically. This runner builds those families exactly
(Reynolds averaging over the group), reduces the identity to coefficient
equations, and certifies the solution sets with Groebner bases over Q.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

C = sp.symbols('c1:4')
S = sp.symbols('s1:4')


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def reduce_trig(expr):
    """Normal form modulo s_a^2 = 1 - c_a^2 (degree <= 1 in each s_a)."""
    e = sp.expand(expr)
    while True:
        poly = sp.Poly(e, *S)
        new = 0
        changed = False
        for mon, coef in poly.terms():
            term = coef
            for a, p in enumerate(mon):
                q, r = divmod(p, 2)
                if q:
                    changed = True
                term *= (1 - C[a] ** 2) ** q * S[a] ** r
            new += term
        e = sp.expand(new)
        if not changed:
            return e


def proper_cubic():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if M.det() == 1:
                out.append(M)
    return out


def key(M):
    return tuple(int(x) for x in M)


def closure(gens):
    found = {key(sp.eye(3)): sp.eye(3)}
    frontier = [sp.eye(3)]
    while frontier:
        nxt = []
        for A in frontier:
            for g in gens:
                B = A * g
                if key(B) not in found:
                    found[key(B)] = B
                    nxt.append(B)
        frontier = nxt
    return list(found.values())


RZ = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RX = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
C3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
HFD = sp.Matrix([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])
GROUPS = {
    'O': [RZ, RX],
    'T': [C3, RZ ** 2],
    'D4': [RZ, RX ** 2],
    'D3': [C3, HFD],
    'D2': [RZ ** 2, RX ** 2],
}


def act(expr, M):
    """f(k) -> f(M k) for a signed permutation matrix M."""
    sub = {}
    for i in range(3):
        j = next(jj for jj in range(3) if M[i, jj] != 0)
        sub[C[i]] = C[j]
        sub[S[i]] = M[i, j] * S[j]
    return sp.expand(sp.sympify(expr).subs(sub, simultaneous=True))


def cell_functions():
    per = [[1, C[a], S[a]] for a in range(3)]
    return [sp.expand(x * y * z) for x, y, z in itertools.product(*per)]


def independent_rows(vectors):
    """Indices of a maximal linearly independent subset (exact rref)."""
    keys = sorted({k for v in vectors for k in v})
    M = sp.Matrix([[v.get(k, 0) for k in keys] for v in vectors])
    _, piv = M.T.rref()
    return list(piv)


def scalar_basis(group, funcs):
    avgs = [sp.expand(sum(act(m, M) for M in group) / len(group)) for m in funcs]
    avgs = [a for a in avgs if a != 0]
    coeff = [sp.Poly(reduce_trig(a), *C, *S).as_dict() for a in avgs]
    return [avgs[i] for i in independent_rows(coeff)]


def coin_action(R, kind='full'):
    """Soldering-menu actions O -> SO(3): trivial, sign twist, axis, full."""
    P = R.applyfunc(abs)
    sg = int(P.det())
    return {'trivial': sp.eye(3), 'sign': sp.diag(1, sg, sg), 'axis': sg * P, 'full': R}[kind]


def vector_basis(group, funcs, kind='full'):
    vecs = []
    for m in funcs:
        for a in range(3):
            h = [sp.Integer(0)] * 3
            h[a] = m
            tot = sp.zeros(3, 1)
            for M in group:
                tot += coin_action(M, kind).T * sp.Matrix([act(x, M) for x in h])
            tot = sp.expand(tot / len(group))
            if any(t != 0 for t in tot):
                vecs.append(tot)
    coeff = []
    for v in vecs:
        d = {}
        for i, x in enumerate(v):
            for mon, val in sp.Poly(reduce_trig(x), *C, *S).as_dict().items():
                d[(i,) + mon] = val
        coeff.append(d)
    return [vecs[i] for i in independent_rows(coeff)]


def unitarity_ideal(group, kind='full'):
    funcs = cell_functions()
    fb = scalar_basis(group, funcs)
    gb = vector_basis(group, funcs, kind)
    a = sp.symbols(f'a0:{len(fb)}')
    b = sp.symbols(f'b0:{len(gb)}')
    f = sum(x * e for x, e in zip(a, fb))
    g = [sum(b[j] * gb[j][i] for j in range(len(gb))) for i in range(3)]
    eqs = list(sp.Poly(reduce_trig(f ** 2 + sum(x ** 2 for x in g) - 1), *C, *S).as_dict().values())
    return fb, gb, a, b, eqs


def fixed_vectors_zero(group) -> bool:
    rows = sp.Matrix.vstack(*[M - sp.eye(3) for M in group])
    return rows.nullspace() == []


def in_radical(G, v, max_power=8) -> bool:
    return any(G.contains(v ** p) for p in range(1, max_power + 1))


def main() -> int:
    checks = Checks()
    O = proper_cubic()
    checks.check('proper cubic group has order 24', len(O) == 24)
    groups = {name: closure(gens) for name, gens in GROUPS.items()}
    expected_orders = {'O': 24, 'T': 12, 'D4': 8, 'D3': 6, 'D2': 4}
    for name, grp in groups.items():
        checks.check(f'{name} has order {expected_orders[name]}', len(grp) == expected_orders[name])
        checks.check(f'{name} fixes no nonzero momentum vector (det U is constant)', fixed_vectors_zero(grp))

    # Theorem 1 and 2: O and T admit only constant walks.
    for name in ('O', 'T'):
        fb, gb, a, b, eqs = unitarity_ideal(groups[name])
        print(f'{name}: {len(fb)} invariant scalars, {len(gb)} equivariant vectors, {len(eqs)} equations')
        G = sp.groebner(eqs, *b, *a[1:], a[0], order='grevlex')
        moving = all(in_radical(G, v) for v in list(b) + list(a[1:]))
        checks.check(f'{name}: every coefficient except a0 vanishes on the variety (radical membership)', moving)
        checks.check(f'{name}: a0^2 - 1 lies in the ideal, so U = +-1 times a phase', G.contains(a[0] ** 2 - 1))

    # Theorem 3: D4 admits motion only along its fourfold axis.
    fb, gb, a, b, eqs = unitarity_ideal(groups['D4'])
    checks.check('D4 basis: f_1 = c3 and g_0 = (0, 0, s3)',
                 sp.simplify(fb[1] - C[2]) == 0 and list(gb[0]) == [0, 0, S[2]])
    G = sp.groebner(eqs, *b, *a[1:], a[0], order='grevlex')
    killed = [v for v in list(b[1:]) + list(a[2:])]
    checks.check('D4: all coefficients except a0, a1, b0 vanish on the variety',
                 all(in_radical(G, v) for v in killed))
    a0, a1, b0 = a[0], a[1], b[0]
    residual = sp.Poly(reduce_trig((a0 + a1 * C[2]) ** 2 + (b0 * S[2]) ** 2 - 1), *C, *S).as_dict().values()
    sol = sp.solve(list(residual), [a0, a1, b0], dict=True)
    axial = [s_ for s_ in sol if s_.get(b0, 0) != 0]
    checks.check('D4 residual system: moving solutions are exactly a0 = 0, a1 = +-1, b0 = +-1',
                 len(axial) == 4 and all(s_[a0] == 0 and abs(s_[a1]) == 1 and abs(s_[b0]) == 1 for s_ in axial))

    # Theorem 3: the other soldering-menu coin actions under O.
    # Trivial action: f and every g_j are O-invariant scalars. The invariant
    # scalars on the cell are polynomials in c_1, c_2, c_3 only, so the identity
    # f^2 + sum_j g_j^2 = 1 holds on [-1, 1]^3 and hence in R[c]; comparing the
    # real top-degree homogeneous parts (a sum of real squares vanishes only if
    # each vanishes) forces every polynomial to be constant.
    inv = scalar_basis(groups['O'], cell_functions())
    checks.check('trivial: every O-invariant cell function is a polynomial in cosines only',
                 all(not sp.sympify(e).has(*S) for e in inv))
    checks.check('trivial: the invariant cosine polynomials have degrees 0..3 (no constant combination besides 1)',
                 sorted(sp.Poly(e, *C).total_degree() for e in inv) == [0, 1, 2, 3])
    for kind in ('sign', 'axis'):
        homo = all(coin_action(A_ * B_, kind) == coin_action(A_, kind) * coin_action(B_, kind) for A_ in O for B_ in O)
        checks.check(f'{kind} coin action is a homomorphism O -> SO(3)',
                     homo and all(coin_action(R, kind).det() == 1 for R in O))
        fb, gb, a, b, eqs = unitarity_ideal(groups['O'], kind)
        G = sp.groebner(eqs, *b, *a[1:], a[0], order='grevlex')
        moving = [j for j, v in enumerate(gb) if any(x.has(*C) or x.has(*S) for x in v)]
        constant = [j for j in range(len(gb)) if j not in moving]
        checks.check(f'{kind}: every k-dependent coefficient of f vanishes on the variety',
                     all(in_radical(G, v) for v in a[1:]))
        killed = []
        for j in moving:
            if in_radical(G, b[j]):
                killed.append(j)
        if len(killed) == len(moving):
            checks.check(f'{kind}: every k-dependent coefficient of g vanishes, so U is a constant coin', True)
        else:
            # remaining k-dependent pieces: solve the residual real system
            rest = [b[j] for j in moving if j not in killed]
            fres = a[0]
            gres = [sum(b[j] * gb[j][i] for j in constant + [m for m in moving if m not in killed]) for i in range(3)]
            res_eqs = list(sp.Poly(reduce_trig(fres ** 2 + sum(x ** 2 for x in gres) - 1), *C, *S).as_dict().values())
            # real solutions require the sum of squares of the surviving moving coefficients to vanish
            sq = sum(v ** 2 for v in rest)
            checks.check(f'{kind}: residual identity forces sum of squares of k-dependent g-coefficients to 0 (real walks are constant coins)',
                         any(sp.expand(e - sq) == 0 or sp.expand(e + sq) == 0 for e in res_eqs))

    # Exhibit: the D2-covariant product walk q_x q_y q_z moves in all three directions.
    c1, c2, c3 = C
    s1, s2, s3 = S
    f = c1 * c2 * c3 + s1 * s2 * s3
    g = [s1 * c2 * c3 - c1 * s2 * s3, c1 * s2 * c3 + s1 * c2 * s3, c1 * c2 * s3 - s1 * s2 * c3]
    checks.check('product walk is unitary: f^2 + |g|^2 = 1', reduce_trig(f ** 2 + sum(x ** 2 for x in g) - 1) == 0)
    d2_ok = all(sp.expand(act(f, M) - f) == 0 and
                all(sp.expand(x) == 0 for x in (sp.Matrix([act(x, M) for x in g]) - M * sp.Matrix(g)))
                for M in groups['D2'])
    checks.check('product walk is D2-covariant (soldered)', d2_ok)
    q = RZ
    rz_ok = sp.expand(act(f, q) - f) == 0 and all(
        sp.expand(x) == 0 for x in (sp.Matrix([act(x, q) for x in g]) - q * sp.Matrix(g)))
    checks.check('product walk is not covariant under the quarter turn about z', not rz_ok)
    jac = sp.Matrix([[sp.diff(x.subs({C[i]: sp.cos(sp.Symbol(f'k{i}')) for i in range(3)} | {S[i]: sp.sin(sp.Symbol(f'k{i}')) for i in range(3)}), sp.Symbol(f'k{j}')) for j in range(3)] for x in g])
    jac0 = jac.subs({sp.Symbol(f'k{i}'): 0 for i in range(3)})
    checks.check('product walk is an isotropic unit-speed Weyl cone at k = 0 (dg/dk = identity)', jac0 == sp.eye(3))
    eps = sp.Symbol('eps')
    nn = sp.symbols('n1:4')
    fk = f.subs({C[i]: sp.cos(eps * nn[i]) for i in range(3)} | {S[i]: sp.sin(eps * nn[i]) for i in range(3)})
    fser = sp.expand(sp.series(fk, eps, 0, 4).removeO())
    target = 1 - eps ** 2 * (nn[0] ** 2 + nn[1] ** 2 + nn[2] ** 2) / 2 + eps ** 3 * nn[0] * nn[1] * nn[2]
    checks.check('cos(omega) = f = 1 - |k|^2/2 + k1 k2 k3 + O(k^4): parity-odd cubic term', sp.expand(fser - target) == 0)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
