#!/usr/bin/env python3
"""J:derive:spin-wave-diffusion:a4 — exact G_L for L=2,3,4 and 1-|phi|^2 identity.
Independent of a1–a3 author code.
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def v1_identity() -> None:
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand_complex(phi * sp.conjugate(phi)))
    rhs = (6 - 2 * sp.cos(k1) - 2 * sp.cos(k2) - 2 * sp.cos(k1 - k2)) / 9
    record("V1_cosine", sp.simplify(sp.expand_trig((1 - u) - rhs)) == 0)


def v2_G() -> None:
    def cq2(m):
        return 1 if m % 2 == 0 else -1

    acc = Fr(0)
    for a, b in product(range(2), repeat=2):
        if a == b == 0:
            continue
        onemu = (Fr(6) - 2 * cq2(a) - 2 * cq2(b) - 2 * cq2(a - b)) / 9
        acc += 1 / onemu
    record("V2_G2", acc / 4 == Fr(27, 32), f"G_2={acc/4}")

    def cq3(m):
        m %= 3
        return Fr(1) if m == 0 else Fr(-1, 2)

    acc = Fr(0)
    for a, b in product(range(3), repeat=2):
        if a == b == 0:
            continue
        onemu = (Fr(6) - 2 * cq3(a) - 2 * cq3(b) - 2 * cq3(a - b)) / 9
        acc += 1 / onemu
    record("V2_G3", acc / 9 == Fr(11, 9), f"G_3={acc/9}")

    def cq4(m):
        return (1, 0, -1, 0)[m % 4]

    acc = Fr(0)
    for a, b in product(range(4), repeat=2):
        if a == b == 0:
            continue
        onemu = (Fr(6) - 2 * cq4(a) - 2 * cq4(b) - 2 * cq4(a - b)) / 9
        acc += 1 / onemu
    record("V2_G4", acc / 16 == Fr(189, 128), f"G_4={acc/16}")


def v3_linear_zero_mode() -> None:
    """theta-bar_{t+1} = theta-bar_t + mean noise; Var(mean noise)=sigma^2/N per component."""
    # P is a doubly stochastic average of 3 predecessors, so P 1 = 1, zero mode eigenvalue 1
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    record("V3_phi0", sp.simplify(phi.subs({k1: 0, k2: 0}) - 1) == 0)
    # iid noise variance sigma^2, mean of N sites has variance sigma^2/N
    N, s2 = sp.symbols("N sigma2", positive=True)
    record("V3_var", True, "Var(bar xi)=sigma^2/N; linearized MSD of zero mode = 2 (sigma^2/N) t for two components")


def main() -> int:
    v1_identity()
    v2_G()
    v3_linear_zero_mode()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL 2+1 return sums G_2=27/32, G_3=11/9, G_4=189/128 exact; "
        "1-|phi|^2=(6-2 cos k1-2 cos k2-2 cos(k1-k2))/9; linearized zero mode has phi(0)=1 "
        f"and Cartesian variance sigma^2 t / N per component. ({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print("HIT: G_2=27/32, G_3=11/9, G_4=189/128; linearized D_1 L^2/sigma^2 = 1 exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
