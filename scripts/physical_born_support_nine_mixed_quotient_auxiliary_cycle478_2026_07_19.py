#!/usr/bin/env python3
"""Cycle 478: compile the final frozen support-nine G55 quotient row.

The exact row and N=823593 are frozen.  The inherited 191-gadget estimate is
also retained as a falsified forecast: it violates the established eight-
outcome physical pointer once normalization complements are included.  A
208-gadget, arity-seven sum DAG is frozen before physical construction.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from io import StringIO
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.modulargcd import _integer_rational_reconstruction


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_support_eight_mixed_quotient_auxiliary_cycle471_2026_07_19 as c471


c466 = c471.c466
c462 = c471.c462
c457 = c471.c457
c454 = c471.c454
c448 = c471.c448
c440 = c471.c440
c398 = c471.c398
c390 = c471.c390
c385 = c471.c385
c436 = c471.c436
c433 = c471.c433
c321 = c471.c321
c317 = c471.c317
I2 = c471.I2
# The inherited service builders call exact_effects repeatedly.  Its tuple is
# immutable and deterministic, so memoize it once in this process before any
# Cycle478 construction.  This is a resource control, not class coarsening.
_EXACT_EFFECTS = c448.exact_effects()
c448.exact_effects = lambda: _EXACT_EFFECTS
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_SUPPORT_NINE_MIXED_QUOTIENT_AUXILIARY_CYCLE478_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 6.0e-10
WALL_CAP_SECONDS = 720.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

# Frozen source representative.  It is not changed after construction begins.
SELECTED_VECTOR = tuple(
    {
        0: -271694, 1: -89182, 2: -717604, 3: 559980,
        4: -1003816, 11: 765000, 16: -942633, 20: 174216,
        31: 512400,
    }.get(index, 0)
    for index in range(55)
)
SELECTED_DENOMINATOR = 823593
SELECTED_SUPPORT = 9
SELECTED_MAXIMUM_COEFFICIENT = 1003816
INHERITED_BINARY_ESTIMATE = 191
FROZEN_BOUNDED_GADGETS = 208
ARITY_SPLITS = 17
PRIOR_COLUMNS = 635
PRIOR_RANK = 620
PRIOR_AUX_RANK = 580
PRIOR_PROJECTED = 15
FROZEN_C471_SHA = "792dc308187359c859a65432bdb3c585cd48528fe0f77e6919f0a3145386c32f"


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
    return DomainMatrix.from_Matrix(matrix).rank()


def contracts() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "support 9", "maximum coefficient 1003816", "normalization n=823593",
        "191-gadget estimate", "208-gadget bounded dag", "720-second wall cap",
        "4 gib rss cap", "resource forecast", "block rank certificate",
        "every exact auxiliary class shared", "full augmented rank",
        "full augmented nullity", "projected-old nullity", "train l=3",
        "held l=6", "all 24 proper-cubic frames", "exact e/g",
        "exact inverse", "dependency-closed deletion",
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
    check("the Cycle478 note freezes the support-nine target, corrected resource DAG, and claim boundary", not missing, missing)


def source_contracts() -> None:
    body = normalized(c471.NOTE)
    runner = Path(c471.__file__)
    check(
        "the Cycle471 retained surface is an explicit contracted source, not silently recomputed evidence",
        c471.NOTE.is_file()
        and sha256(runner.read_bytes()).hexdigest() == FROZEN_C471_SHA
        and "full augmented rank 620" in body
        and "full augmented nullity 15" in body
        and "projected-old nullity 15" in body
        and "final support-9 fixed-g55 row" in body,
        {"Cycle471_surface": "input", "Cycle471_runner_SHA256": FROZEN_C471_SHA,
         "authority": AUTHORITY, "audit": AUDIT},
    )


def bit_values(value: int) -> tuple[int, ...]:
    return tuple(1 << bit for bit in range(value.bit_length() - 1, -1, -1) if value & (1 << bit))


def resource_search_controls() -> None:
    print("\nFROZEN SUPPORT-NINE TARGET / PRECONSTRUCTION RESOURCE FORECAST")
    lift = c448.coefficient_lift(c448.exact_effects())
    root = c462.relation_root(SELECTED_VECTOR)
    eigenvalues = tuple(map(float, np.linalg.eigvalsh(root / SELECTED_DENOMINATOR)))
    coefficients = tuple(abs(value) for value in SELECTED_VECTOR if value)
    denominator_inputs = len(bit_values(SELECTED_DENOMINATOR)) + 1
    coefficient_inputs = tuple(len(bit_values(value)) + 1 for value in coefficients)
    offending_coefficients = sum(count > 8 for count in coefficient_inputs)
    candidate = sp.Matrix([[*SELECTED_VECTOR, *([0] * (PRIOR_COLUMNS - 55))]])
    check(
        "the frozen final representative is exact, independent by the Cycle471 completion contract, and PSD-normalized",
        sum(value != 0 for value in SELECTED_VECTOR) == SELECTED_SUPPORT
        and max(coefficients) == SELECTED_MAXIMUM_COEFFICIENT
        and c462.minimum_denominator(SELECTED_VECTOR) == SELECTED_DENOMINATOR
        and c462.predicted_gadgets(SELECTED_VECTOR, SELECTED_DENOMINATOR) == INHERITED_BINARY_ESTIMATE
        and all(value == 0 for value in lift * sp.Matrix(SELECTED_VECTOR))
        and eigenvalues[0] >= -1e-12 and eigenvalues[-1] <= 1 + 1e-12
        and candidate.cols == PRIOR_COLUMNS,
        {
            "selected_vector": tuple((i, value) for i, value in enumerate(SELECTED_VECTOR) if value),
            "support": SELECTED_SUPPORT,
            "maximum_coefficient": SELECTED_MAXIMUM_COEFFICIENT,
            "minimum_denominator": SELECTED_DENOMINATOR,
            "scaled_root_eigenvalues": eigenvalues,
            "contracted_prior_candidate_ranks": (PRIOR_RANK, PRIOR_RANK + 1),
            "source": "Cycle471 exact completion inventory",
        },
    )
    check(
        "the preconstruction forecast falsifies 191 gadgets and freezes the pointer-lawful 208-gadget DAG",
        denominator_inputs == 9 and offending_coefficients == 8
        and 9 + offending_coefficients == ARITY_SPLITS
        and INHERITED_BINARY_ESTIMATE + ARITY_SPLITS == FROZEN_BOUNDED_GADGETS,
        {
            "inherited_binary_estimate": INHERITED_BINARY_ESTIMATE,
            "normalization_popcount_plus_complement": denominator_inputs,
            "coefficient_popcounts_plus_complement": coefficient_inputs,
            "eight_outcome_pointer_maximum": 8,
            "required_arity_splits": ARITY_SPLITS,
            "frozen_bounded_gadgets": FROZEN_BOUNDED_GADGETS,
            "frozen_new_rows": 2 * FROZEN_BOUNDED_GADGETS,
            "forecast_full_rows": 98 + 624 + 2 * FROZEN_BOUNDED_GADGETS,
            "forecast_effect_classes_upper_bound": PRIOR_COLUMNS + 414,
            "forecast_new_physical_programs_L3_plus_L6": 4 * FROZEN_BOUNDED_GADGETS,
            "safe_rank_strategy": "exact B-block rank and left-null residual certificate; no monolithic repeated rational ranks",
            "row_or_N_changed": False,
        },
    )


@dataclass(frozen=True)
class Cycle478Extension:
    effects: tuple[tuple[sp.Expr, ...], ...]
    all_rows: tuple[tuple[int, ...], ...]
    new_rows: tuple[tuple[int, ...], ...]
    gadgets: tuple[c457.GeneralGadget, ...]
    row_labels: tuple[str, ...]


def build_extension() -> Cycle478Extension:
    prior = c471.build_extension()
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
        if len(inputs) > 7:
            raise RuntimeError(f"{label} exceeds the seven-input plus complement pointer bound")
        rest = c454.complement(total)
        input_indices = tuple(register(item) for item in inputs)
        rest_index = register(rest)
        total_index = register(total)
        rows.extend(((*input_indices, rest_index), (total_index, rest_index)))
        labels.extend((label, label))
        gadgets.append(c457.GeneralGadget(label, inputs, total))
        return total

    def bounded_sum(label: str, parts: tuple[tuple[sp.Expr, ...], ...], total: tuple[sp.Expr, ...]):
        if len(parts) <= 7:
            return install(label, parts, total)
        subtotal = install(f"{label} bounded subtotal", parts[:7], c457.sum_effects(parts[:7]))
        return install(label, (subtotal, *parts[7:]), total)

    nodes: dict[tuple[int, int], tuple[sp.Expr, ...]] = {}

    def scaled(old_class: int, multiple: int) -> tuple[sp.Expr, ...]:
        return c457.scale_effect(c448.exact_effects()[old_class], sp.Rational(multiple, SELECTED_DENOMINATOR))

    def service(side: str, old_class: int, coefficient: int) -> tuple[sp.Expr, ...]:
        nodes[(old_class, 1)] = scaled(old_class, 1)
        power = 2
        while power <= max(coefficient, SELECTED_DENOMINATOR):
            half = nodes[(old_class, power // 2)]
            nodes[(old_class, power)] = install(
                f"{side} E{old_class}/823593 power {power // 2}+{power // 2}",
                (half, half), scaled(old_class, power),
            )
            power *= 2
        denominator_parts = tuple(nodes[(old_class, bit)] for bit in bit_values(SELECTED_DENOMINATOR))
        nodes[(old_class, SELECTED_DENOMINATOR)] = bounded_sum(
            f"{side} E{old_class}/823593 denominator", denominator_parts,
            c448.exact_effects()[old_class],
        )
        coefficient_parts = tuple(nodes[(old_class, bit)] for bit in bit_values(coefficient))
        nodes[(old_class, coefficient)] = bounded_sum(
            f"{side} E{old_class} coefficient {coefficient}", coefficient_parts,
            scaled(old_class, coefficient),
        )
        return nodes[(old_class, coefficient)]

    positive = tuple(service("positive", index, coefficient) for index, coefficient in (
        (3, 559980), (11, 765000), (20, 174216), (31, 512400),
    ))
    negative = tuple(service("negative", index, coefficient) for index, coefficient in (
        (0, 271694), (1, 89182), (2, 717604), (4, 1003816), (16, 942633),
    ))
    positive_root = install("positive mixed root", positive, c457.sum_effects(positive))
    negative_root = install("negative mixed root", negative, c457.sum_effects(negative))
    if c454.exact_key(positive_root) != c454.exact_key(negative_root):
        raise RuntimeError("the frozen Cycle478 relation failed exact closure")
    if len(gadgets) != FROZEN_BOUNDED_GADGETS:
        raise RuntimeError(f"frozen 208-gadget bounded forecast was wrong: observed {len(gadgets)}")
    return Cycle478Extension(
        tuple(effects), prior.all_rows + tuple(rows), tuple(rows), tuple(gadgets), tuple(labels)
    )


def new_programs(extension: Cycle478Extension, contact: np.ndarray) -> tuple[c321.Program, ...]:
    programs = []
    for gadget in extension.gadgets:
        programs.extend(c457.addition_program_pair(gadget, contact))
    return tuple(programs)


def retained_cycle471_controls(
    surface: c440.FiniteSurface,
    prior_results: tuple[dict[str, object], ...],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    extension = c471.build_extension()
    prior_programs = {
        length: tuple(program for result in prior_results for program in result["programs"][length])
        for length in (3, 6)
    }
    added = {length: c471.new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle471-retained", index, "coarse",
            "retained frozen support-eight quotient", tuple(program.coarse_effects),
        )
        for index, program in enumerate(programs[3])
    )
    installed = c385.build_effect_system(surface.installed.menus + presentations, effect_functionality_premise=True)
    matrix = sp.Matrix(np.rint(installed.incidence).astype(int).tolist())
    if installed.incidence.shape != (722, PRIOR_COLUMNS):
        raise RuntimeError(f"retained Cycle471 surface changed: {installed.incidence.shape}")
    return {
        "extension": extension, "programs": added, "installed": installed, "matrix": matrix,
        "rank": PRIOR_RANK, "nullity": PRIOR_COLUMNS - PRIOR_RANK, "projected": PRIOR_PROJECTED,
    }


def modular_rref_nullspace(matrix: sp.Matrix, prime: int) -> tuple[int, tuple[int, ...], np.ndarray]:
    """Dense vectorized RREF over one small prime; rows of output span ker(matrix)."""
    raw = np.asarray(matrix.tolist(), dtype=np.int64) % prime
    rows, cols = raw.shape
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(cols):
        candidates = np.flatnonzero(raw[pivot_row:, column])
        if not len(candidates):
            continue
        selected = pivot_row + int(candidates[0])
        if selected != pivot_row:
            raw[[pivot_row, selected]] = raw[[selected, pivot_row]]
        inverse = pow(int(raw[pivot_row, column]), -1, prime)
        raw[pivot_row] = (raw[pivot_row] * inverse) % prime
        factors = raw[:, column].copy()
        factors[pivot_row] = 0
        raw = (raw - factors[:, None] * raw[pivot_row][None, :]) % prime
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    free = tuple(column for column in range(cols) if column not in set(pivot_columns))
    null = np.zeros((len(free), cols), dtype=np.int64)
    for index, column in enumerate(free):
        null[index, column] = 1
        for row, pivot in enumerate(pivot_columns):
            null[index, pivot] = (-raw[row, column]) % prime
    return len(pivot_columns), tuple(pivot_columns), null


def exact_left_null_certificate(new: sp.Matrix) -> tuple[int, sp.Matrix, int]:
    """CRT-lift a rational left-null basis and verify it over ZZ exactly."""
    primes = (1_000_003, 1_000_033, 1_000_037)
    modular_results = tuple(modular_rref_nullspace(new.T, prime) for prime in primes)
    ranks = tuple(item[0] for item in modular_results)
    pivots = tuple(item[1] for item in modular_results)
    if len(set(ranks)) != 1 or len(set(pivots)) != 1:
        raise RuntimeError(f"modular pivot instability: ranks {ranks}")
    residues = tuple(item[2] for item in modular_results)
    modulus = 1
    combined = np.zeros(residues[0].shape, dtype=object)
    for prime, values in zip(primes, residues):
        inverse = pow(modulus % prime, -1, prime)
        for index in np.ndindex(combined.shape):
            current = int(combined[index])
            current += modulus * (((int(values[index]) - current) % prime) * inverse % prime)
            combined[index] = current
        modulus *= prime
    lifted_rows = []
    for raw_row in combined:
        rationals = []
        for value in raw_row:
            reconstructed = _integer_rational_reconstruction(int(value), modulus, ZZ)
            if reconstructed is None:
                raise RuntimeError("CRT rational reconstruction failed")
            rationals.append(sp.Rational(reconstructed.numerator, reconstructed.denominator))
        denominator = sp.ilcm(*(value.q for value in rationals))
        integers = [int(value * denominator) for value in rationals]
        divisor = abs(sp.gcd_list(integers)) or 1
        integers = [value // divisor for value in integers]
        first = next((value for value in integers if value), 1)
        if first < 0:
            integers = [-value for value in integers]
        lifted_rows.append(integers)
    lifted = sp.Matrix(lifted_rows) if lifted_rows else sp.zeros(0, new.rows)
    return ranks[0], lifted, modulus


def structural_disposition(
    local: sp.Matrix, keep_rows: tuple[int, ...], candidate: sp.Matrix,
    prior_kernel: sp.Matrix,
) -> dict[str, object]:
    kept = local[list(keep_rows), :]
    old = kept[:, :PRIOR_COLUMNS]
    new = kept[:, PRIOR_COLUMNS:]
    # A direct ZZ nullspace is cap-hostile for this sparse 0/1 block.  Modular
    # RREF over three primes, CRT rational reconstruction, and literal integer
    # verification provide the exact lower/upper rank sandwich.
    local_rank, left_null, modulus = exact_left_null_certificate(new)
    exact_left_null = left_null * new == sp.zeros(left_null.rows, new.cols)
    left_independent = (
        left_null.rows == 0
        or exact_rank(left_null) == left_null.rows
    )
    exact_rank_certificate = (
        exact_left_null and left_independent and local_rank + left_null.rows == new.rows
    )
    residual = left_null * old
    residual_rank = exact_rank(residual) if residual.rows else 0
    quotient_signature = residual * prior_kernel.T
    candidate_signature = candidate * prior_kernel.T
    quotient_rank = exact_rank(quotient_signature) if quotient_signature.rows else 0
    candidate_nonzero = any(value != 0 for value in candidate_signature)
    candidate_span = (
        quotient_rank == 1 and candidate_nonzero
        and exact_rank(quotient_signature.col_join(candidate_signature)) == 1
    )
    residual_zero_mod_prior = quotient_rank == 0
    independent = quotient_rank
    rank = PRIOR_RANK + local_rank + independent
    aux_rank = PRIOR_AUX_RANK + local_rank
    projected = 55 - rank + aux_rank
    return {
        "new_block_shape": new.shape, "new_block_rank": local_rank,
        "left_null_rows": left_null.rows, "old_residual_rank": residual_rank,
        "CRT_modulus": modulus, "exact_integer_left_null": exact_left_null,
        "exact_rank_certificate": exact_rank_certificate,
        "quotient_signature_rank": quotient_rank,
        "candidate_signature_nonzero": candidate_nonzero,
        "candidate_span_mod_prior": candidate_span,
        "residual_zero_mod_prior": residual_zero_mod_prior, "rank": rank,
        "nullity": local.cols - rank, "aux_rank": aux_rank, "projected": projected,
    }


def augmented_surface_controls(
    surface: c440.FiniteSurface,
    prior_results: tuple[dict[str, object], ...],
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nFULL CYCLE478 SHARED-AUXILIARY ACCOUNT / BLOCK RANK CERTIFICATE")
    extension = build_extension()
    prior_programs = {
        length: tuple(program for result in prior_results for program in result["programs"][length])
        for length in (3, 6)
    }
    added = {length: new_programs(extension, fixtures[length].contact) for length in (3, 6)}
    all_programs = {length: (*prior_programs[length], *added[length]) for length in (3, 6)}
    presentations = tuple(
        c385.MenuPresentation(
            program.name, "Cycle478-E-over-823593", index, "coarse",
            "frozen support-nine mixed quotient", tuple(program.coarse_effects),
        )
        for index, program in enumerate(all_programs[3])
    )
    installed = c385.build_effect_system(surface.installed.menus + presentations, effect_functionality_premise=True)
    expected = np.zeros((len(extension.all_rows), len(extension.effects)), dtype=int)
    for row_index, row in enumerate(extension.all_rows):
        for class_index in row:
            expected[row_index, class_index] += 1
    physical_rows = np.rint(installed.incidence[-len(extension.all_rows):]).astype(int)
    full = np.rint(installed.incidence).astype(int)
    local = sp.Matrix(expected[-len(extension.new_rows):].tolist())
    candidate = sp.Matrix([[*SELECTED_VECTOR, *([0] * (PRIOR_COLUMNS - 55))]])
    prior_matrix = prior_results[-1]["matrix"]
    certified_prior_rank, prior_kernel, prior_modulus = exact_left_null_certificate(prior_matrix.T)
    prior_kernel_exact = prior_kernel * prior_matrix.T == sp.zeros(prior_kernel.rows, prior_matrix.rows)
    disposition = structural_disposition(
        local, tuple(range(local.rows)), candidate, prior_kernel
    )
    rank = disposition["rank"]
    nullity = disposition["nullity"]
    projected = disposition["projected"]
    prior_prefix = full[:-len(extension.new_rows)]
    prior_matrix_array = np.asarray(prior_matrix.tolist(), dtype=int)
    prefix_match = (
        np.array_equal(prior_prefix[:, :PRIOR_COLUMNS], prior_matrix_array)
        and np.count_nonzero(prior_prefix[:, PRIOR_COLUMNS:]) == 0
    )
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
        float(np.linalg.norm(c317.stack_isometry(program.kraus).conj().T @ c317.stack_isometry(program.kraus) - I2))
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
        "the frozen support-nine row compiles with an exact block certificate and every shared auxiliary class retained",
        len(extension.gadgets) == FROZEN_BOUNDED_GADGETS
        and len(extension.new_rows) == len(added[3]) == len(added[6]) == 416
        and len(extension.all_rows) == 1040
        and installed.incidence.shape[0] == 1138
        and installed.incidence.shape[1] == len(extension.effects)
        and np.array_equal(physical_rows, expected)
        and prefix_match
        and certified_prior_rank == PRIOR_RANK and prior_kernel.rows == 15 and prior_kernel_exact
        and disposition["exact_rank_certificate"]
        and disposition["candidate_span_mod_prior"]
        and disposition["quotient_signature_rank"] == 1
        and nullity == projected == 14 and rank == installed.incidence.shape[1] - 14
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
            "reduction_from_Cycle471": PRIOR_PROJECTED - projected,
            "remaining_beyond_Pauli_tangent": projected - 3,
            "new_auxiliary_classes_beyond_Cycle471": len(extension.effects) - PRIOR_COLUMNS,
            "block_certificate": disposition,
            "retained_prefix_kernel_certificate": {
                "rank": certified_prior_rank, "nullity": prior_kernel.rows,
                "CRT_modulus": prior_modulus, "exact_integer_kernel": prior_kernel_exact,
            },
            "prior_prefix_exactly_recovered": prefix_match,
            "maximum_exact_physical_effect_residual": maximum_effect,
            "maximum_train_held_class_residual": cross_size,
            "maximum_stack_isometry_residual": isometry,
            "trace_grade_residual": trace_residual,
            "Pauli_tangent_residual": tangent_residual,
            "grade_homogeneity_assumed": False,
        },
    )
    return {
        "extension": extension, "programs": added, "installed": installed, "local": local,
        "rank": rank, "nullity": nullity, "projected": projected,
        "disposition": disposition, "prior_kernel": prior_kernel,
    }


def deletion_controls(result: dict[str, object]) -> None:
    print("\nDEPENDENCY-CLOSED ROUTE DELETIONS")
    extension = result["extension"]
    local: sp.Matrix = result["local"]
    prior_kernel: sp.Matrix = result["prior_kernel"]
    candidate = sp.Matrix([[*SELECTED_VECTOR, *([0] * (PRIOR_COLUMNS - 55))]])
    all_rows = set(range(local.rows))
    side_groups = tuple(
        tuple(index for index, label in enumerate(extension.row_labels) if label.startswith(side))
        for side in ("positive", "negative")
    )
    terminal_groups = tuple(
        tuple(index for index, label in enumerate(extension.row_labels) if label == f"{side} mixed root")
        for side in ("positive", "negative")
    )
    side_dispositions = tuple(
        structural_disposition(local, tuple(sorted(all_rows - set(group))), candidate, prior_kernel) for group in side_groups
    )
    terminal_dispositions = tuple(
        structural_disposition(local, tuple(sorted(all_rows - set(group))), candidate, prior_kernel) for group in terminal_groups
    )
    delete_all = (PRIOR_RANK, result["installed"].incidence.shape[1] - PRIOR_RANK, PRIOR_PROJECTED)
    check(
        "dependency-closed deletion of either side and surgical deletion of either root restore the Cycle471 projected freedom",
        result["projected"] == 14 and delete_all[2] == 15
        and tuple(map(len, side_groups)) == (184, 232)
        and tuple(map(len, terminal_groups)) == (2, 2)
        and all(item["exact_rank_certificate"] and item["residual_zero_mod_prior"] and item["projected"] == 15 for item in side_dispositions)
        and all(item["exact_rank_certificate"] and item["residual_zero_mod_prior"] and item["projected"] == 15 for item in terminal_dispositions),
        {
            "delete_all_Cycle478_rows_rank_full_nullity_projected": delete_all,
            "dependency_closed_side_deletions": side_dispositions,
            "dependency_closed_side_row_counts": tuple(map(len, side_groups)),
            "terminal_root_deletions": terminal_dispositions,
            "terminal_root_row_counts": tuple(map(len, terminal_groups)),
        },
    )


def bounded_class_cases(length: int, count: int) -> tuple[c433.FormationCase, ...]:
    """Allocate all finite class fixtures inside the signed seven-bit adapter."""
    fixture = c457.c364.c342.c338.build_fixture(length)
    payloads = c457.c364.words(fixture, 6)
    z = 11 if length == 3 else -11
    width = 126
    return tuple(
        c433.FormationCase(
            length, fixture,
            (index % width - 62, index // width - 4, z),
            (index % width - 63, index // width - 4, z),
            payloads[index % len(payloads)], payloads[(index + 1) % len(payloads)],
            length == 6,
        )
        for index in range(count)
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
    cases_by_length = {length: bounded_class_cases(length, len(installed.effects)) for length in (3, 6)}
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
                output, local_leakage = c436.apply_law(source, pointer, law)
                restored, inverse = c436.apply_law(output, pointer, law, reverse=True)
                word = c440.extract_pointer_word(output)
                packet_failures += int(word is None or restored != source)
                leakage_failures += local_leakage + inverse
                if word is not None:
                    occurrences[class_index].append(word)
                active += 1
            for pointer in range(len(row), 8):
                output, local_leakage = c436.apply_law(source, pointer, law)
                idle_failures += int(output != source or local_leakage)
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
                    f"Cycle478 frame class {class_index}", (case,), ((pointer, 0),), True, False
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
        "all new support-nine contexts pass train/held packets, inverse, leakage, idle, all-24 covariance, and mass controls",
        len(rows) == 416 and max(map(len, rows)) <= 8
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
            "active_pointer_cases": active, "idle_pointer_cases": idle,
            "maximum_effect_residual": maximum_effect,
            "maximum_completeness_residual": maximum_completeness,
            "maximum_fixed_bank_isometry_residual": maximum_bank,
            "maximum_E_G_residual": maximum_forward,
            "maximum_inverse_residual": maximum_inverse,
            "leakage_packet_idle_failures": (leakage_failures, packet_failures, idle_failures),
            "proper_cubic_frames": len(frames), "all_frame_packet_cases": frame_cases,
            "frame_failures": frame_failures, "physical_encoding_covariance": tuple(covariance),
            "one_particle_mass_relative_residual": mass_residual,
            "program_M2_per_eight_program_bank": 3, "pointer_M2": 3,
            "maximum_primitive_support_M2": 3,
        },
    )


def anti_fit_scope_resource_controls(result: dict[str, object], started: float) -> None:
    lift = c448.coefficient_lift(c448.exact_effects())
    corrupted = list(SELECTED_VECTOR)
    corrupted[3] += 1
    exact_corruption = any(value != 0 for value in lift * sp.Matrix(corrupted))
    underscaled = max(np.linalg.eigvalsh(c462.relation_root(SELECTED_VECTOR) / (SELECTED_DENOMINATOR - 1))) > 1
    check(
        "coefficient corruption, underscaling, and the pointer-arity estimate failure remain visible rather than fit away",
        exact_corruption and underscaled
        and c462.predicted_gadgets(SELECTED_VECTOR, SELECTED_DENOMINATOR) == 191
        and len(result["extension"].gadgets) == 208,
        {
            "exact_corruption_detected": exact_corruption,
            "N823592_root_exceeds_identity": underscaled,
            "falsified_unbounded_binary_estimate": 191,
            "frozen_pointer_lawful_observed_gadget_count": len(result["extension"].gadgets),
        },
    )
    check(
        "the frozen fixed-G55 quotient inventory is functionally compiled without selecting grade, state, occurrence, or Born probability",
        result["projected"] == 14 and result["nullity"] == 14
        and AUTHORITY == "none" and AUDIT == "unset",
        {
            "uncompiled_frozen_fixed_G55_quotient_directions": 0,
            "projected_old_nullity": result["projected"],
            "Pauli_tangent_directions": 3,
            "directions_beyond_Pauli_tangent": result["projected"] - 3,
            "cost_optimality_claimed": False, "grade_or_state_selected": False,
            "homogeneity_imported": False, "candidate_packets_are_Records": False,
            "coherent_norm_is_probability": False,
            "occurrence_law": "none", "frequency_law": "none",
            "Born_probability_selected": False,
            "continuum_or_arbitrary_support_closure": False,
            "shared_substrate_obstruction": "none established", "axiom_pressure": "none",
        },
    )
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    check(
        "the frozen 208-gadget compiler completes below its wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and maxrss < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "raw_maxrss_Darwin_bytes": maxrss, "RSS_cap_bytes": RSS_CAP_BYTES},
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle478 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    try:
        contracts()
        source_contracts()
        resource_search_controls()
        fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
        with redirect_stdout(StringIO()):
            surface = c440.reconstruct_surface(fixtures)
            c454_result = c454.exact_and_physical_surface_controls(surface, fixtures)
            c457_result = c457.augmented_surface_controls(surface, c454_result, fixtures)
            c462_result = c462.augmented_surface_controls(surface, c454_result, c457_result, fixtures)
            c466_result = c471.retained_cycle466_controls(
                surface, (c454_result, c457_result, c462_result), fixtures
            )
            c471_result = retained_cycle471_controls(
                surface, (c454_result, c457_result, c462_result, c466_result), fixtures
            )
        result = augmented_surface_controls(
            surface, (c454_result, c457_result, c462_result, c466_result, c471_result), fixtures
        )
        deletion_controls(result)
        physical_packet_controls(result, fixtures)
        anti_fit_scope_resource_controls(result, started)
    except WallCapExceeded as error:
        check("the Cycle478 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY")
    print({
        "result": "final frozen support-nine fixed-G55 quotient row compiled with bounded arity",
        "inherited_191_gadget_estimate": "falsified by eight-outcome pointer arity",
        "frozen_bounded_gadgets": FROZEN_BOUNDED_GADGETS,
        "Cycle471_rank_nullity": (PRIOR_RANK, PRIOR_COLUMNS - PRIOR_RANK),
        "full_augmented_rank": result["rank"] if "result" in locals() else None,
        "full_augmented_nullity": result["nullity"] if "result" in locals() else None,
        "projected_old_nullity": result["projected"] if "result" in locals() else None,
        "uncompiled_frozen_fixed_G55_quotient_directions": 0,
        "grade_or_state_selected": False, "homogeneity_assumed": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
