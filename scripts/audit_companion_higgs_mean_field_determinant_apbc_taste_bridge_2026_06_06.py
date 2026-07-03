#!/usr/bin/env python3
"""Exact determinant bridge for the Higgs mean-field curvature packet.

Checks:
- APBC / hypercube count: 2^4 = 16, matching 4 spin x 4 taste.
- Explicit Euclidean Cl(4) gamma matrices satisfy D_spin^2 = 4 I.
- The spin-taste and color-lifted mean-field operators satisfy
  D_mf^dag D_mf = 4 u_0^2 I_48.
- The trace-log generating functional has W''(0)/48 = 1/(4 u_0^2), matching
  4/(u_0^2 N_taste) at N_taste=16.
"""

from __future__ import annotations

from itertools import product
import sys

import sympy as sp
from sympy.physics.quantum import TensorProduct


RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")


def zero_matrix(m: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in list(m))


def part_1_counts() -> None:
    print("\n[Part 1] APBC / hypercube taste count")
    d = 4
    corners = list(product((0, 1), repeat=d))
    n_apbc = len(corners)
    n_spin = 4
    n_taste = 4
    record("binary APBC hypercube count is 2^4 = 16", n_apbc == 16, f"count={n_apbc}")
    record("spin x taste carrier dimension is 4 x 4 = 16", n_spin * n_taste == 16)
    record("two taste-count descriptions agree", n_apbc == n_spin * n_taste)


def gamma_matrices() -> list[sp.Matrix]:
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    i2 = sp.eye(2)
    return [
        TensorProduct(s1, s1),
        TensorProduct(s1, s2),
        TensorProduct(s1, s3),
        TensorProduct(s2, i2),
    ]


def part_2_clifford() -> sp.Matrix:
    print("\n[Part 2] explicit Euclidean Cl(4) Dirac element")
    gammas = gamma_matrices()
    i4 = sp.eye(4)
    clifford_ok = True
    for a, b in product(range(4), repeat=2):
        target = 2 * i4 if a == b else sp.zeros(4)
        if not zero_matrix(gammas[a] * gammas[b] + gammas[b] * gammas[a] - target):
            clifford_ok = False
    record("{gamma_mu,gamma_nu}=2 delta_mu_nu I", clifford_ok)
    d_spin = sum(gammas, sp.zeros(4))
    record("D_spin^2 = 4 I_4", zero_matrix(d_spin * d_spin - 4 * i4))
    record("D_spin is Hermitian", zero_matrix(d_spin.H - d_spin))
    return d_spin


def part_3_lifts(d_spin: sp.Matrix) -> None:
    print("\n[Part 3] spin-taste/color lift and mean-field determinant form")
    u0, j = sp.symbols("u_0 J", positive=True, real=True)
    i4 = sp.eye(4)
    i16 = sp.eye(16)
    i48 = sp.eye(48)
    d16 = TensorProduct(d_spin, i4)
    d48 = TensorProduct(sp.eye(3), d16)
    record("D_16 has spin-taste dimension 16", d16.shape == (16, 16))
    record("D_16^dag D_16 = 4 I_16", zero_matrix(d16.H * d16 - 4 * i16))
    record("color lift has dimension 48", d48.shape == (48, 48))
    record("D_48^dag D_48 = 4 I_48", zero_matrix(d48.H * d48 - 4 * i48))

    d_mf = u0 * d48
    positive_operator = sp.simplify(d_mf.H * d_mf)
    record("D_mf^dag D_mf = 4 u_0^2 I_48", zero_matrix(positive_operator - 4 * u0**2 * i48))

    n_tot = 48
    n_taste = 16
    w = sp.Rational(n_tot, 2) * sp.log(j**2 + 4 * u0**2)
    curvature = sp.simplify(sp.diff(w, j, 2).subs(j, 0))
    per_mode = sp.simplify(curvature / n_tot)
    r_lattice = sp.simplify(sp.Rational(4, 1) / (u0**2 * n_taste))
    target = sp.Rational(1, 1) / (4 * u0**2)
    record("W(J) = (48/2) log(J^2 + 4 u_0^2) gives W''(0)=48/(4u_0^2)",
           sp.simplify(curvature - n_tot / (4 * u0**2)) == 0,
           f"W''={curvature}")
    record("W''(0)/48 = 1/(4 u_0^2)", sp.simplify(per_mode - target) == 0, f"per_mode={per_mode}")
    record("4/(u_0^2 N_taste) at N_taste=16 equals 1/(4u_0^2)",
           sp.simplify(r_lattice - target) == 0,
           f"R={r_lattice}")
    record("per-mode curvature matches R_lattice", sp.simplify(per_mode - r_lattice) == 0)


def main() -> int:
    print("=" * 78)
    print("Higgs mean-field determinant APBC taste bridge")
    print("No physical Higgs mass identification; finite determinant algebra only.")
    print("=" * 78)
    part_1_counts()
    d_spin = part_2_clifford()
    part_3_lifts(d_spin)

    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    n_fail = sum(1 for _, ok, _ in RESULTS if not ok)
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for name, ok, detail in RESULTS:
        suffix = f" ({detail})" if detail else ""
        print(f"  {'PASS' if ok else 'FAIL'} {name}{suffix}")
    print(f"\nTOTAL: {n_pass} PASS / {n_fail} FAIL")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
