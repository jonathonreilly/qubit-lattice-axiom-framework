#!/usr/bin/env python3
"""Exact freeze of O-covariant one-qubit walks on the 125-point stencil.

The stencil is {-2,...,2}^3 (range two along each axis). By Theorem 0 of the
companion cell note an O-covariant walk is a phase times V = f + i g.sigma with
f O-invariant, g O-equivariant (full-soldered spin-1/2 action), real, and
f^2 + |g|^2 = 1. The stabiliser of each of the three symmetry lines fixes only
the line direction, so on the axis (t,0,0), the face diagonal (t,t,0) and the
body diagonal (t,t,t) the vector g is parallel to the line. There
P = f + i |g|_signed is a unit-modulus Laurent polynomial in e^{it} with
P(0) = 1 (g(0) = 0 by equivariance, sign absorbed in the phase), hence a
monomial: f = cos(m t), |g| = sin(m t) with |m| <= 2, 4, 6 on the three lines.
Each choice (m, q, p) of the three integers is a linear system on the
coefficients. The runner shows every choice except (0, 0, 0) is inconsistent
and that on (0, 0, 0) the unitarity ideal places every remaining coefficient
in the radical, so V = 1.
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

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    'docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

C, S = cell.C, cell.S
Z = sp.Symbol('z')


def range_two_functions():
    per = [[1, C[a], S[a], 2 * C[a] ** 2 - 1, 2 * S[a] * C[a]] for a in range(3)]
    return [sp.expand(x * y * z) for x, y, z in itertools.product(*per)]


LINES = {
    'axis': (1, 0, 0),
    'face': (1, 1, 0),
    'body': (1, 1, 1),
}


def on_line(expr, direction):
    """Restrict to k = t * direction, written as a Laurent polynomial in z = e^{it}."""
    cz, sz = (Z + 1 / Z) / 2, (Z - 1 / Z) / (2 * sp.I)
    sub = {}
    for a, d in enumerate(direction):
        sub[C[a]] = cz if d else 1
        sub[S[a]] = sz if d else 0
    return sp.expand(sp.sympify(expr).subs(sub, simultaneous=True))


def laurent_coeffs(expr, shift=8):
    e = sp.expand(expr * Z ** shift)
    return [x for x in sp.Poly(e, Z).all_coeffs() if x != 0]


def main() -> int:
    checks = cell.Checks()
    O = cell.proper_cubic()
    funcs = range_two_functions()
    checks.check('stencil functions span the 125 offsets {-2..2}^3', len(funcs) == 125)
    fb = cell.scalar_basis(O, funcs)
    gb = cell.vector_basis(O, funcs, 'full')
    checks.check('O-invariant scalars on the stencil: 10', len(fb) == 10)
    checks.check('O-equivariant vectors on the stencil: 15', len(gb) == 15)
    a = sp.symbols(f'a0:{len(fb)}')
    b = sp.symbols(f'b0:{len(gb)}')
    f = sum(x * e for x, e in zip(a, fb))
    g = [sum(b[j] * gb[j][i] for j in range(len(gb))) for i in range(3)]
    eqs = list(sp.Poly(cell.reduce_trig(f ** 2 + sum(x ** 2 for x in g) - 1), *C, *S).as_dict().values())
    checks.check('unitarity identity gives 149 coefficient equations', len(eqs) == 149)

    # g is parallel to each symmetry line along that line (stabiliser fixes only the direction).
    fl = {k: on_line(f, d) for k, d in LINES.items()}
    gl = {k: [on_line(x, d) for x in g] for k, d in LINES.items()}
    checks.check('axis line: g = (g_x, 0, 0)', gl['axis'][1] == 0 and gl['axis'][2] == 0)
    checks.check('face line: g = (g_x, g_x, 0)', sp.expand(gl['face'][0] - gl['face'][1]) == 0 and gl['face'][2] == 0)
    checks.check('body line: g = (g_x, g_x, g_x)',
                 sp.expand(gl['body'][0] - gl['body'][1]) == 0 and sp.expand(gl['body'][0] - gl['body'][2]) == 0)
    g0 = [x.subs({**{C[i]: 1 for i in range(3)}, **{S[i]: 0 for i in range(3)}}) for x in g]
    checks.check('g(0) = 0 identically (O fixes no vector), so f(0) = +-1', all(x == 0 for x in g0))

    # Line degrees bound the monomial exponent: axis <= 2, face <= 4, body <= 6.
    deg = {}
    for k in LINES:
        num = sp.Poly(sp.expand(fl[k] * Z ** 8), Z)
        lo = min(m[0] for m in num.monoms()) - 8
        hi = max(m[0] for m in num.monoms()) - 8
        deg[k] = (lo, hi)
    checks.check('line Laurent degrees of f: axis 2, face 4, body 6',
                 deg == {'axis': (-2, 2), 'face': (-4, 4), 'body': (-6, 6)})

    norm = {'axis': 1, 'face': sp.sqrt(2), 'body': sp.sqrt(3)}
    unknowns = list(a) + list(b)

    def branch(m, q, p):
        lin = []
        for k, n in zip(LINES, (m, q, p)):
            target_f = (Z ** n + Z ** (-n)) / 2
            target_g = (Z ** n - Z ** (-n)) / (2 * sp.I)
            lin += laurent_coeffs(fl[k] - target_f)
            lin += laurent_coeffs(norm[k] * gl[k][0] - target_g)
        return sp.linsolve(lin, unknowns)

    feasible = []
    total = 0
    for m in range(-2, 3):
        for q in range(-4, 5):
            for p in range(-6, 7):
                total += 1
                if branch(m, q, p) != sp.EmptySet:
                    feasible.append((m, q, p))
    checks.check(f'all {total} line branches except (0,0,0) are linearly inconsistent', feasible == [(0, 0, 0)])

    sol = next(iter(branch(0, 0, 0)))
    sub = dict(zip(unknowns, sol))
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sol]), key=str)
    checks.check('trivial branch fixes f(k) = 1 on the three lines and a_0 = 1, a_1..a_9 = 0',
                 sub[a[0]] == 1 and all(sub[x] == 0 for x in a[1:]))
    red = [e for e in (sp.expand(e.subs(sub)) for e in eqs) if e != 0]
    G = sp.groebner(red, *free, order='grevlex')
    checks.check('trivial branch: Groebner basis is proper (the constant walk survives)', G.exprs != [1])
    checks.check(f'trivial branch: each of the {len(free)} remaining coefficients lies in the radical',
                 all(cell.in_radical(G, v, 4) for v in free))
    vals = {v: 0 for v in free}
    f0 = sp.expand(f.subs(sub).subs(vals))
    g0 = [sp.expand(x.subs(sub).subs(vals)) for x in g]
    checks.check('so every O-covariant range-two walk is V = 1, i.e. U = constant phase', f0 == 1 and g0 == [0, 0, 0])

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
