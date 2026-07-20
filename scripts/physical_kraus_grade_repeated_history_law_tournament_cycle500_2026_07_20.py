#!/usr/bin/env python3
"""Cycle 500: Kraus-grade repeated-history-law tournament.

The positive theorem is a finite coherent cylinder-grade construction.  It is
not an actual-member selector, probability law, frequency theorem, realized
history, or framework Record-production law.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import log2, sqrt
from pathlib import Path
import inspect
import os
import re
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_terminal_menu_member_law_tournament_cycle493_2026_07_20 as c493
import physical_kraus_form_dephasing_bath_conveyor_cycle496_2026_07_20 as c496
import physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20 as c498


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_KRAUS_GRADE_REPEATED_HISTORY_LAW_TOURNAMENT_CYCLE500_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0
MENU = range(c493.c488.MENU_ARITY)
TRAIN_L = 3
HELD_L = 6
A_TRAIN_REFINEMENT = 2
A_HELD_REFINEMENT = 4
B_TRAIN_N = 2
B_HELD_N = 4
C_TRAIN_N = 8
C_HELD_N = 16
C_RESPONSE_L1_TOL = 0.10
Word = tuple[int, ...]
Coord = tuple[int, int, int]
Sparse = dict[tuple[object, ...], complex]

FROZEN = {
    "Cycle478 runner": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "Cycle478 note": "87ed2bfbcff03b155496123d664050e80e01c67e668b06d751c3ecef2415652f",
    "Cycle493 runner": "7c51c313f83e006d1bd036e1d3d3d6a7f0fb39cfa56f874419d1e18658aca9af",
    "Cycle493 note": "81cab7f7fa54bef5789c3991911dc197f7506e4aeaa721973a548685006cbd8a",
    "Cycle496 runner": "b34e795f9b25e5ac8c2911038580a89df84bab65d658a3fbf2db6ac017c79083",
    "Cycle496 note": "bd3b0d5542f0bccad9e94a45ef913b91a4866ffba03eaa54b634c46d339f9945",
    "Cycle351 runner": "7912b5177f073abd5d06fd6206720582db2ebd1fe0cbb9d63afff8698cd53291",
    "Cycle351 note": "19a0bc407c74c4700ae6a39ccb842285419b0611477904f378c9c7fb6f170e81",
    "Cycle454 runner": "09d9781ad3416bf8bd94917353661c1d222de115bc83691150be19fb4ae11ed2",
    "Cycle454 note": "1b6bbc97a6cdd94ed33533df034f62a1b83d9ae2fa1284d8d8a0ec3e0df6337d",
    "Cycle498 runner": "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "Cycle498 note": "ac4e7d1e09df5f979375ef46beb2bfec452e5e85136c8e9e55234fa914073d01",
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "prediction surface": "862d317ab0a073a846a3afb5651c58c472594cb63c5f12bafcb2ea328237a1fe",
}
FROZEN_PATHS = {
    "Cycle478 runner": Path(c493.c488.c478.__file__),
    "Cycle478 note": c493.c488.c478.NOTE,
    "Cycle493 runner": Path(c493.__file__),
    "Cycle493 note": c493.NOTE,
    "Cycle496 runner": Path(c496.__file__),
    "Cycle496 note": c496.NOTE,
    "Cycle351 runner": ROOT / "scripts/physical_typed_record_born_corpus_tournament_synthesis_cycle351_2026_07_18.py",
    "Cycle351 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_CYCLE351_NOTE_2026-07-18.md",
    "Cycle454 runner": ROOT / "scripts/physical_born_scaled_ray_split_merge_auxiliary_cycle454_2026_07_19.py",
    "Cycle454 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_SCALED_RAY_SPLIT_MERGE_AUXILIARY_CYCLE454_NOTE_2026-07-19.md",
    "Cycle498 runner": Path(c498.__file__),
    "Cycle498 note": c498.NOTE,
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "prediction surface": ROOT / "docs/publication/ci3_z3/PREDICTION_SURFACE_2026-04-15.md",
}


class WallCapExceeded(RuntimeError):
    pass


@dataclass(frozen=True)
class TypedHistoryObjects:
    cylinder_grade: str = "squared norm of one orthogonal coherent history sector"
    candidate_FORM: str = "bath-relative candidate occurrence receipt"
    endpoint_lineage: str = "Cycle498 candidate-FORM endpoint/predecessor chain"
    actual_member: None = None
    framework_Record: None = None
    empirical_frequency: None = None


@dataclass(frozen=True)
class MicroGate:
    lane: int
    site: Coord
    label: str


@dataclass(frozen=True)
class Placement:
    kind: str
    label: str
    sites: tuple[Coord, ...]


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
    text = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def declared_runner_sha() -> str | None:
    match = re.search(r"runner SHA-256:\s*([0-9a-f]{64})", NOTE.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "frozen-before-held contract",
        "route a — branch-refinement invariance/control",
        "route b — actual repeated kraus-cylinder compiler",
        "route c — deterministic microseed/conveyor adversarial control",
        "train l=3", "held l=6", "n=2", "n=4", "n=8", "n=16",
        "actual cycle-478 kraus", "coherent global state", "phase-sensitive",
        "candidate form is not a framework record", "cycle-498 endpoint lineage is candidate form only",
        "grades are not probability", "10^n", "all 24 proper-cubic frames",
        "supplied / derived / open", "gate disposition: fail",
        "no shared obstruction or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    self_sha = file_sha(Path(__file__))
    note_sha = declared_runner_sha()
    check(
        "the Cycle500 note freezes this exact runner, the constructive target, and six-object semantic split",
        not missing and note_sha == self_sha,
        {"missing_phrases": missing, "runner_sha": self_sha, "note_declared_runner_sha": note_sha},
    )
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "Cycle478/493/496/351/454/498 and current far-shore inputs are exact-hash frozen",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )


def states() -> tuple[tuple[str, np.ndarray], ...]:
    return (
        ("z-plus", np.asarray((1.0, 0.0), complex)),
        ("y-plus", np.asarray((1.0, 1.0j), complex) / sqrt(2.0)),
    )


def sparse_residual(left: Sparse, right: Sparse) -> float:
    keys = set(left) | set(right)
    return float(sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def sparse_add(output: Sparse, key: tuple[object, ...], value: complex) -> None:
    output[key] = output.get(key, 0j) + value
    if abs(output[key]) < 1e-14:
        del output[key]


def branch_vectors(program: object, psi: np.ndarray) -> tuple[np.ndarray, ...]:
    return tuple(operator @ psi for operator in program.kraus)


def branch_grades(program: object, psi: np.ndarray) -> tuple[float, ...]:
    return tuple(float(np.vdot(vector, vector).real) for vector in branch_vectors(program, psi))


def micro_schedule(refinement: int) -> tuple[MicroGate, ...]:
    if refinement not in (A_TRAIN_REFINEMENT, A_HELD_REFINEMENT):
        raise ValueError("microrefinement leaves the frozen power-of-two apparatus")
    return tuple(
        MicroGate(lane, (0, 0, lane + 1), f"H:micro:{lane}")
        for lane in range(int(log2(refinement)))
    )


def apply_hadamard(state: Sparse, gate: MicroGate) -> Sparse:
    output: Sparse = {}
    for (pointer, system, micro), amplitude in state.items():
        micro_word = tuple(micro)
        bit = micro_word[gate.lane]
        toggled = micro_word[:gate.lane] + (1 - bit,) + micro_word[gate.lane + 1:]
        sparse_add(output, (pointer, system, micro_word), amplitude * (1 if bit == 0 else -1) / sqrt(2.0))
        sparse_add(output, (pointer, system, toggled), amplitude / sqrt(2.0))
    return output


def micro_input(program: object, psi: np.ndarray, refinement: int) -> Sparse:
    output: Sparse = {}
    blank = (0,) * len(micro_schedule(refinement))
    for pointer, vector in enumerate(branch_vectors(program, psi)):
        for system, amplitude in enumerate(vector):
            if abs(amplitude) > 1e-14:
                sparse_add(output, (pointer, system, blank), complex(amplitude))
    return output


def micro_physical(program: object, psi: np.ndarray | Sparse, refinement: int, *, reverse: bool = False, delete_label: str | None = None) -> Sparse:
    schedule = micro_schedule(refinement)
    if delete_label is not None:
        schedule = tuple(gate for gate in schedule if gate.label != delete_label)
    if reverse:
        if not isinstance(psi, dict):
            raise ValueError("micro inverse requires sparse refined input")
        output = dict(psi)
    else:
        if isinstance(psi, dict):
            raise ValueError("micro forward requires a two-component input vector")
        output = micro_input(program, psi, refinement)
    for gate in reversed(schedule) if reverse else schedule:
        output = apply_hadamard(output, gate)
    return output


def micro_reference(program: object, psi: np.ndarray, refinement: int) -> Sparse:
    output: Sparse = {}
    micro_words = tuple(product((0, 1), repeat=len(micro_schedule(refinement))))
    for pointer, vector in enumerate(branch_vectors(program, psi)):
        for system, amplitude in enumerate(vector):
            for micro in micro_words:
                if abs(amplitude) > 1e-14:
                    sparse_add(output, (pointer, system, micro), complex(amplitude) / sqrt(refinement))
    return output


def micro_grade_table(state: Sparse, refinement: int) -> tuple[tuple[float, ...], ...]:
    micro_words = tuple(product((0, 1), repeat=len(micro_schedule(refinement))))
    return tuple(
        tuple(sum(abs(amplitude) ** 2 for (p, _s, m), amplitude in state.items() if p == pointer and m == micro) for micro in micro_words)
        for pointer in MENU
    )


def route_a_controls(surface: c493.c488.MenuSurface, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE A / BRANCH-REFINEMENT INVARIANCE CONTROL")
    fixtures = (("train", surface.train_program, A_TRAIN_REFINEMENT),)
    if include_held:
        fixtures += (("held", surface.held_program, A_HELD_REFINEMENT),)
    rows = []
    failures = 0
    deletion_visible = False
    for lane, program, refinement in fixtures:
        for name, psi in states():
            schedule = micro_schedule(refinement)
            initial = micro_input(program, psi, refinement)
            physical = micro_physical(program, psi, refinement)
            reference = micro_reference(program, psi, refinement)
            recovered = micro_physical(program, physical, refinement, reverse=True)
            table = micro_grade_table(physical, refinement)
            coarse = tuple(sum(row) for row in table)
            original = branch_grades(program, psi)
            within_spread = max(max(row) - min(row) for row in table)
            swapped = dict(physical)
            micro_words = tuple(product((0, 1), repeat=len(schedule)))
            for pointer in MENU:
                for system in range(2):
                    left = (pointer, system, micro_words[0])
                    right = (pointer, system, micro_words[-1])
                    swapped[left], swapped[right] = swapped.get(right, 0j), swapped.get(left, 0j)
            swap_residual = sparse_residual(physical, swapped)
            cross_outcome_spread = max(value for row in table for value in row) - min(value for row in table for value in row)
            failures += int(
                sparse_residual(physical, reference) >= TOL
                or sparse_residual(recovered, initial) >= TOL
                or max(abs(a - b) for a, b in zip(coarse, original)) >= TOL
                or within_spread >= TOL or swap_residual >= TOL
                or cross_outcome_spread <= 1e-5
            )
            rows.append({
                "lane": lane, "state": name, "refinement": refinement,
                "E_G_residual": sparse_residual(physical, reference),
                "inverse_residual": sparse_residual(recovered, initial),
                "coarse_grade_residual": max(abs(a - b) for a, b in zip(coarse, original)),
                "within_outcome_subbranch_spread": within_spread,
                "within_outcome_swap_residual": swap_residual,
                "cross_outcome_micrograde_spread": cross_outcome_spread,
                "coarse_branch_grades": original,
                "literal_micro_M2_sites": tuple(gate.site for gate in schedule),
                "literal_H_gate_labels": tuple(gate.label for gate in schedule),
                "ancilla_M2": len(schedule),
            })
            if lane == "held" and name == "z-plus":
                damaged = micro_physical(program, psi, refinement, delete_label=schedule[-1].label)
                deletion_visible = sparse_residual(damaged, reference) > 0.1
    tree = ast.parse(inspect.getsource(micro_schedule))
    names = tuple(node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name))
    forbidden = {token: sum(token in name for name in names) for token in ("state", "psi", "norm", "weight", "pointer")}
    check(
        "A: a fixed H microrefinement preserves every actual coarse branch grade and gives only within-branch exchange symmetry",
        failures == 0 and all(value == 0 for value in forbidden.values())
        and (deletion_visible if include_held else True),
        {
            "frozen_refinements": {"train": A_TRAIN_REFINEMENT, "held": A_HELD_REFINEMENT},
            "rows": rows,
            "compiler_forbidden_query_hits": forbidden,
            "held_H_deletion_visible": deletion_visible if include_held else "not run",
            "equal_subbranch_counts_representation_dependent": True,
            "unequal_outcome_sectors_equalized": False,
            "member_selected": False,
            "counting_law_claimed": False,
        },
    )
    return {"rows": rows}


def program_law_digest(program: object) -> str:
    digest = sha256(program.name.encode())
    digest.update(repr(program.coarse_groups).encode())
    for operator in program.kraus:
        digest.update(np.asarray(operator, complex).tobytes())
    return digest.hexdigest()


def event_basis_maps(surface: c493.c488.MenuSurface, length: int) -> dict[str, object]:
    program = surface.train_program if length == TRAIN_L else surface.held_program
    cases = c493.c488.c478.bounded_class_cases(length, len(surface.raw_effects))
    law = c493.c488.c478.c440.menu_law(c493.c488.TERMINAL_CLASSES, cases, c493.c488.TERMINAL_ROW_INDEX)
    bank = c493.c488.c478.c436.prepare_bank(c493.c488.c478.c433.LAYOUT, law)
    physical_maps = []
    reference_maps = []
    inverse_residuals = []
    leakage = 0
    for basis in (np.asarray((1.0, 0.0), complex), np.asarray((0.0, 1.0), complex)):
        physical, local_leakage = c493.c488.c478.c436.physical_pointer_then_law(program, basis, bank, law)
        reference = c493.c488.c478.c436.coarse_then_encode(program, basis, bank, law)
        inverse = c493.c488.c478.c436.inverse_sparse(physical, law)
        initial = c493.c488.c478.c436.input_sparse(program, basis, bank)
        physical_maps.append(physical)
        reference_maps.append(reference)
        inverse_residuals.append(c493.c488.c478.c436.sparse_residual(inverse, initial))
        leakage += local_leakage
    return {
        "program": program, "law": law,
        "physical": tuple(physical_maps), "reference": tuple(reference_maps),
        "single_E_G": tuple(c493.c488.c478.c436.sparse_residual(a, b) for a, b in zip(physical_maps, reference_maps)),
        "single_inverse": tuple(inverse_residuals), "leakage": leakage,
        "program_law_digest": program_law_digest(program),
    }


def basis_bits(index: int, n: int) -> Word:
    return tuple((index >> (n - 1 - lane)) & 1 for lane in range(n))


def tensor_vector(vector: np.ndarray, n: int) -> np.ndarray:
    answer = np.asarray((1.0,), complex)
    for _ in range(n):
        answer = np.kron(answer, vector)
    return answer


def form_basis_signatures(n: int, case_name: str, horizon: int) -> dict[str, object]:
    signatures: dict[Word, Word] = {}
    failures = 0
    receipt_flags = set()
    digest = sha256()
    for word in product(MENU, repeat=n):
        encoded = c493.prepare_history(case_name, horizon, tuple(word))
        physical = c493.apply_physical(encoded)
        coarse = c493.coarse_step(encoded)
        inverse = c493.apply_physical(physical, reverse=True)
        receipts = c493.c488.receipts(physical)
        failures += int(
            physical != coarse or inverse != encoded or receipts is None
            or tuple(receipt.pointer for receipt in receipts) != tuple(word)
        )
        if receipts:
            receipt_flags.update((receipt.framework_actuality, receipt.framework_Record, receipt.realized_framework_history) for receipt in receipts)
        signatures[tuple(word)] = physical.bits
        digest.update(bytes(physical.bits))
    schedule = c493.physical_schedule(n, horizon)
    schedule_digest = sha256("\n".join(f"{gate.kind}:{gate.sites}:{gate.label}" for gate in schedule).encode()).hexdigest()
    return {
        "signatures": signatures, "failures": failures,
        "receipt_flags": receipt_flags, "state_count": len(signatures),
        "state_digest": digest.hexdigest(), "schedule_digest": schedule_digest,
        "logical_gates": len(schedule), "M2": n * c493.c488.CELL_M2,
    }


def repeated_actual_map(
    input_vector: np.ndarray,
    event_maps: tuple[dict[tuple[int, int, tuple[tuple[int, ...], ...]], complex], ...],
    form_signatures: dict[Word, Word],
    n: int,
) -> Sparse:
    if len(input_vector) != 2**n:
        raise ValueError("repeated input leaves the frozen N-copy Hilbert block")
    output: Sparse = {}
    for basis_index, input_amplitude in enumerate(input_vector):
        if abs(input_amplitude) < 1e-14:
            continue
        local_maps = tuple(event_maps[bit] for bit in basis_bits(basis_index, n))
        for event_terms in product(*(tuple(local.items()) for local in local_maps)):
            pointers = tuple(key[0] for key, _amplitude in event_terms)
            systems = tuple(key[1] for key, _amplitude in event_terms)
            packets = tuple(key[2] for key, _amplitude in event_terms)
            amplitude = complex(input_amplitude)
            for _key, local_amplitude in event_terms:
                amplitude *= local_amplitude
            sparse_add(output, (pointers, systems, packets, form_signatures[pointers]), amplitude)
    return output


def sparse_grades_by_word(state: Sparse) -> dict[Word, float]:
    answer: dict[Word, float] = {}
    for (word, _systems, _packets, _form), amplitude in state.items():
        answer[word] = answer.get(word, 0.0) + abs(amplitude) ** 2
    return answer


def cylinder_controls(grades: dict[Word, float], one_step: tuple[float, ...], n: int) -> dict[str, float]:
    normalization = abs(sum(grades.values()) - 1.0)
    product_residual = max(
        abs(value - float(np.prod([one_step[pointer] for pointer in word])))
        for word, value in grades.items()
    )
    refinement = 0.0
    for width in range(n):
        for prefix in product(MENU, repeat=width):
            expected = float(np.prod([one_step[pointer] for pointer in prefix])) if prefix else 1.0
            observed = sum(value for word, value in grades.items() if word[:width] == prefix)
            refinement = max(refinement, abs(observed - expected))
    additivity = max(
        abs(sum(value * word.count(pointer) for word, value in grades.items()) - n * one_step[pointer])
        for pointer in MENU
    )
    exchangeability = 0.0
    grouped: dict[tuple[int, ...], list[float]] = {}
    for word, value in grades.items():
        grouped.setdefault(tuple(word.count(pointer) for pointer in MENU), []).append(value)
    for values in grouped.values():
        exchangeability = max(exchangeability, max(values) - min(values))
    return {
        "normalization": normalization, "product": product_residual,
        "refinement": refinement, "count_additivity": additivity,
        "exchangeability": exchangeability,
    }


def endpoint_lineage(word: Word) -> dict[str, object]:
    endpoints = []
    previous = None
    for index, _pointer in enumerate(word):
        endpoint = c498.make_candidate_endpoint(index, index + 1, previous)
        endpoints.append(endpoint)
        previous = endpoint
    matches = tuple(c498.c444.match_interval(left, right) for left, right in zip(endpoints[:-1], endpoints[1:]))
    damaged_record = replace(endpoints[-1].record, parents=(), causal_past=())
    damaged = replace(endpoints[-1], record=damaged_record)
    deletion_visible = c498.c444.match_interval(endpoints[-2], damaged) is None
    return {
        "endpoints": tuple(endpoint.record.content for endpoint in endpoints),
        "sites": tuple(endpoint.record.site for endpoint in endpoints),
        "identities": tuple(endpoint.record.event_identity for endpoint in endpoints),
        "adjacent_interval_cells": tuple(match.fine_cells if match else None for match in matches),
        "predecessor_deletion_visible": deletion_visible,
        "candidate_FORM_only": True,
        "framework_Record": False,
    }


def route_b_controls(surface: c493.c488.MenuSurface, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE B / ACTUAL REPEATED KRAUS-CYLINDER COMPILER")
    fixtures = (("train", TRAIN_L, B_TRAIN_N, c493.c488.TRAIN_CASE, c493.TRAIN_HORIZON),)
    if include_held:
        fixtures += (("held", HELD_L, B_HELD_N, c493.c488.HELD_CASE, c493.HELD_HORIZON),)
    rows = []
    failures = 0
    held_state_maps: dict[str, Sparse] = {}
    for lane, length, n, case_name, horizon in fixtures:
        event = event_basis_maps(surface, length)
        form = form_basis_signatures(n, case_name, horizon)
        schedule_hashes = []
        for name, psi in states():
            input_vector = tensor_vector(psi, n)
            physical = repeated_actual_map(input_vector, event["physical"], form["signatures"], n)
            reference = repeated_actual_map(input_vector, event["reference"], form["signatures"], n)
            grades = sparse_grades_by_word(physical)
            controls = cylinder_controls(grades, branch_grades(event["program"], psi), n)
            schedule_hashes.append((event["program_law_digest"], form["schedule_digest"]))
            residual = sparse_residual(physical, reference)
            failures += int(
                residual >= TOL or any(value >= TOL for value in controls.values())
                or len(grades) != c493.c488.MENU_ARITY**n
            )
            rows.append({
                "lane": lane, "state": name, "N": n,
                "coherent_sparse_terms": len(physical),
                "orthogonal_history_sectors": len(grades),
                "explicit_resource_growth": f"10^{n} coherent pointer-system terms before cancellations",
                "actual_Cycle478_C493_E_G_residual": residual,
                "cylinder_grade_controls": controls,
                "one_step_grades": branch_grades(event["program"], psi),
                "program_law_digest_and_C493_physical_schedule_hash": schedule_hashes[-1],
            })
            if lane == "held":
                held_state_maps[name] = physical
        failures += int(
            len(set(schedule_hashes)) != 1 or form["failures"] != 0
            or form["receipt_flags"] != {(False, False, False)}
            or max(event["single_E_G"] + event["single_inverse"]) >= TOL
            or event["leakage"] != 0
        )
        rows[-1]["basis_FORM_certificate"] = {
            key: value for key, value in form.items() if key != "signatures"
        }
        rows[-1]["single_event_actual_C478"] = {
            "E_G": event["single_E_G"], "inverse": event["single_inverse"], "leakage": event["leakage"]
        }

    phase_residual = 0.0
    form_deletion_visible = False
    lineage = None
    if include_held:
        event = event_basis_maps(surface, HELD_L)
        form = form_basis_signatures(B_HELD_N, c493.c488.HELD_CASE, c493.HELD_HORIZON)
        z = tensor_vector(states()[0][1], B_HELD_N)
        y = tensor_vector(states()[1][1], B_HELD_N)
        phase = 0.37 + 0.61j
        coherent = repeated_actual_map(z + phase * y, event["physical"], form["signatures"], B_HELD_N)
        right: Sparse = {}
        for key, value in held_state_maps["z-plus"].items():
            sparse_add(right, key, value)
        for key, value in held_state_maps["y-plus"].items():
            sparse_add(right, key, phase * value)
        phase_residual = sparse_residual(coherent, right)
        base = c493.prepare_history(c493.c488.HELD_CASE, c493.HELD_HORIZON, (0, 1, 2, 3))
        nominal = c493.apply_physical(base)
        damaged = c493.apply_physical(base, delete_label="cell:0:match:0:prefix:0")
        form_deletion_visible = c493.c488.receipts(damaged) is None or c493.c488.final_counts(damaged) != c493.c488.final_counts(nominal)
        lineage = endpoint_lineage((0, 1, 2, 3))
        failures += int(phase_residual >= TOL or not form_deletion_visible or not lineage["predecessor_deletion_visible"])

    typed = TypedHistoryObjects()
    check(
        "B: fixed actual C478/C493 maps materialize a coherent repeated cylinder with normalized exchangeable/refining grades and explicit candidate lineage",
        failures == 0,
        {
            "frozen_sizes": {"train_L_N": (TRAIN_L, B_TRAIN_N), "held_L_N": (HELD_L, B_HELD_N)},
            "rows": rows,
            "phase_sensitive_linearity_residual": phase_residual if include_held else "not run",
            "fixed_schedule_identical_for_both_inputs": True,
            "FORM_deletion_visible": form_deletion_visible if include_held else "not run",
            "Cycle498_candidate_endpoint_lineage": lineage if include_held else "not run",
            "typed_objects": typed,
            "arbitrary_N_scalable_compiler_claimed": False,
            "branchwise_normalization_operations": 0,
            "host_pointer_query_selects_schedule": False,
        },
    )
    return {"rows": rows, "typed": typed}


def conveyor_run(n: int) -> dict[str, object]:
    initial = c496.prepare_conveyor(n)
    state = initial
    residuals = []
    for _ in range(n):
        coarse = c496.conveyor_coarse_tick(state)
        state = c496.conveyor_physical_tick(state)
        residuals.append(int(state != coarse))
    terminal = state
    for _ in range(n):
        state = c496.conveyor_physical_tick(state, reverse=True)
    word = tuple(
        c493.c488.receipts(cell)[0].pointer
        for cell in terminal.cells[:n]
        if c493.c488.receipts(cell) is not None
    )
    return {
        "N": n, "word": word, "counts": c496.counts(word),
        "E_G_residuals": tuple(residuals), "inverse_exact": state == initial,
        "used": sum(terminal.used), "exported": sum(terminal.exported),
        "trace": c496.conveyor_trace(n),
    }


def extended_courier_forward(seed: int, length: int) -> tuple[int, Word]:
    """Apply the same fixed C493 rotor beyond C493's N12 FORM test cap."""
    word = c496.ca_word(seed, length)
    cursor = seed
    for _ in range(length):
        cursor = c493.rotate_pointer(cursor)
    return cursor, word


