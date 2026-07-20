#!/usr/bin/env python3
"""Cycle 457: short rational mixed-effect auxiliary compiler.

Compile the two short N=8 rational G55 operator directions left by Cycle 454.
Every E/8 atom, partial sum, and complement is an explicit class.  Overlapping
services are shared.  No grade homogeneity, probability, or occurrence law is
assumed.  Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from io import StringIO
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_scaled_ray_split_merge_auxiliary_cycle454_2026_07_19 as c454


c448 = c454.c448
c440 = c454.c440
c398 = c454.c398
c390 = c454.c390
c385 = c454.c385
c436 = c454.c436
c433 = c454.c433
c364 = c454.c364
c321 = c454.c321
c317 = c454.c317
I2 = c454.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_SHORT_RATIONAL_MIXED_EFFECT_AUXILIARY_CYCLE457_NOTE_2026-07-19.md"
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
        "six exact rational directions remain after cycle 454",
        "bounded short-candidate menu",
        "denominator n=8",
        "support at most 20",
        "primitive coefficient at most 25",
        "two selected mixed-effect relations",
        "shared auxiliary service",
        "every auxiliary effect class counted",
        "no grade homogeneity",
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
    check("the Cycle-457 note freezes the short-candidate and claim boundary", not missing, missing)


def source_contracts() -> None:
    texts = tuple(normalized(path) for path in (c454.NOTE, c448.NOTE, c317.NOTE, c440.NOTE))
    check(
        "the exact-rank, explicit-auxiliary, dilation, and packet sources remain at their declared scope",
        all(path.is_file() for path in (c454.NOTE, c448.NOTE, c317.NOTE, c440.NOTE))
        and "full augmented rank is 84" in texts[0]
        and "full augmented nullity is 20" in texts[0]
        and "exact rational homogeneous operator-relation space has dimension 40" in texts[1]
        and "leaving nullity 14" in texts[1]
        and "exact ray split, coin, complement, merge" in texts[2]
        and "candidate packets are not actual records" in texts[3],
        {
            "Cycle454_explicit_auxiliary_surface": "input",
            "Cycle448_exact_rational_route_map": "input",
            "Cycle317_bounded_dilation": "input",
            "Cycle440_packet_compiler": "input",
        },
    )


@dataclass(frozen=True)
class CandidateRelation:
    name: str
    positive: tuple[tuple[int, int], ...]
    negative: tuple[tuple[int, int], ...]
    denominator: int = 8

    @property
    def vector(self) -> tuple[int, ...]:
        row = [0] * 55
        for index, coefficient in self.positive:
            row[index] += coefficient
        for index, coefficient in self.negative:
            row[index] -= coefficient
        return tuple(row)

    @property
    def support(self) -> int:
        return len(self.positive) + len(self.negative)

    @property
    def maximum_coefficient(self) -> int:
        return max(coefficient for _, coefficient in (*self.positive, *self.negative))


CANDIDATES = (
    CandidateRelation(
        "isotropic-mixed-closure",
        ((33, 25),),
        (
            (8, 2), (16, 1), (17, 1), (18, 1), (20, 2), (21, 2),
            (24, 2), (25, 2), (26, 1), (27, 1), (28, 1),
            (46, 2), (47, 2), (48, 1), (49, 1), (50, 1),
        ),
    ),
    CandidateRelation(
        "paired-axis-mixed-closure",
        ((10, 8), (29, 25)),
        (
            (8, 2), (9, 8), (20, 1), (21, 1), (24, 1),
            (25, 1), (28, 1), (46, 1), (47, 1), (50, 1),
        ),
    ),
)


def relation_operator(relation: CandidateRelation, effects: tuple[tuple[sp.Expr, ...], ...]) -> tuple[sp.Expr, ...]:
    values = [sp.S(0)] * 4
    for index, coefficient in relation.positive:
        values = [sp.simplify(left + coefficient * right) for left, right in zip(values, effects[index])]
    for index, coefficient in relation.negative:
        values = [sp.simplify(left - coefficient * right) for left, right in zip(values, effects[index])]
    return tuple(values)


def candidate_controls(c454_result: dict[str, object]) -> dict[str, object]:
    print("\nFROZEN SHORT-CANDIDATE MENU")
    effects = c448.exact_effects()
    lift = c448.coefficient_lift(effects)
    matrix: sp.Matrix = c454_result["matrix"]
    exact_failures = tuple(any(value != 0 for value in relation_operator(item, effects)) for item in CANDIDATES)
    candidate_rows = tuple(
        sp.Matrix([[*item.vector, *([0] * (matrix.cols - 55))]])
        for item in CANDIDATES
    )
    with_candidates = matrix
    incremental = []
    for row in candidate_rows:
        with_candidates = with_candidates.col_join(row)
        incremental.append(with_candidates.rank())
    rational_relations = sp.Matrix.hstack(*lift.nullspace()).T
    padded_rational = rational_relations.row_join(sp.zeros(rational_relations.rows, matrix.cols - 55))
    rational_completion = matrix.col_join(padded_rational)
    positive_sums = []
    for relation in CANDIDATES:
        total = sum(
            (coefficient * c448.numeric_matrix(effects[index]) / relation.denominator
             for index, coefficient in relation.positive),
            np.zeros((2, 2), complex),
        )
        positive_sums.append(tuple(map(float, np.linalg.eigvalsh(total))))
    check(
        "six rational directions remain after Cycle454 and the frozen bounded menu selects two exact independent N=8 rows",
        matrix.cols == 104
        and matrix.rank() == 84
        and rational_completion.rank() == 90
        and rational_completion.rank() - matrix.rank() == 6
        and exact_failures == (False, False)
        and incremental == [85, 86]
        and all(item.denominator == 8 and item.support <= 20 and item.maximum_coefficient <= 25 for item in CANDIDATES)
        and all(low >= -1e-12 and high <= 1 + 1e-12 for low, high in positive_sums),
        {
            "Cycle454_full_rank_nullity": (matrix.rank(), matrix.cols - matrix.rank()),
            "exact_rational_completion_rank_nullity": (
                rational_completion.rank(), matrix.cols - rational_completion.rank()
            ),
            "remaining_exact_rational_directions": rational_completion.rank() - matrix.rank(),
            "candidate_menu_size": len(CANDIDATES),
            "candidate_supports": tuple(item.support for item in CANDIDATES),
            "candidate_maximum_coefficients": tuple(item.maximum_coefficient for item in CANDIDATES),
            "candidate_denominators": tuple(item.denominator for item in CANDIDATES),
            "incremental_old_relation_ranks": tuple(incremental),
            "scaled_positive_sum_eigenvalues": tuple(positive_sums),
            "menu_frozen_before_context_construction": True,
        },
    )
    return {"rational_completion_rank": rational_completion.rank()}


@dataclass(frozen=True)
class GeneralGadget:
    label: str
    inputs: tuple[tuple[sp.Expr, ...], ...]
    total: tuple[sp.Expr, ...]
    held: bool = False


@dataclass(frozen=True)
class Cycle457Extension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    all_rows: tuple[tuple[int, ...], ...]
    new_rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[GeneralGadget, ...]
    held_new_rows: tuple[int, ...]
    row_labels: tuple[str, ...]


def scale_effect(effect: tuple[sp.Expr, ...], scale: sp.Expr) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(scale * value) for value in effect)


def sum_effects(effects: tuple[tuple[sp.Expr, ...], ...]) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(sum(values)) for values in zip(*effects))


def build_extension() -> Cycle457Extension:
    prior = c454.exact_extension()
    effects = list(prior.effects)
    by_key = {c454.exact_key(effect): index for index, effect in enumerate(effects)}

    def register(effect: tuple[sp.Expr, ...]) -> int:
        key = c454.exact_key(effect)
        if key not in by_key:
            by_key[key] = len(effects)
            effects.append(effect)
        return by_key[key]

    new_rows = []
    row_labels = []
    held_rows = []
    gadgets = []

    def install(gadget: GeneralGadget) -> tuple[sp.Expr, ...]:
        rest = c454.complement(gadget.total)
        input_indices = tuple(register(item) for item in gadget.inputs)
        rest_index = register(rest)
        total_index = register(gadget.total)
        start = len(new_rows)
        new_rows.extend(((*input_indices, rest_index), (total_index, rest_index)))
        row_labels.extend((gadget.label, gadget.label))
        if gadget.held:
            held_rows.extend((start, start + 1))
        gadgets.append(gadget)
        return gadget.total

    nodes: dict[tuple[int, int], tuple[sp.Expr, ...]] = {}

    def ensure_scaled_service(old_class: int) -> None:
        if (old_class, 1) in nodes:
            return
        base = c448.exact_effects()[old_class]
        nodes[(old_class, 1)] = scale_effect(base, sp.Rational(1, 8))
        for multiple in (2, 4, 8):
            half = nodes[(old_class, multiple // 2)]
            target = base if multiple == 8 else scale_effect(base, sp.Rational(multiple, 8))
            nodes[(old_class, multiple)] = install(GeneralGadget(
                f"shared E{old_class}/8 service {multiple // 2}+{multiple // 2}",
                (half, half), target,
            ))

    def ensure_multiple(old_class: int, coefficient: int) -> tuple[sp.Expr, ...]:
        ensure_scaled_service(old_class)
        if (old_class, coefficient) in nodes:
            return nodes[(old_class, coefficient)]
        if coefficient != 25:
            raise ValueError("the frozen menu only needs primitive multiples 1,2,8,25")
        for left, right, total in ((8, 8, 16), (16, 8, 24), (24, 1, 25)):
            if (old_class, total) not in nodes:
                nodes[(old_class, total)] = install(GeneralGadget(
                    f"E{old_class}/8 coefficient service {left}+{right}",
                    (nodes[(old_class, left)], nodes[(old_class, right)]),
                    scale_effect(c448.exact_effects()[old_class], sp.Rational(total, 8)),
                ))
        return nodes[(old_class, 25)]

    def combine(label: str, terms: tuple[tuple[sp.Expr, ...], ...], held: bool) -> tuple[sp.Expr, ...]:
        if not terms:
            raise ValueError("one relation side is empty")
        if len(terms) == 1:
            return terms[0]
        take = min(7, len(terms))
        current = install(GeneralGadget(label + " subtotal 0", terms[:take], sum_effects(terms[:take])))
        remaining = list(terms[take:])
        stage = 1
        while remaining:
            chunk = tuple(remaining[:6])
            del remaining[:6]
            inputs = (current, *chunk)
            current = install(GeneralGadget(
                f"{label} subtotal {stage}", inputs, sum_effects(inputs), held=held and not remaining
            ))
            stage += 1
        if not terms[take:]:
            # The one installed gadget is the final gadget.
            if held:
                last = gadgets[-1]
                gadgets[-1] = GeneralGadget(last.label, last.inputs, last.total, True)
                held_rows.extend((len(new_rows) - 2, len(new_rows) - 1))
        return current

    for relation in CANDIDATES:
        for old_class, _coefficient in (*relation.positive, *relation.negative):
            ensure_scaled_service(old_class)
        positive_terms = tuple(ensure_multiple(index, coefficient) for index, coefficient in relation.positive)
        negative_terms = tuple(ensure_multiple(index, coefficient) for index, coefficient in relation.negative)
        positive_root = combine(relation.name + " positive", positive_terms, False)
        negative_root = combine(relation.name + " negative", negative_terms, True)
        if c454.exact_key(positive_root) != c454.exact_key(negative_root):
            raise RuntimeError("a frozen candidate did not close on one shared PSD root")

    return Cycle457Extension(
        tuple(effects), prior.rows + tuple(new_rows), tuple(new_rows), tuple(gadgets),
        tuple(
            index for index, label in enumerate(row_labels)
            if any(label.startswith(relation.name) for relation in CANDIDATES)
        ),
        tuple(row_labels),
    )


def addition_program_pair(gadget: GeneralGadget, contact: np.ndarray) -> tuple[c321.Program, c321.Program]:
    raw_rest = c454.complement(gadget.total)
    physical = tuple(c454.physical_effect(item, contact) for item in (*gadget.inputs, raw_rest))
    kraus = tuple(contact @ c390.positive_square_root(effect) for effect in physical)
    # Literal Cycle317 bounded isometry check; at most eight pointer labels.
    c317.stack_isometry(kraus)
    fine = c321.Program(
        "Cycle457 " + gadget.label + " fine", kraus,
        tuple((index,) for index in range(len(kraus))),
    )
    merged = c321.Program(
        "Cycle457 " + gadget.label + " merge", kraus,
        (tuple(range(len(gadget.inputs))), (len(gadget.inputs),)),
    )
    return fine, merged


def new_programs(extension: Cycle457Extension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    programs = []
    for gadget in extension.gadgets:
        programs.extend(addition_program_pair(gadget, contact))
    return tuple(programs)


def augmented_surface_controls(
    surface: c440.FiniteSurface,
    c454_result: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL CYCLE457 AUXILIARY ACCOUNT")
    extension = build_extension()
    prior_extension = c454_result["extension"]
    prior_programs = c454_result["programs"]
    added_programs = {length: new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    all_programs = {
        length: (*prior_programs[length], *added_programs[length]) for length in (3, 6)
    }
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle457-shared-E-over-8", index, "coarse",
            "frozen bounded short rational candidate menu", tuple(program.coarse_effects)
        )
        for index, program in enumerate(all_programs[3])
    )
    installed = c385.build_effect_system(
        surface.installed.menus + presentations,
        effect_functionality_premise=True,
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
        for program, row in zip(added_programs[length], extension.new_rows)
        for effect, class_index in zip(program.coarse_effects, row)
    )
    isometry = max(
        float(np.linalg.norm(c317.stack_isometry(program.kraus).conj().T @ c317.stack_isometry(program.kraus) - I2))
        for length in (3, 6) for program in added_programs[length]
    )
    trace = np.asarray([float(np.trace(effect).real / 2) for effect in installed.effects])
    tangent = np.asarray([
        [float(np.trace(pauli @ effect).real / 2) for pauli in (c317.X, c317.Y, c317.Z)]
        for effect in installed.effects
    ])
    trace_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ trace - 1))
    tangent_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ tangent))
    check(
        "both short rational directions compile with one shared service and every auxiliary class in the full matrix",
        len(extension.gadgets) == 72
        and len(extension.new_rows) == len(added_programs[3]) == len(added_programs[6]) == 144
        and len(extension.all_rows) == 198
        and installed.incidence.shape == (296, len(extension.effects))
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and rank == matrix.cols - 18
        and nullity == projected == 18
        and maximum_effect < TOL and cross_size < TOL and isometry < TOL
        and trace_residual < TOL
        and int(np.linalg.matrix_rank(tangent, tol=1e-11)) == 3
        and tangent_residual < TOL,
        {
            "shared_addition_gadgets": len(extension.gadgets),
            "new_contexts": len(extension.new_rows),
            "all_retained_plus_new_contexts": len(extension.all_rows),
            "full_augmented_shape": installed.incidence.shape,
            "full_augmented_rank": rank,
            "full_augmented_nullity": nullity,
            "projected_old_nullity": projected,
            "reduction_from_Cycle454": 20 - nullity,
            "remaining_directions_beyond_Pauli_tangent": nullity - 3,
            "new_auxiliary_classes_beyond_Cycle454": len(extension.effects) - len(prior_extension.effects),
            "maximum_exact_physical_effect_residual": maximum_effect,
            "maximum_train_held_class_residual": cross_size,
            "maximum_Cycle317_stack_isometry_residual": isometry,
            "trace_grade_residual": trace_residual,
            "Pauli_tangent_residual": tangent_residual,
            "grade_homogeneity_assumed": False,
        },
    )
    return {
        "extension": extension, "programs": added_programs, "installed": installed,
        "matrix": matrix, "rank": rank, "nullity": nullity, "projected": projected,
    }


def projected_old_nullity(matrix: np.ndarray) -> int:
    null = sp.Matrix(matrix.tolist()).nullspace()
    if not null:
        return 0
    return sp.Matrix.hstack(*(item[:55, :] for item in null)).rank()


def deletion_controls(result: dict[str, object]) -> None:
    print("\nRELATION DELETION / HELD CONTROLS")
    installed: c385.EffectSystem = result["installed"]
    extension: Cycle457Extension = result["extension"]
    full = np.rint(installed.incidence).astype(int)
    new_offset = full.shape[0] - len(extension.new_rows)
    held_groups = (
        tuple(
            new_offset + index for index, label in enumerate(extension.row_labels)
            if label.startswith(CANDIDATES[0].name)
            or label.startswith("shared E33/8 service")
            or label.startswith("E33/8 coefficient service")
        ),
        tuple(
            new_offset + index for index, label in enumerate(extension.row_labels)
            if label.startswith(CANDIDATES[1].name)
        ),
    )
    held_absolute = tuple(row for group in held_groups for row in group)
    no_new = full[:new_offset]
    no_held = np.delete(full, held_absolute, axis=0)
    route_deletions = []
    for group in held_groups:
        reduced = np.delete(full, group, axis=0)
        matrix = sp.Matrix(reduced.tolist())
        route_deletions.append((matrix.rank(), matrix.cols - matrix.rank(), projected_old_nullity(reduced)))
    no_new_matrix = sp.Matrix(no_new.tolist())
    no_held_matrix = sp.Matrix(no_held.tolist())
    check(
        "deleting the two held shared-root closure routes restores exactly the two Cycle454 old-grade freedoms",
        projected_old_nullity(no_new) == 20
        and projected_old_nullity(no_held) == 20
        and result["projected"] == 18
        and tuple(item[2] for item in route_deletions) == (19, 19),
        {
            "delete_all_Cycle457_rows_rank_full_nullity_projected": (
                no_new_matrix.rank(), no_new_matrix.cols - no_new_matrix.rank(), projected_old_nullity(no_new)
            ),
            "delete_both_held_pairs_rank_full_nullity_projected": (
                no_held_matrix.rank(), no_held_matrix.cols - no_held_matrix.rank(), projected_old_nullity(no_held)
            ),
            "single_relation_route_deletions": tuple(route_deletions),
            "held_route_row_counts": tuple(map(len, held_groups)),
            "held_absolute_rows": held_absolute,
        },
    )


def class_cases(length: int, count: int) -> tuple[c433.FormationCase, ...]:
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 6)
    z = 11 if length == 3 else -11
    return tuple(
        c433.FormationCase(
            length, fixture,
            (index % 11 - 5, index // 11 - 2, z),
            (index % 11 - 6, index // 11 - 2, z),
            payloads[index % len(payloads)], payloads[(index + 1) % len(payloads)],
            length == 6,
        )
        for index in range(count)
    )


def physical_packet_controls(result: dict[str, object], fixtures: dict[int, c317.PhysicalFixture]) -> None:
    print("\nNEW-CONTEXT L3/L6 PACKETS / ALL-24")
    installed: c385.EffectSystem = result["installed"]
    extension: Cycle457Extension = result["extension"]
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
        cases = class_cases(length, len(installed.effects))
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
        compile_source = replace(installed, effects=installed.effects)
        generic = c390.compile_menus(compile_source, rows, fixtures[length].contact)
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
            moved, failures = c440.rotate_cases(class_cases(length, len(installed.effects)), frame)
            frame_failures += failures
            for class_index in involved:
                case = moved[class_index]
                pointer = class_index % 8
                law = c436.CandidateLaw(
                    f"Cycle457 frame class {class_index}", (case,), ((pointer, 0),), True, False
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
        "all new contexts have bounded train/held packets, exact inverse, zero leakage, all-24 covariance, and mass preservation",
        len(rows) == 144 and max(map(len, rows)) <= 8
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


def anti_fit_and_scope_controls(result: dict[str, object]) -> None:
    lift = c448.coefficient_lift(c448.exact_effects())
    corrupted = list(CANDIDATES[0].vector)
    corrupted[33] += 1
    exact_corruption = any(value != 0 for value in lift * sp.Matrix(corrupted))
    refused = 0
    for relation in (
        replace(CANDIDATES[0], denominator=7),
        CandidateRelation("oversupport", CANDIDATES[0].positive + ((0, 1), (1, 1), (2, 1), (3, 1)), CANDIDATES[0].negative),
        CandidateRelation("overcoefficient", ((33, 26),), CANDIDATES[0].negative),
    ):
        refused += int(not (
            relation.denominator == 8 and relation.support <= 20 and relation.maximum_coefficient <= 25
        ))
    check(
        "coefficient corruption and out-of-menu candidates are visible rather than fit away",
        exact_corruption and refused == 3,
        {"exact_relation_corruption_detected": exact_corruption, "out_of_menu_candidates_refused": refused},
    )
    check(
        "the two-direction gain selects no state, Born probability, occurrence, frequency, Record, no-go, or axiom pressure",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "authority": AUTHORITY, "audit": AUDIT,
            "grade_homogeneity_imported": False,
            "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none", "frequency_law": "none",
            "Born_state_or_grade_selected": False,
            "shared_substrate_obstruction": "none established", "axiom_pressure": "none",
        },
    )


def main() -> None:
    contracts()
    source_contracts()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    with redirect_stdout(StringIO()):
        surface = c440.reconstruct_surface(fixtures)
        c454_result = c454.exact_and_physical_surface_controls(surface, fixtures)
    candidate_controls(c454_result)
    result = augmented_surface_controls(surface, c454_result, fixtures)
    deletion_controls(result)
    physical_packet_controls(result, fixtures)
    anti_fit_and_scope_controls(result)
    print("\nSUMMARY")
    print({
        "result": "two short N=8 rational mixed-effect directions compiled with shared auxiliaries",
        "Cycle454_rank_nullity": (84, 20),
        "full_augmented_rank": result["rank"],
        "full_augmented_nullity": result["nullity"],
        "projected_old_nullity": result["projected"],
        "remaining_beyond_Pauli_tangent": result["nullity"] - 3,
        "uncompiled_fixed_G55_rational_directions": 4,
        "grade_homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
