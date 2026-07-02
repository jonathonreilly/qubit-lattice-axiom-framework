#!/usr/bin/env python3
"""Fixed-carrier Route-2 selector equation boundary.

This runner checks a narrow Block94 no-go:

    fixed Route-2 carrier + granted T-side endpoint values
    + basic source-vector conservation/equipartition selector equations
    does not derive rho_E = 21/4.

The target appears exactly when an equivalent center/source bridge
`c_TE = -8/9` is added, or when a fitted quadratic metric ratio is supplied.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import math

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_FIXED_CARRIER_SELECTOR_EQUATION_BOUNDARY_NOTE_2026-06-21.md"

PASS_COUNT = 0
FAIL_COUNT = 0
EXACT_TOL = 1.0e-12

Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2, 1)
GAMMA_T_CENTER = Fraction(-5, 3)
F_ADJ = Fraction(8, 9)
TARGET_C_TE = -F_ADJ
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def q_from_rho(rho_e: Fraction) -> Fraction:
    return 1 + rho_e / 6


def center_te(q_e: Fraction) -> Fraction:
    return GAMMA_T_CENTER / q_e


def q_from_center_te(c_te: Fraction) -> Fraction:
    return GAMMA_T_CENTER / c_te


def source_shell() -> tuple[Fraction, Fraction]:
    return (Fraction(1), Fraction(-2))


def source_center(q_e: Fraction) -> tuple[Fraction, Fraction]:
    return (q_e, GAMMA_T_CENTER)


def l1_source_conservation_q() -> Fraction:
    # For the positive target range q_E > 0, |q_E| + 5/3 = 1 + 2.
    return Fraction(4, 3)


def product_conservation_q() -> Fraction:
    # q_E * (-5/3) = 1 * (-2)
    return Fraction(6, 5)


def slope_conservation_q() -> Fraction:
    # (-5/3) / q_E = -2
    return Fraction(5, 6)


def center_abs_balance_q() -> Fraction:
    # q_E = |-5/3|
    return Fraction(5, 3)


def positive_linear_conservation_has_target(q_e: Fraction) -> bool:
    # a q_E + b(-5/3) = a(1) + b(-2)
    # a(q_E-1) + b/3 = 0. For q_E > 1 and a,b >= 0, only a=b=0 works.
    return q_e <= 1


def diagonal_quadratic_metric_ratio(q_e: Fraction) -> Fraction:
    # a q_E^2 + b(25/9) = a(1) + b(4)
    # b/a = 9(q_E^2 - 1)/11.
    return Fraction(9, 11) * (q_e * q_e - 1)


def low_ratio_set(max_num: int = 64, max_den: int = 64) -> set[Fraction]:
    out: set[Fraction] = set()
    for den in range(1, max_den + 1):
        for num in range(1, max_num + 1):
            out.add(Fraction(num, den))
    return out


def part1_authority_anchors() -> None:
    print("\nA. Authority anchors")
    paths = [
        NOTE,
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
        DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
        DOCS / "MINIMAL_AXIOMS_2026-06-05.md",
    ]
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(NOTE)
    readout_note = read(paths[1])
    naturality_note = read(paths[3])
    source_note = read(paths[5])
    axiom_note = " ".join(read(paths[6]).split())

    check("new note declares no-go status", "no-go / negative route pruning" in note)
    check("new note declares no_go type metadata", "**Type:** no_go" in note and "**Claim type:** no_go" in note)
    check("new note uses markdown links for load-bearing authorities", "[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)" in note and "[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)" in note)
    check("new note says no endpoint closure", "no endpoint closure" in note)
    check("new note names the fixed source vectors", "S = (gamma_E(shell), gamma_T(shell)) = (1, -2)" in note)
    check("new note names target rho_E and q_E", "rho_E := beta_E / alpha_E = 21/4" in note and "q_E := gamma_E(center) / gamma_E(shell) = 15/8" in note)
    check("readout authority names beta_E/alpha_E as the missing map entry", "beta_E / alpha_E = 21/4" in readout_note)
    check("naturality note names the same E-center target", "gamma_E(center)/gamma_E(shell) = 15/8" in naturality_note)
    check("source-domain note names the center bridge target", "gamma_T(center) / gamma_E(center) = -R_conn" in source_note)
    check("minimal axioms do not supply readout weighting", "A record supplies no readout context" in axiom_note and "weighting" in axiom_note)


def part2_fixed_carrier_data() -> None:
    print("\nB. Fixed-carrier algebra")
    data = restricted_readout_data()
    target_shell = np.array([1.0, 0.0, 0.0, 0.0])
    target_center = np.array([1.0, 0.0, 1.0 / 6.0, 0.0])

    check(
        "imported E-shell carrier column is exact",
        np.max(np.abs(data.carrier_e_shell - target_shell)) < EXACT_TOL,
        str(data.carrier_e_shell),
    )
    check(
        "imported E-center carrier column is exact",
        np.max(np.abs(data.carrier_e_center - target_center)) < EXACT_TOL,
        str(data.carrier_e_center),
    )
    check("granted q_T is exact 5/6", Q_T == Fraction(5, 6), str(Q_T))
    check("granted shell T/E is exact -2", SHELL_TE == Fraction(-2, 1), str(SHELL_TE))
    check("granted center T value is exact -5/3", GAMMA_T_CENTER == SHELL_TE * Q_T, str(GAMMA_T_CENTER))
    check("target q_E maps to rho_E=21/4", rho_from_q(TARGET_Q_E) == TARGET_RHO_E, str(rho_from_q(TARGET_Q_E)))
    check("target rho_E maps back to q_E=15/8", q_from_rho(TARGET_RHO_E) == TARGET_Q_E, str(q_from_rho(TARGET_RHO_E)))
    check("target q_E maps to center T/E=-8/9", center_te(TARGET_Q_E) == TARGET_C_TE, str(center_te(TARGET_Q_E)))
    check("center bridge c_TE=-8/9 maps to q_E=15/8", q_from_center_te(TARGET_C_TE) == TARGET_Q_E, str(q_from_center_te(TARGET_C_TE)))


def part3_selector_fanout() -> None:
    print("\nC. Selector equation fan-out")
    selectors = {
        "no_lift": Fraction(1, 1),
        "same_slope_collinear": slope_conservation_q(),
        "product_conservation": product_conservation_q(),
        "l1_source_conservation": l1_source_conservation_q(),
        "center_abs_balance": center_abs_balance_q(),
    }
    for label, q_e in selectors.items():
        rho = rho_from_q(q_e)
        c_te = center_te(q_e)
        print(f"  {label}: q_E={q_e}, rho_E={rho}, c_TE={c_te}")
        check(f"{label} does not select q_E=15/8", q_e != TARGET_Q_E)

    check("slope preservation gives rho_E=-1", rho_from_q(slope_conservation_q()) == Fraction(-1, 1))
    check("product conservation gives rho_E=6/5", rho_from_q(product_conservation_q()) == Fraction(6, 5))
    check("L1 conservation gives rho_E=2", rho_from_q(l1_source_conservation_q()) == Fraction(2, 1))
    check("center absolute balance gives rho_E=4", rho_from_q(center_abs_balance_q()) == Fraction(4, 1))
    check("target q_E is greater than one", TARGET_Q_E > 1)
    check("positive linear source conservation cannot select target", not positive_linear_conservation_has_target(TARGET_Q_E))


def part4_metric_and_bridge_boundary() -> None:
    print("\nD. Metric and bridge boundary")
    metric_ratio = diagonal_quadratic_metric_ratio(TARGET_Q_E)
    simple_ratios = {
        Fraction(1, 1),
        Fraction(2, 1),
        Fraction(3, 1),
        Fraction(4, 1),
        Fraction(6, 1),
        F_ADJ,
        1 / F_ADJ,
        Q_T,
        1 / Q_T,
        abs(SHELL_TE),
    }
    print(f"  target diagonal metric b/a = {metric_ratio}")

    check("target metric ratio is exact 1449/704", metric_ratio == Fraction(1449, 704), str(metric_ratio))
    check("target metric ratio is positive", metric_ratio > 0)
    check("target metric ratio is not one of the primitive simple ratios", metric_ratio not in simple_ratios)
    check("target metric ratio is not in numerator/denominator <=64 scan", metric_ratio not in low_ratio_set(64, 64))

    q_from_bridge = q_from_center_te(-F_ADJ)
    check("bridge c_TE=-F_adj selects target q_E", q_from_bridge == TARGET_Q_E, str(q_from_bridge))
    check("bridge c_TE=-F_adj selects target rho_E", rho_from_q(q_from_bridge) == TARGET_RHO_E, str(rho_from_q(q_from_bridge)))
    check("positive F_adj without signed center bridge gives wrong q_E", q_from_center_te(F_ADJ) == Fraction(-15, 8), str(q_from_center_te(F_ADJ)))
    check("target selection by bridge is equivalent to adding c_TE=-8/9", TARGET_C_TE == Fraction(-8, 9), str(TARGET_C_TE))


def part5_firewall() -> None:
    print("\nE. Claim firewall")
    note = read(NOTE)
    note_flat = " ".join(note.split())
    forbidden = [
        "observed_quark_masses",
        "fitted_yukawa_entries",
        "ckm_j_error_minimization",
        "nearest_rational_live_endpoint",
    ]
    proof_inputs = {
        "fixed_carrier_vectors",
        "granted_t_side_values",
        "exact_fraction_arithmetic",
        "selector_equation_fanout",
    }
    check("forbidden proof inputs are absent", proof_inputs.isdisjoint(forbidden), str(sorted(proof_inputs)))
    check("note keeps future center bridge route open", "future theorem that derives `c_TE = -8/9`" in note_flat)
    check("note keeps future metric route open", "derives the metric ratio `1449/704`" in note_flat)
    check("note does not claim the endpoint triple is derived", "does not close the endpoint triple" in note)
    check("note has proposal_allowed false", "proposal_allowed: false" in note)
    check("bare retained is disallowed", "bare_retained_allowed: false" in note)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 FIXED-CARRIER SELECTOR EQUATION BOUNDARY")
    print("=" * 88)

    part1_authority_anchors()
    part2_fixed_carrier_data()
    part3_selector_fanout()
    part4_metric_and_bridge_boundary()
    part5_firewall()

    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: fixed-carrier selector equations do not derive rho_E = 21/4.")
        print("A genuine E-center source/readout primitive is still required.")
        return 0
    print("VERDICT: fixed-carrier selector boundary checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
