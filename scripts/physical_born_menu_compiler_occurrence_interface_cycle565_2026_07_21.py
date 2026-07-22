#!/usr/bin/env python3
"""Cycle565: finite physical Born-menu compilers and occurrence firewall.

Three independent finite menu mechanisms are compiled on a bounded M2
substrate: ternary Naimark dilation, mixed-projective split/merge, and a
scaled-projector conserved-resource split.  Menu eligibility and numerical
grades are supplied.  The exact Cycle531/552 occurrence interface is consumed
only after an independent typed MEMBER and matching receipt exist.

Squared branch norms, reduced diagonals, additive grades, and resource shares
are not identified with occurrence probabilities or realized history.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import inspect
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19 as c460
import physical_autonomous_local_member_law_cell_cycle552_2026_07_21 as c552


c531 = c552.c531
c505 = c531.c505

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PR_PINS = {
    5472: {
        "commit": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
        "note": (
            "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_"
            "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
            "aacdadf98ed18c01acea0ea77f480664c50ecd4d",
        ),
        "runner": (
            "scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py",
            "b7aee07b4e7c2077681e34d66304d242a0d4da15",
        ),
    },
    5476: {
        "commit": "a994617819f57e599dd101c654be366123392236",
        "note": (
            "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_"
            "AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
            "9179965852694c9bab3f9a7807145c66a94fbfe5",
        ),
        "runner": (
            "scripts/born_form_scaled_projector_menu_family_sitewise_"
            "forcing_2026_07_17.py",
            "b3dbdd649e00380eff8f99ceb95055501fc7fd22",
        ),
    },
    5479: {
        "commit": "84053108a424cef26dc23e484549df331ad2050f",
        "note": (
            "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_"
            "FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
            "249eafaed1176c2192b5453844f1fa681ba79a54",
        ),
        "runner": (
            "scripts/born_form_menu_outcome_threshold_and_mixed_projective_"
            "forcing_2026_07_17.py",
            "2262c5ce6a087db6c54102ec389a059024fa025b",
        ),
    },
}

LOCAL_PINS = {
    "physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py":
        "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py":
        "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19.py":
        "934f8bcda20d054e4a27f0710ff91da0f16ad0a27f7b6f5e50fa681a656c8c9a",
    "physical_local_menu_registration_bridge_cycle384_2026_07_18.py":
        "6ad39593e4fa9e3f1310372e23036e9c340bb3094cb53371f2306488dc938159",
    "physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18.py":
        "3caee29d02054a7aec31122b1053ab40a2265bb48384bba6fc925e9c457fee06",
    "physical_fixed_menu_schema_compiler_cycle382_2026_07_18.py":
        "38649c1215d7b52a7e6d8325c9b2f04d1b3c4d35d63fd8fc85fbedb2df08b6b5",
}

I2 = np.eye(2, dtype=complex)
SX = np.asarray(((0, 1), (1, 0)), dtype=complex)
SY = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
SZ = np.asarray(((1, 0), (0, -1)), dtype=complex)
PAULIS = (SX, SY, SZ)

REG_PROGRAM = (0, 1, 2)
REG_VALID = 3
REG_WORK = 4
REG_M2 = 5
ANALOG_M2 = 48
RESOURCE_M2 = 72
MENU_COMPILER_M2 = REG_M2 + ANALOG_M2 + RESOURCE_M2

Word = tuple[int, ...]


@dataclass(frozen=True)
class AnalogProgram:
    program: int
    name: str
    route: str
    held: bool
    factors: tuple[np.ndarray, ...]
    isometry: np.ndarray
    offset: int
    schedule: tuple[c460.Gate, ...]
    compile_row: dict[str, object]
    outcome_groups: tuple[tuple[int, ...], ...]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def git_blob(commit: str, path: str) -> str | None:
    completed = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    return completed.stdout.strip() if completed.returncode == 0 else None


def dependency_and_note_controls() -> None:
    print("\nEXACT-PIN / NOTE CONTRACT")
    pin_rows = {}
    for number, row in PR_PINS.items():
        commit = row["commit"]
        pin_rows[number] = {
            kind: {"path": value[0], "expected_blob": value[1],
                   "observed_blob": git_blob(commit, value[0])}
            for kind, value in (("note", row["note"]), ("runner", row["runner"]))
        }
    local_rows = {
        name: file_sha(ROOT / "scripts" / name) for name in LOCAL_PINS
    }
    required = (
        "authority: none", "audit: unset", "cycle 565",
        "local ternary effect-menu / naimark compiler",
        "mixed-projective split/merge compiler",
        "scaled-projector conserved-resource split",
        "exact conditional occurrence interface",
        "additive algebraic weight is not objective member occurrence",
        "a forcing theorem conditional on a supplied functional/menu family is not physical selection",
        "all 24 proper-cubic frames", "all 576 ordered frame products",
        "n1 — normalized alternative routes", "n8 — cross-cycle echo",
        "broad no-go: fail / do not ship", "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check(
        "closed Born PR artifacts, retained physical interfaces, and the Cycle565 note are exact-pinned",
        all(
            item["observed_blob"] == item["expected_blob"]
            for row in pin_rows.values() for item in row.values()
        ) and local_rows == LOCAL_PINS and not missing,
        {"PR_blobs": pin_rows, "local_SHA256": local_rows, "missing_note_phrases": missing},
    )


def projector(direction: tuple[float, float, float]) -> np.ndarray:
    vector = np.asarray(direction, dtype=float)
    if abs(float(vector @ vector) - 1.0) > 2e-12:
        raise ValueError("Bloch direction is not unit")
    return (I2 + sum(component * pauli for component, pauli in zip(vector, PAULIS))) / 2


def effect_of(factor: np.ndarray) -> np.ndarray:
    return factor.conj().T @ factor


def grade(rho: np.ndarray, effect: np.ndarray) -> float:
    value = np.trace(rho @ effect)
    if abs(value.imag) > TOL:
        raise ValueError("supplied grade left the real effect-functional domain")
    return float(value.real)


def trine_factors(unitary: np.ndarray | None = None) -> tuple[np.ndarray, ...]:
    root3 = math.sqrt(3.0)
    directions = (
        (1.0, 0.0, 0.0),
        (-0.5, root3 / 2, 0.0),
        (-0.5, -root3 / 2, 0.0),
    )
    if unitary is None:
        unitary = I2
    return tuple(
        math.sqrt(2.0 / 3.0) * unitary @ projector(direction) @ unitary.conj().T
        for direction in directions
    )


def mixed_factors(components: tuple[tuple[Fraction, tuple[float, float, float]], ...]) -> tuple[np.ndarray, ...]:
    if sum((weight for weight, _ in components), Fraction(0)) != 1:
        raise ValueError("mixed-projective component weights must sum to one")
    factors = []
    for weight, direction in components:
        if weight <= 0:
            raise ValueError("mixed-projective weights must be positive")
        scale = math.sqrt(float(weight))
        factors.extend((
            scale * projector(direction),
            scale * projector(tuple(-entry for entry in direction)),
        ))
    return tuple(factors)


def analog_specifications() -> tuple[tuple[int, str, str, bool, tuple[np.ndarray, ...], tuple[tuple[int, ...], ...]], ...]:
    H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
    z = (0.0, 0.0, 1.0)
    mz = (0.0, 0.0, -1.0)
    x = (1.0, 0.0, 0.0)
    mx = (-1.0, 0.0, 0.0)
    d1 = ((Fraction(3, 4), z), (Fraction(1, 4), mz))
    d2 = ((Fraction(1, 2), z), (Fraction(1, 4), x), (Fraction(1, 4), mx))
    d2_refined = (
        (Fraction(1, 4), z), (Fraction(1, 4), z),
        (Fraction(1, 4), x), (Fraction(1, 4), mx),
    )
    return (
        (0, "A-trine-train", "ternary-naimark", False, trine_factors(), ((0,), (1,), (2,))),
        (1, "A-trine-held-context", "ternary-naimark", True, trine_factors(H), ((0,), (1,), (2,))),
        (2, "B-mixed-D1-train", "mixed-split-merge", False, mixed_factors(d1), ((0, 2), (1, 3))),
        (3, "B-mixed-D2-held", "mixed-split-merge", True, mixed_factors(d2), ((0, 2, 4), (1, 3, 5))),
        (4, "B-mixed-D2-refined-held", "mixed-split-merge", True, mixed_factors(d2_refined), ((0, 2, 4, 6), (1, 3, 5, 7))),
    )


def validate_analog_block_code(program: int, occupied_block: int) -> None:
    if program not in range(5) or occupied_block != program:
        raise ValueError("program label and occupied analog block leave the direct-sum code")


def build_analog_programs() -> tuple[AnalogProgram, ...]:
    programs = []
    offset = 0
    for program, name, route, held, factors, groups in analog_specifications():
        isometry = np.vstack(factors)
        schedule, row = c460.compile_adjacent_isometry(isometry, offset, name)
        programs.append(AnalogProgram(
            program, name, route, held, factors, isometry, offset, schedule, row, groups
        ))
        offset += isometry.shape[0]
    if offset != ANALOG_M2:
        raise ValueError("Cycle565 analog line width drifted")
    return tuple(programs)


def register_schedule() -> tuple[c505.Gate, ...]:
    # valid = NOT(p0 AND p1 AND p2), with one clean work M2.
    return (
        c505.gate("X", (REG_VALID,), "register:seed-valid", REG_M2),
        c505.gate("TOFFOLI", (REG_PROGRAM[0], REG_PROGRAM[1], REG_WORK), "register:pair", REG_M2),
        c505.gate("TOFFOLI", (REG_WORK, REG_PROGRAM[2], REG_VALID), "register:exclude-7", REG_M2),
        c505.gate("TOFFOLI", (REG_PROGRAM[0], REG_PROGRAM[1], REG_WORK), "register:uncompute-pair", REG_M2),
    )


def program_bits(program: int) -> Word:
    if program not in range(8):
        raise ValueError("program leaves three-M2 word")
    return tuple((program >> bit) & 1 for bit in range(3))


def bits_index(bits: Word) -> int:
    return sum(bit << index for index, bit in enumerate(bits))


def index_bits(index: int, width: int) -> Word:
    return tuple((index >> bit) & 1 for bit in range(width))


def apply_bits(bits: Word, schedule: tuple[c505.Gate, ...], *, reverse: bool = False,
               delete_label: str | None = None) -> Word:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("word leaves binary domain")
    sequence = tuple(reversed(schedule)) if reverse else schedule
    word = list(bits)
    for item in sequence:
        if item.label == delete_label:
            continue
        c505.apply_gate(word, item)
    return tuple(word)


def register_matrix() -> np.ndarray:
    matrix = np.zeros((1 << REG_M2, 1 << REG_M2), dtype=complex)
    for column in range(1 << REG_M2):
        source = index_bits(column, REG_M2)
        target = apply_bits(source, register_schedule())
        matrix[bits_index(target), column] = 1.0
    return matrix


def literal_register_trace() -> dict[str, object]:
    literal_schedule = tuple(
        primitive for item in register_schedule() for primitive in c552.expand_logical(item)
    )
    maximum_unitarity = 0.0
    routing_swaps = nn_calls = route_failures = restoration_failures = 0
    digest = sha256()
    for item in literal_schedule:
        size = 1 << len(item.sites)
        matrix = np.asarray(item.matrix, dtype=complex).reshape(size, size)
        maximum_unitarity = max(maximum_unitarity, float(np.max(abs(matrix.conj().T @ matrix - np.eye(size)))))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:".encode())
        digest.update(repr(tuple((z.real.hex(), z.imag.hex()) for z in item.matrix)).encode())
        if len(item.sites) == 1:
            nn_calls += 1
            continue
        first, second = item.sites
        route = c552.line_route(first, second)
        route_failures += sum(abs(left - right) != 1 for left, right in route)
        routing_swaps += 2 * len(route)
        nn_calls += 1 + 6 * len(route)
        labels = list(range(REG_M2))
        for left, right in route:
            labels[left], labels[right] = labels[right], labels[left]
        final_sites = (second - 1, second) if first < second else (second + 1, second)
        restoration_failures += int(tuple(labels[site] for site in final_sites) != (first, second))
        for left, right in reversed(route):
            labels[left], labels[right] = labels[right], labels[left]
        restoration_failures += int(labels != list(range(REG_M2)))
    return {
        "logical_gates": len(register_schedule()),
        "literal_one_two_M2_gates": len(literal_schedule),
        "literal_kinds": dict(Counter(item.kind for item in literal_schedule)),
        "maximum_support_M2": max(len(item.sites) for item in literal_schedule),
        "maximum_unitarity_residual": maximum_unitarity,
        "forward_reverse_adjacent_SWAPS": routing_swaps,
        "NN_calls": nn_calls,
        "route_failures": route_failures,
        "operand_or_restoration_failures": restoration_failures,
        "sha256": digest.hexdigest(),
    }


def registration_controls() -> dict[str, object]:
    print("\nBOUNDED SEVEN-MENU REGISTRATION / LITERAL M2")
    rows = []
    for program in range(8):
        source = (*program_bits(program), 0, 0)
        output = apply_bits(source, register_schedule())
        restored = apply_bits(output, register_schedule(), reverse=True)
        rows.append({
            "program": program, "valid": output[REG_VALID], "work": output[REG_WORK],
            "inverse": restored == source,
        })
    matrix = register_matrix()
    input_embedding = np.zeros((32, 8), dtype=complex)
    target_embedding = np.zeros((32, 8), dtype=complex)
    for program in range(8):
        source = (*program_bits(program), 0, 0)
        target = (*program_bits(program), int(program < 7), 0)
        input_embedding[bits_index(source), program] = 1
        target_embedding[bits_index(target), program] = 1
    trace = literal_register_trace()
    toffoli = c552.c523.bare_toffoli_controls()
    check(
        "one five-M2 reversible predicate registers exactly seven menu programs and compiles to literal one/two-M2 gates",
        all(row["valid"] == int(row["program"] < 7) and row["work"] == 0 and row["inverse"] for row in rows)
        and np.linalg.norm(matrix @ input_embedding - target_embedding) == 0
        and np.linalg.norm(matrix.conj().T @ matrix - np.eye(32)) == 0
        and trace["maximum_support_M2"] == 2 and trace["maximum_unitarity_residual"] < TOL
        and trace["route_failures"] == trace["operand_or_restoration_failures"] == 0
        and toffoli["pass"],
        {"truth_rows": rows, "EG_residual": float(np.linalg.norm(matrix @ input_embedding - target_embedding)),
         "literal_trace": trace, "Cycle523_Toffoli": toffoli},
    )
    return {"matrix": matrix, "trace": trace, "rows": rows}


def apply_analog(state: np.ndarray, schedule: tuple[c460.Gate, ...]) -> np.ndarray:
    output = state.copy()
    for item in schedule:
        left, right = item.sites
        matrix = c460.gate_matrix(item)
        output[:, [left, right], :] = np.einsum(
            "ij,ajk->aik", matrix, output[:, [left, right], :]
        )
    return output


def analog_square_controls(programs: tuple[AnalogProgram, ...], registration: dict[str, object]) -> dict[str, object]:
    print("\nROUTE A/B PHYSICAL E-G / INVERSE / LEAKAGE")
    columns = 2 * len(programs)
    source = np.zeros((32, ANALOG_M2, columns), dtype=complex)
    target = np.zeros_like(source)
    schedule = tuple(item for program in programs for item in program.schedule)
    for block, program in enumerate(programs):
        validate_analog_block_code(program.program, block)
        source_bits = (*program_bits(program.program), 0, 0)
        target_bits = (*program_bits(program.program), 1, 0)
        for component in range(2):
            column = 2 * block + component
            source[bits_index(source_bits), program.offset + component, column] = 1
            target[bits_index(target_bits), program.offset:program.offset + len(program.isometry), column] = program.isometry[:, component]
    after_register = np.einsum("ab,bmc->amc", registration["matrix"], source)
    output = apply_analog(after_register, schedule)
    restored_analog = apply_analog(output, c460.inverse_schedule(schedule))
    restored = np.einsum("ab,bmc->amc", registration["matrix"].conj().T, restored_analog)
    target_flat = target.reshape(32 * ANALOG_M2, columns)
    output_flat = output.reshape(32 * ANALOG_M2, columns)
    coefficients = target_flat.conj().T @ output_flat
    leakage = float(np.linalg.norm(output_flat - target_flat @ coefficients))
    rows = tuple({
        "program": item.program, "name": item.name, "held": item.held,
        "modes": len(item.isometry), "adjacent_Givens": len(item.schedule),
        "Gram": float(np.linalg.norm(item.isometry.conj().T @ item.isometry - I2)),
        **item.compile_row,
    } for item in programs)
    maximum_gate_unitarity = max(
        float(np.linalg.norm(c460.gate_matrix(item).conj().T @ c460.gate_matrix(item) - I2))
        for item in schedule
    )
    check(
        "registered ternary and mixed-projective blocks satisfy Eout Gcoarse = Gphysical Ein with exact inverse on the declared direct-sum code",
        np.linalg.norm(output - target) < TOL and np.linalg.norm(restored - source) < TOL
        and leakage < TOL and maximum_gate_unitarity < TOL
        and all(item.sites[1] == item.sites[0] + 1 for item in schedule),
        {"program_rows": rows, "EG_residual": float(np.linalg.norm(output - target)),
         "inverse_residual": float(np.linalg.norm(restored - source)), "leakage": leakage,
         "maximum_gate_unitarity": maximum_gate_unitarity, "adjacent_Givens": len(schedule)},
    )
    return {"source": source, "target": target, "output": output, "schedule": schedule,
            "EG": float(np.linalg.norm(output - target)), "inverse": float(np.linalg.norm(restored - source)),
            "leakage": leakage, "rows": rows}


def route_a_controls(programs: tuple[AnalogProgram, ...]) -> dict[str, object]:
    print("\nROUTE A — LOCAL TERNARY EFFECT-MENU / NAIMARK")
    train, held = programs[0], programs[1]
    H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
    rho = np.diag((Fraction(2, 3), Fraction(1, 3))).astype(complex)
    rho_held = H @ rho @ H.conj().T
    psi = np.asarray((1, 1j), dtype=complex) / math.sqrt(2)
    held_psi = H @ psi
    rows = []
    for item, state, grading in ((train, psi, rho), (held, held_psi, rho_held)):
        effects = tuple(effect_of(factor) for factor in item.factors)
        output = item.isometry @ state
        branch_weights = tuple(float(np.linalg.norm(output[2*j:2*j+2]) ** 2) for j in range(3))
        effect_weights = tuple(float(np.vdot(state, effect @ state).real) for effect in effects)
        algebraic_grades = tuple(grade(grading, effect) for effect in effects)
        rows.append({
            "program": item.program, "held": item.held,
            "effect_sum_residual": float(np.linalg.norm(sum(effects) - I2)),
            "branch_effect_residual": float(np.linalg.norm(np.asarray(branch_weights) - np.asarray(effect_weights))),
            "isometry_norm": float(np.linalg.norm(output)),
            "supplied_grade_sum": sum(algebraic_grades),
            "branch_squared_norms_not_called_probability": branch_weights,
        })
    context_residual = float(np.linalg.norm(
        held.isometry @ held_psi - np.kron(np.eye(3), H) @ (train.isometry @ psi)
    ))
    grade_context_residual = max(
        abs(grade(rho_held, effect_of(held.factors[j])) - grade(rho, effect_of(train.factors[j])))
        for j in range(3)
    )
    check(
        "the train trine and held rotated trine are normalized Naimark menus with simultaneous-context invariance",
        max(row["effect_sum_residual"] for row in rows) < TOL
        and max(row["branch_effect_residual"] for row in rows) < TOL
        and max(abs(row["isometry_norm"] - 1) for row in rows) < TOL
        and max(abs(row["supplied_grade_sum"] - 1) for row in rows) < TOL
        and context_residual < TOL and grade_context_residual < TOL,
        {"rows": rows, "context_isometry_residual": context_residual,
         "context_grade_residual": grade_context_residual,
         "menu_eligibility": "finite programs 0 and 1 supplied", "grade_functional": "rho supplied"},
    )
    return {"rows": rows, "context": context_residual, "grade_context": grade_context_residual}


def choi_sum(factors: tuple[np.ndarray, ...], indices: tuple[int, ...]) -> np.ndarray:
    return sum((np.outer(factor.reshape(-1, order="F"), factor.reshape(-1, order="F").conj())
                for index, factor in enumerate(factors) if index in indices), np.zeros((4, 4), dtype=complex))


def route_b_controls(programs: tuple[AnalogProgram, ...]) -> dict[str, object]:
    print("\nROUTE B — MIXED-PROJECTIVE SPLIT / MERGE")
    selected = programs[2:5]
    rho = np.asarray(((0.6, 0.1 - 0.05j), (0.1 + 0.05j, 0.4)), dtype=complex)
    rows = []
    for item in selected:
        effects = tuple(effect_of(factor) for factor in item.factors)
        group0 = item.outcome_groups[0]
        merged = sum((effects[index] for index in group0), np.zeros((2, 2), dtype=complex))
        algebraic = sum(grade(rho, effects[index]) for index in group0)
        rows.append({
            "program": item.program, "held": item.held, "fine_outcomes": len(effects),
            "menu_sum_residual": float(np.linalg.norm(sum(effects) - I2)),
            "merged_effect": merged, "merged_grade": grade(rho, merged),
            "fine_additive_grade": algebraic,
            "additivity_residual": abs(algebraic - grade(rho, merged)),
            "selected_choi": choi_sum(item.factors, group0),
        })
    effect_residuals = tuple(float(np.linalg.norm(rows[index]["merged_effect"] - rows[0]["merged_effect"])) for index in (1, 2))
    grade_residuals = tuple(abs(rows[index]["merged_grade"] - rows[0]["merged_grade"]) for index in (1, 2))
    refinement_choi = float(np.linalg.norm(rows[1]["selected_choi"] - rows[2]["selected_choi"]))
    decomposition_choi_separator = float(np.linalg.norm(rows[0]["selected_choi"] - rows[1]["selected_choi"]))
    nonlinear_fine_sums = []
    for item in selected:
        effects = tuple(effect_of(factor) for factor in item.factors)
        nonlinear_fine_sums.append(sum(float(np.trace(effects[index] @ effects[index]).real)
                                       for index in item.outcome_groups[0]))
    nonlinear_separator = max(nonlinear_fine_sums) - min(nonlinear_fine_sums)
    check(
        "three fine presentations merge to one effect and one supplied additive grade; refinement preserves CP while distinct decomposition remains physically visible",
        max(row["menu_sum_residual"] for row in rows) < TOL
        and max(row["additivity_residual"] for row in rows) < TOL
        and max(effect_residuals) < TOL and max(grade_residuals) < TOL
        and refinement_choi < TOL and decomposition_choi_separator > 1e-3
        and nonlinear_separator > 1e-3,
        {"rows": [{key: value for key, value in row.items() if key not in ("merged_effect", "selected_choi")} for row in rows],
         "decomposition_effect_residuals": effect_residuals,
         "decomposition_grade_residuals": grade_residuals,
         "refinement_CP_residual": refinement_choi,
         "distinct_decomposition_CP_separator": decomposition_choi_separator,
         "nonlinear_fine_sum_separator": nonlinear_separator,
         "fine_tags_erased": False, "effect_functionality_and_additivity_supplied": True},
    )
    return {"rows": rows, "effect_residuals": effect_residuals,
            "grade_residuals": grade_residuals, "refinement_CP": refinement_choi,
            "decomposition_CP_separator": decomposition_choi_separator,
            "nonlinear_separator": nonlinear_separator}


def resource_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for block in range(2):
        start = 36 * block
        for quantum in range(12):
            source, target = start + 2 * quantum, start + 2 * quantum + 1
            gates.extend((
                c505.gate("CNOT", (source, target), f"resource:{block}:{quantum}:a", RESOURCE_M2),
                c505.gate("CNOT", (target, source), f"resource:{block}:{quantum}:b", RESOURCE_M2),
                c505.gate("CNOT", (source, target), f"resource:{block}:{quantum}:c", RESOURCE_M2),
            ))
    return tuple(gates)


def resource_word(program: int, *, output: bool = False) -> Word:
    if program not in (5, 6):
        raise ValueError("resource program must be 5 or 6")
    bits = [0] * RESOURCE_M2
    start = 36 * (program - 5)
    for quantum in range(12):
        bits[start + 2 * quantum + int(output)] = 1
        bits[start + 24 + quantum] = 1
    return tuple(bits)


def resource_partition(program: int) -> tuple[int, ...]:
    return (4, 8) if program == 5 else (2, 2, 8)


def resource_validate(bits: Word, program: int, *, output: bool = False) -> None:
    if len(bits) != RESOURCE_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("resource word leaves binary M2 domain")
    if bits != resource_word(program, output=output):
        raise ValueError("resource word leaves declared split code")


def route_c_controls(registration: dict[str, object]) -> dict[str, object]:
    print("\nROUTE C — SCALED-PROJECTOR CONSERVED-RESOURCE SPLIT")
    schedule = resource_schedule()
    rows = []
    rho = np.diag((Fraction(2, 3), Fraction(1, 3))).astype(complex)
    pz, pmz = projector((0.0, 0.0, 1.0)), projector((0.0, 0.0, -1.0))
    for program in (5, 6):
        source = resource_word(program)
        output = apply_bits(source, schedule)
        target = resource_word(program, output=True)
        restored = apply_bits(output, schedule, reverse=True)
        partition = resource_partition(program)
        effects = tuple(float(count) / 12 * pz for count in partition) + (pmz,)
        fine_grade = sum(grade(rho, effect) for effect in effects)
        ray_grade = sum(grade(rho, effect) for effect in effects[:-1])
        program_source = (*program_bits(program), 0, 0)
        program_output = apply_bits(program_source, register_schedule())
        rows.append({
            "program": program, "held": program == 6, "partition": partition,
            "EG_exact": output == target, "inverse_exact": restored == source,
            "registration_valid": program_output[REG_VALID],
            "work": program_output[REG_WORK], "input_excitations": sum(source),
            "output_excitations": sum(output),
            "menu_sum_residual": float(np.linalg.norm(sum(effects) - I2)),
            "supplied_grade_sum": fine_grade, "positive_ray_grade": ray_grade,
        })
    refinement_grade_residual = abs(rows[0]["positive_ray_grade"] - rows[1]["positive_ray_grade"])
    check(
        "physical SWAP networks conserve the scaled-ray resource and train/held splits coarse-grain to the same menu and additive grade",
        all(row["EG_exact"] and row["inverse_exact"] and row["registration_valid"] == 1 and row["work"] == 0 for row in rows)
        and all(row["input_excitations"] == row["output_excitations"] == 24 for row in rows)
        and max(row["menu_sum_residual"] for row in rows) < TOL
        and max(abs(row["supplied_grade_sum"] - 1) for row in rows) < TOL
        and refinement_grade_residual < TOL
        and all(len(item.sites) == 2 and abs(item.sites[0] - item.sites[1]) == 1 for item in schedule),
        {"rows": rows, "refinement_grade_residual": refinement_grade_residual,
         "logical_CNOTs": len(schedule), "resource_is_energy_claimed": False},
    )
    return {"rows": rows, "schedule": schedule,
            "refinement_grade_residual": refinement_grade_residual}


def interface_outcome_count(program: int) -> int:
    return {0: 3, 1: 3, 2: 2, 3: 2, 4: 2, 5: 3, 6: 4}[program]


def validate_interface_member(program: int, member: int) -> None:
    if program not in range(7) or member not in range(interface_outcome_count(program)):
        raise ValueError("menu member leaves registered coarse-outcome interface")


def cycle531_fields(bits: Word) -> Word:
    return tuple(bits[site] for site in c552.C531_OUTPUT_FIELDS)


def occurrence_interface_controls() -> dict[str, object]:
    print("\nEXACT CYCLE531/552 CONDITIONAL OCCURRENCE INTERFACE")
    rows = []
    failures = inverse_failures = mismatch_failures = 0
    for program in range(7):
        for member in range(interface_outcome_count(program)):
            validate_interface_member(program, member)
            source = c552.prepare(
                binding=member, law=0, member=member, head=0,
                edge=1, plus=1, minus=0, K_position=program,
            )
            output = c552.physical_step(source)
            snapshot, law_snapshot = c552.snapshot_view(output, 0)
            source531 = c531.prepare(
                edge=1, plus=1, minus=0, K_position=program,
                binding_label=member, member_label=member, receipt_label=member,
            )
            expected531 = c531.logical_apply(source531)
            failures += int(snapshot != cycle531_fields(expected531))
            failures += int(snapshot[0] != 1 or snapshot[1] != 1 or snapshot[2] != 1)
            failures += int(law_snapshot != c552.one_hot(0))
            inverse_failures += int(c552.apply_schedule(output, reverse=True) != source)

            mismatch = c552.prepare(
                binding=(member + 1) % 5, law=0, member=member, head=0,
                edge=1, plus=1, minus=0, K_position=program,
            )
            mismatch_output = c552.physical_step(mismatch)
            mismatch_snapshot, _ = c552.snapshot_view(mismatch_output, 0)
            mismatch_failures += int(mismatch_snapshot[0] != 1 or mismatch_snapshot[1] != 0 or mismatch_snapshot[2] != 0)
            rows.append({"program": program, "member": member,
                         "occurrence": snapshot[1], "mismatch_occurrence": mismatch_snapshot[1]})
    refused = 0
    for program, member in ((0, 3), (2, 2), (5, 3), (6, 4), (7, 0)):
        try:
            validate_interface_member(program, member)
        except ValueError:
            refused += 1
    # The physical member word, not either supplied grading state, controls the
    # exact binder.  Changing rho therefore changes no interface bit.
    rho_a = np.diag((0.8, 0.2)).astype(complex)
    rho_b = np.diag((0.3, 0.7)).astype(complex)
    grades_differ = abs(grade(rho_a, projector((0.0, 0.0, 1.0)))
                         - grade(rho_b, projector((0.0, 0.0, 1.0)))) > 0.4
    same_source = c552.prepare(binding=0, law=0, member=0, head=0, edge=1, plus=1, minus=0, K_position=0)
    output_under_grade_a = c552.physical_step(same_source)
    output_under_grade_b = c552.physical_step(same_source)
    interface_independent_of_grade = output_under_grade_a == output_under_grade_b
    forbidden = ("grade", "weight", "norm", "diagonal", "probability", "sampler")
    port_name_hits = {}
    for function in (c552.prepare, c552.physical_step, c531.logical_apply):
        tree = ast.parse(inspect.getsource(function))
        names = tuple(
            node.id.lower() if isinstance(node, ast.Name) else node.attr.lower()
            for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute))
        )
        port_name_hits[function.__name__] = {
            token: sum(name == token for name in names) for token in forbidden
        }
    check(
        "registered menu labels reach Cycle552 only as independently supplied members and reproduce the exact Cycle531 conditional occurrence tuple",
        not any((failures, inverse_failures, mismatch_failures)) and refused == 5
        and grades_differ and interface_independent_of_grade
        and all(value == 0 for row in port_name_hits.values() for value in row.values()),
        {"interface_rows": len(rows), "failures": failures, "inverse_failures": inverse_failures,
         "mismatch_failures": mismatch_failures, "domain_refusals": refused,
         "different_supplied_grades_same_member_same_interface": interface_independent_of_grade,
         "interface_AST_forbidden_port_name_hits": port_name_hits,
         "member_source": "supplied Cycle552 MEMBER_STATE and law word",
         "Naimark_or_grade_selects_member": False, "framework_Record_produced": False},
    )
    return {"rows": rows, "failures": failures, "inverse_failures": inverse_failures,
            "mismatch_failures": mismatch_failures, "refusals": refused}


def block_output(program: AnalogProgram, schedule: tuple[c460.Gate, ...]) -> np.ndarray:
    source = np.zeros((ANALOG_M2, 2), dtype=complex)
    source[program.offset:program.offset + 2] = I2
    return c460.apply_schedule(source, schedule)


def deletion_and_domain_controls(programs: tuple[AnalogProgram, ...]) -> dict[str, object]:
    print("\nDELETION / LEAKAGE / LAWFUL DOMAIN")
    full_schedule = tuple(item for program in programs for item in program.schedule)
    analog_deletions = {}
    for program in (programs[1], programs[4]):
        own = program.schedule
        delete_index = len(own) // 2
        damaged = own[:delete_index] + own[delete_index + 1:]
        source = np.zeros((len(program.isometry), 2), dtype=complex)
        source[:2] = I2
        baseline = c460.apply_schedule(source, tuple(
            c460.Gate((item.sites[0] - program.offset, item.sites[1] - program.offset), item.matrix, item.label)
            for item in own
        ))
        damaged_local = c460.apply_schedule(source, tuple(
            c460.Gate((item.sites[0] - program.offset, item.sites[1] - program.offset), item.matrix, item.label)
            for item in damaged
        ))
        analog_deletions[program.name] = float(np.linalg.norm(damaged_local - baseline))

    invalid7 = (*program_bits(7), 0, 0)
    registration_deleted = apply_bits(invalid7, register_schedule(), delete_label="register:exclude-7")
    valid_source = (*program_bits(3), 0, 0)
    cleanup_deleted = apply_bits(valid_source, register_schedule(), delete_label="register:uncompute-pair")

    resource_source = resource_word(6)
    resource_full = apply_bits(resource_source, resource_schedule())
    resource_damaged = apply_bits(resource_source, resource_schedule(), delete_label="resource:1:0:b")
    resource_deletion_residual = math.sqrt(2.0) if resource_damaged != resource_full else 0.0

    malformed = 0
    actions = (
        lambda: projector((1.0, 1.0, 0.0)),
        lambda: mixed_factors(((Fraction(3, 4), (0.0, 0.0, 1.0)),)),
        lambda: resource_validate(tuple([0] * RESOURCE_M2), 5),
        lambda: resource_validate(resource_word(5, output=True), 5),
        lambda: validate_interface_member(7, 0),
        lambda: validate_analog_block_code(1, 0),
        lambda: apply_bits((0, 0, 2, 0, 0), register_schedule()),
    )
    for action in actions:
        try:
            action()
        except ValueError:
            malformed += 1
    schedule_digest = sha256("\n".join(
        f"{item.sites}:{','.join(f'{z.real.hex()}+{z.imag.hex()}j' for z in item.matrix)}"
        for item in full_schedule
    ).encode()).hexdigest()
    check(
        "registration, analog route, resource transfer, and declared domains have visible deletions and zero silent coercion",
        min(analog_deletions.values()) > 1e-6
        and registration_deleted[REG_VALID] == 1 and cleanup_deleted[REG_WORK] == 1
        and resource_deletion_residual == math.sqrt(2.0)
        and malformed == len(actions),
        {"analog_Givens_deletion_residuals": analog_deletions,
         "deleted_invalid7_exclusion_wrongly_admitted": registration_deleted[REG_VALID],
         "deleted_cleanup_work_leakage": cleanup_deleted[REG_WORK],
         "resource_CNOT_deletion_basis_residual": resource_deletion_residual,
         "malformed_refusals": malformed, "analog_schedule_SHA256": schedule_digest},
    )
    return {"analog": analog_deletions, "resource": resource_deletion_residual,
            "malformed": malformed, "analog_digest": schedule_digest}


def covariance_locality_resource_controls(programs, registration, route_c) -> dict[str, object]:
    print("\nALL24 / ALL576 / LOCALITY / RESOURCE")
    frames = c531.c526.c235.proper_cubic_frames()
    line = tuple(np.asarray((site, 0, 0), dtype=int) for site in range(MENU_COMPILER_M2))
    edge_failures = 0
    for frame in frames:
        moved = tuple(frame @ point for point in line)
        edge_failures += sum(int(np.abs(right - left).sum() != 1) for left, right in zip(moved[:-1], moved[1:]))
        edge_failures += int(round(np.linalg.det(frame)) != 1)
    composition_failures = 0
    sample_sites = (0, MENU_COMPILER_M2 // 2, MENU_COMPILER_M2 - 1)
    current_failures = 0
    currents = ((0, 0), (1, 0), (0, 1), (1, 1))
    for first in frames:
        for second in frames:
            combined = second @ first
            for site in sample_sites:
                point = line[site]
                composition_failures += int(not np.array_equal(second @ (first @ point), combined @ point))
            for axis in range(3):
                for rails in currents:
                    axis1, rails1 = c552.frame_current(axis, rails, first)
                    axis2, rails2 = c552.frame_current(axis1, rails1, second)
                    axisc, railsc = c552.frame_current(axis, rails, combined)
                    current_failures += int((axis2, rails2) != (axisc, railsc))

    analog_schedule = tuple(item for program in programs for item in program.schedule)
    register_trace = registration["trace"]
    resource_schedule_local = route_c["schedule"]
    maximum_support = max(
        register_trace["maximum_support_M2"],
        max(len(item.sites) for item in resource_schedule_local),
        2,
    )
    analog_nn = sum(item.sites[1] == item.sites[0] + 1 for item in analog_schedule)
    digest = sha256()
    digest.update(register_trace["sha256"].encode())
    for item in analog_schedule:
        digest.update(f"A:{item.sites}:{item.label}:{item.matrix}".encode())
    for item in resource_schedule_local:
        digest.update(f"C:{item.kind}:{item.sites}:{item.label}".encode())
    check(
        "the 125-M2 finite compiler has literal support at most two and covariant line carriage through all24 and all576 frame products",
        len(frames) == 24 and edge_failures == composition_failures == current_failures == 0
        and maximum_support == 2 and analog_nn == len(analog_schedule)
        and all(abs(item.sites[0] - item.sites[1]) == 1 for item in resource_schedule_local),
        {"proper_cubic_frames": len(frames), "ordered_frame_products": len(frames) ** 2,
         "mapped_line_edge_failures": edge_failures, "composition_failures": composition_failures,
         "oriented_current_group_failures": current_failures,
         "registration_M2": REG_M2, "analog_M2": ANALOG_M2, "resource_M2": RESOURCE_M2,
         "menu_compiler_M2": MENU_COMPILER_M2, "Cycle552_interface_M2": c552.TOTAL_M2,
         "bounded_product_envelope_M2": MENU_COMPILER_M2 + c552.TOTAL_M2,
         "maximum_literal_support_M2": maximum_support,
         "analog_adjacent_Givens": len(analog_schedule),
         "resource_adjacent_CNOTs": len(resource_schedule_local),
         "compiler_trace_SHA256": digest.hexdigest()},
    )
    return {"frames": len(frames), "products": len(frames) ** 2,
            "edge_failures": edge_failures, "composition_failures": composition_failures,
            "current_failures": current_failures, "trace_sha256": digest.hexdigest(),
            "maximum_support": maximum_support}


def no_go_inventory_controls(started: float) -> None:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8 CLAIM GATE")
    n1 = (
        ("ternary effect-menu Naimark", "effect partition / Stinespring isometry / physical menu output", "ATTEMPTED — POSITIVE FINITE"),
        ("mixed-projective split/merge", "presentation pieces / effect-functional quotient and additivity / decomposition-independent grade", "ATTEMPTED — POSITIVE FINITE"),
        ("scaled-projector conserved split", "coefficient quanta / reversible partition conservation / refinement-independent ray grade", "ATTEMPTED — POSITIVE FINITE"),
        ("fixed local menu registration", "program word / reversible finite predicate / admitted pointer dilation", "RULED IN BY PRIOR — Cycle384 positive"),
        ("retained coherent instrument pointer", "Kraus sectors / common FORM control / one objective member", "RULED IN ONLY AS COHERENT BY PRIOR — Cycle493"),
        ("deterministic member-law cell", "one-hot member carrier / fixed recurrence / exact conditional occurrence", "ATTEMPTED THROUGH RETAINED CYCLE552 — POSITIVE CONDITIONAL"),
        ("objective stochastic member source", "local innovation carrier / law-owned member and receipt / calibrated actual corpus", "OPEN"),
    )
    walls = ("finite-menu eligibility/genesis", "selected grade functional", "objective member production",
             "framework Record formation", "Born/frequency calibration")
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "seven-program whitelist and block-position code", "blank registration/work/pointer/resource banks",
        "continuous effects, rays, coefficients, square roots and Givens schedules", "supplied rho trace functional",
        "fine presentation tags and quotient level", "Cycle552 law word and initial member state",
        "Cycle531 edge/binding/K ports", "finite noiseless gates and proper-cubic chart",
    )
    n4 = (
        ("PR5472 effect horn", "conditional E1/E2 finite-effect forcing", "finite ternary Naimark realization only", False),
        ("PR5476 scaled family", "conditional F1/F2 family forcing", "two rational resource splits only", False),
        ("PR5479 mixed family", "conditional X1 forcing and merge functionality", "three finite presentations and one supplied functional", True),
        ("Cycle383", "coarse-effect/CP quotient and visible fine tags", "same decomposition/refinement separator", True),
        ("Cycle384", "six-label local registration E/G", "seven-label finite predicate E/G", True),
        ("Cycles531/552", "independent member/receipt then conditional occurrence", "same exact typed interface", True),
    )
    n5 = (
        ("per-effect/per-menu", "tested on seven finite programs", "positive algebraic and compiler claims only"),
        ("per-presentation", "three mixed presentations", "fine context remains visible"),
        ("per-cell", "125-M2 menu compiler plus typed Cycle552 product interface", "bounded positive"),
        ("held family", "rotated trine, alternative decomposition/refinement, resource refinement", "positive"),
        ("lattice-wide/continuum/corpus", "untested", "no negative or Born claim"),
    )
    n6 = (
        "physically generate and enroll a broader menu family rather than supply the whitelist",
        "derive one grade functional from an operational symmetry or law and audit its domain",
        "build an objective member source that emits the exact Cycle552/Cycle531 type",
        "add framework formation-close-commit-permanence without relabeling pointer copies",
        "compare blinded realized Record frequencies with the separately derived algebraic grade",
    )
    n7 = (
        "A hostile constructive reviewer should join the finite Naimark carrier to a local decohering or objective stochastic apparatus whose retained environment emits one stable typed MEMBER and law receipt, then feed the unchanged Cycle552/531 binder and a non-erasing Record medium. If an independently selected effect-functional grade controls that law and a held-size frequency theorem survives contextual refinements, the present weight/occurrence separation can be bridged without an axiom edit. The terminal obligations are physical menu genesis, one actuality owner, retained outgoing correlations, Record permanence, and blinded calibration; none is excluded here."
    )
    n8 = (
        "Cycles382/384 turned finite table membership into a physical local compiler without universal eligibility",
        "Cycle383 separated effect functionality from visible fine context and CP futures",
        "Cycles478/493 made coherent and conditional menu carriers physical without one actual member",
        "Cycles531/552 retired conditional binder and recurrent member wiring after supplied genesis",
        "closed PR5472/5476/5479 sharpen conditional forcing families but remain unmerged and nonselecting",
    )
    supplied = (
        "seven finite eligible menu programs and program/block code",
        "effects, coefficients, rho grade functional, square roots, quotient/grouping and compile-time Givens",
        "blank registration/work/resource banks and finite routing chart",
        "Cycle531 edge/binding/K interface and Cycle552 law/member genesis",
        "noiseless finite domain, tolerances and frame convention",
    )
    derived = (
        "bounded seven-label registration and literal one/two-M2 compiler",
        "ternary Naimark E/G, inverse, context covariance and held menu",
        "mixed effect/grade decomposition invariance plus CP/fine-context separator",
        "resource-conserving scaled-ray split and refinement invariance",
        "exact conditional occurrence interface after independent member supply",
        "deletions, leakage/domain refusal, all24 and all576 carriage",
    )
    open_items = (
        "universal/autonomous menu-family eligibility and continuous coefficient genesis",
        "physical selection or derivation of a grade functional and its numerical values",
        "objective member production tied to the grade rather than supplied law state",
        "framework Record formation, realized history and permanent medium",
        "Born calibration, sampling, independence and empirical frequency theorem",
        "unbounded noisy cubic tiling and resource renewal",
    )
    elapsed = time.monotonic() - started
    check(
        "full N1-N8 keeps finite constructive gains separate from member occurrence and rejects broad no-go, minimum-content, and axiom-pressure promotion",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 8 and len(n4) == 6
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 400 and len(n8) == 5
        and elapsed < WALL_CAP_SECONDS and rss_bytes() < RSS_CAP_BYTES,
        {"N1_normalized_routes": n1, "N2_pairwise_walls": n2,
         "N3_hidden_condition_scan": n3, "N4_residual_matching": n4,
         "N5_rhetoric_resolution": n5, "N6_partial_closure_paths": n6,
         "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
         "supplied": supplied, "derived": derived, "open": open_items,
         "broad_no_go": "FAIL / DO NOT SHIP", "minimum_content": False,
         "shared_obstruction": False, "axiom_pressure": False,
         "authority": AUTHORITY, "audit": AUDIT,
         "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_bytes": rss_bytes(), "rss_cap_bytes": RSS_CAP_BYTES,
         "six_wall_ledger": {
             "C_ref": "finite eligibility and interface labels explicit; family/grade/member genesis supplied",
             "C_num": "exact finite effects/grades and floating E-G residuals; no selected probability/calibration",
             "C_wrap": "conditional occurrence reached only after supplied member; no Record/history/time",
             "C_int": "one-site menu mechanisms only; no phase-energy or generator-frequency promotion",
             "C_local": "125-M2 compiler plus exact 276-M2 typed interface; tiling/renewal/noise open",
             "C_source": "unchanged; no energy-stress/gravity source law",
         }},
    )


def install_wall_cap() -> None:
    if hasattr(signal, "SIGALRM"):
        def alarm(_signum, _frame):
            raise TimeoutError("Cycle565 exceeded its wall cap")
        signal.signal(signal.SIGALRM, alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    install_wall_cap()
    print("Cycle565 physical Born-menu compiler / occurrence-interface tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        dependency_and_note_controls()
        registration = registration_controls()
        programs = build_analog_programs()
        analog_square_controls(programs, registration)
        route_a_controls(programs)
        route_b_controls(programs)
        route_c = route_c_controls(registration)
        occurrence_interface_controls()
        deletion_and_domain_controls(programs)
        covariance_locality_resource_controls(programs, registration, route_c)
        no_go_inventory_controls(started)
    except Exception as exc:
        check("Cycle565 runner completed without exception", False, repr(exc))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
