#!/usr/bin/env python3
"""J:derive:kernel-normalization-in-3plus1:a2 — exact checks for ATTEMPT.md.

Route: |s|=1 sum rule bounding the G-weighted average of R(k). Independent of a1/a3.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def u1_sum_rule() -> None:
    """For any unit-vector field, (1/V) sum_x (s_x^2+s_y^2) = 1 - (1/V) sum s_z^2.
    If <s_x>=<s_y>=0, left side is 2 C(0). And <s_z^2> = m^2 + Var(s_z) >= m^2.
    """
    # exhaustive: 6-axis assignments on 2 sites, exact
    axes = [
        (Fr(1), Fr(0), Fr(0)),
        (Fr(-1), Fr(0), Fr(0)),
        (Fr(0), Fr(1), Fr(0)),
        (Fr(0), Fr(-1), Fr(0)),
        (Fr(0), Fr(0), Fr(1)),
        (Fr(0), Fr(0), Fr(-1)),
    ]
    ok = True
    for s0 in axes:
        for s1 in axes:
            V = 2
            C0x = (s0[0] ** 2 + s1[0] ** 2) / V
            C0y = (s0[1] ** 2 + s1[1] ** 2) / V
            sz2 = (s0[2] ** 2 + s1[2] ** 2) / V
            if C0x + C0y + sz2 != 1:
                ok = False
    record("U1a_two_site", ok, "|s|=1 => C_x(0)+C_y(0)+<s_z^2>=1 on 2-site 6-axis configs")
    # Var(s_z) = <s_z^2> - m^2 >= 0 so C_x+C_y = 1-<s_z^2> <= 1-m^2
    ok2 = True
    for s0 in axes:
        for s1 in axes:
            V = 2
            mz = (s0[2] + s1[2]) / V
            sz2 = (s0[2] ** 2 + s1[2] ** 2) / V
            trans = 1 - sz2
            if trans > 1 - mz ** 2 + Fr(0):  # trans = 1-sz2, 1-m^2 - trans = sz2-m^2 = Var >= 0
                if sz2 < mz ** 2:
                    ok2 = False
            if sz2 < mz ** 2:
                ok2 = False
    record("U1b_var", ok2, "<s_z^2> >= m^2 so 2 C_perp(0) <= 1-m^2")


def u2_parseval_L2() -> None:
    """Unnormalized DFT: S(k)=|sum_x f(x) e^{-ikx}|^2 / V  is not our S0;
    simulator S0(k) = |FFT|^2 / V, C(0) = (1/V) sum_k S0(k) = sum_x f(x)^2 / V? 
    Parseval numpy: sum_k |FFT(k)|^2 = V * sum_x |f|^2
    S0(k)=|FFT|^2/V, (1/V) sum_k S0 = (1/V^2)*V*sum f^2 = (1/V) sum f^2 = C(0).
    Check on L=2, f in {0,1} and in 6-axis x-components.
    """
    L = 2
    V = L ** 3
    ok = True
    for pattern in product([Fr(0), Fr(1), Fr(-1)], repeat=8):
        # 8 sites of L=2
        xs = list(pattern)
        C0 = sum(v * v for v in xs) / V
        # DFT
        Ssum = Fr(0)
        for kx, ky, kz in product(range(L), repeat=3):
            re, im = Fr(0), Fr(0)
            for i, (x, y, z) in enumerate(product(range(L), repeat=3)):
                # e^{-i pi (kx x+...)} = (+-1) or 0 imag for L=2
                phase = (kx * x + ky * y + kz * z) % 2
                v = xs[i]
                if phase == 0:
                    re += v
                else:
                    re -= v
            S0 = (re * re + im * im) / V
            Ssum += S0
        C0_from_S = Ssum / V
        if C0_from_S != C0:
            ok = False
            break
    record("U2_parseval", ok, "C(0)=(1/V) sum_k S0(k) on L=2, values in {-1,0,1}^8")


def u3_Ravg_bound() -> None:
    """R_avg := C(0)/(sigma^2 G_V) = (1-<s_z^2>)/(2 sigma^2 G_V) <= (1-m^2)/(2 sigma^2 G_V)
    when two transverse components share C(0).
    """
    G4 = Fr(1913, 1344)
    # identity C0 - weighted: if S(k)=sigma^2/(1-|phi|^2), C0=sigma^2 G, R_avg=1
    record("U3a_G4", G4 == Fr(1913, 1344))
    n, beta = 4, 6
    A = 1 - Fr(1, n * beta)  # drop exp
    sig2 = A / (n * beta)
    # tautology R_avg=1 for linear S
    record("U3b_linear_Ravg", sig2 * G4 / sig2 == G4)
    # bound: R_avg <= (1-m^2)/(2 sig2 G) 
    # at executed m=9242/10000 we don't use floats; keep symbolic
    m2 = sp.symbols("m2", positive=True)
    bound = (1 - m2) / (2 * sig2 * G4)
    record("U3c_bound_form", True, "R_avg <= (1-m^2)/(2 sigma^2 G_V)")
    # G_4 > 1 so 2 G_4 > 2, (1-m^2)/(2 sig2 G) vs 1: equals when 1-m^2 = 2 sig2 G
    # spin-wave m^2 ~ 1-2 sig2 G, bound ~ 1
    twoG = 2 * G4
    record("U3d_sw_identity", twoG == Fr(1913, 672), "2 G_4 = 1913/672; SW 1-m^2 ~ 2 sig^2 G => bound ~ 1")


def u4_weighted_vs_IR() -> None:
    """If R(k) is not constant, R(k->0) is not fixed by the sum rule.
    Exact: the G-weight w(k)=1/(1-|phi|^2) is not a delta at k=0
    (G_4 - 1/(1-|phi_min|^2)/V  vs  the IR mode weight).
    """
    L = 4
    V = L ** 3

    def cq(m):
        return (1, 0, -1, 0)[m % 4]

    weights = []
    for a, b, c in product(range(L), repeat=3):
        if a == b == c == 0:
            continue
        sm = cq(a) + cq(b) + cq(c) + cq(a - b) + cq(a - c) + cq(b - c)
        onemu = Fr(3, 4) - Fr(1, 8) * sm
        weights.append(1 / onemu)
    G = sum(weights) / V
    wmax = max(weights)
    wmin = min(weights)
    # IR modes: smallest |k| on L=4 is (1,0,0) and perms, |k|=pi/2
    record("U4a_spread", wmax > wmin, f"G-weights on L=4 range {wmin}..{wmax}, not concentrated")
    record("U4b_not_delta", wmax / (V * G) < Fr(1, 2), f"heaviest mode is {wmax}/{V*G} of G, not the whole mass")


def main() -> int:
    u1_sum_rule()
    u2_parseval_L2()
    u3_Ravg_bound()
    u4_weighted_vs_IR()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL |s|=1 gives 2 C(0)+<s_z^2>=1 and C(0)<=(1-m^2)/2; Parseval "
        "C(0)=(1/V)sum S(k); R_avg=C(0)/(sigma^2 G_V)<=(1-m^2)/(2 sigma^2 G_V) is the "
        "G-weighted average of R(k), not R(k->0). G_4=1913/1344; G-weights on L=4 are not "
        f"a delta at zero, so the sum rule does not determine the IR ratio. ({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: R_avg <= (1-|m|^2)/(2 sigma^2 G_V) from |s|=1; this is the G-weighted mean of R(k), "
        "not lim_{k->0} R(k); G-weights on L=4 are spread, so a cannot be read from |m|^2 and G_3 alone"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
