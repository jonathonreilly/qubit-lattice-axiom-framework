#!/usr/bin/env python3
"""Exact E-center fingerprint packet for the Route-2 readout target.

This runner does not derive rho_E = 21/4.  It records the exact acceptance
test any future nonblind E-center source/readout primitive must pass:

    q_E = 15/8
    rho_E = 21/4
    E-center contrast = 7/8
    q_E/q_T = 9/4
    c_TE = -8/9

and the equivalent slice-level rank-1 prefactor fingerprint inherited from
the exact readout-to-slice factorization.
"""

from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path
import re
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0
EXACT_TOL = 1.0e-12

Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_CONTRAST = Fraction(7, 8)
TARGET_C_TE = Fraction(-8, 9)
TARGET_Q_RATIO = Fraction(9, 4)
TARGET_D_E = Fraction(21, 8)

NOTE_PATH = DOCS / "QUARK_ROUTE2_E_CENTER_FINGERPRINT_EXACT_SUPPORT_NOTE_2026-06-21.md"


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


def label(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_from_rho(rho_e: Fraction) -> Fraction:
    return 1 + rho_e / 6


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def contrast_from_q(q_e: Fraction) -> Fraction:
    return q_e - 1


def q_from_contrast(contrast: Fraction) -> Fraction:
    return 1 + contrast


def center_ratio(q_e: Fraction) -> Fraction:
    return S_TE * Q_T / q_e


def q_ratio(q_e: Fraction) -> Fraction:
    return q_e / Q_T


def d_e_from_rho(rho_e: Fraction) -> Fraction:
    return rho_e / 2


def p_readout(rho_e: Fraction) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    return (
        (Fraction(1), Fraction(0), rho_e, Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0), Fraction(2)),
    )


