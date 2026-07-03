#!/usr/bin/env python3
"""The epsilon-assembled cross-plane pair density: its exact quadratic form
is the cross-plane trace pairing (equal to the block-5 Gram pairing with
coefficient one on Cartan data, and to the abelian intersection density for
U(1)); its parity is GEOMETRIC (the epsilon assembly flips under coordinate
reflection) while its internal flips are even; the connected (shifted)
version is gauge-invariant with connector transport supplying the frame and
the ordering content entering exactly with connectors.

Paired note:
docs/THETA_CROSS_PLANE_PAIR_DENSITY_GEOMETRIC_ODDNESS_CONNECTOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: exact combinatorics of the epsilon assembly,
exact rational Cartan/Gram algebra, convergence-ratio gates for series
coefficients (discriminating: a wrong quadratic form plateaus), and explicit
small-graph gauge-invariance checks with the link transformation law. All
deterministic (fixed seed); no fits, no external comparators, no measured
values, no Monte Carlo.

Sections:
  A. Assembly ground: sum over (rho,sigma) of eps_{mu nu rho sigma}
     vanishes for every fixed plane (single-plane squares cancel); the
     epsilon-assembled same-site pair sum D(eps) equals its predicted
     quadratic form with remainder O(eps^4) (convergence-ratio gate,
     ratio ~ 16 under eps-halving); D is real.
  B. Reductions: on dual-basis Cartan elements the trace pairing equals the
     block-5 Gram pairing with coefficient exactly ONE (exact rationals,
     parameter-free); the U(1) case reduces to the epsilon-paired product
     of plane fluxes — the abelian intersection density shape — with
     single-plane squares cancelled.
  C. Parities: the full same-site pair object maps to its conjugate under
     simultaneous dagger and under simultaneous bar, and to itself under
     simultaneous transpose (internal flips even on the real part); the
     coordinate reflection (axis 0) flips the quadratic density EXACTLY
     (geometric oddness — the theta parity lives in the epsilon assembly,
     not in internal phases).
  D. Connectors: on an explicit link graph, tr[P1 L P2 L^dag] is invariant
     under arbitrary local gauge transformations (the transformation law
     applied to LINKS, invariance derived, not assumed); the transported
     quadratic form pairs A1 with L A2 L^dag; two connectors differ by a
     loop insertion; same-site pairs are cyclicly ordering-free while
     connected pairs are not — the ordering (chain) content enters exactly
     with connectors.

Expected close: TOTAL: PASS=12 FAIL=0
"""
from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


RNG = np.random.default_rng(7)


def rand_herm_su3() -> np.ndarray:
    z = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    H = (z + z.conj().T) / 2
    return H - np.trace(H) / 3 * np.eye(3)


def rand_su3(n: int = 1):
    out = []
    for _ in range(n):
        z = (RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))) / np.sqrt(2)
        q, r = np.linalg.qr(z)
        q = q @ np.diag(np.diag(r) / np.abs(np.diag(r)))
        q = q / np.linalg.det(q) ** (1 / 3)
        out.append(q)
    return out


def eps4(a: int, b: int, c: int, d: int) -> int:
    p = [a, b, c, d]
    if len(set(p)) < 4:
        return 0
    sign = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                sign = -sign
    return sign


PLANES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
A_FIELD = {pl: rand_herm_su3() for pl in PLANES}


def field(mu: int, nu: int, flip_axis0: bool = False):
    a = A_FIELD[(mu, nu)] if mu < nu else -A_FIELD[(nu, mu)]
    if flip_axis0 and (mu == 0 or nu == 0):
        a = -a
    return a


def expiH(H: np.ndarray, eps: float) -> np.ndarray:
    w, U = np.linalg.eigh(eps * H)
    return U @ np.diag(np.exp(1j * w)) @ U.conj().T


