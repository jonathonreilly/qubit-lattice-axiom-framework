#!/usr/bin/env python3
"""Line-branch certificates for covariant one-qubit walks (Theorems 4 and 5).

By Theorem 0 of the companion cell note, a walk covariant under a rotation group
H without fixed vectors is a phase times V = f + i g.sigma with f H-invariant,
g H-equivariant (full-soldered spin-1/2 action), real, f^2 + |g|^2 = 1.

Line lemma. Let e be a lattice line whose stabiliser Stab+(e) = {M in H : M e = e}
fixes only the multiples of e. Along k = t e, g = gamma(t) e/|e| with gamma real,
so P = f + i gamma is a Laurent polynomial in z = e^{it} of modulus one, hence a
unit monomial; P(0) = 1 after absorbing the sign of f(0) = +-1 into the phase
(g(0) = 0 since H fixes no vector). So f = cos(n t), gamma = sin(n t) with |n| at
most the line degree. Each choice of exponents on the chosen lines is a linear
system on the coefficients; the runner solves every branch exactly and closes
the surviving ones with Groebner bases.

Theorem 4: H = O on the 125-point stencil {-2,...,2}^3: only V = 1.
Theorem 5: H = D3 on the 27-point cell: V = 1 or the body-diagonal shifts
V = exp(+-i (k1 + k2 + k3) sigma.(1,1,1)/sqrt 3), and nothing else.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import cubic_covariant_qubit_walk_cell_classification_2026_10_16 as cell  # noqa: E402

AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    'docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

C, S = cell.C, cell.S
Z = sp.Symbol('z')


def stencil_functions(R):
    per = [[sp.Integer(1)] + [sp.expand(sp.chebyshevt(n, C[a])) for n in range(1, R + 1)]
           + [sp.expand(S[a] * sp.chebyshevu(n - 1, C[a])) for n in range(1, R + 1)] for a in range(3)]
    return [sp.expand(x * y * z) for x, y, z in itertools.product(*per)]


def on_line(expr, e):
    """Restrict to k = t e as a Laurent polynomial in z = e^{it} (entries of e in {-1, 0, 1})."""
    sub = {}
    for a, d in enumerate(e):
        if d == 0:
            sub[C[a]], sub[S[a]] = 1, 0
        else:
            sub[C[a]], sub[S[a]] = (Z + 1 / Z) / 2, d * (Z - 1 / Z) / (2 * sp.I)
    return sp.expand(sp.sympify(expr).subs(sub, simultaneous=True))


def laurent_coeffs(expr, shift=20):
    e = sp.expand(expr * Z ** shift)
    return [x for x in sp.Poly(e, Z).all_coeffs() if x != 0] if e != 0 else []


def line_degree(expr, e, shift=20):
    mons = sp.Poly(sp.expand(on_line(expr, e) * Z ** shift), Z).monoms()
    return max(abs(m[0] - shift) for m in mons)


def family(H, R):
    fb = cell.scalar_basis(H, stencil_functions(R))
    gb = cell.vector_basis(H, stencil_functions(R), 'full')
    a = sp.symbols(f'a0:{len(fb)}')
    b = sp.symbols(f'b0:{len(gb)}')
    f = sum(x * y for x, y in zip(a, fb))
    g = [sum(b[j] * gb[j][i] for j in range(len(gb))) for i in range(3)]
    eqs = list(sp.Poly(cell.reduce_trig(f ** 2 + sum(x ** 2 for x in g) - 1), *C, *S).as_dict().values())
    return a, b, f, g, eqs


def stabiliser_fixes_only_line(H, e) -> bool:
    st = [M for M in H if list(M * sp.Matrix(e)) == list(e)]
    fix = sp.Matrix.vstack(*[M - sp.eye(3) for M in st]).nullspace()
    return len(fix) == 1 and sp.Matrix.hstack(fix[0], sp.Matrix(e)).rank() == 1


def branches(f, g, unknowns, lines, degrees):
    fl = [on_line(f, e) for e in lines]
    gl = [sp.expand(sum(ei * on_line(x, e) for ei, x in zip(e, g)) / sp.sqrt(sum(x * x for x in e))) for e in lines]
    out = {}
    for ns in itertools.product(*[range(-d, d + 1) for d in degrees]):
        lin = []
        for F, G, n in zip(fl, gl, ns):
            lin += laurent_coeffs(F - (Z ** n + Z ** (-n)) / 2)
            lin += laurent_coeffs(G - (Z ** n - Z ** (-n)) / (2 * sp.I))
        sol = sp.linsolve(lin, unknowns)
        if sol != sp.EmptySet:
            out[ns] = dict(zip(unknowns, next(iter(sol))))
    return out


def close_branch(sub, eqs):
    """Groebner basis of the unitarity equations on a branch; returns (G, free, point or None)."""
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sub.values()]), key=str)
    red = [e for e in (sp.expand(e.subs(sub)) for e in eqs) if e != 0]
    if not red:
        return None, free, None
    G = sp.groebner(red, *free, order='grevlex')
    if G.exprs == [1]:
        return G, free, None
    pts = sp.solve(G.exprs, free, dict=True)
    return G, free, pts


def main() -> int:
    checks = cell.Checks()

    # ---- Theorem 4: O on the 125-point stencil ----
    O = cell.proper_cubic()
    a, b, f, g, eqs = family(O, 2)
    checks.check('O, range two: 10 invariant scalars, 15 equivariant vectors, 149 equations',
                 (len(a), len(b), len(eqs)) == (10, 15, 149))
    lines = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
    checks.check('O: the stabilisers of the axis, face and body lines fix only the line',
                 all(stabiliser_fixes_only_line(O, e) for e in lines))
    g0 = [x.subs({**{C[i]: 1 for i in range(3)}, **{S[i]: 0 for i in range(3)}}) for x in g]
    checks.check('O: g(0) = 0 identically, so f(0) = +-1', all(x == 0 for x in g0))
    degs = [max(line_degree(f, e), *(line_degree(x, e) for x in g if x != 0)) for e in lines]
    checks.check('O: line degrees 2, 4, 6', degs == [2, 4, 6])
    br = branches(f, g, list(a) + list(b), lines, degs)
    checks.check('O: of the 5 x 9 x 13 = 585 exponent branches only (0, 0, 0) is linearly consistent',
                 list(br) == [(0, 0, 0)])
    sub = br[(0, 0, 0)]
    checks.check('O: branch (0, 0, 0) gives a_0 = 1 and a_1..a_9 = 0',
                 sub[a[0]] == 1 and all(sub[x] == 0 for x in a[1:]))
    G, free, pts = close_branch(sub, eqs)
    checks.check(f'O: on branch (0, 0, 0) each of the {len(free)} free coefficients lies in the radical',
                 len(free) == 6 and all(cell.in_radical(G, v, 4) for v in free))
    vals = {v: 0 for v in free}
    checks.check('Theorem 4: every O-covariant range-two walk is V = 1 (U a constant phase)',
                 sp.expand(f.subs(sub).subs(vals)) == 1 and [sp.expand(x.subs(sub).subs(vals)) for x in g] == [0, 0, 0])

    # ---- Theorem 5: D3 on the 27-point cell ----
    D3 = cell.closure(cell.GROUPS['D3'])
    checks.check('D3 has order 6 and fixes no vector', len(D3) == 6 and cell.fixed_vectors_zero(D3))
    a, b, f, g, eqs = family(D3, 1)
    checks.check('D3, cell: 7 invariant scalars, 12 equivariant vectors, 99 equations',
                 (len(a), len(b), len(eqs)) == (7, 12, 99))
    lines = [(1, 1, 1), (1, -1, 0)]
    checks.check('D3: the stabilisers of the body axis (C3) and the half-turn axis (C2) fix only the line',
                 all(stabiliser_fixes_only_line(D3, e) for e in lines))
    degs = [max(line_degree(f, e), *(line_degree(x, e) for x in g if x != 0)) for e in lines]
    checks.check('D3: line degrees 3 and 2', degs == [3, 2])
    br = branches(f, g, list(a) + list(b), lines, degs)
    checks.check('D3: all 7 x 5 = 35 exponent branches are linearly consistent (lines alone do not decide D3)',
                 len(br) == 35)
    n_hat = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    survivors = {}
    for ns, sub in br.items():
        G, free, pts = close_branch(sub, eqs)
        if G is not None and G.exprs == [1]:
            continue
        survivors[ns] = (G, free, pts, sub)
    checks.check('D3: Groebner bases close every branch except (0, 0) and (+-3, 0)',
                 sorted(survivors) == [(-3, 0), (0, 0), (3, 0)])
    point_ok, walks = True, {}
    for ns, (G, free, pts, sub) in survivors.items():
        point_ok &= pts is not None and len(pts) == 1
        if not point_ok:
            break
        pt = pts[0]
        point_ok &= all(cell.in_radical(G, v - pt[v], 4) for v in free)
        walks[ns] = (sp.expand(f.subs(sub).subs(pt)), [sp.expand(x.subs(sub).subs(pt)) for x in g])
    checks.check('D3: each surviving branch is a single point (v - value in the radical for every free v)', point_ok)
    if point_ok:
        k = sp.symbols('k1:4', real=True)
        trig = {**{C[i]: sp.cos(k[i]) for i in range(3)}, **{S[i]: sp.sin(k[i]) for i in range(3)}}
        Ksum = sum(k)
        const = walks[(0, 0)] == (1, [0, 0, 0])
        shifts = True
        for sgn, ns in ((1, (3, 0)), (-1, (-3, 0))):
            fw, gw = walks[ns]
            shifts &= sp.simplify(sp.expand_trig(sp.cos(Ksum)) - fw.subs(trig)) == 0
            target = sgn * sp.expand_trig(sp.sin(Ksum)) * n_hat
            shifts &= all(sp.simplify(gw[i].subs(trig) - target[i]) == 0 for i in range(3))
        checks.check('Theorem 5: the D3 cell walks are V = 1 and V = exp(+-i (k1+k2+k3) sigma.(1,1,1)/sqrt 3)',
                     const and shifts)
    else:
        checks.check('Theorem 5: the D3 cell walks are V = 1 and the two body-diagonal shifts', False)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
