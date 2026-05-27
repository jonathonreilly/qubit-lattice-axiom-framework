#!/usr/bin/env python3
"""Bounded Omega_Lambda arithmetic cascade over declared inputs.

The runner proves only finite arithmetic over declared premises:
Omega_b, R = Omega_DM/Omega_b, and Omega_total = 1. It also verifies the exact
R_base = 31/9 group-theory support identity. It does not derive BBN, flatness,
Sommerfeld continuation, or a DM relic map.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

NOTE = Path(__file__).resolve().parents[1] / "docs/OMEGA_LAMBDA_DERIVATION_NOTE.md"

PASS = 0
FAIL = 0
TOL = 1.0e-12


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def main() -> int:
    print("Omega_Lambda bounded arithmetic cascade")

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "bounded conditional arithmetic cascade",
        "Omega_b = 0.0492",
        "R = Omega_DM / Omega_b = 5.38",
        "Omega_total = 1",
        "No derivation of `Omega_b`",
        "No derivation of flatness",
        "No audit verdict and no direct ledger retag.",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    c_su3 = Fraction(4, 3)
    dim_su3_adj = Fraction(8, 1)
    c_su2 = Fraction(3, 4)
    dim_su2_adj = Fraction(3, 1)
    hypercharge_norm = Fraction(3, 5)
    r_base = hypercharge_norm * ((c_su3 * dim_su3_adj + c_su2 * dim_su2_adj) / (c_su2 * dim_su2_adj))
    check("R_base exact identity equals 31/9", r_base == Fraction(31, 9), str(r_base))

    omega_b = 0.0492
    ratio_r = 5.38
    omega_total = 1.0
    omega_dm = ratio_r * omega_b
    omega_m = omega_b + omega_dm
    omega_lambda = omega_total - omega_m
    sommerfeld_multiplier = ratio_r / float(r_base)

    check("Omega_b declared positive", omega_b > 0.0, f"Omega_b={omega_b:.6f}")
    check("R declared positive", ratio_r > 0.0, f"R={ratio_r:.6f}")
    check("Omega_total declared flat", abs(omega_total - 1.0) < TOL)
    check("Omega_DM = R * Omega_b", abs(omega_dm - 0.264696) < TOL, f"Omega_DM={omega_dm:.6f}")
    check("Omega_m = Omega_b + Omega_DM", abs(omega_m - 0.313896) < TOL, f"Omega_m={omega_m:.6f}")
    check("Omega_Lambda = Omega_total - Omega_m", abs(omega_lambda - 0.686104) < TOL, f"Omega_Lambda={omega_lambda:.6f}")
    check("rounded Omega_Lambda equals 0.686", round(omega_lambda, 3) == 0.686)
    check(
        "Sommerfeld multiplier is recorded, not derived",
        abs(sommerfeld_multiplier - 1.5619354838709678) < TOL,
        f"S={sommerfeld_multiplier:.12f}",
    )

    print()
    print("Omega_Lambda arithmetic cascade:", "PASS" if FAIL == 0 else "FAIL")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
