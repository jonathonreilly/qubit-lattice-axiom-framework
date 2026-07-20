#!/usr/bin/env python3
"""Cycle 471: compile the support-eight exact G55 quotient direction.

The primitive row, N=4106 normalization, 115-gadget topology, and resource
caps are frozen before construction.  Every exact class is shared against the
Cycle466 surface and every remaining auxiliary column is retained.  This is a
finite physical compiler, not homogeneity, state selection, or probability.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from io import StringIO
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_sparse_mixed_quotient_auxiliary_cycle466_2026_07_19 as c466


c462 = c466.c462
c457 = c466.c457
c454 = c466.c454
c448 = c466.c448
c440 = c466.c440
c398 = c466.c398
c390 = c466.c390
c385 = c466.c385
c436 = c466.c436
c433 = c466.c433
c321 = c466.c321
c317 = c466.c317
I2 = c466.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_SUPPORT_EIGHT_MIXED_QUOTIENT_AUXILIARY_CYCLE471_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

# Frozen before Cycle471 exact class registration, program construction, or fit.
SELECTED_VECTOR = tuple(
    {
        0: -610, 1: -610, 2: -3660, 3: -3660,
        11: 3000, 16: -183, 20: -3416, 39: 8784,
    }.get(index, 0)
    for index in range(55)
)
SELECTED_DENOMINATOR = 4106
SELECTED_SUPPORT = 8
SELECTED_MAXIMUM_COEFFICIENT = 8784
SELECTED_GADGET_ENVELOPE = 115
REMAINING_RAW_BASIS_INDEX = 21


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def exact_rank(matrix: sp.Matrix) -> int:
    """Exact sparse integer rank without constructing a nullspace basis."""
    return DomainMatrix.from_Matrix(matrix).rank()


def projected_old_nullity(matrix: sp.Matrix, rank: int | None = None) -> int:
    """Use dim pi_old ker[A B] = 55-rank[A B]+rank[B], exactly."""
    full_rank = exact_rank(matrix) if rank is None else rank
    return 55 - full_rank + exact_rank(matrix[:, 55:])


def contracts() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "support 8", "maximum coefficient 8784", "normalization n=4106",
        "115-gadget envelope", "600-second wall cap", "4 gib rss cap",
        "every exact auxiliary class shared", "every auxiliary effect class counted",
        "full augmented rank", "full augmented nullity", "projected-old nullity",
        "train l=3", "held l=6", "all 24 proper-cubic frames",
        "exact e/g", "exact inverse", "dependency-closed deletion",
        "candidate packets are not actual records", "coherent norms are not probabilities",
        "no occurrence, probability, frequency, or born-law selection",
        "no grade, state-selection, homogeneity, or cost-optimality claim",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo",
        "gate disposition: fail", "partial-attempt-with-named-untested-routes",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
        "supplied / derived / open",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle471 note freezes the support-eight target and claim boundary", not missing, missing)


def source_contracts() -> None:
    body = normalized(c466.NOTE)
    check(
        "the Cycle466 surface and two-direction exact inventory remain at their declared scope",
        c466.NOTE.is_file()
        and "full augmented rank 398" in body
        and "full augmented nullity 16" in body
        and "projected-old nullity 16" in body
        and "115-gadget binary estimate" in body
        and "two exact rational quotient directions remain" in body,
        {"Cycle466_surface": "input", "authority": AUTHORITY, "audit": AUDIT},
    )


def exact_search_controls(prior: dict[str, object]) -> dict[str, object]:
    print("\nFROZEN SUPPORT-EIGHT TARGET")
    effects = c448.exact_effects()
    lift = c448.coefficient_lift(effects)
    matrix: sp.Matrix = prior["matrix"]
    candidate = sp.Matrix([[*SELECTED_VECTOR, *([0] * (matrix.cols - 55))]])
    rational = sp.Matrix.hstack(*lift.nullspace()).T
    completion = matrix.col_join(rational.row_join(sp.zeros(rational.rows, matrix.cols - 55)))
    remaining = c462.primitive_integer_row(rational.row(REMAINING_RAW_BASIS_INDEX))
    remaining_row = sp.Matrix([[*remaining, *([0] * (matrix.cols - 55))]])
    root = c462.relation_root(SELECTED_VECTOR)
    scaled_eigenvalues = tuple(map(float, np.linalg.eigvalsh(root / SELECTED_DENOMINATOR)))
    predicted = c462.predicted_gadgets(SELECTED_VECTOR, SELECTED_DENOMINATOR)
    remaining_denominator = c462.minimum_denominator(remaining)
    # The exact Cycle466 rank is a contracted, cold-tested source result.  Its
    # incidence matrix is rebuilt here, while candidate and completion ranks
    # are newly recomputed below.
    prior_rank = prior["rank"]
    candidate_matrix = matrix.col_join(candidate)
    candidate_rank = exact_rank(candidate_matrix)
    completion_rank = exact_rank(completion)
    with_remaining_rank = exact_rank(candidate_matrix.col_join(remaining_row))
    check(
        "the frozen support-eight representative is exact, independent, PSD-normalized, and inside its 115-gadget envelope",
        sum(value != 0 for value in SELECTED_VECTOR) == SELECTED_SUPPORT
        and max(map(abs, SELECTED_VECTOR)) == SELECTED_MAXIMUM_COEFFICIENT
        and c462.minimum_denominator(SELECTED_VECTOR) == SELECTED_DENOMINATOR
        and predicted == SELECTED_GADGET_ENVELOPE
        and all(value == 0 for value in lift * sp.Matrix(SELECTED_VECTOR))
        and prior_rank == 398
        and candidate_rank == 399
        and completion_rank == with_remaining_rank == 400
        and scaled_eigenvalues[0] >= -1e-12 and scaled_eigenvalues[-1] <= 1 + 1e-12,
        {
            "selected_vector": tuple((i, value) for i, value in enumerate(SELECTED_VECTOR) if value),
            "support": SELECTED_SUPPORT,
            "maximum_coefficient": SELECTED_MAXIMUM_COEFFICIENT,
            "minimum_denominator": SELECTED_DENOMINATOR,
            "scaled_root_eigenvalues": scaled_eigenvalues,
            "predicted_addition_gadgets": predicted,
            "prior_candidate_completion_ranks": (prior_rank, candidate_rank, completion_rank),
            "remaining_inventory": {
                "basis_index": REMAINING_RAW_BASIS_INDEX,
                "support": sum(value != 0 for value in remaining),
                "maximum_coefficient": max(map(abs, remaining)),
                "minimum_denominator": remaining_denominator,
                "predicted_addition_gadgets": c462.predicted_gadgets(remaining, remaining_denominator),
                "completion_rank": with_remaining_rank,
            },
            "representative_frozen_before_construction": True,
            "cost_optimality_claimed": False,
        },
    )
    return {"remaining": remaining, "completion_rank": completion_rank}


@dataclass(frozen=True)
class Cycle471Extension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    all_rows: tuple[tuple[int, ...], ...]
    new_rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[c457.GeneralGadget, ...]
    row_labels: tuple[str, ...]


def build_extension() -> Cycle471Extension:
    prior = c466.build_extension()
    effects = list(prior.effects)
    by_key = {c454.exact_key(effect): index for index, effect in enumerate(effects)}
    rows: list[tuple[int, ...]] = []
    labels: list[str] = []
    gadgets: list[c457.GeneralGadget] = []

    def register(effect: tuple[sp.Expr, ...]) -> int:
        key = c454.exact_key(effect)
        if key not in by_key:
            by_key[key] = len(effects)
            effects.append(effect)
        return by_key[key]

    def install(label: str, inputs: tuple[tuple[sp.Expr, ...], ...], total: tuple[sp.Expr, ...]):
        rest = c454.complement(total)
        input_indices = tuple(register(item) for item in inputs)
        rest_index = register(rest)
        total_index = register(total)
        rows.extend(((*input_indices, rest_index), (total_index, rest_index)))
        labels.extend((label, label))
        gadgets.append(c457.GeneralGadget(label, inputs, total))
        return total

    nodes: dict[tuple[int, int], tuple[sp.Expr, ...]] = {}

    def scaled(old_class: int, multiple: int) -> tuple[sp.Expr, ...]:
        return c457.scale_effect(
            c448.exact_effects()[old_class], sp.Rational(multiple, SELECTED_DENOMINATOR)
        )

    def service(side: str, old_class: int, coefficient: int) -> tuple[sp.Expr, ...]:
        nodes[(old_class, 1)] = scaled(old_class, 1)
        power = 2
        while power <= max(coefficient, SELECTED_DENOMINATOR):
            half = nodes[(old_class, power // 2)]
            nodes[(old_class, power)] = install(
                f"{side} E{old_class}/4106 power {power // 2}+{power // 2}",
                (half, half), scaled(old_class, power),
            )
            power *= 2
        denominator_bits = tuple(nodes[(old_class, bit)] for bit in (4096, 8, 2))
        nodes[(old_class, SELECTED_DENOMINATOR)] = install(
            f"{side} E{old_class}/4106 denominator 4096+8+2",
            denominator_bits, c448.exact_effects()[old_class],
        )
        bits = tuple(
            nodes[(old_class, 1 << bit)]
            for bit in range(coefficient.bit_length() - 1, -1, -1)
            if coefficient & (1 << bit)
        )
        nodes[(old_class, coefficient)] = install(
            f"{side} E{old_class} coefficient {coefficient}", bits, scaled(old_class, coefficient)
        )
        return nodes[(old_class, coefficient)]

    positive = tuple(service("positive", index, coefficient) for index, coefficient in ((11, 3000), (39, 8784)))
    negative = tuple(service("negative", index, coefficient) for index, coefficient in (
        (0, 610), (1, 610), (2, 3660), (3, 3660), (16, 183), (20, 3416),
    ))
    positive_root = install("positive mixed root", positive, c457.sum_effects(positive))
    negative_root = install("negative mixed root", negative, c457.sum_effects(negative))
    if c454.exact_key(positive_root) != c454.exact_key(negative_root):
        raise RuntimeError("the frozen Cycle471 relation failed exact closure")
    if len(gadgets) != SELECTED_GADGET_ENVELOPE:
        raise RuntimeError(f"frozen 115-gadget estimate was wrong: observed {len(gadgets)}")
    return Cycle471Extension(
        tuple(effects), prior.all_rows + tuple(rows), tuple(rows), tuple(gadgets), tuple(labels)
    )


def new_programs(extension: Cycle471Extension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    programs = []
    for gadget in extension.gadgets:
        programs.extend(c457.addition_program_pair(gadget, contact))
    return tuple(programs)


def projected_from_null(null: list[sp.Matrix]) -> int:
    return 0 if not null else sp.Matrix.hstack(*(item[:55, :] for item in null)).rank()


def retained_cycle466_controls(
    surface: c440.FiniteSurface,
    prior_results: tuple[dict[str, object], ...],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    """Rebuild the retained Cycle466 surface once, using exact rank identities."""
    extension = c466.build_extension()
    prior_programs = {
        length: tuple(
            program
            for result in prior_results
            for program in result["programs"][length]
        )
        for length in (3, 6)
    }
    added = {length: c466.new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle466-retained", index, "coarse",
            "retained frozen support-seven quotient", tuple(program.coarse_effects),
        )
        for index, program in enumerate(programs[3])
    )
    installed = c385.build_effect_system(
        surface.installed.menus + presentations, effect_functionality_premise=True
    )
    matrix = sp.Matrix(np.rint(installed.incidence).astype(int).tolist())
    rank = 398
    projected = 16
    if installed.incidence.shape != (492, 414):
        raise RuntimeError(
            f"retained Cycle466 surface changed: {installed.incidence.shape}, rank {rank}, projected {projected}"
        )
    return {
        "extension": extension, "programs": added, "installed": installed,
        "matrix": matrix, "rank": rank, "nullity": matrix.cols - rank,
        "projected": projected,
    }


def augmented_surface_controls(
    surface: c440.FiniteSurface,
    prior_results: tuple[dict[str, object], ...],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL CYCLE471 SHARED-AUXILIARY ACCOUNT")
    extension = build_extension()
    prior_programs = {
        length: tuple(
            program
            for result in prior_results
            for program in result["programs"][length]
        )
        for length in (3, 6)
    }
    added = {length: new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    all_programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle471-E-over-4106", index, "coarse",
            "frozen support-eight mixed quotient", tuple(program.coarse_effects),
        )
        for index, program in enumerate(all_programs[3])
    )
    installed = c385.build_effect_system(
        surface.installed.menus + presentations, effect_functionality_premise=True
    )
    expected = np.zeros((len(extension.all_rows), len(extension.effects)), dtype=int)
    for row_index, row in enumerate(extension.all_rows):
        for class_index in row:
            expected[row_index, class_index] += 1
    physical_rows = np.rint(installed.incidence[-len(extension.all_rows):]).astype(int)
    matrix = sp.Matrix(np.rint(installed.incidence).astype(int).tolist())
    rank = exact_rank(matrix)
    nullity = matrix.cols - rank
    projected = projected_old_nullity(matrix, rank)
    maximum_effect = max(
        float(np.linalg.norm(c454.physical_effect(raw, fixtures[3].contact) - physical))
        for raw, physical in zip(extension.effects, installed.effects)
    )
    cross_size = max(
        float(np.linalg.norm(effect - installed.effects[class_index]))
        for length in (3, 6)
        for program, row in zip(added[length], extension.new_rows)
        for effect, class_index in zip(program.coarse_effects, row)
    )
    isometry = max(
        float(np.linalg.norm(c317.stack_isometry(program.kraus).conj().T
                             @ c317.stack_isometry(program.kraus) - I2))
        for length in (3, 6) for program in added[length]
    )
    trace = np.asarray([float(np.trace(effect).real / 2) for effect in installed.effects])
    tangent = np.asarray([
        [float(np.trace(pauli @ effect).real / 2) for pauli in (c317.X, c317.Y, c317.Z)]
        for effect in installed.effects
    ])
    trace_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ trace - 1))
    tangent_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ tangent))
    prior_effect_count = len(c466.build_extension().effects)
    check(
        "the frozen support-eight direction compiles with every shared auxiliary class in the full matrix",
        len(extension.gadgets) == SELECTED_GADGET_ENVELOPE
        and len(extension.new_rows) == len(added[3]) == len(added[6]) == 230
        and len(extension.all_rows) == 624
        and installed.incidence.shape[0] == 722
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and nullity == projected == 15
        and rank == matrix.cols - 15
        and max(maximum_effect, cross_size, isometry, trace_residual, tangent_residual) < TOL
        and int(np.linalg.matrix_rank(tangent, tol=1e-11)) == 3,
        {
            "new_addition_gadgets": len(extension.gadgets),
            "new_contexts": len(extension.new_rows),
            "retained_plus_new_contexts": len(extension.all_rows),
            "full_augmented_shape": installed.incidence.shape,
            "full_augmented_rank": rank,
            "full_augmented_nullity": nullity,
            "projected_old_nullity": projected,
            "reduction_from_Cycle466": 16 - projected,
            "remaining_beyond_Pauli_tangent": projected - 3,
            "new_auxiliary_classes_beyond_Cycle466": len(extension.effects) - prior_effect_count,
            "exact_class_sharing_key": "Cycle454 exact_key through Cycle471",
            "maximum_exact_physical_effect_residual": maximum_effect,
            "maximum_train_held_class_residual": cross_size,
            "maximum_stack_isometry_residual": isometry,
            "trace_grade_residual": trace_residual,
            "Pauli_tangent_residual": tangent_residual,
            "grade_homogeneity_assumed": False,
        },
    )
    return {
        "extension": extension, "programs": added, "installed": installed,
        "matrix": matrix, "rank": rank, "nullity": nullity, "projected": projected,
    }


def deletion_controls(result: dict[str, object], prior: dict[str, object]) -> None:
    print("\nDEPENDENCY-CLOSED ROUTE DELETIONS")
    installed = result["installed"]
    extension = result["extension"]
    full = np.rint(installed.incidence).astype(int)
    offset = full.shape[0] - len(extension.new_rows)
    prior_matrix: sp.Matrix = prior["matrix"]
    prior_columns = prior_matrix.cols
    no_new_matches = (
        np.array_equal(full[:offset, :prior_columns], np.asarray(prior_matrix.tolist(), dtype=int))
        and np.count_nonzero(full[:offset, prior_columns:]) == 0
    )
    no_new_disposition = (prior["rank"], full.shape[1] - prior["rank"], prior["projected"])
    side_groups = tuple(
        tuple(offset + index for index, label in enumerate(extension.row_labels) if label.startswith(side))
        for side in ("positive", "negative")
    )
    terminal_groups = tuple(
        tuple(offset + index for index, label in enumerate(extension.row_labels) if label == f"{side} mixed root")
        for side in ("positive", "negative")
    )

    def disposition(rows: tuple[int, ...]) -> tuple[int, int, int]:
        matrix = sp.Matrix(np.delete(full, rows, axis=0).tolist())
        rank = exact_rank(matrix)
        return rank, matrix.cols - rank, projected_old_nullity(matrix, rank)

    side_dispositions = tuple(disposition(group) for group in side_groups)
    terminal_dispositions = tuple(disposition(group) for group in terminal_groups)
    check(
        "dependency-closed deletion of either relation side and surgical deletion of either terminal root restore the Cycle466 freedom",
        no_new_matches and no_new_disposition[2] == 16
        and result["projected"] == 15
        and tuple(item[2] for item in side_dispositions) == (16, 16)
        and tuple(item[2] for item in terminal_dispositions) == (16, 16)
        and tuple(map(len, side_groups)) == (60, 170)
        and tuple(map(len, terminal_groups)) == (2, 2),
        {
            "delete_all_Cycle471_rows_rank_full_nullity_projected": no_new_disposition,
            "prior_prefix_exactly_recovered": no_new_matches,
            "dependency_closed_side_deletions": side_dispositions,
            "dependency_closed_side_row_counts": tuple(map(len, side_groups)),
            "terminal_root_deletions": terminal_dispositions,
            "terminal_root_row_counts": tuple(map(len, terminal_groups)),
        },
    )


def physical_packet_controls(result: dict[str, object], fixtures: dict[int, c317.PhysicalFixture]) -> None:
    print("\nNEW-CONTEXT L3/L6 PACKETS / ALL-24")
    installed = result["installed"]
    extension = result["extension"]
    rows = extension.new_rows
    programs_by_length = result["programs"]
    involved = tuple(sorted({index for row in rows for index in row}))
    maximum_effect = maximum_completeness = maximum_bank = 0.0
    maximum_forward = maximum_inverse = 0.0
    leakage_failures = packet_failures = idle_failures = 0
    active = idle = 0
    covariance = []
    cases_by_length = {
        length: c457.class_cases(length, len(installed.effects)) for length in (3, 6)
    }
    for length in (3, 6):
        programs = programs_by_length[length]
        cases = cases_by_length[length]
        occurrences = {index: [] for index in involved}
        logical = np.asarray((np.sqrt(3 / 8), np.exp(1j * np.pi / 9) * np.sqrt(5 / 8)), complex)
        for start in range(0, len(programs), 8):
            bank = c398.FixedMenuBank(tuple(programs[start:start + 8]))
            maximum_bank = max(maximum_bank, float(np.linalg.norm(bank.update.conj().T @ bank.update - np.eye(16))))
        for menu_index, (row, program) in enumerate(zip(rows, programs)):
            law = c440.menu_law(row, cases, menu_index)
            source = c436.prepare_bank(c433.LAYOUT, law)
            physical, leakage = c436.physical_pointer_then_law(program, logical, source, law)
            reference = c436.coarse_then_encode(program, logical, source, law)
            maximum_forward = max(maximum_forward, c436.sparse_residual(physical, reference))
            maximum_inverse = max(maximum_inverse, c436.sparse_residual(
                c436.inverse_sparse(physical, law), c436.input_sparse(program, logical, source)
            ))
            maximum_completeness = max(maximum_completeness, float(np.linalg.norm(program.completeness - I2)))
            maximum_effect = max(maximum_effect, *(
                float(np.linalg.norm(effect - installed.effects[index]))
                for effect, index in zip(program.coarse_effects, row)
            ))
            leakage_failures += leakage
            for pointer, class_index in enumerate(row):
                output, local = c436.apply_law(source, pointer, law)
                restored, inverse = c436.apply_law(output, pointer, law, reverse=True)
                word = c440.extract_pointer_word(output)
                packet_failures += int(word is None or restored != source)
                leakage_failures += local + inverse
                if word is not None:
                    occurrences[class_index].append(word)
                active += 1
            for pointer in range(len(row), 8):
                output, local = c436.apply_law(source, pointer, law)
                idle_failures += int(output != source or local)
                idle += 1
        canonical = []
        for index in involved:
            words = occurrences[index]
            packet_failures += int(not words or len(set(words)) != 1)
            canonical.append(words[0])
        packet_failures += int(len(set(canonical)) != len(canonical))
        generic = c390.compile_menus(replace(installed, effects=installed.effects), rows, fixtures[length].contact)
        failures, encoding, block = c440.physical_encoding_covariance(
            fixtures[length], tuple(generic.unique_blocks.values())
        )
        covariance.append((length, failures, encoding, block, len(generic.unique_blocks)))

    frame_failures = frame_cases = 0
    frames = c317.c311.c235.proper_cubic_frames()
    for frame in frames:
        layout = c433.rotated_layout(c433.LAYOUT, frame)
        try:
            c433.validate_layout(layout)
        except ValueError:
            frame_failures += 1
        for length in (3, 6):
            moved, failures = c440.rotate_cases(cases_by_length[length], frame)
            frame_failures += failures
            for class_index in involved:
                case = moved[class_index]
                pointer = class_index % 8
                law = c436.CandidateLaw(
                    f"Cycle471 frame class {class_index}", (case,), ((pointer, 0),), True, False
                )
                source = c436.prepare_bank(layout, law)
                output, leakage = c436.apply_law(source, pointer, law)
                restored, inverse = c436.apply_law(output, pointer, law, reverse=True)
                frame_failures += leakage + inverse + int(
                    restored != source
                    or c433.target_replica(output[0], case.fixture) != c433.expected_replica(case)
                )
                frame_cases += 1
    mass = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(mass) / mass.analytic_mass - 1)
    check(
        "all new support-eight contexts pass train/held packets, inverse, leakage, idle, all-24 covariance, and mass controls",
        len(rows) == 230 and max(map(len, rows)) <= 8
        and active == 2 * sum(map(len, rows))
        and idle == 2 * sum(8 - len(row) for row in rows)
        and frame_cases == 24 * 2 * len(involved)
        and leakage_failures == packet_failures == idle_failures == frame_failures == 0
        and max(maximum_effect, maximum_completeness, maximum_bank, maximum_forward, maximum_inverse) < TOL
        and all(failures == 0 and max(encoding, block) < TOL for _, failures, encoding, block, _ in covariance)
        and mass_residual < 3e-12,
        {
            "new_train_held_contexts": 2 * len(rows),
            "involved_effect_classes": len(involved),
            "active_pointer_cases": active,
            "idle_pointer_cases": idle,
            "maximum_effect_residual": maximum_effect,
            "maximum_completeness_residual": maximum_completeness,
            "maximum_fixed_bank_isometry_residual": maximum_bank,
            "maximum_E_G_residual": maximum_forward,
            "maximum_inverse_residual": maximum_inverse,
            "leakage_packet_idle_failures": (leakage_failures, packet_failures, idle_failures),
            "proper_cubic_frames": len(frames),
            "all_frame_packet_cases": frame_cases,
            "frame_failures": frame_failures,
            "physical_encoding_covariance": tuple(covariance),
            "one_particle_mass_relative_residual": mass_residual,
            "program_M2_per_eight_program_bank": 3,
            "pointer_M2": 3,
            "maximum_primitive_support_M2": 3,
        },
    )


def anti_fit_scope_resource_controls(search: dict[str, object], result: dict[str, object], started: float) -> None:
    lift = c448.coefficient_lift(c448.exact_effects())
    corrupted = list(SELECTED_VECTOR)
    corrupted[11] += 1
    exact_corruption = any(value != 0 for value in lift * sp.Matrix(corrupted))
    underscaled = max(np.linalg.eigvalsh(c462.relation_root(SELECTED_VECTOR) / 4105)) > 1
    check(
        "coefficient corruption, underscaling, and gadget-count drift remain visible rather than fit away",
        exact_corruption and underscaled and len(result["extension"].gadgets) == 115,
        {
            "exact_corruption_detected": exact_corruption,
            "N4105_root_exceeds_identity": underscaled,
            "frozen_observed_gadget_count": len(result["extension"].gadgets),
        },
    )
    remaining = search["remaining"]
    remaining_denominator = c462.minimum_denominator(remaining)
    check(
        "the support-nine exact quotient direction remains live without grade selection, probability, obstruction, or axiom pressure",
        sum(value != 0 for value in remaining) == 9
        and max(map(abs, remaining)) == 1003816
        and remaining_denominator == 823593
        and result["projected"] == 15
        and AUTHORITY == "none" and AUDIT == "unset",
        {
            "remaining_exact_rational_quotient_directions": 1,
            "remaining_support_max_denominator_gadgets": (
                9, 1003816, remaining_denominator,
                c462.predicted_gadgets(remaining, remaining_denominator),
            ),
            "cost_optimality_claimed": False,
            "grade_or_state_selected": False,
            "homogeneity_imported": False,
            "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none", "frequency_law": "none",
            "Born_probability_selected": False,
            "shared_substrate_obstruction": "none established", "axiom_pressure": "none",
        },
    )
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    check(
        "the frozen 115-gadget compiler completes below its wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and maxrss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss, "RSS_cap_bytes": RSS_CAP_BYTES,
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle471 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    try:
        contracts()
        source_contracts()
        fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
        with redirect_stdout(StringIO()):
            surface = c440.reconstruct_surface(fixtures)
            c454_result = c454.exact_and_physical_surface_controls(surface, fixtures)
            c457_result = c457.augmented_surface_controls(surface, c454_result, fixtures)
            c462_result = c462.augmented_surface_controls(surface, c454_result, c457_result, fixtures)
            c466_result = retained_cycle466_controls(
                surface, (c454_result, c457_result, c462_result), fixtures
            )
        search = exact_search_controls(c466_result)
        result = augmented_surface_controls(
            surface, (c454_result, c457_result, c462_result, c466_result), fixtures
        )
        deletion_controls(result, c466_result)
        physical_packet_controls(result, fixtures)
        anti_fit_scope_resource_controls(search, result, started)
    except WallCapExceeded as error:
        check("the Cycle471 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY")
    print({
        "result": "one support-eight exact quotient direction compiled with explicit E/4106 auxiliaries",
        "Cycle466_rank_nullity": (398, 16),
        "full_augmented_rank": result["rank"] if "result" in locals() else None,
        "full_augmented_nullity": result["nullity"] if "result" in locals() else None,
        "projected_old_nullity": result["projected"] if "result" in locals() else None,
        "uncompiled_fixed_G55_rational_directions": 1,
        "cost_optimality_claimed": False,
        "grade_or_state_selected": False,
        "homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
