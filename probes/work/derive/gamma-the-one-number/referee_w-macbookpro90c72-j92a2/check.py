#!/usr/bin/env python3
"""Referee for J:derive:gamma-the-one-number:a2.

Independent exact checks. The box is the open cube {0,...,n-1}^3 with walls at
phi = 1. The Green function solves (1 - average) G = delta at the centre.
The body is re-solved from the divided law, not copied from the attempt.
The side-3 value 22/17 is also obtained from a 4-orbit reduction.
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def solve(A, b):
    n = len(A)
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        if p != c:
            M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [v / piv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[r][n] for r in range(n)]


def cube(n):
    sites = list(itertools.product(range(n), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    nbr = []
    for s in sites:
        row = []
        for axis in range(3):
            for step in (1, -1):
                t = list(s)
                t[axis] += step
                t = tuple(t)
                row.append(idx[t] if t in idx else None)
        nbr.append(row)
    return sites, idx, nbr


def green(n):
    sites, idx, nbr = cube(n)
    N = len(sites)
    c = idx[(n // 2,) * 3]
    A = [[Fr(0)] * N for _ in range(N)]
    b = [Fr(0)] * N
    for i in range(N):
        A[i][i] = Fr(1)
        for j in nbr[i]:
            if j is not None:
                A[i][j] -= Fr(1, 6)
    b[c] = Fr(1)
    g = solve(A, b)
    return g[c], g, sites, idx, nbr, c


def orbit_side3():
    """Centre, face, edge, corner. Walls contribute nothing to the average."""
    # C - F = 1
    # F - C/6 - 4E/6 = 0
    # E - 2F/6 - 2K/6 = 0
    # K - E/2 = 0
    A = [
        [Fr(1), Fr(-1), Fr(0), Fr(0)],
        [Fr(-1, 6), Fr(1), Fr(-4, 6), Fr(0)],
        [Fr(0), Fr(-2, 6), Fr(1), Fr(-2, 6)],
        [Fr(0), Fr(0), Fr(-1, 2), Fr(1)],
    ]
    return solve(A, [Fr(1), Fr(0), Fr(0), Fr(0)])[0]


def body(n, gam, m):
    """(12/gamma)(phi - avg) = -m phi_0 at the body, phi - avg = 0 elsewhere, walls 1."""
    g0, _, sites, _, nbr, c = green(n)
    N = len(sites)
    A = [[Fr(0)] * N for _ in range(N)]
    b = [Fr(0)] * N
    for i in range(N):
        coef = Fr(12) / gam if i == c else Fr(1)
        A[i][i] = coef + (m if i == c else Fr(0))
        for j in nbr[i]:
            if j is None:
                b[i] += coef / 6
            else:
                A[i][j] -= coef / 6
    return solve(A, b), g0, nbr, c


# ---------- R1. Green values, including an orbit reduction on side 3 ----------
g1, _, _, _, _, _ = green(1)
g3, _, _, _, _, _ = green(3)
g5, _, _, _, _, _ = green(5)
orb = orbit_side3()
r1 = g1 == 1 and g3 == Fr(22, 17) and g5 == Fr(136, 99) and orb == g3 and g5 > g3 > g1
ok("R1", r1, f"G0(0) = {g1}, {g3}, {g5} on sides 1, 3, 5; the side-3 orbit reduction gives {orb}")

# ---------- R2. point body, undivided law, neighbour values ----------
good, rows = True, []
for n in (1, 3, 5):
    for gam, m in ((Fr(1), Fr(3)), (Fr(7, 2), Fr(2, 5))):
        phi, g0, nbr, c = body(n, gam, m)
        x = gam * g0 * m / 12
        good &= phi[c] == 1 / (1 + x)
        for i, val in enumerate(phi):
            avg = sum((phi[j] if j is not None else Fr(1)) for j in nbr[i]) / 6
            e = m * val ** 2 if i == c else Fr(0)
            good &= Fr(12) / gam * val * (val - avg) == -e
        good &= all((phi[j] if j is not None else Fr(1)) == phi[c] * (1 + gam * m / 12) for j in nbr[c])
    rows.append(f"side {n} G0={green(n)[0]}")
ok("R2", good, "divided law re-solved in rationals: phi_0 = 1/(1+x), undivided law at every site, neighbours at phi_0(1+gamma m/12); " + ", ".join(rows))

# ---------- R3. self-consistency does not fix gamma m ----------
gam, m, G0 = sp.symbols("gamma m G0")
phi0 = 1 / (1 + gam * G0 * m / 12)
kappa = sp.together(phi0 ** 2 / (phi0 * (1 + gam * m / 12)) ** 2)
ident = sp.simplify(kappa - 1 / (1 + gam * m / 12) ** 2) == 0
roots = sp.solve(sp.Eq((1 + gam * m / 12) ** 2, (1 + gam * G0 * m / 12) ** 2), m)
roots = [sp.factor(r) for r in roots]
want = {sp.Integer(0), sp.factor(-24 / (gam * (G0 + 1)))}
on_wall = sp.simplify((kappa - phi0 ** 2).subs(G0, 1)) == 0
r3 = ident and set(roots) == want and on_wall
ok("R3", r3,
   "kappa = (1+gamma m/12)^{-2} identically; equating it with w_0 = phi_0^2 has roots m=0 and "
   "m=-24/(gamma(1+G0)) only, so no m>0 unless G0=1, where the equation is an identity. It fixes no gamma m")

# ---------- R4. saturation, and the ledger is stationary for every gamma ----------
lim = sp.limit(m / (1 + gam * G0 * m / 12), m, sp.oo)
sat = sp.simplify(lim - 12 / (gam * G0)) == 0
stat = True
for n, pairs in ((3, ((Fr(1), Fr(3)), (Fr(9, 4), Fr(5, 3)))), (5, ((Fr(2), Fr(4)),))):
    sites, _, nbr = cube(n)
    c = (n // 2,) * 3
    c = {s: i for i, s in enumerate(sites)}[c]
    for gam_v, m_v in pairs:
        phi, _, nbr, c = body(n, gam_v, m_v)
        for i, val in enumerate(phi):
            acc = Fr(0)
            for j in nbr[i]:
                other = phi[j] if j is not None else Fr(1)
                acc += val - other
            # d/d phi_i of (2/gamma) sum (diff)^2 is (4/gamma) sum (phi_i - other); body adds 2 m phi_0
            deriv = (Fr(4) / gam_v) * acc
            if i == c:
                deriv += 2 * m_v * phi[c]
            stat &= deriv == 0
ok("R4", sat and stat,
   "m phi_0 -> 12/(gamma G0(0)); the ledger gradient vanishes on the solved field at unrelated gammas on sides 3 and 5, so gamma is a free label")

# ---------- R5. the scale reference, from its own text ----------
note = open("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md").read()
r5 = (
    "a^{-1} = M_Pl" in note
    and "zero dimensionless" in note
    and "does not assert `a/l_P = 1`" in note
    and "separate open gravity derivation" in note
    and "does not supply any dimensionless quantity" in note
)
ok("R5", r5,
   "the scale-reference primitive states a^{-1}=M_Pl as a units conversion with zero dimensionless content and "
   "explicitly does not assert a/l_P=1; gamma=4 pi is that open statement, not a consequence of the primitive")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - the point body, the failed self-consistency, and a gamma-independent ledger all survive exact rational checks; the scale reference fixes no pure number.")
print("HIT: confirmed - on a walled box, phi_0 = 1/(1+(gamma/12) G0(0) m) with G0(0) = 1, 22/17, 136/99 on sides 1, 3, 5, and every neighbour at phi_0(1+gamma m/12); equating the tick ratio with the site rate has no root m>0 except the side-1 identity, and the ledger m w_0+(2/gamma) sum (diff)^2 is stationary for every gamma>0. The scale reference supplies no dimensionless content, so it yields gamma=4 pi only by assuming a=l_P. Nothing in these clauses fixes gamma.")
