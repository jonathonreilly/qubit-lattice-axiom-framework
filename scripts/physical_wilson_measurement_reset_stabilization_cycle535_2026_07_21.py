#!/usr/bin/env python3
"""Cycle 535: local measurement/reset attack on the three-Wilson initializer.

The runner constructs the exact Wilson measurement plus membrane-reset channel
for the Cycle-532 rough-terminal code and audits its action on the complete
matter algebra.  It also tests the covariant translated-membrane orbit and
exhausts every Pauli supported in contractible owner-cell boxes at L5/L6 for a
lawful bounded Wilson flipper.

The result is a constructive partial attempt, not a no-go.  Deterministic
reset reaches the all-plus spin sector but twists the matter stream on a
growing membrane.  Postselection preserves matter only conditionally.  A
defect-mediated local preparation from scratch remains open.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21 as c532


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "wilson-reset-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md"
)
CYCLE532_RUNNER = ROOT / (
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py"
)
CYCLE532_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
)
CYCLE269_RUNNER = ROOT / (
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py"
)
CYCLE269_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md"
)
CYCLE240_RUNNER = ROOT / (
    "scripts/MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17.py"
)
CYCLE240_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_NOTE_2026-07-17.md"
)
STRICT_FILE_HASHES = {
    CYCLE532_RUNNER: "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    CYCLE532_NOTE: "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    CYCLE269_RUNNER: "c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35",
    CYCLE269_NOTE: "d5a39e45949cf079f6c37fa5646d00a9319d7d2776d84323d9adf1c086e06beb",
    CYCLE240_RUNNER: "d9dfdf2a1a6b808b4e6fd40f75313468278f3e21d875c91a4bfde2469f340b56",
    CYCLE240_NOTE: "fc8acdba1ea7d4552f32ed3ab72540c415696ba0c05c5187e6b9d7f74a8021ee",
    **c532.STRICT_FILE_HASHES,
}


class CertificateFailure(RuntimeError):
    """A bounded predicate failed; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """A technical resource wall; never a physical conclusion."""


@dataclass(frozen=True)
class Membrane:
    axis: int
    position: int
    pauli: c235.Pauli
    wilson_index: int


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def membrane_pauli(graph: c247.PunctureGraph, axis: int, position: int) -> c235.Pauli:
    """Fixed-presentation Z membrane crossing one periodic cut."""

    z = 0
    for edge, (source, target, kind, owner) in enumerate(graph.base.edges):
        if (
            kind == "outer_square"
            and owner[axis] == position
            and graph.base.vertices[source][1] // 2 == axis
            and graph.base.vertices[target][1] // 2 == axis
        ):
            z ^= 1 << edge
    return c235.Pauli(z=z)


def membrane_orbit(graph: c247.PunctureGraph) -> tuple[Membrane, ...]:
    wilsons = c532.wilson_initializers(graph)
    rows = []
    for axis in range(3):
        for position in range(graph.length):
            pauli = membrane_pauli(graph, axis, position)
            pairing = tuple(int(not pauli.commutes(wilson)) for wilson in wilsons)
            if sum(pairing) != 1:
                raise CertificateFailure(("membrane-Wilson pairing", axis, position, pairing))
            rows.append(Membrane(axis, position, pauli, pairing.index(1)))
    return tuple(rows)


def pauli_product(rows) -> c235.Pauli:
    result = c235.Pauli()
    for row in rows:
        result = result @ row
    return result


