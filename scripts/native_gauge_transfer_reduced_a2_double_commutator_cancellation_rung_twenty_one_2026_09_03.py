#!/usr/bin/env python3
"""Exact Rung-21 reduced-A2 double-commutator cancellation.

Derived here:

  P2 exp(-Q) = (1/2) R^2(H exp(-Q)) + 3 H exp(-Q)
  T2_sad = (1/2)[R,[R,T0]] + 3 T0

For a real symmetric T0, real skew-symmetric R, and simple eigenvalues,
Rayleigh--Schrodinger mixing from T1=[R,T0] cancels the diagonal double
commutator exactly. Every relative second-order eigenvalue correction is 3,
so this piece contributes zero to a log eigenvalue ratio.

Scope: the reduced saddle correction and displayed finite self-adjoint
perturbation class only. No total-a2 sign, uniform gap, continuum limit,
physical mass gap, audit verdict, or TOE-score change is asserted.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NATIVE_GAUGE_TRANSFER_REDUCED_A2_DOUBLE_COMMUTATOR_CANCELLATION_"
    "RUNG_TWENTY_ONE_BOUNDED_NOTE_2026-09-03.md"
)
PARENT = ROOT / "docs" / (
    "NATIVE_GAUGE_TRANSFER_REDUCED_A2_EIGENVALUE_RATIO_EPS_CANCELLATION_"
    "RUNG_TWENTY_BOUNDED_NOTE_2026-06-12.md"
)
PARENT_RUNNER = ROOT / "scripts" / (
    "native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_"
    "rung_twenty_bounded_2026_06_12.py"
)
note = NOTE.read_text(encoding="utf-8")
parent = PARENT.read_text(encoding="utf-8")
parent_runner = PARENT_RUNNER.read_text(encoding="utf-8")

check(
    "note declares bounded theorem and independent status authority",
    "**Claim type:** bounded_theorem" in note
    and "Status authority: independent audit lane only." in note,
)
check(
    "note states exact result and fences total sign / continuum claims",
    "T_2^sad = (1/2)[R,[R,T_0]] + 3 T_0." in note
    and "does not, by itself, establish that the full coefficient is positive"
    in note
    and "an infinite-volume or continuum Yang–Mills result" in note,
)
check(
    "one-hop parent package contains and checks the source P2 identity",
    "and the `P_2` reduction" in parent
    and 'check("P_2 exp(-Q) = (1/2) R^2[H exp(-Q)] + 3 H exp(-Q)"'
    in parent_runner,
)
check(
    "note uses durable repository paths",
    "/tmp/" not in note and "file://" not in note,
)
check(
    "note discloses reconstruction provenance",
    "original temporary `RUNG_21` artifact" in note
    and "independently reconstructs" in note
    and "not represented as a byte-identical copy" in note,
)


print("[Part 1] exact reduced-A2 differential identities")
x, y = sp.symbols("x y", real=True)
H = x * y * (x + y) / 2
Q = x**2 + x * y + y**2
u = x + y
G1 = (u**2 + 2 * x * y) / 2
P1 = sp.expand(G1 - 3 * u * H)
P2 = sp.expand(
    sp.Rational(3, 2) * u
    - 3 * u * G1
    + sp.Rational(9, 2) * u**2 * H
)
W = H * sp.exp(-Q)


def R(poly: sp.Expr) -> sp.Expr:
    return sp.diff(poly, x) + sp.diff(poly, y)


def L(poly: sp.Expr) -> sp.Expr:
    return sp.Rational(1, 3) * (
        sp.diff(poly, x, 2)
        - sp.diff(poly, x, y)
        + sp.diff(poly, y, 2)
    )


check("R H = (u^2+2xy)/2", sp.expand(R(H) - G1) == 0)
check("R Q = 3u", sp.expand(R(Q) - 3 * u) == 0)
check(
    "R(H exp(-Q)) = P1 exp(-Q)",
    sp.simplify(sp.exp(Q) * R(W) - P1) == 0,
)
check(
    "P2 exp(-Q) = (1/2)R^2(H exp(-Q)) + 3H exp(-Q)",
    sp.simplify(
        sp.exp(Q)
        * (P2 * sp.exp(-Q) - sp.Rational(1, 2) * R(R(W)) - 3 * W)
    )
    == 0,
)
derived_shift = sp.simplify(
    (
        P2 * sp.exp(-Q)
        - sp.Rational(1, 2) * R(R(W))
    )
    / W
)
check(
    "the residual multiplier is derived as the state-independent constant 3",
    derived_shift == 3,
)

coefficients = {
    (i, j): sp.Symbol(f"c_{i}_{j}") for i in range(5) for j in range(5)
}
generic = sum(c * x**i * y**j for (i, j), c in coefficients.items())
check("[R,L] = 0 on a generic degree-eight bivariate polynomial",
      sp.expand(R(L(generic)) - L(R(generic))) == 0)


print("[Part 2] exact finite-dimensional perturbation identity")
eigenvalues = [sp.Integer(v) for v in (2, 3, 5, 7, 11)]
T0 = sp.diag(*eigenvalues)
raw = sp.Matrix(
    [
        [0, 2, -1, 3, 0],
        [4, 0, 5, -2, 1],
        [2, -3, 0, 1, 4],
        [1, 2, -5, 0, 3],
        [-2, 1, 0, 4, 0],
    ]
)
Rmat = raw - raw.T
T1 = Rmat * T0 - T0 * Rmat
double_commutator = (
    Rmat * (Rmat * T0 - T0 * Rmat)
    - (Rmat * T0 - T0 * Rmat) * Rmat
)
T2 = sp.Rational(1, 2) * double_commutator + derived_shift * T0

check("R is exactly skew-symmetric", Rmat.T == -Rmat)
check("T1=[R,T0] is exactly symmetric", T1.T == T1)
check("T2 is exactly symmetric", T2.T == T2)
check(
    "T2 - (1/2)[R,[R,T0]] = 3T0 exactly",
    T2 - sp.Rational(1, 2) * double_commutator == derived_shift * T0,
)

relative_corrections: list[sp.Expr] = []
mixing_terms: list[sp.Expr] = []
for i, mu_i in enumerate(eigenvalues):
    mixing = sum(
        T1[k, i] ** 2 / (mu_i - eigenvalues[k])
        for k in range(len(eigenvalues))
        if k != i
    )
    mixing_terms.append(sp.simplify(mixing))
    check(
        f"state {i}: mixing cancels half the double commutator",
        sp.simplify(
            mixing
            + sp.Rational(1, 2) * double_commutator[i, i]
        )
        == 0,
    )
    correction = sp.simplify(T2[i, i] + mixing)
    relative_corrections.append(sp.simplify(correction / mu_i))

check(
    "all five relative second-order corrections equal 3",
    relative_corrections == [sp.Integer(3)] * len(eigenvalues),
)
check(
    "all pairwise log-ratio second-order contributions vanish",
    all(
        sp.simplify(relative_corrections[i] - relative_corrections[j]) == 0
        for i in range(len(eigenvalues))
        for j in range(i)
    ),
)


print("[Part 3] similarity-expansion interpretation and falsifier")
eps = sp.Symbol("eps")
identity = sp.eye(T0.rows)
left = identity + eps * Rmat + eps**2 * Rmat**2 / 2
right = identity - eps * Rmat + eps**2 * Rmat**2 / 2
expanded = sp.expand(left * T0 * right)


def matrix_coefficient(matrix: sp.Matrix, symbol: sp.Symbol, degree: int) -> sp.Matrix:
    return matrix.applyfunc(lambda value: sp.expand(value).coeff(symbol, degree))


check(
    "orthogonal-similarity expansion has first coefficient [R,T0]",
    matrix_coefficient(expanded, eps, 1) == T1,
)
check(
    "orthogonal-similarity expansion has second coefficient half double commutator",
    matrix_coefficient(expanded, eps, 2)
    == sp.Rational(1, 2) * double_commutator,
)

nonuniform = sp.diag(0, 0, 0, 0, 1)
T2_control = T2 + nonuniform
control_relative = [
    sp.simplify((T2_control[i, i] + mixing_terms[i]) / eigenvalues[i])
    for i in range(len(eigenvalues))
]
check(
    "falsifier: a nonuniform second-order remainder breaks ratio cancellation",
    len(set(control_relative)) > 1,
)

print(f"relative corrections: {relative_corrections}")
print(f"control relative corrections: {control_relative}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
