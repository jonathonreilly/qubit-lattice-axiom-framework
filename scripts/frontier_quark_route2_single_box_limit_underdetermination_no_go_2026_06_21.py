#!/usr/bin/env python3
"""Single-box E-center calibration limit underdetermination no-go.

The measured Route-2 E-center lift at the 15^3 box is useful support, but a
single finite-box value cannot certify the exact infinite-volume limit.  This
runner constructs explicit finite-size laws that agree at N=15 and converge to
different exact q_E limits, one closing q_E=15/8 and one not.
"""

from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CACHE = ROOT / "logs" / "runner-cache" / "frontier_tensor_support_center_excess_law.txt"

PASS = 0
FAIL = 0

N0 = 15
TARGET_Q_E = Fraction(15, 8)
ALT_Q_E = Fraction(469, 250)  # 15/8 + 1/1000
TARGET_RHO_E = Fraction(21, 4)
ALT_RHO_E = Fraction(657, 125)
NOTE_PATH = DOCS / "QUARK_ROUTE2_E_CENTER_SINGLE_BOX_LIMIT_UNDERDETERMINATION_NO_GO_NOTE_2026-06-21.md"


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def dec_fraction(text: str) -> Fraction:
    return Fraction(Decimal(text))


def label(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def parse_gamma_values() -> dict[str, Fraction]:
    text = read(CACHE)
    values: dict[str, Fraction] = {}
    for key, pattern in (
        ("gE_center", r"gamma_E\(center\)\s*=\s*([-+0-9.eE]+)"),
        ("gE_shell", r"gamma_E\(shell\)\s*=\s*([-+0-9.eE]+)"),
        ("gT_center", r"gamma_T\(center\)\s*=\s*([-+0-9.eE]+)"),
        ("gT_shell", r"gamma_T\(shell\)\s*=\s*([-+0-9.eE]+)"),
    ):
        match = re.search(pattern, text)
        if match:
            values[key] = dec_fraction(match.group(1))
    return values


def q_law(limit: Fraction, measured: Fraction, n: int, power: int = 1) -> Fraction:
    return limit + (measured - limit) * Fraction(N0, n) ** power


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def check_anchor(path: Path, snippets: tuple[str, ...]) -> None:
    text = read(path)
    for index, snippet in enumerate(snippets, 1):
        check(f"authority_anchor_{path.name}_{index}", snippet in text, snippet)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 SINGLE-BOX E-CENTER LIMIT UNDERDETERMINATION NO-GO")
    print("=" * 88)

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    required = (
        CACHE,
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md",
    )
    for path in required:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    check_anchor(
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        (
            "The landed cache cannot distinguish",
            "The decisive discriminator is a **box-size scan and extrapolation of",
            "a derivation of `21/4`",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "source-domain, or readout-map primitive is supplied.",
            "E-center-blind endpoint class",
        ),
    )
    check_anchor(
        DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md",
        (
            "The live `E`-channel shell/center quotient is",
            "15/8 = 1.875",
            "not retained, because the current theorem stack does not yet derive `15/8`",
        ),
    )

    print()
    print("B. Parse the single-box measured calibration")
    print("-" * 72)
    values = parse_gamma_values()
    check("cache_has_all_gamma_values", set(values) == {"gE_center", "gE_shell", "gT_center", "gT_shell"})
    q_e_15 = values["gE_center"] / values["gE_shell"]
    q_t_15 = values["gT_center"] / values["gT_shell"]
    rho_e_15 = rho_from_q(q_e_15)
    check("measured_qE_near_target", abs(float(q_e_15 - TARGET_Q_E)) < 0.002, f"q_E(15)={float(q_e_15):.12f}")
    check("measured_qE_not_exact_target", q_e_15 != TARGET_Q_E, f"q_E(15)-15/8={float(q_e_15 - TARGET_Q_E):.12e}")
    check("measured_rho_near_target", abs(float(rho_e_15 - TARGET_RHO_E)) < 0.01, f"rho_E(15)={float(rho_e_15):.12f}")
    check("measured_qT_much_tighter_than_qE", abs(float(q_t_15 - Fraction(5, 6))) < abs(float(q_e_15 - TARGET_Q_E)), f"q_T gap={float(abs(q_t_15-Fraction(5,6))):.3e}; q_E gap={float(abs(q_e_15-TARGET_Q_E)):.3e}")

    print()
    print("C. Two explicit finite-size laws with the same N=15 datum")
    print("-" * 72)
    target_at_15 = q_law(TARGET_Q_E, q_e_15, N0)
    alt_at_15 = q_law(ALT_Q_E, q_e_15, N0)
    check("target_limit_law_matches_N15", target_at_15 == q_e_15)
    check("alternate_limit_law_matches_N15", alt_at_15 == q_e_15)
    check("target_limit_is_15_8", TARGET_Q_E == Fraction(15, 8))
    check("alternate_limit_is_not_15_8", ALT_Q_E != TARGET_Q_E and ALT_Q_E == TARGET_Q_E + Fraction(1, 1000), f"alt={label(ALT_Q_E)}")
    check("target_rho_limit_is_21_4", rho_from_q(TARGET_Q_E) == TARGET_RHO_E)
    check("alternate_rho_limit_differs", rho_from_q(ALT_Q_E) == ALT_RHO_E and ALT_RHO_E != TARGET_RHO_E, f"alt_rho={label(ALT_RHO_E)}")

    coeff_target = N0 * (q_e_15 - TARGET_Q_E)
    coeff_alt = N0 * (q_e_15 - ALT_Q_E)
    check("target_correction_coefficient_small", abs(float(coeff_target)) < 0.02, f"coeff={float(coeff_target):.6e}")
    check("alternate_correction_coefficient_small", abs(float(coeff_alt)) < 0.02, f"coeff={float(coeff_alt):.6e}")

    for n in (30, 60, 120, 240):
        target_n = q_law(TARGET_Q_E, q_e_15, n)
        alt_n = q_law(ALT_Q_E, q_e_15, n)
        check(f"laws_separate_at_N{n}", target_n != alt_n, f"target={float(target_n):.12f}; alt={float(alt_n):.12f}")
        check(f"target_law_has_constant_1_over_N_coefficient_N{n}", n * (target_n - TARGET_Q_E) == coeff_target)
        check(f"alt_law_has_constant_1_over_N_coefficient_N{n}", n * (alt_n - ALT_Q_E) == coeff_alt)

    print()
    print("D. Underdetermination persists for another common rate")
    print("-" * 72)
    for n in (30, 60, 120):
        target_n2 = q_law(TARGET_Q_E, q_e_15, n, power=2)
        alt_n2 = q_law(ALT_Q_E, q_e_15, n, power=2)
        check(f"quadratic_laws_match_N15_and_separate_N{n}", q_law(TARGET_Q_E, q_e_15, N0, 2) == q_e_15 and q_law(ALT_Q_E, q_e_15, N0, 2) == q_e_15 and target_n2 != alt_n2)

    print()
    print("E. Paired note hygiene")
    print("-" * 72)
    note_exists = NOTE_PATH.exists()
    check("paired_note_exists", note_exists, str(NOTE_PATH.relative_to(ROOT)))
    if note_exists:
        note = read(NOTE_PATH)
        check("paired_note_states_single_box_no_go", "single-box limit underdetermination no-go" in note)
        check("paired_note_preserves_measured_route", "does not reject the measured-calibration route" in note)
        check("paired_note_status_not_bare_retained", re.search(r"(?m)^(?:\\*\\*)?Status(?:\\*\\*)?:\\s*(retained|promoted)\\b", note) is None)
        banned = (
            "retained " "branch-local",
            "would become " "retained",
            "promoted to " "retained",
            "retained on the actual " "surface",
            "Nature-grade " "closure",
            "closes the " "parent",
        )
        check("paired_note_avoids_banned_phrases", all(phrase not in note for phrase in banned))

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: no-go for exactifying the Route-2 E-center fingerprint from "
        "one finite-box calibration point.  The same N=15 q_E datum is "
        "compatible with explicit decaying finite-size laws converging to "
        "15/8 and to a distinct nearby limit, so a box-size scan, convergence "
        "law, or independent source theorem remains required."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
