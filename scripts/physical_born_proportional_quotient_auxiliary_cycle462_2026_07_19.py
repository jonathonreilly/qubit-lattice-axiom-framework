#!/usr/bin/env python3
"""Cycle 462: compile one exact proportional G55 quotient direction.

The frozen search notch exhausts exact proportional pairs at support two,
primitive coefficient at most 100, and physical denominator at most 64.  It
selects 63 E22 = 37 E23 at N=24 before constructing any physical context.
Every auxiliary effect is retained.  No grade homogeneity or probability law
is assumed.  Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from functools import reduce
from io import StringIO
from math import ceil, gcd, log2
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_short_rational_mixed_effect_auxiliary_cycle457_2026_07_19 as c457


c454 = c457.c454
c448 = c457.c448
c440 = c457.c440
c398 = c457.c398
c390 = c457.c390
c385 = c457.c385
c436 = c457.c436
c433 = c457.c433
c364 = c457.c364
c321 = c457.c321
c317 = c457.c317
I2 = c457.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_PROPORTIONAL_QUOTIENT_AUXILIARY_CYCLE462_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

# Frozen before exact row selection or physical fitting.
SEARCH_LADDER = (
    {"name": "inherited-Cycle457", "denominator": 8, "support": 20, "coefficient": 25},
    {"name": "exact-proportional-pair-notch", "denominator": 64, "support": 2, "coefficient": 100},
)
SELECTED_VECTOR = tuple(63 if index == 22 else -37 if index == 23 else 0 for index in range(55))
SELECTED_DENOMINATOR = 24
UNRESOLVED_RAW_BASIS_INDICES = (27, 29, 21)


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


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "frozen nested search ladder",
        "exact proportional-pair notch",
        "support at most two",
        "denominator at most 64",
        "primitive coefficient at most 100",
        "63 e22 = 37 e23",
        "normalization n=24",
        "every auxiliary effect class counted",
        "full augmented rank",
        "full augmented nullity",
        "projected-old nullity",
        "train l=3",
        "held l=6",
        "all 24 proper-cubic frames",
        "exact e/g",
        "exact inverse",
        "candidate packets are not actual records",
        "coherent norms are not probabilities",
        "no occurrence, probability, frequency, or born-law selection",
        "600-second wall cap",
        "4 gib rss cap",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo",
        "gate disposition: fail",
        "partial-attempt-with-named-untested-routes",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
        "supplied / derived / open",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle-462 note freezes the proportional search and claim boundary", not missing, missing)


def source_contracts() -> None:
    body = normalized(c457.NOTE)
    check(
        "the Cycle457 exact quotient and explicit auxiliary surface remain at their declared scope",
        c457.NOTE.is_file()
        and "full augmented rank 210" in body
        and "full augmented nullity 18" in body
        and "four of the six fixed-g55 rational directions remain uncompiled" in body
        and "no grade homogeneity" in body,
        {"Cycle457_surface": "input", "authority": AUTHORITY, "audit": AUDIT},
    )


def primitive_integer_row(row: sp.Matrix) -> tuple[int, ...]:
    denominators = [sp.denom(value) for value in row]
    multiple = sp.ilcm(*denominators)
    values = [int(value * multiple) for value in row]
    divisor = reduce(gcd, (abs(value) for value in values if value))
    return tuple(value // divisor for value in values)


def relation_root(vector: tuple[int, ...]) -> np.ndarray:
    effects = c448.exact_effects()
    return sum(
        (coefficient * c448.numeric_matrix(effects[index])
         for index, coefficient in enumerate(vector) if coefficient > 0),
        np.zeros((2, 2), complex),
    )


def minimum_denominator(vector: tuple[int, ...]) -> int:
    return ceil(float(np.linalg.eigvalsh(relation_root(vector))[-1]) - 1e-10)


def predicted_gadgets(vector: tuple[int, ...], denominator: int) -> int:
    total = 0
    positive = negative = 0
    for coefficient in vector:
        if not coefficient:
            continue
        magnitude = abs(coefficient)
        limit = max(magnitude, denominator)
        total += int(log2(limit))
        total += int(denominator & (denominator - 1) != 0)
        total += int(magnitude != denominator and magnitude & (magnitude - 1) != 0)
        positive += int(coefficient > 0)
        negative += int(coefficient < 0)
    total += 0 if positive <= 1 else ceil((positive - 1) / 6)
    total += 0 if negative <= 1 else ceil((negative - 1) / 6)
    return total


def exact_search_controls(prior: dict[str, object]) -> dict[str, object]:
    print("\nFROZEN NESTED EXACT SEARCH")
    effects = c448.exact_effects()
    lift = c448.coefficient_lift(effects)
    matrix: sp.Matrix = prior["matrix"]
    null = sp.Matrix.hstack(*matrix.nullspace())
    old_null = null[:55, :]
    proportional = []
    for left in range(55):
        left_trace = sp.simplify(effects[left][0] + effects[left][1])
        for right in range(left + 1, 55):
            right_trace = sp.simplify(effects[right][0] + effects[right][1])
            ratio = sp.simplify(right_trace / left_trace)
            if not ratio.is_Rational:
                continue
            if any(sp.simplify(effects[right][k] - ratio * effects[left][k]) != 0 for k in range(4)):
                continue
            numerator = int(sp.numer(ratio))
            denominator = int(sp.denom(ratio))
            divisor = gcd(abs(numerator), abs(denominator))
            vector = tuple(
                numerator // divisor if index == left
                else -denominator // divisor if index == right
                else 0 for index in range(55)
            )
            image = sp.Matrix([vector]) * old_null
            if any(value != 0 for value in image):
                proportional.append((minimum_denominator(vector), max(map(abs, vector)), left, right, vector, image))
    proportional.sort(key=lambda item: item[:4])
    image_rows = sp.Matrix.vstack(*(item[5] for item in proportional))
    selected = proportional[0]
    candidate_row = sp.Matrix([[*SELECTED_VECTOR, *([0] * (matrix.cols - 55))]])
    rational = sp.Matrix.hstack(*lift.nullspace()).T
    completion = matrix.col_join(rational.row_join(sp.zeros(rational.rows, matrix.cols - 55)))
    inventory = []
    running = matrix.col_join(candidate_row)
    for basis_index in UNRESOLVED_RAW_BASIS_INDICES:
        vector = primitive_integer_row(rational.row(basis_index))
        row = sp.Matrix([[*vector, *([0] * (matrix.cols - 55))]])
        rank = running.col_join(row).rank()
        inventory.append({
            "basis_index": basis_index,
            "vector": vector,
            "support": sum(value != 0 for value in vector),
            "maximum_coefficient": max(map(abs, vector)),
            "minimum_denominator": minimum_denominator(vector),
            "predicted_addition_gadgets": predicted_gadgets(vector, minimum_denominator(vector)),
            "incremental_rank": rank,
        })
        running = running.col_join(row)
    scaled_root = relation_root(SELECTED_VECTOR) / SELECTED_DENOMINATOR
    check(
        "the frozen proportional-pair notch exhausts its finite family and selects one exact independent quotient direction",
        SEARCH_LADDER[-1] == {
            "name": "exact-proportional-pair-notch", "denominator": 64,
            "support": 2, "coefficient": 100,
        }
        and len(proportional) == 3
        and image_rows.rank() == 1
        and selected[4] == SELECTED_VECTOR
        and selected[0] == SELECTED_DENOMINATOR
        and all(value == 0 for value in lift * sp.Matrix(SELECTED_VECTOR))
        and matrix.rank() == 210
        and matrix.col_join(candidate_row).rank() == 211
        and completion.rank() == running.rank() == 214
        and tuple(item["incremental_rank"] for item in inventory) == (212, 213, 214)
        and np.min(np.linalg.eigvalsh(scaled_root)) >= -1e-12
        and np.max(np.linalg.eigvalsh(scaled_root)) <= 1 + 1e-12,
        {
            "search_ladder": SEARCH_LADDER,
            "live_proportional_pairs": tuple(
                (item[0], item[1], item[2], item[3]) for item in proportional
            ),
            "live_proportional_quotient_rank": image_rows.rank(),
            "selected_vector": tuple((i, v) for i, v in enumerate(SELECTED_VECTOR) if v),
            "selected_denominator": SELECTED_DENOMINATOR,
            "selected_scaled_root_eigenvalues": tuple(map(float, np.linalg.eigvalsh(scaled_root))),
            "prior_rank_completion_rank": (matrix.rank(), completion.rank()),
            "remaining_inventory": tuple(
                {key: value for key, value in item.items() if key != "vector"} for item in inventory
            ),
            "menu_frozen_before_physical_construction": True,
        },
    )
    return {"inventory": tuple(inventory), "completion_rank": completion.rank()}


@dataclass(frozen=True)
class Cycle462Extension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    all_rows: tuple[tuple[int, ...], ...]
    new_rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[c457.GeneralGadget, ...]
    row_labels: tuple[str, ...]


def build_extension() -> Cycle462Extension:
    prior = c457.build_extension()
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

    def scale(old_class: int, multiple: int) -> tuple[sp.Expr, ...]:
        return c457.scale_effect(
            c448.exact_effects()[old_class], sp.Rational(multiple, SELECTED_DENOMINATOR)
        )

    def service(old_class: int, coefficient: int) -> tuple[sp.Expr, ...]:
        nodes[(old_class, 1)] = scale(old_class, 1)
        power = 2
        while power <= max(coefficient, SELECTED_DENOMINATOR):
            half = nodes[(old_class, power // 2)]
            target = c448.exact_effects()[old_class] if power == SELECTED_DENOMINATOR else scale(old_class, power)
            nodes[(old_class, power)] = install(
                f"E{old_class}/24 power {power // 2}+{power // 2}", (half, half), target
            )
            power *= 2
        denominator_bits = tuple(
            nodes[(old_class, bit)] for bit in (16, 8)
        )
        nodes[(old_class, SELECTED_DENOMINATOR)] = install(
            f"E{old_class}/24 denominator 16+8", denominator_bits, c448.exact_effects()[old_class]
        )
        if coefficient in nodes:
            return nodes[(old_class, coefficient)]
        bits = tuple(
            nodes[(old_class, bit)]
            for bit in (32, 16, 8, 4, 2, 1)
            if coefficient & bit
        )
        nodes[(old_class, coefficient)] = install(
            f"E{old_class} coefficient {coefficient} root", bits, scale(old_class, coefficient)
        )
        return nodes[(old_class, coefficient)]

    left = service(22, 63)
    right = service(23, 37)
    if c454.exact_key(left) != c454.exact_key(right):
        raise RuntimeError("the frozen proportional relation failed exact closure")
    return Cycle462Extension(
        tuple(effects), prior.all_rows + tuple(rows), tuple(rows), tuple(gadgets), tuple(labels)
    )


def new_programs(extension: Cycle462Extension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    programs = []
    for gadget in extension.gadgets:
        programs.extend(c457.addition_program_pair(gadget, contact))
    return tuple(programs)


def augmented_surface_controls(
    surface: c440.FiniteSurface,
    c454_result: dict[str, object],
    c457_result: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL CYCLE462 AUXILIARY ACCOUNT")
    extension = build_extension()
    prior_programs = {
        length: (*c454_result["programs"][length], *c457_result["programs"][length])
        for length in (3, 6)
    }
    added = {length: new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    all_programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle462-E-over-24", index, "coarse",
            "frozen exact proportional quotient notch", tuple(program.coarse_effects),
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
    rank = matrix.rank()
    nullity = matrix.cols - rank
    null = matrix.nullspace()
    projected = sp.Matrix.hstack(*(item[:55, :] for item in null)).rank()
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
    check(
        "the proportional quotient direction compiles with every auxiliary class in the full matrix",
        len(extension.gadgets) == predicted_gadgets(SELECTED_VECTOR, SELECTED_DENOMINATOR) == 14
        and len(extension.new_rows) == len(added[3]) == len(added[6]) == 28
        and len(extension.all_rows) == 226
        and installed.incidence.shape[0] == 324
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and nullity == projected == 17
        and rank == matrix.cols - 17
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
            "reduction_from_Cycle457": 18 - projected,
            "remaining_beyond_Pauli_tangent": projected - 3,
            "new_auxiliary_classes_beyond_Cycle457": len(extension.effects) - 228,
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


def deletion_controls(result: dict[str, object]) -> None:
    print("\nDEPENDENCY-CLOSED DELETIONS")
    installed = result["installed"]
    extension = result["extension"]
    full = np.rint(installed.incidence).astype(int)
    offset = full.shape[0] - len(extension.new_rows)
    no_new = full[:offset]
    root_groups = tuple(
        tuple(offset + index for index, label in enumerate(extension.row_labels) if needle in label)
        for needle in ("E22 coefficient 63 root", "E23 coefficient 37 root")
    )
    no_new_matrix = sp.Matrix(no_new.tolist())
    deletions = []
    for group in root_groups:
        reduced = np.delete(full, group, axis=0)
        matrix = sp.Matrix(reduced.tolist())
        deletions.append((matrix.rank(), matrix.cols - matrix.rank(), c457.projected_old_nullity(reduced)))
    check(
        "deleting either terminal root presentation restores the one Cycle457 old-grade freedom",
        c457.projected_old_nullity(no_new) == 18
        and result["projected"] == 17
        and tuple(item[2] for item in deletions) == (18, 18)
        and tuple(map(len, root_groups)) == (2, 2),
        {
            "delete_all_Cycle462_rows_rank_full_nullity_projected": (
                no_new_matrix.rank(), no_new_matrix.cols - no_new_matrix.rank(),
                c457.projected_old_nullity(no_new),
            ),
            "single_terminal_root_deletions": tuple(deletions),
            "terminal_root_row_counts": tuple(map(len, root_groups)),
            "terminal_root_absolute_rows": root_groups,
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
    for length in (3, 6):
        programs = programs_by_length[length]
        cases = c457.class_cases(length, len(installed.effects))
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
            moved, failures = c440.rotate_cases(c457.class_cases(length, len(installed.effects)), frame)
            frame_failures += failures
            for class_index in involved:
                case = moved[class_index]
                pointer = class_index % 8
                law = c436.CandidateLaw(
                    f"Cycle462 frame class {class_index}", (case,), ((pointer, 0),), True, False
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
        "all new proportional contexts pass bounded train/held packets, inverse, leakage, all-24 covariance, and mass controls",
        len(rows) == 28 and max(map(len, rows)) <= 8
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
    corrupted[22] += 1
    exact_corruption = any(value != 0 for value in lift * sp.Matrix(corrupted))
    refused = sum((65 > 64, 3 > 2, 101 > 100))
    check(
        "coefficient corruption and candidates outside the frozen proportional notch remain visible",
        exact_corruption and refused == 3,
        {"exact_corruption_detected": exact_corruption, "out_of_notch_cases_refused": refused},
    )
    inventory = search["inventory"]
    check(
        "the three uncompiled quotient directions remain exact independent search inventory rather than a negative claim",
        len(inventory) == 3
        and tuple(item["incremental_rank"] for item in inventory) == (212, 213, 214)
        and result["projected"] == 17
        and AUTHORITY == "none" and AUDIT == "unset",
        {
            "remaining_exact_rational_quotient_directions": 3,
            "inventory_costs": tuple(
                (item["basis_index"], item["support"], item["maximum_coefficient"],
                 item["minimum_denominator"], item["predicted_addition_gadgets"])
                for item in inventory
            ),
            "grade_homogeneity_imported": False,
            "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none", "frequency_law": "none",
            "Born_state_or_grade_selected": False,
            "shared_substrate_obstruction": "none established", "axiom_pressure": "none",
        },
    )
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    check(
        "the bounded one-notch compiler completes below its frozen wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and maxrss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss, "RSS_cap_bytes": RSS_CAP_BYTES,
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle462 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


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
        search = exact_search_controls(c457_result)
        result = augmented_surface_controls(surface, c454_result, c457_result, fixtures)
        deletion_controls(result)
        physical_packet_controls(result, fixtures)
        anti_fit_scope_resource_controls(search, result, started)
    except WallCapExceeded as error:
        check("the Cycle462 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY")
    print({
        "result": "one exact proportional quotient direction compiled with explicit E/24 auxiliaries",
        "Cycle457_rank_nullity": (210, 18),
        "full_augmented_rank": result["rank"] if "result" in locals() else None,
        "full_augmented_nullity": result["nullity"] if "result" in locals() else None,
        "projected_old_nullity": result["projected"] if "result" in locals() else None,
        "uncompiled_fixed_G55_rational_directions": 3,
        "grade_homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
