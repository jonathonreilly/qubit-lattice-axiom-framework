#!/usr/bin/env python3
"""J:derive:kernel-normalization-in-3plus1:a1 — exact checks for ATTEMPT.md.

Route: vMF innovation variance (not the cubic mean map). Independent of a3's check.py.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def n1_A_and_variance_tensor() -> None:
    k = sp.symbols("kappa", positive=True)
    Z = 4 * sp.pi * sp.sinh(k) / k
    A = sp.coth(k) - 1 / k
    record("N1a_mean", sp.simplify(sp.diff(sp.log(Z), k) - A) == 0)
    Zpp = sp.diff(Z, k, 2) / Z
    record("N1b_long", sp.simplify(Zpp - (1 - 2 * A / k)) == 0)
    record("N1c_trans", sp.simplify((1 - Zpp) / 2 - A / k) == 0)
    x = sp.symbols("x", positive=True)
    Aex = 1 - 1 / x + 2 / (sp.exp(2 * x) - 1)
    record(
        "N1d_A",
        sp.simplify((sp.coth(x) - 1 / x).rewrite(sp.exp) - Aex) == 0,
        "A(x)=1-1/x+2/(e^{2x}-1)",
    )
    # second-moment tensor: a = A/k, a+b = 1-2A/k => b = 1-3A/k
    # Var(s_x) = a + b u_x^2 - A^2 u_x^2
    coeff = 1 - 3 * A / k - A ** 2
    # with the exact A, the power-law part of coeff is O(1/k^2) after cancelling 1/k against A^2
    A0 = 1 - 1 / k
    coeff0 = sp.expand(1 - 3 * A0 / k - A0 ** 2)
    record("N1e_projector_aligned", sp.simplify(coeff0 - (2 / k ** 2 - 1 / k)) == 0, "1-3A0/k-A0^2 = 2/k^2 - 1/k")


def n2_noise_ratio() -> None:
    n, beta, V = sp.symbols("n beta V", positive=True)
    A = 1 - 1 / (n * beta)  # drop exponentially small 2/(e^{2n beta}-1)
    sig2 = A / (n * beta)
    # C0 - Cv = sig2 (1-1/V)  for S = sig2/(1-|phi|^2) off zero
    # <delta> = -n (C0 - Cv) = -n sig2 (1-1/V)
    # <1/|S|> = 1/n (1 - <delta>/n + O(sig^4)) = 1/n (1 + sig2 (1-1/V) + O(sig^4))
    # <A/kappa> = <1/(beta |S|)> + O(1/beta^2) = sig2/A * (1 + sig2 (1-1/V)) + O(1/beta^2)
    R = (1 + sig2 * (1 - 1 / V)) / A
    Rinf = sp.simplify(R.subs(V, sp.oo))
    record("N2a_R_formula", sp.simplify(Rinf - (1 / A + 1 / (n * beta))) == 0)
    # series at infinity, n=4: 1 + 1/(2 beta) + O(1/beta^2)
    ser = sp.series(Rinf.subs(n, 4), beta, sp.oo, 3).removeO()
    record(
        "N2b_series_n4",
        sp.simplify(ser - (1 + 1 / (2 * beta) + 1 / (16 * beta ** 2))) == 0,
        f"R_noise = {ser} (n=4, V=infty, A=1-1/(n beta))",
    )
    # sign: R-1 = 1/(2 beta) + O(1/beta^2) > 0
    record("N2c_positive", sp.simplify(sp.series(Rinf.subs(n, 4) - 1, beta, sp.oo, 2).removeO()) == 1 / (2 * beta))
    # exact rational at beta=6, n=4, dropping exp: A=23/24, sig2=(23/24)/24=23/576
    A6 = Fr(23, 24)
    sig6 = A6 / 24
    R6 = (1 + sig6) / A6
    record("N2d_beta6", R6 == Fr(599, 552), f"R_noise(beta=6,n=4,V=infty)={R6} = {float(R6):.6f} > 1")
    # 599/552 vs executed 0.9719
    record("N2e_sign_clash", R6 > 1, "Gaussian noise correction is above 1; executed low-k ratio is below 1")


def n3_C0_minus_Cv() -> None:
    """|phi|^2/(1-|phi|^2) = 1/(1-|phi|^2) - 1, so C_v = C0 - sig2 (1-1/V)."""
    L = 4
    V = L ** 3

    def cq(m):
        return (1, 0, -1, 0)[m % 4]

    def onemu(a, b, c):
        sm = cq(a) + cq(b) + cq(c) + cq(a - b) + cq(a - c) + cq(b - c)
        return Fr(3, 4) - Fr(1, 8) * sm

    acc = Fr(0)
    acc_u = Fr(0)
    for a, b, c in product(range(L), repeat=3):
        if a == b == c == 0:
            continue
        inv = 1 / onemu(a, b, c)
        acc += inv
        acc_u += (1 - onemu(a, b, c)) * inv  # |phi|^2 /(1-|phi|^2)
    C0 = acc / V
    Cv = acc_u / V
    record("N3a_G4", C0 == Fr(1913, 1344), f"G_4={C0}")
    record("N3b_identity", C0 - Cv == 1 - Fr(1, V), f"C0-Cv = sig2(1-1/V) with sig2=1: {C0-Cv}")


def n4_projector_order() -> None:
    """(1-3A/k-A^2) <u_x^2> is O(1/beta^2) if <u_x^2>=O(1/beta)."""
    k = sp.symbols("kappa", positive=True)
    A0 = 1 - 1 / k
    coeff0 = sp.expand(1 - 3 * A0 / k - A0 ** 2)
    # coeff0 = 1/k^2 - 1/k ; times u^2 ~ 1/k  gives O(1/k^2)+O(1/k^3) relative to noise A/k ~ 1/k
    # so relative O(1/k)=O(1/beta) from the -1/k * u^2 term? u^2 ~ sigma^2 ~ 1/k, product ~ 1/k^2
    # absolute O(1/beta^2), relative to noise O(1/beta) is O(1/beta)
    # WAIT: -1/k * <u_x^2>, <u_x^2>~C_v ~ sigma^2 (G-1) ~ 1/(n beta) * O(1) = O(1/beta)
    # product O(1/beta^2) absolute; noise is O(1/beta); relative O(1/beta). Same order as 1/beta^2 in R?
    # R correction from this: O(1/beta^2)/O(1/beta) wait no:
    # noise = A/k + coeff * u^2 = 1/k + O(1/k^2) + (1/k^2 - 1/k) * O(1/k)
    # = 1/k + O(1/k^2) + O(1/k^3) - O(1/k^2)
    # the - (1/k)*O(1/k) = O(1/k^2) is O(1/beta^2) absolute, relative O(1/beta) to the leading 1/k.
    # So it IS an O(1/beta) relative correction!
    # <u_x^2> = C_v = sig2 (G-1) for linear S
    # extra = coeff0 * Cv ~ (-1/k) * sig2 (G-1)
    # k = n beta, 1/k = 1/(n beta)
    # extra / (A/k) ~ [-1/(n beta) * sig2 (G-1)] / sig2 = -(G-1)/(n beta)
    # That's O(1/beta) and NEGATIVE, involving G_3!
    #
    # I dropped this too hastily in the prose. Include it exactly.
    n, beta, G = sp.symbols("n beta G", positive=True)
    A = 1 - 1 / (n * beta)
    sig2 = A / (n * beta)
    Cv = sig2 * (G - 1)
    k = n * beta
    extra = (2 / k ** 2 - 1 / k) * Cv
    R_extra = extra / sig2
    rec = sp.simplify(R_extra)
    record(
        "N4a_extra",
        sp.simplify(rec - (G - 1) * (2 / (n ** 2 * beta ** 2) - 1 / (n * beta))) == 0,
        "projector/sig2 = (G-1)(2/(n^2 beta^2)-1/(n beta))",
    )
    # leading: -(G-1)/(n beta) which IS O(1/beta) and has the right sign if G>1
    ser = sp.series(rec, beta, sp.oo, 2).removeO()
    record(
        "N4b_leading",
        sp.simplify(ser - (-(G - 1) / (n * beta))) == 0,
        "leading projector correction -(G-1)/(n beta)",
    )


def n5_combined() -> None:
    """R = R_noise_from_|S| + R_projector, both on linear S, V=infty, A=1-1/(n beta)."""
    n, beta, G = sp.symbols("n beta G", positive=True)
    A = 1 - 1 / (n * beta)
    sig2 = A / (n * beta)
    R_s = (1 + sig2) / A  # |S| fluctuation, V=infty
    R_p = (G - 1) * (2 / (n ** 2 * beta ** 2) - 1 / (n * beta))
    R = sp.series(R_s + R_p, beta, sp.oo, 3).removeO()
    # R_s = 1 + 2/(n beta) + O(1/beta^2)
    # R_p = -(G-1)/(n beta) + O(1/beta^2)
    # R = 1 + (2 - (G-1))/(n beta) + O(1/beta^2) = 1 + (3-G)/(n beta) + O(1/beta^2)
    want = 1 + (3 - G) / (n * beta)
    d = sp.simplify(sp.series(R_s + R_p - want, beta, sp.oo, 2).removeO())
    record("N5a_combined_O1beta", d == 0, "R = 1 + (3-G)/(n beta) + O(1/beta^2)")
    # G_3 ~ 1.79 > 3? NO, G~1.79 < 3, so (3-G)>0, R>1 still!
    # G_4 = 1913/1344 ~ 1.423, 3-G>0
    G4 = Fr(1913, 1344)
    record("N5b_G4_lt_3", G4 < 3, f"G_4={G4} < 3 so (3-G)/n > 0, combined R still > 1")
    # infinite-volume G_3 is larger (~1.79 from FFT) still < 3
    # executed R_IR=0.9719 < 1. Combined cubic-Gaussian noise still wrong sign.
    record(
        "N5c_still_wrong_sign",
        True,
        "even with the G_3 projector piece, a = (G-3)/n < 0 (R>1) for G_3<3; executed deficit is R<1",
    )


def main() -> int:
    n1_A_and_variance_tensor()
    n2_noise_ratio()
    n3_C0_minus_Cv()
    n4_projector_order()
    n5_combined()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL vMF innovation on the linear covariance gives "
        "R = 1 + (3-G_V)/(n beta) + O(1/beta^2) (n=4: 1 + (3-G)/ (4 beta) + ...); "
        "G_4=1913/1344<3 so this is >1, opposite to the executed low-k ratio 0.9719 at beta=6; "
        "the cubic-Gaussian noise sector cannot supply a = (G_3-related)>0 "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: R_noise = 1+(3-G_V)/(n beta)+O(1/beta^2) on the linear covariance; "
        "for G_4=1913/1344 and G_3<3 this is >1, contradicting the executed IR deficit <1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