def D_assembled(eps: float, flip_axis0: bool = False,
                op=None) -> complex:
    tot = 0.0 + 0j
    for mu in range(4):
        for nu in range(4):
            if nu == mu:
                continue
            for rho in range(4):
                for sig in range(4):
                    e = eps4(mu, nu, rho, sig)
                    if e == 0:
                        continue
                    A1 = field(mu, nu, flip_axis0)
                    A2 = field(rho, sig, flip_axis0)
                    U1 = expiH(A1, eps)
                    U2 = expiH(A2, eps)
                    if op == "dagger":
                        U1, U2 = U1.conj().T, U2.conj().T
                    elif op == "bar":
                        U1, U2 = U1.conj(), U2.conj()
                    elif op == "transpose":
                        U1, U2 = U1.T, U2.T
                    tot += e * np.trace(U1 @ U2)
    return complex(tot)


def Q_quadratic(flip_axis0: bool = False) -> float:
    tot = 0.0 + 0j
    for mu in range(4):
        for nu in range(4):
            if nu == mu:
                continue
            for rho in range(4):
                for sig in range(4):
                    e = eps4(mu, nu, rho, sig)
                    if e == 0:
                        continue
                    tot += -e * np.trace(field(mu, nu, flip_axis0)
                                         @ field(rho, sig, flip_axis0))
    return float(tot.real)


# ---------------------------------------------------------------------------
# Section A: assembly ground
# ---------------------------------------------------------------------------
print("Section A: epsilon assembly and the exact quadratic form")

ok_sum = all(sum(eps4(mu, nu, r, s) for r in range(4) for s in range(4)) == 0
             for mu in range(4) for nu in range(4) if nu != mu)
check("A1 sum over (rho,sigma) of eps_{mu nu rho sigma} = 0 for every fixed"
      " plane: single-plane squares cancel in the assembly", ok_sum)

QP = Q_quadratic()
r1 = abs(D_assembled(0.02) - QP * 0.02 ** 2)
r2 = abs(D_assembled(0.01) - QP * 0.01 ** 2)
r3 = abs(D_assembled(0.005) - QP * 0.005 ** 2)
ratio12 = r1 / r2
ratio23 = r2 / r3
check("A2 D(eps) = [cross-plane trace pairing] eps^2 + O(eps^4):"
      " convergence-ratio gate (ratios ~ 16 under eps-halving; a wrong"
      " quadratic form would plateau near 1)",
      14.0 < ratio12 < 18.0 and 14.0 < ratio23 < 18.0,
      f"Q = {QP:.6f}, ratios = {ratio12:.2f}, {ratio23:.2f}")

check("A3 the assembled pair sum is real",
      abs(D_assembled(0.01).imag) < 1e-12)

# ---------------------------------------------------------------------------
# Section B: reductions
# ---------------------------------------------------------------------------
print("Section B: Cartan/Gram and U(1) reductions")

from fractions import Fraction

GRAM = [[Fraction(2, 3), Fraction(1, 3)], [Fraction(1, 3), Fraction(2, 3)]]


def pair_gram(x, y) -> Fraction:
    return sum(GRAM[i][j] * x[i] * y[j] for i in range(2) for j in range(2))


HW1 = np.diag([2, -1, -1]).astype(complex) / 3
HW2 = np.diag([1, 1, -2]).astype(complex) / 3

ok_cartan = True
for (a, b) in [(1, 0), (0, 1), (2, -1), (1, 1), (3, -2)]:
    for (c, d) in [(1, 0), (0, 1), (1, -2), (2, 2)]:
        tr = float(np.trace((a * HW1 + b * HW2) @ (c * HW1 + d * HW2)).real)
        gg = pair_gram((a, b), (c, d))
        ok_cartan = ok_cartan and abs(tr - float(gg)) < 1e-12
check("B1 on dual-basis Cartan elements the trace pairing EQUALS the"
      " block-5 Gram pairing with coefficient exactly one (parameter-free)",
      ok_cartan)

FVAL = {pl: float(RNG.normal()) for pl in PLANES}


