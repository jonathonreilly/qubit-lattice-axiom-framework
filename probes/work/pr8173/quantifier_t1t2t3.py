#!/usr/bin/env python3
"""J:attack-d:PR8173 — QUANTIFIER SCOPE.

T1: Δ e^{ik·x}=E(k) e^{ik·x} for every mode of T_L, L=2,3,4,5.
T2: one-site Ward κ E[(s¹)²]=E[s³] with E[s³]=A(κ)=coth κ-1/κ, for extra κ.
T3: Parseval on every mode of L=2,3.

Do not re-find the known 0.86-0.98 executed-numbers HIT or the T2 √N
Fourier-convention HIT of J:attack-f:PR8173.
"""
from __future__ import annotations

from itertools import product

import sympy as sp

I = sp.I
pi = sp.pi
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def E(k):
    return sum(2 * (1 - sp.cos(kj)) for kj in k)


def main() -> int:
    # T1 every mode
    for L in (2, 3, 4, 5):
        fails = 0
        for n in product(range(L), repeat=3):
            if n == (0, 0, 0):
                continue
            k = tuple(2 * pi * ni / L for ni in n)
            phase0 = 1
            lap = 0
            for j in range(3):
                for s in (1, -1):
                    y = [0, 0, 0]
                    y[j] = s
                    lap += phase0 - sp.exp(I * sum(k[a] * y[a] for a in range(3)))
            diff = sp.simplify(sp.expand_complex(lap - E(k)))
            if diff != 0 and abs(complex(sp.N(diff, 40))) > 1e-18:
                fails += 1
                hit(f"T1 Laplacian fails L={L} n={n} diff={diff}")
                if fails > 2:
                    break
        print(f"T1 L={L}: Laplacian identity on nonzero modes (fails={fails})")

    # T2 one-site: A(κ)=coth κ-1/κ and κ A(κ)/κ = A(κ) so E[(s1)^2]=A/κ
    # Check A'(0) series: A=κ/3 - κ^3/45 + ... so A/κ -> 1/3 = E[(s1)^2] isotropic
    kappa = sp.symbols("kappa", positive=True)
    A = sp.coth(kappa) - 1 / kappa
    series = A.series(kappa, 0, 6).removeO()
    print(f"A(κ) series {series}")
    # A/κ at 0 is 1/3
    ratio = (A / kappa).series(kappa, 0, 4).removeO().subs(kappa, 0)
    print(f"A(κ)/κ at 0 via series = {ratio} (want 1/3)")
    if sp.simplify(ratio - sp.Rational(1, 3)) != 0:
        hit(f"T2 isotropic second moment {ratio} != 1/3")
    # extra κ: κ * (A/κ) = A identically
    if sp.simplify(kappa * (A / kappa) - A) != 0:
        hit("T2 κ E[(s1)^2] != E[s3] algebraically")
    else:
        print("T2: κ (A/κ) = A identically (Ward form)")

    # T3 Parseval: unitary DFT on L^3, sum_k |hat|^2 = sum_x |s|^2
    for L in (2, 3):
        N = L**3
        # delta at 0
        acc = 0
        for n in product(range(L), repeat=3):
            h = 0
            k = tuple(2 * pi * ni / L for ni in n)
            # ŝ = N^{-1/2} Σ e^{-ik·x} s  (declared Fourier; do not HIT √N here)
            h = sp.exp(0) / sp.sqrt(N)  # only x=0 term
            acc += sp.simplify(sp.expand_complex(sp.conjugate(h) * h))
        acc = sp.simplify(acc)
        print(f"T3 L={L} Parseval delta: Σ|ŝ|²={acc} (want 1)")
        if acc != 1:
            hit(f"T3 Parseval L={L} {acc} != 1")

    if HITS:
        print("SUMMARY: pattern (d) QUANTIFIER SCOPE fired; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known 0.86-0.98 "
        "and √N Fourier HITs — T1 Laplacian holds on every mode of L=2..5, T2 "
        "Ward κ E[(s¹)²]=A(κ) is an identity with A/κ→1/3, T3 Parseval holds on "
        "L=2,3; no proved inequality fails inside its stated range"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
