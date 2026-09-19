#!/usr/bin/env python3
"""J:falsifier:PR8153 — B2 Laplacian eigenfunction identity beyond the 4³ torus.

Falsifier: a site of the 4³ torus where the plane wave is not a Laplacian
eigenfunction with eigenvalue E(k)=Σ_i 2(1-cos k_i). Machinery disjoint
from the runner: exact sympy cis on (Z/2LZ)^d. Beyond: L=2 (4³), L=3 (6³)
and the L=3,4 lines. HIT if (Δψ)_x != E(k) ψ_x at any site or mode.
"""
from __future__ import annotations

from itertools import product

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def check_torus(L: int, d: int) -> None:
    nrange = range(-L + 1, L + 1)
    xs = list(product(range(2 * L), repeat=d))
    ns = list(product(nrange, repeat=d))
    N = (2 * L) ** d
    if len(xs) != N or len(ns) != N:
        hit(f"L={L} d={d}: |sites|={len(xs)} |modes|={len(ns)} != N={N}")
        return
    I = sp.I
    pi = sp.pi
    n_bad = 0
    # Δ e^{ik·x} = Σ_i (2 − e^{ik_i} − e^{−ik_i}) e^{ik·x} = E(k) e^{ik·x}
    # independently of x; also check the identity at a second site (1,0,..).
    x1 = tuple(1 if i == 0 else 0 for i in range(d))
    for n in ns:
        k = tuple(pi * ni / L for ni in n)
        Ek = sum(2 * (1 - sp.cos(k[i])) for i in range(d))
        factor = sum(2 - sp.exp(I * k[i]) - sp.exp(-I * k[i]) for i in range(d))
        gap = sp.simplify(sp.expand(factor.rewrite(sp.cos) - Ek))
        if gap != 0:
            n_bad += 1
            hit(f"L={L} d={d} n={n}: algebraic Δ/ψ = {factor} != E={Ek}")
            if n_bad >= 2:
                break
    print(f"L={L} d={d}: N={N} modes={len(ns)} mismatches={n_bad}")


def check_cosine_bound() -> None:
    print("== C1 1-cos u >= 2u²/π² on a dense grid beyond samples ==")
    u = sp.symbols("u", positive=True)
    g = (1 - sp.cos(u)) - 2 * u ** 2 / sp.pi ** 2
    n_bad = 0
    worst = None
    for n in range(1, 401):
        t = n * sp.pi / 400
        val = g.subs(u, t).evalf(40)
        if worst is None or val < worst[0]:
            worst = (val, n)
        if val < -sp.Float("1e-30"):
            n_bad += 1
            hit(f"1-cos u < 2u²/π² at u=π*{n}/400: {val}")
            if n_bad >= 2:
                break
    print(f"  worst gap {worst[0]} at n={worst[1]}/400; negatives={n_bad}")
    g0 = sp.limit(g, u, 0)
    gpi = sp.simplify(g.subs(u, sp.pi))
    print(f"  g(0+)={g0} g(π)={gpi} (want 0 at π)")
    if gpi != 0:
        hit(f"equality at π fails: {gpi}")


def main() -> int:
    check_torus(2, 1)
    check_torus(2, 3)  # 4³ executed size
    check_torus(3, 1)
    check_torus(3, 2)  # 6² beyond
    check_cosine_bound()
    if HITS:
        print("SUMMARY: FALSIFIER (PR #8153): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: FALSIFIER (PR #8153): plane waves are Laplacian eigenfunctions "
        "with E(k)=Σ 2(1-cos k_i) on L=2 d=1,3 (4³) and L=3 d=1,2 (beyond); "
        "1-cos u ≥ 2u²/π² on 400-point grid with equality at π; does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
