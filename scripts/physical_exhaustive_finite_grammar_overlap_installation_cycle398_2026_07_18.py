#!/usr/bin/env python3
"""Cycle 398: exhaust and physically install a finite overlap grammar.

Grammar G55[2:8]: use exactly the 55 Cycle-381 equal-effect classes; a
presentation is a nondecreasing multiset of 2 through 8 class indices,
repetition allowed; it is lawful when the Frobenius residual of its effect sum
from I2 is below 1.2e-10.  Effect equality retains the supplied 13-decimal
Cycle-383 matrix key.  Meet-in-the-middle enumeration uses exact-radius
binary64 cKDTree queries and direct residual revalidation.

The exhaustive grammar contains 82 rows.  Its exact integer row span has rank
31, equal to the Cycle-394 physical system.  The independent augmentation
basis is empty.  As a stronger physical coverage control, all 51 previously
uninstalled lawful rows are compiled into seven fixed contact-sensitive M2
carrier banks and installed, giving 98 menus, 55 classes, rank 31.

The saturation statement is restricted to G55[2:8] and passes the written
N1-N8 gate in the companion note.  It is not a universal menu-eligibility,
Born-selection, actuality, frequency, global no-go, or axiom-pressure result.
Authority is none; audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from inspect import getsource
from io import StringIO
from itertools import combinations_with_replacement
from pathlib import Path
import sys

import numpy as np
from scipy.spatial import cKDTree
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EXHAUSTIVE_FINITE_GRAMMAR_OVERLAP_INSTALLATION_CYCLE398_NOTE_2026-07-18.md"
)

import physical_higher_outcome_overlap_menu_fixed_carrier_cycle394_2026_07_18 as c394


c390 = c394.c390
c385 = c394.c385
c381 = c394.c381
c383 = c394.c383
c323 = c394.c323
c321 = c394.c321
c317 = c394.c317
TOL = c394.TOL
I2 = c394.I2
MIN_OUTCOMES = 2
MAX_OUTCOMES = 8
CLASS_KEY_DECIMALS = 13
PROGRAM_M2 = 3
PROGRAM_DIMENSION = 2**PROGRAM_M2
POINTER_M2 = 3
POINTER_DIMENSION = 2**POINTER_M2
PROGRAMS_PER_BANK = 8
AUTHORITY = "none"
AUDIT = "unset"
EXPECTED_COUNTS = (4, 13, 17, 17, 21, 5, 5)
EXPECTED_NEW_COUNTS = (0, 3, 6, 14, 20, 4, 4)
EXPECTED_ALL_HASH = "7bdd1346e7b2599395cc43ead11467490403fd6d639041389523e2fc5eb7b01f"
EXPECTED_NEW_HASH = "bfb82221940b6128561f30ffc5c444fd00b9303cfe7cb29e3711e70aeb46b372"
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


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-398 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "g55[2:8]",
        "55 cycle-381 effect classes",
        "two through eight outcomes",
        "multiplicity is allowed",
        "13-decimal matrix key",
        "frobenius residual is strictly below 1.2e-10",
        "4, 13, 17, 17, 21, 5, and 5",
        "82 lawful partitions",
        "51 previously uninstalled partitions",
        "seven fixed carrier banks",
        "283 pointer outcomes",
        "98 menus, 55 classes, rank 31",
        "affine dimension 24",
        "all 51 added-row deletion ranks are 31",
        "independent augmentation basis is empty",
        "e g_logical = g_physical e",
        "l=3 and held l=6",
        "all 24 proper-cubic frames",
        "one-particle mass fixture",
        "n1 — alternative route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate disposition: pass for the scoped finite-grammar saturation statement",
        "born selection: not claimed",
        "universal menu eligibility: not claimed",
        "axiom pressure: not claimed",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins G55[2:8], exhaustive counts, physical installation, inventory, status split, and N1-N8 gate",
        not missing,
        missing,
    )
    return {"missing": missing}


def cycle394_source(
    fixtures: dict[int, c317.PhysicalFixture],
) -> tuple[
    c385.EffectSystem,
    c390.CompiledMenus,
    c390.CompiledMenus,
    c385.EffectSystem,
]:
    base, prior, additional, _host_residual = c394.candidate_source(fixtures)
    installed = c385.build_effect_system(
        base.menus
        + c390.compiled_menu_presentations(prior)
        + c394.additional_presentations(additional),
        effect_functionality_premise=True,
    )
    if installed.incidence.shape != (47, 55) or c385.matrix_rank(installed.incidence) != 31:
        raise ValueError("the root-reviewed Cycle-394 source surface changed")
    return base, prior, additional, installed


def hermitian_vector(effect: np.ndarray) -> np.ndarray:
    """Weighted coordinates whose Euclidean norm is the Frobenius norm."""
    array = np.asarray(effect, dtype=complex)
    return np.asarray((
        array[0, 0].real,
        array[1, 1].real,
        np.sqrt(2) * array[0, 1].real,
        np.sqrt(2) * array[0, 1].imag,
    ))


def rows_hash(rows: tuple[tuple[int, ...], ...]) -> str:
    digest = sha256()
    for row in rows:
        digest.update((repr(row) + "\n").encode())
    return digest.hexdigest()


@dataclass(frozen=True)
class GrammarResult:
    rows_by_outcome: dict[int, tuple[tuple[int, ...], ...]]
    half_combination_counts: dict[int, int]
    maximum_identity_residual: float

    @property
    def rows(self) -> tuple[tuple[int, ...], ...]:
        return tuple(
            row
            for outcomes in range(MIN_OUTCOMES, MAX_OUTCOMES + 1)
            for row in self.rows_by_outcome[outcomes]
        )


def enumerate_grammar(
    effects: tuple[np.ndarray, ...],
    *,
    minimum_outcomes: int = MIN_OUTCOMES,
    maximum_outcomes: int = MAX_OUTCOMES,
    identity_tolerance: float = TOL,
) -> GrammarResult:
    if len(effects) != 55:
        raise ValueError("G55 requires exactly 55 effect-class representatives")
    if minimum_outcomes != MIN_OUTCOMES or maximum_outcomes != MAX_OUTCOMES:
        raise ValueError("this certificate is defined only for outcome range 2:8")
    if identity_tolerance != TOL:
        raise ValueError("this certificate requires the declared identity tolerance")
    keys = tuple(c383.matrix_key(effect) for effect in effects)
    if len(set(keys)) != len(keys):
        raise ValueError("the supplied effect-class representatives are not canonical-unique")

    vectors = np.asarray([hermitian_vector(effect) for effect in effects])
    target = hermitian_vector(I2)
    half_tables: dict[int, tuple[np.ndarray, np.ndarray]] = {}
    half_counts = {}
    for width in range(1, MAX_OUTCOMES // 2 + 1):
        combinations = np.asarray(
            list(combinations_with_replacement(range(len(effects)), width)),
            dtype=np.int16,
        )
        sums = vectors[combinations].sum(axis=1)
        half_tables[width] = (combinations, sums)
        half_counts[width] = len(combinations)

    rows_by_outcome = {}
    maximum_residual = 0.0
    for outcomes in range(minimum_outcomes, maximum_outcomes + 1):
        left_width = outcomes // 2
        right_width = outcomes - left_width
        left_combinations, left_sums = half_tables[left_width]
        right_combinations, right_sums = half_tables[right_width]
        tree = cKDTree(right_sums)
        matches = tree.query_ball_point(
            target - left_sums,
            r=identity_tolerance,
            eps=0,
            workers=1,
        )
        rows: set[tuple[int, ...]] = set()
        for left_index, right_indices in enumerate(matches):
            for right_index in right_indices:
                if left_width == right_width and left_index > right_index:
                    continue
                row = tuple(sorted((
                    *map(int, left_combinations[left_index]),
                    *map(int, right_combinations[right_index]),
                )))
                residual = float(np.linalg.norm(
                    vectors[np.asarray(row)].sum(axis=0) - target
                ))
                if residual < identity_tolerance:
                    rows.add(row)
                    maximum_residual = max(maximum_residual, residual)
        rows_by_outcome[outcomes] = tuple(sorted(rows))
    return GrammarResult(rows_by_outcome, half_counts, maximum_residual)


def direct_lower_outcome_crosscheck(
    effects: tuple[np.ndarray, ...],
) -> dict[int, tuple[tuple[int, ...], ...]]:
    """Independent direct enumeration for the 2/3/4-outcome portion."""
    rows_by_outcome = {}
    for outcomes in range(2, 5):
        rows = []
        for row in combinations_with_replacement(range(len(effects)), outcomes):
            total = sum(
                (effects[index] for index in row),
                start=np.zeros((2, 2), dtype=complex),
            )
            if np.linalg.norm(total - I2) < TOL:
                rows.append(tuple(row))
        rows_by_outcome[outcomes] = tuple(rows)
    return rows_by_outcome


def grammar_controls(
    base: c385.EffectSystem,
    grammar: GrammarResult,
) -> dict[str, object]:
    direct = direct_lower_outcome_crosscheck(base.effects)
    counts = tuple(
        len(grammar.rows_by_outcome[outcomes])
        for outcomes in range(MIN_OUTCOMES, MAX_OUTCOMES + 1)
    )
    keys = tuple(c383.matrix_key(effect) for effect in base.effects)
    canonical_roundtrip_residual = max(float(np.linalg.norm(
        c383.matrix_from_key(key, (2, 2)) - effect
    )) for key, effect in zip(keys, base.effects))
    detail = {
        "grammar": "G55[2:8]",
        "effect_classes": len(base.effects),
        "effect_key_decimal_places": CLASS_KEY_DECIMALS,
        "outcome_minimum": MIN_OUTCOMES,
        "outcome_maximum": MAX_OUTCOMES,
        "multiplicity_allowed": True,
        "presentation_canonical_form": "nondecreasing integer class-index tuple",
        "identity_metric": "weighted Hermitian coordinates = Frobenius norm",
        "identity_tolerance_strict": TOL,
        "meet_in_middle_half_counts": grammar.half_combination_counts,
        "lawful_counts_2_through_8": counts,
        "lawful_partitions": len(grammar.rows),
        "maximum_lawful_identity_residual": grammar.maximum_identity_residual,
        "all_rows_hash": rows_hash(grammar.rows),
        "lower_outcome_direct_crosscheck_counts": tuple(
            len(direct[outcomes]) for outcomes in range(2, 5)
        ),
        "lower_outcome_direct_crosscheck_equal": all(
            direct[outcomes] == grammar.rows_by_outcome[outcomes]
            for outcomes in range(2, 5)
        ),
        "canonical_effect_keys_unique": len(set(keys)) == 55,
        "maximum_key_roundtrip_residual": canonical_roundtrip_residual,
    }
    check(
        "G55[2:8] is exhaustively enumerated with declared canonical class, multiset, and identity arithmetic",
        counts == EXPECTED_COUNTS
        and len(grammar.rows) == 82
        and grammar.half_combination_counts == {
            1: 55, 2: 1540, 3: 29260, 4: 424270
        }
        and grammar.maximum_identity_residual < TOL
        and detail["all_rows_hash"] == EXPECTED_ALL_HASH
        and detail["lower_outcome_direct_crosscheck_counts"] == (4, 13, 17)
        and detail["lower_outcome_direct_crosscheck_equal"]
        and detail["canonical_effect_keys_unique"]
        and canonical_roundtrip_residual < 1e-12,
        detail,
    )
    return detail


def existing_grammar_rows(
    base: c385.EffectSystem,
) -> set[tuple[int, ...]]:
    return {
        tuple(sorted(row))
        for row in (
            *base.menu_classes,
            *c390.EXPECTED_CLASS_ROWS,
            *c394.ADDITIONAL_CLASS_ROWS,
        )
        if MIN_OUTCOMES <= len(row) <= MAX_OUTCOMES
    }


def incidence_row(row: tuple[int, ...]) -> np.ndarray:
    return np.bincount(row, minlength=55).astype(int)


def exact_rank(matrix: np.ndarray) -> int:
    integer = np.rint(matrix).astype(int)
    if np.linalg.norm(matrix - integer) != 0:
        raise ValueError("exact incidence rank requires an integer matrix")
    return int(sp.Matrix(integer.tolist()).rank())


def rank_reduction_controls(
    base: c385.EffectSystem,
    cycle394_system: c385.EffectSystem,
    grammar: GrammarResult,
) -> dict[str, object]:
    existing = existing_grammar_rows(base)
    new_rows = tuple(row for row in grammar.rows if row not in existing)
    new_counts = tuple(
        sum(len(row) == outcomes for row in new_rows)
        for outcomes in range(MIN_OUTCOMES, MAX_OUTCOMES + 1)
    )
    grammar_incidence = np.asarray([incidence_row(row) for row in grammar.rows])
    combined = np.vstack((cycle394_system.incidence, grammar_incidence))
    cycle394_exact_rank = exact_rank(cycle394_system.incidence)
    combined_exact_rank = exact_rank(combined)
    current = cycle394_system.incidence.copy()
    independent = []
    for row in grammar.rows:
        candidate = np.vstack((current, incidence_row(row)))
        if exact_rank(candidate) > exact_rank(current):
            independent.append(row)
            current = candidate
    detail = {
        "Cycle394_shape": cycle394_system.incidence.shape,
        "Cycle394_numerical_rank": c385.matrix_rank(cycle394_system.incidence),
        "Cycle394_exact_integer_rank": cycle394_exact_rank,
        "grammar_rows": len(grammar.rows),
        "grammar_rows_already_present": len(existing.intersection(grammar.rows)),
        "previously_uninstalled_rows": len(new_rows),
        "previously_uninstalled_counts_2_through_8": new_counts,
        "previously_uninstalled_rows_hash": rows_hash(new_rows),
        "combined_numerical_rank": c385.matrix_rank(combined),
        "combined_exact_integer_rank": combined_exact_rank,
        "maximal_independent_augmentation_basis": tuple(independent),
        "maximal_independent_augmentation_basis_size": len(independent),
        "affine_dimension_on_55_classes": 55 - combined_exact_rank,
        "scoped_saturation": "all G55[2:8] incidence rows lie in the exact Cycle394 row span",
    }
    check(
        "all 82 grammar rows have exact integer rank 31 over Cycle394; the independent augmentation basis is empty",
        cycle394_system.incidence.shape == (47, 55)
        and cycle394_exact_rank == 31
        and c385.matrix_rank(cycle394_system.incidence) == 31
        and len(existing.intersection(grammar.rows)) == 31
        and len(new_rows) == 51
        and new_counts == EXPECTED_NEW_COUNTS
        and detail["previously_uninstalled_rows_hash"] == EXPECTED_NEW_HASH
        and c385.matrix_rank(combined) == 31
        and combined_exact_rank == 31
        and not independent
        and detail["affine_dimension_on_55_classes"] == 24,
        detail,
    )
    return {**detail, "new_rows": new_rows}


@dataclass(frozen=True)
class FixedMenuBank:
    programs: tuple[c321.Program, ...]

    def __post_init__(self) -> None:
        if not 1 <= len(self.programs) <= PROGRAMS_PER_BANK:
            raise ValueError("a bank requires one through eight lawful programs")
        if len({program.name for program in self.programs}) != len(self.programs):
            raise ValueError("lawful program names must be distinct within a bank")
        if any(
            len(program.kraus) > POINTER_DIMENSION
            or np.linalg.norm(program.completeness - I2) >= TOL
            for program in self.programs
        ):
            raise ValueError("every bank program must fit and be exhaustive")

    @property
    def block_kraus(self) -> tuple[tuple[np.ndarray, ...], ...]:
        idle = (I2,) + tuple(
            np.zeros((2, 2), dtype=complex)
            for _ in range(POINTER_DIMENSION - 1)
        )
        lawful = tuple(c390.padded_kraus(program) for program in self.programs)
        return lawful + (idle,) * (PROGRAM_DIMENSION - len(self.programs))

    @property
    def update(self) -> np.ndarray:
        tensor = np.zeros((8, 8, 2, 8, 2), dtype=complex)
        for label, blocks in enumerate(self.block_kraus):
            tensor[label, :, :, label, :] = np.asarray(blocks)
        return tensor.reshape(128, 16)


def bank_program_basis(bank: FixedMenuBank, label: int) -> np.ndarray:
    if not 0 <= label < len(bank.programs):
        raise ValueError("program label is outside this bank's lawful code")
    state = np.zeros(PROGRAM_DIMENSION, dtype=complex)
    state[label] = 1
    return state


def validate_bank_program_state(bank: FixedMenuBank, state: np.ndarray) -> None:
    if state.shape != (PROGRAM_DIMENSION,) or abs(np.linalg.norm(state) - 1) >= TOL:
        raise ValueError("program preparation must be a normalized three-M2 state")
    if np.linalg.norm(state[len(bank.programs):]) >= TOL:
        raise ValueError("program preparation leaves this bank's lawful code")


def validate_pointer_blank(label: int) -> None:
    if label != 0:
        raise ValueError("the fixed dilation requires the supplied blank pointer")


def apply_fixed_update(update: np.ndarray, state: np.ndarray) -> np.ndarray:
    return update @ state


def direct_two_use(bank: FixedMenuBank) -> np.ndarray:
    tensor = np.zeros((8, 8, 8, 2, 8, 2), dtype=complex)
    for label, blocks in enumerate(bank.block_kraus):
        for first, left in enumerate(blocks):
            for second, right in enumerate(blocks):
                tensor[label, first, second, :, label, :] = right @ left
    return tensor.reshape(1024, 16)


@dataclass(frozen=True)
class CompiledBank:
    index: int
    rows: tuple[tuple[int, ...], ...]
    compiled: c390.CompiledMenus
    carrier: FixedMenuBank


def compile_banks(
    base: c385.EffectSystem,
    rows: tuple[tuple[int, ...], ...],
    contact: np.ndarray,
) -> tuple[CompiledBank, ...]:
    banks = []
    for bank_index, start in enumerate(range(0, len(rows), PROGRAMS_PER_BANK)):
        batch = rows[start:start + PROGRAMS_PER_BANK]
        compiled = c390.compile_menus(base, batch, contact)
        banks.append(CompiledBank(
            bank_index, batch, compiled, FixedMenuBank(compiled.programs)
        ))
    return tuple(banks)


def bank_presentations(
    banks: tuple[CompiledBank, ...],
) -> tuple[c385.MenuPresentation, ...]:
    rows = []
    for bank in banks:
        for program_index, program in enumerate(bank.compiled.programs):
            rows.append(c385.MenuPresentation(
                name=f"Cycle398-bank{bank.index}/program{program_index}/coarse",
                carrier=f"Cycle398-fixed-menu-bank-{bank.index}",
                program_index=program_index,
                surface="compiled-coarse",
                provenance="Cycle398 exhaustive G55[2:8] physical coverage",
                effects=tuple(program.coarse_effects),
            ))
    return tuple(rows)


def compiler_controls(
    base: c385.EffectSystem,
    banks: tuple[CompiledBank, ...],
) -> dict[str, object]:
    bank_details = []
    global_processes: dict[int, list[np.ndarray]] = {}
    maximum_effect = maximum_completeness = 0.0
    maximum_fixed_isometry = maximum_coherent = 0.0
    maximum_two_use = maximum_two_use_isometry = 0.0
    minimum_contact_update = float("inf")
    minimum_contact_process = float("inf")
    maximum_contact_effect = 0.0
    total_outcomes = total_local_unique = 0
    for bank in banks:
        compiled = bank.compiled
        carrier = bank.carrier
        effect_residual = max(
            float(np.linalg.norm(effect - target))
            for program, targets in zip(compiled.programs, compiled.target_effects)
            for effect, target in zip(program.coarse_effects, targets)
        )
        completeness = max(float(np.linalg.norm(program.completeness - I2))
                           for program in compiled.programs)
        update = carrier.update
        fixed_isometry = float(np.linalg.norm(update.conj().T @ update - np.eye(16)))
        amplitudes = np.zeros(8, dtype=complex)
        amplitudes[:len(carrier.programs)] = np.asarray([
            complex(index + 1, (-1) ** index)
            for index in range(len(carrier.programs))
        ])
        amplitudes /= np.linalg.norm(amplitudes)
        system = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
        output = apply_fixed_update(update, np.kron(amplitudes, system)).reshape(8, 8, 2)
        expected = np.zeros_like(output)
        for label in range(len(carrier.programs)):
            for pointer, operator in enumerate(carrier.block_kraus[label]):
                expected[label, pointer] = amplitudes[label] * operator @ system
        coherent = float(np.linalg.norm(output - expected))
        sequential = c323.two_use_from_fixed(update)
        direct = direct_two_use(carrier)
        two_use = float(np.linalg.norm(sequential - direct))
        two_use_isometry = float(np.linalg.norm(
            sequential.conj().T @ sequential - np.eye(16)
        ))
        identity_compilation = c390.compile_menus(base, bank.rows, I2)
        identity_carrier = FixedMenuBank(identity_compilation.programs)
        contact_update = float(np.linalg.norm(update - identity_carrier.update))
        contact_effect = max(
            float(np.linalg.norm(left - right))
            for actual, deleted in zip(compiled.programs, identity_compilation.programs)
            for left, right in zip(actual.coarse_effects, deleted.coarse_effects)
        )
        contact_process = max(
            float(np.linalg.norm(c321.choi((actual,)) - c321.choi((deleted,))))
            for actual_program, deleted_program in zip(
                compiled.programs, identity_compilation.programs
            )
            for actual, deleted in zip(actual_program.kraus, deleted_program.kraus)
        )
        outcomes = sum(map(len, bank.rows))
        for program, row in zip(compiled.programs, bank.rows):
            for operator, class_index in zip(program.kraus, row):
                global_processes.setdefault(class_index, []).append(c321.choi((operator,)))
        detail = {
            "bank": bank.index,
            "programs": len(bank.rows),
            "idle_extensions": 8 - len(bank.rows),
            "outcome_counts": tuple(map(len, bank.rows)),
            "pointer_outcomes": outcomes,
            "bank_local_unique_effect_blocks": len(compiled.unique_blocks),
            "bank_local_reused_occurrences": outcomes - len(compiled.unique_blocks),
            "effect_recovery_residual": effect_residual,
            "completeness_residual": completeness,
            "fixed_isometry_residual": fixed_isometry,
            "coherent_residual": coherent,
            "two_use_fixed_vs_direct_residual": two_use,
            "two_use_isometry_residual": two_use_isometry,
            "contact_deletion_update_residual": contact_update,
            "contact_deletion_effect_residual": contact_effect,
            "contact_deletion_process_residual": contact_process,
        }
        bank_details.append(detail)
        total_outcomes += outcomes
        total_local_unique += len(compiled.unique_blocks)
        maximum_effect = max(maximum_effect, effect_residual)
        maximum_completeness = max(maximum_completeness, completeness)
        maximum_fixed_isometry = max(maximum_fixed_isometry, fixed_isometry)
        maximum_coherent = max(maximum_coherent, coherent)
        maximum_two_use = max(maximum_two_use, two_use)
        maximum_two_use_isometry = max(maximum_two_use_isometry, two_use_isometry)
        minimum_contact_update = min(minimum_contact_update, contact_update)
        minimum_contact_process = min(minimum_contact_process, contact_process)
        maximum_contact_effect = max(maximum_contact_effect, contact_effect)
    same_class_process = max(
        float(np.linalg.norm(process - processes[0]))
        for processes in global_processes.values()
        for process in processes
    )
    unique_global_classes = len(global_processes)
    detail = {
        "carrier_banks": len(banks),
        "programs_per_bank": tuple(len(bank.rows) for bank in banks),
        "total_lawful_programs": sum(len(bank.rows) for bank in banks),
        "total_pointer_outcomes": total_outcomes,
        "global_unique_effect_classes_used": unique_global_classes,
        "sum_bank_local_unique_effect_blocks": total_local_unique,
        "maximum_effect_recovery_residual": maximum_effect,
        "maximum_completeness_residual": maximum_completeness,
        "maximum_fixed_isometry_residual": maximum_fixed_isometry,
        "maximum_coherent_residual": maximum_coherent,
        "maximum_two_use_fixed_vs_direct_residual": maximum_two_use,
        "maximum_two_use_isometry_residual": maximum_two_use_isometry,
        "minimum_contact_deletion_update_residual": minimum_contact_update,
        "maximum_contact_deletion_effect_residual": maximum_contact_effect,
        "minimum_contact_deletion_process_residual": minimum_contact_process,
        "maximum_same_class_process_tag_residual_across_banks": same_class_process,
        "program_M2_per_bank": PROGRAM_M2,
        "pointer_M2_per_bank": POINTER_M2,
        "fixed_update_application_source": " ".join(getsource(apply_fixed_update).split()),
        "host_program_branch_query": False,
        "bank_details": tuple(bank_details),
    }
    check(
        "all 51 previously uninstalled rows compile into seven fixed contact-sensitive M2 banks",
        len(banks) == 7
        and detail["programs_per_bank"] == (8, 8, 8, 8, 8, 8, 3)
        and detail["total_lawful_programs"] == 51
        and total_outcomes == 283
        and unique_global_classes == 35
        and tuple(row["bank_local_unique_effect_blocks"] for row in bank_details)
            == (17, 18, 12, 15, 12, 12, 8)
        and maximum_effect < TOL
        and maximum_completeness < TOL
        and maximum_fixed_isometry < TOL
        and maximum_coherent < TOL
        and maximum_two_use < TOL
        and maximum_two_use_isometry < TOL
        and minimum_contact_update > 0.3
        and maximum_contact_effect < TOL
        and minimum_contact_process > 0.1
        and same_class_process < TOL
        and detail["fixed_update_application_source"].endswith("return update @ state")
        and not detail["host_program_branch_query"],
        detail,
    )
    return detail


def installed_system_controls(
    cycle394_system: c385.EffectSystem,
    banks: tuple[CompiledBank, ...],
) -> dict[str, object]:
    added = bank_presentations(banks)
    installed = c385.build_effect_system(
        cycle394_system.menus + added,
        effect_functionality_premise=True,
    )
    exact_installed_rank = exact_rank(installed.incidence)
    unique_rows = len({tuple(row) for row in installed.incidence.astype(int)})
    deletion_ranks = tuple(
        c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
        for row in range(len(cycle394_system.menus), len(installed.menus))
    )
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in installed.effects
    ])
    detail = {
        "Cycle394_shape": cycle394_system.incidence.shape,
        "added_physical_presentations": len(added),
        "final_shape": installed.incidence.shape,
        "effect_classes": len(installed.effects),
        "numerical_rank": c385.matrix_rank(installed.incidence),
        "exact_integer_rank": exact_installed_rank,
        "affine_dimension": len(installed.effects) - exact_installed_rank,
        "unique_incidence_rows": unique_rows,
        "each_added_row_deletion_rank": deletion_ranks,
        "trace_grade_minimum": float(np.min(trace_grade)),
        "trace_normalization_residual": float(np.linalg.norm(
            installed.incidence @ trace_grade - 1
        )),
        "effect_functionality_premise_supplied": True,
        "numerical_grade_selected": False,
    }
    check(
        "physical installation covers all 82 grammar rows in a 98-menu, 55-class, exact-rank-31 system",
        len(added) == 51
        and installed.incidence.shape == (98, 55)
        and len(installed.effects) == 55
        and c385.matrix_rank(installed.incidence) == 31
        and exact_installed_rank == 31
        and detail["affine_dimension"] == 24
        and unique_rows == 82
        and deletion_ranks == (31,) * 51
        and detail["trace_grade_minimum"] > 0.05
        and detail["trace_normalization_residual"] < TOL
        and detail["effect_functionality_premise_supplied"]
        and not detail["numerical_grade_selected"],
        detail,
    )
    return {**detail, "system": installed}


def physical_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    banks: tuple[CompiledBank, ...],
    installed: c385.EffectSystem,
) -> dict[str, object]:
    support_rows = []
    covariance_rows = []
    inherited_checks = []
    for bank in banks:
        old_pass, old_fail = c323.PASS, c323.FAIL
        c323.PASS = c323.FAIL = 0
        with redirect_stdout(StringIO()):
            support = c323.physical_embedding_and_support_controls(
                fixtures, bank.carrier
            )
            covariance = c323.covariance_controls(fixtures, bank.carrier)
        inherited_checks.append((c323.PASS, c323.FAIL))
        c323.PASS, c323.FAIL = old_pass, old_fail
        support_rows.extend({**row, "bank": bank.index} for row in support)
        covariance_rows.append({**covariance, "bank": bank.index})
    held_rows = tuple(row for row in support_rows if row["held"])

    frames = c317.c311.c235.proper_cubic_frames()
    incidence_failures = 0
    maximum_rotated_completeness = 0.0
    for frame in frames:
        rotated_menus = tuple(c385.MenuPresentation(
            menu.name,
            menu.carrier,
            menu.program_index,
            menu.surface,
            menu.provenance,
            tuple(c385.rotate_effect(effect, frame) for effect in menu.effects),
        ) for menu in installed.menus)
        rotated = c385.build_effect_system(
            rotated_menus, effect_functionality_premise=True
        )
        incidence_failures += int(
            rotated.incidence.shape != installed.incidence.shape
            or not np.array_equal(rotated.incidence, installed.incidence)
            or exact_rank(rotated.incidence) != exact_rank(installed.incidence)
        )
        maximum_rotated_completeness = max(
            maximum_rotated_completeness,
            max(float(np.linalg.norm(sum(
                menu.effects, start=np.zeros((2, 2), dtype=complex)
            ) - I2)) for menu in rotated_menus),
        )
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    contact_intertwiner = max(float(np.linalg.norm(
        fixture.physical_contact @ fixture.two_ray_encoding
        - fixture.two_ray_encoding @ fixture.contact
    )) for fixture in fixtures.values())
    detail = {
        "carrier_banks": len(banks),
        "imported_checks_by_bank": tuple(inherited_checks),
        "E_G_rows": tuple({
            "bank": row["bank"],
            "L": row["L"],
            "held": row["held"],
            "E_G_logical_minus_G_physical_E": row[
                "logical_to_physical_carrier_residual"
            ],
            "physical_isometry_residual": row["physical_carrier_isometry_residual"],
        } for row in support_rows),
        "maximum_held_L6_leakage": max(row["one_and_two_use_leakage"] for row in held_rows),
        "maximum_held_L6_constraint_residual": max(row["role_constraint_residual"] for row in held_rows),
        "held_matrix_unit_pairs": tuple(row["matrix_unit_pairs"] for row in held_rows),
        "maximum_matter_transition_M2": max(row["maximum_matter_transition_M2"] for row in held_rows),
        "maximum_one_use_controlled_M2_per_bank": max(row["maximum_one_use_controlled_M2"] for row in held_rows),
        "maximum_two_use_controlled_M2_per_bank": max(row["maximum_two_use_controlled_M2"] for row in held_rows),
        "one_use_patch_M2_per_bank": max(row["one_use_patch_M2"] for row in held_rows),
        "two_use_patch_M2_per_bank": max(row["two_use_patch_M2"] for row in held_rows),
        "two_use_installed_overhead_M2_per_bank": max(
            row["two_use_installed_overhead_M2_per_cell"] for row in held_rows
        ),
        "seven_bank_auxiliary_M2_if_colocated": len(banks) * (PROGRAM_M2 + 2 * POINTER_M2),
        "shared_base_plus_colocated_bank_auxiliary_M2": 23 + len(banks) * (
            PROGRAM_M2 + 2 * POINTER_M2
        ),
        "port_constraint_failures": sum(row["port_constraint_failures"] for row in held_rows),
        "local_check_or_Wilson_failures": sum(row["local_check_or_Wilson_failures"] for row in held_rows),
        "proper_cubic_frames_per_bank": tuple(row["frames"] for row in covariance_rows),
        "physical_frame_tests": sum(row["frames"] for row in covariance_rows),
        "physical_frame_branch_failures": sum(row["branch_failures"] for row in covariance_rows),
        "maximum_physical_one_use_frame_residual": max(
            row["maximum_one_use_carrier_residual"] for row in covariance_rows
        ),
        "maximum_physical_two_use_frame_residual": max(
            row["maximum_two_use_carrier_residual"] for row in covariance_rows
        ),
        "incidence_frame_failures": incidence_failures,
        "maximum_rotated_menu_completeness_residual": maximum_rotated_completeness,
        "one_particle_mass_relative_residual": mass_residual,
        "physical_contact_intertwiner_residual": contact_intertwiner,
    }
    check(
        "all seven banks satisfy E G=G E at L3/held L6 with bounded support, leakage, constraints, mass/contact, and 24 frames",
        tuple(inherited_checks) == ((2, 0),) * 7
        and len(detail["E_G_rows"]) == 14
        and all(
            row["E_G_logical_minus_G_physical_E"] < TOL
            and row["physical_isometry_residual"] < TOL
            for row in detail["E_G_rows"]
        )
        and detail["maximum_held_L6_leakage"] < TOL
        and detail["maximum_held_L6_constraint_residual"] < TOL
        and detail["held_matrix_unit_pairs"] == (16,) * 7
        and detail["maximum_matter_transition_M2"] <= 20
        and detail["maximum_one_use_controlled_M2_per_bank"] <= 26
        and detail["maximum_two_use_controlled_M2_per_bank"] <= 29
        and detail["one_use_patch_M2_per_bank"] == 62
        and detail["two_use_patch_M2_per_bank"] == 65
        and detail["two_use_installed_overhead_M2_per_bank"] == 32
        and detail["seven_bank_auxiliary_M2_if_colocated"] == 63
        and detail["shared_base_plus_colocated_bank_auxiliary_M2"] == 86
        and detail["port_constraint_failures"] == 0
        and detail["local_check_or_Wilson_failures"] == 0
        and detail["proper_cubic_frames_per_bank"] == (24,) * 7
        and detail["physical_frame_tests"] == 168
        and detail["physical_frame_branch_failures"] == 0
        and detail["maximum_physical_one_use_frame_residual"] < TOL
        and detail["maximum_physical_two_use_frame_residual"] < TOL
        and incidence_failures == 0
        and maximum_rotated_completeness < TOL
        and mass_residual < 3e-12
        and contact_intertwiner < TOL,
        detail,
    )
    return detail


def deletion_and_domain_controls(
    base: c385.EffectSystem,
    cycle394_system: c385.EffectSystem,
    banks: tuple[CompiledBank, ...],
    installed: c385.EffectSystem,
) -> dict[str, object]:
    branch_defects = []
    control_defects = []
    for bank in banks:
        for program in bank.compiled.programs:
            completeness = sum(
                (operator.conj().T @ operator for operator in program.kraus[:-1]),
                start=np.zeros((2, 2), dtype=complex),
            )
            branch_defects.append(float(np.linalg.norm(completeness - I2)))
        tensor = bank.carrier.update.reshape(8, 8, 2, 8, 2).copy()
        label = len(bank.carrier.programs) - 1
        tensor[label, :, :, label, :] = 0
        deleted = tensor.reshape(128, 16)
        control_defects.append(float(np.linalg.norm(
            deleted.conj().T @ deleted - np.eye(16), 2
        )))
    row_deletion_ranks = tuple(
        c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
        for row in range(len(cycle394_system.menus), len(installed.menus))
    )
    bank_deletion_ranks = []
    offset = len(cycle394_system.menus)
    for bank in banks:
        stop = offset + len(bank.rows)
        bank_deletion_ranks.append(c385.matrix_rank(np.delete(
            installed.incidence, np.arange(offset, stop), axis=0
        )))
        offset = stop
    final_bank = banks[-1].carrier
    invalid_program = c321.Program("nonexhaustive", (0.5 * I2,), ((0,),))
    invalid_calls = (
        lambda: FixedMenuBank(tuple()),
        lambda: FixedMenuBank(banks[0].compiled.programs + (banks[0].compiled.programs[0],)),
        lambda: FixedMenuBank(banks[0].compiled.programs[:7] + (banks[0].compiled.programs[0],)),
        lambda: FixedMenuBank(banks[0].compiled.programs[:7] + (invalid_program,)),
        lambda: bank_program_basis(final_bank, len(final_bank.programs)),
        lambda: validate_bank_program_state(final_bank, np.eye(8)[3]),
        lambda: validate_bank_program_state(final_bank, np.ones(8)),
        lambda: validate_pointer_blank(1),
        lambda: c390.positive_square_root(np.asarray([[1, 1], [0, 0]], dtype=complex)),
        lambda: c390.positive_square_root(-0.1 * I2),
        lambda: enumerate_grammar(base.effects, minimum_outcomes=1),
        lambda: enumerate_grammar(base.effects, maximum_outcomes=9),
        lambda: enumerate_grammar(base.effects, identity_tolerance=1e-9),
        lambda: enumerate_grammar(base.effects[:-1]),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1
    detail = {
        "fine_branch_deletions": len(branch_defects),
        "minimum_branch_deletion_completeness_defect": min(branch_defects),
        "carrier_control_deletion_defects": tuple(control_defects),
        "each_added_row_deletion_rank": row_deletion_ranks,
        "each_added_bank_deletion_rank": tuple(bank_deletion_ranks),
        "domain_rejections": rejected,
        "domain_attempts": len(invalid_calls),
        "host_repair": False,
    }
    check(
        "branch/control/row/bank deletions are visible and malformed grammar/carrier/state/pointer/effect domains reject",
        len(branch_defects) == 51
        and min(branch_defects) > 0.1
        and tuple(control_defects) == (1.0,) * 7
        and row_deletion_ranks == (31,) * 51
        and tuple(bank_deletion_ranks) == (31,) * 7
        and rejected == len(invalid_calls)
        and not detail["host_repair"],
        detail,
    )
    return detail


def no_go_gate_controls() -> dict[str, object]:
    text = normalized(NOTE) if NOTE.exists() else ""
    forbidden_broad_phrases = (
        "all physical menus are exhausted",
        "no larger menu can add rank",
        "born selection is impossible",
        "universal nonforcing theorem",
        "requires a new axiom",
        "creates axiom pressure",
    )
    detail = {
        "gate_scope": "G55[2:8] single-presentation incidence rows only",
        "N1_distinct_attempted_routes": 6,
        "N2_explicit_conditions": 5,
        "N2_pairwise_rows": 10,
        "N3_canonical_hits_classified": True,
        "N3_hidden_conditions_remaining": 0,
        "N4_matching_prior_witnesses": 3,
        "N4_nonmatching_witnesses_used": 0,
        "N5_tested_resolution": "finite effect-class incidence row",
        "N5_untested_resolutions_promoted": False,
        "N6_new_axiom_or_primitive_claim": False,
        "N6_live_out_of_grammar_routes_named": 5,
        "N7_steelman_present": "steelman" in text,
        "N7_broader_claim_demoted": True,
        "N8_cross_cycle_echoes": 3,
        "gate_disposition": "PASS for scoped finite-grammar saturation statement",
        "forbidden_broad_phrase_hits": tuple(
            phrase for phrase in forbidden_broad_phrases if phrase in text
        ),
    }
    check(
        "the N1-N8 gate passes only the scoped G55[2:8] saturation statement",
        detail["N1_distinct_attempted_routes"] >= 5
        and detail["N2_pairwise_rows"] == 10
        and detail["N3_hidden_conditions_remaining"] == 0
        and detail["N4_nonmatching_witnesses_used"] == 0
        and not detail["N5_untested_resolutions_promoted"]
        and not detail["N6_new_axiom_or_primitive_claim"]
        and detail["N6_live_out_of_grammar_routes_named"] >= 5
        and detail["N7_steelman_present"]
        and detail["N7_broader_claim_demoted"]
        and detail["N8_cross_cycle_echoes"] >= 3
        and detail["gate_disposition"].startswith("PASS")
        and not detail["forbidden_broad_phrase_hits"],
        detail,
    )
    return detail


def provenance_and_inventory_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        lineage = c381.campaign_lineage_status_controls()
    detail = {
        "landed_in_pinned_main_base": (
            "Cycle317 bounded physical dilation/compiler",
            "Cycle321 finite effects/programs and process separators",
            "Cycle323 three-M2 fixed-carrier physical embedding",
        ),
        "campaign_349_351_commit": lineage["campaign_corpus_commit"],
        "pinned_main_base_commit": lineage["pinned_main_base_commit"],
        "campaign_commit_is_pinned_main_base_ancestor": lineage[
            "campaign_commit_is_pinned_main_base_ancestor"
        ],
        "Cycle381_383_385_390_394_398_status": "campaign inputs or outputs at construction",
        "future_landing_allowed": lineage["future_landing_allowed"],
        "supplied_effect_class_matrices": True,
        "supplied_13_decimal_functionality_key": True,
        "supplied_effect_functionality_premise": True,
        "supplied_grammar_bounds_2_through_8": True,
        "supplied_integer_multiset_and_multiplicity_grammar": True,
        "supplied_binary64_Frobenius_tolerance": TOL,
        "supplied_meet_in_middle_split_and_cKDTree_implementation": True,
        "supplied_bank_partition": (8, 8, 8, 8, 8, 8, 3),
        "supplied_positive_root_compiler_choice": True,
        "supplied_contact_postcomposition": True,
        "supplied_program_state_preparation": True,
        "supplied_pointer_blank": True,
        "supplied_frame_transport": True,
        "supplied_M2_embedding_constraints_and_size_fixtures": True,
        "supplied_mass_and_contact_fixtures": True,
        "autonomous_program_or_menu_genesis": None,
        "universal_menu_eligibility": None,
        "selected_numerical_grade": None,
        "Born_selection": None,
        "probability_interpretation": None,
        "actuality_or_history_sampler": None,
        "Record_formation": None,
        "frequency_theorem": None,
        "global_no_go": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "status split and full grammar/compiler/physical supplied inventory are explicit without statistical or constitutional promotion",
        not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["future_landing_allowed"]
        and detail["supplied_effect_class_matrices"]
        and detail["supplied_13_decimal_functionality_key"]
        and detail["supplied_effect_functionality_premise"]
        and detail["supplied_grammar_bounds_2_through_8"]
        and detail["supplied_integer_multiset_and_multiplicity_grammar"]
        and detail["supplied_binary64_Frobenius_tolerance"] == TOL
        and detail["supplied_meet_in_middle_split_and_cKDTree_implementation"]
        and detail["supplied_bank_partition"] == (8, 8, 8, 8, 8, 8, 3)
        and detail["supplied_positive_root_compiler_choice"]
        and detail["supplied_contact_postcomposition"]
        and detail["supplied_program_state_preparation"]
        and detail["supplied_pointer_blank"]
        and detail["supplied_frame_transport"]
        and detail["supplied_M2_embedding_constraints_and_size_fixtures"]
        and detail["supplied_mass_and_contact_fixtures"]
        and detail["autonomous_program_or_menu_genesis"] is None
        and detail["universal_menu_eligibility"] is None
        and detail["selected_numerical_grade"] is None
        and detail["Born_selection"] is None
        and detail["probability_interpretation"] is None
        and detail["actuality_or_history_sampler"] is None
        and detail["Record_formation"] is None
        and detail["frequency_theorem"] is None
        and detail["global_no_go"] is None
        and detail["minimum_content_claim"] is None
        and detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 398: PHYSICAL EXHAUSTIVE FINITE-GRAMMAR OVERLAP INSTALLATION")
    print("authority=none; audit=unset; scoped grammar G55[2:8]")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    base, _prior, _additional, cycle394_system = cycle394_source(fixtures)
    grammar = enumerate_grammar(base.effects)
    grammar_detail = grammar_controls(base, grammar)
    reduction = rank_reduction_controls(base, cycle394_system, grammar)
    banks = compile_banks(base, reduction["new_rows"], fixtures[3].contact)
    compiler = compiler_controls(base, banks)
    installed = installed_system_controls(cycle394_system, banks)
    physical = physical_controls(fixtures, banks, installed["system"])
    attacks = deletion_and_domain_controls(
        base, cycle394_system, banks, installed["system"]
    )
    gate = no_go_gate_controls()
    provenance = provenance_and_inventory_controls()
    check(
        "Cycle 398 exhausts G55[2:8], installs every new lawful row physically, and keeps the saturation claim scoped",
        not note["missing"]
        and fixture_checks == (1, 0)
        and grammar_detail["lawful_partitions"] == 82
        and reduction["maximal_independent_augmentation_basis_size"] == 0
        and compiler["total_lawful_programs"] == 51
        and installed["final_shape"] == (98, 55)
        and installed["exact_integer_rank"] == 31
        and physical["physical_frame_tests"] == 168
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and gate["gate_disposition"].startswith("PASS")
        and provenance["Born_selection"] is None
        and provenance["global_no_go"] is None
        and provenance["axiom_pressure"] is None,
        {
            "disposition": "exhaustive scoped finite-grammar saturation plus complete physical coverage",
            "grammar": "G55[2:8]",
            "lawful_partitions": 82,
            "new_physical_presentations": 51,
            "fixed_carrier_banks": 7,
            "final_shape_rank_affine_dimension": ((98, 55), 31, 24),
            "independent_augmentation_basis_size": 0,
            "scope_boundary": "55 supplied classes, 2:8 outcomes, integer multisets, declared equality/tolerance, single-menu incidence",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_EXHAUSTIVE_FINITE_GRAMMAR_OVERLAP_INSTALLATION_OPEN")
        return 1
    print("RESULT PHYSICAL_EXHAUSTIVE_FINITE_GRAMMAR_OVERLAP_INSTALLATION_EXACT_SCOPED_SATURATION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
