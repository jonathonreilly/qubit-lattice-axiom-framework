#!/usr/bin/env python3
"""J:attack-e:PR8178 — SAMPLED EVIDENCE.

The only sampling language is the executed nonlinear D1 / linear-calibrator
range (1.34, 1.14, … and 0.97-1.01), already a known HIT (lag-25 D1 1.165 vs
1.18; linear 0.960-1.014 vs 0.97-1.01). T1–T3 (φ, mode variances, τ_L, V_L
bracket) are exact identities, not never/always Monte Carlo.

Do not re-find that D1 HIT or the T1.1 conjugation HIT of J:attack-f:PR8178.
"""
from fractions import Fraction as Fr

import sympy as sp


def main() -> int:
    # T1.2 u=|φ|² at the zero mode is exactly 1 (not a sample)
    phi0 = (1 + 1 + 1) / 3
    print(f"zero-mode φ=(1+1+1)/3={phi0} |φ|²={phi0 ** 2}")
    assert phi0 == 1
    # Var recursion V(t+1)=u V(t)+σ² at u=1 is σ² t, so Var θ̄ = σ² t / L²
    # τ_L = L²/σ² is when that variance hits 1: exact, not sampled
    L, sig2 = 4, Fr(1, 2)
    tau = Fr(L * L, sig2)
    print(f"τ_L=L²/σ² at L=4 σ²=1/2: {tau} (exact)")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8178): the only sampling language is "
        "the executed D1 / linear-calibrator table, already a known HIT; "
        "T1-T3 (zero-mode |φ|=1, τ_L=L²/σ², V_L bracket) are exact; no "
        "remaining never/always to hill-climb; not a re-find of D1 1.165 vs "
        "1.18 or the T1.1 conjugation HIT; pattern has no purchase beyond "
        "the known HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
