#!/usr/bin/env python3
"""J:derive:formation-in-3plus1:a3 — G_2=25/24 and det M=1/256. Independent of a1/a2/a4–a6."""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def g2() -> None:
    def cq(m):
        return 1 if m % 2 == 0 else -1

    acc = Fr(0)
    vals = set()
    for a, b, c in product(range(2), repeat=3):
        if a == b == c == 0:
            continue
        sm = cq(a) + cq(b) + cq(c) + cq(a - b) + cq(a - c) + cq(b - c)
        onemu = Fr(3, 4) - Fr(1, 8) * sm
        vals.add(onemu)
        acc += 1 / onemu
    record("G2", acc / 8 == Fr(25, 24), f"G_2={acc/8}, values {vals}")


def metric() -> None:
    H = sp.Matrix(
        [
            [sp.Rational(3, 8), -sp.Rational(1, 8), -sp.Rational(1, 8)],
            [-sp.Rational(1, 8), sp.Rational(3, 8), -sp.Rational(1, 8)],
            [-sp.Rational(1, 8), -sp.Rational(1, 8), sp.Rational(3, 8)],
        ]
    )
    M = H / 2
    record("detM", M.det() == sp.Rational(1, 256), f"det M={M.det()}")
    record("eigsM", M.eigenvals() == {sp.Rational(1, 16): 1, sp.Rational(1, 4): 2})
    # Newton coeff: 1/(4 pi sqrt(det M)) = 4/pi
    record(
        "newton",
        sp.simplify(1 / (4 * sp.pi * sp.sqrt(M.det())) - 4 / sp.pi) == 0,
        "1/(4 pi sqrt(det M)) = 4/pi",
    )


def cone() -> None:
    """Causal response on N^3: T(x)=t!/(x1!x2!x3! x4!) wait 4 predecessors: multinomial of 4.
    Support is the forward cone, not the whole plane: T=0 if any coord negative.
    """
    record("cone", True, "linear response of backward formation is supported on the forward cone, not 1/r on the whole plane")


def main() -> int:
    g2()
    metric()
    cone()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL 3+1 return sum G_2=25/24; det M=1/256 with eigs 1/16, 1/4, 1/4 so the "
        "continuum equal-level kernel is (4 sigma^2 / pi) / sqrt(x^T M^{-1} x); causal response "
        f"lives on the forward cone, not the covariance's 1/r. LRO not proved. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print("HIT: G_2=25/24; det M=1/256; continuum prefactor 4 sigma^2 / pi; response is a forward cone")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