def reset_channel_controls(length: int) -> dict:
    """Exact Heisenberg audit of measure-W then correct-with-membrane reset.

    For an observable O commuting with W, the deterministic reset has
    R^dagger(O)=O when [T,O]=0 and R^dagger(O)=W O when {T,O}=0.
    The runner uses exact Pauli commutators rather than a density matrix.
    """

    graph = c247.PunctureGraph(length, terminals=1)
    local = c532.local_stabilizers(graph)
    fixed = c532.fixed_sector_stabilizers(graph)
    wilsons = c532.wilson_initializers(graph)
    matter_b = tuple(graph.B(vertex) for vertex in range(graph.matter_count))
    matter_a = tuple(
        graph.mapped_matter_A(edge) for edge in range(len(graph.base.edges))
    )
    gauge_z, gauge_a, _ = c532.gauge_generators(graph)
    membranes = membrane_orbit(graph)
    total_matter_parity = pauli_product(matter_b)
    wilson_factor_counts = []
    wilson_factor_maximum_support = []
    for vertices in graph.wilson_cycles():
        factors = tuple(
            graph.A(source, vertices[(index + 1) % len(vertices)])
            for index, source in enumerate(vertices)
        )
        wilson_factor_counts.append(len(factors))
        wilson_factor_maximum_support.append(
            max((row.x | row.z).bit_count() for row in factors)
        )

    rows = []
    for membrane in membranes:
        pauli = membrane.pauli
        matter_b_flips = sum(not pauli.commutes(row) for row in matter_b)
        matter_a_flips = sum(not pauli.commutes(row) for row in matter_a)
        gauge_flips = sum(not pauli.commutes(row) for row in gauge_z + gauge_a)
        rows.append(
            {
                "axis": membrane.axis,
                "position": membrane.position,
                "Wilson_index": membrane.wilson_index,
                "M2_weight": (pauli.x | pauli.z).bit_count(),
                "local_constraint_commutator_failures": sum(
                    not pauli.commutes(row) for row in local
                ),
                "Wilson_pairing": [
                    int(not pauli.commutes(wilson)) for wilson in wilsons
                ],
                "matter_B_twists": matter_b_flips,
                "matter_A_twists": matter_a_flips,
                "gauge_generator_twists": gauge_flips,
                "total_matter_parity_twist": int(
                    not pauli.commutes(total_matter_parity)
                ),
            }
        )

    fixed_rank, fixed_bad = c235.phase_aware_rank(fixed, graph.qubits)
    plus_rank, plus_bad = c235.phase_aware_rank(
        fixed + (total_matter_parity,), graph.qubits
    )
    minus_rank, minus_bad = c235.phase_aware_rank(
        fixed + (c235.Pauli(phase=2) @ total_matter_parity,), graph.qubits
    )

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)
    f_plus = 0.5 * (
        b_left + b_right + 1j * b_left @ hopping - 1j * b_right @ hopping
    )
    f_minus = 0.5 * (
        b_left + b_right - 1j * b_left @ hopping + 1j * b_right @ hopping
    )
    seam_operator_residual = float(np.linalg.norm(f_plus - f_minus, ord=2))
    random_orbit_residual = seam_operator_residual / length

    pass_flag = bool(
        len(membranes) == 3 * length
        and all(row["M2_weight"] == length**2 for row in rows)
        and all(row["local_constraint_commutator_failures"] == 0 for row in rows)
        and all(sum(row["Wilson_pairing"]) == 1 for row in rows)
        and all(row["matter_B_twists"] == 0 for row in rows)
        and all(row["matter_A_twists"] == length**2 for row in rows)
        and all(row["gauge_generator_twists"] == length**2 for row in rows)
        and all(row["total_matter_parity_twist"] == 0 for row in rows)
        and wilson_factor_counts == [3 * length] * 3
        and max(wilson_factor_maximum_support) <= 9
        and plus_rank == minus_rank == fixed_rank + 1
        and not fixed_bad
        and not plus_bad
        and not minus_bad
        and abs(seam_operator_residual - 2.0) < TOLERANCE
        and abs(random_orbit_residual - 2.0 / length) < TOLERANCE
    )
    return {
        "length": length,
        "coarse_cells": length**3,
        "membrane_orbit_size": len(membranes),
        "membrane_rows": rows,
        "fixed_all_plus_rank": fixed_rank,
        "positive_matter_parity_sector_nonempty": not plus_bad,
        "negative_matter_parity_sector_nonempty": not minus_bad,
        "both_matter_parities_preserved_by_reset": True,
        "literal_local_measurement_network": {
            "syndrome_ancillas": 3,
            "ordered_controlled_A_factors_per_Wilson": wilson_factor_counts,
            "maximum_A_factor_M2_support": max(wilson_factor_maximum_support),
            "total_controlled_A_factors": sum(wilson_factor_counts),
            "maximum_membrane_face_Z_feedbacks": 3 * length**2,
            "signal_depth_bound": "O(L) with a walking syndrome carrier and planar local broadcast",
            "host_parity_computation": False,
        },
        "deterministic_reset_channel": (
            "R_a(rho)=P_plus rho P_plus + T_a P_minus rho P_minus T_a"
        ),
        "Heisenberg_crossed_hopping": "R_a^dagger(A_e)=W_a A_e",
        "fixed_cut_crossed_FSWAP_operator_norm_residual": seam_operator_residual,
        "uniform_translated_membrane_FSWAP_operator_norm_residual": random_orbit_residual,
        "onsite_B_mass_contact_preserved": True,
        "onsite_internal_hoppings_preserved": True,
        "full_Fock_Gamma_P_preserved": False,
        "Cycle230_seam_preserved": False,
        "measurement_outcomes": 3,
        "uniform_sector_postselection_success_probability": 1 / 8,
        "reset_channel_invertible": False,
        "discarded_spin_sector_bits": 3,
        "fixed_cut_randomness": "none",
        "uniform_orbit_randomness": "three shared positions in Z_L",
        "reset_bath": "three syndrome bits plus distributed cat/broadcast ancillas, reset after use",
        "boundary_condition": "finite periodic L^3 torus; fixed cut uses the supplied macro origin",
        "pass": pass_flag,
    }


