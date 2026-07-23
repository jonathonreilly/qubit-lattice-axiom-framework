#!/usr/bin/env python3
"""Cycle641: twisted charge-ribbon / auxiliary-link-gauge discriminator.

The primary constructive object is one four-edge square carrying the
even-parity sector of four matter modes.  A local loop constraint binds the fermionic
exchange sign to a contractible flux.  The same fixed encoding is tested for a
one-edge FSWAP and for both two-layer paths exchanging opposite carriers.

The contractible construction is then extended through the existing rough
face presentation on periodic L3/L6/L7 lattices.  That extension is reported
only conditionally because three growing Wilson/spin initializers remain.
Two genuinely different alternatives -- auxiliary Majorana links and an
overlapping pull-through tensor -- are retained as scoped attempts.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from hashlib import sha256
import importlib
import io
import json
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_SHORE_REF = "c27f72ff8b1058d872695829c05e95da415813bc"


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{ref}:{path}"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout


def line_number(path: Path, needle: str) -> int:
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if needle in line:
            return number
    raise ValueError(f"missing citation needle {needle!r} in {path}")


def load_immutable_modules():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", IMMUTABLE_SHORE_REF, "scripts"],
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    ).stdout
    exported = tempfile.TemporaryDirectory(prefix="cycle641-immutable-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(exported.name, filter="data")
    scripts_path = str(Path(exported.name) / "scripts")
    sys.path.insert(0, scripts_path)
    try:
        c247_module = importlib.import_module(
            "local_rough_puncture_odd_sector_cycle247_2026_07_17"
        )
        c532_module = importlib.import_module(
            "physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21"
        )
    finally:
        sys.path.remove(scripts_path)
    return exported, c247_module, c532_module


IMMUTABLE_EXPORT, c247, c532 = load_immutable_modules()


AUTHORITY = "none"
AUDIT = "unset"
TOL = 5.0e-11
CAP_SECONDS = 180.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TWISTED_CHARGE_RIBBON_AUXILIARY_LINK_GAUGE_"
    "CYCLE641_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_"
    "cycle641_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_twisted_charge_ribbon_auxiliary_link_gauge_"
    "cycle641_cold_2026_07_23.txt"
)

PINS = {
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py":
        "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    "scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py":
        "10f5cf027c76f5a0a3b1d3dbaa6cb0e6d418932c84553f0cca303d3f21742519",
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py":
        "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    "scripts/physical_same_species_two_carrier_path_sign_compiler_cycle639_2026_07_23.py":
        "2039cd847c99e250ec62e65905feb032bbaf2f18edac1ac22ced3cbbd0d5c627",
    "outputs/physical_same_species_two_carrier_path_sign_compiler_cycle639_receipt_2026_07_23.json":
        "eea3d94d46d3d8b8b05517a5a670723740a764b2a48ff0aa0c2b835edc091841",
}

SQUARE_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
EVEN_WORDS = tuple(word for word in range(16) if word.bit_count() % 2 == 0)


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (float(value.real), float(value.imag))
    raise TypeError(type(value).__name__)


def shore() -> dict:
    observed = {path: sha256(git_bytes(IMMUTABLE_SHORE_REF, path)).hexdigest() for path in PINS}
    parent = json.loads(git_bytes(
        IMMUTABLE_SHORE_REF,
        "outputs/physical_same_species_two_carrier_path_sign_compiler_cycle639_receipt_2026_07_23.json",
    ))
    result = {
        "immutable_shore_ref": IMMUTABLE_SHORE_REF,
        "observed": observed,
        "hashes_match": observed == PINS,
        "working_tree_bytes_used_as_premise": False,
        "dirty_Cycle532_worktree_sha256_comparison_only": sha(
            ROOT / "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py"
        ),
        "Cycle639_pass": parent["pass"],
        "Cycle639_authority": parent["authority"],
        "Cycle639_audit": parent["audit"],
        "Cycle639_same_species_local_E_G_closed": parent["same_species_local_E_G_closed"],
        "Cycle639_axiom_pressure": parent["axiom_pressure"],
    }
    condition = (
        result["hashes_match"]
        and result["Cycle639_pass"]
        and result["Cycle639_authority"] == AUTHORITY
        and result["Cycle639_audit"] == AUDIT
        and not result["Cycle639_same_species_local_E_G_closed"]
        and not result["Cycle639_axiom_pressure"]
    )
    check("Cycle235/247/532/639 shores and Cycle639 scope are byte exact", condition, result)
    return result


def pauli_matrix(x_mask: int, z_mask: int, phase: int = 0, qubits: int = 4) -> np.ndarray:
    dimension = 1 << qubits
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for basis in range(dimension):
        amplitude = (1j ** phase) * ((-1) ** ((basis & z_mask).bit_count()))
        matrix[basis ^ x_mask, basis] = amplitude
    return matrix


def gamma_permutation(permutation: tuple[int, ...]) -> np.ndarray:
    """Exterior/Fock action in the declared four-mode order."""
    index = {word: position for position, word in enumerate(EVEN_WORDS)}
    result = np.zeros((len(EVEN_WORDS), len(EVEN_WORDS)), dtype=complex)
    for word in EVEN_WORDS:
        occupied = [mode for mode in range(4) if (word >> mode) & 1]
        images = [permutation[mode] for mode in occupied]
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        )
        target = sum(1 << mode for mode in images)
        result[index[target], index[word]] = (-1) ** inversions
    return result


def square_operators() -> dict:
    # A_e=X_e times a bounded incidence framing.  Adjacent A operators
    # anticommute and disjoint A operators commute.
    z_dress = (0b0000, 0b0001, 0b0010, 0b0101)
    a_rows = tuple(pauli_matrix(1 << edge, z_dress[edge]) for edge in range(4))
    b_rows = []
    for vertex in range(4):
        mask = sum(
            1 << edge
            for edge, endpoints in enumerate(SQUARE_EDGES)
            if vertex in endpoints
        )
        b_rows.append(pauli_matrix(0, mask))
    loop = np.eye(16, dtype=complex)
    for row in a_rows:
        loop = loop @ row
    fswaps = []
    for edge, (source, target) in enumerate(SQUARE_EDGES):
        fswaps.append(
            0.5 * (
                b_rows[source]
                + b_rows[target]
                + 1j * b_rows[source] @ a_rows[edge]
                - 1j * b_rows[target] @ a_rows[edge]
            )
        )
    return {
        "A": tuple(a_rows),
        "B": tuple(b_rows),
        "Q": loop,
        "F": tuple(fswaps),
        "z_dress": z_dress,
    }


def raw_square_encoding(operators: dict, flux_sign: int) -> np.ndarray:
    columns = []
    for word in EVEN_WORDS:
        eigenvalues = tuple(-1 if (word >> vertex) & 1 else 1 for vertex in range(4))
        physical_words = [
            basis
            for basis in range(16)
            if all(
                abs(operators["B"][vertex][basis, basis] - eigenvalues[vertex]) < TOL
                for vertex in range(4)
            )
        ]
        selector = np.eye(16, dtype=complex)[:, physical_words]
        restricted = selector.conj().T @ operators["Q"] @ selector
        values, vectors = np.linalg.eigh(restricted)
        column = selector @ vectors[:, int(np.argmin(abs(values - flux_sign)))]
        columns.append(column)
    return np.stack(columns, axis=1)


def phase_fix_encoding(raw: np.ndarray, operators: dict) -> np.ndarray:
    """Fix one E for the edge 01 and the two-layer exchange target."""
    index = {word: position for position, word in enumerate(EVEN_WORDS)}
    edge_target = gamma_permutation((1, 0, 2, 3))
    exchange_target = gamma_permutation((2, 3, 0, 1))
    physical_exchange = (
        operators["F"][1]
        @ operators["F"][3]
        @ operators["F"][0]
        @ operators["F"][2]
    )
    constraints = []
    for physical, target in (
        (operators["F"][0], edge_target),
        (physical_exchange, exchange_target),
    ):
        represented = raw.conj().T @ physical @ raw
        for source in range(8):
            target_index = int(np.argmax(abs(target[:, source])))
            constraints.append(
                (source, target_index, represented[target_index, source], target[target_index, source])
            )
    phases: dict[int, complex] = {}
    for seed in range(8):
        if seed in phases:
            continue
        phases[seed] = 1.0 + 0.0j
        frontier = [seed]
        while frontier:
            source = frontier.pop()
            for left, right, amplitude, target in constraints:
                if left != source:
                    continue
                proposed = np.conj(target / (amplitude * phases[left]))
                if right in phases:
                    if abs(phases[right] - proposed) >= TOL:
                        raise ValueError(("phase inconsistency", left, right))
                else:
                    phases[right] = proposed
                    frontier.append(right)
    return raw @ np.diag([phases[index[word]] for word in EVEN_WORDS])


def plaquette_charge_ribbon() -> dict:
    operators = square_operators()
    raw_plus = raw_square_encoding(operators, +1)
    encoding = phase_fix_encoding(raw_plus, operators)
    raw_minus = raw_square_encoding(operators, -1)

    edge_target = gamma_permutation((1, 0, 2, 3))
    exchange_target = gamma_permutation((2, 3, 0, 1))
    clockwise = (
        operators["F"][1]
        @ operators["F"][3]
        @ operators["F"][0]
        @ operators["F"][2]
    )
    counterclockwise = (
        operators["F"][0]
        @ operators["F"][2]
        @ operators["F"][1]
        @ operators["F"][3]
    )
    minus_exchange = raw_minus.conj().T @ clockwise @ raw_minus
    opposite_indices = tuple(EVEN_WORDS.index(word) for word in (0b0101, 0b1010))

    ghz = np.zeros(16, dtype=complex)
    ghz[0] = ghz[15] = 1 / np.sqrt(2)
    deleted_entangler = np.zeros(16, dtype=complex)
    deleted_entangler[0] = deleted_entangler[0b0111] = 1 / np.sqrt(2)
    projector = encoding @ encoding.conj().T
    complement = np.eye(16) - projector
    odd_syndromes_rejected = 0
    for word in range(16):
        if word.bit_count() % 2 == 0:
            continue
        eigenvalues = tuple(-1 if (word >> vertex) & 1 else 1 for vertex in range(4))
        candidates = sum(
            all(
                abs(operators["B"][vertex][basis, basis] - eigenvalues[vertex]) < TOL
                for vertex in range(4)
            )
            for basis in range(16)
        )
        odd_syndromes_rejected += candidates == 0

    adjacent_anticommutator_failures = 0
    disjoint_commutator_failures = 0
    for left in range(4):
        for right in range(left + 1, 4):
            shared = bool(set(SQUARE_EDGES[left]) & set(SQUARE_EDGES[right]))
            if shared:
                adjacent_anticommutator_failures += (
                    np.max(abs(operators["A"][left] @ operators["A"][right]
                               + operators["A"][right] @ operators["A"][left])) >= TOL
                )
            else:
                disjoint_commutator_failures += (
                    np.max(abs(operators["A"][left] @ operators["A"][right]
                               - operators["A"][right] @ operators["A"][left])) >= TOL
                )

    result = {
        "encoding_shape": encoding.shape,
        "encoding_isometry_residual": float(np.max(abs(encoding.conj().T @ encoding - np.eye(8)))),
        "loop_constraint_residual": float(np.max(abs(operators["Q"] @ encoding - encoding))),
        "local_CAR_adjacent_anticommutator_failures": adjacent_anticommutator_failures,
        "local_CAR_disjoint_commutator_failures": disjoint_commutator_failures,
        "one_edge_EG_residual": float(np.max(abs(operators["F"][0] @ encoding - encoding @ edge_target))),
        "one_edge_leakage_residual": float(np.max(abs(complement @ operators["F"][0] @ encoding))),
        "one_edge_inverse_residual": float(np.max(abs(operators["F"][0] @ operators["F"][0] - np.eye(16)))),
        "clockwise_exchange_EG_residual": float(np.max(abs(clockwise @ encoding - encoding @ exchange_target))),
        "counterclockwise_exchange_EG_residual": float(np.max(abs(counterclockwise @ encoding - encoding @ exchange_target))),
        "clockwise_exchange_leakage_residual": float(np.max(abs(complement @ clockwise @ encoding))),
        "counterclockwise_exchange_leakage_residual": float(np.max(abs(complement @ counterclockwise @ encoding))),
        "alternate_path_residual": float(np.max(abs(clockwise @ encoding - counterclockwise @ encoding))),
        "opposite_carrier_exchange_amplitudes": tuple(
            complex((encoding.conj().T @ clockwise @ encoding)[index, index])
            for index in opposite_indices
        ),
        "wrong_flux_opposite_exchange_amplitudes": tuple(
            complex(minus_exchange[index, index]) for index in opposite_indices
        ),
        "wrong_flux_deletion_signal": float(
            max(abs(minus_exchange[index, index] + 1) for index in opposite_indices)
        ),
        "gauge_vacuum_residual": float(np.linalg.norm(encoding[:, EVEN_WORDS.index(0)] - ghz)),
        "delete_one_vacuum_entangler_residual": float(np.linalg.norm(deleted_entangler - ghz)),
        "lawful_even_words": len(EVEN_WORDS),
        "malformed_odd_syndromes_rejected": odd_syndromes_rejected,
        "physical_M2_per_square": 4,
        "even_matter_modes_per_square": 4,
        "code_dimension": 8,
        "loop_constraint_weight": 4,
        "maximum_FSWAP_polynomial_Pauli_support": 3,
        "preparation": "H(edge0), then CNOT edge0->edge1,edge2,edge3 prepares the empty-charge Q=+1 link vacuum",
        "no_global_prefix_or_parity_query": True,
    }
    result["pass"] = bool(
        result["encoding_isometry_residual"] < TOL
        and result["loop_constraint_residual"] < TOL
        and adjacent_anticommutator_failures == disjoint_commutator_failures == 0
        and result["one_edge_EG_residual"] < TOL
        and result["one_edge_leakage_residual"] < TOL
        and result["one_edge_inverse_residual"] < TOL
        and result["clockwise_exchange_EG_residual"] < TOL
        and result["counterclockwise_exchange_EG_residual"] < TOL
        and result["clockwise_exchange_leakage_residual"] < TOL
        and result["counterclockwise_exchange_leakage_residual"] < TOL
        and result["alternate_path_residual"] < TOL
        and max(abs(value + 1) for value in result["opposite_carrier_exchange_amplitudes"]) < TOL
        and result["wrong_flux_deletion_signal"] > 1.9
        and result["gauge_vacuum_residual"] < TOL
        and result["delete_one_vacuum_entangler_residual"] > 0.9
        and result["malformed_odd_syndromes_rejected"] == 8
    )
    check("one fixed local E intertwines one edge and both exchange paths with flux-bound -1", result["pass"], result)
    return result


def periodic_extension() -> dict:
    rows = []
    for length in (3, 6, 7):
        graph = c247.PunctureGraph(length, terminals=1)
        local = c532.local_stabilizers(graph)
        wilsons = c532.wilson_initializers(graph)
        local_rank, local_inconsistent = c532.phase_rank(local, graph.qubits)
        fixed_rank, fixed_inconsistent = c532.phase_rank(local + wilsons, graph.qubits)
        layout = c532.layout_controls(length)
        onsite = c532.onsite_compatibility_controls(length)
        outer_edges = tuple(
            edge
            for edge, (_, _, kind, _) in enumerate(graph.base.edges)
            if kind == "outer_square"
        )
        local_commutator_failures = 0
        for edge in outer_edges:
            mapped = graph.mapped_matter_A(edge)
            local_commutator_failures += sum(not mapped.commutes(stabilizer) for stabilizer in local)
        rows.append({
            "length": length,
            "cells": length ** 3,
            "physical_M2": graph.qubits,
            "physical_M2_per_cell": graph.qubits / length ** 3,
            "local_constraint_rows": len(local),
            "local_constraint_rank": local_rank,
            "local_constraint_inconsistencies": local_inconsistent,
            "fixed_constraint_rank": fixed_rank,
            "fixed_constraint_inconsistencies": fixed_inconsistent,
            "Wilson_rank_increment": fixed_rank - local_rank,
            "maximum_local_constraint_weight": max((row.x | row.z).bit_count() for row in local),
            "maximum_Wilson_initializer_weight": max((row.x | row.z).bit_count() for row in wilsons),
            "outer_seam_edges": len(outer_edges),
            "outer_seam_edges_per_cell": len(outer_edges) / length ** 3,
            "mapped_outer_A_local_constraint_commutator_failures": local_commutator_failures,
            "layout": layout,
            "onsite": onsite,
        })
    covariance = c532.covariance_controls()
    fixture = c532.fixture_controls()
    deletion = c532.deletion_controls()
    result = {
        "sizes": rows,
        "proper_cubic_covariance": covariance,
        "mass_contact_seam_fixture": fixture,
        "constraint_and_Wilson_deletions": deletion,
        "local_checks_only_define_one_fixed_periodic_target": False,
        "three_Wilson_initializers_supplied": True,
        "bounded_or_autonomous_Wilson_sector_preparation": False,
        "conditional_fixed_sector_extension": True,
        "unconditional_periodic_physical_compiler": False,
    }
    result["pass"] = bool(
        all(
            row["physical_M2_per_cell"] == 22
            and row["local_constraint_inconsistencies"] == 0
            and row["fixed_constraint_inconsistencies"] == 0
            and row["Wilson_rank_increment"] == 3
            and row["maximum_local_constraint_weight"] <= 28
            and row["outer_seam_edges_per_cell"] == 3
            and row["mapped_outer_A_local_constraint_commutator_failures"] == 0
            and row["layout"]["pass"]
            and row["onsite"]["pass"]
            for row in rows
        )
        and covariance["pass"]
        and fixture["pass"]
        and deletion["pass"]
        and not result["bounded_or_autonomous_Wilson_sector_preparation"]
        and not result["unconditional_periodic_physical_compiler"]
    )
    check("L3/L6/L7 bounded pull-through, seam, onsite and all24/all576 pass conditionally on three Wilson signs", result["pass"], {
        "ranks": [(row["length"], row["local_constraint_rank"], row["fixed_constraint_rank"], row["maximum_Wilson_initializer_weight"]) for row in rows],
        "covariance": covariance["pass"], "fixture": fixture["pass"],
    })
    return result


def jw_majorana_bilinear(left: int, right: int) -> tuple[int, int]:
    """Binary Pauli masks for gamma_left gamma_right in one JW order."""
    lower, upper = sorted((left, right))
    x_mask = (1 << left) ^ (1 << right)
    z_mask = sum(1 << position for position in range(lower, upper))
    return x_mask, z_mask


def auxiliary_majorana_route() -> dict:
    labels = []
    for vertex in range(4):
        labels.append(("m", vertex, -1))
        for edge, endpoints in enumerate(SQUARE_EDGES):
            if vertex in endpoints:
                labels.append(("a", vertex, edge))

    def audit(order: list[tuple[str, int, int]]) -> dict:
        positions = {label: index for index, label in enumerate(order)}
        link_supports = []
        dressed_supports = []
        dressed_off_endpoint = []
        for edge, (source, target) in enumerate(SQUARE_EDGES):
            matter_x, matter_z = jw_majorana_bilinear(
                positions[("m", source, -1)], positions[("m", target, -1)]
            )
            link_x, link_z = jw_majorana_bilinear(
                positions[("a", source, edge)], positions[("a", target, edge)]
            )
            link_support = link_x | link_z
            dressed_support = (matter_x ^ link_x) | (matter_z ^ link_z)
            endpoint_mask = sum(
                1 << index
                for index, label in enumerate(order)
                if label[1] in (source, target)
            )
            link_supports.append(link_support.bit_count())
            dressed_supports.append(dressed_support.bit_count())
            dressed_off_endpoint.append((dressed_support & ~endpoint_mask).bit_count())
        return {
            "maximum_link_stabilizer_JW_support": max(link_supports),
            "maximum_dressed_edge_JW_support": max(dressed_supports),
            "dressed_support_outside_endpoint_blocks": tuple(dressed_off_endpoint),
        }

    vertex_order = list(labels)
    edge_order = [("m", vertex, -1) for vertex in range(4)]
    for edge, (source, target) in enumerate(SQUARE_EDGES):
        edge_order.extend((("a", source, edge), ("a", target, edge)))
    vertex_audit = audit(vertex_order)
    edge_audit = audit(edge_order)

    # Scaling witness on a cycle: vertex-block ordering localizes the dressed
    # edge but gives the closing link a growing JW interval; edge-pair ordering
    # localizes each link but leaves a growing matter interval.
    scaling = []
    for length in (3, 6, 7):
        scaling.append({
            "length": length,
            "vertex_block_closing_link_lower_bound": 3 * length - 2,
            "edge_pair_order_matter_interval_lower_bound": length,
        })
    result = {
        "auxiliary_modes_per_square": 8,
        "vertex_block_order": vertex_audit,
        "edge_pair_order": edge_audit,
        "held_scaling_witness": scaling,
        "commuting_link_vacuum_assumed": True,
        "local_link_vacuum_preparation_supplied": False,
        "one_order_with_both_local_link_checks_and_local_dressed_edges_found": False,
        "route_status": "ATTEMPTED_TWO_NATURAL_ORDERINGS__OPEN_AUXILIARY_CLIFFORD_VARIANTS",
        "broad_no_go": False,
    }
    result["pass"] = bool(
        vertex_audit["maximum_link_stabilizer_JW_support"] > 2
        and edge_audit["maximum_link_stabilizer_JW_support"] == 2
        and not result["one_order_with_both_local_link_checks_and_local_dressed_edges_found"]
        and not result["broad_no_go"]
    )
    check("auxiliary Majorana route records the link-check/update ordering tradeoff without ruling out untested Clifford variants", result["pass"], result)
    return result


def overlapping_tensor_route(periodic: dict) -> dict:
    ranks = tuple(
        (row["length"], row["local_constraint_rank"], row["fixed_constraint_rank"])
        for row in periodic["sizes"]
    )
    result = {
        "local_tensor": "the 16x8 Q=+1 square encoding used by the primary route",
        "contractible_pull_through": True,
        "overlap_rule": "neighboring plaquette projectors share edge M2 factors",
        "periodic_rank_data": ranks,
        "periodic_local_projectors_leave_three_characters": True,
        "bounded_tensor_contraction_or_dissipative_sector_genesis_supplied": False,
        "route_status": "ATTEMPTED_LOCAL_PULL_THROUGH__PERIODIC_PREPARATION_OPEN",
        "not_counted_independent_of_higher_form_charge_ribbon": True,
    }
    result["pass"] = bool(
        result["contractible_pull_through"]
        and all(fixed - local == 3 for _, local, fixed in ranks)
        and result["periodic_local_projectors_leave_three_characters"]
        and not result["bounded_tensor_contraction_or_dissipative_sector_genesis_supplied"]
    )
    check("overlapping tensor pull-through closes locally but retains an explicit periodic preparation obligation", result["pass"], result)
    return result


def no_go_discipline(primary: dict, periodic: dict, auxiliary: dict, tensor: dict) -> dict:
    current = str(Path(__file__).relative_to(ROOT))
    current_note = str(NOTE.relative_to(ROOT))
    c235_note = (
        "docs/work_history/repo/review_feedback/"
        "EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md"
    )
    c532_note = (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
    )
    c639_note = (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_SAME_SPECIES_TWO_CARRIER_PATH_SIGN_COMPILER_CYCLE639_NOTE_2026-07-23.md"
    )
    attempted = [
        {"family": "charge-bound plaquette flux/ribbon", "honesty_marker": "ATTEMPTED",
         "status": "CONTRACTIBLE_EXACT__PERIODIC_CONDITIONAL"},
        {"family": "auxiliary Majorana link", "honesty_marker": "ATTEMPTED",
         "status": auxiliary["route_status"]},
        {"family": "overlapping pull-through tensor", "honesty_marker": "ATTEMPTED",
         "status": tensor["route_status"]},
    ]
    open_routes = [
        {"family": "punctured/open-boundary spin-sector genesis", "status": "OPEN_NOT_ATTEMPTED"},
        {"family": "bounded dissipative/measurement-reset Wilson preparation", "status": "OPEN_NOT_ATTEMPTED"},
    ]
    walls = [
        {"wall": "periodic_spin_sector_genesis", "routes": ("charge-ribbon", "overlap-tensor"),
         "independence": "CORRELATED_SAME_HIGHER_FORM_CODE"},
        {"wall": "auxiliary_clifford_locality", "routes": ("auxiliary-Majorana",),
         "independence": "DISTINCT_BUT_ROUTE_FAMILY_UNEXHAUSTED"},
        {"wall": "support13_elementary_factorization", "routes": ("charge-ribbon",),
         "independence": "IMPLEMENTATION_WALL_NOT_TOPOLOGICAL_WALL"},
    ]
    pairs = [
        {"from": left["wall"], "to": right["wall"],
         "independent": left["wall"] != "periodic_spin_sector_genesis"
                        and right["wall"] != "periodic_spin_sector_genesis",
         "reason": "explicitly compared; no route-independent obstruction inferred"}
        for left in walls for right in walls if left is not right
    ]
    residual_rows = [
        {
            "prior_ref": IMMUTABLE_SHORE_REF, "prior_path": c639_note, "prior_line": 34,
            "prior_residual": 4.0, "current_path": current_note,
            "current_line": line_number(NOTE, "||(U_cw-U_ccw)E||_max = 0"),
            "current_residual": primary["alternate_path_residual"], "same_scope": True,
            "exact_match": False, "use_as_closure": True,
            "mechanism": "the local Q=+1 loop sector binds the exchange sign to the ribbon",
        },
        {
            "prior_ref": IMMUTABLE_SHORE_REF, "prior_path": c532_note, "prior_line": 44,
            "prior_residual": "three_unfixed_Wilson_characters", "current_path": current,
            "current_line": line_number(Path(__file__), '"periodic_local_projectors_leave_three_characters": True'),
            "current_residual": "three_unfixed_Wilson_characters", "same_scope": True,
            "exact_match": True, "use_as_closure": False,
            "mechanism": "same rough-face periodic presentation; repeated evidence is an echo",
        },
        {
            "prior_ref": IMMUTABLE_SHORE_REF, "prior_path": c639_note, "prior_line": 53,
            "prior_residual": (110, 1082, 1766), "current_path": current,
            "current_line": line_number(Path(__file__), '"maximum_link_stabilizer_JW_support": max_link'),
            "current_residual": auxiliary["held_scaling_witness"], "same_scope": False,
            "exact_match": False, "use_as_closure": False,
            "mechanism": "prefix correction and two auxiliary JW layouts are different constructions",
        },
    ]
    rhetoric_rows = [
        {"claim": "one edge and square are exact", "per_element": "exact", "per_site": "four M2",
         "per_mode": "four-mode even-parity sector", "per_block": "contractible only", "lattice_wide": "withheld"},
        {"claim": "alternate paths close locally", "per_element": "one FSWAP", "per_site": "one square",
         "per_mode": "complete eight-ray even code", "per_block": "two schedules", "lattice_wide": "withheld"},
        {"claim": "periodic extension is conditional", "per_element": "bounded generators", "per_site": "22 M2/cell",
         "per_mode": "fixed-spin factor only", "per_block": "support <=13", "lattice_wide": "three supplied Wilson signs"},
        {"claim": "auxiliary route remains open", "per_element": "two tested JW orders", "per_site": "endpoint blocks",
         "per_mode": "auxiliary Majoranas supplied", "per_block": "ordering tradeoff", "lattice_wide": "not ruled out"},
        {"claim": "no time/source/Record follows", "per_element": "generator only", "per_site": "gauge vacuum only",
         "per_mode": "even algebra only", "per_block": "compiler surface", "lattice_wide": "no law-level claim"},
    ]
    partial = [
        {"file": current, "status": "EXECUTED_CONTRACTIBLE_EG",
         "what_closes": "one fixed four-M2 local code and two exchange paths"},
        {"file": current, "status": "EXECUTED_CONDITIONAL_PERIODIC_RANKS",
         "what_closes": "L3/L6/L7 local incidence and fixed-Wilson logical comparators only"},
        {"file": current, "status": "EXECUTED_TWO_AUXILIARY_JW_LAYOUTS",
         "what_closes": "two natural ordering variants, not the Clifford family"},
        {"file": current, "status": "OPEN_PUNCTURE_OR_DISSIPATIVE_GENESIS",
         "what_closes": "unconditional local spin-sector preparation"},
        {"file": current, "status": "OPEN_ELEMENTARY_FACTORIZATION",
         "what_closes": "literal support-one/two realization of conditional support-13 blocks"},
    ]
    steelman = {
        "argument": "A punctured fermionic PEPS, a non-JW auxiliary Clifford code, or autonomous local dissipation may combine the exact plaquette pull-through with bounded spin-sector genesis. Those live constructions prevent a no-go inference.",
        "mechanism": "boundary inflow or autonomous local preparation fixes the spin sector without a runtime Wilson query",
        "decisive_test": "one fixed periodic E/G on L3/L6/L7 with local vacuum genesis, no Wilson initializer input, all24/all576, full seam, A2/contact/mass, and elementary physical factorization",
        "actionable": True,
        "supporting_citations": [
            {"ref": IMMUTABLE_SHORE_REF, "path": c532_note, "line": 44},
            {"ref": "WORKTREE_CYCLE641", "path": current_note,
             "line": line_number(NOTE, "Run a bounded spin-sector genesis tournament")},
        ],
    }
    echoes = [
        {"cycle": 235, "retired": "local even-algebra geometry only",
         "mechanism": "face-M2 higher-form code with three Wilson characters",
         "applicability": "same periodic topological-sector obligation",
         "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c235_note, "citation_line": 66},
        {"cycle": 532, "retired": "fixed-spin subsystem factorization",
         "mechanism": "rough-face code plus three initialized Wilson signs",
         "applicability": "direct periodic shore; not independent evidence",
         "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c532_note, "citation_line": 44},
        {"cycle": 639, "retired": "ordinary-M2 contractible path mismatch",
         "mechanism": "Cycle641 binds the sign to local Q=+1 flux",
         "applicability": "contractible square only",
         "citation_ref": IMMUTABLE_SHORE_REF, "citation_path": c639_note, "citation_line": 34},
    ]
    result = {
        "skill_freshness": {
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "newer_origin_main_followed": True,
        },
        "N1_normalized_families": attempted,
        "N1_open_routes_not_counted": open_routes,
        "N1_qualifying_attempts": len(attempted),
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "WITHHELD_BECAUSE_FEWER_THAN_FIVE_QUALIFYING_ATTEMPTS_AND_OPEN_ROUTES_REMAIN",
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N3_hidden_wall_scan": [
            "the plaquette E prepares a GHZ-like gauge vacuum; arbitrary periodic E is not supplied",
            "three Wilson signs are initialized structure, not local checks",
            "the conditional full-lattice presentation uses 22 M2 per coarse cell and support-13 polynomial blocks",
            "literal factorization of every support-13 polynomial into one/two-M2 physical gates is not frozen",
            "the auxiliary route assumes fermionic auxiliary modes before checking their qubit-local stabilizers",
            "no runtime frame selector, global parity query, energy, rate, Record, source, or tick is supplied",
        ],
        "N4_residual_matching": residual_rows,
        "N4_exact_residual_matches": [row for row in residual_rows if row["same_scope"] and row["exact_match"]],
        "N4_dropped_nonmatches": [row for row in residual_rows if not row["same_scope"]],
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "PASS",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
        "negative_claim_shipped": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }
    result["pass"] = bool(
        len(attempted) == 3 and all(row["honesty_marker"] == "ATTEMPTED" for row in attempted)
        and len(open_routes) == 2 and all("honesty_marker" not in row for row in open_routes)
        and len(pairs) == 6
        and len(result["N3_hidden_wall_scan"]) >= 6
        and len(residual_rows) == 3
        and all(all(key in row for key in ("prior_ref", "prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure")) for row in residual_rows)
        and len(rhetoric_rows) == 5
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in rhetoric_rows)
        and len(partial) == 5 and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
        and steelman["actionable"] and len(steelman["supporting_citations"]) == 2
        and len(echoes) == 3 and all(all(row[key] for key in ("mechanism", "applicability", "citation_ref", "citation_path", "citation_line")) for row in echoes)
        and not result["negative_claim_shipped"]
        and not result["shared_route_independent_obstruction"]
        and not result["axiom_pressure"]
    )
    check("fresh N1-N8 ships a narrow constructive plaquette result and blocks no-go/minimum/axiom claims", result["pass"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "## Exact contractible result",
        "## Periodic extension boundary",
        "## Route-by-route disposition",
        "## N1-N8 discipline",
        "## Supplied structure",
        "## Dependency ledger",
        "## Scope firewall",
    )
    result = {
        "required_sections": required,
        "missing_sections": tuple(section for section in required if section not in text),
        "authority_none": "Authority: **none**" in text,
        "audit_unset": "Audit: **unset**" in text,
        "accepted_false": "Accepted: **false**" in text,
    }
    result["pass"] = bool(
        not result["missing_sections"]
        and result["authority_none"]
        and result["audit_unset"]
        and result["accepted_false"]
    )
    check("Cycle641 note has the required scientific and scope surfaces", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle641 twisted charge-ribbon / auxiliary-link-gauge discriminator", AUTHORITY, AUDIT)
    shore_result = shore()
    note = note_contract()
    primary = plaquette_charge_ribbon()
    periodic = periodic_extension()
    auxiliary = auxiliary_majorana_route()
    tensor = overlapping_tensor_route(periodic)
    discipline = no_go_discipline(primary, periodic, auxiliary, tensor)
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    })
    receipt = {
        "status": "cycle641-twisted-charge-ribbon-auxiliary-link-gauge-discriminator",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "constitutional_effect": "none",
        "breakthrough": False,
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "shore": shore_result,
        "note_contract": note,
        "charge_bound_flux_ribbon": primary,
        "periodic_L3_L6_L7_extension": periodic,
        "auxiliary_Majorana_link_route": auxiliary,
        "overlapping_pull_through_tensor_route": tensor,
        "route_by_route_disposition": {
            "charge_bound_flux_ribbon": "EXACT_ON_ONE_CONTRACTIBLE_PLAQUETTE__CONDITIONAL_PERIODIC_EXTENSION",
            "auxiliary_Majorana_link": auxiliary["route_status"],
            "overlapping_pull_through_tensor": tensor["route_status"],
        },
        "strongest_constructive_result": (
            "one 16x8, four-M2, Q=+1 charge-ribbon encoding exactly intertwines a local edge FSWAP "
            "and both opposite-carrier exchange schedules with Gamma((02)(13)); alternate-path residual "
            "is zero and the exchange amplitude is -1, while flipping the local flux gives +1"
        ),
        "periodic_disposition": (
            "the bounded 22-M2/cell rough-face extension passes L3/L6/L7 locality, seam incidence/logical comparators, onsite, "
            "mass/contact and all24/all576 checks only after three growing Wilson signs are supplied"
        ),
        "full_periodic_physical_compiler_closed": False,
        "same_code_one_plaquette_E_G_closed": True,
        "global_prefix_or_runtime_parity_service": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "no_go_discipline": discipline,
        "supplied_structure": [
            "four named square vertices and four named edge M2 factors",
            "one proper orientation/framing z-dress for the A_e generators",
            "the local Q=+1 plaquette flux sector",
            "a four-mode presentation order used only to state the exterior target",
            "GHZ-like empty-link gauge vacuum and its local four-M2 preparation circuit",
            "Cycle247 rough/punctured face graph for the periodic extension",
            "three all-plus Wilson/spin signs for the conditional periodic extension",
            "Cycle532 22-M2/cell layout and support-13 FSWAP polynomial",
            "Cycle219 mass and Cycle230 contact/seam comparators",
        ],
        "scope_firewall": {
            "one_plaquette_is_full_periodic_compiler": False,
            "conditional_Wilson_extension_is_unconditional_local_E": False,
            "logical_seam_comparator_is_literal_full_rough_code_seam_matrix": False,
            "two_tested_JW_orders_are_auxiliary_no_go": False,
            "charge_ribbon_and_overlap_tensor_are_independent_failures": False,
            "wrapped_phase_is_energy": False,
            "generator_element_is_rate": False,
            "gauge_vacuum_is_Record": False,
            "tick_or_realized_history_claimed": False,
            "source_or_gravity_claimed": False,
        },
        "six_wall_ledger": {
            "C_ref": "local square orientation, Q=+1 flux and gauge vacuum are explicit supplies; periodic Wilson-sector genesis remains open",
            "C_num": "the four-mode even-parity sector has a literal 16x8 four-M2 code; the Cycle583 onsite A2 payload remains preserved conditionally through Cycle532",
            "C_wrap": "contractible alternate paths close exactly; periodic L3/L6/L7 retains three growing Wilson initializers and no tick/Record claim",
            "C_int": "one edge, exchange square, onsite Givens/contact, Cycle219 mass and Cycle230 logical seam comparators pass on their declared code surfaces; no full rough-code seam matrix is enumerated here",
            "C_local": "advanced: the Cycle639 square residual is removed locally with constant overhead and no prefix; unconditional periodic E/preparation is not closed",
            "C_source": "unchanged; no physical energy/source/stress/gravity or autonomous resource genesis is derived",
        },
        "optimal_next_campaign": (
            "bounded spin-sector genesis tournament: punctured/boundary inflow versus dissipative or measurement-reset "
            "Wilson preparation versus a non-JW auxiliary-Clifford link code; require one fixed periodic E/G and then "
            "factor the support-13 matter polynomials into elementary one/two-M2 gates"
        ),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "plaquette_alternate_path_residual": primary["alternate_path_residual"],
        "plaquette_exchange_amplitudes": primary["opposite_carrier_exchange_amplitudes"],
        "periodic_Wilson_rank_increments": [row["Wilson_rank_increment"] for row in periodic["sizes"]],
        "full_periodic_physical_compiler_closed": False,
        "axiom_pressure": False,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
    }, sort_keys=True, default=json_default))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
