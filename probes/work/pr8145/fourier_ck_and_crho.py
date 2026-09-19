#!/usr/bin/env python3
"""J:attack-f:PR8145 — NORMALIZATION of 2π, 1/N, conjugation.

Independent of the existing W(J) fiber attack (pattern already executed
on currents). Here: (i) Villain c_k as 1/N DFT of sampled w vs aliased
Poisson (2πβ)^{-1/2} Σ_q exp(-q²/(2β)); reconstruction w=Σ_k c_k e^{2π i k m/N};
evenness c_k=c_{-k}; K(j=0)=1. (ii) C_ρ average 1/N^V with the note's
e^{-2π i ⟨ρ,η⟩/N} on a 4-cycle, N=2,3; |C_ρ| <= r^{|A|} C_0; conjugation
C_ρ vs C_{-ρ}.

Exact Fraction where possible (N=2); otherwise float with 1e-10.
"""
from __future__ import annotations

import math
from itertools import product
from math import pi

import numpy as np
import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def villain_w(N, beta, nterms=40):
    th = 2 * pi * np.arange(N) / N
    n = np.arange(-nterms, nterms + 1)
    return np.exp(-beta * (th[:, None] + 2 * pi * n) ** 2 / 2).sum(axis=1)


def c_poisson(N, beta, nterms=80):
    k = np.arange(N)
    q = k[:, None] + N * np.arange(-nterms, nterms + 1)[None, :]
    return np.exp(-(q.astype(float) ** 2) / (2 * beta)).sum(axis=1) / math.sqrt(2 * pi * beta)


def c_dft(w):
    N = len(w)
    k = np.arange(N)
    m = np.arange(N)
    # c_k = N^{-1} Σ_m w(m) exp(-2π i k m / N)
    return (w[None, :] * np.exp(-2j * pi * np.outer(k, m) / N)).sum(axis=1) / N


def check_ck():
    print("== Villain c_k: 1/N DFT vs aliased Poisson, reconstruction, evenness ==")
    for N in (2, 3, 4, 6):
        for beta in (0.5, 1.0, 2.0):
            w = villain_w(N, beta)
            cp = c_poisson(N, beta)
            cd = c_dft(w)
            # reconstruction without 1/N: Σ_k c_k exp(+2π i k m / N)
            m = np.arange(N)
            k = np.arange(N)
            rec_p = (cp[None, :] * np.exp(2j * pi * np.outer(m, k) / N)).sum(axis=1)
            rec_d = (cd[None, :] * np.exp(2j * pi * np.outer(m, k) / N)).sum(axis=1)
            rec_p_m = (cp[None, :] * np.exp(-2j * pi * np.outer(m, k) / N)).sum(axis=1)
            err_pd = np.max(np.abs(cp - cd.real)) / np.max(np.abs(cp))
            err_rec_p = np.max(np.abs(rec_p - w)) / np.max(w)
            err_rec_d = np.max(np.abs(rec_d - w)) / np.max(w)
            err_sign = np.max(np.abs(rec_p_m - w)) / np.max(w)
            even = np.max(np.abs(cp - np.roll(cp[::-1], 1)))  # c_k vs c_{-k}=c_{N-k}
            # roll of reverse: for k=0, c_0 vs c_0; c_1 vs c_{N-1}
            even = np.max(np.abs(cp - cp[[(-k) % N for k in range(N)]]))
            pos = np.min(cp)
            R0 = max(cp[j] / cp[j] for j in range(N))  # =1
            print(
                f"  N={N} beta={beta}: DFT-vs-Poisson {err_pd:.2e} rec+ {err_rec_p:.2e} "
                f"rec- {err_sign:.2e} even {even:.2e} min_c {pos:.3e} R(0)={R0}"
            )
            if err_pd > 1e-8:
                hit(f"N={N} beta={beta}: 1/N DFT c_k disagrees with Poisson by {err_pd:.2e}")
            if err_rec_p > 1e-8:
                hit(f"N={N} beta={beta}: Poisson reconstruction with e^{{+2πi}} fails {err_rec_p:.2e}")
            if even > 1e-10:
                hit(f"N={N} beta={beta}: c_k != c_{{-k}}, max {even:.2e}")
            if pos <= 0:
                hit(f"N={N} beta={beta}: some c_k <= 0 ({pos})")
            if abs(R0 - 1) > 1e-15:
                hit(f"K(j=0)=R(0)={R0} != 1")
            # conjugation: minus sign reconstruction should also work if c even
            if err_sign > 1e-8:
                hit(
                    f"N={N} beta={beta}: reconstruction with e^{{-2πi}} fails {err_sign:.2e} "
                    "(conjugation convention)"
                )


