#!/usr/bin/env python3
"""Exact bounded-scope runner for the EW current OZI support row.

This runner verifies the repaired row's binding content:

  F_adj = (N_c^2 - 1) / N_c^2,
  F_singlet = 1 / N_c^2,
  K_EW(kappa) = 1 / (F_adj + kappa F_singlet),

and confirms that bounded kappa supplies an O(1/N_c^2) disconnected size
class without selecting kappa = 0.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


NOTE = Path("docs/EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md")


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"[{status}] {label}{suffix}")

    def summary(self) -> int:
        print(f"SUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        return 0 if self.fail_count == 0 else 1


def f_adj(nc: int) -> Fraction:
    return Fraction(nc * nc - 1, nc * nc)


def f_singlet(nc: int) -> Fraction:
    return Fraction(1, nc * nc)


def k_ew(nc: int, kappa: Fraction) -> Fraction:
    return 1 / (f_adj(nc) + kappa * f_singlet(nc))


def main() -> int:
    gate = Gate()

    print("EW current OZI scope repair certificate")
    print("=" * 72)

    for nc in range(2, 8):
        c = f_adj(nc)
        s = f_singlet(nc)
        gate.check(
            f"N_c={nc}: channel fractions sum to one",
            c + s == 1,
            f"C={c}, S={s}",
        )
        gate.check(
            f"N_c={nc}: disconnected/connected size is 1/(N_c^2-1)",
            s / c == Fraction(1, nc * nc - 1),
            f"S/C={s / c}",
        )

    gate.check("N_c=3 connected fraction is 8/9", f_adj(3) == Fraction(8, 9))
    gate.check("N_c=3 singlet fraction is 1/9", f_singlet(3) == Fraction(1, 9))
    gate.check("kappa=0 gives K_EW=9/8", k_ew(3, Fraction(0)) == Fraction(9, 8))
    gate.check("kappa=1 gives K_EW=1", k_ew(3, Fraction(1)) == Fraction(1, 1))
    gate.check(
        "two completions share Fierz/OZI premises but differ in K_EW",
        f_adj(3) == Fraction(8, 9)
        and f_singlet(3) == Fraction(1, 9)
        and k_ew(3, Fraction(0)) != k_ew(3, Fraction(1)),
        f"K0={k_ew(3, Fraction(0))}, K1={k_ew(3, Fraction(1))}",
    )

    for kappa in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
        ratio = kappa * f_singlet(3) / f_adj(3)
        gate.check(
            f"bounded kappa={kappa} remains in O(1/N_c^2) size class",
            ratio == kappa / 8,
            f"kappa*S/C={ratio}",
        )

    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does not derive the physical EW connected-trace selector",
        "does not derive an unconditional exact `9/8` EW matching coefficient",
        "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md",
        "K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)",
    ]
    for needle in required:
        gate.check(f"source note contains required firewall: {needle}", needle in text)

    forbidden = [
        "this theorem unblocks",
        "physical (continuum-matched) EW vacuum polarization equals the connected",
        "continuum readout therefore picks up only",
        "addresses the matching-rule gap",
        "standard 1/N_c expansion surface",
    ]
    lowered = text.lower()
    for needle in forbidden:
        gate.check(f"source note omits old overclaim: {needle}", needle.lower() not in lowered)

    return gate.summary()


if __name__ == "__main__":
    raise SystemExit(main())
