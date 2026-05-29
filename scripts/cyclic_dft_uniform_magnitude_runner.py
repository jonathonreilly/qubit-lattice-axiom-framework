#!/usr/bin/env python3
"""Bounded checker for normalized cyclic DFT uniform magnitudes."""

from __future__ import annotations

import cmath
import math

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    PASS += int(condition)
    FAIL += int(not condition)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def dft_entry(N: int, j: int, k: int) -> complex:
    omega = cmath.exp(2j * math.pi / N)
    return omega ** (j * k) / math.sqrt(N)


def main() -> int:
    print("=" * 72)
    print("CYCLIC DFT UNIFORM MAGNITUDE -- BOUNDED CHECK")
    print("=" * 72)

    for N in [2, 3, 4, 5, 6, 7, 12]:
        target = 1.0 / N
        ok_all = True
        for j in range(N):
            for k in range(N):
                mag_sq = abs(dft_entry(N, j, k)) ** 2
                if abs(mag_sq - target) > 1e-12:
                    ok_all = False
        check(
            f"all normalized Z_{N} DFT entries have |F_N[j,k]|^2 = 1/{N}",
            ok_all,
            f"{N*N} entries checked",
        )

    for N in [3, 4, 5]:
        omega = cmath.exp(2j * math.pi / N)
        orthogonal = True
        for a in range(N):
            for b in range(N):
                inner = sum((omega ** (a * g)).conjugate() * (omega ** (b * g)) for g in range(N)) / N
                expected = 1.0 if a == b else 0.0
                if abs(inner - expected) > 1e-12:
                    orthogonal = False
        check(f"Z_{N} character orthogonality holds", orthogonal)

    N = 3
    target = 1.0 / N
    for j in range(N):
        for k in range(N):
            mag_sq = abs(dft_entry(N, j, k)) ** 2
            check(
                f"Z_3 entry ({j},{k}) has magnitude squared 1/3",
                abs(mag_sq - target) < 1e-12,
                f"value={mag_sq:.12f}",
            )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: cyclic DFT uniform magnitude theorem FAILED.")
        return 1
    print("VERDICT: cyclic DFT uniform magnitude theorem holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
