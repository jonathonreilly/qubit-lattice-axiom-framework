#!/usr/bin/env python3
"""J:attack-f:PR8173 — NORMALIZATION of Fourier N, N^{-1/2}, 1/N.

Declared objects: ŝ^a(k) = N^{-1/2} Σ_x e^{-ik·x} s_x^a, k in (2π/L) Z^3.
T2 writes βh · N ⟨(m̂¹)²⟩ = ⟨m̂³⟩ and the proof sets Σ_x s_x^3 = N m̂³,
i.e. m̂ = N^{-1} Σ s (magnetization density), not the declared k=0 Fourier
mode N^{-1/2} Σ s. T3 / D1 mix the same N vs N^{-1/2} in Parseval.

Do not re-find the known executed-numbers HIT on c(β,k) in 0.86–0.98.

Exact: Ward in extensive magnetizations (the proof's cancellation) plus
the two translations of m̂; Parseval on a 4-ring with rational data under
both conventions.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def check_t2_factor():
    print("== T2: declared Fourier m̂ = N^{-1/2} M vs proof m̂ = N^{-1} M ==")
    # Ward identity as proved (bond terms cancel): <M^3> = beta h <(M^1)^2>
    # with M^a = Σ_x s_x^a. Independent of Fourier convention.
    beta, h, N = sp.symbols("beta h N", positive=True)
    M1, M3 = sp.symbols("M1 M3", real=True)
    # two translations
    m_four = lambda M: M / sp.sqrt(N)  # declared ŝ(k=0)
    m_dens = lambda M: M / N  # proof's Σ s = N m̂
    # claimed T2: beta h * N * <(m1)^2> - <m3>  == 0
    claimed = lambda m1, m3: beta * h * N * m1 ** 2 - m3
    # substitute Ward <M3> = beta h <M1^2> at the level of the quadratic
    # monomials (the identity is linear in the 3-component and quadratic in 1).
    ward_M3 = beta * h * M1 ** 2
    gap_four = sp.simplify(claimed(m_four(M1), m_four(ward_M3)))
    gap_dens = sp.simplify(claimed(m_dens(M1), m_dens(ward_M3)))
    print(f"  T2 residual with declared ŝ(0)=N^{{-1/2}} M: {gap_four}")
    print(f"  T2 residual with proof m̂=N^{{-1}} M:         {gap_dens}")
    # density convention: residual 0
    if gap_dens != 0:
        hit(f"density convention does not close T2: residual {gap_dens}")
    # Fourier convention: residual = beta h M1^2 (sqrt(N) - 1) or similar
    # gap_four = beta*h*N*(M1^2/N) - (beta*h*M1^2)/sqrt(N)
    #          = beta*h M1^2 (1 - N^{-1/2})
    expected = beta * h * M1 ** 2 * (1 - 1 / sp.sqrt(N))
    if sp.simplify(gap_four - expected) != 0:
        # still a HIT if nonzero
        if gap_four == 0:
            print("  declared Fourier accidentally closes T2")
        else:
            hit(
                f"T2 βh N⟨(m̂¹)²⟩=⟨m̂³⟩ fails for declared ŝ=N^{{-1/2}}Σ: "
                f"residual {gap_four} (expected {expected})"
            )
    else:
        hit(
            "T2 βh·N⟨(m̂¹)²⟩=⟨m̂³⟩ uses m̂=N^{-1}Σs (proof: Σs=N m̂) but the "
            f"declared Fourier ŝ(k=0)=N^{{-1/2}}Σs leaves residual "
            f"βh M1² (1-N^{{-1/2}}); factor √N at every L>1"
        )
    for L in (2, 3, 4):
        Nv = L ** 3
        # residual / (beta h M1^2) = 1 - N^{-1/2}
        factor = sp.sqrt(Nv)
        print(f"  L={L} N={Nv}: LHS/RHS of T2 under declared ŝ is {factor} (not 1)")


def check_parseval():
    print("== T3/D1 Parseval on a 4-ring, both conventions ==")
    f = [Fraction(3, 7), Fraction(-2, 7), Fraction(5, 7), Fraction(1, 7)]
    N = 4
    # unnormalized hat(k) = Σ_x f_x exp(-2π i k x / N)  [D1]
    # unitary hat(k) = N^{-1/2} * unnormalized          [declared]
    F_unn = []
    F_uni = []
    for k in range(N):
        acc = sum(
            (sp.Rational(f[x].numerator, f[x].denominator) * sp.exp(-2 * sp.pi * sp.I * k * x / N))
            for x in range(N)
        )
        acc = sp.simplify(acc)
        F_unn.append(acc)
        F_uni.append(sp.simplify(acc / sp.sqrt(N)))
    sum_unn = sp.simplify(sum(sp.Abs(z) ** 2 for z in F_unn) / N)
    sum_uni = sp.simplify(sum(sp.Abs(z) ** 2 for z in F_uni) / N)
    sum_sq = sum(fx * fx for fx in f)
    avg_sq = sum_sq / N
    print(f"  N^{{-1}} Σ|hat_unn|^2 = {sum_unn}")
    print(f"  N^{{-1}} Σ|hat_uni|^2 = {sum_uni}")
    print(f"  Σ_x f_x^2             = {sum_sq}")
    print(f"  ⟨f_x^2⟩               = {avg_sq}")
    # D1 printed identity: N^{-1} Σ |hat|^2 = Σ f^2  — holds for unnormalized only
    d1_unn = sp.simplify(sum_unn - sp.Rational(sum_sq.numerator, sum_sq.denominator)) == 0
    d1_uni = sp.simplify(sum_uni - sp.Rational(sum_sq.numerator, sum_sq.denominator)) == 0
    # T3 statement: N^{-1} Σ |ŝ|^2 = ⟨f^2⟩  — holds for unitary only
    t3_unn = sp.simplify(sum_unn - sp.Rational(avg_sq.numerator, avg_sq.denominator)) == 0
    t3_uni = sp.simplify(sum_uni - sp.Rational(avg_sq.numerator, avg_sq.denominator)) == 0
    print(f"  D1 identity holds unnormalized={d1_unn} unitary={d1_uni}")
    print(f"  T3 identity holds unnormalized={t3_unn} unitary={t3_uni}")
    if not d1_unn:
        hit("D1 unnormalized Parseval failed on the 4-ring rational data")
    if not t3_uni:
        hit("T3 unitary Parseval failed on the 4-ring rational data")
    if d1_uni:
        print("  D1 identity accidentally holds for declared ŝ (unexpected)")
    else:
        # this is the convention clash: D1's printed equation is false for declared ŝ
        hit(
            "D1 prints N^{-1}Σ_k|f̂(k)|² = Σ_x f_x² (true only for unnormalized "
            "DFT hat=Σ e^{-ikx} f); under the declared ŝ=N^{-1/2}Σ the same "
            f"4-ring data gives N^{{-1}}Σ|ŝ|²={sum_uni} != Σ f²={sum_sq} "
            f"(equals ⟨f²⟩={avg_sq} instead, which is T3)"
        )


def check_GL_inversion():
    """G_L(r)=N^{-1} Σ_{k≠0} e^{ikr}/E(k) inverts Δ on the zero-sum subspace."""
    print("== G_L inversion (N^{-1}, e^{+ikr}) on T_L^3, L=2,4 ==")
    for L in (2, 4):
        N = L ** 3
        sites = list(product(range(L), repeat=3))

        def E(n):
            return sum(2 * (1 - sp.cos(2 * sp.pi * nj / L)) for nj in n)

        def G(r):
            acc = 0
            for n in product(range(L), repeat=3):
                if n == (0, 0, 0):
                    continue
                kdot = 2 * sp.pi * sum(n[j] * r[j] for j in range(3)) / L
                acc += sp.exp(sp.I * kdot) / E(n)
            return sp.simplify(acc / N)

        # (ΔG)_0 = Σ_{y~0} (G(0)-G(y)) should equal 1 - 1/N
        G0 = G((0, 0, 0))
        lap0 = 0
        for j in range(3):
            for s in (1, -1):
                y = [0, 0, 0]
                y[j] = s % L
                lap0 += G0 - G(tuple(y))
        lap0 = sp.simplify(sp.re(lap0))
        want = 1 - sp.Rational(1, N)
        print(f"  L={L}: (ΔG)_0={lap0} want {want}")
        if sp.simplify(lap0 - want) != 0:
            hit(f"G_L inversion fails at L={L}: (ΔG)_0={lap0} != 1-1/N={want}")


def main() -> int:
    check_t2_factor()
    check_parseval()
    check_GL_inversion()
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: NORMALIZATION (PR #8173): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8173): declared ŝ=N^{-1/2}Σ, T2/D1 N-factors "
        "and Parseval identities recompute consistently; no convention clash"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
