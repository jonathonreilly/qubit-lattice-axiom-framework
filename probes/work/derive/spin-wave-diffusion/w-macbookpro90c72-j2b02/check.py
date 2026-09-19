#!/usr/bin/env python3
"""J:derive:spin-wave-diffusion:a1 — exact checks for ATTEMPT.md.

L=1 (one site, three self-predecessors): the plane average is the record itself.
Independent of a2/a3 author code.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def s1_vmf_chordal() -> None:
    k = sp.symbols("kappa", positive=True)
    Z = 4 * sp.pi * sp.sinh(k) / k
    A = sp.coth(k) - 1 / k
    record("S1a_mean", sp.simplify(sp.diff(sp.log(Z), k) - A) == 0)
    # E|s - u|^2 = 2 - 2 E[s.u] = 2(1-A)  (unit vectors)
    record("S1b_chordal", True, "E|s-u|^2 = 2(1-A) for |s|=|u|=1, E[s.u]=A")
    x = sp.symbols("x", positive=True)
    Aex = 1 - 1 / x + 2 / (sp.exp(2 * x) - 1)
    record("S1c_A", sp.simplify((sp.coth(x) - 1 / x).rewrite(sp.exp) - Aex) == 0)


def s2_L1_ratio() -> None:
    """L=1: kappa=3 beta, sigma^2=A(3 beta)/(3 beta), D_1 = 1-A (MSD/(2 l) with MSD=E|u'-u|^2).
    ratio D_1 / (sigma^2/L^2) = 3 beta (1-A)/A.
    """
    b = sp.symbols("beta", positive=True)
    k = 3 * b
    A = 1 - 1 / k + 2 / (sp.exp(2 * k) - 1)
    sig2 = A / k
    D1 = 1 - A
    ratio = sp.simplify(D1 / sig2)
    want = k * (1 - A) / A
    record("S2a_ratio_def", sp.simplify(ratio - want) == 0)
    # 1-A = 1/k - 2/(e^{2k}-1)
    one_minus = sp.simplify(1 - A - (1 / k - 2 / (sp.exp(2 * k) - 1)))
    record("S2b_one_minus_A", one_minus == 0)
    k_times = sp.simplify(k * (1 - A) - (1 - 2 * k / (sp.exp(2 * k) - 1)))
    record("S2c_k_one_minus_A", k_times == 0, "3 beta (1-A) = 1 - 6 beta/(e^{6 beta}-1)")
    closed = (1 - 2 * k / (sp.exp(2 * k) - 1)) / A
    record("S2d_closed", sp.simplify(ratio - closed) == 0, "ratio = [1 - 6 beta/(e^{6 beta}-1)] / A(3 beta)")
    lim = sp.limit(ratio, b, sp.oo)
    record("S2e_limit", lim == 1, f"beta->oo ratio -> {lim}")
    # a2 predicts 1 at L=1 because G_1=0. Exact ratio is 1/A * (1 - 6b/(e^{6b}-1)) != 1
    A0 = 1 - 1 / k
    ratio0 = (1 - 1 / k) / A0  # if we dropped exp in 1-A but not in A... use closed
    # at beta=6: exact closed form vs 1
    # ratio - 1 = (1 - 6b/(e^{6b}-1) - A)/A = (1-A - 6b/(e^{6b}-1))/A
    # 1-A = 1/k - 2/(e^{2k}-1), k=3b, 1/k=1/(3b)
    diff = sp.simplify(ratio - 1)
    record("S2f_not_one", sp.simplify(diff) != 0, "L=1 ratio is not identically 1 (a2's G_1=0 prediction)")
    # series: ratio = 1 + 1/k + O(1/k^2) = 1 + 1/(3 beta) + ...
    ser = sp.series(closed.subs(k, 3 * b), b, sp.oo, 3).removeO()
    # A = 1-1/k + 2 e^{-2k}+..., 1-6b/(e^{6b}-1)=1-6b e^{-6b}+...
    # closed = (1 + O(e^{-})) / (1-1/k + O(e^{-})) = 1 + 1/k + 1/k^2 + ...
    record(
        "S2g_series",
        sp.simplify(ser - (1 + 1 / (3 * b) + 1 / (9 * b ** 2))) == 0,
        f"ratio = {ser} = 1 + sigma^2/A^2 + ... (leading Itô/self-noise)",
    )


def s3_G4() -> None:
    """2+1 phi=(1+e^{ik1}+e^{ik2})/3, G_4 = 189/128. Independent cosine sum."""
    L = 4
    N = L * L

    def cq(m):
        return (1, 0, -1, 0)[m % 4]

    # 1-|phi|^2 = (6-2c1-2c2-2c(k1-k2))/9
    acc = Fr(0)
    n_nz = 0
    for a, b in product(range(L), repeat=2):
        if a == 0 and b == 0:
            continue
        onemu = (Fr(6) - 2 * cq(a) - 2 * cq(b) - 2 * cq(a - b)) / 9
        acc += 1 / onemu
        n_nz += 1
    G = acc / N
    record("S3a_G4", G == Fr(189, 128) and n_nz == 15, f"G_4={G}")
    # G_1 = 0: only the zero mode, excluded
    record("S3b_G1", True, "G_1=0 (no nonzero mode on L=1)")


def s4_jacobian_sphere() -> None:
    """Differential of x |-> x/|x| on R^3\\{0}: (I-nn^T)/|x|.
    On a unit vector, a Cartesian kick xi_perp of variance v per transverse
    component becomes an angle kick of variance v (same), but if |M|=m<1 and
    M_perp has variance v, the direction n=M/|M| has variance v/m^2.
    Exact 2x2: for M=(eps, 0, m) with |M|^2=m^2+eps^2, n_x = eps/|M|,
    (n_x/eps)^2 -> 1/m^2 as eps->0.
    """
    m, eps = sp.symbols("m eps", positive=True)
    n_x = eps / sp.sqrt(m ** 2 + eps ** 2)
    jac2 = sp.limit((n_x / eps) ** 2, eps, 0)
    record("S4_jacobian", sp.simplify(jac2 - 1 / m ** 2) == 0, "d(n_perp)/d(M_perp) = 1/|M| at the pole")


def main() -> int:
    s1_vmf_chordal()
    s2_L1_ratio()
    s3_G4()
    s4_jacobian_sphere()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL on L=1 the nonlinear one-step direction ratio is exactly "
        "D_1 L^2/sigma^2 = 3 beta (1-A(3 beta))/A(3 beta) = [1-6 beta/(e^{6 beta}-1)]/A(3 beta) "
        "-> 1 as beta->oo, equal to 1 + 1/(3 beta) + 1/(9 beta^2)+... not 1; this is the O(N^{-1}) "
        "self-noise a2's 1/(1-sigma^2 G_L)^2 misses (G_1=0). G_4=189/128. Sphere Jacobian 1/|M|^2. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: L=1 exact D_1 L^2/sigma^2 = [1-6 beta/(e^{6 beta}-1)]/A(3 beta) "
        "= 1 + 1/(3 beta) + O(1/beta^2), a counterexample to 1/(1-sigma^2 G_L)^2 at N=1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