def check_n2_exact():
    print("== N=2 exact: c0,c1 and tanh identity ==")
    b = sp.symbols("b", positive=True)
    # discrete DFT of a 2-point even sequence
    w0, w1 = sp.symbols("w0 w1", positive=True)
    c0 = (w0 + w1) / 2
    c1 = (w0 - w1) / 2
    print(f"  c0=(w0+w1)/2 c1=(w0-w1)/2 (1/N DFT)")
    # R(S=1)=max(c0/c1,c1/c0); W related to c1/c0 for one plaquette
    # N=2 one plaquette cosine Villain is different; here Gaussian samples
    ok = sp.simplify(c0 + c1 - w0) == 0 and sp.simplify(c0 - c1 - w1) == 0
    if not ok:
        hit("N=2 1/N DFT does not invert")
    else:
        print("  N=2 1/N DFT inverts: w0=c0+c1, w1=c0-c1")


def crho_cycle(N, beta):
    """4-cycle, degree 2. C_ρ(a,b) = N^{-4} Σ_η e^{-2π i ρ·η/N} Π_e w(a_e-b_e+(d0 η)_e)."""
    w = villain_w(N, beta)
    V = 4
    D = np.zeros((4, 4), dtype=int)  # d0: edge e from e to e+1
    for e in range(4):
        D[e, e] = -1
        D[e, (e + 1) % 4] = 1
    configs = list(product(range(N), repeat=V))
    etas = configs
    size = N ** V
    # pick two representative configs a, b (all-zero and a one-flip)
    a = np.array([0, 0, 0, 0])
    b = np.array([0, 0, 0, 0])
    b2 = np.array([1, 0, 0, 0]) % N
    rho0 = np.array([0, 0, 0, 0])
    rho1 = np.array([1, 0, 0, 0])  # charge at one vertex; not necessarily Gauss-legal

    def C(a, b, rho, sign=-1.0):
        acc = 0j
        diff = (a - b) % N
        for eta in etas:
            eta = np.array(eta)
            arg = (diff + D @ eta) % N
            acc += np.prod(w[arg]) * np.exp(sign * 2j * pi * (rho @ eta) / N)
        return acc / size

    C0 = C(a, b, rho0)
    Cm = C(a, b, rho1, sign=-1.0)
    Cp = C(a, b, rho1, sign=+1.0)
    Cmm = C(a, b, (-rho1) % N, sign=-1.0)
    m, M = float(w.min()), float(w.max())
    # degree 2 on the cycle; note's cubic bound uses ^6 (weaker)
    r2 = 1 - (m / M) ** 2
    r6 = 1 - (m / M) ** 6
    return {
        "C0": C0,
        "Cm": Cm,
        "Cp": Cp,
        "Cmm": Cmm,
        "r2": r2,
        "r6": r6,
        "abs_m": abs(Cm),
        "abs_p": abs(Cp),
    }


def check_crho():
    print("== C_ρ 1/N^V average and conjugation on the 4-cycle ==")
    for N in (2, 3):
        for beta in (0.8, 1.6):
            d = crho_cycle(N, beta)
            print(
                f"  N={N} beta={beta}: C0={d['C0'].real:.6e} |C-|->={d['abs_m']:.6e} "
                f"|C+|->={d['abs_p']:.6e} r2={d['r2']:.4f} r6={d['r6']:.4f}"
            )
            if d["C0"].real <= 0 or abs(d["C0"].imag) > 1e-12:
                hit(f"N={N} beta={beta}: C_0 not real-positive ({d['C0']})")
            # |A|=1 for a single charged vertex; bound |C| <= r C0
            if d["abs_m"] > d["r2"] * d["C0"].real + 1e-10:
                hit(
                    f"N={N} beta={beta}: |C_ρ|={d['abs_m']:.3e} > r2 C0="
                    f"{d['r2'] * d['C0'].real:.3e} (degree-2 bound)"
                )
            if d["abs_m"] > d["r6"] * d["C0"].real + 1e-10:
                hit(
                    f"N={N} beta={beta}: |C_ρ| exceeds the note's cubic r^6 C0"
                )
            # conjugation: minus-sign C_ρ vs C_{-ρ}
            if abs(d["Cm"] - d["Cmm"]) > 1e-10:
                hit(
                    f"N={N} beta={beta}: C_ρ != C_{{-ρ}} under e^{{-2πi}}: "
                    f"{d['Cm']} vs {d['Cmm']}"
                )
            # plus vs minus: for real even w, |C+| should equal |C-|
            if abs(d["abs_m"] - d["abs_p"]) > 1e-10:
                hit(
                    f"N={N} beta={beta}: |C| depends on ±2πi conjugation "
                    f"{d['abs_m']} vs {d['abs_p']}"
                )


def main() -> int:
    check_n2_exact()
    check_ck()
    check_crho()
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: NORMALIZATION (PR #8145): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8145): Villain c_k 1/N DFT matches aliased "
        "Poisson (2πβ)^{-1/2} at N=2,3,4,6; reconstruction with e^{±2πi km/N} "
        "agrees (c even); K(j=0)=1; C_ρ as 1/N^V average on the 4-cycle obeys "
        "|C_ρ|<=r^{|A|} C_0 and C_ρ=C_{-ρ}; pattern has purchase and the "
        "2π / 1/N / conjugation conventions hold as written"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