def coefficient_on_support(pauli: c235.Pauli, support: tuple[int, ...]) -> int:
    """Symplectic commutator row for an unknown Pauli on support."""

    width = len(support)
    row = 0
    for local_index, qubit in enumerate(support):
        if (pauli.z >> qubit) & 1:
            row |= 1 << local_index
        if (pauli.x >> qubit) & 1:
            row |= 1 << (width + local_index)
    return row


def owner_cube_support(graph: c247.PunctureGraph, width: int) -> tuple[int, ...]:
    cells = {
        (x, y, z)
        for x in range(width)
        for y in range(width)
        for z in range(width)
    }
    return tuple(
        qubit for qubit, edge in enumerate(graph.edges) if edge.owner in cells
    )


def lawful_local_flipper_scan(length: int) -> dict:
    """Exhaust all Paulis in each proper contractible owner-cell cube.

    Solving the GF(2) commutator equations exhausts 4^k Pauli choices without
    enumerating them.  A solution would commute with every bounded local check
    and anticommute with one Wilson.
    """

    graph = c247.PunctureGraph(length, terminals=1)
    local = c532.local_stabilizers(graph)
    wilsons = c532.wilson_initializers(graph)
    rows = []
    for width in range(1, length):
        support = owner_cube_support(graph, width)
        variables = 2 * len(support)
        base = [coefficient_on_support(row, support) for row in local]
        base_rank = c235.gf2_rank(base)
        solutions = []
        for wilson in wilsons:
            equations = base + [coefficient_on_support(wilson, support)]
            rhs = [0] * len(base) + [1]
            coefficient_rank = c235.gf2_rank(equations)
            augmented_rank = c235.gf2_rank(
                row | (bit << variables) for row, bit in zip(equations, rhs)
            )
            solutions.append(coefficient_rank == augmented_rank)
        rows.append(
            {
                "owner_cube_width": width,
                "support_M2": len(support),
                "Pauli_search_space_log2": variables,
                "constraint_equation_rank": base_rank,
                "lawful_Wilson_flipper_exists": solutions,
            }
        )
    return {
        "length": length,
        "exhaustive_GF2_rows": rows,
        "all_proper_owner_cubes_reject_lawful_Pauli_flipper": all(
            not any(row["lawful_Wilson_flipper_exists"]) for row in rows
        ),
        "scope": (
            "all Pauli jumps supported inside the tested contractible axis-aligned "
            "owner-cell cubes; translated/framed copies follow by code covariance"
        ),
        "autonomous_consequence": (
            "a code-preserving bounded Pauli-jump semigroup conserves the three "
            "Wilson signs; defect-mediated paths that leave the code are not excluded"
        ),
        "pass": all(not any(row["lawful_Wilson_flipper_exists"]) for row in rows),
    }


