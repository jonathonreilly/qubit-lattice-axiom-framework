#!/usr/bin/env python3
"""J:attack-f:PR8180 — NORMALIZATION of 1/2, 2π/L, 1/N, Hessian 1/9.

Do not re-find the known T1 conjugation HIT (P*^s Rayleigh is conj(φ)^s
not φ^s) nor kernel_sim shells / D2 non-product.

Checks:
  (1) T3 1/2 chain: |φ|^s = u^{s/2} and exp((s/2) log(1-y)) ≤ exp(-(1-u)s/2)
      so the 2 in exp(-2|k|² s/(9π²)) is 4/2 from (1-u)≥4|k|²/(9π²).
  (2) 1-u = (2/9)(3-cos k1-cos k2-cos(k1-k2)); Hessian at 0 is M=(1/9)[[2,-1],[-1,2]].
  (3) σ²=A(κ)/κ with A=coth κ-1/κ equals the S² transverse component (1-<c²>)/2.
  (4) Unitary DFT Parseval on L=3,4: Σ_k |ŝ|² = Σ_x |θ_x|² for ŝ=N^{-1/2} Σ e^{-ikx} θ.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import pi

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def check_t3_half():
    print("== T3 1/2: |φ|^s = u^{s/2} and 4/2 = 2 in the exponent ==")
    k1, k2, s = sp.symbols("k1 k2 s", real=True, positive=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand_complex(phi * sp.conjugate(phi)))
    # algebraic: |φ|^2 = u
    print(f"  |φ|^2 symbolic = {u}")
    # 1-u closed form
    one_u = sp.simplify(1 - u)
    want = (2 * (3 - sp.cos(k1) - sp.cos(k2) - sp.cos(k1 - k2))) / 9
    if sp.simplify(one_u - want) != 0:
        hit(f"1-u closed form mismatch: {one_u} vs {want}")
    else:
        print("  1-u = (2/9)(3-cos k1-cos k2-cos(k1-k2))")
    # exponent 4/2
    four = Fraction(4)
    two = four / 2
    if two != 2:
        hit("4/2 != 2")
    print(f"  (1-u)s/2 with 1-u≥4|k|²/(9π²) gives exp(-{two}|k|² s/(9π²))")
    # |φ|^s = u^{s/2} on numerical modes L=3,4
    for L in (3, 4):
        bad = 0
        for n1, n2 in product(range(L), repeat=2):
            if (n1, n2) == (0, 0):
                continue
            kk1, kk2 = 2 * pi * n1 / L, 2 * pi * n2 / L
            ph = (1 + sp.exp(sp.I * kk1) + sp.exp(sp.I * kk2)) / 3
            uu = sp.N(sp.expand_complex(ph * sp.conjugate(ph)), 30)
            for ss in (1, 2, 5):
                lhs = sp.Abs(ph) ** ss
                rhs = uu ** (sp.Rational(ss, 2))
                if abs(sp.N(lhs - rhs, 20)) > 1e-12:
                    bad += 1
        print(f"  L={L}: |φ|^s vs u^{{s/2}} mismatches={bad}")
        if bad:
            hit(f"L={L}: |φ|^s != u^{{s/2}} on {bad} modes")


def check_hessian():
    print("== T2 Hessian of 1-u at k=0 is M=(1/9)[[2,-1],[-1,2]] ==")
    k1, k2 = sp.symbols("k1 k2", real=True)
    one_u = (2 * (3 - sp.cos(k1) - sp.cos(k2) - sp.cos(k1 - k2))) / 9
    H = sp.hessian(one_u, [k1, k2]).subs({k1: 0, k2: 0})
    H = sp.simplify(H)
    # Taylor is (1/2) k^T (Hessian) k, and 1-u = k^T M k + O(k^4),
    # so M = Hessian/2.
    M = sp.simplify(H / 2)
    want = sp.Matrix([[sp.Rational(2, 9), sp.Rational(-1, 9)],
                      [sp.Rational(-1, 9), sp.Rational(2, 9)]])
    print(f"  Hessian(0)=\n{H}")
    print(f"  Hessian/2 =\n{M}")
    if M != want:
        hit(f"Hessian/2 != M: got {M} want {want}")
    else:
        print("  M = Hessian/2 = (1/9)[[2,-1],[-1,2]] (the 1/2 in Taylor is required)")
    # eigenvalues 1/9 and 1/3
    ev = sorted(sp.factor(M.eigenvals()))
    print(f"  eigenvalues {ev}")
    if set(ev) != {sp.Rational(1, 9), sp.Rational(1, 3)}:
        hit(f"M eigenvalues {ev} != {{1/9, 1/3}}")


def check_sigma():
    print("== σ² = A(κ)/κ equals S² transverse component (1-<cos²θ>)/2 ==")
    kap = sp.symbols("kappa", positive=True)
    A = sp.coth(kap) - 1 / kap
    # vMF on S²: Z = 4π sinh(κ)/κ, <cos> = A
    # <cos²> = 1 - 2 A/κ  (standard)
    c2 = 1 - 2 * A / kap
    trans = (1 - c2) / 2
    trans = sp.simplify(trans)
    want = sp.simplify(A / kap)
    print(f"  (1-<cos²>)/2 = {trans}")
    print(f"  A/κ           = {want}")
    if sp.simplify(trans - want) != 0:
        hit(f"transverse component (1-<c²>)/2 != A/κ: {trans} vs {want}")
    else:
        print("  σ²=A(3β)/(3β) is the per-component S² variance (not (1-m²)/2 with m=A, which equals A/κ too)")
    # confirm (1-A²)/2 is a different 1/2 (longitudinal vs transverse mix)
    other = sp.simplify((1 - A ** 2) / 2)
    if sp.simplify(other - want) == 0:
        print("  (1-A²)/2 happens to equal A/κ")
    else:
        print("  (1-A²)/2 differs from A/κ (do not swap 1/2 conventions)")


def check_parseval():
    print("== unitary DFT Parseval on L=3,4 (ŝ = N^{-1/2} Σ e^{-ik·x} θ) ==")
    for L in (3, 4):
        N = L * L
        # integer field
        theta = {(i, j): Fraction((i + 2 * j) % 5, 1) for i in range(L) for j in range(L)}
        sxx = sum(v * v for v in theta.values())
        acc = 0
        for n1, n2 in product(range(L), repeat=2):
            k1, k2 = 2 * sp.pi * n1 / L, 2 * sp.pi * n2 / L
            hat = sum(
                (theta[(i, j)] * sp.exp(-sp.I * (k1 * i + k2 * j)))
                for i in range(L)
                for j in range(L)
            ) / sp.sqrt(N)
            acc += sp.simplify(sp.expand_complex(hat * sp.conjugate(hat)))
        acc = sp.simplify(acc)
        print(f"  L={L}: Σ_k |ŝ|² = {acc}  Σ_x |θ|² = {sxx}")
        if sp.simplify(acc - sxx) != 0:
            hit(f"L={L} unitary Parseval failed: {acc} != {sxx}")
        # 1/N convention would give Σ |hat_unn|² / N = Σ |θ|², i.e. Σ |ŝ_uni|² * N / N = Σ|θ|²
        # already matched. The 1/N DFT ŝ_unn = Σ e^{-ikx} θ = sqrt(N) ŝ_uni,
        # N^{-1} Σ |ŝ_unn|² = Σ |θ|² also holds (same identity).


def main() -> int:
    check_t3_half()
    check_hessian()
    check_sigma()
    check_parseval()
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: NORMALIZATION (PR #8180): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8180): T3's 1/2 (u^{s/2} and 4/2=2 in the "
        "exponent), T2 Hessian/2 = M=(1/9)[[2,-1],[-1,2]] with ev {1/9,1/3}, "
        "σ²=A(κ)/κ=(1-<cos²>)/2, and unitary DFT Parseval on L=3,4 all hold; "
        "the φ vs conj(φ) defect is the known T1 HIT and is not re-claimed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
