#!/usr/bin/env python3
"""Cycle 440: finite Born-proof-basis protected candidate-packet compiler.

Compile the complete Cycle-398 G55[2:8] installed physical menu surface through
the Cycle-436 effect-functional route latch into Cycle-370-compatible protected
candidate packets.  The finite incidence system and its exact rational
nullspace are audited separately from physical packet formation.

The menu family, effect equality key, class codec, routing tables, eligibility,
and grading remain supplied.  Packets are candidates, never actual Records;
no occurrence, probability, Born law, or actualization is selected.
Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
from io import StringIO
from itertools import combinations
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.optimize import linprog
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_exhaustive_finite_grammar_overlap_installation_cycle398_2026_07_18 as c398
import physical_effect_functionality_protected_candidate_record_tournament_cycle436_2026_07_19 as c436


c390 = c398.c390
c385 = c398.c385
c383 = c398.c383
c321 = c398.c321
c317 = c398.c317
c433 = c436.c433
c370 = c436.c370
c364 = c436.c364

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FINITE_BORN_PROOF_BASIS_PROTECTED_PACKET_COMPILER_"
    "CYCLE440_NOTE_2026-07-19.md"
)
C317_NOTE = c317.NOTE
C321_NOTE = c436.C321_NOTE
C383_NOTE = c436.C383_NOTE
C398_NOTE = c398.NOTE
C436_NOTE = c436.NOTE
PR_HEADS = {
    "origin/pr-5472": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
    "origin/pr-5476": "a994617819f57e599dd101c654be366123392236",
    "origin/pr-5479": "84053108a424cef26dc23e484549df331ad2050f",
}
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
CLASS_KEY_DECIMALS = 13
PROGRAMS_PER_BANK = 8
POINTER_M2 = 3
PROGRAM_M2 = 3
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


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
    required = (
        "authority: none",
        "audit: unset",
        "98 physical menu presentations",
        "55 effect-equivalence classes",
        "82 unique incidence rows",
        "13-decimal effect key",
        "same physical effect class, same candidate packet word",
        "inequivalent physical effect classes, distinct candidate packet words",
        "exact integer rank 31",
        "exact nullity 24",
        "21 directions beyond the affine qubit-trace tangent",
        "positive normalized non-trace vector",
        "train l=3",
        "held l=6",
        "all 24 proper-cubic frames",
        "exact e/g",
        "exact inverse",
        "candidate packets are not actual records",
        "no occurrence, probability, or born-law selection",
        "pr #5472",
        "pr #5476",
        "pr #5479",
        "supplied / derived / open",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-440 note freezes the finite protected-packet compiler boundary", not missing, missing)


def source_contract() -> None:
    texts = tuple(normalized(path) for path in (C317_NOTE, C321_NOTE, C383_NOTE, C398_NOTE, C436_NOTE))
    actual_heads = {
        ref: subprocess.check_output(("git", "rev-parse", ref), cwd=ROOT, text=True).strip()
        for ref in PR_HEADS
    }
    check(
        "the physical X1^(8), quotient, finite grammar, and candidate-packet sources remain at their declared scope",
        "x1^(8)" in texts[0]
        and "same coarse cp maps" in texts[1]
        and "fine apparatus labels remain physically visible" in texts[2]
        and "98 menus, 55 classes, rank 31" in texts[3]
        and "candidate packet is not an actual record" in texts[4]
        and actual_heads == PR_HEADS,
        {
            "PR_heads": actual_heads,
            "Cycle317_literal_total_X1_supplied": False,
            "Cycle398_universal_menu_eligibility": False,
            "Cycle436_Record_admission": False,
        },
    )


@dataclass(frozen=True)
class FiniteSurface:
    base: c385.EffectSystem
    installed: c385.EffectSystem
    grammar: c398.GrammarResult
    banks: tuple[c398.CompiledBank, ...]
    programs: dict[int, c390.CompiledMenus]


def fixture_mass_controls(fixtures: dict[int, c317.PhysicalFixture]) -> None:
    rows = []
    for length, fixture in fixtures.items():
        rows.append({
            "L": length,
            "held": length == 6,
            "Gram_residual": float(np.linalg.norm(
                fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - c398.I2
            )),
            "contact_intertwiner_residual": float(np.linalg.norm(
                fixture.physical_contact @ fixture.two_ray_encoding
                - fixture.two_ray_encoding @ fixture.contact
            )),
            "constraint_residual": float(np.linalg.norm(
                fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding
            )),
        })
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    check(
        "the declared train/held physical fixtures satisfy their seam, constraint, and one-particle mass controls",
        all(max(row["Gram_residual"], row["contact_intertwiner_residual"], row["constraint_residual"]) < TOL for row in rows)
        and mass_residual < 3e-12,
        {"rows": rows, "one_particle_mass_relative_residual": mass_residual},
    )


def reconstruct_surface(fixtures: dict[int, c317.PhysicalFixture]) -> FiniteSurface:
    print("\nFINITE G55[2:8] PHYSICAL SURFACE")
    base, _prior, _additional, cycle394 = c398.cycle394_source(fixtures)
    grammar = c398.enumerate_grammar(base.effects)
    existing = c398.existing_grammar_rows(base)
    new_rows = tuple(row for row in grammar.rows if row not in existing)
    banks = c398.compile_banks(base, new_rows, fixtures[3].contact)
    installed = c385.build_effect_system(
        cycle394.menus + c398.bank_presentations(banks),
        effect_functionality_premise=True,
    )
    programs = {
        length: c390.compile_menus(base, installed.menu_classes, fixtures[length].contact)
        for length in (3, 6)
    }
    counts = tuple(sum(len(row) == arity for row in grammar.rows) for arity in range(2, 9))
    pointer_outcomes = sum(map(len, installed.menu_classes))
    bank_counts = tuple(
        min(PROGRAMS_PER_BANK, len(installed.menus) - start)
        for start in range(0, len(installed.menus), PROGRAMS_PER_BANK)
    )
    fixed_isometry = 0.0
    for length in (3, 6):
        for start in range(0, len(installed.menus), PROGRAMS_PER_BANK):
            bank = c398.FixedMenuBank(tuple(programs[length].programs[start:start + PROGRAMS_PER_BANK]))
            fixed_isometry = max(
                fixed_isometry,
                float(np.linalg.norm(bank.update.conj().T @ bank.update - np.eye(16))),
            )
    effect_recovery = max(
        float(np.linalg.norm(effect - base.effects[class_index]))
        for length in (3, 6)
        for program, row in zip(programs[length].programs, installed.menu_classes)
        for effect, class_index in zip(program.coarse_effects, row)
    )
    completeness = max(
        float(np.linalg.norm(program.completeness - c398.I2))
        for compiled in programs.values()
        for program in compiled.programs
    )
    check(
        "all 98 installed menus recompile uniformly into fixed eight-program/eight-pointer physical banks at train and held size",
        installed.incidence.shape == (98, 55)
        and len(grammar.rows) == 82
        and counts == c398.EXPECTED_COUNTS
        and len(new_rows) == 51
        and len(banks) == 7
        and bank_counts == (8,) * 12 + (2,)
        and max(map(len, installed.menu_classes)) == 8
        and effect_recovery < TOL
        and completeness < TOL
        and fixed_isometry < TOL,
        {
            "installed_shape": installed.incidence.shape,
            "unique_grammar_rows": len(grammar.rows),
            "lawful_counts_2_through_8": counts,
            "uniform_fixed_banks": len(bank_counts),
            "programs_per_bank": bank_counts,
            "pointer_outcomes_train": pointer_outcomes,
            "pointer_outcomes_held": pointer_outcomes,
            "maximum_effect_recovery_residual": effect_recovery,
            "maximum_completeness_residual": completeness,
            "maximum_fixed_bank_isometry_residual": fixed_isometry,
            "program_M2": PROGRAM_M2,
            "pointer_M2": POINTER_M2,
        },
    )
    return FiniteSurface(base, installed, grammar, banks, programs)


def equality_class_controls(surface: FiniteSurface) -> dict[str, object]:
    print("\nEFFECT-KEY EQUALITY CLASS AUDIT")
    representatives = surface.installed.effects
    keys = tuple(c383.matrix_key(effect) for effect in representatives)
    groups: list[list[np.ndarray]] = [[] for _ in representatives]
    key_failures = 0
    for menu, classes in zip(surface.installed.menus, surface.installed.menu_classes):
        for effect, class_index in zip(menu.effects, classes):
            groups[class_index].append(np.asarray(effect, dtype=complex))
            key_failures += int(c383.matrix_key(effect) != keys[class_index])
    within = max(
        float(np.linalg.norm(effect - representatives[index]))
        for index, group in enumerate(groups)
        for effect in group
    )
    between = min(
        float(np.linalg.norm(representatives[left] - representatives[right]))
        for left, right in combinations(range(len(representatives)), 2)
    )
    occurrences = tuple(len(group) for group in groups)
    check(
        "the supplied 13-decimal effect key has zero ambiguity on all physical menu occurrences",
        len(keys) == len(set(keys)) == 55
        and key_failures == 0
        and within < TOL
        and between > TOL
        and min(occurrences) > 0,
        {
            "effect_classes": len(representatives),
            "effect_key_decimal_places": CLASS_KEY_DECIMALS,
            "maximum_within_class_Frobenius_dispersion": within,
            "minimum_between_class_Frobenius_gap": between,
            "key_or_class_ambiguities": key_failures,
            "minimum_occurrences_per_class": min(occurrences),
            "maximum_occurrences_per_class": max(occurrences),
        },
    )
    return {"within": within, "between": between, "occurrences": occurrences}


def rational_interior_solution(matrix: sp.Matrix) -> sp.Matrix:
    rows, columns = matrix.shape
    array = np.asarray(matrix.tolist(), dtype=float)
    # Maximize a common two-sided margin t.
    objective = np.zeros(columns + 1)
    objective[-1] = -1
    upper = []
    bound = []
    for index in range(columns):
        row = np.zeros(columns + 1)
        row[index] = -1
        row[-1] = 1
        upper.append(row)
        bound.append(0)
        row = np.zeros(columns + 1)
        row[index] = 1
        row[-1] = 1
        upper.append(row)
        bound.append(1)
    equality = np.hstack((array, np.zeros((rows, 1))))
    result = linprog(
        objective,
        A_ub=np.asarray(upper),
        b_ub=np.asarray(bound),
        A_eq=equality,
        b_eq=np.ones(rows),
        bounds=[(None, None)] * columns + [(0, 0.5)],
        method="highs",
    )
    if not result.success or result.x[-1] <= 1e-5:
        raise RuntimeError("finite incidence surface has no resolved interior point")
    _rref, pivots = matrix.rref()
    free = tuple(index for index in range(columns) if index not in pivots)
    free_values = sp.Matrix([
        sp.Rational(Fraction(float(result.x[index])).limit_denominator(10**6).numerator,
                    Fraction(float(result.x[index])).limit_denominator(10**6).denominator)
        for index in free
    ])
    pivot_matrix = matrix[:, tuple(pivots)]
    free_matrix = matrix[:, free]
    rhs = sp.ones(rows, 1) - free_matrix * free_values
    pivot_values = pivot_matrix.gauss_jordan_solve(rhs)[0]
    answer = sp.zeros(columns, 1)
    for index, value in zip(pivots, pivot_values):
        answer[index] = value
    for index, value in zip(free, free_values):
        answer[index] = value
    if matrix * answer != sp.ones(rows, 1):
        raise RuntimeError("rational interior reconstruction is not exact")
    return answer


def constraint_matrix_controls(surface: FiniteSurface) -> dict[str, object]:
    print("\nEXACT FINITE NORMALIZATION / TRACE-FORM DIAGNOSTIC")
    integer = np.rint(surface.installed.incidence).astype(int)
    matrix = sp.Matrix(integer.tolist())
    rank = int(matrix.rank())
    nullspace = matrix.nullspace()
    nullity = len(nullspace)
    exact_vector = rational_interior_solution(matrix)
    exact_equations = matrix * exact_vector == sp.ones(matrix.rows, 1)
    vector = np.asarray([float(value) for value in exact_vector], dtype=float)
    margin = min(float(np.min(vector)), float(1 - np.max(vector)))
    rational_tuple = tuple(
        f"{int(value.p)}/{int(value.q)}" for value in exact_vector
    )
    vector_hash = sha256(repr(rational_tuple).encode()).hexdigest()
    maximum_numerator = max(abs(int(value.p)) for value in exact_vector)
    maximum_denominator = max(int(value.q) for value in exact_vector)

    effects = surface.installed.effects
    trace_grade = np.asarray([float(np.trace(effect).real / 2) for effect in effects])
    paulis = (c317.X, c317.Y, c317.Z)
    tangent = np.asarray([
        [float(np.trace(pauli @ effect).real / 2) for pauli in paulis]
        for effect in effects
    ])
    tangent_rank = int(np.linalg.matrix_rank(tangent, tol=1e-11))
    tangent_menu_residual = float(np.linalg.norm(integer @ tangent))
    trace_menu_residual = float(np.linalg.norm(integer @ trace_grade - 1))
    coefficients, *_ = np.linalg.lstsq(tangent, vector - trace_grade, rcond=None)
    trace_fit = trace_grade + tangent @ coefficients
    trace_fit_residual = float(np.linalg.norm(vector - trace_fit))
    exact_float_residual = float(np.linalg.norm(integer @ vector - 1))

    # Exhibit one exact rational null direction not contained in the trace tangent.
    outside_residuals = []
    for item in nullspace:
        candidate = np.asarray([float(value) for value in item], dtype=float)
        fit, *_ = np.linalg.lstsq(tangent, candidate, rcond=None)
        outside_residuals.append(float(np.linalg.norm(candidate - tangent @ fit)))
    outside = max(outside_residuals)
    check(
        "the protected physical-menu incidence has exact rank 31/nullity 24 and contains an explicit positive normalized non-trace grade",
        matrix.shape == (98, 55)
        and rank == 31
        and nullity == 24
        and exact_equations
        and margin > 1e-4
        and exact_float_residual < 1e-12
        and tangent_rank == 3
        and tangent_menu_residual < TOL
        and trace_menu_residual < TOL
        and outside > 1e-4
        and trace_fit_residual > 1e-4,
        {
            "matrix_shape": matrix.shape,
            "exact_integer_rank": rank,
            "exact_rational_nullity": nullity,
            "affine_qubit_trace_tangent_rank": tangent_rank,
            "finite_directions_beyond_trace_tangent": nullity - tangent_rank,
            "positive_nontrace_vector_exact_menu_equations": exact_equations,
            "positive_nontrace_vector_float_menu_residual": exact_float_residual,
            "positive_nontrace_vector_two_sided_margin": margin,
            "positive_nontrace_vector_minimum_entry": float(np.min(vector)),
            "positive_nontrace_vector_maximum_entry": float(np.max(vector)),
            "positive_nontrace_vector_SHA256": vector_hash,
            "positive_nontrace_vector_first_five": rational_tuple[:5],
            "positive_nontrace_vector_maximum_abs_numerator": maximum_numerator,
            "positive_nontrace_vector_maximum_denominator": maximum_denominator,
            "positive_nontrace_vector_affine_trace_fit_residual": trace_fit_residual,
            "maximum_exact_null_basis_distance_from_trace_tangent": outside,
            "maximally_mixed_trace_grade_menu_residual": trace_menu_residual,
            "trace_tangent_menu_residual": tangent_menu_residual,
            "interpretation": "coherent finite grade diagnostic only; no numerical grade or probability is selected",
        },
    )
    return {
        "rank": rank,
        "nullity": nullity,
        "margin": margin,
        "trace_fit_residual": trace_fit_residual,
        "vector": exact_vector,
    }


def class_cases(length: int) -> tuple[c433.FormationCase, ...]:
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 6)
    cases = []
    z = 11 if length == 3 else -11
    for class_index in range(55):
        target = (class_index % 11 - 5, class_index // 11 - 2, z)
        predecessor = (target[0] - 1, target[1], target[2])
        cases.append(c433.FormationCase(
            length,
            fixture,
            target,
            predecessor,
            payloads[class_index % len(payloads)],
            payloads[(class_index + 1) % len(payloads)],
            length == 6,
        ))
    return tuple(cases)


def menu_law(row: tuple[int, ...], cases: tuple[c433.FormationCase, ...], index: int) -> c436.CandidateLaw:
    unique = tuple(dict.fromkeys(row))
    block_for_class = {class_index: block for block, class_index in enumerate(unique)}
    return c436.CandidateLaw(
        f"Cycle440 finite effect-functional menu {index}",
        tuple(cases[class_index] for class_index in unique),
        tuple((pointer, block_for_class[class_index]) for pointer, class_index in enumerate(row)),
        True,
        False,
    )


def extract_pointer_word(bank: c436.Bank) -> Word | None:
    words = tuple(word for word in c436.bank_signature(bank) if any(word))
    if not words:
        return None
    if len(words) != 1:
        raise RuntimeError("one pointer branch wrote more than one candidate packet")
    return words[0]


def packet_compiler_controls(surface: FiniteSurface) -> dict[str, object]:
    print("\nALL-98 PHYSICAL POINTER-TO-CANDIDATE-PACKET COMPILER")
    logical = np.asarray((np.sqrt(3 / 8), np.exp(1j * np.pi / 9) * np.sqrt(5 / 8)), dtype=complex)
    cases_by_length = {length: class_cases(length) for length in (3, 6)}
    occurrences = {length: [[] for _ in range(55)] for length in (3, 6)}
    rows = []
    failures = 0
    max_effect = max_completeness = max_forward = max_inverse = 0.0
    max_matcher_leakage = max_workspace = 0
    idle_branches = 0
    active_branches = 0
    for length in (3, 6):
        cases = cases_by_length[length]
        compiled = surface.programs[length]
        for menu_index, (class_row, program) in enumerate(zip(surface.installed.menu_classes, compiled.programs)):
            law = menu_law(class_row, cases, menu_index)
            bank = c436.prepare_bank(c433.LAYOUT, law)
            physical, leakage = c436.physical_pointer_then_law(program, logical, bank, law)
            reference = c436.coarse_then_encode(program, logical, bank, law)
            forward = c436.sparse_residual(physical, reference)
            inverse = c436.sparse_residual(
                c436.inverse_sparse(physical, law),
                c436.input_sparse(program, logical, bank),
            )
            effect_residual = max(
                float(np.linalg.norm(effect - surface.installed.effects[class_index]))
                for effect, class_index in zip(program.coarse_effects, class_row)
            )
            completeness = float(np.linalg.norm(program.completeness - c398.I2))
            for pointer, class_index in enumerate(class_row):
                output, local_leakage = c436.apply_law(bank, pointer, law)
                expected = c436.reference_law(bank, pointer, law)
                restored, inverse_leakage = c436.apply_law(output, pointer, law, reverse=True)
                word = extract_pointer_word(output)
                occurrences[length][class_index].append(word)
                block = next(
                    item for item in output
                    if c436.bank_signature((item,))[0] == word
                )
                block_index = next(
                    mapped for label, mapped in law.label_to_block if label == pointer
                )
                failures += int(
                    output != expected
                    or restored != bank
                    or local_leakage
                    or inverse_leakage
                    or word is None
                    or c433.target_replica(block, law.cases[block_index].fixture)
                    != c433.expected_replica(law.cases[block_index])
                )
                active_branches += 1
                max_matcher_leakage = max(max_matcher_leakage, local_leakage, inverse_leakage)
                max_workspace = max(max_workspace, c436.bank_workspace(output))
            for pointer in range(len(class_row), 8):
                idle, local_leakage = c436.apply_law(bank, pointer, law)
                failures += int(idle != bank or local_leakage)
                idle_branches += 1
            max_effect = max(max_effect, effect_residual)
            max_completeness = max(max_completeness, completeness)
            max_forward = max(max_forward, forward)
            max_inverse = max(max_inverse, inverse)
            failures += int(max(effect_residual, completeness, forward, inverse) > TOL or leakage)
            rows.append({
                "L": length,
                "menu": menu_index,
                "outcomes": len(class_row),
                "unique_packet_blocks": len(set(class_row)),
                "E_G_residual": forward,
                "inverse_residual": inverse,
            })

    equality_failures = separation_failures = 0
    class_hashes = {}
    for length in (3, 6):
        canonical = []
        for class_index, group in enumerate(occurrences[length]):
            equality_failures += int(not group or len(set(group)) != 1)
            canonical.append(group[0])
        separation_failures += int(len(set(canonical)) != 55)
        class_hashes[length] = tuple(c436.sha256(repr(word).encode()).hexdigest() for word in canonical)
    check(
        "every train/held menu branch has exact E/G and inverse, with equal effects sharing and unequal effects separating protected candidate-packet words",
        failures == equality_failures == separation_failures == 0
        and len(rows) == 196
        and active_branches == 2 * sum(map(len, surface.installed.menu_classes))
        and max(max_effect, max_completeness, max_forward, max_inverse) < TOL
        and max_matcher_leakage == max_workspace == 0,
        {
            "menu_length_cases": len(rows),
            "active_pointer_branches": active_branches,
            "idle_pointer_branches": idle_branches,
            "maximum_effect_residual": max_effect,
            "maximum_completeness_residual": max_completeness,
            "maximum_E_G_residual": max_forward,
            "maximum_inverse_residual": max_inverse,
            "maximum_matcher_leakage": max_matcher_leakage,
            "maximum_packet_workspace_leakage": max_workspace,
            "within_class_packet_word_failures": equality_failures,
            "between_class_packet_word_failures": separation_failures,
            "distinct_packet_words_per_length": 55,
            "pointer_remains_physically_present": True,
            "packet_hashes_reported_as_diagnostic_not_identity_rule": {
                length: hashes[:3] for length, hashes in class_hashes.items()
            },
            "failures": failures,
        },
    )
    return {"cases": cases_by_length, "occurrences": occurrences, "rows": rows}


def rotate_cases(
    cases: tuple[c433.FormationCase, ...], frame: np.ndarray
) -> tuple[tuple[c433.FormationCase, ...], int]:
    fixture, mapping, failures = c364.c342.mapped_fixture(cases[0].fixture, frame)
    moved = tuple(c433.FormationCase(
        case.length,
        fixture,
        c433.rotated_coord(case.target, frame),
        c433.rotated_coord(case.predecessor, frame),
        c364.rotate_payload(case.payload, mapping),
        c364.rotate_payload(case.prior_payload, mapping),
        case.held,
    ) for case in cases)
    return moved, failures


def physical_encoding_covariance(
    fixture: c317.PhysicalFixture,
    unique_blocks: tuple[np.ndarray, ...],
) -> tuple[int, float, float]:
    reducer = c317.c311.c305.StabilizerReducer(fixture.code)
    selected = np.zeros((127, 2), dtype=complex)
    selected[
        [c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)] for stream_slice in (0, 1)],
        [0, 1],
    ] = 1
    failures = 0
    maximum_encoding = maximum_block = 0.0
    for frame in c317.c311.c235.proper_cubic_frames():
        logical_r = c317.c311.logical_frame_representation(frame)
        old_r, frame_failures = c317.c311.flagged_frame_representation(
            fixture.encoder, fixture.basis_rows, fixture.occurrence, frame, reducer
        )
        mapping, phases, mapping_failures = c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        carried = fixture.full_encoding @ logical_r @ selected
        mapped = c317.c311.apply_signed_mapping(new_mapping, new_phases, fixture.two_ray_encoding)
        residual = float(np.linalg.norm(mapped - carried))
        maximum_encoding = max(maximum_encoding, residual)
        for block in unique_blocks:
            maximum_block = max(maximum_block, float(np.linalg.norm((mapped - carried) @ block)))
        failures += frame_failures + mapping_failures
    return failures, maximum_encoding, maximum_block


def covariance_resource_controls(
    surface: FiniteSurface,
    packet: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nALL-24 COVARIANCE / RESOURCE ACCOUNT")
    frames = c317.c311.c235.proper_cubic_frames()
    packet_failures = inverse_failures = support_failures = mapping_failures = 0
    packet_cases = 0
    for frame in frames:
        layout = c433.rotated_layout(c433.LAYOUT, frame)
        try:
            c433.validate_layout(layout)
        except ValueError:
            support_failures += 1
        matcher_coords = tuple(c433.rotated_coord(coord, frame) for coord in c436.MATCHER_COORDS)
        support_failures += sum(
            not c436.matcher_support_with_coords(item, matcher_coords)
            for label in range(8)
            for item in c436.matcher_schedule(label)
        )
        support_failures += int(not c436.matcher_support_with_coords(
            c436.matcher_gate("CNOT", (c436.ENABLE_SITE, c436.ROUTE_SITE), "route-latch"),
            matcher_coords,
        ))
        for length in (3, 6):
            moved_cases, failures = rotate_cases(packet["cases"][length], frame)
            mapping_failures += failures
            for class_index, case in enumerate(moved_cases):
                law = c436.CandidateLaw(
                    f"Cycle440 frame class {class_index}", (case,), ((class_index % 8, 0),), True, False
                )
                source = c436.prepare_bank(layout, law)
                pointer = class_index % 8
                output, leakage = c436.apply_law(source, pointer, law)
                restored, inverse_leakage = c436.apply_law(output, pointer, law, reverse=True)
                packet_failures += leakage + int(
                    c433.target_replica(output[0], case.fixture) != c433.expected_replica(case)
                )
                inverse_failures += inverse_leakage + int(restored != source)
                packet_cases += 1

    encoding_rows = []
    for length in (3, 6):
        unique_blocks = tuple(surface.programs[length].unique_blocks.values())
        failures, encoding_residual, block_residual = physical_encoding_covariance(
            fixtures[length], unique_blocks
        )
        encoding_rows.append({
            "L": length,
            "frame_failures": failures,
            "two_ray_encoding_residual": encoding_residual,
            "all_compiled_K_block_residual": block_residual,
            "compiled_unique_effect_blocks": len(unique_blocks),
        })
    pointer_patch = 59
    block_resource = len(c433.LAYOUT.sites) + c436.POINTER_BITS + c436.MATCHER_WORK_M2 + 240
    maximum_menu_blocks = 8
    maximum_bank_resource = PROGRAM_M2 + pointer_patch + maximum_menu_blocks * block_resource
    suite_resource = 13 * maximum_bank_resource
    check(
        "the complete class codec and every compiled effect block are proper-cubic covariant at train and held size with bounded support",
        len(frames) == 24
        and packet_cases == 24 * 2 * 55
        and packet_failures == inverse_failures == support_failures == mapping_failures == 0
        and all(
            row["frame_failures"] == 0
            and row["two_ray_encoding_residual"] < TOL
            and row["all_compiled_K_block_residual"] < TOL
            and row["compiled_unique_effect_blocks"] == 55
            for row in encoding_rows
        ),
        {
            "proper_cubic_frames": len(frames),
            "class_length_frame_packet_cases": packet_cases,
            "packet_failures": packet_failures,
            "inverse_failures": inverse_failures,
            "rotated_support_failures": support_failures,
            "payload_mapping_failures": mapping_failures,
            "physical_encoding_rows": encoding_rows,
            "Cycle433_plus_matcher_router_M2_per_packet_block": block_resource,
            "maximum_simultaneous_packet_blocks": maximum_menu_blocks,
            "maximum_selected_bank_M2": maximum_bank_resource,
            "full_13_bank_suite_M2_conservative_sum": suite_resource,
            "maximum_primitive_support_M2": 3,
            "resource_accounts_are_bounds_not_optimality_claims": True,
        },
    )
    return {"bank_m2": maximum_bank_resource, "suite_m2": suite_resource}


def deletion_domain_controls(
    surface: FiniteSurface,
    packet: dict[str, object],
) -> dict[str, object]:
    print("\nDELETION / LEAKAGE / LAWFUL-DOMAIN CONTROLS")
    row_index = next(index for index, row in enumerate(surface.installed.menu_classes) if len(row) == 8)
    row = surface.installed.menu_classes[row_index]
    cases = packet["cases"][6]
    law = menu_law(row, cases, row_index)
    bank = c436.prepare_bank(c433.LAYOUT, law)
    pointer = 0
    nominal, nominal_leakage = c436.apply_law(bank, pointer, law)

    deleted_matcher, matcher_leakage = c436.apply_law(
        bank, pointer, law, delete_matcher_gate="zero-match-invert:lane0"
    )
    matcher_visible = deleted_matcher != nominal and matcher_leakage == 0

    block_index = next(block for label, block in law.label_to_block if label == pointer)
    desired = c370.encode_replica(law.cases[block_index].fixture, c433.expected_replica(law.cases[block_index]))
    lane = next(index for index in range(24, 54) if desired[index])
    layers, removed = c433.without_gate(c433.LAYOUT.layers, f"field-write:lane{lane}")
    payload_deleted, payload_leakage = c436.apply_law(bank, pointer, law, layers=layers)
    payload_visible = c436.bank_signature(payload_deleted) != c436.bank_signature(nominal)

    program = surface.programs[6].programs[row_index]
    deleted_kraus = (np.zeros_like(program.kraus[0]),) + program.kraus[1:]
    branch_defect = float(np.linalg.norm(
        sum((operator.conj().T @ operator for operator in deleted_kraus), start=np.zeros((2, 2), dtype=complex))
        - c398.I2
    ))

    dropped = c436.CandidateLaw(
        "dropped routing label",
        law.cases,
        tuple(item for item in law.label_to_block if item[0] != pointer),
        True,
        False,
    )
    dropped_output, dropped_leakage = c436.apply_law(bank, pointer, dropped)
    route_deletion_visible = dropped_output == bank and dropped_leakage == 0

    dirty = c436.mutate_target_bit(bank[block_index], 24)
    dirty_bank = tuple(dirty if index == block_index else item for index, item in enumerate(bank))
    dirty_output, dirty_leakage = c436.apply_law(dirty_bank, pointer, law)
    dirty_refused = dirty_output == dirty_bank and dirty_leakage == 0

    occupancy_rejections = 0
    formed_block = nominal[block_index]
    for occupancy_lane in range(c370.OCCUPANCY_BITS):
        corrupted = c436.mutate_target_bit(formed_block, occupancy_lane)
        try:
            c433.target_replica(corrupted, law.cases[block_index].fixture)
        except ValueError:
            occupancy_rejections += 1

    malformed = (
        lambda: menu_law(tuple(range(9)), cases, 0),
        lambda: c436.prepare_bank(c433.LAYOUT, c436.CandidateLaw("absent", (cases[0],), ((0, 1),), True, False)),
        lambda: c436.prepare_bank(c433.LAYOUT, c436.CandidateLaw("duplicate", (cases[0],), ((0, 0), (0, 0)), True, False)),
        lambda: c436.pointer_word(8),
        lambda: c436.apply_law(bank[:-1], pointer, law),
        lambda: c433.prepare(c433.LAYOUT, replace(law.cases[0], payload=law.cases[0].payload[:-1])),
        lambda: c385.build_effect_system((), effect_functionality_premise=True),
        lambda: c385.build_effect_system(surface.installed.menus[:1], effect_functionality_premise=False),
    )
    rejections = 0
    for call in malformed:
        try:
            result = call()
            if isinstance(result, c436.CandidateLaw):
                c436.validate_law(result)
        except (TypeError, ValueError, RuntimeError, IndexError):
            rejections += 1

    check(
        "pointer matcher, packet field, menu branch, class route, protected occupancy, dirty target, and malformed domains are deletion-sensitive",
        nominal_leakage == payload_leakage == 0
        and c436.bank_workspace(nominal) == 0
        and matcher_visible
        and removed == 1
        and payload_visible
        and branch_defect > 1e-3
        and route_deletion_visible
        and dirty_refused
        and occupancy_rejections == c370.OCCUPANCY_BITS
        and rejections == len(malformed),
        {
            "matcher_gate_deletion_visible": matcher_visible,
            "deleted_payload_lane": lane,
            "payload_gate_deletion_visible": payload_visible,
            "physical_outcome_branch_completeness_defect": branch_defect,
            "class_route_deletion_visible": route_deletion_visible,
            "dirty_target_refused": dirty_refused,
            "single_occupancy_fault_rejections": occupancy_rejections,
            "lawful_domain_rejections": rejections,
            "nominal_matcher_leakage": nominal_leakage,
            "nominal_packet_workspace_leakage": c436.bank_workspace(nominal),
        },
    )
    return {"branch_defect": branch_defect, "domain_rejections": rejections}


def premise_inventory_controls(resources: dict[str, object]) -> None:
    print("\nEXACT THEOREM-PREMISE / SUPPLIED-DERIVED-OPEN LEDGER")
    actual_heads = {
        ref: subprocess.check_output(("git", "rev-parse", ref), cwd=ROOT, text=True).strip()
        for ref in PR_HEADS
    }
    ledger = {
        "PR5472_E1": "55 supplied physical effect classes only; not all effects",
        "PR5472_E2": "98 supplied finite menus only; not every finite effect partition",
        "PR5476_F1": "finite overlap subset only; not all scaled projectors",
        "PR5476_F2": "finite overlap subset only; not every scaled-projector menu",
        "PR5479_G1_G2": "finite binary/ternary examples only; not all effect menus",
        "PR5479_X1": "bounded 2:8 pointer presentations only; not total D_mix or arbitrary finite X1",
        "trace_form_fixed_on_finite_basis": False,
        "full_theorem_premise_set_triggered": False,
    }
    inventory = {
        "supplied": (
            "G55[2:8] family bounds, 98 presentations, and program states",
            "13-decimal effect equality key and 55 class representatives",
            "class-to-Cycle364 packet codec and all routing tables",
            "blank local router corridors, protected blocks, and primitive control bits",
            "menu eligibility and any numerical grading",
        ),
        "derived": (
            "train/held physical menu effects, completeness, and fixed-bank isometry",
            "same-class packet identity and different-class packet separation",
            "exact packet E/G, inverse, covariance, and zero nominal leakage",
            "exact integer rank 31 and exact rational nullity 24",
            "positive exact-normalized finite non-trace grade diagnostic",
        ),
        "open": (
            "autonomous family/program/class-codec generation",
            "total E1, F1, or X1 effect domains",
            "universal E2, F2, G1, or G2 eligibility",
            "selected grading, occurrence, actualization, or statistics",
            "probability interpretation, full Born law, or Record admission",
        ),
        "semantic_flags": {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "candidate_packet_is_actual_Record": False,
            "numerical_grade_selected": False,
            "sector_norm_or_menu_sum_called_probability": False,
            "occurrence_probability_or_Born_law_selected": False,
            "axiom_pressure": False,
        },
        "resources": resources,
    }
    check(
        "the exact PR premise boundary and supplied class codec keep the finite physical result below total-domain or statistical claims",
        actual_heads == PR_HEADS
        and not ledger["trace_form_fixed_on_finite_basis"]
        and not ledger["full_theorem_premise_set_triggered"]
        and inventory["semantic_flags"]["authority"] == "none"
        and inventory["semantic_flags"]["audit"] == "unset"
        and not any(
            value for key, value in inventory["semantic_flags"].items()
            if key not in ("authority", "audit")
        ),
        {"PR_heads": actual_heads, "premise_ledger": ledger, "inventory": inventory},
    )


def main() -> None:
    note_contract()
    source_contract()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    fixture_mass_controls(fixtures)
    surface = reconstruct_surface(fixtures)
    equality_class_controls(surface)
    constraint_matrix_controls(surface)
    packet = packet_compiler_controls(surface)
    resources = covariance_resource_controls(surface, packet, fixtures)
    deletion_domain_controls(surface, packet)
    premise_inventory_controls(resources)
    print(f"\nSUMMARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
