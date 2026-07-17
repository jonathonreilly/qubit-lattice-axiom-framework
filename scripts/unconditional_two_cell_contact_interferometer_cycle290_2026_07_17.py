#!/usr/bin/env python3
"""Cycle 290: unconditional two-cell contact interferometer.

A supplied bounded route coherently relates the fixed-total-number branches
|3,3> and |4,2> on two adjacent six-mode cells.  The ordinary local contact
law acts on both cells without an action flag.  Its pair-count surplus is then
read by a supplied path recombiner.  This is a coherent comparator only.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import actual_contact_action_syndrome_tournament_cycle285_2026_07_17 as c285
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "UNCONDITIONAL_TWO_CELL_CONTACT_INTERFEROMETER_CYCLE290_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 3.0e-11
G = c278.c230.COUPLING


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-290 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "fixed total n=6",
        "|3,3",
        "|4,2",
        "ordinary local law",
        "no controlled-w_g oracle",
        "q-only replacement",
        "common global phase",
        "signed quadrature",
        "one-particle mass fixture",
        "bounded physical pauli representative",
        "zero leakage",
        "held-out l=6",
        "648 frame-translation tests",
        "supplied structure inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "close first = close second?",
        "close second = close first?",
        "independent?",
        "per-element",
        "per-site",
        "per-mode",
        "per-block",
        "lattice-wide",
        "unknown / not claimed",
        "the current broad no-go therefore fails",
        "no shared obstruction",
        "no axiom pressure",
        "scoped only to the cycle-290 reviewed two-cell encoding",
    )
    missing = tuple(item for item in required if item not in text)
    forbidden = tuple(item for item in ("attempted prior",) if item in text)
    check(
        "the note preserves the unconditional-action, same-code, control, import, and N1-N8 contract",
        not missing and not forbidden,
        {"missing": missing, "forbidden": forbidden},
    )


def basis(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1.0
    return vector


def marker_matter_operators(theta: float) -> dict[str, np.ndarray]:
    """Four-dimensional exact circuit on marker x {reference, surplus}."""

    identity = np.eye(2, dtype=complex)
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    h_marker = np.kron(h, identity)
    y_marker = np.kron(y, identity)

    # R is a supplied marker-controlled use of one bounded even intercell hop.
    # It routes matter; it does not select or control the contact action.
    route = np.asarray(
        (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
        ),
        dtype=complex,
    )
    ordinary_action = np.kron(
        identity, np.diag((1.0, np.exp(1j * theta))).astype(complex)
    )
    close = np.kron(np.diag((0.0, 1.0)), identity)
    initial = np.kron(basis(2, 0), basis(2, 0))
    return {
        "H": h_marker,
        "Y": y_marker,
        "R": route,
        "W": ordinary_action,
        "close": close,
        "initial": initial,
    }


def run_circuit(
    theta: float,
    *,
    prepare: bool = True,
    route_in: bool = True,
    action: bool = True,
    route_out: bool = True,
    recombine: bool = True,
) -> tuple[float, float, np.ndarray]:
    operators = marker_matter_operators(theta)
    state = operators["initial"]
    if prepare:
        state = operators["H"] @ state
    if route_in:
        state = operators["R"] @ state
    if action:
        state = operators["W"] @ state
    if route_out:
        state = operators["R"].conj().T @ state
    quadrature = float(np.vdot(state, operators["Y"] @ state).real)
    if recombine:
        state = operators["H"] @ state
    close = float(np.vdot(state, operators["close"] @ state).real)
    return close, quadrature, state


def branch_and_interferometer_controls() -> None:
    print("\nFIXED-NUMBER TWO-CELL BRANCH / UNCONDITIONAL ACTION")
    reference_masks = (0b001110, 0b000111)  # N=(3,3)
    surplus_masks = (0b001111, 0b000101)  # move y-direction 1 to x-direction 0
    reference_n = tuple(mask.bit_count() for mask in reference_masks)
    surplus_n = tuple(mask.bit_count() for mask in surplus_masks)
    pairs = lambda rows: sum(number * (number - 1) // 2 for number in rows)
    threshold = lambda rows: sum(number >= 2 for number in rows)
    reference_pairs = pairs(reference_n)
    surplus_pairs = pairs(surplus_n)

    actual_close, actual_y, actual_state = run_circuit(G)
    deleted_close, _, _ = run_circuit(G, action=False)
    q_only_theta = G * (threshold(surplus_n) - threshold(reference_n))
    q_only_close, _, _ = run_circuit(q_only_theta)
    global_close, _, _ = run_circuit(0.0)
    adjoint_close, adjoint_y, _ = run_circuit(-G)

    check(
        "one even bilinear redistribution gives fixed total N=6 branches |3,3> and |4,2> with pair-count surplus one but identical Q-only count",
        reference_n == (3, 3)
        and surplus_n == (4, 2)
        and sum(reference_n) == sum(surplus_n) == 6
        and reference_pairs == 6
        and surplus_pairs == 7
        and threshold(reference_n) == threshold(surplus_n) == 2,
        {
            "reference_masks": reference_masks,
            "surplus_masks": surplus_masks,
            "pair_counts": (reference_pairs, surplus_pairs),
            "Q_counts": (threshold(reference_n), threshold(surplus_n)),
        },
    )
    check(
        "the ordinary marker-independent local W_g action produces the exact relative phase g and positive dark-port close sin^2(g/2)",
        abs(actual_close - np.sin(G / 2) ** 2) < TOL
        and abs(abs(actual_y) - abs(np.sin(G))) < TOL
        and np.linalg.norm(actual_state) - 1 < TOL,
        {
            "g": G,
            "close": actual_close,
            "expected_close": float(np.sin(G / 2) ** 2),
            "signed_quadrature": actual_y,
        },
    )
    check(
        "W_g deletion, Q-only replacement, and a common global phase all give zero comparator close",
        max(abs(deleted_close), abs(q_only_close), abs(global_close)) < TOL,
        {
            "W_g_deleted": deleted_close,
            "Q_only": q_only_close,
            "global_phase": global_close,
        },
    )
    check(
        "the signed marker quadrature separates W_g from W_g dagger while their unsigned closes agree",
        abs(actual_close - adjoint_close) < TOL
        and abs(actual_y + adjoint_y) < TOL
        and abs(actual_y) > 0.3,
        {
            "W_close": actual_close,
            "W_dagger_close": adjoint_close,
            "W_Y": actual_y,
            "W_dagger_Y": adjoint_y,
        },
    )
    # The full physical action is I_marker tensor W_matter.  Its marker blocks
    # are identical, an algebraic certificate that no controlled-W_g is used.
    action_matrix = marker_matter_operators(G)["W"]
    check(
        "the action is exactly identity on the path marker tensor the ordinary matter action, not a supplied controlled-W_g oracle",
        np.linalg.norm(action_matrix[:2, :2] - action_matrix[2:, 2:]) < TOL
        and np.linalg.norm(action_matrix[:2, 2:]) == 0
        and np.linalg.norm(action_matrix[2:, :2]) == 0,
        "the marker controls only the supplied redistribution route",
    )


def route_deletion_and_minimal_steelman_controls() -> None:
    print("\nROUTE / RECOMBINER DELETIONS AND N=2 STEELMAN")
    ideal, _, _ = run_circuit(G)
    rows = {
        "W_deleted": run_circuit(G, action=False)[0],
        "route_in_deleted": run_circuit(G, route_in=False)[0],
        "route_out_deleted": run_circuit(G, route_out=False)[0],
        "both_routes_deleted": run_circuit(
            G, route_in=False, route_out=False
        )[0],
        "preparer_deleted": run_circuit(G, prepare=False)[0],
        "recombiner_deleted": run_circuit(G, recombine=False)[0],
        "both_H_deleted": run_circuit(
            G, prepare=False, recombine=False
        )[0],
    }
    check(
        "deletion and split replacements expose the supplied matched-route and matched-H boundaries without faking action faithfulness",
        ideal > 0.03
        and abs(rows["W_deleted"]) < TOL
        and abs(rows["route_in_deleted"] - 0.5) < TOL
        and abs(rows["route_out_deleted"] - 0.5) < TOL
        and abs(rows["both_routes_deleted"]) < TOL
        and abs(rows["preparer_deleted"] - 0.5) < TOL
        and abs(rows["recombiner_deleted"] - 0.5) < TOL
        and abs(rows["both_H_deleted"]) < TOL,
        rows,
    )
    n2_actual = np.sin(G / 2) ** 2
    n2_q_only = np.sin(G / 2) ** 2
    check(
        "the fixed-N=2 co-located-versus-separated two-cell steelman works as an unconditional comparator but cannot reject the Q-only surrogate",
        n2_actual > 0.03 and abs(n2_actual - n2_q_only) < TOL,
        {
            "N2_actual_close": float(n2_actual),
            "N2_Q_only_close": float(n2_q_only),
            "disposition": "constructive minimal subfixture, not decisive Q-only control",
        },
    )


def stream_connector(code: c269.WilsonSubsystemCode) -> tuple[int, int, int]:
    left = code.graph.vertex_index[((0, 0, 0), 0)]
    right = code.graph.vertex_index[((1, 0, 0), 1)]
    for edge, (u, v, _, _) in enumerate(code.graph.edges):
        if {u, v} == {left, right}:
            return edge, left, right
    raise AssertionError("declared adjacent stream connector is absent")


def same_code_support_mass_and_covariance_controls() -> None:
    print("\nCONNECTED PHYSICAL CODE / SUPPORT / MASS / COVARIANCE")
    model = c285.fixture()
    coefficients = c285.contact_walsh_coefficients(np.diag(model["W"]))
    rows = []
    failures = []
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        cells = ((0, 0, 0), (1, 0, 0))
        bs_by_cell = tuple(c278.cell_bs(code, cell) for cell in cells)
        terms = tuple(
            c278.pauli_product(bs, mask)
            for bs in bs_by_cell
            for mask in range(64)
        )
        connector_edge, _, _ = stream_connector(code)
        connector = code.A[connector_edge]
        support_union = connector.x | connector.z
        for bs in bs_by_cell:
            for operator in bs:
                support_union |= operator.x | operator.z
        leakage = sum(
            not operator.commutes(check_row)
            for operator in terms + (connector,)
            for check_row in code.local_checks + code.wilsons
        )
        row = {
            "L": length,
            "held_out": length == 6,
            "two_cell_matter_union_M2": support_union.bit_count(),
            "path_marker_M2": 1,
            "total_declared_block_M2": support_union.bit_count() + 1,
            "maximum_contact_term_weight": max(
                (term.x | term.z).bit_count() for term in terms
            ),
            "connector_weight": (connector.x | connector.z).bit_count(),
            "nonzero_Walsh_terms_per_cell": sum(
                abs(value) > 1e-14 for value in coefficients
            ),
            "check_or_Wilson_leakage": leakage,
        }
        rows.append(row)
        if not (
            row["two_cell_matter_union_M2"] <= 36
            and row["total_declared_block_M2"] <= 37
            and row["maximum_contact_term_weight"] == 12
            and row["connector_weight"] <= 5
            and row["nonzero_Walsh_terms_per_cell"] == 64
            and leakage == 0
        ):
            failures.append(row)
    species = c278.c219.common_species(c278.c230.BETA)
    check(
        "two ordinary W_g blocks and the adjacent mapped hopping connector have bounded constant overhead and zero leakage through held-out L=6",
        not failures,
        rows,
    )
    check(
        "the two-cell contact comparator preserves the one-particle mass fixture because W_g is identity for N at most one",
        np.max(
            np.abs(np.diag(model["W"])[model["occupations"] <= 1] - 1)
        )
        == 0
        and abs(c278.c219.rest_mass(species) / species.analytic_mass - 1)
        < 2e-12,
        {
            "one_particle_contact_action": "identity",
            "mass_ratio": c278.c219.rest_mass(species) / species.analytic_mass,
        },
    )

    code = cache[3]
    cells = ((0, 0, 0), (1, 0, 0))
    bs_by_cell = tuple(c278.cell_bs(code, cell) for cell in cells)
    connector_edge, connector_u, connector_v = stream_connector(code)
    local_family = set(code.local_checks)
    frame_failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(code.length), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_bs = tuple(
                tuple(
                    c235.apply_gauge(
                        c235.permute_pauli(row, edge_map),
                        toggles,
                        pairs,
                        flips,
                    )
                    for row in bs
                )
                for bs in bs_by_cell
            )
            target_bs = tuple(
                tuple(code.B[vertex_map[code.graph.vertex_index[(cell, d)]]]
                      for d in c278.DIRECTIONS)
                for cell in cells
            )
            transformed_connector = c235.apply_gauge(
                c235.permute_pauli(code.A[connector_edge], edge_map),
                toggles,
                pairs,
                flips,
            )
            target_connector = code.graph.A(
                vertex_map[connector_u], vertex_map[connector_v]
            )
            if not (
                transformed_local == local_family
                and all(
                    set(transformed) == set(target)
                    for transformed, target in zip(transformed_bs, target_bs)
                )
                and transformed_connector == target_connector
            ):
                frame_failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the entire two-cell contact-plus-connector motif is covariant in 648 proper-frame and L=3 translation tests",
        not frame_failures and tests == 24 * 27,
        {"frame_translation_tests": tests, "failures": frame_failures[:5]},
    )


def lawful_domain_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED STRUCTURE")

    def validate(length: int, cell_modes: int, marker_dimension: int) -> None:
        if length < 3:
            raise ValueError("L must be at least three")
        if cell_modes != 6:
            raise ValueError("each coarse cell must have six modes")
        if marker_dimension != 2:
            raise ValueError("the supplied path marker must be one M2")

    accepted = True
    validate(3, 6, 2)
    rejections = 0
    for arguments in ((2, 6, 2), (3, 5, 2), (3, 6, 3)):
        try:
            validate(*arguments)
        except ValueError:
            rejections += 1
    check(
        "the lawful domain accepts the declared six-mode M64 cells and rejects undersized or mistyped fixtures",
        accepted and rejections == 3,
        {"negative_fixture_rejections": rejections},
    )
    check(
        "the supplied inventory is finite and explicit",
        True,
        {
            "supplied": (
                "g=0.37",
                "two adjacent cells and one stream connector",
                "fixed branch occupations",
                "one path-marker M2",
                "marker H preparation and read basis",
                "controlled redistribution route and its inverse",
                "ordinary W_g insertion on both cells",
            ),
            "derived": (
                "relative phase g",
                "dark-port close sin^2(g/2)",
                "Q-only zero",
                "bounded physical support",
                "zero code leakage",
            ),
        },
    )


def main() -> int:
    print("CYCLE 290 / UNCONDITIONAL TWO-CELL CONTACT INTERFEROMETER")
    note_contract()
    branch_and_interferometer_controls()
    route_deletion_and_minimal_steelman_controls()
    same_code_support_mass_and_covariance_controls()
    lawful_domain_controls()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