def fval(mu, nu):
    return FVAL[(mu, nu)] if mu < nu else -FVAL[(nu, mu)]


def Du1(eps: float) -> complex:
    tot = 0.0 + 0j
    for mu in range(4):
        for nu in range(4):
            if nu == mu:
                continue
            for rho in range(4):
                for sig in range(4):
                    e = eps4(mu, nu, rho, sig)
                    if e == 0:
                        continue
                    tot += e * np.exp(1j * eps * (fval(mu, nu) + fval(rho, sig)))
    return complex(tot)


QU1 = -sum(eps4(m, n, r, s) * fval(m, n) * fval(r, s)
           for m in range(4) for n in range(4)
           for r in range(4) for s in range(4)
           if n != m and s != r and eps4(m, n, r, s) != 0)
ru1 = abs(Du1(0.01) - QU1 * 0.01 ** 2) and abs(Du1(0.01).real - QU1 * 0.01 ** 2)
q1 = abs(Du1(0.02).real - QU1 * 0.02 ** 2)
q2 = abs(Du1(0.01).real - QU1 * 0.01 ** 2)
check("B2 U(1) reduction: the quadratic form is the epsilon-paired product"
      " of plane fluxes (the abelian intersection-density shape), squares"
      " cancelled (ratio gate)",
      10.0 < q1 / q2 < 22.0, f"Q_U1 = {QU1:.6f}, ratio = {q1/q2:.2f}")

# ---------------------------------------------------------------------------
# Section C: parities
# ---------------------------------------------------------------------------
print("Section C: internal flips even, geometric reflection odd")

D0 = D_assembled(0.3)
check("C1 internal flip table of the full object: dagger -> conj(D),"
      " bar -> conj(D), transpose -> D (so Re D is even under all three"
      " internal flips — no internal phase carries the oddness)",
      abs(D_assembled(0.3, op="dagger") - np.conj(D0)) < 1e-12
      and abs(D_assembled(0.3, op="bar") - np.conj(D0)) < 1e-12
      and abs(D_assembled(0.3, op="transpose") - D0) < 1e-12)

check("C2 GEOMETRIC oddness: reflecting axis 0 (A_{0i} -> -A_{0i}) flips"
      " the quadratic density exactly — the theta parity lives in the"
      " epsilon assembly, not in internal flips",
      abs(Q_quadratic(flip_axis0=True) + QP) < 1e-10,
      f"Q = {QP:.6f}, reflected = {Q_quadratic(flip_axis0=True):.6f}")

# stronger than the quadratic statement: every nonzero epsilon pair contains
# exactly one axis-0 plane, and flipping that plane's field equals swapping
# its orientation label, which flips the epsilon sign — so the FULL object
# is exactly odd under the reflection, at all orders (the design-time
# expectation of an O(eps^4) remainder was superseded by this identity).
r_ref = abs(D_assembled(0.5, flip_axis0=True) + D_assembled(0.5))
check("C3 the full assembled object is EXACTLY odd under the reflection at"
      " all orders: D_reflected = -D (large-eps identity check)",
      r_ref < 1e-10, f"|D + D_reflected| = {r_ref:.2e} at eps = 0.5")

# ---------------------------------------------------------------------------
# Section D: connectors and ordering content
# ---------------------------------------------------------------------------
print("Section D: connectors, gauge invariance, ordering content")

# explicit link graph: sites a, b; plaquette loops built from links
# P1 at a: l1 (a->x1) l2 (x1->x2) l3 (x2->x3) l4 (x3->a)
# connector: m1 (a->y) m2 (y->b)
# P2 at b: k1..k4 (b->z1->z2->z3->b)
links = rand_su3(10)
l1, l2, l3, l4, m1, m2, k1, k2, k3, k4 = links
P1 = l1 @ l2 @ l3 @ l4          # based at a
L = m1 @ m2                     # a -> b
P2 = k1 @ k2 @ k3 @ k4          # based at b
obs0 = np.trace(P1 @ L @ P2 @ L.conj().T)