def mat_vec(
    mat: tuple[tuple[Fraction, ...], tuple[Fraction, ...]],
    vec: tuple[Fraction, Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    return tuple(sum(row[i] * vec[i] for i in range(4)) for row in mat)  # type: ignore[return-value]


def tensor_prefactor(
    readout_vec: tuple[Fraction, Fraction],
    time_vec: tuple[Fraction, ...],
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    return tuple(tuple(component * t for t in time_vec) for component in readout_vec)  # type: ignore[return-value]


def difference(
    left: tuple[tuple[Fraction, ...], tuple[Fraction, ...]],
    right: tuple[tuple[Fraction, ...], tuple[Fraction, ...]],
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(len(left[row])))
        for row in range(2)
    )  # type: ignore[return-value]


def check_anchor(path: Path, snippets: tuple[str, ...]) -> None:
    text = read(path)
    for index, snippet in enumerate(snippets, 1):
        check(f"authority_anchor_{path.name}_{index}", snippet in text, snippet)


def reachable(edges: tuple[tuple[str, str], ...], source: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for left, right in edges:
        graph[left].append(right)
    queue: deque[str] = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


CURRENT_TYPED_EDGES: tuple[tuple[str, str], ...] = (
    ("route2_support_delta_A1", "route2_bilinear_carrier_K_R"),
    ("route2_bilinear_carrier_K_R", "route2_restricted_readout_family"),
    ("route2_restricted_readout_family", "route2_endpoint_algebra"),
    ("route2_t_side_candidates", "route2_q_T_5_6_and_shell_TE_minus_2"),
)

FINGERPRINT_EDGES: tuple[tuple[str, str], ...] = (
    ("route2_ecenter_contrast_7_8", "route2_q_E_15_8"),
    ("route2_q_E_15_8", "route2_rho_E_21_4"),
    ("route2_q_E_15_8", "route2_center_TE_minus_8_9"),
    ("route2_q_E_15_8", "route2_qE_over_qT_9_4"),
)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 E-CENTER FINGERPRINT EXACT SUPPORT")
    print("=" * 88)

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    required = (
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md",
    )
    for path in required:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    check_anchor(
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6",
            "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E.",
            "So `rho_E = 0` and `rho_E = 21/4` are both exact admissible maps",
        ),
    )
    check_anchor(
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        (
            "Xi_P(t ; c) = (P_R c) \u2297 V_R(t)",
            "because the readout-map endpoint triple is not derived",
        ),
    )
    check_anchor(
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        (
            "P(rho_E) = [[1, 0, rho_E, 0],",
            "Xi_a(t ; c) - Xi_b(t ; c) = ((P_a - P_b) c) \u2297 V_R(t)",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "P(rho_E) E-center = (1 + rho_E/6, 0).",
            "source-domain, or readout-map primitive is supplied.",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        (
            "q_E = (9/4)",
            "no derivation of 21/4 is claimed",
        ),
    )
    check_anchor(
        DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md",
        (
            "gamma_E(center)/gamma_E(shell) = 15/8.",
            "positive repair must add a real E-center lift or equivalent source/readout",
        ),
    )

    print()
    print("B. Exact fingerprint equivalences")
    print("-" * 72)
    check("target_q_from_rho", q_from_rho(TARGET_RHO_E) == TARGET_Q_E, f"q_E={label(q_from_rho(TARGET_RHO_E))}")
    check("target_rho_from_q", rho_from_q(TARGET_Q_E) == TARGET_RHO_E, f"rho_E={label(rho_from_q(TARGET_Q_E))}")
    check("target_contrast_from_q", contrast_from_q(TARGET_Q_E) == TARGET_CONTRAST, f"contrast={label(contrast_from_q(TARGET_Q_E))}")
    check("target_q_from_contrast", q_from_contrast(TARGET_CONTRAST) == TARGET_Q_E, f"q_E={label(q_from_contrast(TARGET_CONTRAST))}")
    check("target_center_ratio", center_ratio(TARGET_Q_E) == TARGET_C_TE, f"c_TE={label(center_ratio(TARGET_Q_E))}")
    check("target_q_ratio", q_ratio(TARGET_Q_E) == TARGET_Q_RATIO, f"q_E/q_T={label(q_ratio(TARGET_Q_E))}")
    check("target_D_E", d_e_from_rho(TARGET_RHO_E) == TARGET_D_E, f"D_E={label(d_e_from_rho(TARGET_RHO_E))}")

    alternatives = (
        ("no_lift", Fraction(0, 1)),
        ("unit_lift", Fraction(1, 1)),
        ("same_as_T", Fraction(-1, 1)),
        ("large_lift", Fraction(8, 1)),
    )
    for name, rho in alternatives:
        q = q_from_rho(rho)
        check(f"{name}_does_not_hit_q", q != TARGET_Q_E, f"q_E={label(q)}")
        check(f"{name}_does_not_hit_contrast", contrast_from_q(q) != TARGET_CONTRAST, f"contrast={label(contrast_from_q(q))}")
        check(f"{name}_does_not_hit_center_ratio", center_ratio(q) != TARGET_C_TE, f"c_TE={label(center_ratio(q))}")

    print()
    print("C. Carrier/readout fingerprint")
    print("-" * 72)
    e_shell = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    e_center = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
    target_p = p_readout(TARGET_RHO_E)
    no_lift_p = p_readout(Fraction(0, 1))
    shell_readout = mat_vec(target_p, e_shell)
    center_readout = mat_vec(target_p, e_center)
    no_lift_center_readout = mat_vec(no_lift_p, e_center)
    check("target_E_shell_readout", shell_readout == (Fraction(1), Fraction(0)), str(shell_readout))
    check("target_E_center_readout", center_readout == (TARGET_Q_E, Fraction(0)), str(center_readout))
    check("target_E_center_minus_shell", center_readout[0] - shell_readout[0] == TARGET_CONTRAST, f"delta={label(center_readout[0] - shell_readout[0])}")
    check("no_lift_E_center_equals_shell", no_lift_center_readout == shell_readout, str(no_lift_center_readout))
    check("excess_derivative_is_rho", TARGET_CONTRAST / Fraction(1, 6) == TARGET_RHO_E, f"derivative={label(TARGET_CONTRAST / Fraction(1, 6))}")

    data = restricted_readout_data()
    live_q_e = Fraction.from_float(float(data.q_e)).limit_denominator(10**12)
    live_rho = Fraction.from_float(float(data.rho_e)).limit_denominator(10**12)
    check("live_q_E_is_comparator_not_exact_target", abs(float(data.q_e) - float(TARGET_Q_E)) > EXACT_TOL, f"live={data.q_e:.12f}, target={float(TARGET_Q_E):.12f}")
    check("live_rho_is_comparator_not_exact_target", abs(float(data.rho_e) - float(TARGET_RHO_E)) > EXACT_TOL, f"live={data.rho_e:.12f}, target={float(TARGET_RHO_E):.12f}")
    check("live_values_are_near_target", abs(float(data.q_e) - float(TARGET_Q_E)) < 0.002 and abs(float(data.rho_e) - float(TARGET_RHO_E)) < 0.01, f"q={float(live_q_e):.12f}, rho={float(live_rho):.12f}")

    print()
    print("D. Slice-level fingerprint")
    print("-" * 72)
    time_vec = (Fraction(3), Fraction(-2), Fraction(5))
    shell_tensor = tensor_prefactor(shell_readout, time_vec)
    target_center_tensor = tensor_prefactor(center_readout, time_vec)
    no_lift_center_tensor = tensor_prefactor(no_lift_center_readout, time_vec)
    target_minus_no_lift = difference(target_center_tensor, no_lift_center_tensor)
    expected_diff = tensor_prefactor((TARGET_CONTRAST, Fraction(0)), time_vec)
    check("slice_difference_matches_7_8_prefactor", target_minus_no_lift == expected_diff, str(target_minus_no_lift))
    check(
        "slice_difference_component_ratios_are_7_8",
        all(target_minus_no_lift[0][i] / time_vec[i] == TARGET_CONTRAST for i in range(len(time_vec)) if time_vec[i] != 0),
        ", ".join(label(target_minus_no_lift[0][i] / time_vec[i]) for i in range(len(time_vec)) if time_vec[i] != 0),
    )
    check("slice_time_row_unchanged", target_minus_no_lift[1] == (Fraction(0), Fraction(0), Fraction(0)), str(target_minus_no_lift[1]))
    check("shell_tensor_nonzero_for_ratio", any(x != 0 for x in shell_tensor[0]))

    print()
    print("E. Trace graph")
    print("-" * 72)
    check(
        "current_graph_lacks_fingerprint_node",
        not reachable(CURRENT_TYPED_EDGES, "route2_restricted_readout_family", "route2_ecenter_contrast_7_8"),
    )
    augmented = CURRENT_TYPED_EDGES + FINGERPRINT_EDGES + (("route2_restricted_readout_family", "route2_ecenter_contrast_7_8"),)
    check(
        "fingerprint_edge_reaches_q_E",
        reachable(augmented, "route2_restricted_readout_family", "route2_q_E_15_8"),
    )
    check(
        "fingerprint_edge_reaches_rho_E",
        reachable(augmented, "route2_restricted_readout_family", "route2_rho_E_21_4"),
    )
    check(
        "fingerprint_edge_reaches_center_ratio",
        reachable(augmented, "route2_restricted_readout_family", "route2_center_TE_minus_8_9"),
    )

    print()
    print("F. Paired note hygiene")
    print("-" * 72)
    note_exists = NOTE_PATH.exists()
    check("paired_note_exists", note_exists, str(NOTE_PATH.relative_to(ROOT)))
    if note_exists:
        note = read(NOTE_PATH)
        check("paired_note_says_not_derivation", "not a derivation of the endpoint triple" in note)
        check("paired_note_names_fingerprint", "E-center contrast `7/8`" in note)
        check("paired_note_keeps_exact_support_status", "**Status:** exact support" in note)
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
        "VERDICT: exact support only.  Any future nonblind E-center "
        "source/readout primitive that closes the Route-2 target must supply "
        "the exact fingerprint q_E=15/8, rho_E=21/4, contrast=7/8, "
        "q_E/q_T=9/4, and c_TE=-8/9.  The current bank still does not derive "
        "that fingerprint."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
