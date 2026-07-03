#!/usr/bin/env python3
"""Typed R_conn magnitude bridge no-go for the current Route-2 bank.

This runner attacks the post-sign-split residual:

    |gamma_T(center) / gamma_E(center)| = R_conn = 8/9.

It proves a narrow obstruction for the current source inventory.  The exact
SU(3) color scalar is constant across the Route-2 restricted readout family,
while the center T/E magnitude varies with the free E-center readout entry.
Therefore a color-only or E-center-blind current primitive cannot supply the
typed magnitude bridge.  A future nonblind source/readout theorem is not ruled
out.
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
NEGATIVE_NUMERATOR = S_TE * Q_T
R_CONN = Fraction(8, 9)
TARGET_RHO_E = Fraction(21, 4)
TARGET_Q_E = Fraction(15, 8)

NOTE_PATH = DOCS / "QUARK_ROUTE2_TYPED_RCONN_MAGNITUDE_BRIDGE_NO_GO_NOTE_2026-06-21.md"


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


def r_conn(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_from_rho(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def center_te_from_q(q_e: Fraction) -> Fraction:
    return NEGATIVE_NUMERATOR / q_e


def abs_center_te_from_rho(rho_e: Fraction) -> Fraction:
    return abs(center_te_from_q(q_from_rho(rho_e)))


def reduced_map(rho_e: Fraction) -> np.ndarray:
    return np.array(
        [
            [1.0, 0.0, float(rho_e), 0.0],
            [0.0, -2.0, 0.0, 2.0],
        ],
        dtype=float,
    )


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
    ("route2_bright_E_T", "route2_bilinear_carrier_K_R"),
    ("route2_bilinear_carrier_K_R", "route2_restricted_readout_family"),
    ("route2_restricted_readout_family", "route2_endpoint_algebra"),
    ("route2_t_side_candidates", "route2_q_T_5_6_and_shell_TE_minus_2"),
    ("route2_center_TE_minus_8_9", "route2_q_E_15_8"),
    ("route2_q_E_15_8", "route2_rho_E_21_4"),
    ("su3_color_trace_channel", "su3_R_conn_8_9"),
)

MISSING_MAGNITUDE_BRIDGE = ("su3_R_conn_8_9", "route2_abs_center_TE_8_9")
MISSING_SIGNED_BRIDGE = ("su3_R_conn_8_9", "route2_center_TE_minus_8_9")


def same_vector(left: np.ndarray, right: np.ndarray) -> bool:
    return bool(np.max(np.abs(left - right)) < EXACT_TOL)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 TYPED R_CONN MAGNITUDE BRIDGE NO-GO")
    print("=" * 88)

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    required = (
        DOCS / "RCONN_DERIVED_NOTE.md",
        DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md",
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
    )
    for path in required:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    check_anchor(
        DOCS / "RCONN_DERIVED_NOTE.md",
        (
            "At `N_c = 3`, `F_adj = 8/9`.",
            "The exact `8/9` support remains available as `F_adj`, not as a",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
        (
            "There is no current typed edge",
            "The sign and endpoint orientation are not supplied by the color projection",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md",
        (
            "No current retained note supplies a typed source-domain",
            "The exact restricted carrier/readout family after granting the T-side values",
        ),
    )
    check_anchor(
        DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E.",
            "So `rho_E = 0` and `rho_E = 21/4` are both exact admissible maps",
        ),
    )
    check_anchor(
        DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "This note **does not derive**",
            "the bilinear microscopic carrier `K_R(q)` on the",
        ),
    )
    check_anchor(
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        (
            "admissible readout in the 1-parameter family `P(rho_E)`",
            "with `rho_E = beta_E / alpha_E` the irreducible undetermined entry.",
        ),
    )

    print()
    print("B. Exact magnitude algebra")
    print("-" * 72)
    check("su3_adjoint_fraction_nc3", r_conn(3) == R_CONN, f"F_adj={label(r_conn(3))}")
    check("target_q_E_from_rho", q_from_rho(TARGET_RHO_E) == TARGET_Q_E, f"q_E={label(q_from_rho(TARGET_RHO_E))}")
    check("target_abs_center_ratio", abs_center_te_from_rho(TARGET_RHO_E) == R_CONN, f"|c_TE|={label(abs_center_te_from_rho(TARGET_RHO_E))}")
    check("no_lift_abs_center_ratio_differs", abs_center_te_from_rho(Fraction(0, 1)) == Fraction(5, 3), f"|c_TE|={label(abs_center_te_from_rho(Fraction(0, 1)))}")
    check("unit_lift_abs_center_ratio_differs", abs_center_te_from_rho(Fraction(1, 1)) == Fraction(10, 7), f"|c_TE|={label(abs_center_te_from_rho(Fraction(1, 1)))}")
    check("larger_lift_abs_center_ratio_differs", abs_center_te_from_rho(Fraction(8, 1)) == Fraction(5, 7), f"|c_TE|={label(abs_center_te_from_rho(Fraction(8, 1)))}")

    examples = (Fraction(0, 1), Fraction(1, 1), TARGET_RHO_E, Fraction(8, 1))
    magnitudes = tuple(abs_center_te_from_rho(rho) for rho in examples)
    check("positive_family_has_multiple_magnitudes", len(set(magnitudes)) == len(magnitudes), ", ".join(label(m) for m in magnitudes))
    check("only_target_example_has_Rconn_magnitude", [rho for rho in examples if abs_center_te_from_rho(rho) == R_CONN] == [TARGET_RHO_E])
    check("color_scalar_constant_across_family", len({R_CONN for _ in examples}) == 1, f"F_adj={label(R_CONN)}")
    check(
        "color_only_function_cannot_equal_variable_readout_magnitude",
        len(set(magnitudes)) > 1,
        "same color input, different |center T/E| values",
    )

    print()
    print("C. E-center-blind witness family")
    print("-" * 72)
    data = restricted_readout_data()
    p_zero = reduced_map(Fraction(0, 1))
    p_target = reduced_map(TARGET_RHO_E)
    p_unit = reduced_map(Fraction(1, 1))
    for name, col in (
        ("E_shell", data.carrier_e_shell),
        ("T_shell", data.carrier_t_shell),
        ("T_center", data.carrier_t_center),
    ):
        check(
            f"rho0_and_target_agree_on_{name}",
            same_vector(p_zero @ col, p_target @ col),
            f"{p_zero @ col} vs {p_target @ col}",
        )
        check(
            f"rho1_and_target_agree_on_{name}",
            same_vector(p_unit @ col, p_target @ col),
            f"{p_unit @ col} vs {p_target @ col}",
        )
    check(
        "rho0_and_target_differ_on_E_center",
        not same_vector(p_zero @ data.carrier_e_center, p_target @ data.carrier_e_center),
        f"{p_zero @ data.carrier_e_center} vs {p_target @ data.carrier_e_center}",
    )
    check(
        "rho1_and_target_differ_on_E_center",
        not same_vector(p_unit @ data.carrier_e_center, p_target @ data.carrier_e_center),
        f"{p_unit @ data.carrier_e_center} vs {p_target @ data.carrier_e_center}",
    )

    blind_signature_zero = (
        tuple(np.round(p_zero @ data.carrier_e_shell, 12)),
        tuple(np.round(p_zero @ data.carrier_t_shell, 12)),
        tuple(np.round(p_zero @ data.carrier_t_center, 12)),
    )
    blind_signature_target = (
        tuple(np.round(p_target @ data.carrier_e_shell, 12)),
        tuple(np.round(p_target @ data.carrier_t_shell, 12)),
        tuple(np.round(p_target @ data.carrier_t_center, 12)),
    )
    check("E_center_blind_signature_is_identical", blind_signature_zero == blind_signature_target)
    check(
        "E_center_blind_signature_cannot_select_magnitude",
        abs_center_te_from_rho(Fraction(0, 1)) != abs_center_te_from_rho(TARGET_RHO_E),
        f"{label(abs_center_te_from_rho(Fraction(0, 1)))} vs {label(abs_center_te_from_rho(TARGET_RHO_E))}",
    )

    print()
    print("D. Typed graph firewall")
    print("-" * 72)
    check("current_graph_lacks_magnitude_edge", MISSING_MAGNITUDE_BRIDGE not in CURRENT_TYPED_EDGES)
    check("current_graph_lacks_signed_edge", MISSING_SIGNED_BRIDGE not in CURRENT_TYPED_EDGES)
    check(
        "current_graph_no_path_to_abs_center_ratio",
        not reachable(CURRENT_TYPED_EDGES, "su3_R_conn_8_9", "route2_abs_center_TE_8_9"),
    )
    check(
        "current_graph_no_path_to_signed_center_ratio",
        not reachable(CURRENT_TYPED_EDGES, "su3_R_conn_8_9", "route2_center_TE_minus_8_9"),
    )
    check(
        "current_graph_no_path_to_rho_target",
        not reachable(CURRENT_TYPED_EDGES, "su3_R_conn_8_9", "route2_rho_E_21_4"),
    )
    magnitude_augmented = CURRENT_TYPED_EDGES + (MISSING_MAGNITUDE_BRIDGE,)
    check(
        "adding_only_magnitude_edge_reaches_abs_node",
        reachable(magnitude_augmented, "su3_R_conn_8_9", "route2_abs_center_TE_8_9"),
    )
    check(
        "adding_only_magnitude_edge_still_no_signed_path",
        not reachable(magnitude_augmented, "su3_R_conn_8_9", "route2_center_TE_minus_8_9"),
    )

    print()
    print("E. Wrong-structure controls")
    print("-" * 72)
    check("wrong_nc2_scalar_is_not_target_magnitude", r_conn(2) == Fraction(3, 4) and r_conn(2) != R_CONN, f"Nc=2 F_adj={label(r_conn(2))}")
    check("wrong_nc4_scalar_is_not_target_magnitude", r_conn(4) == Fraction(15, 16) and r_conn(4) != R_CONN, f"Nc=4 F_adj={label(r_conn(4))}")
    q_wrong_nc2 = Fraction(5, 3) / r_conn(2)
    rho_wrong_nc2 = rho_from_q(q_wrong_nc2)
    check("wrong_nc2_if_forced_gives_wrong_endpoint", rho_wrong_nc2 == Fraction(22, 3), f"rho_E={label(rho_wrong_nc2)}")

    print()
    print("F. Paired note hygiene")
    print("-" * 72)
    note_exists = NOTE_PATH.exists()
    check("paired_note_exists", note_exists, str(NOTE_PATH.relative_to(ROOT)))
    if note_exists:
        note = read(NOTE_PATH)
        check("paired_note_states_narrow_no_go", "no-go for the current color-only and E-center-blind typed-magnitude route" in note)
        check("paired_note_preserves_future_bridge", "does not rule out a future nonblind source/readout theorem" in note)
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
        "VERDICT: no-go for the current typed-magnitude route.  The SU(3) "
        "color scalar is constant while |center T/E| varies across the exact "
        "Route-2 readout family, and the current typed graph has no edge from "
        "R_conn/F_adj to the Route-2 magnitude node.  A future nonblind "
        "source/readout bridge is not ruled out."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