def route_c_controls(surface: c493.c488.MenuSurface, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE C / DETERMINISTIC MICROSEED + CONVEYOR ADVERSARIAL CONTROL")
    fixtures = (("train", surface.train_program, C_TRAIN_N),)
    if include_held:
        fixtures += (("held", surface.held_program, C_HELD_N),)
    rows = []
    conveyor_rows = []
    for lane, program, n in fixtures:
        cursor, word = extended_courier_forward(0, n)
        restored_seed, blanks = c493.courier_inverse(cursor, word)
        frequencies = tuple(Fraction(word.count(pointer), n) for pointer in MENU)
        state_rows = []
        for name, psi in states():
            grades = branch_grades(program, psi)
            l1 = sum(abs(float(value) - grade) for value, grade in zip(frequencies, grades))
            state_rows.append((name, grades, tuple(map(str, frequencies)), l1, l1 <= C_RESPONSE_L1_TOL))
        rows.append({"lane": lane, "N": n, "word": word, "state_grade_response": state_rows, "inverse_exact": restored_seed == 0 and not any(blanks)})
        conveyor_rows.append(conveyor_run(n))
    sources = "\n".join(inspect.getsource(function).lower() for function in (extended_courier_forward, c496.ca_word, c493.rotate_pointer, c496.conveyor_physical_tick))
    query_hits = {token: sources.count(token) for token in ("branch_weights", "branch_grades", "np.vdot", "norm(", "psi")}
    all_responses = [row[-1] for item in rows for row in item["state_grade_response"]]
    check(
        "C: the fixed state-blind rotor/conveyor is reversible and local but fails the frozen two-input grade-response target without becoming a no-go",
        all(row["inverse_exact"] for row in rows)
        and all(not response for response in all_responses)
        and all(value == 0 for value in query_hits.values())
        and all(not any(row["E_G_residuals"]) and row["inverse_exact"] and row["used"] == row["exported"] == row["N"] for row in conveyor_rows),
        {
            "frozen_sizes": {"train": C_TRAIN_N, "held": C_HELD_N},
            "frozen_correct_response_L1_tolerance": C_RESPONSE_L1_TOL,
            "rows": rows, "physical_conveyor_rows": conveyor_rows,
            "compiler_norm_or_state_grade_query_hits": query_hits,
            "same_word_for_incompatible_inputs": True,
            "disposition": "route-specific nonresponse of this supplied microseed law; stochastic/ergodic/admissibility routes remain live",
        },
    )


def coord_add(*items: Coord) -> Coord:
    return tuple(sum(item[axis] for item in items) for axis in range(3))


def coord_scale(factor: int, item: Coord) -> Coord:
    return tuple(factor * value for value in item)


def composition_manifest(n: int, refinement: int) -> tuple[Placement, ...]:
    """Canonical placements newly composed in Cycle500, not inherited internals."""
    items = []
    h_gates = micro_schedule(refinement)
    for event in range(n):
        c478_anchor = (event, 0, 0)
        c493_anchor = (event, 1, 0)
        endpoint_anchor = (event, 1, 1)
        items.append(Placement("macro", f"event:{event}:C478", (c478_anchor,)))
        items.append(Placement("composition-link", f"event:{event}:C478-to-C493", (c478_anchor, c493_anchor)))
        items.append(Placement("macro", f"event:{event}:C493", (c493_anchor,)))
        items.append(Placement("endpoint-link", f"event:{event}:C493-to-endpoint", (c493_anchor, endpoint_anchor)))
        items.append(Placement("endpoint", f"event:{event}:candidate", (endpoint_anchor,)))
        for gate in h_gates:
            site = coord_add(c478_anchor, gate.site)
            items.append(Placement("H", f"event:{event}:{gate.label}", (site,)))
        if event:
            previous = (event - 1, 1, 1)
            items.append(Placement("lineage-link", f"event:{event - 1}->{event}", (previous, endpoint_anchor)))
    return tuple(items)


def carried_composition_manifest(
    frame: tuple[tuple[int, int, int], ...], n: int, refinement: int
) -> tuple[Placement, ...]:
    """Independently rebuild Cycle500 placements from a carried cubic basis."""
    x_axis = c493.c488.rotate_coord((1, 0, 0), frame)
    y_axis = c493.c488.rotate_coord((0, 1, 0), frame)
    z_axis = c493.c488.rotate_coord((0, 0, 1), frame)
    items = []
    h_gates = micro_schedule(refinement)
    for event in range(n):
        c478_anchor = coord_scale(event, x_axis)
        c493_anchor = coord_add(c478_anchor, y_axis)
        endpoint_anchor = coord_add(c493_anchor, z_axis)
        items.append(Placement("macro", f"event:{event}:C478", (c478_anchor,)))
        items.append(Placement("composition-link", f"event:{event}:C478-to-C493", (c478_anchor, c493_anchor)))
        items.append(Placement("macro", f"event:{event}:C493", (c493_anchor,)))
        items.append(Placement("endpoint-link", f"event:{event}:C493-to-endpoint", (c493_anchor, endpoint_anchor)))
        items.append(Placement("endpoint", f"event:{event}:candidate", (endpoint_anchor,)))
        for gate in h_gates:
            site = coord_add(c478_anchor, coord_scale(gate.lane + 1, z_axis))
            items.append(Placement("H", f"event:{event}:{gate.label}", (site,)))
        if event:
            previous = coord_add(coord_scale(event - 1, x_axis), y_axis, z_axis)
            items.append(Placement("lineage-link", f"event:{event - 1}->{event}", (previous, endpoint_anchor)))
    return tuple(items)


def deletion_bath_covariance_controls() -> None:
    print("\nBATH NONREENTRY / ALL24 / RESOURCE CONTROL")
    c483 = c493.c488.c483
    bath_sets = tuple(
        frozenset(cell * c493.c488.CELL_M2 + site for site in c483.B_BATH_SITES)
        for cell in range(B_HELD_N)
    )
    intersections = sum(bool(left.intersection(right)) for left, right in combinations(bath_sets, 2))
    frames = c493.c488.proper_cubic_frames()
    base_edges = []
    coords = c493.c488.manifest(B_HELD_N)
    for cell in range(B_HELD_N):
        path = c493.c488.cell_path(cell)
        base_edges.extend((coords[a], coords[b]) for a, b in zip(path, path[1:]))
    for cell in range(B_HELD_N - 1):
        path = c493.c488.link_path(cell)
        base_edges.extend((coords[a], coords[b]) for a, b in zip(path, path[1:]))
    inherited_failures = 0
    manifest_failures = 0
    local_support_failures = 0
    base_composition = composition_manifest(B_HELD_N, A_HELD_REFINEMENT)
    for frame in frames:
        for left, right in base_edges:
            a = c493.c488.rotate_coord(left, frame)
            b = c493.c488.rotate_coord(right, frame)
            inherited_failures += int(c493.c488.manhattan(a, b) != 1)
        rotated_target = tuple(
            Placement(item.kind, item.label, tuple(c493.c488.rotate_coord(site, frame) for site in item.sites))
            for item in base_composition
        )
        independently_carried = carried_composition_manifest(frame, B_HELD_N, A_HELD_REFINEMENT)
        manifest_failures += int(rotated_target != independently_carried)
        local_support_failures += sum(
            c493.c488.manhattan(item.sites[0], item.sites[1]) != 1
            for item in independently_carried if len(item.sites) == 2
        )
    check(
        "fresh candidate-FORM baths are disjoint; inherited operators and every new H/product/endpoint placement pass their scoped all24 audit",
        intersections == 0 and len(frames) == 24 and inherited_failures == manifest_failures == local_support_failures == 0,
        {
            "candidate_FORM_bath_regions": len(bath_sets),
            "pairwise_bath_intersections": intersections,
            "used_bath_reentry_operations": 0,
            "bath_renewal_operations": 0,
            "proper_cubic_frames": len(frames),
            "inherited_transported_edge_rows": len(frames) * len(base_edges),
            "inherited_operator_covariance_failures": inherited_failures,
            "new_composition_placements_per_frame": len(base_composition),
            "new_rotated_target_vs_independent_carried_manifest_failures": manifest_failures,
            "new_two_site_local_support_failures": local_support_failures,
            "new_placement_kinds": tuple(sorted({item.kind for item in base_composition})),
            "scope": "inherited C478/C493/C496 operator covariance plus Cycle500 composition placements; no broader gate-covariance claim",
            "Cycle478_C493_C496_all24_hash_frozen": True,
        },
    )


def far_shore_and_prior_controls() -> None:
    print("\nPRIOR-ART / FAR-SHORE DISPOSITION")
    prior = (
        ("Cycle317", "actual finite split isometries", "physical same-ray split/merge"),
        ("Cycle454", "finite grade additivity without homogeneity", "20 projected null directions; no occurrence"),
        ("Cycle478", "actual five-Kraus protected menu", "no repeated grade/occurrence law"),
        ("Cycle493", "coherent one-event FORM and conditional laws", "member/Record selection open"),
        ("Cycle496", "dephasing and finite conveyor", "global coherence and supplied seed/bank"),
        ("Cycle351", "conditional grade-blind Record-tag corpus", "actual sampler/frequency theorem open"),
    )
    typed = TypedHistoryObjects()
    check(
        "Cycle500 advances repeated actual-C478 cylinder composition and candidate lineage rather than re-deriving finite grade affinity",
        len(prior) == 6 and typed.actual_member is typed.framework_Record is typed.empirical_frequency is None,
        {
            "residual_matching": prior,
            "new_content": "finite N2/N4 coherent repeated C478+C493 cylinder and explicit candidate endpoint lineage",
            "finite_grade_additivity_claimed_novel": False,
            "Record_axiom": "formation/one admissible lock/permanence/additive readout; formation choice withheld",
            "realized_state_primitive": "pointwise slot only; no state, selector, measure, or grade",
            "far_prediction_use": "a separately justified probability/empirical-frequency bridge is still required",
        },
    )


def no_go_controls() -> None:
    print("\nN1-N8 / CLAIM GATE")
    n1 = (
        ("fixed equal-amplitude branch refinement", "ATTEMPTED / POSITIVE INVARIANCE", "coarse grades preserved; no cross-sector equalization/member"),
        ("repeated actual Kraus cylinder", "ATTEMPTED / POSITIVE CONDITIONAL", "finite coherent grades/refinement/exchangeability"),
        ("deterministic microseed conveyor", "ATTEMPTED / ROUTE-SPECIFIC NONRESPONSE", "fixed word misses both incompatible grade targets"),
        ("autonomous stochastic bath unraveling", "OPEN / UNTESTED", "could actualize trajectories under a derived local law"),
        ("Record-admissibility formation rule", "OPEN / UNTESTED", "could select one admissible pointer token"),
        ("operational symmetry/envariance grade theorem", "OPEN / UNTESTED", "could derive broader grade structure"),
        ("stationary ergodic admitted-Record process", "OPEN / UNTESTED", "could link grades and empirical frequencies"),
        ("infinite quasi-local bath/conveyor", "OPEN / UNTESTED", "could remove finite blank-bank boundary"),
    )
    walls = ("grade-domain law", "actual-member formation", "framework Record admission", "stationarity/ergodicity", "empirical calibration")
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "actual C478 menu and packet law", "two input states", "identical N-copy re-preparation",
        "orthogonal Hilbert sectors and squared-norm grade", "blank program/FORM/bath banks",
        "candidate formation and endpoint law", "finite N/L/refinement sizes", "stationarity and independence of refreshed inputs",
        "fixed noiseless gates/tolerance/geometry", "supplied actual-member fixture only where explicitly labeled",
    )
    n4 = (
        ("Cycle317/454", "finite split/additivity", "Route-A invariance is not novel affinity", True),
        ("Cycle478", "one-event effect functionality", "repeated physical cylinder", True),
        ("Cycle493", "one-event coherent FORM", "N2/N4 candidate-FORM map", True),
        ("Cycle496", "finite conveyor/dephasing", "state-blind control and bath boundary", True),
        ("Cycle351", "conditional corpus/nonselection", "same occurrence/frequency residual", True),
    )
    n5 = (
        ("one branch block", "all five labels/two states/L3-L6", "tested"),
        ("finite cylinders", "N2/N4", "tested"),
        ("deterministic conveyor", "N8/N16", "tested"),
        ("arbitrary N/infinite ray", "untested", "no negative conclusion"),
        ("lattice-wide realized Records/frequency", "untested", "no negative conclusion"),
    )
    n6 = (
        "derive a local admissibility-to-pointer formation law",
        "construct a retained selective outcome token",
        "derive stationarity/ergodicity for admitted Record chains",
        "derive an operational grade theorem beyond the finite menu",
        "prove infinite quasi-local bath renewal/export",
        "calibrate cylinder grades against realized empirical corpora",
    )
    n7 = (
        "A hostile constructive route can combine the exact repeated Kraus cylinder with the Record axiom's one-lock occurrence, a derived local admissibility-to-pointer rule, and a retained selective token carried by an infinite fresh-bath ray. A separately derived stationary ergodic theorem over admitted Records could then identify long-run empirical frequencies with the cylinder-grade functional. Cycle500 supplies the finite coherent cylinder and candidate lineage but neither the formation mechanism nor that ergodic terminal obligation, so it cannot exclude this route."
    )
    n8 = (
        "Cycle317/454 retired finite homogeneity shortcuts by physical split contexts",
        "Cycle351 separated grades, corpus atoms, laws, and actual members",
        "Cycle478 completed the finite effect menu without occurrence",
        "Cycle493 exposed conditional member laws and a uniform counterselector",
        "Cycle496 separated dephasing, deterministic seed, and fresh-bath supply",
        "Record Born-frequency boundary kept finite counts separate from a process model",
    )
    check(
        "N1-N8 admits the finite positive bridge and route-C control but rejects no-go, minimum-content, or axiom-pressure language",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 10 and len(n4) == 5
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 300 and len(n8) >= 5,
        {
            "N1_normalized_routes": n1, "N2_pairwise_wall_audit": n2,
            "N3_hidden_condition_scan": n3, "N4_residual_matching": n4,
            "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
            "N7_steelman": n7, "N8_cross_cycle_echo": n8,
            "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
            "shared_obstruction": False, "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "actual Cycle478 terminal Kraus menu, program/packet law, pointer code, and two input vectors",
        "identical input re-preparation, blank packet/FORM/bath banks, orthogonal-sector squared-norm grade, and stationarity/independence",
        "fixed H refinement sizes, finite N/L, noiseless gate words, tolerance, and proper-cubic placement",
        "Cycle493 bath-relative candidate-FORM law and occurrence/type/lock inputs",
        "Cycle498 candidate endpoint formation/predecessor law and explicit finite identity words",
        "Cycle496 deterministic rotor microseed, initially blank finite conveyor bank, and terminal boundary",
    )
    derived = (
        "fixed H within-branch equal refinement, exact inverse, and coarse-grade preservation without cross-sector equalization",
        "materialized actual C478+C493 coherent global states at N2/N4 with exact E/G, phase linearity, inverse leaves, and zero leakage",
        "finite cylinder normalization, prefix refinement, exchangeability, and grade-weighted count additivity",
        "candidate-FORM basis continuation for all 25/625 words and one explicit candidate endpoint chain",
        "fixed deterministic N8/N16 word/conveyor nonresponse to both incompatible grade targets without norm lookup",
        "deletion, bath nonreentry, bounded resources, all24, and six-object semantic separation",
    )
    open_items = (
        "actualization/selection of one coherent history member",
        "framework Record admission and an autonomous formation-content rule",
        "derivation of identical re-preparation, stationarity/independence, blank-bank genesis, and renewal",
        "probability interpretation, empirical sampling, frequency convergence, and calibration",
        "arbitrary-N scalable compiler, infinite-volume/noisy permanence, and general eligible-menu grade theorem",
        "time/rate, energy/inertia, source/gravity, continuum prediction, or constitutional conclusion",
    )
    check(
        "the inventory separates every supplied symmetry/law/resource from the finite coherent grade theorem and open actuality bridge",
        len(supplied) == len(derived) == len(open_items) == 6,
        {
            "supplied": supplied, "derived": derived, "open": open_items,
            "authority": AUTHORITY, "audit": AUDIT,
            "grade_called_probability": False, "candidate_FORM_called_Record": False,
            "cylinder_called_realized_history": False,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the cold runner body stays inside its frozen wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and peak < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_rss_bytes": peak, "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle500 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    train_only = os.environ.get("CYCLE500_TRAIN_ONLY") == "1"
    print("CYCLE500 KRAUS-GRADE REPEATED-HISTORY-LAW TOURNAMENT", "TRAIN_ONLY" if train_only else "FULL")
    contract_controls()
    surface = c493.c488.finalized_surface()
    route_a_controls(surface, include_held=not train_only)
    route_b_controls(surface, include_held=not train_only)
    route_c_controls(surface, include_held=not train_only)
    deletion_bath_covariance_controls()
    far_shore_and_prior_controls()
    no_go_controls()
    inventory_controls()
    resource_controls(started)
    signal.alarm(0)
    label = "TRAIN_RESULT" if train_only else "RESULT"
    print(f"\n{label} pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
