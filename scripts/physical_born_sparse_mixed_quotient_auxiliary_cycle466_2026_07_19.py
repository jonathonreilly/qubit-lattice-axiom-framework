#!/usr/bin/env python3
"""Cycle 466: compile the first sparse mixed quotient direction after Cycle462.

The representative, N=732 normalization, 84-gadget estimate, and resource
envelope are frozen before construction.  Every exact auxiliary class is
shared against Cycles 454/457/462 and retained in the full incidence matrix.
No cost optimality, homogeneity, Born selection, or probability is assumed.
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_proportional_quotient_auxiliary_cycle462_2026_07_19 as c462


c457 = c462.c457
c454 = c462.c454
c448 = c462.c448
c440 = c462.c440
c398 = c462.c398
c390 = c462.c390
c385 = c462.c385
c436 = c462.c436
c433 = c462.c433
c321 = c462.c321
c317 = c462.c317
I2 = c462.I2
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_SPARSE_MIXED_QUOTIENT_AUXILIARY_CYCLE466_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

# Frozen before any Cycle466 class registration, physical compilation, or fit.
SELECTED_VECTOR = tuple(
    {
        0: -366, 1: -366, 2: -2196, 3: -2196,
        11: 1000, 16: -549, 37: 1464,
    }.get(index, 0)
    for index in range(55)
)
SELECTED_DENOMINATOR = 732
SELECTED_SUPPORT = 7
SELECTED_MAXIMUM_COEFFICIENT = 2196
SELECTED_GADGET_ENVELOPE = 84
REMAINING_RAW_BASIS_INDICES = (29, 21)


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
        "authority: none", "audit: unset", "exact target contract",
        "support 7", "maximum coefficient 2196", "normalization n=732",
        "84-gadget envelope", "600-second wall cap", "4 gib rss cap",
        "every exact auxiliary class shared", "every auxiliary effect class counted",
        "full augmented rank", "full augmented nullity", "projected-old nullity",
        "train l=3", "held l=6", "all 24 proper-cubic frames",
        "exact e/g", "exact inverse", "dependency-closed deletion",
        "candidate packets are not actual records", "coherent norms are not probabilities",
        "no occurrence, probability, frequency, or born-law selection",
        "no cost-optimality or grade-homogeneity claim",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo",
        "gate disposition: fail", "partial-attempt-with-named-untested-routes",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
        "supplied / derived / open",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle466 note freezes the sparse mixed target and claim boundary", not missing, missing)


def source_contracts() -> None:
    body = normalized(c462.NOTE)
    check(
        "the Cycle462 quotient surface and sparse inventory remain at their declared scope",
        c462.NOTE.is_file()
        and "full augmented rank 237" in body
        and "full augmented nullity 17" in body
        and "projected-old nullity 17" in body
        and "estimated 84 explicit addition gadgets" in body
        and "three exact fixed-g55 rational quotient directions remain" in body,
        {"Cycle462_surface": "input", "authority": AUTHORITY, "audit": AUDIT},
    )


def exact_search_controls(prior: dict[str, object]) -> dict[str, object]:
    print("\nFROZEN SPARSE MIXED TARGET")
    effects = c448.exact_effects()
    lift = c448.coefficient_lift(effects)
    matrix: sp.Matrix = prior["matrix"]
    candidate = sp.Matrix([[*SELECTED_VECTOR, *([0] * (matrix.cols - 55))]])
    rational = sp.Matrix.hstack(*lift.nullspace()).T
    completion = matrix.col_join(rational.row_join(sp.zeros(rational.rows, matrix.cols - 55)))
    running = matrix.col_join(candidate)
    inventory = []
    for basis_index in REMAINING_RAW_BASIS_INDICES:
        vector = c462.primitive_integer_row(rational.row(basis_index))
        row = sp.Matrix([[*vector, *([0] * (matrix.cols - 55))]])
        rank = running.col_join(row).rank()
        denominator = c462.minimum_denominator(vector)
        inventory.append({
            "basis_index": basis_index,
            "vector": vector,
            "support": sum(value != 0 for value in vector),
            "maximum_coefficient": max(map(abs, vector)),
            "minimum_denominator": denominator,
            "predicted_addition_gadgets": c462.predicted_gadgets(vector, denominator),
            "incremental_rank": rank,
        })
        running = running.col_join(row)
    root = c462.relation_root(SELECTED_VECTOR)
    scaled_eigenvalues = tuple(map(float, np.linalg.eigvalsh(root / SELECTED_DENOMINATOR)))
    predicted = c462.predicted_gadgets(SELECTED_VECTOR, SELECTED_DENOMINATOR)
    check(
        "the frozen support-seven representative is exact, independent, PSD-normalized, and inside its 84-gadget envelope",
        sum(value != 0 for value in SELECTED_VECTOR) == SELECTED_SUPPORT
        and max(map(abs, SELECTED_VECTOR)) == SELECTED_MAXIMUM_COEFFICIENT
        and c462.minimum_denominator(SELECTED_VECTOR) == SELECTED_DENOMINATOR
        and predicted == SELECTED_GADGET_ENVELOPE
        and all(value == 0 for value in lift * sp.Matrix(SELECTED_VECTOR))
        and matrix.rank() == 237
        and matrix.col_join(candidate).rank() == 238
        and completion.rank() == running.rank() == 240
        and tuple(item["incremental_rank"] for item in inventory) == (239, 240)
        and scaled_eigenvalues[0] >= -1e-12 and scaled_eigenvalues[-1] <= 1 + 1e-12,
        {
            "selected_vector": tuple((i, value) for i, value in enumerate(SELECTED_VECTOR) if value),
            "support": SELECTED_SUPPORT,
            "maximum_coefficient": SELECTED_MAXIMUM_COEFFICIENT,
            "minimum_denominator": SELECTED_DENOMINATOR,
            "scaled_root_eigenvalues": scaled_eigenvalues,
            "predicted_addition_gadgets": predicted,
            "prior_candidate_completion_ranks": (matrix.rank(), matrix.col_join(candidate).rank(), completion.rank()),
            "remaining_inventory": tuple(
                {key: value for key, value in item.items() if key != "vector"} for item in inventory
            ),
            "representative_frozen_before_construction": True,
            "cost_optimality_claimed": False,
        },
    )
    return {"inventory": tuple(inventory), "completion_rank": completion.rank()}


@dataclass(frozen=True)
class Cycle466Extension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    all_rows: tuple[tuple[int, ...], ...]
    new_rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[c457.GeneralGadget, ...]
    row_labels: tuple[str, ...]


def build_extension() -> Cycle466Extension:
    prior = c462.build_extension()
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
                f"{side} E{old_class}/732 power {power // 2}+{power // 2}",
                (half, half), scaled(old_class, power),
            )
            power *= 2
        denominator_bits = tuple(
            nodes[(old_class, bit)] for bit in (512, 128, 64, 16, 8, 4)
        )
        nodes[(old_class, SELECTED_DENOMINATOR)] = install(
            f"{side} E{old_class}/732 denominator 512+128+64+16+8+4",
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

    positive = tuple(service("positive", index, coefficient) for index, coefficient in ((11, 1000), (37, 1464)))
    negative = tuple(service("negative", index, coefficient) for index, coefficient in (
        (0, 366), (1, 366), (2, 2196), (3, 2196), (16, 549),
    ))
    positive_root = install("positive mixed root", positive, c457.sum_effects(positive))
    negative_root = install("negative mixed root", negative, c457.sum_effects(negative))
    if c454.exact_key(positive_root) != c454.exact_key(negative_root):
        raise RuntimeError("the frozen Cycle466 relation failed exact closure")
    if len(gadgets) != SELECTED_GADGET_ENVELOPE:
        raise RuntimeError(f"frozen 84-gadget estimate was wrong: observed {len(gadgets)}")
    return Cycle466Extension(
        tuple(effects), prior.all_rows + tuple(rows), tuple(rows), tuple(gadgets), tuple(labels)
    )


def new_programs(extension: Cycle466Extension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    programs = []
    for gadget in extension.gadgets:
        programs.extend(c457.addition_program_pair(gadget, contact))
    return tuple(programs)


def augmented_surface_controls(
    surface: c440.FiniteSurface,
    c454_result: dict[str, object],
    c457_result: dict[str, object],
    c462_result: dict[str, object],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL CYCLE466 SHARED-AUXILIARY ACCOUNT")
    extension = build_extension()
    prior_programs = {
        length: (
            *c454_result["programs"][length],
            *c457_result["programs"][length],
            *c462_result["programs"][length],
        )
        for length in (3, 6)
    }
    added = {length: new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    all_programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle466-E-over-732", index, "coarse",
            "frozen support-seven sparse mixed quotient", tuple(program.coarse_effects),
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
        "the frozen sparse mixed direction compiles with every shared auxiliary class in the full matrix",
        len(extension.gadgets) == SELECTED_GADGET_ENVELOPE
        and len(extension.new_rows) == len(added[3]) == len(added[6]) == 168
        and len(extension.all_rows) == 394
        and installed.incidence.shape[0] == 492
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and nullity == projected == 16
        and rank == matrix.cols - 16
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
            "reduction_from_Cycle462": 17 - projected,
            "remaining_beyond_Pauli_tangent": projected - 3,
            "new_auxiliary_classes_beyond_Cycle462": len(extension.effects) - len(c462.build_extension().effects),
            "exact_class_sharing_key": "Cycle454 exact_key across Cycles454/457/462/466",
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
    print("\nDEPENDENCY-CLOSED ROUTE DELETIONS")
    installed = result["installed"]
    extension = result["extension"]
    full = np.rint(installed.incidence).astype(int)
    offset = full.shape[0] - len(extension.new_rows)
    no_new = full[:offset]
    side_groups = tuple(
        tuple(offset + index for index, label in enumerate(extension.row_labels) if label.startswith(side))
        for side in ("positive", "negative")
    )
    terminal_groups = tuple(
        tuple(offset + index for index, label in enumerate(extension.row_labels) if label == f"{side} mixed root")
        for side in ("positive", "negative")
    )

    def disposition(rows: tuple[int, ...]) -> tuple[int, int, int]:
        reduced = np.delete(full, rows, axis=0)
        matrix = sp.Matrix(reduced.tolist())
        return matrix.rank(), matrix.cols - matrix.rank(), c457.projected_old_nullity(reduced)

    no_new_disposition = disposition(tuple(range(offset, full.shape[0])))
    side_dispositions = tuple(disposition(group) for group in side_groups)
    terminal_dispositions = tuple(disposition(group) for group in terminal_groups)
    check(
        "dependency-closed deletion of either relation side and surgical deletion of either terminal root restore the Cycle462 freedom",
        no_new_disposition[2] == 17
        and result["projected"] == 16
        and tuple(item[2] for item in side_dispositions) == (17, 17)
        and tuple(item[2] for item in terminal_dispositions) == (17, 17)
        and tuple(map(len, side_groups)) == (48, 120)
        and tuple(map(len, terminal_groups)) == (2, 2),
        {
            "delete_all_Cycle466_rows_rank_full_nullity_projected": no_new_disposition,
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
                    f"Cycle466 frame class {class_index}", (case,), ((pointer, 0),), True, False
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
        "all new sparse mixed contexts pass train/held packets, inverse, leakage, all-24 covariance, and mass controls",
        len(rows) == 168 and max(map(len, rows)) <= 8
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
    underscaled = max(np.linalg.eigvalsh(c462.relation_root(SELECTED_VECTOR) / 731)) > 1
    check(
        "coefficient corruption, underscaling, and gadget-count drift remain visible rather than fit away",
        exact_corruption and underscaled and len(result["extension"].gadgets) == 84,
        {
            "exact_corruption_detected": exact_corruption,
            "N731_root_exceeds_identity": underscaled,
            "frozen_observed_gadget_count": len(result["extension"].gadgets),
        },
    )
    inventory = search["inventory"]
    check(
        "two uncompiled exact quotient directions remain live without homogeneity, Born closure, obstruction, or axiom pressure",
        len(inventory) == 2
        and tuple(item["incremental_rank"] for item in inventory) == (239, 240)
        and result["projected"] == 16
        and AUTHORITY == "none" and AUDIT == "unset",
        {
            "remaining_exact_rational_quotient_directions": 2,
            "inventory_costs": tuple(
                (item["basis_index"], item["support"], item["maximum_coefficient"],
                 item["minimum_denominator"], item["predicted_addition_gadgets"])
                for item in inventory
            ),
            "cost_optimality_claimed": False,
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
        "the frozen 84-gadget compiler completes below its wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and maxrss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss, "RSS_cap_bytes": RSS_CAP_BYTES,
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle466 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


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
            c462_result = c462.augmented_surface_controls(
                surface, c454_result, c457_result, fixtures
            )
        search = exact_search_controls(c462_result)
        result = augmented_surface_controls(
            surface, c454_result, c457_result, c462_result, fixtures
        )
        deletion_controls(result)
        physical_packet_controls(result, fixtures)
        anti_fit_scope_resource_controls(search, result, started)
    except WallCapExceeded as error:
        check("the Cycle466 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY")
    print({
        "result": "one support-seven exact mixed quotient direction compiled with explicit E/732 auxiliaries",
        "Cycle462_rank_nullity": (237, 17),
        "full_augmented_rank": result["rank"] if "result" in locals() else None,
        "full_augmented_nullity": result["nullity"] if "result" in locals() else None,
        "projected_old_nullity": result["projected"] if "result" in locals() else None,
        "uncompiled_fixed_G55_rational_directions": 2,
        "cost_optimality_claimed": False,
        "grade_homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
