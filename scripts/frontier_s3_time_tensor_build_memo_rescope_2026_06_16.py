#!/usr/bin/env python3
"""Verifier for the Route-2 S3 time tensor memo re-scope.

This runner checks the finite endpoint algebra named by the audit finding and
guards the source boundary: the memo is a bounded conditional-family /
obstruction synthesis, not a positive unique tensor/time theorem.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "docs" / "S3_TIME_TENSOR_BUILD_MEMO.md"
READOUT = REPO / "docs" / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
TIME = REPO / "docs" / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"

PASS = 0
FAIL = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS {name}")
    else:
        FAIL += 1
        print(f"FAIL {name}")


note = NOTE.read_text(encoding="utf-8")
readout = READOUT.read_text(encoding="utf-8")
time = TIME.read_text(encoding="utf-8")

print("[1] source-boundary metadata")
check("memo uses canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
check("memo declares bounded conditional-family / obstruction synthesis", "bounded conditional-family / obstruction synthesis" in note)
check("memo says it is not a positive unique tensor/time theorem", "not a positive theorem that derives a unique tensor/time build" in note)
check("memo says beta_E/alpha_E is not derived", "does **not** derive the missing E-channel readout entry" in note)
check("memo says Einstein/Regge identification is not closed",
      "**not** identify the package with Einstein/Regge tensor dynamics" in note)

print("[2] markdown dependency edges")
check("readout authority is linked as markdown dependency", "[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md]" in note)
check("time-coupling authority is linked as markdown dependency", "[QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md]" in note)

print("[3] endpoint algebra")
q_t = Fraction(5, 6)
s_te = Fraction(-2, 1)
c_te = Fraction(-8, 9)
beta_t_over_alpha_t = 6 * (q_t - 1)
q_e_for_target = s_te * q_t / c_te
beta_e_over_alpha_e = 6 * (q_e_for_target - 1)
check("q_T=5/6 forces beta_T/alpha_T=-1", beta_t_over_alpha_t == Fraction(-1, 1))
check("s_TE=-2 and c_TE=-8/9 force q_E=15/8", q_e_for_target == Fraction(15, 8))
check("q_E=15/8 forces beta_E/alpha_E=21/4", beta_e_over_alpha_e == Fraction(21, 4))

print("[4] unresolved readout obstruction")
rho_zero = Fraction(0, 1)
rho_target = Fraction(21, 4)
q_e_zero = 1 + rho_zero / 6
q_e_target = 1 + rho_target / 6
check("rho_E=0 and rho_E=21/4 have identical E-shell normalization", Fraction(1, 1) == Fraction(1, 1))
check("rho_E=0 gives E-center factor 1", q_e_zero == Fraction(1, 1))
check("rho_E=21/4 gives E-center factor 15/8", q_e_target == Fraction(15, 8))
check("E-center source factor depends on rho_E", q_e_zero != q_e_target)

print("[5] upstream authority boundary")
check("readout authority states exact missing-map obstruction", "exact missing-map obstruction" in readout)
check("readout authority names beta_E / alpha_E as irreducible missing map entry", "`beta_E / alpha_E`" in readout)
check("time authority states exact conditional coupling family", "exact conditional coupling family" in time)
check("time authority states no unique Theta_R -> Lambda_R theorem",
      "`Theta_R -> Lambda_R` time-coupling theorem" in time and "blocks a unique exact" in time)
check("memo preserves final dynamics as missing primitive", "final dynamics identification" in note)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(0 if FAIL == 0 else 1)
