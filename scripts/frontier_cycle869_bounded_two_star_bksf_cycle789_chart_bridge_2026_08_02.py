#!/usr/bin/env python3
"""Cycle869 bounded two-star BKSF/Cycle789 target-chart bridge.

The positive theorem in this runner is finite and local: the landed Cycle709
four-transvection Clifford exactly intertwines one Cycle703 OpenReference seam
character with a bounded PatchGraph-plus-rail character, and the complete
E/character/E^-1 word is compiled to literal returned nearest-neighbour M2
gates.  A two-star AB/BA interface is repaired by one exact landed rail
cleanup.

The stronger direct substitution into every Cycle789 global-JW target row is
an active route-specific discriminator.  Its nonzero held commutator-Gram
census forces the overall disposition to PARTIAL_EXECUTABLE_BRIDGE.  This is
not a no-go or an axiom-pressure claim.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle708_physical_endpoint_cube_core_2026_07_26 as G
import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as EG
import frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27 as R


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/BOUNDED_TWO_STAR_BKSF_CYCLE789_TARGET_CHART_BRIDGE_"
    "CYCLE869_BOUNDED_THEOREM_NOTE_2026-08-02.md"
)
TARGET_SPEC_PATH = (
    "docs/work_history/repo/review_feedback/BOUNDED_TWO_STAR_BKSF_"
    "CYCLE789_TARGET_CHART_BRIDGE_"
    "CYCLE869_TARGET_SPEC_2026-08-02.md"
)
EXPECTED_TARGET_SPEC_SHA256 = (
    "2220b3f4a35fa1ad80a9069c0c2436bd7418fc5c9896b0bc62974340fa0b05e9"
)
FROZEN_TARGET_SOURCE_COMMIT = "8622da346adf2db00f1e774faa63b542585353de"
PACKAGE_BASE_COMMIT = "1900b64260f39f075c59f2e353079c44e8ede031"
EXPECTED_LOADED_HELPER_COUNT = 45
EXPECTED_LOADED_HELPER_CLOSURE_SHA256 = (
    "41bb2d352bea3d43677b574fbf6cc111800590a344366ec4a60e1e708d233530"
)

PINNED_DIRECT_IMPORTS = {
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py":
        "102f8bc31e60fd4a452a1cfab176129f922665e10b564f0421dc26ffb11ee152",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py":
        "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py":
        "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py":
        "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py":
        "6a309f6449d155244b1dbee581cbe169937db5fe815c4dcc3e93929274a79004",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py":
        "dee1557eca4b88af75c469413290801577415cdf4ebfa3d970ceaa5ea15a2a8b",
}

AUDIT_INPUT_PATHS = (
    TARGET_SPEC_PATH,
    "docs/RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    *tuple(PINNED_DIRECT_IMPORTS),
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

Pauli = C.Pauli
Coord = tuple[int, int, int]
PRIMARY = (3, 2, 2)
HELD = (5, 3, 2)
TERM_INDEX = 2
TOL = 5.0e-10


def sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def loaded_helper_closure() -> dict[str, object]:
    """Pin every repo-local Python helper actually loaded by this runner."""

    runner = Path(__file__).resolve()
    rows: dict[str, str] = {}
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if not raw:
            continue
        try:
            path = Path(raw).resolve()
            relative = path.relative_to(ROOT)
        except (OSError, ValueError):
            continue
        if (
            relative.parts
            and relative.parts[0] == "scripts"
            and path.suffix == ".py"
            and path != runner
        ):
            rows[relative.as_posix()] = sha256_file(path)
    ordered = tuple(sorted(rows.items()))
    observed = sha256(json.dumps(
        ordered, separators=(",", ":")
    ).encode()).hexdigest()
    return {
        "expected_loaded_helper_count": EXPECTED_LOADED_HELPER_COUNT,
        "loaded_helper_count": len(ordered),
        "expected_closure_sha256": EXPECTED_LOADED_HELPER_CLOSURE_SHA256,
        "observed_closure_sha256": observed,
        "runner_path_excluded": str(runner.relative_to(ROOT)),
        "inventory": tuple(
            {"path": path, "sha256": digest_value}
            for path, digest_value in ordered
        ),
        "match": (
            len(ordered) == EXPECTED_LOADED_HELPER_COUNT
            and observed == EXPECTED_LOADED_HELPER_CLOSURE_SHA256
        ),
    }


def package_base_commit_certificate() -> dict[str, object]:
    """Require the declared package base when Git metadata is available."""

    metadata = subprocess.run(
        ("git", "-C", str(ROOT), "rev-parse", "--git-dir"),
        check=False,
        capture_output=True,
        text=True,
    ).returncode == 0
    exists = False
    if metadata:
        exists = subprocess.run(
            (
                "git", "-C", str(ROOT), "cat-file", "-e",
                f"{PACKAGE_BASE_COMMIT}^{{commit}}",
            ),
            check=False,
            capture_output=True,
            text=True,
        ).returncode == 0
    return {
        "named_package_base_commit": PACKAGE_BASE_COMMIT,
        "repository_has_git_metadata": metadata,
        "commit_object_exists": exists if metadata else None,
        "pass": not metadata or exists,
    }


def pinned_input_certificate() -> dict[str, object]:
    rows = []
    for relative, expected in PINNED_DIRECT_IMPORTS.items():
        path = ROOT / relative
        observed = sha256_file(path) if path.is_file() else None
        rows.append({
            "path": relative,
            "expected_sha256": expected,
            "observed_sha256": observed,
            "match": observed == expected,
        })
    target_observed = sha256_file(ROOT / TARGET_SPEC_PATH)
    closure = loaded_helper_closure()
    base = package_base_commit_certificate()
    return {
        "frozen_target_source_commit": FROZEN_TARGET_SOURCE_COMMIT,
        "package_base_commit": base,
        "direct_imports": tuple(rows),
        "direct_import_hash_failures": sum(not row["match"] for row in rows),
        "loaded_helper_closure": closure,
        "target_spec_path": TARGET_SPEC_PATH,
        "target_spec_expected_sha256": EXPECTED_TARGET_SPEC_SHA256,
        "target_spec_observed_sha256": target_observed,
        "target_spec_hash_match": target_observed == EXPECTED_TARGET_SPEC_SHA256,
    }


def note_contract() -> dict[str, object]:
    text = " ".join(
        (ROOT / NOTE_PATH).read_text(encoding="utf-8")
        .lower().replace("*", "").split()
    )
    required = (
        "authority: none",
        "audit: unset",
        "partial executable bridge",
        "39 code-placement m2",
        "40 declared bridge-register m2",
        "155 distinct routed-footprint locations",
        "120 to 119",
        "76 graph-edge and four rail",
        "24 proper-cubic frames",
        "576 ordered frame products",
        "supplied",
        "derived",
        "open",
        "no no-go",
    )
    missing = tuple(item for item in required if item not in text)
    return {"required_phrases": len(required), "missing": missing, "pass": not missing}


def fields(row) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def weight(row) -> int:
    return (row.x | row.z).bit_count()


def anticommutes(left, right) -> int:
    return ((left.x & right.z).bit_count() + (left.z & right.x).bit_count()) & 1


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def diameter(sites) -> int:
    sites = tuple(sites)
    return max((l1(left, right) for left in sites for right in sites), default=0)


def support_sites(row, sites: tuple[Coord, ...]) -> tuple[Coord, ...]:
    return tuple(
        site for index, site in enumerate(sites)
        if ((row.x | row.z) >> index) & 1
    )


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def to_b(row):
    return B.Pauli(row.phase, row.x, row.z)


def from_b(row) -> Pauli:
    return Pauli(row.phase, row.x, row.z)


def conjugate_s(row: Pauli, qubit: int, dagger: bool, width: int) -> Pauli:
    images = list(C.identity_images(width))
    bit = 1 << qubit
    images[qubit] = Pauli(3 if dagger else 1, bit, bit)
    return C.apply_images(tuple(images), row, width)


def instruction_family(kind: str) -> tuple[str, str | None]:
    if kind.endswith("_H") or kind in ("basis_H", "char_H"):
        return "H", None
    if "Sdg" in kind:
        return "Sdg", None
    if kind.endswith("_S") or kind in ("basis_S", "phase_S"):
        return "S", None
    if "CNOT" in kind or "CP_X" in kind:
        return "CP", "X"
    if "CP_Y" in kind:
        return "CP", "Y"
    if "CP_Z" in kind:
        return "CP", "Z"
    if "sign_Z" in kind:
        return "Z", None
    raise ValueError(("unknown Clifford instruction", kind))


def conjugate_instruction(row: Pauli, instruction, index, width: int) -> Pauli:
    family, letter = instruction_family(instruction.kind)
    wires = tuple(index[site] for site in instruction.sites)
    if family == "H":
        return from_b(B.conjugate_h(to_b(row), wires[0]))
    if family == "S":
        return conjugate_s(row, wires[0], False, width)
    if family == "Sdg":
        return conjugate_s(row, wires[0], True, width)
    if family == "Z":
        bit = 1 << wires[0]
        return Pauli((row.phase + 2 * bool(row.x & bit)) % 4, row.x, row.z)
    return from_b(B.conjugate_controlled_letter(
        to_b(row), wires[0], wires[1], str(letter)
    ))


def tableau(word, sites: tuple[Coord, ...]) -> tuple[Pauli, ...]:
    index = {site: qubit for qubit, site in enumerate(sites)}
    rows = list(C.identity_images(len(sites)))
    for instruction in word:
        rows = [
            conjugate_instruction(row, instruction, index, len(sites))
            for row in rows
        ]
    return tuple(rows)


def inverse_instruction(instruction):
    kind = instruction.kind
    if "Sdg" in kind:
        inverse_kind = kind.replace("Sdg", "S")
    elif kind.endswith("_S") or kind in ("basis_S", "phase_S"):
        inverse_kind = kind[:-1] + "Sdg"
    else:
        inverse_kind = kind
    return P.c707.Instruction(
        "inverse_" + inverse_kind,
        instruction.sites,
        instruction.matrix.conj().T,
    )


def inverse_word(word):
    return tuple(inverse_instruction(row) for row in reversed(word))


def controlled_matrix(letter: str) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    target = {
        "X": P.c707.c655.X,
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": np.diag((1, -1)).astype(complex),
    }[letter]
    p0 = np.diag((1, 0)).astype(complex)
    p1 = np.diag((0, 1)).astype(complex)
    # c707 uses target as the matrix MSB and the first listed/control wire as
    # the LSB.  This reproduces its landed CNOT convention exactly.
    return np.kron(identity, p0) + np.kron(target, p1)


def character_word(row, data_sites: tuple[Coord, ...], ancilla: Coord):
    axes, sign = P.c707.pauli_axes(row, data_sites)
    word = [P.c707.Instruction("char_H", (ancilla,), P.c707.c655.H)]
    if sign == -1:
        word.append(P.c707.Instruction(
            "char_sign_Z", (ancilla,), np.diag((1, -1)).astype(complex)
        ))
    word.extend(
        P.c707.Instruction(
            f"char_CP_{axis}", (ancilla, site), controlled_matrix(axis)
        )
        for site, axis in axes
    )
    word.append(P.c707.Instruction("char_H", (ancilla,), P.c707.c655.H))
    return tuple(word)


def execute_word(state, word, sites: tuple[Coord, ...]):
    index = {site: wire for wire, site in enumerate(sites)}
    output = state
    for instruction in word:
        output = P.c707.apply_gate(
            output,
            instruction.matrix,
            tuple(index[site] for site in instruction.sites),
            len(sites),
        )
    return output


def phase_aligned(observed, expected) -> tuple[float, complex]:
    overlap = np.vdot(expected, observed)
    phase = overlap / abs(overlap) if abs(overlap) else 1.0 + 0.0j
    return float(np.linalg.norm(observed - phase * expected)), complex(phase)


def symbolic_route_return(routed) -> dict[str, int]:
    touched = tuple(sorted({site for gate in routed for site in gate.sites}))
    labels = {site: (37 * index + 11) % 101 for index, site in enumerate(touched)}
    initial = dict(labels)
    swap_gates = 0
    for gate in routed:
        if gate.kind == "route_swap":
            left, right = gate.sites
            labels[left], labels[right] = labels[right], labels[left]
            swap_gates += 1
    return {
        "symbolic_dirty_labels": len(labels),
        "symbolic_route_swap_gates": swap_gates,
        "symbolic_non_swap_gates": len(routed) - swap_gates,
        "symbolic_dirty_label_return_failures": sum(
            labels[key] != value for key, value in initial.items()
        ),
    }


def canonical_literal_bridge() -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    eq, graph, site_map, gauges, all_sites, collisions = P.placement_bundle(cells)
    source_open = R.source_fswap_terms(eq, (0, 0, 0), 0)[TERM_INDEX]
    source = C.natural(eq, source_open)
    bounded = eq.forward(source_open)
    logical_jw = R.expected_logical_terms(eq, (0, 0, 0), 0)[TERM_INDEX]
    factors = C.seam_factors(eq, (0, 0, 0), 0)
    abstract_e = C.seam_images(eq, (0, 0, 0), 0)
    abstract_exact = C.apply_images(abstract_e, source, eq.qubits) == bounded

    physical_factors = tuple(
        P.physical_lift(row, eq, graph, site_map, gauges)[0]
        for row in factors
    )
    _local, e_support, e_word = P.compile_factor_rows(
        physical_factors, C.ROTATION_SIGNS, all_sites
    )
    source_physical = P.physical_lift(
        source, eq, graph, site_map, gauges
    )[0]
    bounded_physical = P.physical_lift(
        bounded, eq, graph, site_map, gauges
    )[0]
    midpoint = next(iter(gauges.values()))
    ancilla = (midpoint[0], midpoint[1], midpoint[2] + 1)
    if ancilla in all_sites:
        raise AssertionError("character ancilla collides with code placement")
    source_character = character_word(source_physical, all_sites, ancilla)
    bounded_character = character_word(bounded_physical, all_sites, ancilla)
    e_inverse = inverse_word(e_word)
    register_sites = all_sites + (ancilla,)
    left_word = source_character + e_word
    right_word = e_word + bounded_character
    sandwich = e_inverse + source_character + e_word

    left_tableau = tableau(left_word, register_sites)
    right_tableau = tableau(right_word, register_sites)
    sandwich_tableau = tableau(sandwich, register_sites)
    bounded_tableau = tableau(bounded_character, register_sites)
    left_failures = sum(a != b for a, b in zip(left_tableau, right_tableau))
    sandwich_failures = sum(
        a != b for a, b in zip(sandwich_tableau, bounded_tableau)
    )

    active_sites = tuple(sorted({
        site for instruction in left_word + right_word
        for site in instruction.sites
    }))
    active_index = {site: index for index, site in enumerate(active_sites)}
    rng = np.random.default_rng(869)
    state = rng.normal(size=1 << len(active_sites)) + 1j * rng.normal(
        size=1 << len(active_sites)
    )
    state /= np.linalg.norm(state)

    def compare(seed):
        observed = execute_word(seed, left_word, active_sites)
        expected = execute_word(seed, right_word, active_sites)
        return phase_aligned(observed, expected)

    state_residual, state_phase = compare(state)
    repeated_left, _repeated_right = site_map[graph.stream_edges[0][0]]
    dirty_gauge = P.c707.apply_gate(
        state, P.c707.c655.X,
        (active_index[repeated_left],), len(active_sites)
    )
    dirty_ancilla = P.c707.apply_gate(
        state, P.c707.c655.X,
        (active_index[ancilla],), len(active_sites)
    )
    dirty_gauge_residual, _ = compare(dirty_gauge)
    dirty_ancilla_residual, _ = compare(dirty_ancilla)

    routed, route_report = P.c707.route_word(sandwich)
    symbolic = symbolic_route_return(routed)
    expected_route_swaps = sum(
        2 * max(0, l1(*instruction.sites) - 1)
        for instruction in sandwich if len(instruction.sites) == 2
    )
    touched = set(route_report["touched_coordinates"])
    declared = set(all_sites) | {ancilla}
    resource = {
        "code_placement_M2": len(all_sites),
        "character_ancilla_M2": 1,
        "character_ancilla_distinct_from_code": ancilla not in all_sites,
        "declared_bridge_register_M2": len(declared),
        "routing_corridor_footprint_distinct_locations": len(touched),
        "routed_footprint_declared_register_locations": len(touched & declared),
        "routing_transit_only_locations": len(touched - declared),
        "declared_register_locations_not_touched_by_this_word": len(declared - touched),
    }

    deletion = {}
    for deleted in range(4):
        deletion[f"delete_E_factor_{deleted}_generator_failures"] = (
            C.mismatch_counts(
                C._factor_subset_images(eq, factors, deleted),
                C.target_images(eq),
            )["exact"]
        )
    wrong_sign = C.identity_images(eq.qubits)
    for index, (factor, sign) in enumerate(zip(factors, C.ROTATION_SIGNS)):
        wrong_sign = C.compose(
            C.transvection_images(
                eq.qubits, factor, -sign if index == 0 else sign
            ),
            wrong_sign,
            eq.qubits,
        )
    reversed_schedule = C.identity_images(eq.qubits)
    for factor, sign in reversed(tuple(zip(factors, C.ROTATION_SIGNS))):
        reversed_schedule = C.compose(
            C.transvection_images(eq.qubits, factor, sign),
            reversed_schedule,
            eq.qubits,
        )
    first_cp = next(
        index for index, row in enumerate(bounded_character)
        if row.kind.startswith("char_CP")
    )
    deleted_character = tuple(
        row for index, row in enumerate(bounded_character)
        if index != first_cp
    )
    wrong_open = R.source_fswap_terms(eq, (0, 0, 0), 0)[3]
    wrong_physical = P.physical_lift(
        eq.forward(wrong_open), eq, graph, site_map, gauges
    )[0]
    wrong_character = character_word(wrong_physical, all_sites, ancilla)
    deletion.update({
        "delete_one_character_CP_tableau_failures": sum(
            a != b for a, b in zip(
                tableau(deleted_character, register_sites), bounded_tableau
            )
        ),
        "wrong_character_row_tableau_failures": sum(
            a != b for a, b in zip(
                tableau(wrong_character, register_sites), bounded_tableau
            )
        ),
        "wrong_first_rotation_sign_generator_failures": C.mismatch_counts(
            wrong_sign, C.target_images(eq)
        )["exact"],
        "reversed_E_schedule_generator_failures": C.mismatch_counts(
            reversed_schedule, C.target_images(eq)
        )["exact"],
    })

    transvection = C.reference_certificate()
    controller = P.c707.cycle655_controller(routed, code_sites=len(all_sites))
    return {
        "cells": cells,
        "logical_global_JW_row": fields(logical_jw),
        "source_openreference_row": fields(source_open),
        "bounded_patchgraph_row": fields(bounded),
        "abstract_signed_intertwiner_exact": abstract_exact,
        "ambient_EJ_equals_JE_tableau_failures": left_failures,
        "ambient_sandwich_tableau_failures": sandwich_failures,
        "state_residual_up_to_projective_phase": state_residual,
        "state_projective_phase": (state_phase.real, state_phase.imag),
        "dirty_repetition_seed_residual": dirty_gauge_residual,
        "dirty_ancilla_seed_residual": dirty_ancilla_residual,
        "resource_inventory": resource,
        "placement_collisions": collisions,
        "physical_E_factor_weights": tuple(map(weight, physical_factors)),
        "source_character_weight": weight(source_physical),
        "bounded_character_weight": weight(bounded_physical),
        "E_active_support": len(e_support),
        "active_word_sites": len(active_sites),
        "active_word_diameter": diameter(active_sites),
        "E_character_Einverse_primitive_gates": (
            len(e_word), len(source_character), len(e_inverse)
        ),
        "routed_gates": len(routed),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "delete_first_swap_detected_macros": route_report[
            "delete_first_swap_detected_macros"
        ],
        "routed_word_sha256": route_report["word_sha256"],
        "expected_route_swap_gates": expected_route_swaps,
        **symbolic,
        "deletions_and_mutations": deletion,
        "restricted_transvection": {
            "rank_S_minus_I": transvection["rank_S_minus_I"],
            "depth_le_three_hits": transvection["depth_le_three_hits"],
            "constructed_depth": transvection["constructed_transvection_depth"],
            "signed_mismatches": transvection["signed_mismatches"],
            "delete_factor_failures": transvection["delete_factor_failures"],
        },
        "Cycle655_selection_controller": {
            "program_length": controller["program_length"],
            "fixed_cube_radius": controller["fixed_cube_radius"],
            "selected_order_failures": controller["selected_order_failures"],
            "token_return_failures": controller["token_return_failures"],
            "delete_clock_shift_changes_word": controller[
                "delete_clock_shift_changes_word"
            ],
            "maximum_bypass_action_residual": controller[
                "maximum_bypass_action_residual"
            ],
            "maximum_bypass_work_leakage": controller[
                "maximum_bypass_work_leakage"
            ],
            "boundary": "selection closes; Cycle707 blank-bypass H incompatibility remains",
        },
    }


def overlap_interface() -> dict[str, object]:
    cells = G.box_cells((2, 2, 2))
    eq, graph, site_map, gauges, _all_sites, collisions = P.placement_bundle(cells)
    keys = tuple(C.seam_key(label) for label in eq.rail_labels)
    pair = C.cleanup_edges(eq)[0]
    left_key, right_key = keys[pair[0]], keys[pair[1]]
    left = C.seam_images(eq, *left_key)
    right = C.seam_images(eq, *right_key)
    ab = C.compose(right, left, eq.qubits)
    ba = C.compose(left, right, eq.qubits)
    cleanup = C.cleanup_images(eq, (pair,))
    repaired_ab = C.compose(cleanup, ab, eq.qubits)
    repaired_ba = C.compose(cleanup, ba, eq.qubits)

    rails = P.rail_sites(eq, graph, gauges)
    left_site, right_site = rails[pair[0]], rails[pair[1]]
    h = P.c707.c655.H
    word = (
        P.c707.Instruction("interface_outer_H", (left_site,), h),
        P.c707.Instruction("interface_outer_H", (right_site,), h),
        P.c707.Instruction("interface_CZ_H", (right_site,), h),
        P.c707.Instruction(
            "interface_CZ_CNOT", (left_site, right_site), P.c707.c655.CNOT
        ),
        P.c707.Instruction("interface_CZ_H", (right_site,), h),
        P.c707.Instruction("interface_outer_H", (left_site,), h),
        P.c707.Instruction("interface_outer_H", (right_site,), h),
    )
    routed, route = P.c707.route_word(word)

    stabilizers = eq.target_w[len(eq.target_logical_z):]
    stabilizer_rank = gf2_rank(
        row.x | (row.z << eq.qubits) for row in stabilizers
    )
    deleted_rank = gf2_rank(
        row.x | (row.z << eq.qubits) for row in stabilizers[1:]
    )

    left_cells = G.box_cells((2, 2, 2))
    right_cells = tuple((x + 1, y, z) for x, y, z in left_cells)
    left_view = P.placement_bundle(left_cells, origin=(-8, 0, 0))
    right_view = P.placement_bundle(right_cells, origin=(8, 0, 0))
    left_map = P.address_placement(*left_view[:4])
    right_map = P.address_placement(*right_view[:4])
    shared = tuple(sorted(set(left_map) & set(right_map), key=repr))
    shared_kind = Counter(key[0] for key in shared)
    shared_sites = {site for key in shared for site in left_map[key]}
    shared_failures = sum(left_map[key] != right_map[key] for key in shared)
    primary = P.primary_word()
    primary_overlap = P.overlap_certificate(primary)
    return {
        "left_seam": left_key,
        "right_seam": right_key,
        "shared_cell": tuple(
            set(C.seam_endpoints(left_key)) & set(C.seam_endpoints(right_key))
        ),
        "raw_AB_BA_mismatches": C.mismatch_counts(ab, ba),
        "cleanup_AB_to_BA_mismatches": C.mismatch_counts(repaired_ab, ba),
        "cleanup_BA_to_AB_mismatches": C.mismatch_counts(repaired_ba, ab),
        "union_target_stabilizer_rank": stabilizer_rank,
        "expected_union_target_stabilizer_rank": eq.qubits - 6 * len(cells),
        "delete_one_union_stabilizer_rank": deleted_rank,
        "left_rail_index_site": (pair[0], left_site),
        "right_rail_index_site": (pair[1], right_site),
        "rail_distance": l1(left_site, right_site),
        "placement_collisions": collisions,
        "cleanup_primitive_gates": len(word),
        "cleanup_routed_gates": len(routed),
        "cleanup_maximum_route_distance": route["maximum_route_distance"],
        "cleanup_non_NN_failures": route["non_NN_failures"],
        "cleanup_operand_order_failures": route["operand_order_failures"],
        "cleanup_route_return_failures": route["route_return_failures"],
        "cleanup_delete_first_swap_detected_macros": route[
            "delete_first_swap_detected_macros"
        ],
        "cleanup_H_CNOT_H_CZ_residual": float(np.linalg.norm(
            np.kron(h, P.c707.c655.I2)
            @ P.c707.c655.CNOT
            @ np.kron(h, P.c707.c655.I2)
            - np.diag((1, 1, 1, -1))
        )),
        "shared_address_count": len(shared),
        "shared_address_kind_census": dict(shared_kind),
        "shared_address_failures": shared_failures,
        "shared_bank_M2": len(shared_sites),
        "two_cube_overlap_M2": primary_overlap["cube_overlap_M2"],
        "two_cube_union_M2": primary_overlap["cube_union_M2"],
        "two_cube_union_equals_primary": primary_overlap[
            "cube_union_equals_primary"
        ],
    }


def candidate_row(eq, fixture, tag):
    if tag[0] == "onsite_Z":
        cell, mode = tag[1:3]
        return eq.target_logical_z[6 * cell + mode]
    if tag[0] == "onsite_XX":
        cell, mode = tag[1:3]
        return eq.target_logical_x[6 * cell + mode] @ eq.target_logical_x[
            6 * cell + mode + 1
        ]
    _left, _right, owner, axis, _lm, _rm = fixture.edges[tag[1]]
    source = R.source_fswap_terms(eq, tuple(owner), int(axis))[TERM_INDEX]
    return eq.forward(source)


def chart_fixture(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = M.CompanionFixture.build(shape)
    eq = G.build_equivalence(fixture.cells).equivalence
    _graph_rows, tags = B.P.direct_graph_basis(fixture)
    targets = B.EB.target_rows(fixture, tags)
    candidates = tuple(candidate_row(eq, fixture, tag) for tag in tags)
    gram_failures = tuple(
        (left, right)
        for right in range(len(tags)) for left in range(right)
        if anticommutes(candidates[left], candidates[right])
        != anticommutes(targets[left], targets[right])
    )

    eqp, graph, site_map, gauges, all_sites, collisions = P.placement_bundle(
        fixture.cells
    )
    edges = []
    for tag, target, candidate in zip(tags, targets, candidates):
        if tag[0] != "edge":
            continue
        physical = P.physical_lift(
            candidate, eqp, graph, site_map, gauges
        )[0]
        decoded, leakage, stabilizer = R.decode_term(candidate, eq)
        difference = decoded @ target
        edges.append({
            "global_JW_weight": weight(target),
            "bounded_abstract_weight": weight(candidate),
            "bounded_physical_weight": weight(physical),
            "bounded_physical_diameter": diameter(
                support_sites(physical, all_sites)
            ),
            "decoded_difference_is_Z_only": difference.x == 0,
            "decoded_difference_Z_weight": difference.z.bit_count(),
            "decoded_leakage": leakage,
            "decoded_stabilizer_weight": stabilizer.bit_count(),
        })
    companion = M.relation_certificate(fixture)
    relation_rows = companion.pop("relation_rows")
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "seams": len(fixture.edges),
        "direct_basis_rows": len(tags),
        "Gram_pair_tests": len(tags) * (len(tags) - 1) // 2,
        "Gram_failures": len(gram_failures),
        "first_Gram_failures": gram_failures[:12],
        "candidate_nonhermitian_rows": sum(
            row.phase % 2 != ((row.x & row.z).bit_count() & 1)
            for row in candidates
        ),
        "global_JW_edge_weight_minimum": min(
            row["global_JW_weight"] for row in edges
        ),
        "global_JW_edge_weight_maximum": max(
            row["global_JW_weight"] for row in edges
        ),
        "bounded_edge_abstract_weight_maximum": max(
            row["bounded_abstract_weight"] for row in edges
        ),
        "bounded_edge_physical_weight_maximum": max(
            row["bounded_physical_weight"] for row in edges
        ),
        "bounded_edge_physical_diameter_maximum": max(
            row["bounded_physical_diameter"] for row in edges
        ),
        "all_decoded_differences_Z_only": all(
            row["decoded_difference_is_Z_only"] for row in edges
        ),
        "decoded_difference_Z_weight_maximum": max(
            row["decoded_difference_Z_weight"] for row in edges
        ),
        "literal_code_and_rail_M2": len(all_sites),
        "literal_formula_18N_plus_3M": (
            18 * len(fixture.cells) + 3 * len(fixture.edges)
        ),
        "literal_constant_bound_27N": 27 * len(fixture.cells),
        "literal_placement_collisions": collisions,
        "companion_relation_algebra": {
            key: companion[key] for key in (
                "physical_rank",
                "target_even_rank",
                "expected_target_even_rank",
                "physical_minus_target_rank",
                "commutator_Gram_failures",
                "non_Hermitian_physical_generators",
                "relation_stabilizer_rank",
                "relation_centralizer_failures",
                "relation_mutual_commutator_failures",
                "relation_phase_contradictions",
            )
        },
        "companion_relation_rows": len(relation_rows),
    }


def landed_edge_gauge_boundary(shape: tuple[int, int, int]):
    fixture = EG.CellEdgeGauge.build(shape)
    common = EG.diagonal_common_e(fixture)
    local = EG.constraint_and_update_certificate(fixture)
    return {
        "shape": shape,
        "matter_qubits": fixture.matter_qubits,
        "edge_gauge_qubits": len(fixture.edges),
        "physical_qubits": fixture.qubits,
        "common_E_failures": {
            "logical_leakage": common["logical_leakage_failures"],
            "stabilizer_commutator": common["stabilizer_commutator_failures"],
            "logical_terms": common["transformed_logical_term_failures"],
            "coordinates": common["transformed_coordinate_failures"],
            "phases": common["transformed_phase_failures"],
        },
        "maximum_local_term_weight": local["maximum_physical_term_weight"],
        "shared_edge_use_minimum": local["shared_edge_register_use_minimum"],
        "shared_edge_use_maximum": local["shared_edge_register_use_maximum"],
        "local_plaquette_rank": local["local_plaquette_rank"],
        "cycle_space_rank": local["cycle_space_rank"],
        "delete_one_loop_rank_maximum": local[
            "delete_one_independent_loop_rank_maximum"
        ],
        "maximum_raw_tableau_logical_X_weight": local[
            "maximum_raw_tableau_logical_X_weight"
        ],
        "literal_bounded_full_algebra_E_compiled_here": False,
    }


def covariance_certificate() -> dict[str, object]:
    source = C.F.build_equivalence(((0, 0, 0), (1, 0, 0)))
    source_open = R.source_fswap_terms(source, (0, 0, 0), 0)[TERM_INDEX]
    source_bounded = source.forward(source_open)
    frames = C.F.base.proper_cubic_frames()
    frame_failures = 0
    for frame in frames:
        cells = tuple(
            tuple(int(value) for value in frame @ C.F.np.asarray(cell))
            for cell in source.cells
        )
        target = C.F.build_equivalence(cells)
        open_transform = C.F.graph_transform_data(
            source.open_graph, target.open_graph, frame
        )
        patch_transform = C.F.graph_transform_data(
            source.patch_graph, target.patch_graph, frame
        )
        moved_source = C.F.transform_graph_pauli(
            source_open, open_transform[2], open_transform[3],
            open_transform[4], open_transform[5]
        )
        moved_bounded = C.F.transform_augmented_pauli(
            source_bounded, source, target, patch_transform, open_transform[0]
        )
        frame_failures += moved_bounded != target.forward(moved_source)

    product_failures = 0
    for left in frames:
        for right in frames:
            direct = left @ right
            mid_cells = tuple(
                tuple(int(value) for value in right @ C.F.np.asarray(cell))
                for cell in source.cells
            )
            final_cells = tuple(
                tuple(int(value) for value in left @ C.F.np.asarray(cell))
                for cell in mid_cells
            )
            mid = C.F.build_equivalence(mid_cells)
            final = C.F.build_equivalence(final_cells)
            first_open = C.F.graph_transform_data(
                source.open_graph, mid.open_graph, right
            )
            second_open = C.F.graph_transform_data(
                mid.open_graph, final.open_graph, left
            )
            direct_open = C.F.graph_transform_data(
                source.open_graph, final.open_graph, direct
            )
            first_patch = C.F.graph_transform_data(
                source.patch_graph, mid.patch_graph, right
            )
            second_patch = C.F.graph_transform_data(
                mid.patch_graph, final.patch_graph, left
            )
            direct_patch = C.F.graph_transform_data(
                source.patch_graph, final.patch_graph, direct
            )
            mid_source = C.F.transform_graph_pauli(
                source_open, first_open[2], first_open[3],
                first_open[4], first_open[5]
            )
            seq_source = C.F.transform_graph_pauli(
                mid_source, second_open[2], second_open[3],
                second_open[4], second_open[5]
            )
            dir_source = C.F.transform_graph_pauli(
                source_open, direct_open[2], direct_open[3],
                direct_open[4], direct_open[5]
            )
            mid_bounded = C.F.transform_augmented_pauli(
                source_bounded, source, mid, first_patch, first_open[0]
            )
            seq_bounded = C.F.transform_augmented_pauli(
                mid_bounded, mid, final, second_patch, second_open[0]
            )
            dir_bounded = C.F.transform_augmented_pauli(
                source_bounded, source, final, direct_patch, direct_open[0]
            )
            product_failures += seq_source != dir_source
            product_failures += seq_bounded != dir_bounded
            product_failures += final.forward(seq_source) != seq_bounded
    factors = C.frame_transport_certificate()
    factor_products = C.frame_product_certificate()
    return {
        "proper_cubic_frames": len(frames),
        "signed_character_frame_diagram_failures": frame_failures,
        "ordered_frame_products": len(frames) ** 2,
        "signed_character_product_diagram_failures": product_failures,
        "E_factor_signed_frame_failures": factors["signed_exact_failures"],
        "E_factor_phase_only_frame_failures": factors[
            "signed_phase_only_failures"
        ],
        "E_factor_product_diagram_failures": factor_products[
            "signed_factor_diagram_failures"
        ],
        "state_scope": (
            "canonical 20-site state lift executed separately; 24/576 are exact "
            "signed operator diagrams, not dense state executions"
        ),
    }


def main() -> None:
    pins = pinned_input_certificate()
    note = note_contract()
    bridge = canonical_literal_bridge()
    overlap = overlap_interface()
    fixtures = tuple(chart_fixture(shape) for shape in (PRIMARY, HELD))
    edge_gauge = tuple(
        landed_edge_gauge_boundary(shape) for shape in (PRIMARY, HELD)
    )
    covariance = covariance_certificate()

    resources = bridge["resource_inventory"]
    checks = {
        "direct_imports_and_frozen_target_are_content_pinned": (
            pins["direct_import_hash_failures"] == 0
            and pins["target_spec_hash_match"]
            and pins["loaded_helper_closure"]["match"]
            and pins["package_base_commit"]["pass"]
        ),
        "bounded_theorem_note_contract": note["pass"],
        "canonical_signed_and_literal_intertwiner_exact": (
            bridge["abstract_signed_intertwiner_exact"]
            and bridge["ambient_EJ_equals_JE_tableau_failures"] == 0
            and bridge["ambient_sandwich_tableau_failures"] == 0
            and bridge["state_residual_up_to_projective_phase"] < TOL
        ),
        "corrected_bridge_resource_inventory_exact": (
            resources["code_placement_M2"] == 39
            and resources["character_ancilla_M2"] == 1
            and resources["character_ancilla_distinct_from_code"]
            and resources["declared_bridge_register_M2"] == 40
            and resources["routing_corridor_footprint_distinct_locations"] == 155
            and resources["routed_footprint_declared_register_locations"] == 20
            and resources["routing_transit_only_locations"] == 135
            and resources["declared_register_locations_not_touched_by_this_word"] == 20
        ),
        "literal_routes_and_dirty_inputs_close": (
            bridge["placement_collisions"] == 0
            and bridge["non_NN_failures"] == 0
            and bridge["operand_order_failures"] == 0
            and bridge["route_return_failures"] == 0
            and bridge["symbolic_route_swap_gates"]
            == bridge["expected_route_swap_gates"]
            and bridge["symbolic_non_swap_gates"]
            == sum(bridge["E_character_Einverse_primitive_gates"])
            and bridge["symbolic_dirty_label_return_failures"] == 0
            and bridge["dirty_repetition_seed_residual"] < TOL
            and bridge["dirty_ancilla_seed_residual"] < TOL
        ),
        "all_deletions_and_mutations_active": (
            all(value > 0 for value in bridge["deletions_and_mutations"].values())
            and bridge["delete_first_swap_detected_macros"] > 0
        ),
        "restricted_transvection_and_selection_controls_close": (
            bridge["restricted_transvection"]["rank_S_minus_I"] == 3
            and not any(bridge["restricted_transvection"][
                "depth_le_three_hits"
            ].values())
            and bridge["restricted_transvection"]["constructed_depth"] == 4
            and bridge["Cycle655_selection_controller"][
                "selected_order_failures"
            ] == 0
            and bridge["Cycle655_selection_controller"][
                "token_return_failures"
            ] == 0
            and bridge["Cycle655_selection_controller"][
                "delete_clock_shift_changes_word"
            ]
        ),
        "two_star_AB_BA_cleanup_exact": (
            overlap["raw_AB_BA_mismatches"]["exact"] == 2
            and not any(overlap["cleanup_AB_to_BA_mismatches"].values())
            and not any(overlap["cleanup_BA_to_AB_mismatches"].values())
            and overlap["cleanup_non_NN_failures"] == 0
            and overlap["cleanup_operand_order_failures"] == 0
            and overlap["cleanup_route_return_failures"] == 0
            and overlap["cleanup_H_CNOT_H_CZ_residual"] < TOL
        ),
        "union_stabilizer_deletion_rank_is_gated": (
            overlap["union_target_stabilizer_rank"] == 120
            and overlap["expected_union_target_stabilizer_rank"] == 120
            and overlap["delete_one_union_stabilizer_rank"] == 119
        ),
        "shared_address_and_M2_census_is_gated": (
            overlap["shared_address_count"] == 80
            and overlap["shared_address_kind_census"] == {
                "edge": 76, "rail": 4
            }
            and overlap["shared_address_failures"] == 0
            and overlap["shared_bank_M2"] == 84
            and overlap["two_cube_overlap_M2"] == 84
            and overlap["two_cube_union_M2"] == 276
            and overlap["two_cube_union_equals_primary"]
        ),
        "primary_held_support_and_literal_scaling_bounded": (
            max(row["bounded_edge_physical_weight_maximum"] for row in fixtures)
            <= 17
            and max(row["bounded_edge_physical_diameter_maximum"] for row in fixtures)
            <= 29
            and all(
                row["literal_code_and_rail_M2"]
                == row["literal_formula_18N_plus_3M"]
                <= row["literal_constant_bound_27N"]
                and row["literal_placement_collisions"] == 0
                for row in fixtures
            )
        ),
        "direct_full_chart_substitution_route_is_discriminated": (
            fixtures[0]["Gram_failures"] == 22
            and fixtures[1]["Gram_failures"] == 76
        ),
        "landed_edge_gauge_full_algebra_alternative_remains_exact": all(
            not any(row["common_E_failures"].values())
            and row["shared_edge_use_minimum"]
            == row["shared_edge_use_maximum"] == 1
            for row in edge_gauge
        ),
        "signed_operator_covariance_closes_24_576": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["signed_character_frame_diagram_failures"] == 0
            and covariance["signed_character_product_diagram_failures"] == 0
            and covariance["E_factor_signed_frame_failures"] == 0
            and covariance["E_factor_phase_only_frame_failures"] == 0
            and covariance["E_factor_product_diagram_failures"] == 0
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "disposition": "PARTIAL_EXECUTABLE_BRIDGE",
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "checks": checks,
        "content_pins": pins,
        "note_contract": note,
        "canonical_literal_bridge": bridge,
        "overlap_and_shared_interface": overlap,
        "primary_and_held_chart_discriminator": fixtures,
        "landed_edge_gauge_exact_alternative_boundary": edge_gauge,
        "proper_cubic_covariance": covariance,
        "supplied": (
            "Cycle703 OpenReference/local-Gauss BKSF charts and local incidence order",
            "Cycle707 spacing-16 PatchGraph repetition placement and returned router",
            "Cycle709 four signed seam transvections, coframe transport, and cleanup predicate",
            "Cycle789 direct even-CAR tags, global-JW targets, encoded sectors, and finite charts",
            "Cycle720 half-edge companion and cell-edge gauge diagnostics",
        ),
        "derived": (
            "the frozen TERM_INDEX=2 controlled-character bridge and exact E J = J E tableau",
            "the 39+1=40 register inventory and separate 155-location routed footprint",
            "the literal two-star AB/BA cleanup and gated union/shared-address censuses",
            "the primary/held direct-substitution Gram discriminator",
            "dirty input, deletion, controller-selection, and signed 24/576 controls",
        ),
        "open": (
            "a bounded literal full-algebra E replacing the landed edge-gauge growing logical orientation",
            "compilation of that E, every Cycle789 edge character, and E^-1 on primary and held banks",
            "one complete three-register signed Cycle789 channel on the edge-gauge quotient",
            "autonomous sector preparation, enforcement, controller genesis, and repair",
        ),
        "claim_boundary": (
            "Exact finite canonical and transported one-seam bridge plus exact two-star cleanup. "
            "The direct all-row substitution is rejected only on its measured primary/held Gram "
            "residuals.  The overall result is partial and makes no no-go, asymptotic, autonomous, "
            "time, Record/Born, source, or axiom-pressure claim."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print(
        "CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_PASS"
        if report["status"] == "PASS"
        else "CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_FAIL"
    )
    raise SystemExit(0 if report["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
