#!/usr/bin/env python3
"""Certificate for the EW color-projection kappa-family no-go repair."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NC = 3
G1_LATTICE = 0.43779
G2_LATTICE = 0.61090
KAPPAS = (Fraction(0, 1), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1))
COMMON_SCALES = (Fraction(1, 2), Fraction(4, 5), Fraction(13, 10))


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


class Checkbook:
    def __init__(self) -> None:
        self.checks: list[Check] = []

    def require(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append(Check(name, bool(ok), detail))

    @property
    def pass_count(self) -> int:
        return sum(1 for check in self.checks if check.ok)

    @property
    def fail_count(self) -> int:
        return sum(1 for check in self.checks if not check.ok)

    def report(self) -> None:
        print("CHECK SUMMARY")
        for check in self.checks:
            status = "PASS" if check.ok else "FAIL"
            print(f"  {status:4s} {check.name}: {check.detail}")


def f_adj(n: int = NC) -> Fraction:
    return Fraction(n * n - 1, n * n)


def k_ew(kappa: Fraction, n: int = NC) -> Fraction:
    f = f_adj(n)
    return Fraction(1, 1) / (f + kappa * (1 - f))


def sin2(g1: float, g2: float) -> float:
    return (g1 * g1) / (g1 * g1 + g2 * g2)


def cmt_scaled_k(kappa: Fraction, scale: Fraction) -> Fraction:
    f = f_adj()
    c = f * scale * scale
    s = (1 - f) * scale * scale
    total = c + s
    return total / (c + kappa * s)


def run_family_checks(checks: Checkbook) -> None:
    f = f_adj()
    k0 = k_ew(Fraction(0, 1))
    k_half = k_ew(Fraction(1, 2))
    k1 = k_ew(Fraction(1, 1))
    print("EW KAPPA-FAMILY PACKET")
    print(f"  F_adj={f}, K(0)={k0}, K(1/2)={k_half}, K(1)={k1}")

    checks.require("exact F_adj at Nc=3", f == Fraction(8, 9), f"F_adj={f}")
    checks.require("connected selector value", k0 == Fraction(9, 8), f"K(0)={k0}")
    checks.require("half selector value", k_half == Fraction(18, 17), f"K(1/2)={k_half}")
    checks.require("full-trace selector value", k1 == Fraction(1, 1), f"K(1)={k1}")
    checks.require("selector values differ", k0 > k_half > k1, f"{k0} > {k_half} > {k1}")
    checks.require(
        "two-completion no-go witness",
        k0 != k1,
        "kappa=0 and kappa=1 share F_adj but produce different K_EW",
    )

    base_sin2 = sin2(G1_LATTICE, G2_LATTICE)
    base_ratio = G1_LATTICE / G2_LATTICE

    for kappa in KAPPAS:
        k_val = k_ew(kappa)
        direct = Fraction(1, 1) / (Fraction(8, 9) + kappa * Fraction(1, 9))
        scale = math.sqrt(float(k_val))
        g1_scaled = G1_LATTICE * scale
        g2_scaled = G2_LATTICE * scale
        scaled_sin2 = sin2(g1_scaled, g2_scaled)
        scaled_ratio = g1_scaled / g2_scaled

        checks.require(
            f"kappa-family identity kappa={kappa}",
            k_val == direct,
            f"K={k_val}",
        )
        checks.require(
            f"weak-angle preservation kappa={kappa}",
            math.isclose(scaled_sin2, base_sin2, rel_tol=0.0, abs_tol=1e-15),
            f"sin2={scaled_sin2:.15f}",
        )
        checks.require(
            f"coupling-ratio preservation kappa={kappa}",
            math.isclose(scaled_ratio, base_ratio, rel_tol=0.0, abs_tol=1e-15),
            f"g1/g2={scaled_ratio:.15f}",
        )

    for kappa in (Fraction(0, 1), Fraction(1, 2), Fraction(1, 1)):
        values = [cmt_scaled_k(kappa, scale) for scale in COMMON_SCALES]
        checks.require(
            f"CMT common-scale invariance kappa={kappa}",
            all(value == values[0] for value in values),
            f"values={values}",
        )


def run_note_checks(checks: Checkbook) -> None:
    note_path = os.path.join(ROOT, "docs", "YT_EW_COLOR_PROJECTION_THEOREM.md")
    with open(note_path, "r", encoding="utf-8") as handle:
        text = handle.read()

    checks.require("note declares no_go", "**Claim type:** no_go" in text, "claim type marker present")
    checks.require("note names runner", "scripts/yt_ew_kappa_family_nogo_certificate.py" in text, "runner path present")
    checks.require("note names kappa_EW", "kappa_EW" in text, "free readout coefficient present")
    checks.require("note states no new axiom", "No new axiom" in text, "no-new-axiom sentence present")
    checks.require(
        "note keeps selector conditional",
        "does not claim that `kappa_EW = 0` is derived" in text,
        "selector disclaimer present",
    )


def execution_certificate(checks: Checkbook) -> None:
    """Print-only N5 execution certificate; appends no check, counts nothing."""
    family = {str(kappa): str(k_ew(kappa)) for kappa in KAPPAS}
    base = sin2(G1_LATTICE, G2_LATTICE)
    rescale_ok = all(
        math.isclose(
            sin2(G1_LATTICE * math.sqrt(float(k_ew(kappa))),
                 G2_LATTICE * math.sqrt(float(k_ew(kappa)))),
            base,
            rel_tol=0.0,
            abs_tol=1e-15,
        )
        for kappa in KAPPAS
    )
    print("N5 EXECUTION CERTIFICATE")
    print(
        f"per_element: checked and not executed — nothing matrix-valued is "
        f"instantiated in this certificate; F_adj = (N_c^2 - 1)/N_c^2 is "
        f"evaluated straight from N_c = {NC} as an exact Fraction, so there is "
        f"no operator whose individual entries could be resolved."
    )
    print(
        f"per_site: checked and not executed — the readout coefficient family "
        f"is a global matching statement with no positional content at all: no "
        f"coordinate, neighbour or extent is defined, so the question of what "
        f"happens at a given site does not arise here."
    )
    print(
        f"per_mode: checked and not executed — no eigenvalue problem, momentum "
        f"variable or normal-mode expansion occurs; g_1 and g_2 are two fixed "
        f"scalar couplings, not modes, so this runner decides nothing at mode "
        f"granularity."
    )
    print(
        f"per_block: the adjoint and singlet colour blocks carry everything "
        f"this runner resolves, in exact rational arithmetic — with "
        f"F_adj = {f_adj()} the selector family "
        f"K_EW(kappa) = 1 / (F_adj + kappa (1 - F_adj)) takes the values "
        f"{family} at kappa = 0, 1/2, 1, 2, and each of those stays invariant "
        f"under the common CMT rescalings {[str(s) for s in COMMON_SCALES]}, "
        f"so the block weights fix the family but never the selector."
    )
    print(
        f"lattice_wide: checked and not executed — the lattice appears only as "
        f"the two scalar anchors g_1 = {G1_LATTICE} and g_2 = {G2_LATTICE} "
        f"taken as given, with no volume, spacing or configuration built "
        f"anywhere; the weak-angle result is the algebraic fact that a common "
        f"rescaling cancels in sin^2 theta_W and in g_1/g_2 for every kappa in "
        f"the family, verified at abs tol 1e-15 ({rescale_ok})."
    )


def main() -> None:
    checks = Checkbook()
    print("=" * 92)
    print("EW COLOR PROJECTION KAPPA-FAMILY NO-GO CERTIFICATE")
    print("  exact K_EW(kappa_EW) algebra; no selector derivation")
    print("=" * 92)
    run_family_checks(checks)
    run_note_checks(checks)

    print()
    print("FINITE READ")
    print("  F_adj=8/9 is exact algebraic support.")
    print("  K_EW=9/8 is only the kappa_EW=0 specialization.")
    print("  Weak-angle preservation holds for any fixed kappa_EW.")
    print("  The current packet does not derive kappa_EW=0.")
    print()
    checks.report()
    print()
    execution_certificate(checks)
    print()
    print(f"RUNNER STATUS: {'PASS' if checks.fail_count == 0 else 'FAIL'} (PASS={checks.pass_count} FAIL={checks.fail_count})")
    if checks.fail_count:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
