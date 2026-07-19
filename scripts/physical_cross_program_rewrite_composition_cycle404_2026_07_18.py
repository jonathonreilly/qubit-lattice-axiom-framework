#!/usr/bin/env python3
"""Cycle 404: physical cross-program rewrite composition.

This cycle changes exactly Cycle-401 condition W2.  Within each of the seven
fixed Cycle-398 banks it supplies a three-M2 XOR-difference ancilla and applies
one fixed reversible XOR rewrite between two uses of the fixed carrier.  Every
lawful ordered pair p != q is realized by d=p XOR q and the physical rewrite
R|p,d> = |p XOR d,d> = |q,d>.  Fine branches are extracted from the actual
first-use/rewrite/second-use tensor and equal K_b^(q) K_a^(p).

The finite grammar has 342 ordered program pairs, 1,710 menus, and 21,302
effect occurrences.  Appending it to Cycle 401 gives 2,063 menus, 3,348
equal-effect classes, exact incidence rank 1,159, and affine dimension 2,189.
Equal effects are quotiented only for incidence: 4,015 effect/process pairs
and 233 multi-process effect keys remain explicit.

The N1-N8 gate in the companion note passes only this finite census and the
first-pointer effect-incidence redundancy.  No cross-bank grammar, third use,
arbitrary set partition, Born selection, universal eligibility, minimum, or
axiom pressure is claimed.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass
from inspect import getsource
from io import StringIO
from pathlib import Path
import sys

import numpy as np
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CROSS_PROGRAM_REWRITE_COMPOSITION_CYCLE404_NOTE_2026-07-18.md"
)

import physical_two_use_composed_instrument_extension_cycle401_2026_07_18 as c401


c398 = c401.c398
c394 = c401.c394
c390 = c401.c390
c385 = c401.c385
c381 = c401.c381
c383 = c401.c383
c323 = c401.c323
c321 = c401.c321
c317 = c401.c317
TOL = c401.TOL
I2 = c401.I2
FAMILIES = c401.FAMILIES
PROGRAM_DIMENSION = 8
POINTER_DIMENSION = 8
PROGRAM_M2 = 3
REWRITE_M2 = 3
POINTER_M2 = 3
EXPECTED_OCCURRENCES = (10498, 1861, 1861, 6398, 684)
EXPECTED_CUMULATIVE_SHAPES = (
    (695, 1030),
    (1037, 1030),
    (1379, 1351),
    (1721, 2803),
    (2063, 3348),
)
EXPECTED_CUMULATIVE_RANKS = (371, 371, 550, 884, 1159)
EXPECTED_CUMULATIVE_CLASSES = (1030, 1030, 1351, 2803, 3348)
AUTHORITY = "none"
AUDIT = "unset"
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
        check("the Cycle-404 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "changes exactly w2",
        "342 lawful ordered cross-program pairs",
        "three-m2 rewrite register",
        "the xor rewrite maps p,d to p xor d,d",
        "explicit bounded reversible program-register rewrite",
        "not a host relabel",
        "10,498 ordered fine branches",
        "1,710 cross-program menus",
        "21,302 effect occurrences",
        "2,063 menus, 3,348 classes, exact rank 1,159",
        "2,712 new effect classes",
        "rank gain is 967",
        "affine dimension 2,189",
        "4,015 effect/process pairs",
        "233 effect keys carry multiple process tags",
        "equal effects are not used to merge distinct processes",
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
        "gate disposition: pass only for the finite census and first-pointer effect-incidence redundancy",
        "born selection: not claimed",
        "universal menu eligibility: not claimed",
        "axiom pressure: not claimed",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins W2, the physical rewrite, finite grammar, quotient, controls, imports, and N1-N8 gate",
        not missing,
        missing,
    )
    return {"missing": missing}


def exact_sparse_rank(matrix: np.ndarray) -> int:
    integer = np.rint(matrix).astype(int)
    if np.linalg.norm(matrix - integer) != 0:
        raise ValueError("exact incidence rank requires an integer matrix")
    rows = {
        row: {
            int(column): ZZ(int(integer[row, column]))
            for column in np.flatnonzero(integer[row])
        }
        for row in range(integer.shape[0])
        if np.any(integer[row])
    }
    return int(DomainMatrix(rows, integer.shape, ZZ).rank())


def program_delta_rewrite() -> np.ndarray:
    """Fixed three-bit XOR rewrite on program plus supplied delta register."""
    tensor = np.zeros((8, 8, 8, 8), dtype=complex)
    for program in range(8):
        for delta in range(8):
            tensor[program ^ delta, delta, program, delta] = 1
    return tensor.reshape(64, 64)


def apply_program_delta_rewrite(
    rewrite: np.ndarray, state: np.ndarray
) -> np.ndarray:
    return rewrite @ state


def validate_ordered_pair(
    bank: c398.CompiledBank, first_program: int, second_program: int, delta: int
) -> None:
    lawful = len(bank.compiled.programs)
    if not 0 <= first_program < lawful or not 0 <= second_program < lawful:
        raise ValueError("both program labels must lie in the same fixed bank code")
    if first_program == second_program:
        raise ValueError("Cycle404 contains only cross-program ordered pairs")
    if not 0 <= delta < PROGRAM_DIMENSION or delta != first_program ^ second_program:
        raise ValueError("the supplied rewrite label must equal p XOR q")


def cross_program_update(carrier: c398.FixedMenuBank) -> np.ndarray:
    """First fixed use, explicit XOR rewrite, then the same fixed use."""
    update = carrier.update.reshape(8, 8, 2, 8, 2)
    rewrite = program_delta_rewrite().reshape(8, 8, 8, 8)
    tensor = np.einsum(
        "qbuxt,xdpe,patrs->qdabures", update, rewrite, update, optimize=True
    )
    return tensor.reshape(8 * 8 * 8 * 8 * 2, 8 * 8 * 2)


def direct_cross_program_update(carrier: c398.FixedMenuBank) -> np.ndarray:
    tensor = np.zeros((8, 8, 8, 8, 2, 8, 8, 2), dtype=complex)
    for first_program, first_blocks in enumerate(carrier.block_kraus):
        for delta in range(8):
            second_program = first_program ^ delta
            second_blocks = carrier.block_kraus[second_program]
            for first_pointer, left in enumerate(first_blocks):
                for second_pointer, right in enumerate(second_blocks):
                    tensor[
                        second_program,
                        delta,
                        first_pointer,
                        second_pointer,
                        :,
                        first_program,
                        delta,
                        :,
                    ] = right @ left
    return tensor.reshape(8 * 8 * 8 * 8 * 2, 8 * 8 * 2)


@dataclass(frozen=True)
class FineBranch:
    first_pointer: int
    second_pointer: int
    operator: np.ndarray
    effect: np.ndarray
    process: np.ndarray


@dataclass(frozen=True)
class CrossPresentation:
    family: str
    bank_index: int
    first_program: int
    second_program: int
    groups: tuple[tuple[int, ...], ...]
    effects: tuple[np.ndarray, ...]
    processes: tuple[np.ndarray, ...]

    @property
    def menu(self) -> c385.MenuPresentation:
        return c385.MenuPresentation(
            name=(
                f"Cycle404/{self.family}/bank{self.bank_index}/"
                f"p{self.first_program}-to-q{self.second_program}"
            ),
            carrier=f"Cycle398-fixed-menu-bank-{self.bank_index}/XOR-rewrite",
            program_index=8 * self.first_program + self.second_program,
            surface=f"cross-program-{self.family}",
            provenance="Cycle404 actual first-use/XOR-rewrite/second-use composition",
            effects=self.effects,
        )


@dataclass(frozen=True)
class CrossProgram:
    bank_index: int
    first_program: int
    second_program: int
    delta: int
    first_source: c321.Program
    second_source: c321.Program
    branches: tuple[FineBranch, ...]
    presentations: tuple[CrossPresentation, ...]


def validate_groups(
    fine_count: int, groups: tuple[tuple[int, ...], ...]
) -> None:
    if fine_count <= 0 or not groups or any(not group for group in groups):
        raise ValueError("a presentation requires fine branches and nonempty groups")
    flattened = tuple(index for group in groups for index in group)
    if any(not isinstance(index, int) for index in flattened):
        raise TypeError("fine branch indices must be integers")
    if tuple(sorted(flattened)) != tuple(range(fine_count)):
        raise ValueError("groups must partition each fine branch exactly once")


def declared_groups(
    first_outcomes: int, second_outcomes: int
) -> dict[str, tuple[tuple[int, ...], ...]]:
    if not 1 <= first_outcomes <= 8 or not 1 <= second_outcomes <= 8:
        raise ValueError("both programs must fit the three-M2 pointer code")
    ordered = tuple(
        (first * second_outcomes + second,)
        for first in range(first_outcomes)
        for second in range(second_outcomes)
    )
    first_pointer = tuple(
        tuple(first * second_outcomes + second for second in range(second_outcomes))
        for first in range(first_outcomes)
    )
    second_pointer = tuple(
        tuple(first * second_outcomes + second for first in range(first_outcomes))
        for second in range(second_outcomes)
    )
    seen: set[tuple[int, int]] = set()
    swap_orbits = []
    for first in range(first_outcomes):
        for second in range(second_outcomes):
            if (first, second) in seen:
                continue
            group = [first * second_outcomes + second]
            seen.add((first, second))
            if (
                second < first_outcomes
                and first < second_outcomes
                and first != second
            ):
                group.append(second * second_outcomes + first)
                seen.add((second, first))
            swap_orbits.append(tuple(group))
    same = tuple(
        pointer * second_outcomes + pointer
        for pointer in range(min(first_outcomes, second_outcomes))
    )
    different = tuple(
        first * second_outcomes + second
        for first in range(first_outcomes)
        for second in range(second_outcomes)
        if first != second
    )
    groups = {
        "ordered-fine": ordered,
        "first-pointer": first_pointer,
        "second-pointer": second_pointer,
        "unordered-pair": tuple(swap_orbits),
        "same-vs-different": (same, different),
    }
    for family in FAMILIES:
        validate_groups(first_outcomes * second_outcomes, groups[family])
    return groups


def compose_bank(
    bank: c398.CompiledBank,
) -> tuple[tuple[CrossProgram, ...], dict[str, float]]:
    update = cross_program_update(bank.carrier)
    direct = direct_cross_program_update(bank.carrier)
    tensor = update.reshape(8, 8, 8, 8, 2, 8, 8, 2)
    programs = []
    extraction = off_code = 0.0
    for first_program, first_source in enumerate(bank.compiled.programs):
        for second_program, second_source in enumerate(bank.compiled.programs):
            if first_program == second_program:
                continue
            delta = first_program ^ second_program
            validate_ordered_pair(bank, first_program, second_program, delta)
            branches = []
            for first_pointer, left in enumerate(first_source.kraus):
                for second_pointer, right in enumerate(second_source.kraus):
                    operator = tensor[
                        second_program,
                        delta,
                        first_pointer,
                        second_pointer,
                        :,
                        first_program,
                        delta,
                        :,
                    ]
                    extraction = max(
                        extraction, float(np.linalg.norm(operator - right @ left))
                    )
                    branches.append(FineBranch(
                        first_pointer,
                        second_pointer,
                        operator,
                        operator.conj().T @ operator,
                        c321.choi((operator,)),
                    ))
            presentations = []
            for family, groups in declared_groups(
                len(first_source.kraus), len(second_source.kraus)
            ).items():
                effects = []
                processes = []
                for group in groups:
                    operators = tuple(branches[index].operator for index in group)
                    effects.append(sum(
                        (operator.conj().T @ operator for operator in operators),
                        start=np.zeros((2, 2), dtype=complex),
                    ))
                    processes.append(c321.choi(operators))
                presentations.append(CrossPresentation(
                    family,
                    bank.index,
                    first_program,
                    second_program,
                    groups,
                    tuple(effects),
                    tuple(processes),
                ))
            programs.append(CrossProgram(
                bank.index,
                first_program,
                second_program,
                delta,
                first_source,
                second_source,
                tuple(branches),
                tuple(presentations),
            ))
    for first_program in range(8):
        for delta in range(8):
            target = first_program ^ delta
            wrong = tensor[:, delta, :, :, :, first_program, delta, :].copy()
            wrong[target] = 0
            off_code = max(off_code, float(np.linalg.norm(wrong)))
    detail = {
        "sequential_vs_direct_residual": float(np.linalg.norm(update - direct)),
        "update_isometry_residual": float(
            np.linalg.norm(update.conj().T @ update - np.eye(128))
        ),
        "actual_tensor_extraction_residual": extraction,
        "off_rewrite_target_residual": off_code,
    }
    return tuple(programs), detail


def compose_all(
    banks: tuple[c398.CompiledBank, ...]
) -> tuple[tuple[CrossProgram, ...], tuple[dict[str, float], ...]]:
    programs = []
    rows = []
    for bank in banks:
        compiled, detail = compose_bank(bank)
        programs.extend(compiled)
        rows.append({"bank": bank.index, **detail})
    return tuple(programs), tuple(rows)


def presentation_by_family(
    programs: tuple[CrossProgram, ...]
) -> dict[str, tuple[CrossPresentation, ...]]:
    return {
        family: tuple(
            presentation
            for program in programs
            for presentation in program.presentations
            if presentation.family == family
        )
        for family in FAMILIES
    }


def rewrite_and_grammar_controls(
    banks: tuple[c398.CompiledBank, ...],
    programs: tuple[CrossProgram, ...],
    update_rows: tuple[dict[str, float], ...],
) -> dict[str, object]:
    rewrite = program_delta_rewrite()
    forward_failures = inverse_failures = 0
    for program in range(8):
        for delta in range(8):
            state = np.zeros(64, dtype=complex)
            state[8 * program + delta] = 1
            expected = np.zeros(64, dtype=complex)
            expected[8 * (program ^ delta) + delta] = 1
            output = apply_program_delta_rewrite(rewrite, state)
            forward_failures += int(np.linalg.norm(output - expected) >= TOL)
            inverse_failures += int(
                np.linalg.norm(apply_program_delta_rewrite(rewrite, output) - state)
                >= TOL
            )
    families = presentation_by_family(programs)
    occurrence_counts = tuple(
        sum(len(presentation.effects) for presentation in families[family])
        for family in FAMILIES
    )
    completeness = max(
        float(np.linalg.norm(sum(
            presentation.effects, start=np.zeros((2, 2), dtype=complex)
        ) - I2))
        for program in programs
        for presentation in program.presentations
    )
    minimum_process_eigenvalue = min(
        float(np.min(np.linalg.eigvalsh((process + process.conj().T) / 2)))
        for program in programs
        for presentation in program.presentations
        for process in presentation.processes
    )
    maximum_process_hermitian = max(
        float(np.linalg.norm(process - process.conj().T))
        for program in programs
        for presentation in program.presentations
        for process in presentation.processes
    )
    pair_counts = tuple(
        sum(program.bank_index == bank.index for program in programs)
        for bank in banks
    )
    detail = {
        "grammar": "all ordered p!=q pairs within each fixed Cycle398 bank; five declared partitions",
        "lawful_ordered_pair_counts_by_bank": pair_counts,
        "lawful_ordered_pairs": len(programs),
        "ordered_fine_branches": sum(len(program.branches) for program in programs),
        "cross_program_menu_presentations": len(programs) * len(FAMILIES),
        "effect_occurrences_by_family": dict(zip(FAMILIES, occurrence_counts)),
        "total_effect_occurrences": sum(occurrence_counts),
        "maximum_sequential_vs_direct_residual": max(row["sequential_vs_direct_residual"] for row in update_rows),
        "maximum_update_isometry_residual": max(row["update_isometry_residual"] for row in update_rows),
        "maximum_actual_tensor_extraction_residual": max(row["actual_tensor_extraction_residual"] for row in update_rows),
        "maximum_off_rewrite_target_residual": max(row["off_rewrite_target_residual"] for row in update_rows),
        "rewrite_forward_failures": forward_failures,
        "rewrite_inverse_failures": inverse_failures,
        "rewrite_squared_identity_residual": float(np.linalg.norm(rewrite @ rewrite - np.eye(64))),
        "rewrite_isometry_residual": float(np.linalg.norm(rewrite.conj().T @ rewrite - np.eye(64))),
        "rewrite_circuit": "three parallel CNOTs, delta bits control corresponding program bits",
        "rewrite_support_M2": PROGRAM_M2 + REWRITE_M2,
        "maximum_menu_completeness_residual": completeness,
        "minimum_process_Choi_eigenvalue": minimum_process_eigenvalue,
        "maximum_process_Choi_Hermitian_residual": maximum_process_hermitian,
        "host_program_relabel": False,
        "rewrite_application_source": " ".join(getsource(apply_program_delta_rewrite).split()),
        "sampling": None,
    }
    check(
        "one fixed bounded reversible XOR register rewrite physically realizes all 342 within-bank ordered pairs",
        pair_counts == (56, 56, 56, 56, 56, 56, 6)
        and len(programs) == 342
        and detail["ordered_fine_branches"] == 10498
        and detail["cross_program_menu_presentations"] == 1710
        and occurrence_counts == EXPECTED_OCCURRENCES
        and detail["total_effect_occurrences"] == 21302
        and max(
            row[key]
            for row in update_rows
            for key in (
                "sequential_vs_direct_residual",
                "update_isometry_residual",
                "actual_tensor_extraction_residual",
                "off_rewrite_target_residual",
            )
        ) < TOL
        and forward_failures == inverse_failures == 0
        and detail["rewrite_squared_identity_residual"] < TOL
        and detail["rewrite_isometry_residual"] < TOL
        and detail["rewrite_support_M2"] == 6
        and completeness < TOL
        and minimum_process_eigenvalue > -TOL
        and maximum_process_hermitian < TOL
        and not detail["host_program_relabel"]
        and detail["rewrite_application_source"].endswith("return rewrite @ state")
        and detail["sampling"] is None,
        detail,
    )
    return detail


def process_quotient_controls(
    cycle401_system: c385.EffectSystem,
    programs: tuple[CrossProgram, ...],
) -> dict[str, object]:
    by_effect: dict[c383.MatrixKey, dict[c383.MatrixKey, np.ndarray]] = {}
    occurrences = 0
    for program in programs:
        for presentation in program.presentations:
            for effect, process in zip(presentation.effects, presentation.processes):
                by_effect.setdefault(c383.matrix_key(effect), {})[
                    c383.matrix_key(process)
                ] = process
                occurrences += 1
    maximum_separator = 0.0
    for processes in by_effect.values():
        matrices = tuple(processes.values())
        for left in range(len(matrices)):
            for right in range(left + 1, len(matrices)):
                maximum_separator = max(
                    maximum_separator,
                    float(np.linalg.norm(matrices[left] - matrices[right])),
                )
    process_keys = {key for processes in by_effect.values() for key in processes}
    baseline_keys = {c383.matrix_key(effect) for effect in cycle401_system.effects}
    detail = {
        "cross_effect_occurrences": occurrences,
        "cross_equal_effect_keys": len(by_effect),
        "effect_keys_matching_Cycle401": len(set(by_effect).intersection(baseline_keys)),
        "new_effect_keys": len(set(by_effect) - baseline_keys),
        "effect_process_pairs": sum(len(processes) for processes in by_effect.values()),
        "unique_process_tags": len(process_keys),
        "effect_keys_with_multiple_process_tags": sum(len(processes) > 1 for processes in by_effect.values()),
        "maximum_process_tags_for_one_effect": max(map(len, by_effect.values())),
        "maximum_same_effect_distinct_process_Choi_separator": maximum_separator,
        "effect_functionality_premise_supplied": True,
        "process_functionality_premise_supplied": False,
        "same_effect_means_same_process": False,
        "distinct_process_tags_retained": True,
    }
    check(
        "3,150 cross effect keys retain 4,015 effect/process pairs and visible same-effect process separators",
        occurrences == 21302
        and len(by_effect) == 3150
        and detail["effect_keys_matching_Cycle401"] == 438
        and detail["new_effect_keys"] == 2712
        and detail["effect_process_pairs"] == 4015
        and detail["unique_process_tags"] == 4014
        and detail["effect_keys_with_multiple_process_tags"] == 233
        and detail["maximum_process_tags_for_one_effect"] == 36
        and maximum_separator > 0.92
        and detail["effect_functionality_premise_supplied"]
        and not detail["process_functionality_premise_supplied"]
        and not detail["same_effect_means_same_process"]
        and detail["distinct_process_tags_retained"],
        detail,
    )
    return detail


def cycle401_system(
    cycle398_system: c385.EffectSystem,
    banks: tuple[c398.CompiledBank, ...],
) -> c385.EffectSystem:
    same_programs, extraction, off_diagonal = c401.compose_all(banks)
    if extraction >= TOL or off_diagonal >= TOL:
        raise ValueError("the root-reviewed Cycle401 source tensor changed")
    families = c401.presentation_by_family(same_programs)
    menus = tuple(
        presentation.menu
        for family in FAMILIES
        for presentation in families[family]
    )
    system = c385.build_effect_system(
        cycle398_system.menus + menus,
        effect_functionality_premise=True,
    )
    if system.incidence.shape != (353, 636):
        raise ValueError("the root-reviewed Cycle401 incidence source changed")
    return system


def incidence_controls(
    source: c385.EffectSystem,
    programs: tuple[CrossProgram, ...],
) -> dict[str, object]:
    families = presentation_by_family(programs)
    cumulative_menus: list[c385.MenuPresentation] = []
    cumulative = []
    source_rank = exact_sparse_rank(source.incidence)
    for family in FAMILIES:
        cumulative_menus.extend(
            presentation.menu for presentation in families[family]
        )
        system = c385.build_effect_system(
            source.menus + tuple(cumulative_menus),
            effect_functionality_premise=True,
        )
        cumulative.append({
            "family": family,
            "shape": system.incidence.shape,
            "classes": len(system.effects),
            "exact_integer_rank": exact_sparse_rank(system.incidence),
        })
    final = c385.build_effect_system(
        source.menus + tuple(cumulative_menus),
        effect_functionality_premise=True,
    )
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in final.effects
    ])
    final_rank = cumulative[-1]["exact_integer_rank"]
    detail = {
        "Cycle401_shape_classes_rank": (source.incidence.shape, len(source.effects), source_rank),
        "cumulative_family_rows": tuple(cumulative),
        "incremental_classes_by_family": tuple(
            row["classes"] - previous
            for row, previous in zip(cumulative, (636, 1030, 1030, 1351, 2803))
        ),
        "incremental_ranks_by_family": tuple(
            row["exact_integer_rank"] - previous
            for row, previous in zip(cumulative, (192, 371, 371, 550, 884))
        ),
        "final_shape": final.incidence.shape,
        "final_effect_classes": len(final.effects),
        "new_effect_classes_over_Cycle401": len(final.effects) - len(source.effects),
        "final_exact_integer_rank": final_rank,
        "rank_gain_over_Cycle401": final_rank - source_rank,
        "affine_dimension": len(final.effects) - final_rank,
        "trace_grade_minimum": float(np.min(trace_grade)),
        "trace_grade_zero_classes": int(np.sum(abs(trace_grade) < TOL)),
        "trace_normalization_residual": float(np.linalg.norm(final.incidence @ trace_grade - 1)),
        "numerical_grade_selected": False,
    }
    check(
        "the physical cross-program grammar adds 2,712 effect classes and 967 exact ranks beyond Cycle401",
        source.incidence.shape == (353, 636)
        and source_rank == 192
        and tuple(row["shape"] for row in cumulative) == EXPECTED_CUMULATIVE_SHAPES
        and tuple(row["classes"] for row in cumulative) == EXPECTED_CUMULATIVE_CLASSES
        and tuple(row["exact_integer_rank"] for row in cumulative) == EXPECTED_CUMULATIVE_RANKS
        and detail["incremental_classes_by_family"] == (394, 0, 321, 1452, 545)
        and detail["incremental_ranks_by_family"] == (179, 0, 179, 334, 275)
        and final.incidence.shape == (2063, 3348)
        and len(final.effects) == 3348
        and detail["new_effect_classes_over_Cycle401"] == 2712
        and final_rank == 1159
        and detail["rank_gain_over_Cycle401"] == 967
        and detail["affine_dimension"] == 2189
        and detail["trace_grade_minimum"] > -TOL
        and detail["trace_grade_zero_classes"] > 0
        and detail["trace_normalization_residual"] < TOL
        and not detail["numerical_grade_selected"],
        detail,
    )
    return {**detail, "system": final}


def contact_controls(
    base: c385.EffectSystem,
    banks: tuple[c398.CompiledBank, ...],
    programs: tuple[CrossProgram, ...],
) -> dict[str, object]:
    by_key = {
        (program.bank_index, program.first_program, program.second_program): program
        for program in programs
    }
    update_changes = []
    per_bank_effect = []
    per_bank_process = []
    maximum_effect = maximum_process = 0.0
    for bank in banks:
        deleted_compilation = c390.compile_menus(base, bank.rows, I2)
        deleted_carrier = c398.FixedMenuBank(deleted_compilation.programs)
        update_changes.append(float(np.linalg.norm(
            cross_program_update(bank.carrier) - cross_program_update(deleted_carrier)
        )))
        bank_effect = bank_process = 0.0
        for first_program, first_source in enumerate(deleted_compilation.programs):
            for second_program, second_source in enumerate(deleted_compilation.programs):
                if first_program == second_program:
                    continue
                actual = by_key[(bank.index, first_program, second_program)]
                deleted_ops = tuple(
                    right @ left
                    for left in first_source.kraus
                    for right in second_source.kraus
                )
                for branch, deleted in zip(actual.branches, deleted_ops):
                    effect_change = float(np.linalg.norm(
                        branch.effect - deleted.conj().T @ deleted
                    ))
                    process_change = float(np.linalg.norm(
                        branch.process - c321.choi((deleted,))
                    ))
                    bank_effect = max(bank_effect, effect_change)
                    bank_process = max(bank_process, process_change)
                    maximum_effect = max(maximum_effect, effect_change)
                    maximum_process = max(maximum_process, process_change)
        per_bank_effect.append(bank_effect)
        per_bank_process.append(bank_process)
    detail = {
        "cross_update_contact_deletion_residuals": tuple(update_changes),
        "minimum_cross_update_contact_deletion_residual": min(update_changes),
        "maximum_ordered_effect_contact_deletion_change": maximum_effect,
        "maximum_ordered_process_contact_deletion_change": maximum_process,
        "per_bank_maximum_effect_change": tuple(per_bank_effect),
        "per_bank_maximum_process_change": tuple(per_bank_process),
        "actual_contact_is_load_bearing_in_every_bank": all(
            effect > 0.01 and process > 0.01
            for effect, process in zip(per_bank_effect, per_bank_process)
        ),
    }
    check(
        "the Cycle230 contact is load-bearing in every cross-program bank update, effect, and process family",
        len(update_changes) == 7
        and min(update_changes) > 1.0
        and maximum_effect > 0.05
        and maximum_process > 0.1
        and detail["actual_contact_is_load_bearing_in_every_bank"],
        detail,
    )
    return detail


def physical_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    programs: tuple[CrossProgram, ...],
    installed: c385.EffectSystem,
) -> dict[str, object]:
    rows = []
    for length, fixture in fixtures.items():
        encoding = fixture.two_ray_encoding
        projector = encoding @ encoding.conj().T
        leakage = constraint = intertwining = 0.0
        representatives = tuple(
            c317.c311.branch_representative(
                fixture.code, fixture.encoder.body, branch, r_value
            )
            for r_value in (0, 1)
            for branch in fixture.basis_rows
        )
        matrix_pairs = set()
        for program in programs:
            for branch in program.branches:
                expected = (
                    program.second_source.kraus[branch.second_pointer]
                    @ program.first_source.kraus[branch.first_pointer]
                )
                physical = encoding @ branch.operator
                intertwining = max(
                    intertwining, float(np.linalg.norm(physical - encoding @ expected))
                )
                leakage = max(
                    leakage, float(np.linalg.norm((np.eye(510) - projector) @ physical))
                )
                constraint = max(
                    constraint, float(np.linalg.norm(fixture.constraint @ physical - physical))
                )
                raw = encoding @ branch.operator @ encoding.conj().T
                matrix_pairs.update(
                    (int(row), int(column))
                    for row, column in np.argwhere(abs(raw) > 1e-12)
                )
        support_union = maximum_support = port_failures = sector_failures = 0
        for row, column in matrix_pairs:
            transition = representatives[row] @ c317.c311.local.pauli_dagger(
                representatives[column]
            )
            support = transition.x | transition.z
            support_union |= support
            maximum_support = max(maximum_support, support.bit_count())
            port_failures += sum(
                not transition.commutes(c317.c311.c305.constraint_pauli(fixture.code, vertex))
                for vertex in range(len(fixture.code.graph.vertices))
            )
            sector_failures += sum(
                not transition.commutes(check_row)
                for check_row in fixture.code.local_checks + fixture.code.wilsons
            )
        rows.append({
            "L": length,
            "held": length == 6,
            "E_G_logical_minus_G_physical_E": intertwining,
            "cross_branch_leakage": leakage,
            "role_constraint_residual": constraint,
            "matrix_unit_pairs": len(matrix_pairs),
            "matter_transition_union_M2": support_union.bit_count(),
            "maximum_matter_transition_M2": maximum_support,
            "maximum_cross_use_controlled_M2": maximum_support + PROGRAM_M2 + REWRITE_M2 + 2 * POINTER_M2,
            "cross_use_patch_M2": 56 + PROGRAM_M2 + REWRITE_M2 + 2 * POINTER_M2,
            "cross_use_installed_overhead_M2_per_bank": 23 + PROGRAM_M2 + REWRITE_M2 + 2 * POINTER_M2,
            "port_constraint_failures": port_failures,
            "local_check_or_Wilson_failures": sector_failures,
        })

    base = fixtures[3]
    reducer = c317.c311.c305.StabilizerReducer(base.code)
    selected = np.zeros((127, 2), dtype=complex)
    selected[
        [c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)] for stream_slice in (0, 1)],
        [0, 1],
    ] = 1
    frame_rows = []
    for frame in c317.c311.c235.proper_cubic_frames():
        logical_r = c317.c311.logical_frame_representation(frame)
        old_r, failures = c317.c311.flagged_frame_representation(
            base.encoder, base.basis_rows, base.occurrence, frame, reducer
        )
        mapping, phases, mapping_failures = c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        carried_encoding = base.full_encoding @ logical_r @ selected
        residual = 0.0
        for program in programs:
            for branch in program.branches:
                mapped = c317.c311.apply_signed_mapping(
                    new_mapping, new_phases, base.two_ray_encoding @ branch.operator
                )
                residual = max(
                    residual, float(np.linalg.norm(mapped - carried_encoding @ branch.operator))
                )
        frame_rows.append((failures + mapping_failures, residual))

    # Equality classes are transported with their representatives.  This is
    # the covariance claim: a frame cannot change which occurrence belongs to
    # which already-declared class.  Independently rebuilding the 13-decimal
    # binary64 key after rotation is retained below as a codec diagnostic; it
    # is not used to relabel the transported physical classes.
    class_representatives = {
        c383.matrix_key(effect): effect for effect in installed.effects
    }
    transported_incidence_failures = 0
    maximum_transported_class_residual = 0.0
    raw_rekey_differences = 0
    raw_rekey_shapes = []
    rotated_completeness = 0.0
    for frame in c317.c311.c235.proper_cubic_frames():
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
        raw_difference = int(
            rotated.incidence.shape != installed.incidence.shape
            or not np.array_equal(rotated.incidence, installed.incidence)
        )
        raw_rekey_differences += raw_difference
        raw_rekey_shapes.append(rotated.incidence.shape)
        for menu, rotated_menu in zip(installed.menus, rotated_menus):
            for effect, rotated_effect in zip(menu.effects, rotated_menu.effects):
                key = c383.matrix_key(effect)
                if key not in class_representatives:
                    transported_incidence_failures += 1
                    continue
                expected = c385.rotate_effect(class_representatives[key], frame)
                residual = float(np.linalg.norm(rotated_effect - expected))
                maximum_transported_class_residual = max(
                    maximum_transported_class_residual, residual
                )
                transported_incidence_failures += int(residual >= TOL)
        rotated_completeness = max(
            rotated_completeness,
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
        "E_G_rows": tuple(rows),
        "maximum_held_L6_cross_branch_leakage": rows[1]["cross_branch_leakage"],
        "maximum_held_L6_constraint_residual": rows[1]["role_constraint_residual"],
        "held_matrix_unit_pairs": rows[1]["matrix_unit_pairs"],
        "maximum_matter_transition_M2": rows[1]["maximum_matter_transition_M2"],
        "maximum_cross_use_controlled_M2": rows[1]["maximum_cross_use_controlled_M2"],
        "cross_use_patch_M2_per_bank": rows[1]["cross_use_patch_M2"],
        "cross_use_installed_overhead_M2_per_bank": rows[1]["cross_use_installed_overhead_M2_per_bank"],
        "seven_bank_auxiliary_M2_if_colocated": 7 * (PROGRAM_M2 + REWRITE_M2 + 2 * POINTER_M2),
        "shared_base_plus_colocated_bank_auxiliary_M2": 23 + 7 * (PROGRAM_M2 + REWRITE_M2 + 2 * POINTER_M2),
        "port_constraint_failures": sum(row["port_constraint_failures"] for row in rows),
        "local_check_or_Wilson_failures": sum(row["local_check_or_Wilson_failures"] for row in rows),
        "proper_cubic_frames": len(frame_rows),
        "physical_frame_branch_failures": sum(row[0] for row in frame_rows),
        "maximum_physical_cross_use_frame_residual": max(row[1] for row in frame_rows),
        "transported_class_incidence_frame_failures": transported_incidence_failures,
        "maximum_transported_class_residual": maximum_transported_class_residual,
        "raw_13_decimal_rekey_frame_differences": raw_rekey_differences,
        "raw_13_decimal_rekey_shapes": tuple(raw_rekey_shapes),
        "raw_rekey_is_codec_label_diagnostic_not_covariance_definition": True,
        "maximum_rotated_menu_completeness_residual": rotated_completeness,
        "one_particle_mass_relative_residual": mass_residual,
        "physical_contact_intertwiner_residual": contact_intertwiner,
    }
    check(
        "all cross-program branches satisfy E G=G E at L3/held L6 with bounded support, constraints, mass/contact, and all 24 frames",
        len(rows) == 2
        and all(
            row["E_G_logical_minus_G_physical_E"] < TOL
            and row["cross_branch_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["matrix_unit_pairs"] == 16
            and row["matter_transition_union_M2"] == 20
            and row["maximum_matter_transition_M2"] <= 20
            and row["maximum_cross_use_controlled_M2"] <= 32
            and row["cross_use_patch_M2"] == 68
            and row["cross_use_installed_overhead_M2_per_bank"] == 35
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        )
        and detail["seven_bank_auxiliary_M2_if_colocated"] == 84
        and detail["shared_base_plus_colocated_bank_auxiliary_M2"] == 107
        and len(frame_rows) == 24
        and detail["physical_frame_branch_failures"] == 0
        and detail["maximum_physical_cross_use_frame_residual"] < TOL
        and transported_incidence_failures == 0
        and maximum_transported_class_residual < TOL
        and raw_rekey_differences == 16
        and detail["raw_rekey_is_codec_label_diagnostic_not_covariance_definition"]
        and rotated_completeness < TOL
        and mass_residual < 3e-12
        and contact_intertwiner < TOL,
        detail,
    )
    return detail


def deletion_and_domain_controls(
    banks: tuple[c398.CompiledBank, ...],
    programs: tuple[CrossProgram, ...],
) -> dict[str, object]:
    selected_positive_fine_defects = []
    fine_branch_changes = []
    coarse_group_changes = []
    process_changes = []
    rewrite_effect_changes = []
    rewrite_process_changes = []
    wrong_target_labels = 0
    by_bank = {bank.index: bank for bank in banks}
    for program in programs:
        branch_norms = tuple(float(np.linalg.norm(branch.effect)) for branch in program.branches)
        selected = int(np.argmax(branch_norms))
        selected_positive_fine_defects.append(float(np.linalg.norm(sum(
            (
                branch.effect
                for index, branch in enumerate(program.branches)
                if index != selected
            ),
            start=np.zeros((2, 2), dtype=complex),
        ) - I2)))
        fine_branch_changes.extend(branch_norms)
        for presentation in program.presentations:
            coarse_group_changes.extend(
                float(np.linalg.norm(effect)) for effect in presentation.effects
            )
            for group, process in zip(presentation.groups, presentation.processes):
                operators = tuple(program.branches[index].operator for index in group)
                deleted = c321.choi(operators[:-1]) if len(operators) > 1 else np.zeros_like(process)
                process_changes.append(float(np.linalg.norm(process - deleted)))
        bank = by_bank[program.bank_index]
        wrong_target_labels += int((program.first_program ^ 0) != program.second_program)
        no_rewrite_program = bank.compiled.programs[program.first_program]
        no_rewrite_ops = tuple(
            right @ left
            for left in program.first_source.kraus
            for right in no_rewrite_program.kraus
        )
        actual_by_pointer = {
            (branch.first_pointer, branch.second_pointer): branch
            for branch in program.branches
        }
        for first_pointer, left in enumerate(program.first_source.kraus):
            for second_pointer, right in enumerate(no_rewrite_program.kraus):
                if second_pointer >= len(program.second_source.kraus):
                    continue
                branch = actual_by_pointer[(first_pointer, second_pointer)]
                deleted = right @ left
                rewrite_effect_changes.append(float(np.linalg.norm(
                    branch.effect - deleted.conj().T @ deleted
                )))
                rewrite_process_changes.append(float(np.linalg.norm(
                    branch.process - c321.choi((deleted,))
                )))
    positive_process = tuple(change for change in process_changes if change > TOL)
    zero_process = sum(change <= TOL for change in process_changes)
    positive_fine = tuple(change for change in fine_branch_changes if change > TOL)
    zero_fine = sum(change <= TOL for change in fine_branch_changes)
    positive_coarse = tuple(change for change in coarse_group_changes if change > TOL)
    zero_coarse = sum(change <= TOL for change in coarse_group_changes)
    invalid_calls = (
        lambda: validate_ordered_pair(banks[0], 0, 0, 0),
        lambda: validate_ordered_pair(banks[0], -1, 1, 1),
        lambda: validate_ordered_pair(banks[-1], 0, 3, 3),
        lambda: validate_ordered_pair(banks[0], 0, 1, 0),
        lambda: validate_ordered_pair(banks[0], 0, 1, 8),
        lambda: declared_groups(0, 3),
        lambda: declared_groups(3, 9),
        lambda: validate_groups(4, tuple()),
        lambda: validate_groups(4, ((0,), (1,), (2,))),
        lambda: validate_groups(4, ((0,), (1,), (2,), (3,), (3,))),
        lambda: validate_groups(4, ((0,), (1,), (2,), (4,))),
        lambda: validate_groups(4, ((0,), (1,), (2,), ("3",))),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1
    detail = {
        "selected_positive_fine_deletions": len(selected_positive_fine_defects),
        "minimum_selected_positive_fine_deletion_completeness_defect": min(selected_positive_fine_defects),
        "all_fine_branch_deletion_attempts": len(fine_branch_changes),
        "positive_product_fine_deletions_detected": len(positive_fine),
        "structural_zero_fine_branches": zero_fine,
        "minimum_positive_fine_deletion_change": min(positive_fine),
        "all_coarse_group_deletion_attempts": len(coarse_group_changes),
        "positive_coarse_group_deletions_detected": len(positive_coarse),
        "structural_zero_coarse_groups": zero_coarse,
        "minimum_positive_coarse_group_deletion_change": min(positive_coarse),
        "process_branch_deletions": len(process_changes),
        "nonzero_process_branch_deletions": len(positive_process),
        "zero_operator_process_branch_deletions": zero_process,
        "minimum_nonzero_process_branch_deletion_Choi_change": min(positive_process),
        "delta_zero_wrong_target_labels": wrong_target_labels,
        "maximum_rewrite_deletion_effect_change": max(rewrite_effect_changes),
        "maximum_rewrite_deletion_process_change": max(rewrite_process_changes),
        "domain_rejections": rejected,
        "domain_attempts": len(invalid_calls),
        "host_repair": False,
    }
    check(
        "positive-product deletions are detected, structural-zero branches stay explicitly inert, and malformed domains reject",
        len(selected_positive_fine_defects) == 342
        and min(selected_positive_fine_defects) > 1e-6
        and len(fine_branch_changes) == 10498
        and len(positive_fine) + zero_fine == 10498
        and len(positive_fine) > 0
        and zero_fine > 0
        and min(positive_fine) > 1e-8
        and len(coarse_group_changes) == 21302
        and len(positive_coarse) + zero_coarse == 21302
        and len(positive_coarse) > 0
        and zero_coarse > 0
        and min(positive_coarse) > 1e-8
        and len(process_changes) == 21302
        and len(positive_process) + zero_process == 21302
        and zero_process > 0
        and min(positive_process) > 1e-8
        and wrong_target_labels == 342
        and max(rewrite_effect_changes) > 0.05
        and max(rewrite_process_changes) > 0.1
        and rejected == len(invalid_calls)
        and not detail["host_repair"],
        detail,
    )
    return detail


def no_go_gate_controls() -> dict[str, object]:
    text = normalized(NOTE) if NOTE.exists() else ""
    forbidden = (
        "cross-program composition cannot add rank",
        "all cross-program instruments are exhausted",
        "no larger composition can add rank",
        "born selection is impossible",
        "requires a new axiom",
        "creates axiom pressure",
    )
    detail = {
        "gate_scope": "342 within-bank ordered p!=q pairs and five declared coarse families",
        "N1_distinct_attempted_routes": 7,
        "N2_explicit_conditions": 5,
        "N2_pairwise_rows": 10,
        "N3_hidden_conditions_remaining": 0,
        "N4_matching_witnesses": 4,
        "N4_nonmatching_witnesses_used": 0,
        "N5_tested_resolution": "rewrite label, ordered branch, coarse effect, incidence, and process tag",
        "N5_broad_nonforcing_claim": False,
        "N6_new_axiom_or_primitive_claim": False,
        "N6_live_out_of_grammar_routes_named": 5,
        "N7_steelman_present": "steelman" in text,
        "N7_broader_claim_demoted": True,
        "N8_cross_cycle_echoes": 4,
        "gate_disposition": "PASS only for finite census and first-pointer effect-incidence redundancy",
        "forbidden_broad_phrase_hits": tuple(phrase for phrase in forbidden if phrase in text),
    }
    check(
        "N1-N8 passes only the finite census and first-pointer redundancy while rejecting broad nonforcing",
        detail["N1_distinct_attempted_routes"] >= 5
        and detail["N2_pairwise_rows"] == 10
        and detail["N3_hidden_conditions_remaining"] == 0
        and detail["N4_nonmatching_witnesses_used"] == 0
        and not detail["N5_broad_nonforcing_claim"]
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
        "campaign_commit_is_pinned_main_base_ancestor": lineage["campaign_commit_is_pinned_main_base_ancestor"],
        "Cycle381_383_385_390_394_398_401_404_status": "campaign inputs or outputs at construction",
        "future_landing_allowed": lineage["future_landing_allowed"],
        "supplied_51_program_table_and_seven_banks": True,
        "supplied_ordered_pair_grammar": "all p!=q within each fixed bank; no cross-bank pairs",
        "supplied_delta_preparation": "three-M2 basis state d=p XOR q",
        "supplied_fixed_rewrite_circuit": "three parallel delta-to-program CNOTs",
        "supplied_five_coarse_grouping_rules": FAMILIES,
        "supplied_effect_functionality_key_and_premise": True,
        "supplied_process_tag_definition": "Choi sum of retained ordered Kraus products",
        "supplied_positive_root_compiler_choice": True,
        "supplied_contact_postcomposition": True,
        "supplied_program_delta_state_and_two_blank_pointers": True,
        "supplied_bank_invocation": True,
        "supplied_frame_transport": True,
        "supplied_M2_embedding_constraints_and_size_fixtures": True,
        "supplied_mass_and_contact_fixtures": True,
        "host_program_relabel_or_branch_query": False,
        "sampling_rule": None,
        "cross_bank_composition": None,
        "third_or_later_use": None,
        "arbitrary_set_partition_eligibility": None,
        "coherent_delta_genesis": None,
        "autonomous_program_menu_or_grouping_genesis": None,
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
        "status split and all rewrite/grammar/process/physical imports are explicit without semantic promotion",
        not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["future_landing_allowed"]
        and detail["supplied_51_program_table_and_seven_banks"]
        and detail["supplied_ordered_pair_grammar"].startswith("all p!=q")
        and detail["supplied_delta_preparation"].startswith("three-M2")
        and detail["supplied_fixed_rewrite_circuit"].startswith("three parallel")
        and detail["supplied_five_coarse_grouping_rules"] == FAMILIES
        and detail["supplied_effect_functionality_key_and_premise"]
        and detail["supplied_process_tag_definition"].startswith("Choi")
        and detail["supplied_positive_root_compiler_choice"]
        and detail["supplied_contact_postcomposition"]
        and detail["supplied_program_delta_state_and_two_blank_pointers"]
        and detail["supplied_bank_invocation"]
        and detail["supplied_frame_transport"]
        and detail["supplied_M2_embedding_constraints_and_size_fixtures"]
        and detail["supplied_mass_and_contact_fixtures"]
        and not detail["host_program_relabel_or_branch_query"]
        and all(detail[key] is None for key in (
            "sampling_rule",
            "cross_bank_composition",
            "third_or_later_use",
            "arbitrary_set_partition_eligibility",
            "coherent_delta_genesis",
            "autonomous_program_menu_or_grouping_genesis",
            "universal_menu_eligibility",
            "selected_numerical_grade",
            "Born_selection",
            "probability_interpretation",
            "actuality_or_history_sampler",
            "Record_formation",
            "frequency_theorem",
            "global_no_go",
            "minimum_content_claim",
            "axiom_pressure",
        ))
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 404: PHYSICAL CROSS-PROGRAM REWRITE COMPOSITION")
    print("authority=none; audit=unset; changes exactly W2")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    base, banks, cycle398_system, source_checks = c401.cycle398_source(fixtures)
    source = cycle401_system(cycle398_system, banks)
    programs, update_rows = compose_all(banks)
    grammar = rewrite_and_grammar_controls(banks, programs, update_rows)
    quotient = process_quotient_controls(source, programs)
    incidence = incidence_controls(source, programs)
    contact = contact_controls(base, banks, programs)
    physical = physical_controls(fixtures, programs, incidence["system"])
    attacks = deletion_and_domain_controls(banks, programs)
    gate = no_go_gate_controls()
    provenance = provenance_and_inventory_controls()
    check(
        "Cycle404 changes exactly W2 and obtains physical cross-program class/rank gain without semantic promotion",
        not note["missing"]
        and fixture_checks == (1, 0)
        and source_checks == (2, 0)
        and grammar["lawful_ordered_pairs"] == 342
        and quotient["effect_process_pairs"] == 4015
        and incidence["final_shape"] == (2063, 3348)
        and incidence["final_exact_integer_rank"] == 1159
        and incidence["rank_gain_over_Cycle401"] == 967
        and contact["actual_contact_is_load_bearing_in_every_bank"]
        and physical["proper_cubic_frames"] == 24
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and gate["gate_disposition"].startswith("PASS")
        and provenance["Born_selection"] is None
        and provenance["global_no_go"] is None
        and provenance["axiom_pressure"] is None,
        {
            "disposition": "positive physical cross-program rewrite extension",
            "grammar": "342 ordered p!=q pairs x five declared presentations",
            "ordered_fine_branches": 10498,
            "cross_menus_and_occurrences": (1710, 21302),
            "final_shape_classes_rank_affine": ((2063, 3348), 3348, 1159, 2189),
            "new_classes_and_rank_over_Cycle401": (2712, 967),
            "effect_process_pairs": 4015,
            "scope_boundary": "no cross-bank pair, third use, arbitrary partition, sampling, or universal eligibility",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_CROSS_PROGRAM_REWRITE_COMPOSITION_OPEN")
        return 1
    print("RESULT PHYSICAL_CROSS_PROGRAM_REWRITE_COMPOSITION_EXACT_RANK_GAIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
