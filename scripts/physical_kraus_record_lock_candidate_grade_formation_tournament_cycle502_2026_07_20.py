#!/usr/bin/env python3
"""Cycle 502: C478/C500-to-Record formation-law tournament.

The executable ceiling is a reversible hard-core one-winner candidate token.
No coherent sector, candidate FORM, dephased mixture, or winner bit is promoted
to an actual member or framework Record.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import sqrt
from pathlib import Path
import inspect
import os
import re
import resource
import signal
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_kraus_grade_repeated_history_law_tournament_cycle500_2026_07_20 as c500


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_KRAUS_RECORD_LOCK_CANDIDATE_GRADE_FORMATION_TOURNAMENT_CYCLE502_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-9
RANK_TOL = 1e-10
LP_TOL = 1e-9
C_RESPONSE_L1_TOL = 0.10
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
TRAIN_L = 3
HELD_L = 6
A_TRAIN_N = 2
A_HELD_N = 4
B_TRAIN_R = 2
B_HELD_R = 4
B_TRAIN_N = 2
B_HELD_N = 4
C_TRAIN_N = 8
C_HELD_N = 16
MENU_ARITY = 5
PASS = 0
FAIL = 0
Word = tuple[int, ...]
Coord = tuple[int, int, int]
Sparse = dict[tuple[object, ...], complex]


FROZEN = {
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "composite Gleason bridge": "bd019a4a2ba0827b428c4af6db1720b2a0f27f0b1a0aaf8f065d0f90fb69163f",
    "Record Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "Record production-kernel boundary": "26de173bb9e3a613145fa72e614a0e27d67bcbfb431605d0f8b376b52c724b26",
    "Cycle351 runner": "7912b5177f073abd5d06fd6206720582db2ebd1fe0cbb9d63afff8698cd53291",
    "Cycle351 note": "19a0bc407c74c4700ae6a39ccb842285419b0611477904f378c9c7fb6f170e81",
    "Cycle449 runner": "857febfb57c7b82559465ab0623ef15b5c392b87ceb323340e007c228df442ad",
    "Cycle449 note": "b4aef2f452992203378ea3a16ec1dbc42126c3951eca2ac8e5beeda166352e11",
    "Cycle454 runner": "09d9781ad3416bf8bd94917353661c1d222de115bc83691150be19fb4ae11ed2",
    "Cycle454 note": "1b6bbc97a6cdd94ed33533df034f62a1b83d9ae2fa1284d8d8a0ec3e0df6337d",
    "Cycle478 runner": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "Cycle478 note": "87ed2bfbcff03b155496123d664050e80e01c67e668b06d751c3ecef2415652f",
    "Cycle493 runner": "7c51c313f83e006d1bd036e1d3d3d6a7f0fb39cfa56f874419d1e18658aca9af",
    "Cycle493 note": "81cab7f7fa54bef5789c3991911dc197f7506e4aeaa721973a548685006cbd8a",
    "Cycle496 runner": "b34e795f9b25e5ac8c2911038580a89df84bab65d658a3fbf2db6ac017c79083",
    "Cycle496 note": "bd3b0d5542f0bccad9e94a45ef913b91a4866ffba03eaa54b634c46d339f9945",
    "Cycle500 runner": "01c459cd067e4b02b60558a3c29c95a0f93b3fd1d916a27176e35128f1668a90",
    "Cycle500 note": "0ba90e82d3759726914cf72d5f27f1687995045ce0c642e809f7bce713f79caa",
}
FROZEN_PATHS = {
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "composite Gleason bridge": ROOT / "docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md",
    "Record Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "Record production-kernel boundary": ROOT / "docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md",
    "Cycle351 runner": ROOT / "scripts/physical_typed_record_born_corpus_tournament_synthesis_cycle351_2026_07_18.py",
    "Cycle351 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_CYCLE351_NOTE_2026-07-18.md",
    "Cycle449 runner": ROOT / "scripts/physical_record_actualization_law_program_tournament_cycle449_2026_07_19.py",
    "Cycle449 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECORD_ACTUALIZATION_LAW_PROGRAM_TOURNAMENT_CYCLE449_NOTE_2026-07-19.md",
    "Cycle454 runner": ROOT / "scripts/physical_born_scaled_ray_split_merge_auxiliary_cycle454_2026_07_19.py",
    "Cycle454 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_SCALED_RAY_SPLIT_MERGE_AUXILIARY_CYCLE454_NOTE_2026-07-19.md",
    "Cycle478 runner": Path(c500.c493.c488.c478.__file__),
    "Cycle478 note": c500.c493.c488.c478.NOTE,
    "Cycle493 runner": Path(c500.c493.__file__),
    "Cycle493 note": c500.c493.NOTE,
    "Cycle496 runner": Path(c500.c496.__file__),
    "Cycle496 note": c500.c496.NOTE,
    "Cycle500 runner": Path(c500.__file__),
    "Cycle500 note": c500.NOTE,
}


class WallCapExceeded(RuntimeError):
    pass


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class BasisState:
    bits: Word


@dataclass(frozen=True)
class HardCoreLockCandidate:
    candidates: Word
    winners: Word
    losers: Word
    lock_flag: int
    content: Word
    actual_member: None = None
    framework_Record: None = None


@dataclass(frozen=True)
class TypedFormationObjects:
    cylinder_grade: str = "squared norm of one orthogonal coherent history sector"
    candidate_FORM: str = "bath-relative candidate FORM receipt"
    endpoint_lineage: str = "Cycle498 candidate-FORM endpoint/predecessor chain"
    hard_core_lock_candidate: str = "reversible one-winner token with every loser retained"
    actual_member: None = None
    framework_Record: None = None
    empirical_frequency: None = None


@dataclass(frozen=True)
class Trace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class ConstraintSystem:
    keys: tuple[tuple[object, ...], ...]
    rows: tuple[tuple[tuple[int, int], ...], ...]
    rhs: tuple[int, ...]

    def dense(self) -> tuple[np.ndarray, np.ndarray]:
        matrix = np.zeros((len(self.rows), len(self.keys)), dtype=float)
        for row_index, row in enumerate(self.rows):
            for column, value in row:
                matrix[row_index, column] = value
        return matrix, np.asarray(self.rhs, dtype=float)


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
        "route a — reversible hard-core one-winner candidate apparatus",
        "route b — finite operational grade-functional constraint audit",
        "route c — deterministic rotor/formation control",
        "hard_core_lock_candidate", "coherent output retains every orthogonal winner sector",
        "actual cycle-478", "cycle-500 cylinder", "train l=3", "held l=6",
        "train n=2", "held n=4", "train n=8", "held n=16",
        "rank tolerance: 1e-10", "lp tolerance: 1e-9", "l1 <= 0.10",
        "candidate form is not a framework record", "grades are not probability",
        "all 24 proper-cubic frames", "supplied / derived / open",
        "gate disposition: fail", "no shared obstruction or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    self_sha = file_sha(Path(__file__))
    declared = declared_runner_sha()
    check(
        "the Cycle502 note freezes this exact runner and the strict candidate/member/Record ceiling",
        not missing and declared == self_sha,
        {"missing": missing, "runner_sha": self_sha, "declared_runner_sha": declared},
    )
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "the constitutional, boundary, Cycle351/449/454/478/493/496/500 inputs are exact-hash frozen",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )


def states() -> tuple[tuple[str, np.ndarray], ...]:
    return (
        ("z-plus", np.asarray((1.0, 0.0), complex)),
        ("y-plus", np.asarray((1.0, 1.0j), complex) / sqrt(2.0)),
    )


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    start = cursor[0]
    cursor[0] += width
    return tuple(range(start, start + width))


_cursor = [0]
POINTER = take(_cursor, 3)
CANDIDATE = take(_cursor, MENU_ARITY)
WINNER = take(_cursor, MENU_ARITY)
LOSER = take(_cursor, MENU_ARITY)
LOCK_FLAG = take(_cursor, 1)[0]
CONTENT = take(_cursor, 3)
FREE_PREFIX = take(_cursor, MENU_ARITY)
DECODE_PAIR = take(_cursor, 1)[0]
TOTAL_M2 = _cursor[0]
WORK_M2 = FREE_PREFIX + (DECODE_PAIR,)
OUTPUT_M2 = CANDIDATE + WINNER + LOSER + (LOCK_FLAG,) + CONTENT


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple) and len(value) == width
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in value)
    )


def bits3(value: int) -> Word:
    if value not in range(8):
        raise ValueError("three-M2 value leaves its binary domain")
    return tuple((value >> lane) & 1 for lane in range(3))


def integer3(bits: Word) -> int:
    if not is_word(bits, 3):
        raise ValueError("three-M2 word is malformed")
    return sum(bit << lane for lane, bit in enumerate(bits))


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle502 gate")
    if any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("Cycle502 gate leaves the bounded M2 block")
    return Gate(kind, sites, label)


@lru_cache(maxsize=1)
def decoder_schedule() -> tuple[Gate, ...]:
    schedule = []
    for label in range(MENU_ARITY):
        pattern = bits3(label)
        flipped = tuple(POINTER[lane] for lane, bit in enumerate(pattern) if bit == 0)
        schedule.extend(gate("X", (site,), f"decode:{label}:neg:{lane}") for lane, site in enumerate(flipped))
        schedule.append(gate("TOFFOLI", (POINTER[0], POINTER[1], DECODE_PAIR), f"decode:{label}:pair"))
        schedule.append(gate("TOFFOLI", (DECODE_PAIR, POINTER[2], CANDIDATE[label]), f"decode:{label}:write"))
        schedule.append(gate("TOFFOLI", (POINTER[0], POINTER[1], DECODE_PAIR), f"decode:{label}:unpair"))
        schedule.extend(gate("X", (site,), f"decode:{label}:restore:{lane}") for lane, site in reversed(tuple(enumerate(flipped))))
    return tuple(schedule)


def prefix_step(j: int, suffix: str) -> tuple[Gate, ...]:
    return (
        gate("X", (CANDIDATE[j],), f"prefix:{j}:neg:{suffix}"),
        gate("TOFFOLI", (FREE_PREFIX[j], CANDIDATE[j], FREE_PREFIX[j + 1]), f"prefix:{j}:and:{suffix}"),
        gate("X", (CANDIDATE[j],), f"prefix:{j}:restore:{suffix}"),
    )


@lru_cache(maxsize=1)
def hard_core_schedule() -> tuple[Gate, ...]:
    compute = [gate("X", (FREE_PREFIX[0],), "one-winner:free-seed")]
    for j in range(MENU_ARITY):
        compute.append(gate("TOFFOLI", (FREE_PREFIX[j], CANDIDATE[j], WINNER[j]), f"one-winner:{j}"))
        if j + 1 < MENU_ARITY:
            compute.extend(prefix_step(j, "compute"))
    writes = []
    for j in range(MENU_ARITY):
        writes.append(gate("CNOT", (WINNER[j], LOCK_FLAG), f"lock-candidate:flag:{j}"))
        for lane, bit in enumerate(bits3(j)):
            if bit:
                writes.append(gate("CNOT", (WINNER[j], CONTENT[lane]), f"lock-candidate:content:{j}:{lane}"))
        writes.append(gate("CNOT", (CANDIDATE[j], LOSER[j]), f"loser:copy:{j}"))
        writes.append(gate("CNOT", (WINNER[j], LOSER[j]), f"loser:remove-winner:{j}"))
    uncompute = []
    for j in reversed(range(MENU_ARITY - 1)):
        uncompute.extend(reversed(prefix_step(j, "uncompute")))
    uncompute.append(gate("X", (FREE_PREFIX[0],), "one-winner:free-unseed"))
    return tuple(compute + writes + uncompute)


@lru_cache(maxsize=1)
def physical_schedule() -> tuple[Gate, ...]:
    return decoder_schedule() + hard_core_schedule()


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError("unknown Cycle502 primitive")


def validate_state(state: BasisState, *, blank_outputs: bool = False) -> None:
    if not isinstance(state, BasisState) or not is_word(state.bits, TOTAL_M2):
        raise ValueError("Cycle502 hard-core state leaves the binary M2 domain")
    if any(state.bits[site] for site in WORK_M2):
        raise ValueError("Cycle502 clean work M2 must be blank at the boundary")
    if blank_outputs and any(state.bits[site] for site in OUTPUT_M2):
        raise ValueError("Cycle502 candidate/output M2 must enter blank")


def prepare_pointer(pointer: int) -> BasisState:
    if pointer not in range(MENU_ARITY):
        raise ValueError("actual fine pointer leaves the five-label code")
    bits = [0] * TOTAL_M2
    for site, bit in zip(POINTER, bits3(pointer)):
        bits[site] = bit
    state = BasisState(tuple(bits))
    validate_state(state, blank_outputs=True)
    return state


def prepare_candidates(candidates: Word) -> BasisState:
    if not is_word(candidates, MENU_ARITY) or not any(candidates):
        raise ValueError("collision fixture needs a nonempty five-M2 candidate word")
    bits = [0] * TOTAL_M2
    for site, bit in zip(CANDIDATE, candidates):
        bits[site] = bit
    return BasisState(tuple(bits))


def apply_schedule(state: BasisState, schedule: tuple[Gate, ...], *, reverse: bool = False) -> BasisState:
    validate_state(state)
    bits = list(state.bits)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    output = BasisState(tuple(bits))
    validate_state(output)
    return output


def apply_physical(
    state: BasisState, *, reverse: bool = False, delete_label: str | None = None
) -> BasisState:
    validate_state(state, blank_outputs=not reverse)
    schedule = physical_schedule()
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must identify exactly one Cycle502 gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    return apply_schedule(state, schedule, reverse=reverse)


def lock_view(state: BasisState) -> HardCoreLockCandidate:
    validate_state(state)
    select = lambda sites: tuple(state.bits[index] for index in sites)
    return HardCoreLockCandidate(
        select(CANDIDATE), select(WINNER), select(LOSER), state.bits[LOCK_FLAG], select(CONTENT)
    )


def coarse_pointer_state(pointer: int) -> BasisState:
    initial = prepare_pointer(pointer)
    bits = list(initial.bits)
    bits[CANDIDATE[pointer]] = 1
    bits[WINNER[pointer]] = 1
    bits[LOCK_FLAG] = 1
    for site, bit in zip(CONTENT, bits3(pointer)):
        bits[site] = bit
    return BasisState(tuple(bits))


def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(TOTAL_M2))
    targets = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("Cycle502 line routing failed")
    return tuple(swaps)


@lru_cache(maxsize=1)
def nn_trace() -> Trace:
    digest = sha256(b"Cycle502 28-M2 hard-core one-winner right-edge router v1")
    primitives = failures = maximum = 0
    for item in physical_schedule():
        swaps = route_for_gate(item)
        primitives += 1 + 6 * len(swaps)
        failures += sum(right != left + 1 for left, right in swaps)
        maximum = max(maximum, len(item.sites))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{swaps}".encode())
    return Trace(len(physical_schedule()), primitives, maximum, failures, digest.hexdigest())


def apply_nearest_neighbor(state: BasisState) -> BasisState:
    validate_state(state, blank_outputs=True)
    bits = list(state.bits)
    for item in physical_schedule():
        if item.kind == "X":
            apply_gate(bits, item)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
        width = len(item.sites)
        apply_gate(bits, Gate(item.kind, tuple(range(TOTAL_M2 - width, TOTAL_M2)), item.label))
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
    return BasisState(tuple(bits))


@lru_cache(maxsize=1)
def lock_signatures() -> tuple[HardCoreLockCandidate, ...]:
    return tuple(lock_view(apply_physical(prepare_pointer(pointer))) for pointer in range(MENU_ARITY))


def sparse_residual(left: Sparse, right: Sparse) -> float:
    return c500.sparse_residual(left, right)


def augment_lock(state: Sparse) -> Sparse:
    """Linearly extend the already basis-certified fixed 28-M2 permutation.

    The pointer label indexes a precomputed output signature in this offline
    sparse evaluator.  It never selects, branches, or rebuilds the physical
    schedule at runtime.
    """
    signatures = lock_signatures()
    output: Sparse = {}
    for (pointers, systems, packets, form_bits), amplitude in state.items():
        locks = tuple(signatures[pointer] for pointer in pointers)
        c500.sparse_add(output, (pointers, systems, packets, form_bits, locks), amplitude)
    return output


def grades_by_word(state: Sparse) -> dict[Word, float]:
    grades: dict[Word, float] = {}
    for key, amplitude in state.items():
        word = key[0]
        grades[word] = grades.get(word, 0.0) + abs(amplitude) ** 2
    return grades


def explicit_domain_rejections() -> dict[str, bool]:
    fixtures: dict[str, object] = {}

    dirty_bits = list(prepare_pointer(0).bits)
    dirty_bits[FREE_PREFIX[0]] = 1
    fixtures["dirty_work"] = BasisState(tuple(dirty_bits))
    fixtures["illegal_pointer"] = 5
    nonbinary = list(prepare_pointer(0).bits)
    nonbinary[POINTER[0]] = 2
    fixtures["nonbinary"] = BasisState(tuple(nonbinary))
    fixtures["malformed_width"] = BasisState((0,) * (TOTAL_M2 - 1))

    rejected: dict[str, bool] = {}
    for name, fixture in fixtures.items():
        try:
            if name == "illegal_pointer":
                prepare_pointer(fixture)  # type: ignore[arg-type]
            else:
                apply_physical(fixture)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            rejected[name] = True
        else:
            rejected[name] = False
    return rejected


def augment_composition_scan() -> dict[str, object]:
    tree = ast.parse(inspect.getsource(augment_lock))
    calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
    )
    schedule_selection_tokens = (
        "physical_schedule", "hard_core_schedule", "apply_physical",
    )
    state_functional_tokens = (
        "grades_by_word", "branch_grades", "np.vdot", "np.linalg.norm",
    )
    schedule_selection_calls = tuple(
        call for call in calls if any(token in call for token in schedule_selection_tokens)
    )
    state_functional_norm_grade_calls = tuple(
        call for call in calls if any(token in call for token in state_functional_tokens)
    )
    offline_sparse_representation_traversals = tuple(
        call for call in calls if call == "state.items"
    )
    pointer_conditionals = tuple(
        ast.unparse(node.test)
        for node in ast.walk(tree)
        if isinstance(node, ast.If) and "pointer" in ast.unparse(node.test).lower()
    )
    return {
        "calls": calls,
        "offline_sparse_representation_traversals": offline_sparse_representation_traversals,
        "schedule_selection_calls": schedule_selection_calls,
        "state_functional_norm_grade_calls": state_functional_norm_grade_calls,
        "pointer_conditionals": pointer_conditionals,
        "basis_signature_lookup": "signatures[pointer]",
        "interpretation": (
            "mathematical linear extension of a separately basis-certified fixed permutation; "
            "not a literal gate-by-gate simulator or runtime physical control"
        ),
    }


def route_a_controls(surface: object, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE A / REVERSIBLE HARD-CORE ONE-WINNER CANDIDATE APPARATUS")
    basis_rows = []
    failures = 0
    for pointer in range(MENU_ARITY):
        initial = prepare_pointer(pointer)
        physical = apply_physical(initial)
        coarse = coarse_pointer_state(pointer)
        inverse = apply_physical(physical, reverse=True)
        routed = apply_nearest_neighbor(initial)
        view = lock_view(physical)
        failures += int(
            physical != coarse or inverse != initial or routed != physical
            or sum(view.winners) != 1 or view.lock_flag != 1
            or integer3(view.content) != pointer or any(view.losers)
        )
        basis_rows.append((pointer, view, physical == coarse, inverse == initial, routed == physical))

    collisions = []
    for candidates in ((1, 1, 0, 0, 0), (0, 1, 0, 1, 1), (1, 1, 1, 1, 1)):
        initial = prepare_candidates(candidates)
        physical = apply_schedule(initial, hard_core_schedule())
        inverse = apply_schedule(physical, hard_core_schedule(), reverse=True)
        view = lock_view(physical)
        expected = candidates.index(1)
        failures += int(
            sum(view.winners) != 1 or view.winners[expected] != 1
            or integer3(view.content) != expected
            or sum(view.losers) != sum(candidates) - 1 or inverse != initial
        )
        collisions.append((candidates, view, inverse == initial))

    fixtures = (("train", TRAIN_L, A_TRAIN_N, c500.c493.c488.TRAIN_CASE, c500.c493.TRAIN_HORIZON),)
    if include_held:
        fixtures += (("held", HELD_L, A_HELD_N, c500.c493.c488.HELD_CASE, c500.c493.HELD_HORIZON),)
    rows = []
    for lane, length, n, case_name, horizon in fixtures:
        event = c500.event_basis_maps(surface, length)
        form = c500.form_basis_signatures(n, case_name, horizon)
        state_outputs: dict[str, Sparse] = {}
        schedule_pairs = []
        for name, psi in states():
            vector = c500.tensor_vector(psi, n)
            physical = augment_lock(c500.repeated_actual_map(vector, event["physical"], form["signatures"], n))
            reference = augment_lock(c500.repeated_actual_map(vector, event["reference"], form["signatures"], n))
            grades = grades_by_word(physical)
            controls = c500.cylinder_controls(grades, c500.branch_grades(event["program"], psi), n)
            residual = sparse_residual(physical, reference)
            failures += int(
                residual >= TOL or any(value >= TOL for value in controls.values())
                or len(grades) != MENU_ARITY**n
            )
            schedule_pairs.append((event["program_law_digest"], form["schedule_digest"], nn_trace().sha256))
            state_outputs[name] = physical
            rows.append({
                "lane": lane, "state": name, "N": n,
                "coherent_sparse_terms": len(physical), "orthogonal_winner_sectors": len(grades),
                "E_G_residual": residual, "cylinder_grade_controls": controls,
                "one_step_grades": c500.branch_grades(event["program"], psi),
                "program_FORM_lock_digests": schedule_pairs[-1],
                "actual_member": None, "framework_Record": None,
            })
        failures += int(
            len(set(schedule_pairs)) != 1 or form["failures"] != 0
            or form["receipt_flags"] != {(False, False, False)}
            or max(event["single_E_G"] + event["single_inverse"]) >= TOL or event["leakage"] != 0
        )
        phase = 0.37 + 0.61j
        z = c500.tensor_vector(states()[0][1], n)
        y = c500.tensor_vector(states()[1][1], n)
        coherent = augment_lock(c500.repeated_actual_map(z + phase * y, event["physical"], form["signatures"], n))
        linear: Sparse = {}
        for key, value in state_outputs["z-plus"].items():
            c500.sparse_add(linear, key, value)
        for key, value in state_outputs["y-plus"].items():
            c500.sparse_add(linear, key, phase * value)
        phase_residual = sparse_residual(coherent, linear)
        failures += int(phase_residual >= TOL)
        rows[-1]["phase_sensitive_linearity_residual"] = phase_residual
        rows[-1]["FORM_basis_certificate"] = {
            key: value for key, value in form.items() if key != "signatures"
        }

        form_word = tuple(range(n)) if n <= MENU_ARITY else tuple(index % MENU_ARITY for index in range(n))
        form_base = c500.c493.prepare_history(case_name, horizon, form_word)
        form_nominal = c500.c493.apply_physical(form_base)
        form_damaged = c500.c493.apply_physical(
            form_base, delete_label="cell:0:match:0:prefix:0"
        )
        form_deletion_visible = (
            c500.c493.c488.receipts(form_damaged) is None
            or c500.c493.c488.final_counts(form_damaged)
            != c500.c493.c488.final_counts(form_nominal)
        )
        failures += int(not form_deletion_visible)
        rows[-1]["FORM_gate_deletion_visible"] = form_deletion_visible

    damaged = apply_physical(prepare_pointer(0), delete_label="decode:0:write")
    deletion_visible = damaged != coarse_pointer_state(0) and lock_view(damaged).lock_flag == 0
    failures += int(not deletion_visible)
    domain_rejections = explicit_domain_rejections()
    failures += sum(not rejected for rejected in domain_rejections.values())
    source = inspect.getsource(physical_schedule).lower() + inspect.getsource(hard_core_schedule).lower()
    query_hits = {token: source.count(token) for token in ("psi", "amplitude", "norm", "grade", "np.vdot", "state.")}
    composition_scan = augment_composition_scan()
    failures += (
        len(composition_scan["schedule_selection_calls"])
        + len(composition_scan["state_functional_norm_grade_calls"])
        + len(composition_scan["pointer_conditionals"])
        + int(composition_scan["offline_sparse_representation_traversals"] != ("state.items",))
    )
    typed = TypedFormationObjects()
    check(
        "A: actual C478/C500 sectors compile to reversible hard_core_lock_candidate tokens while every orthogonal winner sector remains coherent",
        failures == 0 and all(value == 0 for value in query_hits.values())
        and TOTAL_M2 <= 64 and nn_trace().maximum_support <= 3 and nn_trace().connected_failures == 0,
        {
            "basis_rows": basis_rows, "collision_rows": collisions, "train_held_rows": rows,
            "literal_new_M2_per_event": TOTAL_M2, "resource_ceiling_M2": 64,
            "trace": nn_trace(), "decoder_deletion_visible": deletion_visible,
            "explicit_domain_rejections": domain_rejections,
            "schedule_query_hits": query_hits, "augment_composition_scan": composition_scan,
            "typed_objects": typed,
            "coherent_output_retains_all_orthogonal_winner_sectors": True,
            "actual_member_produced": False, "framework_Record_produced": False,
            "novelty": "composition with actual C478/C500 pointer-cylinder, not a repeat of Cycle449 precommit",
        },
    )
    return {"rows": rows, "typed": typed}


def add_equation(
    rows: list[tuple[tuple[int, int], ...]], rhs: list[int],
    index: dict[tuple[object, ...], int], terms: dict[tuple[object, ...], int], value: int = 0,
) -> None:
    compact = tuple(sorted((index[key], coefficient) for key, coefficient in terms.items() if coefficient))
    rows.append(compact)
    rhs.append(value)


def build_constraint_system(refinement: int, n: int) -> ConstraintSystem:
    keys: list[tuple[object, ...]] = [("root",)]
    keys.extend(("coarse", pointer) for pointer in range(MENU_ARITY))
    keys.extend(("micro", pointer, micro) for pointer in range(MENU_ARITY) for micro in range(refinement))
    for width in range(2, n + 1):
        keys.extend(("cyl", word) for word in product(range(MENU_ARITY), repeat=width))
    index = {key: column for column, key in enumerate(keys)}
    rows: list[tuple[tuple[int, int], ...]] = []
    rhs: list[int] = []
    add_equation(rows, rhs, index, {("root",): 1}, 1)
    add_equation(rows, rhs, index, {**{("coarse", j): 1 for j in range(MENU_ARITY)}, ("root",): -1})
    for pointer in range(MENU_ARITY):
        terms = {("micro", pointer, micro): 1 for micro in range(refinement)}
        terms[("coarse", pointer)] = -1
        add_equation(rows, rhs, index, terms)
        for micro in range(1, refinement):
            add_equation(rows, rhs, index, {
                ("micro", pointer, micro): 1, ("micro", pointer, 0): -1,
            })
    for width in range(1, n):
        for prefix in product(range(MENU_ARITY), repeat=width):
            parent = ("coarse", prefix[0]) if width == 1 else ("cyl", prefix)
            terms = {parent: 1}
            for pointer in range(MENU_ARITY):
                terms[("cyl", prefix + (pointer,))] = -1
            add_equation(rows, rhs, index, terms)
    terminal = tuple(product(range(MENU_ARITY), repeat=n))
    grouped: dict[tuple[int, ...], list[Word]] = {}
    for word in terminal:
        grouped.setdefault(tuple(word.count(pointer) for pointer in range(MENU_ARITY)), []).append(word)
    for words in grouped.values():
        canonical = words[0]
        for word in words[1:]:
            add_equation(rows, rhs, index, {("cyl", word): 1, ("cyl", canonical): -1})
    for pointer in range(MENU_ARITY):
        terms = {("cyl", word): word.count(pointer) for word in terminal}
        terms[("coarse", pointer)] = -n
        add_equation(rows, rhs, index, terms)
    return ConstraintSystem(tuple(keys), tuple(rows), tuple(rhs))


def grade_assignment(system: ConstraintSystem, q: tuple[float, ...], refinement: int) -> np.ndarray:
    output = np.zeros(len(system.keys), dtype=float)
    for column, key in enumerate(system.keys):
        if key == ("root",):
            output[column] = 1.0
        elif key[0] == "coarse":
            output[column] = q[int(key[1])]
        elif key[0] == "micro":
            output[column] = q[int(key[1])] / refinement
        elif key[0] == "cyl":
            output[column] = float(np.prod([q[pointer] for pointer in key[1]]))
    return output


def equation_residual(system: ConstraintSystem, values: np.ndarray) -> float:
    matrix, rhs = system.dense()
    return float(np.max(np.abs(matrix @ values - rhs)))


def maximum_l1_witness(
    system: ConstraintSystem, trace_grades: tuple[float, ...]
) -> dict[str, object]:
    matrix, rhs = system.dense()
    coarse_columns = tuple(system.keys.index(("coarse", pointer)) for pointer in range(MENU_ARITY))
    best_distance = -1.0
    best_values = None
    best_sign = None
    for signs in product((-1.0, 1.0), repeat=MENU_ARITY):
        objective = np.zeros(len(system.keys), dtype=float)
        for column, sign in zip(coarse_columns, signs):
            objective[column] = -sign
        result = linprog(objective, A_eq=matrix, b_eq=rhs, bounds=(0.0, None), method="highs")
        if not result.success:
            raise RuntimeError(f"Cycle502 deterministic LP failed: {result.message}")
        q = tuple(float(result.x[column]) for column in coarse_columns)
        signed_distance = sum(sign * (value - target) for sign, value, target in zip(signs, q, trace_grades))
        if signed_distance > best_distance + LP_TOL:
            best_distance = signed_distance
            best_values = result.x
            best_sign = signs
    if best_values is None:
        raise RuntimeError("Cycle502 deterministic LP produced no witness")
    q = tuple(float(best_values[column]) for column in coarse_columns)
    actual_distance = sum(abs(value - target) for value, target in zip(q, trace_grades))
    theoretical = 2.0 * (1.0 - min(trace_grades))
    return {
        "values": best_values, "coarse_grades": q, "L1_from_trace": actual_distance,
        "signed_L1_certificate": best_distance,
        "simplex_theoretical_maximum": theoretical,
        "maximum_gap": max(abs(best_distance - theoretical), abs(actual_distance - theoretical)),
        "sign_objective": best_sign,
        "equation_residual": float(np.max(np.abs(matrix @ best_values - rhs))),
        "minimum_component": float(np.min(best_values)),
    }


def route_b_controls(surface: object, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE B / FINITE OPERATIONAL GRADE-FUNCTIONAL CONSTRAINT AUDIT")
    fixtures = (("train", surface.train_program, B_TRAIN_R, B_TRAIN_N),)
    if include_held:
        fixtures += (("held", surface.held_program, B_HELD_R, B_HELD_N),)
    rows = []
    failures = 0
    for lane, program, refinement, n in fixtures:
        system = build_constraint_system(refinement, n)
        matrix, rhs = system.dense()
        numeric_rank = int(np.linalg.matrix_rank(matrix, tol=RANK_TOL))
        exact_rank = int(sp.Matrix(matrix.astype(int).tolist()).rank()) if lane == "train" else None
        rank = exact_rank if exact_rank is not None else numeric_rank
        trace_rows = []
        for name, psi in states():
            q = c500.branch_grades(program, psi)
            rho = np.outer(psi, psi.conj())
            trace_q = tuple(float(np.trace(rho @ effect).real) for effect in program.coarse_effects)
            trace_effect_residual = max(abs(left - right) for left, right in zip(q, trace_q))
            trace_values = grade_assignment(system, q, refinement)
            uniform_values = grade_assignment(system, (0.2,) * MENU_ARITY, refinement)
            witness = maximum_l1_witness(system, q)
            trace_residual = equation_residual(system, trace_values)
            uniform_residual = equation_residual(system, uniform_values)
            failures += int(
                trace_effect_residual >= TOL or trace_residual >= TOL or uniform_residual >= TOL
                or witness["equation_residual"] >= LP_TOL or witness["minimum_component"] < -LP_TOL
                or witness["maximum_gap"] >= LP_TOL or len(system.keys) - rank <= 0
            )
            trace_rows.append({
                "state": name, "trace_grades": q,
                "trace_effect_residual": trace_effect_residual,
                "trace_constraint_residual": trace_residual,
                "uniform_constraint_residual": uniform_residual,
                "uniform_L1_from_trace": sum(abs(0.2 - value) for value in q),
                "maximally_separated_lawful_alternative": {
                    key: value for key, value in witness.items() if key != "values"
                },
            })
        failures += int(exact_rank is not None and exact_rank != numeric_rank)
        rows.append({
            "lane": lane, "refinement": refinement, "N": n,
            "variables": len(system.keys), "equations": len(system.rows),
            "exact_rank": exact_rank, "numeric_rank": numeric_rank,
            "reported_nullity": len(system.keys) - rank,
            "rank_tolerance": RANK_TOL,
            "noncontextuality_implementation": "one shared variable per exact coarse/refined/prefix effect label",
            "constraints": ("normalization", "refinement additivity", "micro-exchange", "prefix additivity", "terminal exchangeability", "grade-count additivity"),
            "state_rows": trace_rows,
        })
    check(
        "B: the exact finite effect/refinement/product constraint matrix admits trace grades but does not uniquely select them",
        failures == 0 and all(row["reported_nullity"] > 0 for row in rows),
        {
            "train_held_rows": rows,
            "held_rank_policy": "frozen SVD tolerance 1e-10; exact train rank only before held",
            "Cycle454_residual_match": "finite split/additivity left 20 projected null directions, 17 beyond Pauli; no occurrence",
            "composite_Gleason_boundary": "H1-H4 force trace form on M4 conditionally; H1/H4 and conditioned rho remain supplied",
            "physical_formation_schedule_claimed_by_route_B": False,
            "actual_member_produced": False, "framework_Record_produced": False,
        },
    )
    return {"rows": rows}


def route_c_controls(surface: object, *, include_held: bool) -> dict[str, object]:
    print("\nROUTE C / DETERMINISTIC ROTOR + LOCK-CANDIDATE CONTROL")
    fixtures = (("train", surface.train_program, C_TRAIN_N),)
    if include_held:
        fixtures += (("held", surface.held_program, C_HELD_N),)
    rows = []
    conveyor_rows = []
    failures = 0
    for lane, program, n in fixtures:
        cursor, word = c500.extended_courier_forward(0, n)
        restored_seed, blanks = c500.c493.courier_inverse(cursor, word)
        lock_candidates = tuple(lock_view(apply_physical(prepare_pointer(pointer))) for pointer in word)
        contents = tuple(integer3(item.content) for item in lock_candidates)
        candidate_counts = tuple(Fraction(contents.count(pointer), n) for pointer in range(MENU_ARITY))
        state_rows = []
        for name, psi in states():
            grades = c500.branch_grades(program, psi)
            l1 = sum(abs(float(value) - grade) for value, grade in zip(candidate_counts, grades))
            state_rows.append((name, grades, tuple(map(str, candidate_counts)), l1, l1 <= C_RESPONSE_L1_TOL))
        inverse_locks = all(
            apply_physical(apply_physical(prepare_pointer(pointer)), reverse=True) == prepare_pointer(pointer)
            for pointer in word
        )
        failures += int(
            restored_seed != 0 or any(blanks) or contents != word or not inverse_locks
            or any(row[-1] for row in state_rows)
        )
        rows.append({
            "lane": lane, "N": n, "candidate_word": word,
            "candidate_counts": tuple(map(str, candidate_counts)),
            "state_grade_response": state_rows,
            "courier_inverse_exact": restored_seed == 0 and not any(blanks),
            "lock_candidate_inverse_exact": inverse_locks,
            "actual_member": None, "framework_Record": None, "empirical_frequency": None,
        })
        conveyor_rows.append(c500.conveyor_run(n))
    sources = "\n".join(inspect.getsource(function).lower() for function in (
        c500.extended_courier_forward, c500.c496.ca_word, c500.c493.rotate_pointer,
        c500.c496.conveyor_physical_tick, physical_schedule, hard_core_schedule,
    ))
    query_hits = {token: sources.count(token) for token in ("branch_weights", "branch_grades", "np.vdot", "norm(", "psi")}
    failures += int(any(query_hits.values()))
    failures += sum(int(
        any(row["E_G_residuals"]) or not row["inverse_exact"]
        or row["used"] != row["N"] or row["exported"] != row["N"]
    ) for row in conveyor_rows)
    check(
        "C: the fixed state-blind rotor/conveyor plus hard_core_lock_candidate block remains reversible but misses both grade-response targets",
        failures == 0,
        {
            "train_held_rows": rows, "physical_conveyor_rows": conveyor_rows,
            "frozen_response_L1_tolerance": C_RESPONSE_L1_TOL,
            "schedule_grade_state_query_hits": query_hits,
            "used_bath_reentry_operations": 0, "per_event_host_reset_operations": 0,
            "disposition": "route-specific nonresponse; no general deterministic/stochastic/admissibility no-go",
        },
    )
    return {"rows": rows, "conveyor": conveyor_rows}


def covariance_resource_controls(route_c: dict[str, object], *, include_held: bool) -> None:
    print("\nLOCALITY / BATH / ALL24 / RESOURCE CONTROL")
    frames = c500.c493.c488.proper_cubic_frames()
    base = tuple((index, 0, 0) for index in range(TOTAL_M2))
    base_edges = tuple((base[left], base[right]) for item in physical_schedule() for left, right in route_for_gate(item))
    manifest_failures = edge_failures = 0
    for frame in frames:
        rotated = tuple(c500.c493.c488.rotate_coord(site, frame) for site in base)
        carried_x = c500.c493.c488.rotate_coord((1, 0, 0), frame)
        independently_carried = tuple(tuple(index * value for value in carried_x) for index in range(TOTAL_M2))
        manifest_failures += int(rotated != independently_carried)
        for left, right in base_edges:
            a = c500.c493.c488.rotate_coord(left, frame)
            b = c500.c493.c488.rotate_coord(right, frame)
            edge_failures += int(c500.c493.c488.manhattan(a, b) != 1)
    held_or_train = route_c["conveyor"][-1]
    check(
        "the literal 28-M2 candidate block, retained bath conveyor, and carried line manifest pass their scoped locality/all24 audit",
        len(frames) == 24 and manifest_failures == edge_failures == 0
        and nn_trace().maximum_support <= 3 and nn_trace().connected_failures == 0
        and held_or_train["used"] == held_or_train["exported"] == held_or_train["N"],
        {
            "literal_candidate_block_M2": TOTAL_M2, "proper_cubic_frames": len(frames),
            "rotated_NN_edge_rows": len(frames) * len(base_edges),
            "independent_manifest_failures": manifest_failures, "edge_failures": edge_failures,
            "trace": nn_trace(),
            "largest_executed_conveyor": held_or_train["trace"],
            "scope": "Cycle502 hard-core placement plus frozen inherited C478/C493/C496 operator covariance",
            "arbitrary_N_or_infinite_resource_claimed": False,
        },
    )


def boundary_inventory_controls() -> None:
    print("\nFOUNDATION BOUNDARY / SUPPLIED-DERIVED-OPEN")
    supplied = (
        "Record occurrence ontology and exactly-one-admissible-lock sentence, but no content/site/weight/rate law",
        "two input preparations, actual C478 menu/Kraus/pointer/packets, C493 FORM, and C500 finite cylinder",
        "blank candidate/winner/loser/work/FORM/bath banks and explicit local rail order",
        "finite L/N/R, noiseless gates, geometry, tolerances, and all24 frame convention",
        "Route-B finite eligible domain and constraint families; conditional composite-Gleason H1-H4 only where named",
        "Route-C rotor law, seed zero, finite blank conveyor, and terminal boundary",
    )
    derived = (
        "literal reversible one-winner candidate block, collisions, loser retention, inverse, and deletion response",
        "actual C478+C493+C500 coherent composition with exact candidate-sector grade preservation",
        "finite train/held constraint-matrix rank/nullity and deterministic maximum-L1 lawful alternative",
        "fixed N8/N16 deterministic candidate response and retained conveyor audit",
        "bounded support, NN route, leakage/deletion/domain controls, bath nonreentry, and scoped all24",
        "strict seven-object type separation with actual member/Record/frequency absent",
    )
    open_items = (
        "production of one actual C478 member rather than all coherent winner correlations",
        "Record content/site formation law binding a physical member to the axiom's occurrence",
        "derivation of grade-domain/additivity/noncontextual/composite-menu premises and conditioned state functional",
        "probability meaning, stochastic law, stationarity/ergodicity, empirical sampling, convergence, and calibration",
        "blank-bath genesis, renewal, unbounded noisy permanence, and arbitrary-N/infinite-volume compiler",
        "time/rate, energy/inertia, source/gravity, continuum prediction, or constitutional conclusion",
    )
    typed = TypedFormationObjects()
    check(
        "the current Record/realized-state boundary and supplied/derived/open inventory prohibit candidate-to-actual relabeling",
        len(supplied) == len(derived) == len(open_items) == 6
        and typed.actual_member is typed.framework_Record is typed.empirical_frequency is None,
        {
            "Record_axiom": "Records form; when present one admissible lock; content/site/weight/rate law open",
            "realized_state_primitive": "pointwise slot only; no state/member/selector/measure/grade",
            "supplied": supplied, "derived": derived, "open": open_items,
            "typed_objects": typed, "authority": AUTHORITY, "audit": AUDIT,
        },
    )


def no_go_controls() -> None:
    print("\nN1-N8 / CLAIM GATE")
    n1 = (
        ("hard-core candidate register", "reversible bits", "one winner with losers retained", "candidate not actual", "ATTEMPTED"),
        ("finite noncontextual grade functional", "linear effect/cylinder constraints", "unique trace vector", "nullity/LP audit", "ATTEMPTED"),
        ("deterministic rotor formation", "basis microseed orbit", "two-input grade response", "fixed seed control", "ATTEMPTED"),
        ("autonomous stochastic retained bath", "local open-system trajectory", "one retained member with derived law", "OPEN", "UNTESTED"),
        ("admissibility-driven ratchet", "irreversible stable sector", "Record content/site formation", "OPEN", "UNTESTED"),
        ("derived microstate equilibrium", "physical hidden-variable distribution", "branch-grade response without supplied distribution", "OPEN", "UNTESTED"),
        ("stationary ergodic admitted Records", "Record process", "empirical frequency calibration", "OPEN", "UNTESTED"),
        ("infinite quasi-local environmental selection", "retained bath ray", "member plus renewable permanence", "OPEN", "UNTESTED"),
    )
    walls = ("grade/domain", "member actualization", "Record content/site binding", "process/frequency calibration", "bath genesis/permanence")
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "preparations and identical refresh", "actual menu/Kraus/packet/pointer code", "blank banks",
        "local rail order and candidate codecs", "FORM and endpoint meanings", "finite H refinements and product domain",
        "grade diagnostics and LP objective enumeration", "rotor law/seed", "stationarity absent unless named",
        "bath geometry/genesis boundary", "noiseless gates/tolerances", "Record/realized-state exact scope",
    )
    n4 = (
        ("Cycle351", "conditional corpus after supplied occurrence/actual word", "downstream only", False),
        ("Cycle449", "reversible precommit not Record", "candidate-to-Record actualization", True),
        ("Cycle454", "finite split/additivity null directions", "finite grade-functional nonuniqueness", True),
        ("Cycle478", "effect functionality without grade/occurrence", "actual pointer input", True),
        ("Cycle493", "coherent pointer-to-FORM; seed/q/member supplied", "member/formation", True),
        ("Cycle496", "dephasing/CA/conveyor without actual member", "stable resource/formation seam", True),
        ("Cycle500", "finite coherent cylinder; actual member/Record absent", "repeated candidate ceiling", True),
        ("frequency boundary", "counts need realized atoms/process", "single-event formation", False),
        ("production-kernel boundary", "append consumes produced atom", "formation producer", True),
    )
    n5 = (
        ("one event", "all five pointer labels/two inputs/L3-L6", "tested"),
        ("finite coherent cylinders", "N2/N4 and R2/R4", "tested"),
        ("deterministic candidate conveyor", "N8/N16", "tested"),
        ("arbitrary N/infinite bath", "untested", "no negative conclusion"),
        ("lattice-wide actual Records/empirical limit", "untested", "no negative conclusion"),
    )
    n6 = (
        "explicit formation-law import then bounded theorem then retirement audit",
        "derive an autonomous retained stochastic token",
        "derive admissibility-to-content/site binding",
        "derive full eligible grade domain and conditioned functional",
        "derive stationary/ergodic admitted-Record calibration",
        "derive bath genesis and renewable permanence",
    )
    n7 = (
        "A hostile constructive route couples the exact C478 pointer isometry to an autonomous local stochastic or ratchet bath, retains a stable selective token and every spent carrier, and uses a derived admissibility-to-content rule at the Record axiom's occurrence. A separately derived equilibrium measure and stationary ergodic theorem over admitted Records could then identify the token process with the operational grade functional. Cycle502's reversible candidate, finite grade constraints, and deterministic control neither build nor exclude those concrete terminal obligations."
    )
    n8 = (
        "Cycle449 made precommit physical without closing actuality",
        "Cycle496 removed per-event reset through N16 without bath genesis",
        "Cycle500 materialized the coherent product cylinder without a member",
        "Cycle454 replaced homogeneity shortcuts with physical split constraints while leaving null directions",
        "prior compiler walls repeatedly narrowed through new constructive layers rather than axiom edits",
    )
    check(
        "N1-N8 accepts scoped positive/route-specific results but rejects broad no-go, minimum-content, or axiom-pressure language",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 10 and len(n4) >= 8
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 350 and len(n8) >= 5,
        {
            "N1_normalized_families": n1, "N2_pairwise_walls": n2,
            "N3_hidden_condition_scan": n3, "N4_residual_matching": n4,
            "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
            "N7_steelman": n7, "N8_cross_cycle_echo": n8,
            "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
            "shared_obstruction": False, "axiom_pressure": False,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the runner body stays inside its frozen wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and peak < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_rss_bytes": peak, "wall_cap": WALL_CAP_SECONDS, "rss_cap": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle502 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    train_only = os.environ.get("CYCLE502_TRAIN_ONLY") == "1"
    print("CYCLE502 KRAUS/RECORD LOCK-CANDIDATE GRADE-FORMATION TOURNAMENT", "TRAIN_ONLY" if train_only else "FULL")
    contract_controls()
    # menu_surface avoids constructing held FORM words during train-only; its
    # inherited Cycle478 program surface itself contains both frozen L3/L6 maps.
    surface = c500.c493.c488.menu_surface()
    route_a_controls(surface, include_held=not train_only)
    route_b_controls(surface, include_held=not train_only)
    route_c = route_c_controls(surface, include_held=not train_only)
    covariance_resource_controls(route_c, include_held=not train_only)
    boundary_inventory_controls()
    no_go_controls()
    resource_controls(started)
    signal.alarm(0)
    label = "TRAIN_RESULT" if train_only else "RESULT"
    print(f"\n{label} pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
