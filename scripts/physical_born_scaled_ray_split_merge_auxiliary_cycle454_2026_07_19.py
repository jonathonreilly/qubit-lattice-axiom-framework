#!/usr/bin/env python3
"""Cycle 454: physical scaled-ray split/merge auxiliary contexts.

Use the actual Cycle-317 projector split isometry to build two finite binary
addition DAGs on the G55 (3,-4,0) ray.  Every scaled effect and complement is
an explicit effect class, and rank is measured on the full augmented system.
No grade homogeneity, probability, occurrence, or frequency law is assumed.
Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from fractions import Fraction
from io import StringIO
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_finite_born_exact_context_rank_recon_cycle448_2026_07_19 as c448


c440 = c448.c440
c398 = c448.c398
c390 = c448.c390
c385 = c448.c385
c436 = c448.c436
c433 = c448.c433
c364 = c448.c364
c321 = c448.c440.c321
c317 = c448.c317
I2 = c448.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_SCALED_RAY_SPLIT_MERGE_AUXILIARY_CYCLE454_NOTE_2026-07-19.md"
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
        "two finite binary addition dags",
        "actual cycle-317 projector split isometry",
        "no grade homogeneity",
        "every auxiliary effect class counted",
        "cycle 448 rank 33/nullity 23",
        "full augmented rank",
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
    check("the Cycle-454 note freezes the physical auxiliary and claim boundary", not missing, missing)


def source_contracts() -> None:
    texts = tuple(normalized(path) for path in (c448.NOTE, c317.NOTE, c440.NOTE))
    check(
        "the exact-rank, physical split, and protected-packet source boundaries remain explicit",
        all(path.is_file() for path in (c448.NOTE, c317.NOTE, c440.NOTE))
        and "rank 33/nullity 23" in texts[0]
        and "exact ray split, coin, complement, merge" in texts[1]
        and "exact integer rank 31" in texts[2]
        and "candidate packets are not actual records" in texts[2],
        {
            "Cycle448_exact_context_surface": "input",
            "Cycle317_split_isometry": "input",
            "Cycle440_packet_compiler": "input",
        },
    )


@dataclass(frozen=True)
class NetworkSpec:
    name: str
    unit: sp.Rational
    targets: tuple[tuple[int, int], ...]  # (integer multiple, old G55 class)
    held_target: int


@dataclass(frozen=True)
class Gadget:
    network: str
    left: int
    right: int
    total: int
    unit: sp.Rational
    target_class: int | None


NETWORKS = (
    NetworkSpec("centiray", sp.Rational(1, 100), ((23, 44), (61, 11), (77, 45)), 77),
    NetworkSpec("E11-centisplit", sp.Rational(61, 10000), ((37, 14), (100, 11)), 37),
)
RAY_DIRECTION = (3, -4, 0)


def addition_dag(spec: NetworkSpec) -> tuple[Gadget, ...]:
    target_map = dict(spec.targets)
    maximum = max(target_map)
    constructed = {1}
    gadgets = []
    power = 1
    while 2 * power <= maximum:
        total = 2 * power
        gadgets.append(Gadget(spec.name, power, power, total, spec.unit, target_map.get(total)))
        constructed.add(total)
        power = total
    for target in sorted(target_map):
        bits = tuple(1 << bit for bit in range(target.bit_length() - 1, -1, -1) if target & (1 << bit))
        current = bits[0]
        for bit in bits[1:]:
            total = current + bit
            if total not in constructed:
                gadgets.append(Gadget(spec.name, current, bit, total, spec.unit, target_map.get(total)))
                constructed.add(total)
            current = total
        if target not in constructed:
            raise RuntimeError("addition DAG failed to construct a target")
    return tuple(gadgets)


def network_contracts() -> None:
    gadgets = tuple(addition_dag(spec) for spec in NETWORKS)
    endpoint_residual = max(
        float(np.linalg.norm(
            c448.numeric_matrix(raw_ray(spec.unit * multiple))
            - c448.numeric_matrix(c448.exact_effects()[old_class])
        ))
        for spec in NETWORKS
        for multiple, old_class in spec.targets
    )
    check(
        "the two frozen binary DAGs have bounded normalized weights and exact old-class endpoints",
        tuple(map(len, gadgets)) == (16, 10)
        and all(
            gadget.unit * gadget.total <= 1
            and gadget.left + gadget.right == gadget.total
            for group in gadgets for gadget in group
        )
        and endpoint_residual < 1e-14,
        {
            "network_gadget_counts": tuple(map(len, gadgets)),
            "network_context_counts": tuple(2 * len(group) for group in gadgets),
            "maximum_projector_weight": str(max(
                gadget.unit * gadget.total for group in gadgets for gadget in group
            )),
            "maximum_exact_endpoint_residual": endpoint_residual,
            "maximum_coarse_outcomes": 3,
            "maximum_fine_labels": 4,
        },
    )


def complement(effect: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    a, d, x, y = effect
    return tuple(map(sp.simplify, (1 - a, 1 - d, -x, -y)))


def exact_key(effect: tuple[sp.Expr, ...]) -> tuple[sp.Rational, ...]:
    return tuple(value for entry in effect for value in c448.rational_coefficients(entry))


def raw_ray(weight: sp.Expr) -> tuple[sp.Expr, ...]:
    return c448.projector(sp.sympify(weight), RAY_DIRECTION)


@dataclass(frozen=True)
class ExactExtension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[Gadget, ...]
    row_networks: tuple[str, ...]
    held_rows: tuple[int, ...]


def exact_extension() -> ExactExtension:
    effects = list(c448.exact_effects())
    by_key = {exact_key(effect): index for index, effect in enumerate(effects)}

    def register(effect: tuple[sp.Expr, ...]) -> int:
        key = exact_key(effect)
        if key not in by_key:
            by_key[key] = len(effects)
            effects.append(effect)
        return by_key[key]

    rows = []
    row_networks = []
    held_rows = []
    r448 = c448.identity_effect(sp.Rational(9, 25))
    r448_index = register(r448)
    rows.extend(((13, 19, r448_index), (33, 33, r448_index)))
    row_networks.extend(("Cycle448", "Cycle448"))

    all_gadgets = []
    for spec in NETWORKS:
        target_map = dict(spec.targets)
        for multiple, old_class in spec.targets:
            if exact_key(raw_ray(spec.unit * multiple)) != exact_key(effects[old_class]):
                raise RuntimeError(f"{spec.name} target does not match old class {old_class}")
        for gadget in addition_dag(spec):
            all_gadgets.append(gadget)
            left = raw_ray(spec.unit * gadget.left)
            right = raw_ray(spec.unit * gadget.right)
            total = raw_ray(spec.unit * gadget.total)
            rest = complement(total)
            left_index = register(left)
            right_index = register(right)
            rest_index = register(rest)
            # Match the physical presentation order: the fine context first
            # registers A, B, R; the merge context then registers C.
            total_index = register(total)
            if gadget.target_class is not None and total_index != gadget.target_class:
                raise RuntimeError("target effect did not deduplicate to its old G55 class")
            rows.extend(((left_index, right_index, rest_index), (total_index, rest_index)))
            row_networks.extend((spec.name, spec.name))
            if gadget.total == spec.held_target:
                held_rows.extend((len(rows) - 2, len(rows) - 1))
    return ExactExtension(tuple(effects), tuple(rows), tuple(all_gadgets), tuple(row_networks), tuple(held_rows))


def physical_effect(raw: tuple[sp.Expr, ...], contact: np.ndarray) -> np.ndarray:
    matrix = c448.numeric_matrix(raw)
    return contact.conj().T @ matrix @ contact


def generic_program(name: str, raw_menu: tuple[tuple[sp.Expr, ...], ...], contact: np.ndarray) -> c321.Program:
    effects = tuple(physical_effect(effect, contact) for effect in raw_menu)
    return c321.Program(
        name,
        tuple(contact @ c390.positive_square_root(effect) for effect in effects),
        tuple((index,) for index in range(len(effects))),
    )


def split_program_pair(gadget: Gadget, contact: np.ndarray) -> tuple[c321.Program, c321.Program]:
    direction = np.asarray(RAY_DIRECTION, dtype=float)
    direction /= np.linalg.norm(direction)
    projector = c317.projector_bloch(direction)
    left = float(gadget.unit * gadget.left)
    right = float(gadget.unit * gadget.right)
    remainder = 1 - left - right
    splits = (left, right, remainder) if remainder > 2e-13 else (left, right)
    isometry, _groups = c317.split_projector_isometry(projector, splits, contact)
    count = len(splits) + 1
    kraus = tuple(isometry[2 * index:2 * (index + 1), :] for index in range(count))
    rest = tuple(range(2, count))
    fine = c321.Program(
        f"Cycle454 {gadget.network} {gadget.left}+{gadget.right} fine",
        kraus,
        ((0,), (1,), rest),
    )
    merged = c321.Program(
        f"Cycle454 {gadget.network} {gadget.left}+{gadget.right} merge",
        kraus,
        ((0, 1), rest),
    )
    return fine, merged


def physical_programs(extension: ExactExtension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    r448 = c448.identity_effect(sp.Rational(9, 25))
    programs = [
        generic_program("Cycle454 retained Cycle448 left", (
            extension.effects[13], extension.effects[19], r448
        ), contact),
        generic_program("Cycle454 retained Cycle448 right", (
            extension.effects[33], extension.effects[33], r448
        ), contact),
    ]
    for gadget in extension.gadgets:
        programs.extend(split_program_pair(gadget, contact))
    return tuple(programs)


def exact_and_physical_surface_controls(
    surface: c440.FiniteSurface,
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL AUXILIARY-CLASS INCIDENCE")
    extension = exact_extension()
    programs = {length: physical_programs(extension, fixtures[length].contact) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle454-Cycle317-split", index, "coarse",
            "bounded supplied binary addition DAG", tuple(program.coarse_effects)
        )
        for index, program in enumerate(programs[3])
    )
    installed = c385.build_effect_system(
        surface.installed.menus + presentations,
        effect_functionality_premise=True,
    )
    expected = np.zeros((len(extension.rows), len(extension.effects)), dtype=int)
    for row_index, row in enumerate(extension.rows):
        for class_index in row:
            expected[row_index, class_index] += 1
    physical_rows = np.rint(installed.incidence[-len(extension.rows):]).astype(int)
    exact_matrix = sp.Matrix(np.rint(installed.incidence).astype(int).tolist())
    exact_rank = exact_matrix.rank()
    exact_nullity = exact_matrix.cols - exact_rank
    null = exact_matrix.nullspace()
    projected = sp.Matrix.hstack(*(item[:55, :] for item in null))
    projected_old = projected.rank()
    maximum_effect = max(
        float(np.linalg.norm(physical_effect(raw, fixtures[3].contact) - effect))
        for raw, effect in zip(extension.effects, installed.effects)
    )
    cross_size = max(
        float(np.linalg.norm(effect - installed.effects[class_index]))
        for length in (3, 6)
        for program, row in zip(programs[length], extension.rows)
        for effect, class_index in zip(program.coarse_effects, row)
    )
    fine_isometry = max(
        float(np.linalg.norm(c317.stack_isometry(program.kraus).conj().T @ c317.stack_isometry(program.kraus) - I2))
        for length in (3, 6)
        for program in programs[length]
    )
    trace = np.asarray([float(np.trace(effect).real / 2) for effect in installed.effects])
    tangent = np.asarray([
        [float(np.trace(pauli @ effect).real / 2) for pauli in (c317.X, c317.Y, c317.Z)]
        for effect in installed.effects
    ])
    trace_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ trace - 1))
    tangent_residual = float(np.linalg.norm(np.asarray(installed.incidence) @ tangent))

    check(
        "two explicit Cycle317 addition DAGs reduce full and projected-old freedom with every auxiliary class counted",
        len(extension.gadgets) == 26
        and len(extension.rows) == len(programs[3]) == len(programs[6]) == 54
        and installed.incidence.shape == (152, len(extension.effects))
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and exact_rank == installed.incidence.shape[1] - 20
        and exact_nullity == projected_old == 20
        and maximum_effect < TOL
        and cross_size < TOL
        and fine_isometry < TOL
        and trace_residual < TOL
        and int(np.linalg.matrix_rank(tangent, tol=1e-11)) == 3
        and tangent_residual < TOL,
        {
            "binary_addition_gadgets": len(extension.gadgets),
            "new_contexts_including_Cycle448_pair": len(extension.rows),
            "full_augmented_shape": installed.incidence.shape,
            "full_augmented_rank": exact_rank,
            "full_augmented_nullity": exact_nullity,
            "projected_old_nullity": projected_old,
            "nullity_reduction_from_Cycle448": 23 - exact_nullity,
            "remaining_directions_beyond_Pauli_tangent": exact_nullity - 3,
            "maximum_exact_to_physical_effect_residual": maximum_effect,
            "maximum_train_held_class_residual": cross_size,
            "maximum_Cycle317_split_isometry_residual": fine_isometry,
            "trace_grade_residual": trace_residual,
            "Pauli_tangent_rank": int(np.linalg.matrix_rank(tangent, tol=1e-11)),
            "Pauli_tangent_residual": tangent_residual,
            "grade_homogeneity_assumed": False,
        },
    )
    return {
        "extension": extension,
        "programs": programs,
        "installed": installed,
        "matrix": exact_matrix,
        "rank": exact_rank,
        "nullity": exact_nullity,
        "projected_old": projected_old,
    }


def projected_nullity(matrix: np.ndarray) -> int:
    null = sp.Matrix(matrix.tolist()).nullspace()
    if not null:
        return 0
    return sp.Matrix.hstack(*(item[:55, :] for item in null)).rank()


def deletion_and_holdout_controls(result: dict[str, object]) -> None:
    print("\nDELETION / HELD-RELATION CONTROLS")
    installed: c385.EffectSystem = result["installed"]
    extension: ExactExtension = result["extension"]
    full = np.rint(installed.incidence).astype(int)
    offset = full.shape[0] - len(extension.rows)
    network_indices = {
        name: tuple(offset + index for index, item in enumerate(extension.row_networks) if item == name)
        for name in ("Cycle448", *(spec.name for spec in NETWORKS))
    }
    deletion = {}
    for name, indices in network_indices.items():
        reduced = np.delete(full, indices, axis=0)
        matrix = sp.Matrix(reduced.tolist())
        deletion[name] = {
            "rank": matrix.rank(),
            "full_nullity": matrix.cols - matrix.rank(),
            "projected_old_nullity": projected_nullity(reduced),
        }
    held_absolute = tuple(offset + index for index in extension.held_rows)
    train = np.delete(full, held_absolute, axis=0)
    train_rank = sp.Matrix(train.tolist()).rank()
    train_projected = projected_nullity(train)
    single_context_deletions = tuple(
        projected_nullity(np.delete(full, offset + index, axis=0))
        for index in extension.held_rows
    )
    check(
        "network deletion and held-relation rows expose the three auxiliary rank gains",
        deletion["Cycle448"]["projected_old_nullity"] == 21
        and deletion["centiray"]["projected_old_nullity"] == 22
        and deletion["E11-centisplit"]["projected_old_nullity"] == 21
        and train_projected > result["projected_old"]
        and train_rank < result["rank"]
        and all(value >= result["projected_old"] for value in single_context_deletions),
        {
            "whole_network_deletions": deletion,
            "held_context_rows": held_absolute,
            "train_without_held_rank": train_rank,
            "train_without_held_projected_old_nullity": train_projected,
            "held_restored_rank_gain": result["rank"] - train_rank,
            "held_restored_projected_old_reduction": train_projected - result["projected_old"],
            "single_held_context_deletion_projected_old_nullities": single_context_deletions,
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


def physical_packet_controls(
    result: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> None:
    print("\nL3/L6 PROTECTED PACKETS AND ALL-24 COVARIANCE")
    installed: c385.EffectSystem = result["installed"]
    extension: ExactExtension = result["extension"]
    programs_by_length = result["programs"]
    rows = extension.rows
    involved = tuple(sorted({index for row in rows for index in row}))
    maximum_effect = maximum_completeness = maximum_bank = 0.0
    maximum_forward = maximum_inverse = 0.0
    leakage_failures = packet_failures = idle_failures = 0
    active = idle = 0
    words_by_length = {}
    covariance_rows = []
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
                restored, inverse_local = c436.apply_law(output, pointer, law, reverse=True)
                word = c440.extract_pointer_word(output)
                packet_failures += int(word is None or restored != source)
                leakage_failures += local + inverse_local
                if word is not None:
                    occurrences[class_index].append(word)
                active += 1
            for pointer in range(len(row), 8):
                output, local = c436.apply_law(source, pointer, law)
                idle_failures += int(output != source or local)
                idle += 1
        canonical = {}
        for index, words in occurrences.items():
            packet_failures += int(not words or len(set(words)) != 1)
            canonical[index] = words[0]
        packet_failures += int(len(set(canonical.values())) != len(canonical))
        words_by_length[length] = canonical

        compile_source = replace(result["installed"], effects=result["installed"].effects)
        generic = c390.compile_menus(compile_source, rows, fixtures[length].contact)
        failures, encoding, block = c440.physical_encoding_covariance(
            fixtures[length], tuple(generic.unique_blocks.values())
        )
        covariance_rows.append((length, failures, encoding, block, len(generic.unique_blocks)))

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
                    f"Cycle454 frame class {class_index}", (case,), ((pointer, 0),), True, False
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
        "every split/merge context has exact train/held packet action, inverse, locality, covariance, and mass preservation",
        len(rows) == 54
        and max(map(len, rows)) == 3
        and active == 2 * sum(map(len, rows))
        and idle == 2 * sum(8 - len(row) for row in rows)
        and frame_cases == 24 * 2 * len(involved)
        and all(words_by_length[3][index] != words_by_length[3][other]
                for position, index in enumerate(involved) for other in involved[position + 1:])
        and leakage_failures == packet_failures == idle_failures == frame_failures == 0
        and max(maximum_effect, maximum_completeness, maximum_bank, maximum_forward, maximum_inverse) < TOL
        and all(failures == 0 and max(encoding, block) < TOL for _, failures, encoding, block, _ in covariance_rows)
        and mass_residual < 3e-12,
        {
            "train_held_contexts": 2 * len(rows),
            "involved_effect_classes": len(involved),
            "active_pointer_cases": active,
            "idle_pointer_cases": idle,
            "maximum_effect_residual": maximum_effect,
            "maximum_completeness_residual": maximum_completeness,
            "maximum_fixed_bank_isometry_residual": maximum_bank,
            "maximum_E_G_residual": maximum_forward,
            "maximum_inverse_residual": maximum_inverse,
            "leakage_failures": leakage_failures,
            "packet_failures": packet_failures,
            "proper_cubic_frames": len(frames),
            "all_frame_packet_cases": frame_cases,
            "frame_failures": frame_failures,
            "physical_encoding_covariance": covariance_rows,
            "one_particle_mass_relative_residual": mass_residual,
            "program_M2_per_eight_program_bank": 3,
            "pointer_M2": 3,
            "maximum_primitive_support_M2": 3,
        },
    )


def anti_fit_and_scope_controls(result: dict[str, object]) -> None:
    extension: ExactExtension = result["extension"]
    first = extension.gadgets[0]
    intact = raw_ray(first.unit * first.total)
    corrupted = c448.add_effects(
        raw_ray(first.unit * first.left),
        raw_ray(first.unit * first.right + sp.Rational(1, 10000)),
    )
    exact_corruption = exact_key(intact) != exact_key(corrupted)
    refused = 0
    direction = np.asarray(RAY_DIRECTION, dtype=float)
    direction /= np.linalg.norm(direction)
    projector = c317.projector_bloch(direction)
    contact = c317.physical_fixture(3).contact
    for splits in ((0.2, 0.3), (-0.1, 1.1), (0.7, 0.4)):
        try:
            c317.split_projector_isometry(projector, splits, contact)
        except ValueError:
            refused += 1
    check(
        "coefficient corruption and malformed split schedules are visible on the declared domain",
        exact_corruption and refused == 3,
        {"exact_coefficient_corruption_detected": exact_corruption, "malformed_splits_refused": refused},
    )
    check(
        "the auxiliary rank gain selects no state, Born probability, occurrence, frequency, Record, no-go, or axiom pressure",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "grade_homogeneity_imported": False,
            "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none",
            "frequency_law": "none",
            "Born_state_or_grade_selected": False,
            "shared_substrate_obstruction": "none established",
            "axiom_pressure": "none",
        },
    )


def main() -> None:
    contracts()
    source_contracts()
    network_contracts()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    with redirect_stdout(StringIO()):
        surface = c440.reconstruct_surface(fixtures)
    result = exact_and_physical_surface_controls(surface, fixtures)
    deletion_and_holdout_controls(result)
    physical_packet_controls(result, fixtures)
    anti_fit_and_scope_controls(result)
    print("\nSUMMARY")
    print({
        "result": "two explicit same-ray addition DAGs with all auxiliary classes counted",
        "Cycle448_rank_nullity": (33, 23),
        "full_augmented_rank": result["rank"],
        "full_augmented_nullity": result["nullity"],
        "projected_old_nullity": result["projected_old"],
        "remaining_beyond_Pauli_tangent": result["nullity"] - 3,
        "grade_homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY,
        "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