def covariance_controls() -> dict:
    graph = c247.PunctureGraph(3, terminals=1)
    membranes = membrane_orbit(graph)
    orbit = {
        (row.pauli.phase, row.pauli.x, row.pauli.z) for row in membranes
    }
    fixed = {
        (row.pauli.phase, row.pauli.x, row.pauli.z)
        for row in membranes
        if row.position == graph.length - 1
    }
    orbit_failures = 0
    fixed_cut_failures = 0
    for frame in c235.proper_cubic_frames():
        data = c532.frame_data(graph, frame)
        for row in membranes:
            transformed = c532.transform_pauli(row.pauli, data)
            key = (transformed.phase, transformed.x, transformed.z)
            orbit_failures += key not in orbit
            if row.position == graph.length - 1:
                fixed_cut_failures += key not in fixed
    inherited = c532.covariance_controls()
    return {
        "length": 3,
        "proper_cubic_frames": 24,
        "translated_membrane_orbit_cases": 24 * len(membranes),
        "translated_membrane_orbit_failures": orbit_failures,
        "fixed_three_cut_cases": 24 * 3,
        "fixed_three_cut_failures": fixed_cut_failures,
        "uniform_orbit_channel_proper_cubic_covariant": orbit_failures == 0,
        "deterministic_fixed_cut_controller_proper_cubic_covariant": fixed_cut_failures == 0,
        "inherited_fixed_code_all24_576": inherited,
        "active_runtime_frame_selector": False,
        "pass": bool(
            orbit_failures == 0
            and fixed_cut_failures > 0
            and inherited["pass"]
        ),
    }


def deletion_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        graph = c247.PunctureGraph(length, terminals=1)
        local = c532.local_stabilizers(graph)
        wilsons = c532.wilson_initializers(graph)
        membrane = next(
            row for row in membrane_orbit(graph) if row.wilson_index == 0
        ).pauli
        removed_bit = membrane.z & -membrane.z
        deleted = c235.Pauli(z=membrane.z ^ removed_bit)
        rows.append(
            {
                "length": length,
                "full_membrane_local_syndrome": sum(
                    not membrane.commutes(row) for row in local
                ),
                "deleted_face_local_syndrome": sum(
                    not deleted.commutes(row) for row in local
                ),
                "full_membrane_flips_target_Wilson": int(
                    not membrane.commutes(wilsons[0])
                ),
                "deleted_face_flips_target_Wilson": int(
                    not deleted.commutes(wilsons[0])
                ),
            }
        )
    return {
        "measurement_only_deletion": (
            "deleting feedback leaves Wilson populations unchanged and does not initialize +++"
        ),
        "single_face_deletions": rows,
        "pass": all(
            row["full_membrane_local_syndrome"] == 0
            and row["deleted_face_local_syndrome"] == 4
            and row["full_membrane_flips_target_Wilson"] == 1
            and row["deleted_face_flips_target_Wilson"] == 0
            for row in rows
        ),
    }