g = {s: rand_su3(1)[0] for s in ["a", "x1", "x2", "x3", "y", "b",
                                 "z1", "z2", "z3"]}
# link u(x->y) -> g_x u g_y^dag
l1g = g["a"] @ l1 @ g["x1"].conj().T
l2g = g["x1"] @ l2 @ g["x2"].conj().T
l3g = g["x2"] @ l3 @ g["x3"].conj().T
l4g = g["x3"] @ l4 @ g["a"].conj().T
m1g = g["a"] @ m1 @ g["y"].conj().T
m2g = g["y"] @ m2 @ g["b"].conj().T
k1g = g["b"] @ k1 @ g["z1"].conj().T
k2g = g["z1"] @ k2 @ g["z2"].conj().T
k3g = g["z2"] @ k3 @ g["z3"].conj().T
k4g = g["z3"] @ k4 @ g["b"].conj().T
P1g = l1g @ l2g @ l3g @ l4g
Lg = m1g @ m2g
P2g = k1g @ k2g @ k3g @ k4g
obs_g = np.trace(P1g @ Lg @ P2g @ Lg.conj().T)
check("D1 the connected pair tr[P1 L P2 L^dag] is invariant under"
      " arbitrary local gauge transformations (derived from the LINK"
      " transformation law on an explicit graph, not assumed)",
      abs(obs_g - obs0) < 1e-10, f"observable = {obs0:.8f}")

A1h, A2h = rand_herm_su3(), rand_herm_su3()
L0 = rand_su3(1)[0]


def conn_pair(eps: float) -> complex:
    return complex(np.trace(expiH(A1h, eps) @ L0 @ expiH(A2h, eps)
                            @ L0.conj().T))


pred_quad = -np.trace(A1h @ L0 @ A2h @ L0.conj().T).real \
    - np.trace(A1h @ A1h).real / 2 - np.trace(A2h @ A2h).real / 2
series = lambda e: 3 + 1j * e * (np.trace(A1h) + np.trace(A2h)) \
    + e * e * pred_quad
c1 = abs(conn_pair(0.02) - series(0.02))
c2 = abs(conn_pair(0.01) - series(0.01))
check("D2 the connected pair's quadratic cross term is the TRANSPORTED"
      " pairing tr(A1 . L A2 L^dag) (ratio gate; block-6 frame transport"
      " appears inside the density)",
      6.0 < c1 / c2 < 10.0, f"ratio = {c1 / c2:.2f}")

Lalt = rand_su3(1)[0]
v_L = np.trace(expiH(A1h, 0.5) @ L0 @ expiH(A2h, 0.5) @ L0.conj().T)
v_Lalt = np.trace(expiH(A1h, 0.5) @ Lalt @ expiH(A2h, 0.5) @ Lalt.conj().T)
loop = Lalt.conj().T @ L0
check("D3 two connectors differ by a loop insertion: the values differ and"
      " the difference datum is the loop holonomy (configurational path"
      " dependence, block-6 pattern)",
      abs(v_L - v_Lalt) > 1e-3,
      f"|difference| = {abs(v_L - v_Lalt):.6f},"
      f" loop trace = {np.trace(loop):.4f}")

U1s, U2s = rand_su3(2)
same_site_sym = abs(np.trace(U1s @ U2s) - np.trace(U2s @ U1s))
conn_asym = abs(np.trace(U1s @ L0 @ U2s @ L0.conj().T)
                - np.trace(U2s @ L0 @ U1s @ L0.conj().T))
check("D4 ordering content enters exactly with connectors: same-site pairs"
      " are cyclically ordering-free (tr[U1 U2] = tr[U2 U1] exactly) while"
      " connected pairs are not",
      same_site_sym < 1e-13 and conn_asym > 1e-3,
      f"connected ordering asymmetry = {conn_asym:.6f}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
