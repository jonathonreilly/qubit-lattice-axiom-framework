#!/usr/bin/env python3
"""Cycle 448: exact finite Born-context rank reconstruction.

Reconstruct the Cycle-440 G55 effects in exact pre-contact algebraic
coordinates, separate exact operator equalities from tolerance collisions,
and compile the strongest bounded original-class context extension found by
the width-at-most-four collision scan.  This is a finite grade/additivity
diagnostic.  It selects no state, probability, occurrence, or frequency law.
Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction
from io import StringIO
from itertools import combinations_with_replacement
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_finite_born_proof_basis_protected_packet_compiler_cycle440_2026_07_19 as c440


c398 = c440.c398
c390 = c440.c390
c385 = c440.c385
c436 = c440.c436
c433 = c440.c433
c364 = c440.c364
c317 = c440.c317
I2 = c440.c398.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FINITE_BORN_EXACT_CONTEXT_RANK_RECON_CYCLE448_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
PASS = 0
FAIL = 0


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


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "exact pre-contact algebraic coordinates",
        "rank 31/nullity 24",
        "rank 33/nullity 23",
        "one exact independent original-class relation",
        "e13 + e19 = 2 e33",
        "0.36 i",
        "train l=3",
        "held l=6",
        "all 24 proper-cubic frames",
        "candidate packets are not actual records",
        "coherent norms are not probabilities",
        "no occurrence, probability, frequency, or born-law selection",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo",
        "gate disposition: fail",
        "partial-attempt-with-named-untested-routes",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
        "supplied / derived / open",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-448 note freezes the exact finite rank boundary", not missing, missing)


def projector(scale: sp.Expr, direction: tuple[sp.Expr, sp.Expr, sp.Expr]) -> tuple[sp.Expr, ...]:
    x, y, z = map(sp.sympify, direction)
    norm = sp.sqrt(sp.simplify(x * x + y * y + z * z))
    x, y, z = x / norm, y / norm, z / norm
    return tuple(sp.simplify(item) for item in (
        scale * (1 + z) / 2,
        scale * (1 - z) / 2,
        scale * x / 2,
        -scale * y / 2,
    ))


def unit_projector(scale: sp.Expr, direction: tuple[sp.Expr, sp.Expr, sp.Expr]) -> tuple[sp.Expr, ...]:
    x, y, z = direction
    return tuple(sp.simplify(item) for item in (
        scale * (1 + z) / 2,
        scale * (1 - z) / 2,
        scale * x / 2,
        -scale * y / 2,
    ))


def identity_effect(scale: sp.Expr) -> tuple[sp.Expr, ...]:
    return sp.sympify(scale), sp.sympify(scale), sp.S(0), sp.S(0)


def add_effects(*effects: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(items)) for items in zip(*effects))


def exact_effects() -> tuple[tuple[sp.Expr, ...], ...]:
    """Exact raw effects before the common contact conjugation, in G55 order."""
    q = sp.Rational
    effects: list[tuple[sp.Expr, ...]] = []

    c14 = 2 / (1 + 6 / sp.sqrt(14))
    direction = (1, 2, 3)
    effects.extend((projector(c14 / 2, direction), projector(c14 / 2, (-1, -2, -3))))
    for weight, axis in (
        (c14 / (2 * sp.sqrt(14)), (-1, 0, 0)),
        (c14 / sp.sqrt(14), (0, -1, 0)),
        (3 * c14 / (2 * sp.sqrt(14)), (0, 0, -1)),
    ):
        effects.extend((projector(weight, axis), projector(weight, tuple(-x for x in axis))))
    effects.append(identity_effect(q(1, 2)))
    effects.extend((projector(q(1, 2), (1, -1, 2)), projector(q(1, 2), (-1, 1, -2))))
    effects.extend((
        projector(q(61, 100), (3, -4, 0)),
        projector(q(61, 100), (-3, 4, 0)),
        identity_effect(q(39, 100)),
        projector(q(2257, 10000), (3, -4, 0)),
        projector(q(3843, 10000), (3, -4, 0)),
    ))
    effects.extend((
        unit_projector(q(2, 3), (1, 0, 0)),
        unit_projector(q(2, 3), (-q(1, 2), sp.sqrt(3) / 2, 0)),
        unit_projector(q(2, 3), (-q(1, 2), -sp.sqrt(3) / 2, 0)),
        identity_effect(q(1, 4)),
    ))
    effects.extend((
        projector(1, (2, -3, 6)),
        projector(1, (-2, 3, -6)),
        projector(q(37, 100), (2, -3, 6)),
        projector(q(63, 100), (2, -3, 6)),
    ))

    development = tuple(projector(scale, axis) for scale, axis in (
        (c14, (1, 2, 3)),
        (c14 / sp.sqrt(14), (-1, 0, 0)),
        (2 * c14 / sp.sqrt(14), (0, -1, 0)),
        (3 * c14 / sp.sqrt(14), (0, 0, -1)),
    ))
    effects.extend((*development, add_effects(development[2], development[3])))
    effects.extend((
        projector(q(8, 25), (1, -1, 2)),
        projector(q(8, 25), (-1, 1, -2)),
        projector(q(17, 25), (2, 3, -1)),
        projector(q(17, 25), (-2, -3, 1)),
        identity_effect(q(8, 25)),
        identity_effect(q(17, 25)),
    ))
    effects.extend((
        projector(q(1, 3), (1, 0, 0)),
        projector(q(1, 3), (-1, 0, 0)),
        projector(q(1, 3), (0, 1, 0)),
        projector(q(1, 3), (0, -1, 0)),
        projector(q(1, 3), (0, 0, 1)),
        projector(q(1, 3), (0, 0, -1)),
        identity_effect(q(1, 3)),
    ))
    effects.extend((
        projector(1, (3, -4, 0)),
        projector(1, (-3, 4, 0)),
        projector(q(23, 100), (3, -4, 0)),
        projector(q(77, 100), (3, -4, 0)),
    ))

    c21 = 2 / (1 + 7 / sp.sqrt(21))
    held = tuple(projector(scale, axis) for scale, axis in (
        (c21, (-4, 1, 2)),
        (4 * c21 / sp.sqrt(21), (1, 0, 0)),
        (c21 / sp.sqrt(21), (0, -1, 0)),
        (2 * c21 / sp.sqrt(21), (0, 0, -1)),
    ))
    effects.extend((*held, add_effects(held[2], held[3])))
    effects.extend((
        projector(q(8, 25), (-2, 5, 1)),
        projector(q(8, 25), (2, -5, -1)),
        projector(q(17, 25), (1, 3, -4)),
        projector(q(17, 25), (-1, -3, 4)),
    ))
    if len(effects) != 55:
        raise RuntimeError("exact G55 reconstruction has the wrong size")
    return tuple(effects)


RADICALS = tuple(sp.sqrt(number) for number in (3, 6, 14, 21, 26, 30))


def rational_coefficients(expression: sp.Expr) -> tuple[sp.Rational, ...]:
    expanded = sp.expand(sp.radsimp(expression))
    coefficients = []
    remainder = expanded
    for radical in RADICALS:
        coefficient = sp.simplify(expanded.coeff(radical))
        coefficients.append(coefficient)
        remainder = sp.simplify(remainder - coefficient * radical)
    if not remainder.is_Rational or any(not item.is_Rational for item in coefficients):
        raise ValueError("effect escaped the declared exact radical basis")
    return remainder, *coefficients


def coefficient_lift(effects: tuple[tuple[sp.Expr, ...], ...]) -> sp.Matrix:
    columns = [tuple(value for entry in effect for value in rational_coefficients(entry)) for effect in effects]
    return sp.Matrix(columns).T


def numeric_matrix(effect: tuple[sp.Expr, ...]) -> np.ndarray:
    a, d, x, y = map(complex, effect)
    return np.asarray(((a, x + 1j * y), (x - 1j * y, d)), dtype=complex)


def exact_source_controls(surface: c440.FiniteSurface, fixture: c317.PhysicalFixture) -> dict[str, object]:
    effects = exact_effects()
    contact = fixture.contact
    maximum = max(
        float(np.linalg.norm(numeric_matrix(exact) - contact @ physical @ contact.conj().T))
        for exact, physical in zip(effects, surface.installed.effects)
    )
    lift = coefficient_lift(effects)
    incidence = sp.Matrix(np.rint(surface.installed.incidence).astype(int).tolist())
    rational_relations = sp.Matrix.hstack(*lift.nullspace()).T
    ceiling = incidence.col_join(rational_relations)
    check(
        "the supplied G55 effects have an exact algebraic source reconstruction and an exact fixed-surface rational relation account",
        maximum < TOL
        and lift.shape == (28, 55)
        and lift.rank() == 15
        and len(lift.nullspace()) == 40
        and incidence.rank() == 31
        and ceiling.rank() == 41,
        {
            "exact_precontact_coordinate_rows": lift.rows,
            "exact_rational_coordinate_rank": lift.rank(),
            "exact_rational_operator_relation_dimension": len(lift.nullspace()),
            "physical_backcheck_residual": maximum,
            "Cycle440_exact_rank": incidence.rank(),
            "fixed_G55_rational_relation_ceiling_rank": ceiling.rank(),
            "fixed_G55_projected_old_nullity_at_ceiling": 55 - ceiling.rank(),
        },
    )
    return {"effects": effects, "lift": lift, "incidence": incidence, "ceiling": ceiling}


def add_modular(row: tuple[int, ...], basis: dict[int, list[int]], prime: int = 2147483647) -> bool:
    vector = [int(value) % prime for value in row]
    for pivot in sorted(basis):
        if vector[pivot]:
            factor = vector[pivot]
            source = basis[pivot]
            vector = [(left - factor * right) % prime for left, right in zip(vector, source)]
    try:
        pivot = next(index for index, value in enumerate(vector) if value)
    except StopIteration:
        return False
    inverse = pow(vector[pivot], prime - 2, prime)
    vector = [value * inverse % prime for value in vector]
    for old_pivot, source in tuple(basis.items()):
        if source[pivot]:
            factor = source[pivot]
            basis[old_pivot] = [
                left - factor * right
                for left, right in zip(source, vector)
            ]
            basis[old_pivot] = [value % prime for value in basis[old_pivot]]
    basis[pivot] = vector
    return True


def collision_controls(exact: dict[str, object]) -> dict[str, object]:
    print("\nEXACT WIDTH-AT-MOST-FOUR ORIGINAL-CLASS COLLISIONS")
    effects = exact["effects"]
    lift: sp.Matrix = exact["lift"]
    incidence: sp.Matrix = exact["incidence"]
    independent_rows = sp.Matrix(lift.T).rref()[1]
    keys = []
    for column in range(55):
        values = []
        for row in independent_rows:
            item = lift[row, column]
            values.append(Fraction(int(item.p), int(item.q)))
        keys.append(tuple(values))
    numeric = np.asarray([[float(value) for value in effect] for effect in effects])
    groups: dict[tuple[Fraction, ...], list[tuple[int, ...]]] = defaultdict(list)
    bounded_sums = 0
    for width in range(1, 5):
        for combination in combinations_with_replacement(range(55), width):
            a, d, x, y = numeric[np.asarray(combination)].sum(axis=0)
            if a > 1 + 1e-12 or d > 1 + 1e-12 or (1 - a) * (1 - d) - x * x - y * y < -2e-12:
                continue
            key = tuple(
                sum((keys[index][component] for index in combination), Fraction())
                for component in range(len(independent_rows))
            )
            groups[key].append(combination)
            bounded_sums += 1

    relations: list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for group in groups.values():
        for left_index in range(len(group)):
            for right_index in range(left_index + 1, len(group)):
                left_counts, right_counts = Counter(group[left_index]), Counter(group[right_index])
                common = left_counts & right_counts
                left_counts -= common
                right_counts -= common
                left = tuple(sorted(left_counts.elements()))
                right = tuple(sorted(right_counts.elements()))
                if not left or not right:
                    continue
                vector = [0] * 55
                for index in left:
                    vector[index] += 1
                for index in right:
                    vector[index] -= 1
                canonical = min(tuple(vector), tuple(-value for value in vector))
                if canonical not in seen:
                    seen.add(canonical)
                    relations.append((left, right, tuple(vector)))

    modular_basis: dict[int, list[int]] = {}
    for row in incidence.tolist():
        add_modular(tuple(map(int, row)), modular_basis)
    selected = []
    for relation in sorted(relations, key=lambda item: (
        max(len(item[0]), len(item[1])), len(item[0]) + len(item[1]), item[0], item[1]
    )):
        if add_modular(relation[2], modular_basis):
            selected.append(relation)
    exact_augmented = incidence.col_join(sp.Matrix([selected[0][2]]))
    chosen_left, chosen_right, _vector = selected[0]
    left_matrix = sum((numeric_matrix(effects[index]) for index in chosen_left), np.zeros((2, 2), complex))
    right_matrix = sum((numeric_matrix(effects[index]) for index in chosen_right), np.zeros((2, 2), complex))
    complement = I2 - left_matrix
    collision_residual = float(np.linalg.norm(left_matrix - right_matrix))
    complement_eigenvalues = np.linalg.eigvalsh(complement)
    check(
        "the exhaustive exact bounded multiset scan adds exactly one independent original-class relation",
        bounded_sums == 47198
        and sum(len(group) > 1 for group in groups.values()) == 3982
        and len(relations) == 1011
        and len(selected) == 1
        and chosen_left == (13, 19)
        and chosen_right == (33, 33)
        and exact_augmented.rank() == 32
        and collision_residual < 1e-14
        and np.min(complement_eigenvalues) > 0.35
        and np.max(complement_eigenvalues) < 0.37,
        {
            "bounded_multiset_sums": bounded_sums,
            "exact_collision_keys": sum(len(group) > 1 for group in groups.values()),
            "deduplicated_exact_relations": len(relations),
            "independent_rank_gain": len(selected),
            "projected_old_exact_rank": exact_augmented.rank(),
            "projected_old_nullity": 55 - exact_augmented.rank(),
            "selected_relation": "E13 + E19 = 2 E33",
            "operator_collision_residual": collision_residual,
            "complement_eigenvalues": tuple(map(float, complement_eigenvalues)),
        },
    )
    return {
        "left": chosen_left,
        "right": chosen_right,
        "vector": selected[0][2],
        "complement": complement,
        "relations": tuple(relations),
    }


def extended_incidence_controls(surface: c440.FiniteSurface, collision: dict[str, object]) -> dict[str, object]:
    base = np.rint(surface.installed.incidence).astype(int)
    extended = np.zeros((base.shape[0] + 2, base.shape[1] + 1), dtype=int)
    extended[:base.shape[0], :base.shape[1]] = base
    for index in collision["left"]:
        extended[-2, index] += 1
    for index in collision["right"]:
        extended[-1, index] += 1
    extended[-2:, -1] = 1
    matrix = sp.Matrix(extended.tolist())
    exact_rank = matrix.rank()
    exact_nullity = matrix.cols - exact_rank
    deletion_ranks = tuple(sp.Matrix(np.delete(extended, row, axis=0).tolist()).rank() for row in (-2, -1))
    old_projection_ranks = []
    for rows in (extended, np.delete(extended, -2, axis=0), np.delete(extended, -1, axis=0), extended[:-2]):
        null = sp.Matrix(rows.tolist()).nullspace()
        projected = sp.Matrix.hstack(*(item[:55, :] for item in null)) if null else sp.zeros(55, 0)
        old_projection_ranks.append(projected.rank())
    trace = np.asarray([
        *(float(np.trace(effect).real / 2) for effect in surface.installed.effects),
        float(np.trace(collision["complement"]).real / 2),
    ])
    paulis = (c317.X, c317.Y, c317.Z)
    tangent = np.asarray([
        [float(np.trace(pauli @ effect).real / 2) for pauli in paulis]
        for effect in (*surface.installed.effects, collision["complement"])
    ])
    interior = c440.rational_interior_solution(matrix)
    values = np.asarray([float(item) for item in interior])
    check(
        "the two normalized contexts reduce both full augmented and projected-old grade freedom by exactly one",
        matrix.shape == (100, 56)
        and exact_rank == 33
        and exact_nullity == 23
        and deletion_ranks == (32, 32)
        and tuple(old_projection_ranks) == (23, 24, 24, 24)
        and np.linalg.norm(extended @ trace - 1) < TOL
        and np.linalg.norm(extended @ tangent) < TOL
        and np.min(values) > 1e-5
        and np.max(values) < 1 - 1e-5,
        {
            "augmented_shape": matrix.shape,
            "exact_rank": exact_rank,
            "exact_nullity": exact_nullity,
            "projected_old_nullity": old_projection_ranks[0],
            "single_context_deletion_ranks": deletion_ranks,
            "projected_old_nullity_intact_delete_left_delete_right_delete_pair": tuple(old_projection_ranks),
            "trace_grade_residual": float(np.linalg.norm(extended @ trace - 1)),
            "Pauli_tangent_rank": int(np.linalg.matrix_rank(tangent, tol=1e-11)),
            "Pauli_tangent_residual": float(np.linalg.norm(extended @ tangent)),
            "positive_interior_minimum": float(np.min(values)),
            "positive_interior_maximum": float(np.max(values)),
            "remaining_directions_beyond_Pauli_tangent": exact_nullity - 3,
        },
    )
    return {"matrix": extended, "rank": exact_rank, "nullity": exact_nullity}


def class_cases(length: int, count: int = 56) -> tuple[c433.FormationCase, ...]:
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 6)
    z = 11 if length == 3 else -11
    return tuple(
        c433.FormationCase(
            length,
            fixture,
            (index % 11 - 5, index // 11 - 2, z),
            (index % 11 - 6, index // 11 - 2, z),
            payloads[index % len(payloads)],
            payloads[(index + 1) % len(payloads)],
            length == 6,
        )
        for index in range(count)
    )


def physical_compiler_controls(
    surface: c440.FiniteSurface,
    collision: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nTWO-CONTEXT PHYSICAL COMPILER")
    rows = (tuple((*collision["left"], 55)), tuple((*collision["right"], 55)))
    effects = (*surface.installed.effects, collision["complement"])
    compile_source = replace(surface.base, effects=effects)
    maximum_effect = maximum_completeness = maximum_forward = maximum_inverse = 0.0
    maximum_covariance = maximum_block = 0.0
    packet_failures = pointer_cases = 0
    packet_words: dict[int, list[tuple[int, ...]]] = {3: [], 6: []}
    compiled_by_length = {}
    for length in (3, 6):
        compiled = c390.compile_menus(compile_source, rows, fixtures[length].contact)
        compiled_by_length[length] = compiled
        bank = c398.FixedMenuBank(compiled.programs)
        maximum_completeness = max(
            maximum_completeness,
            *(float(np.linalg.norm(program.completeness - I2)) for program in compiled.programs),
            float(np.linalg.norm(bank.update.conj().T @ bank.update - np.eye(16))),
        )
        cases = class_cases(length)
        logical = np.asarray((np.sqrt(3 / 8), np.exp(1j * np.pi / 9) * np.sqrt(5 / 8)), complex)
        for menu_index, (row, program) in enumerate(zip(rows, compiled.programs)):
            law = c440.menu_law(row, cases, menu_index)
            source = c436.prepare_bank(c433.LAYOUT, law)
            physical, leakage = c436.physical_pointer_then_law(program, logical, source, law)
            reference = c436.coarse_then_encode(program, logical, source, law)
            maximum_forward = max(maximum_forward, c436.sparse_residual(physical, reference))
            maximum_inverse = max(maximum_inverse, c436.sparse_residual(
                c436.inverse_sparse(physical, law), c436.input_sparse(program, logical, source)
            ))
            maximum_effect = max(maximum_effect, *(
                float(np.linalg.norm(effect - effects[index]))
                for effect, index in zip(program.coarse_effects, row)
            ))
            packet_failures += leakage
            for pointer, class_index in enumerate(row):
                output, local_leakage = c436.apply_law(source, pointer, law)
                restored, inverse_leakage = c436.apply_law(output, pointer, law, reverse=True)
                word = c440.extract_pointer_word(output)
                packet_failures += local_leakage + inverse_leakage + int(restored != source or word is None)
                if class_index == 55 and word is not None:
                    packet_words[length].append(word)
                pointer_cases += 1
        failures, encoding, block = c440.physical_encoding_covariance(
            fixtures[length], tuple(compiled.unique_blocks.values())
        )
        packet_failures += failures
        maximum_covariance = max(maximum_covariance, encoding)
        maximum_block = max(maximum_block, block)

    frames = c317.c311.c235.proper_cubic_frames()
    frame_packet_cases = 0
    for frame in frames:
        layout = c433.rotated_layout(c433.LAYOUT, frame)
        c433.validate_layout(layout)
        for length in (3, 6):
            moved, failures = c440.rotate_cases(class_cases(length), frame)
            packet_failures += failures
            for class_index, case in enumerate(moved):
                pointer = class_index % 8
                law = c436.CandidateLaw(
                    f"Cycle448 frame class {class_index}", (case,), ((pointer, 0),), True, False
                )
                source = c436.prepare_bank(layout, law)
                output, leakage = c436.apply_law(source, pointer, law)
                restored, inverse_leakage = c436.apply_law(output, pointer, law, reverse=True)
                packet_failures += leakage + inverse_leakage + int(
                    restored != source
                    or c433.target_replica(output[0], case.fixture) != c433.expected_replica(case)
                )
                frame_packet_cases += 1

    mass = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(mass) / mass.analytic_mass - 1)
    check(
        "both exact contexts compile to protected packets at train/held size with all-24 covariance and the mass fixture preserved",
        pointer_cases == 12
        and frame_packet_cases == 24 * 2 * 56
        and all(len(words) == 2 and words[0] == words[1] for words in packet_words.values())
        and packet_failures == 0
        and max(maximum_effect, maximum_completeness, maximum_forward, maximum_inverse) < TOL
        and max(maximum_covariance, maximum_block) < TOL
        and mass_residual < 3e-12,
        {
            "menus_per_length": 2,
            "maximum_outcomes": 3,
            "active_pointer_cases": pointer_cases,
            "shared_complement_packet_equal_train_held": tuple(
                len(words) == 2 and words[0] == words[1] for words in packet_words.values()
            ),
            "maximum_effect_residual": maximum_effect,
            "maximum_completeness_or_bank_isometry_residual": maximum_completeness,
            "maximum_E_G_residual": maximum_forward,
            "maximum_inverse_residual": maximum_inverse,
            "proper_cubic_frames": len(frames),
            "all_frame_packet_cases": frame_packet_cases,
            "maximum_encoding_covariance_residual": maximum_covariance,
            "maximum_compiled_block_covariance_residual": maximum_block,
            "one_particle_mass_relative_residual": mass_residual,
            "program_M2": 3,
            "pointer_M2": 3,
            "maximum_primitive_support_M2": 3,
        },
    )
    return {"rows": rows, "compiled": compiled_by_length}


def anti_fit_controls(collision: dict[str, object], exact: dict[str, object]) -> None:
    effects = exact["effects"]
    left = sum((numeric_matrix(effects[index]) for index in collision["left"]), np.zeros((2, 2), complex))
    wrong = I2 - left + 0.01 * c317.Z
    wrong_left = float(np.linalg.norm(left + wrong - I2))
    right = sum((numeric_matrix(effects[index]) for index in collision["right"]), np.zeros((2, 2), complex))
    wrong_right = float(np.linalg.norm(right + wrong - I2))
    corrupted = list(collision["vector"])
    corrupted[13] += 1
    exact_failure = any(value != 0 for value in exact["lift"] * sp.Matrix(corrupted))
    check(
        "complement and exact-relation corruptions are visible rather than absorbed by tolerance or fitting",
        wrong_left > 1e-3 and wrong_right > 1e-3 and exact_failure,
        {
            "wrong_complement_left_normalization_residual": wrong_left,
            "wrong_complement_right_normalization_residual": wrong_right,
            "one_coefficient_exact_lift_failure": exact_failure,
        },
    )


def scope_controls() -> None:
    check(
        "the finite rank gain remains grade-only and creates no Born, Record, frequency, no-go, or axiom-pressure claim",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none",
            "frequency_law": "none",
            "Born_state_or_grade_selected": False,
            "fixed_G55_width_four_scan_is_global_no_go": False,
            "shared_substrate_obstruction": "none established",
            "axiom_pressure": "none",
        },
    )


def main() -> None:
    contracts()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    with redirect_stdout(StringIO()):
        surface = c440.reconstruct_surface(fixtures)
    exact = exact_source_controls(surface, fixtures[3])
    collision = collision_controls(exact)
    extended_incidence_controls(surface, collision)
    physical_compiler_controls(surface, collision, fixtures)
    anti_fit_controls(collision, exact)
    scope_controls()
    print("\nSUMMARY")
    print({
        "result": "one exact independent original-class context relation compiled",
        "base_rank_nullity": (31, 24),
        "augmented_rank_nullity": (33, 23),
        "projected_old_nullity": 23,
        "remaining_nontrace_directions": 20,
        "fixed_G55_rational_incidence_ceiling_projected_nullity": 14,
        "no_go_gate": "FAIL; demoted to partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY,
        "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