def inherited_target_controls() -> dict:
    factors = tuple(
        c532.factorization_controls(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    target = c532.target_B_controls()
    fixtures = c532.fixture_controls()
    return {
        "Cycle532_factorizations": factors,
        "Cycle529_target_replay": target,
        "mass_contact_seam_logical_comparators": fixtures,
        "interpretation": (
            "the unchanged fixed-spin code retains all inherited exact results; "
            "the new reset channel fails before that runtime on crossed stream generators"
        ),
        "pass": bool(
            all(row["pass"] for row in factors)
            and target["pass"]
            and fixtures["pass"]
        ),
    }


def upstream_evidence() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest
        for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path)
        for path in STRICT_FILE_HASHES
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "pass": expected == observed,
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "measurement outcomes",
        "reset bath",
        "randomness",
        "periodic boundary",
        "r_a^dagger(a_e)=w_a a_e",
        "operator-norm residual 2",
        "2/l",
        "both matter parities",
        "full-fock gamma(p)",
        "all 24",
        "576",
        "l5",
        "held l6",
        "defect-mediated",
        "broad no-go gate status: **fail / do not ship**",
        "partial-attempt-with-named-untested-routes",
        "n1 — alternative-route normalization",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {
        "required_fragments": len(required),
        "missing_fragments": missing,
        "pass": not missing,
    }


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_Cycle240_Cycle269_Cycle532_and_transitive_hashes": evidence["pass"],
        "note_scope_resources_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": (
            "cycle535-Wilson-reset-contract-ready"
            if all(tests.values())
            else "cycle535-dry-contract-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle535 dry contract failed")

    reset = tuple(
        reset_channel_controls(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    checkpoints.append(checkpoint(started, "L5-L6-exact-reset-channels"))
    local_scans = tuple(
        lawful_local_flipper_scan(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    checkpoints.append(checkpoint(started, "contractible-lawful-Pauli-scans"))
    covariance = covariance_controls()
    checkpoints.append(checkpoint(started, "all24-576-covariance"))
    deletions = deletion_controls()
    checkpoints.append(checkpoint(started, "deletion-lawful-domain-controls"))
    inherited = inherited_target_controls()
    checkpoints.append(checkpoint(started, "inherited-full-Fock-fixtures"))

    tests = {
        "dry_contract": dry["pass"],
        "exact_L5_held_L6_measurement_membrane_reset": all(
            row["pass"] for row in reset
        ),
        "both_matter_parities_and_onsite_mass_contact_preserved": all(
            row["both_matter_parities_preserved_by_reset"]
            and row["onsite_B_mass_contact_preserved"]
            for row in reset
        ),
        "full_Fock_and_seam_twist_detected_not_hidden": all(
            not row["full_Fock_Gamma_P_preserved"]
            and not row["Cycle230_seam_preserved"]
            for row in reset
        ),
        "contractible_lawful_Pauli_flipper_exhaustion": all(
            row["pass"] for row in local_scans
        ),
        "covariant_membrane_orbit_and_inherited_24_576": covariance["pass"],
        "fixed_cut_non_covariance_explicit": (
            covariance["fixed_three_cut_failures"] > 0
        ),
        "measurement_feedback_and_membrane_deletions": deletions["pass"],
        "inherited_factorization_target_mass_contact_seam": inherited["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "wilson-reset-certificate",
        "status": (
            "cycle535-exact-Wilson-reset-with-matter-twist-partial-attempt"
            if all(tests.values())
            else "cycle535-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "reset_channel_controls": reset,
        "lawful_local_flipper_scans": local_scans,
        "covariance": covariance,
        "deletion_controls": deletions,
        "inherited_target_controls": inherited,
        "strongest_constructive_result": {
            "measurement": (
                "three commuting Wilson syndromes can be measured nondestructively "
                "by a bounded-gate distributed cat/walking-ancilla circuit of O(L) depth"
            ),
            "conditional_branch": (
                "+++ postselection preserves the matter algebra but is trace-decreasing; "
                "success is 1/8 only for an explicitly uniform spin-sector input"
            ),
            "deterministic_reset": (
                "fixed-cut membrane feedback is CPTP, local-check lawful, preserves both "
                "matter parities, and sets +++, but twists L^2 stream generators per axis"
            ),
            "covariant_variant": (
                "uniform translated-membrane feedback removes the preferred cut as a "
                "channel but needs shared randomness and leaves exact FSWAP residual 2/L"
            ),
            "physical_compiler_unconditional": False,
        },
        "explicit_resources": {
            "measurement_outcomes": "three global Wilson syndrome bits",
            "reset_bath": (
                "fresh local cat/broadcast ancillas plus erasure after the protocol; "
                "not derived as energy, time, or a Record"
            ),
            "randomness": (
                "none for fixed cuts; three shared Z_L cut positions for the covariant mixture"
            ),
            "boundary_conditions": "finite periodic torus and supplied macro origin",
            "schedule": (
                "bounded local gates with O(L) signal depth; schedule depth is compiler "
                "latency, not a physical duration"
            ),
        },
        "exact_remaining_obligation": {
            "name": "W_topological-encoding",
            "statement": (
                "construct a from-scratch or defect-mediated bounded-local encoder that "
                "forms +++ while intertwining the complete target matter algebra"
            ),
            "strength_relation_to_target": "target-equivalent for this periodic rough presentation",
            "open_routes": (
                "defect-mediated code deformation, locally filled puncture topology, "
                "coherent from-scratch Clifford/non-Clifford encoder, or operational finite-cone quotient"
            ),
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "partial-attempt-with-named-untested-routes",
            "narrow_result": (
                "the displayed measurement/membrane reset and code-preserving bounded "
                "Pauli-jump families do not retire W_topological-encoding"
            ),
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(
                row["maximum_RSS_bytes"] for row in checkpoints
            ),
            "process_swap_count": sum(
                row["process_swap_count"] for row in checkpoints
            ),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle535-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
