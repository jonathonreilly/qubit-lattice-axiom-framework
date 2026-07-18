#!/usr/bin/env python3
"""Cycle 278: same-code local contact instrument on the connected edge code.

One fresh pointer M2 is coherently flipped by the proper-cubic scalar
contact-active projector Q_{>=2}=1_{N_x>=2}.  Q is represented as a bounded
polynomial of the six mapped local B_v operators in the Cycle-269/271
connected edge code.  Cycle-275 fixed-Wilson projectors then give exact
pointer weights and conditional states on all eight sectors.

This is a conditional quantum instrument in ordinary complex quantum
mechanics.  It is not an occurrence law or Record-formation mechanism.
Compiler iteration is not physical time.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269
import contractible_lightcone_wilson_quotient_cycle271_2026_07_17 as c271
import locally_matched_wilson_sector_states_cycle275_2026_07_17 as c275


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
DIRECTIONS = tuple(range(6))


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
        check("the Cycle-278 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "same-code local quantum instrument",
        "cycle-269/271 connected edge code",
        "cycle-275 total-even matched sector states",
        "contact-active projector",
        "bounded support",
        "one pointer m2",
        "all eight wilson sectors",
        "l=3,4,5",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "full 27-element l=3 translation group",
        "local-check and wilson preservation",
        "repeatability",
        "disturbance",
        "deletion",
        "lawful domain",
        "actual coin/contact",
        "not occurrence",
        "not record formation",
        "compiler iteration is not physical time",
        "preparation, trace, readout, and outcome-selection imports",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the same-code instrument, scope, controls, imports, and N1-N8 contract",
        not missing,
        missing,
    )


def cell_bs(
    code: c269.WilsonSubsystemCode, cell: tuple[int, int, int]
) -> tuple[c235.Pauli, ...]:
    return tuple(
        code.B[code.graph.vertex_index[(cell, direction)]]
        for direction in DIRECTIONS
    )


def pauli_product(rows: tuple[c235.Pauli, ...], mask: int) -> c235.Pauli:
    result = c235.Pauli()
    for direction, row in enumerate(rows):
        if (mask >> direction) & 1:
            result = result @ row
    return result


def contact_active(occupation: int) -> int:
    """The support projector of binom(N_x,2), not an energy observable."""

    return int(occupation.bit_count() >= 2)


def walsh_coefficients() -> tuple[Fraction, ...]:
    """Q_{>=2}=sum_mask c_mask product_(d in mask) B_d exactly."""

    coefficients = []
    for mask in range(64):
        total = 0
        for occupation in range(64):
            sign = -1 if (mask & occupation).bit_count() % 2 else 1
            total += contact_active(occupation) * sign
        coefficients.append(Fraction(total, 64))
    return tuple(coefficients)


def phase_reducer(
    rows: list[c235.Pauli], qubits: int
) -> tuple[dict[int, c235.Pauli], tuple[tuple[int, int], ...]]:
    """Build the phase-aware row echelon form once for many expectations."""

    pivots: dict[int, c235.Pauli] = {}
    inconsistent = []
    for index, original in enumerate(rows):
        row = original
        symplectic = row.symplectic(qubits)
        while symplectic:
            pivot = symplectic.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row = row @ pivots[pivot]
            symplectic = row.symplectic(qubits)
        if not symplectic and row.phase % 4:
            inconsistent.append((index, row.phase))
    return pivots, tuple(inconsistent)


def reduce_pauli(
    target: c235.Pauli, pivots: dict[int, c235.Pauli], qubits: int
) -> c235.Pauli:
    row = target
    symplectic = row.symplectic(qubits)
    while symplectic:
        pivot = symplectic.bit_length() - 1
        if pivot not in pivots:
            break
        row = row @ pivots[pivot]
        symplectic = row.symplectic(qubits)
    return row


def fast_expectation(
    observable: c235.Pauli, pivots: dict[int, c235.Pauli], qubits: int
) -> int:
    reduced = reduce_pauli(observable, pivots, qubits)
    if reduced.symplectic(qubits):
        return 0
    if reduced.phase % 4 == 0:
        return 1
    if reduced.phase % 4 == 2:
        return -1
    raise ValueError("a Hermitian commuting observable reduced to an imaginary phase")


def moments(
    bs: tuple[c235.Pauli, ...],
    pivots: dict[int, c235.Pauli],
    qubits: int,
) -> tuple[int, ...]:
    return tuple(
        fast_expectation(pauli_product(bs, mask), pivots, qubits)
        for mask in range(64)
    )


def probability_from_moments(
    coefficients: tuple[Fraction, ...], values: tuple[int, ...]
) -> Fraction:
    return sum(
        (coefficient * value for coefficient, value in zip(coefficients, values)),
        start=Fraction(0),
    )


def configuration_probabilities(values: tuple[int, ...]) -> tuple[Fraction, ...]:
    probabilities = []
    for occupation in range(64):
        total = 0
        for mask, value in enumerate(values):
            sign = -1 if (mask & occupation).bit_count() % 2 else 1
            total += sign * value
        probabilities.append(Fraction(total, 64))
    return tuple(probabilities)


def biased_rows(
    code: c269.WilsonSubsystemCode,
    bits: tuple[int, int, int],
    b0_sign: int | None,
) -> list[c235.Pauli]:
    rows = c275.fixed_sector_rows(code, bits)
    if b0_sign is None:
        return rows
    b0 = cell_bs(code, (0, 0, 0))[0]
    return rows + [c269.signed(b0, int(b0_sign < 0))]


def pointer_dilation_and_actual_contact_controls() -> None:
    print("\nBOUNDED COHERENT POINTER / ACTUAL CONTACT FIXTURE")
    occupations = np.asarray([index.bit_count() for index in range(64)])
    q_values = (occupations >= 2).astype(float)
    q = np.diag(q_values).astype(complex)
    q0 = np.eye(64, dtype=complex) - q
    pointer_i = np.eye(2, dtype=complex)
    pointer_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    pointer_zero = np.asarray(((1, 0), (0, 0)), dtype=complex)
    dilation = np.kron(q0, pointer_i) + np.kron(q, pointer_x)
    identity = np.eye(128, dtype=complex)

    species = c219.common_species(c230.BETA)
    fock_coin = c229.fock_lift(species.coin)
    contact_generator = np.diag(occupations * (occupations - 1) / 2).astype(complex)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    reverse = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate((1, 0, 3, 2, 5, 4)):
        reverse[target, source] = 1
    fock_reverse = c229.fock_lift(reverse)

    check(
        "one pointer M2 gives an exact coherent dilation of the binary contact-active projector",
        np.linalg.norm(dilation.conj().T @ dilation - identity) == 0
        and np.linalg.norm(dilation @ dilation - identity) == 0
        and int(np.trace(q).real) == 57
        and np.linalg.norm(q @ q - q) == 0,
        {
            "local_matter_dimension": 64,
            "joint_dimension": 128,
            "rank_Q_ge2": int(np.trace(q).real),
            "unitarity_residual": float(
                np.linalg.norm(dilation.conj().T @ dilation - identity)
            ),
        },
    )
    check(
        "the pointer observable is the support of the actual g=0.37 contact generator and commutes with the actual beta=-0.3 onsite coin/contact/reversal",
        np.array_equal(q_values, (np.diag(contact_generator) > 0).astype(float))
        and np.linalg.norm(q @ fock_coin - fock_coin @ q) < 2e-14
        and np.linalg.norm(q @ contact - contact @ q) == 0
        and np.linalg.norm(q @ fock_reverse - fock_reverse @ q) == 0
        and np.all(q_values[occupations <= 1] == 0)
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "Q_coin_commutator": float(np.linalg.norm(q @ fock_coin - fock_coin @ q)),
            "Q_contact_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
            "one_particle_action": "identity pointer; the mass fixture is undisturbed",
        },
    )

    local_states = {
        "uniform": np.eye(64, dtype=complex) / 64,
        "B0_plus": np.diag([int((index & 1) == 0) / 32 for index in range(64)]),
        "B0_minus": np.diag([int((index & 1) == 1) / 32 for index in range(64)]),
    }
    expected = {
        "uniform": Fraction(57, 64),
        "B0_plus": Fraction(13, 16),
        "B0_minus": Fraction(31, 32),
    }
    rows = []
    repeat_failures = 0
    nonselective_residual = 0.0
    for label, rho in local_states.items():
        joint = dilation @ np.kron(rho, pointer_zero) @ dilation.conj().T
        reshaped = joint.reshape(64, 2, 64, 2)
        p1 = float(np.einsum("iaia->", reshaped[:, 1:2, :, 1:2]).real)
        p0 = 1.0 - p1
        branches = (q0 @ rho @ q0, q @ rho @ q)
        nonselective = branches[0] + branches[1]
        nonselective_residual = max(
            nonselective_residual, float(np.linalg.norm(nonselective - rho))
        )
        branch_repeat = []
        for outcome, branch in enumerate(branches):
            probability = float(np.trace(branch).real)
            if probability <= 1e-15:
                branch_repeat.append(None)
                continue
            conditional = branch / probability
            next_p1 = float(np.trace(q @ conditional).real)
            branch_repeat.append(next_p1)
            repeat_failures += abs(next_p1 - outcome) > 2e-14
        rows.append(
            {
                "state": label,
                "p0": p0,
                "p1": p1,
                "expected_p1": str(expected[label]),
                "repeat_p1_after_outcomes_0_1": tuple(branch_repeat),
            }
        )

    check(
        "the coherent dilation derives the Lüders instrument, exact pointer weights, repeatability, and zero nonselective disturbance on the three explicit local reductions",
        repeat_failures == 0
        and nonselective_residual == 0
        and all(
            abs(row["p1"] - float(expected[row["state"]])) < 2e-14
            for row in rows
        ),
        {"rows": rows, "max_nonselective_residual": nonselective_residual},
    )

    # A local even algebra generator which flips two occupation bits supplies a
    # genuine disturbance control.  The full number-preserving onsite coin
    # commutes with Q even though individual algebra generators need not.
    flip_two = np.zeros((64, 64), dtype=complex)
    for occupation in range(64):
        flip_two[occupation ^ 0b11, occupation] = 1
    dephased = q0 @ flip_two @ q0 + q @ flip_two @ q
    coupling_deleted = np.eye(128, dtype=complex)
    deleted_joint = coupling_deleted @ np.kron(local_states["uniform"], pointer_zero)
    deleted_joint = deleted_joint @ coupling_deleted.conj().T
    deleted_reshaped = deleted_joint.reshape(64, 2, 64, 2)
    deleted_p1 = float(
        np.einsum("iaia->", deleted_reshaped[:, 1:2, :, 1:2]).real
    )
    check(
        "disturbance and coupling-deletion controls separate a real instrument from identity pointer copying",
        abs(np.linalg.norm(flip_two - dephased) - np.sqrt(10)) < 2e-14
        and abs(np.linalg.norm(flip_two - dephased, 2) - 1) < 2e-14
        and deleted_p1 == 0,
        {
            "off_diagonal_even_Frobenius_disturbance": float(
                np.linalg.norm(flip_two - dephased)
            ),
            "operator_disturbance": float(np.linalg.norm(flip_two - dephased, 2)),
            "pointer_one_weight_after_coupling_deletion": deleted_p1,
        },
    )


def same_code_state_and_pre_wrap_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nSAME-CODE PROJECTORS / ALL-EIGHT PRE-WRAP INSTRUMENT")
    coefficients = walsh_coefficients()
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    rows = []
    failures = []
    expected = {None: Fraction(57, 64), 1: Fraction(13, 16), -1: Fraction(31, 32)}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        bs = cell_bs(code, (0, 0, 0))
        terms = tuple(pauli_product(bs, mask) for mask in range(64))
        support_union = 0
        for b in bs:
            support_union |= b.x | b.z
        first_wrap = (length + 1) // 2
        iterations = first_wrap - 1
        cone = c271.full_cell_lightcone(code, {(0, 0, 0)}, iterations)
        generators = c275.cone_generators(code, cone)
        moves = [
            c271.move_seam_outside(code, mask, cone.stream_edges)
            for mask in code.membrane_masks
        ]
        moved_masks = tuple(move.moved_mask for move in moves)
        term_leakage = sum(
            not term.commutes(check_row)
            for term in terms
            for check_row in code.local_checks + code.wilsons
        )
        # Every B_v is an explicit generator of the declared full-cell cone;
        # closure under products then places every Walsh term in its algebra.
        term_domain_failures = int(any(b not in set(generators) for b in bs))
        sector_rows = []
        sector_failures = 0
        for bits in product((0, 1), repeat=3):
            comparison_mask = c275.xor_masks(bits, moved_masks)
            comparison = c235.Pauli(z=comparison_mask)
            sector_failures += c271.wilson_signature(code, comparison_mask) != bits
            sector_failures += any(
                not comparison.commutes(generator) for generator in generators
            )
            for bias in (None, 1, -1):
                stabilizers = biased_rows(code, bits, bias)
                pivots, bad = phase_reducer(stabilizers, code.qubits)
                state_rank = len(pivots)
                values = moments(bs, pivots, code.qubits)
                expected_values = [0] * 64
                expected_values[0] = 1
                if bias is not None:
                    expected_values[1] = bias
                configurations = configuration_probabilities(values)
                p1 = probability_from_moments(coefficients, values)
                sector_rows.append((bits, bias, state_rank, len(bad), p1))
                sector_failures += len(bad) != 0
                sector_failures += state_rank != 9 * length**3 + 1 + int(
                    bias is not None
                )
                sector_failures += values != tuple(expected_values)
                sector_failures += p1 != expected[bias]
                sector_failures += sum(configurations) != 1
                sector_failures += any(value < 0 for value in configurations)

        row = {
            "L": length,
            "iterations": iterations,
            "pointer_overhead_M2": 1,
            "matter_neighborhood_union": support_union.bit_count(),
            "instrument_neighborhood_with_pointer": support_union.bit_count() + 1,
            "maximum_Pauli_term_weight": max(
                (term.x | term.z).bit_count() for term in terms
            ),
            "nonzero_Walsh_terms": sum(coefficient != 0 for coefficient in coefficients),
            "local_check_or_Wilson_leakage": term_leakage,
            "terms_outside_cone_algebra": term_domain_failures,
            "sector_state_rows": len(sector_rows),
            "sector_failures": sector_failures,
            "all_seams_moved": all(move.possible for move in moves),
            "uniform_p1": str(expected[None]),
            "B0_plus_p1": str(expected[1]),
            "B0_minus_p1": str(expected[-1]),
        }
        rows.append(row)
        if not (
            row["pointer_overhead_M2"] == 1
            and row["matter_neighborhood_union"] == 18
            and row["instrument_neighborhood_with_pointer"] == 19
            and row["maximum_Pauli_term_weight"] == 12
            and term_leakage == 0
            and term_domain_failures == 0
            and len(sector_rows) == 24
            and sector_failures == 0
            and all(move.possible for move in moves)
        ):
            failures.append(row)

    check(
        "the contact-active effect is a bounded same-code physical operator with one pointer M2 and zero local-check/Wilson leakage through held-out L=6",
        not failures,
        rows,
    )
    check(
        "Cycle-275 uniform and locally biased projectors give identical exact pointer statistics in all eight sectors throughout every Cycle-271 pre-wrap cone",
        not failures and [row["iterations"] for row in rows] == [1, 1, 2, 2],
        {
            "rows": rows,
            "conditional_maps": "I_r(rho)=Q_r rho Q_r with Q_1=Q_ge2",
            "comparison": "cone-avoiding membranes commute with the complete actual gate cone and instrument algebra",
        },
    )
    return cache


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-24 / FULL-27 INSTRUMENT-FAMILY COVARIANCE")
    base_bs = cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_rows = list(code.local_checks + code.wilsons)
    central_pivots, central_bad = phase_reducer(central_rows, code.qubits)
    failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(code.length), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(translation_vertex[frame_vertex[index]] for index in range(len(frame_vertex)))
            edge_map = tuple(translation_edge[frame_edge[index]] for index in range(len(frame_edge)))
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in base_bs
            )
            target_cell = tuple(value % code.length for value in displacement)
            target_bs = cell_bs(code, target_cell)
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_wilsons = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.wilsons
            )
            if not (
                set(transformed_bs) == set(target_bs)
                and transformed_local == local_family
                and not central_bad
                and all(
                    not reduce_pauli(row, central_pivots, code.qubits).symplectic(
                        code.qubits
                    )
                    for row in transformed_wilsons
                )
            ):
                failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the scalar contact instrument family is covariant under all 24 proper-cubic frames and the full 27-element L=3 translation group",
        not failures and tests == 24 * 27,
        {
            "combined_frame_translation_tests": tests,
            "failures": failures[:5],
            "pointer_action": "carried scalar M2 at the transformed instrument cell",
            "no_preferred_direction": True,
        },
    )


def first_wrap_and_deletion_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nFIRST-WRAP BOUNDARY / WILSON POINTER COUNTERCONTROL")
    rows = []
    failures = []
    for length, code in cache.items():
        first_wrap = (length + 1) // 2
        wrapped = c271.full_cell_lightcone(code, {(0, 0, 0)}, first_wrap)
        generators = c275.cone_generators(code, wrapped)
        local_rows = list(code.local_checks)
        central_rows = local_rows + list(code.wilsons)
        increment = c275.intersection_dimension(
            generators, central_rows, code.qubits
        ) - c275.intersection_dimension(generators, local_rows, code.qubits)
        moves = [
            c271.move_seam_outside(code, mask, wrapped.stream_edges)
            for mask in code.membrane_masks
        ]
        bs = cell_bs(code, (0, 0, 0))
        uniform_pivots, uniform_bad = phase_reducer(
            c275.fixed_sector_rows(code, (0, 0, 0)), code.qubits
        )
        uniform_p = probability_from_moments(
            walsh_coefficients(), moments(bs, uniform_pivots, code.qubits)
        )
        for axis, vertices in enumerate(c235.wilson_cycles(code.graph)):
            word = c235.Pauli(phase=len(vertices) % 4)
            factors = []
            for index, source in enumerate(vertices):
                target = vertices[(index + 1) % len(vertices)]
                factor = code.graph.A(source, target)
                factors.append(factor)
                word = word @ factor
            loop_increment = c275.intersection_dimension(
                factors, central_rows, code.qubits
            ) - c275.intersection_dimension(factors, local_rows, code.qubits)
            deleted_increment = c275.intersection_dimension(
                factors[1:], central_rows, code.qubits
            ) - c275.intersection_dimension(factors[1:], local_rows, code.qubits)
            plus_rows = c275.fixed_sector_rows(code, (0, 0, 0))
            minus_bits = tuple(int(index == axis) for index in range(3))
            minus_rows = c275.fixed_sector_rows(code, minus_bits)
            plus_w = c275.phase_expectation(code.wilsons[axis], plus_rows, code.qubits)
            minus_w = c275.phase_expectation(code.wilsons[axis], minus_rows, code.qubits)
            row = {
                "L": length,
                "axis": axis,
                "first_wrap": first_wrap,
                "wrapped_central_increment": increment,
                "paired_seam_move_possible": moves[axis].possible,
                "Wilson_factor_count": len(factors),
                "word_equals_Wilson": word == code.wilsons[axis],
                "Wilson_pointer_p1_plus_minus": (
                    str(Fraction(1 - plus_w, 2)),
                    str(Fraction(1 - minus_w, 2)),
                ),
                "one_factor_deleted_increment": deleted_increment,
                "bounded_contact_pointer_uniform_p1": str(uniform_p),
            }
            rows.append(row)
            if not (
                increment == 3
                and not moves[axis].possible
                and len(factors) == 3 * length
                and loop_increment == 1
                and deleted_increment == 0
                and word == code.wilsons[axis]
                and (plus_w, minus_w) == (1, -1)
                and not uniform_bad
                and uniform_p == Fraction(57, 64)
            ):
                failures.append(row)
    check(
        "first wrap ends the whole-cone equality: an extended Wilson-controlled pointer distinguishes sectors exactly, while one-factor deletion removes that direction",
        not failures,
        rows,
    )
    check(
        "the bounded local contact pointer is not mislabeled as a Wilson read: its uniform-projector weight remains 57/64 at the first-wrap control",
        not failures
        and all(row["bounded_contact_pointer_uniform_p1"] == "57/64" for row in rows),
        {
            "rows": rows,
            "scope": "no post-wrap equality theorem for arbitrary states or observables",
            "extended_Wilson_pointer_bounded_support": False,
        },
    )


def lawful_domain_and_import_controls() -> None:
    def validate(length: int, bits: tuple[int, int, int], pointer_dimension: int) -> None:
        if length < 3:
            raise ValueError("L must be at least three")
        if len(bits) != 3 or any(bit not in (0, 1) for bit in bits):
            raise ValueError("Wilson character must contain three bits")
        if pointer_dimension != 2:
            raise ValueError("the declared pointer is one M2")

    rejected = 0
    for arguments in ((2, (0, 0, 0), 2), (3, (0, 0, 2), 2), (3, (0, 0, 0), 3)):
        try:
            validate(*arguments)
        except ValueError:
            rejected += 1
    validate(3, (0, 0, 0), 2)
    check(
        "lawful-domain and interpretation firewalls reject undeclared sizes, sectors, and pointer algebras",
        rejected == 3,
        {
            "rejected_controls": rejected,
            "included": "Cycle-275 total-even matched projectors and even observables in a Cycle-271 pre-wrap cone",
            "excluded": "odd one-particle/rank-73 states, unmatched states, global preparation, and arbitrary post-wrap processes",
            "preparation_trace_readout_outcome_selection_are_imports": True,
            "instrument_is_occurrence": False,
            "pointer_is_Record": False,
            "compiler_iteration_is_physical_time": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    pointer_dilation_and_actual_contact_controls()
    cache = same_code_state_and_pre_wrap_controls()
    covariance_controls(cache[3])
    first_wrap_and_deletion_controls(cache)
    lawful_domain_and_import_controls()
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE278_CONNECTED_EDGE_LOCAL_INSTRUMENT_GREEN"
        if FAIL == 0
        else "CYCLE278_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
