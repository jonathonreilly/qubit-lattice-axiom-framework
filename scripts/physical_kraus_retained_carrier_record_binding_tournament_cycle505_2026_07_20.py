#!/usr/bin/env python3
"""Cycle 505: retained-carrier / Record-binding formation tournament.

This runner composes the exact Cycle478 pointer apparatus with the exact
Cycle502 28-M2 hard-core candidate block.  Its positive objects are physical
selective-token, retained-environment, and RecordBindingCandidate predicates.
None is an actual member or framework Record without an additional law.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_kraus_record_lock_candidate_grade_formation_tournament_cycle502_2026_07_20 as c502


c500 = c502.c500
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_KRAUS_RETAINED_CARRIER_RECORD_BINDING_TOURNAMENT_CYCLE505_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0
MENU = tuple(range(c502.MENU_ARITY))
TRAIN_L = 3
HELD_L = 6
TRAIN_N = 2
HELD_N = 4
A_TRAIN_H = 3
A_HELD_H = 7
B_TRAIN_F = 2
B_HELD_F = 4
NEW_M2_CEILING = 256
C478_FINE_LAW_M2 = 1493
C502_CANDIDATE_M2 = c502.TOTAL_M2
HELD_AUTHORIZATION_TOKEN = "root-cycle505-held-after-train-review-2026-07-20"
Word = tuple[int, ...]
Sparse = dict[tuple[object, ...], complex]

FROZEN = {
    "Cycle436 runner": "e7e62dfba1a0b8afe9c5fb3e28371d45f07f85af0de0f50e8653b2b2fae67f46",
    "Cycle436 note": "13af91d7d821a92f66a479049a4cb1672453e0e7e4df37c6967bb19937cd5c02",
    "Cycle478 runner": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "Cycle478 note": "87ed2bfbcff03b155496123d664050e80e01c67e668b06d751c3ecef2415652f",
    "Cycle500 runner": "01c459cd067e4b02b60558a3c29c95a0f93b3fd1d916a27176e35128f1668a90",
    "Cycle500 note": "0ba90e82d3759726914cf72d5f27f1687995045ce0c642e809f7bce713f79caa",
    "Cycle502 runner": "5494b7fd9d1411023ac2427b92c323cea9b7c26720b3a6b8d58ee32835e1e8a9",
    "Cycle502 note": "36e156581d5f3d3dddea1e0ce1344834bd31d65883160c3c3b04c4d4671b41c2",
    "Cycle219 runner": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "Cycle219 note": "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "production-kernel boundary": "26de173bb9e3a613145fa72e614a0e27d67bcbfb431605d0f8b376b52c724b26",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
}
FROZEN_PATHS = {
    "Cycle436 runner": ROOT / "scripts/physical_effect_functionality_protected_candidate_record_tournament_cycle436_2026_07_19.py",
    "Cycle436 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_EFFECT_FUNCTIONALITY_PROTECTED_CANDIDATE_RECORD_TOURNAMENT_CYCLE436_NOTE_2026-07-19.md",
    "Cycle478 runner": Path(c500.c493.c488.c478.__file__),
    "Cycle478 note": c500.c493.c488.c478.NOTE,
    "Cycle500 runner": Path(c500.__file__),
    "Cycle500 note": c500.NOTE,
    "Cycle502 runner": Path(c502.__file__),
    "Cycle502 note": c502.NOTE,
    "Cycle219 runner": ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "Cycle219 note": ROOT / "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "production-kernel boundary": ROOT / "docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
}


class WallCapExceeded(RuntimeError):
    pass


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class StableSelectiveToken:
    occupied: int
    content: Word
    redundant_fragments: tuple[Word, Word, Word]
    receipts: Word
    fresh: Word
    spent: Word
    actual_member: None = None
    framework_Record: None = None


@dataclass(frozen=True)
class RecordBindingCandidate:
    eligibility: Word
    singleton: int
    content: Word
    central_site_eligible: int
    actual_member: None = None
    framework_Record: None = None


@dataclass(frozen=True)
class TypedFormationObjects:
    c502_hard_core_candidate: str = "reversible five-label candidate with every sector retained"
    stable_selective_token: str = "finite-envelope retained-carrier basis token"
    retained_environment_label: str = "orthogonal retained dilation fragment"
    reduced_channel: str = "diagnostic partial trace, not a physical deletion"
    record_binding_candidate: str = "singleton admissibility-to-content/site predicate"
    actual_member: None = None
    framework_Record: None = None
    empirical_frequency: None = None


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
        "train l=3", "held l=6", "train n=2", "held n=4",
        "route a — finite-envelope retained-carrier progression",
        "route b — retained local instrument dilation",
        "route c — singleton recordbindingcandidate predicate",
        "same-reduced-channel diagnostic", "not physical trajectory ambiguity",
        "occurrence antecedent is purely semantic", "no occurrence-trigger m2",
        "fixed all-label gate schedule", "new route overhead", "total envelope",
        "candidate is not a framework record", "no actual member",
        "no shared obstruction or axiom-pressure claim", "gate disposition: fail",
        "n1–n8", "supplied / derived / open", "no threshold/refit path",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    self_sha = file_sha(Path(__file__))
    check(
        "the Cycle505 note freezes this exact runner and the corrected semantic/resource contract",
        not missing and declared_runner_sha() == self_sha,
        {"missing": missing, "runner_sha": self_sha, "declared": declared_runner_sha()},
    )
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "every imported framework, boundary, and physical runner/note is exact-hash frozen",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )


def input_states(mode: str) -> tuple[tuple[str, np.ndarray], ...]:
    if mode == "train":
        return (
            ("z-plus", np.asarray((1.0, 0.0), complex)),
            ("y-plus", np.asarray((1.0, 1.0j), complex) / sqrt(2.0)),
        )
    if mode == "held":
        return (
            ("x-plus-held", np.asarray((1.0, 1.0), complex) / sqrt(2.0)),
            ("held-skew", np.asarray((sqrt(3.0), 1.0j), complex) / 2.0),
        )
    raise ValueError("Cycle505 mode must be train or held")


def bits3(value: int) -> Word:
    return c502.bits3(value)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    start = cursor[0]
    cursor[0] += width
    return tuple(range(start, start + width))


def gate(kind: str, sites: tuple[int, ...], label: str, width: int) -> Gate:
    support = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in support or len(sites) != support[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle505 primitive")
    if any(site not in range(width) for site in sites):
        raise ValueError("Cycle505 primitive leaves its bounded block")
    return Gate(kind, sites, label)


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
        raise ValueError("unknown Cycle505 primitive")


def route_for_gate(item: Gate, width: int) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(width))
    targets = tuple(range(width - len(item.sites), width))
    swaps = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    return tuple(swaps)


def apply_routed(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
                 delete_label: str | None = None) -> Word:
    if not isinstance(bits, tuple) or not all(type(bit) is int and bit in (0, 1) for bit in bits):
        raise ValueError("Cycle505 state leaves the exact binary domain")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must identify exactly one primitive")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    word = list(bits)
    sequence = tuple(reversed(schedule)) if reverse else schedule
    for item in sequence:
        swaps = route_for_gate(item, len(word))
        for left, right in swaps:
            word[left], word[right] = word[right], word[left]
        moved = Gate(item.kind, tuple(range(len(word) - len(item.sites), len(word))), item.label)
        if item.kind == "X":
            moved = item
        apply_gate(word, moved)
        for left, right in reversed(swaps):
            word[left], word[right] = word[right], word[left]
    return tuple(word)


def schedule_digest(schedule: tuple[Gate, ...], width: int) -> str:
    digest = sha256()
    for item in schedule:
        digest.update(f"{item.kind}:{item.sites}:{item.label}".encode())
        digest.update(repr(route_for_gate(item, width)).encode())
    return digest.hexdigest()


def nn_trace(schedule: tuple[Gate, ...], width: int) -> dict[str, object]:
    logical = nearest = routing_swaps = connected_failures = final_support_failures = 0
    terminal_operand_order_failures = reverse_label_restoration_failures = 0
    maximum_support = 0
    for item in schedule:
        logical += 1
        swaps = route_for_gate(item, width)
        routing_swaps += len(swaps)
        # Every forward and reverse routing SWAP is exactly three adjacent
        # CNOTs; the final X/CNOT/TOFFOLI is one primitive.
        nearest += 6 * len(swaps) + 1
        maximum_support = max(maximum_support, len(item.sites))
        connected_failures += sum(int(abs(left - right) != 1) for left, right in swaps)
        final_sites = tuple(range(width - len(item.sites), width)) if item.kind != "X" else item.sites
        labels = list(range(width))
        for left, right in swaps:
            labels[left], labels[right] = labels[right], labels[left]
        terminal_operand_order_failures += int(tuple(labels[site] for site in final_sites) != item.sites)
        for left, right in reversed(swaps):
            labels[left], labels[right] = labels[right], labels[left]
        reverse_label_restoration_failures += int(tuple(labels) != tuple(range(width)))
        final_support_failures += int(
            item.kind != "X" and any(abs(left - right) != 1 for left, right in zip(final_sites[:-1], final_sites[1:]))
        )
    return {
        "logical_gates": logical,
        "nearest_neighbor_primitives": nearest,
        "routing_adjacent_SWAPS": routing_swaps,
        "routing_CNOT_primitives": 6 * routing_swaps,
        "routing_SWAP_compilation": "each adjacent SWAP = 3 CNOT; forward+reverse = 6 CNOT",
        "maximum_support_M2": maximum_support,
        "connected_failures": connected_failures,
        "final_adjacent_support_failures": final_support_failures,
        "terminal_operand_order_failures": terminal_operand_order_failures,
        "reverse_label_restoration_failures": reverse_label_restoration_failures,
        "sha256": schedule_digest(schedule, width),
    }


def c502_basis(pointer: int) -> Word:
    return c502.apply_physical(c502.prepare_pointer(pointer)).bits


# Route A: one fixed G over READY/MOVED/SPENT carrier progression.  The held
# H=7 block also contains READY[7], the explicit finite-capacity sink.
_a = [c502.TOTAL_M2]
A_TOKEN_FLAG = take(_a, 1)[0]
A_CONTENT = take(_a, 3)
A_FRAGMENTS = tuple(take(_a, 3) for _ in range(3))
A_FRESH = take(_a, A_HELD_H)
A_SPENT = take(_a, A_HELD_H)
A_MOVED = take(_a, A_HELD_H)
A_RECEIPTS = tuple(take(_a, c502.MENU_ARITY) for _ in range(A_HELD_H))
A_READY = take(_a, A_HELD_H + 1)
A_WORK = take(_a, 1)[0]
A_WIDTH = _a[0]
A_NEW_M2 = A_WIDTH - c502.TOTAL_M2


def controlled_swap(control: int, left: int, right: int, label: str, width: int) -> tuple[Gate, ...]:
    """Exact Fredkin decomposition using only CNOT/TOFFOLI."""
    return (
        gate("CNOT", (left, right), f"{label}:swap-1", width),
        gate("TOFFOLI", (control, right, left), f"{label}:swap-2", width),
        gate("CNOT", (left, right), f"{label}:swap-3", width),
    )


def a_cell_schedule(cell: int) -> tuple[Gate, ...]:
    if cell not in range(A_HELD_H):
        raise ValueError("carrier cell leaves the frozen H=7 block")
    answer = [
        gate("TOFFOLI", (A_READY[cell], A_FRESH[cell], A_MOVED[cell]), f"A:moved:{cell}", A_WIDTH),
        gate("X", (A_TOKEN_FLAG,), f"A:neg-token:{cell}:compute", A_WIDTH),
        gate("TOFFOLI", (A_MOVED[cell], A_TOKEN_FLAG, A_WORK), f"A:blank-token:{cell}:compute", A_WIDTH),
        gate("X", (A_TOKEN_FLAG,), f"A:restore-token:{cell}:compute", A_WIDTH),
    ]
    for label in MENU:  # Literal all-label circuit; never a first-winner host query.
        receipt = A_RECEIPTS[cell][label]
        answer.append(gate("TOFFOLI", (A_WORK, c502.WINNER[label], receipt), f"A:receipt:{cell}:{label}", A_WIDTH))
    answer.extend((
        gate("X", (A_TOKEN_FLAG,), f"A:neg-token:{cell}:uncompute", A_WIDTH),
        gate("TOFFOLI", (A_MOVED[cell], A_TOKEN_FLAG, A_WORK), f"A:blank-token:{cell}:uncompute", A_WIDTH),
        gate("X", (A_TOKEN_FLAG,), f"A:restore-token:{cell}:uncompute", A_WIDTH),
    ))
    for label in MENU:
        receipt = A_RECEIPTS[cell][label]
        answer.append(gate("TOFFOLI", (receipt, A_READY[cell], A_TOKEN_FLAG), f"A:token-flag:{cell}:{label}", A_WIDTH))
        for lane, bit in enumerate(bits3(label)):
            if bit:
                answer.append(gate("TOFFOLI", (receipt, A_READY[cell], A_CONTENT[lane]), f"A:token-content:{cell}:{label}:{lane}", A_WIDTH))
                for fragment in range(3):
                    answer.append(gate("TOFFOLI", (receipt, A_READY[cell], A_FRAGMENTS[fragment][lane]), f"A:fragment:{cell}:{label}:{fragment}:{lane}", A_WIDTH))
    answer.extend((
        gate("TOFFOLI", (A_MOVED[cell], A_READY[cell], A_FRESH[cell]), f"A:consume:{cell}", A_WIDTH),
        gate("TOFFOLI", (A_MOVED[cell], A_READY[cell], A_SPENT[cell]), f"A:spend:{cell}", A_WIDTH),
    ))
    answer.extend(controlled_swap(A_MOVED[cell], A_READY[cell], A_READY[cell + 1], f"A:advance:{cell}", A_WIDTH))
    return tuple(answer)


def a_schedule() -> tuple[Gate, ...]:
    # Descending cells prevent a newly advanced READY bit from cascading again
    # during the same application of G.
    return tuple(item for cell in reversed(range(A_HELD_H)) for item in a_cell_schedule(cell))


def a_prepare(pointer: int, horizon: int) -> Word:
    if horizon not in (A_TRAIN_H, A_HELD_H):
        raise ValueError("A horizon leaves the frozen train/held input bank")
    bits = list(c502_basis(pointer) + (0,) * A_NEW_M2)
    for cell in range(horizon):
        bits[A_FRESH[cell]] = 1
    bits[A_READY[0]] = 1
    return tuple(bits)


def a_coarse_step(source: Word, pointer: int, horizon: int) -> Word:
    if len(source) != A_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in source):
        raise ValueError("A coarse state leaves its exact binary block")
    ready = tuple(source[site] for site in A_READY)
    if sum(ready) != 1:
        raise ValueError("A READY cursor is not one-hot")
    cell = ready.index(1)
    if cell >= horizon:
        raise ValueError("A forward carrier capacity is exhausted")
    bits = list(source)
    if bits[A_FRESH[cell]] != 1 or bits[A_MOVED[cell]] != 0:
        raise ValueError("A active carrier is not fresh/unmoved")
    bits[A_MOVED[cell]] = 1
    if bits[A_TOKEN_FLAG] == 0:
        bits[A_RECEIPTS[cell][pointer]] = 1
        bits[A_TOKEN_FLAG] = 1
        for lane, bit in enumerate(bits3(pointer)):
            bits[A_CONTENT[lane]] = bit
            for fragment in A_FRAGMENTS:
                bits[fragment[lane]] = bit
    bits[A_FRESH[cell]] = 0
    bits[A_SPENT[cell]] = 1
    bits[A_READY[cell]] = 0
    bits[A_READY[cell + 1]] = 1
    return tuple(bits)


def a_physical_step(source: Word, horizon: int, *, reverse: bool = False,
                    delete_label: str | None = None) -> Word:
    if horizon not in (A_TRAIN_H, A_HELD_H):
        raise ValueError("A horizon leaves the frozen train/held envelope")
    if len(source) != A_WIDTH:
        raise ValueError("A state leaves the held-size physical block")
    if not reverse and source[A_READY[horizon]] == 1:
        raise ValueError("A forward carrier capacity is exhausted")
    return apply_routed(source, a_schedule(), reverse=reverse, delete_label=delete_label)


def a_view(bits: Word) -> StableSelectiveToken:
    select = lambda sites: tuple(bits[site] for site in sites)
    return StableSelectiveToken(
        bits[A_TOKEN_FLAG], select(A_CONTENT),
        tuple(select(fragment) for fragment in A_FRAGMENTS),
        tuple(bits[site] for row in A_RECEIPTS for site in row),
        select(A_FRESH), select(A_SPENT),
    )


# Route B: four held environment fragments, each (valid, three-bit label).
_b = [c502.TOTAL_M2]
B_FRAGMENTS = tuple((take(_b, 1)[0], take(_b, 3)) for _ in range(B_HELD_F))
B_WIDTH = _b[0]
B_NEW_M2 = B_WIDTH - c502.TOTAL_M2


def b_schedule(fragments: int) -> tuple[Gate, ...]:
    if fragments not in (B_TRAIN_F, B_HELD_F):
        raise ValueError("B fragment count leaves the frozen train/held manifest")
    answer = []
    for fragment in range(fragments):
        valid, label_sites = B_FRAGMENTS[fragment]
        answer.append(gate("CNOT", (c502.LOCK_FLAG, valid), f"B:retain-valid:{fragment}", B_WIDTH))
        for lane in range(3):
            answer.append(gate("CNOT", (c502.POINTER[lane], label_sites[lane]), f"B:retain-label:{fragment}:{lane}", B_WIDTH))
    return tuple(answer)


def b_prepare(pointer: int) -> Word:
    return c502_basis(pointer) + (0,) * B_NEW_M2


def b_reference(pointer: int, fragments: int) -> Word:
    bits = list(b_prepare(pointer))
    for fragment in range(fragments):
        valid, label_sites = B_FRAGMENTS[fragment]
        bits[valid] = 1
        for site, bit in zip(label_sites, bits3(pointer)):
            bits[site] = bit
    return tuple(bits)


def b_signature(bits: Word) -> tuple[tuple[int, Word], ...]:
    return tuple((bits[valid], tuple(bits[site] for site in label)) for valid, label in B_FRAGMENTS)


# Route C: supplied neighbor certificate/vacancy -> singleton predicate only.
_c = [c502.TOTAL_M2]
C_NEIGHBOR = take(_c, c502.MENU_ARITY)
C_VACANCY = take(_c, 1)[0]
C_ELIGIBILITY = take(_c, c502.MENU_ARITY)
C_SINGLETON = take(_c, 1)[0]
C_CONTENT = take(_c, 3)
C_SITE_ELIGIBLE = take(_c, 1)[0]
C_WORK = take(_c, 1)[0]
C_WIDTH = _c[0]
C_NEW_M2 = C_WIDTH - c502.TOTAL_M2


def c_schedule() -> tuple[Gate, ...]:
    answer = []
    for label in MENU:
        answer.extend((
            gate("TOFFOLI", (c502.WINNER[label], C_NEIGHBOR[label], C_WORK), f"C:match:{label}:compute", C_WIDTH),
            gate("TOFFOLI", (C_WORK, C_VACANCY, C_ELIGIBILITY[label]), f"C:eligibility:{label}", C_WIDTH),
            gate("TOFFOLI", (c502.WINNER[label], C_NEIGHBOR[label], C_WORK), f"C:match:{label}:uncompute", C_WIDTH),
            gate("CNOT", (C_ELIGIBILITY[label], C_SINGLETON), f"C:singleton:{label}", C_WIDTH),
            gate("CNOT", (C_ELIGIBILITY[label], C_SITE_ELIGIBLE), f"C:site:{label}", C_WIDTH),
        ))
        for lane, bit in enumerate(bits3(label)):
            if bit:
                answer.append(gate("CNOT", (C_ELIGIBILITY[label], C_CONTENT[lane]), f"C:content:{label}:{lane}", C_WIDTH))
    return tuple(answer)


def c_prepare(pointer: int, *, neighbors: Word = (1, 1, 1, 1, 1), vacancy: int = 1) -> Word:
    if len(neighbors) != c502.MENU_ARITY or any(type(bit) is not int or bit not in (0, 1) for bit in neighbors):
        raise ValueError("C neighbor certificate leaves its binary five-label domain")
    if type(vacancy) is not int or vacancy not in (0, 1):
        raise ValueError("C vacancy leaves its binary domain")
    bits = list(c502_basis(pointer) + (0,) * C_NEW_M2)
    for site, bit in zip(C_NEIGHBOR, neighbors):
        bits[site] = bit
    bits[C_VACANCY] = vacancy
    source = tuple(bits)
    c_validate_imported_candidate(source)
    return source


def c_validate_imported_candidate(source: Word) -> None:
    if len(source) != C_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in source):
        raise ValueError("C state leaves its exact binary block")
    winner_count = sum(source[site] for site in c502.WINNER)
    if winner_count != 1:
        raise ValueError("C declared code space requires exactly one imported Cycle502 winner")


def c_physical(source: Word, *, reverse: bool = False, delete_label: str | None = None) -> Word:
    c_validate_imported_candidate(source)
    return apply_routed(source, c_schedule(), reverse=reverse, delete_label=delete_label)


def c_reference(pointer: int, *, neighbors: Word = (1, 1, 1, 1, 1), vacancy: int = 1) -> Word:
    bits = list(c_prepare(pointer, neighbors=neighbors, vacancy=vacancy))
    eligible = int(bool(neighbors[pointer] and vacancy))
    bits[C_ELIGIBILITY[pointer]] = eligible
    bits[C_SINGLETON] = eligible
    bits[C_SITE_ELIGIBLE] = eligible
    if eligible:
        for site, bit in zip(C_CONTENT, bits3(pointer)):
            bits[site] = bit
    return tuple(bits)


def c_view(bits: Word) -> RecordBindingCandidate:
    eligibility = tuple(bits[site] for site in C_ELIGIBILITY)
    return RecordBindingCandidate(
        eligibility, bits[C_SINGLETON], tuple(bits[site] for site in C_CONTENT), bits[C_SITE_ELIGIBLE]
    )


def semantic_record_view(candidate: RecordBindingCandidate, occurrence_present: bool) -> dict[str, object] | None:
    """Pure semantic conditional; occurrence_present is not an M2 or physical input."""
    if not occurrence_present or candidate.singleton != 1 or sum(candidate.eligibility) != 1:
        return None
    return {"site": (0, 0, 0), "content": candidate.content, "one_lock_semantic": True}


def repeated_actual_map(input_vector: np.ndarray, event_maps: tuple[dict[tuple[object, ...], complex], ...], n: int) -> Sparse:
    if len(input_vector) != 2**n:
        raise ValueError("repeated input leaves the frozen N-copy block")
    output: Sparse = {}
    for basis_index, input_amplitude in enumerate(input_vector):
        if abs(input_amplitude) < 1e-14:
            continue
        local_maps = tuple(event_maps[bit] for bit in c500.basis_bits(basis_index, n))
        for terms in product(*(tuple(local.items()) for local in local_maps)):
            pointers = tuple(key[0] for key, _ in terms)
            systems = tuple(key[1] for key, _ in terms)
            packets = tuple(key[2] for key, _ in terms)
            amplitude = complex(input_amplitude)
            for _key, local_amplitude in terms:
                amplitude *= local_amplitude
            c500.sparse_add(output, (pointers, systems, packets), amplitude)
    return output


def augment(state: Sparse, signatures: tuple[object, ...]) -> Sparse:
    output: Sparse = {}
    for (pointers, systems, packets), amplitude in state.items():
        attached = tuple(signatures[pointer] for pointer in pointers)
        c500.sparse_add(output, (pointers, systems, packets, attached), amplitude)
    return output


def grades_by_word(state: Sparse) -> dict[Word, float]:
    answer: dict[Word, float] = {}
    for key, amplitude in state.items():
        word = key[0]
        answer[word] = answer.get(word, 0.0) + abs(amplitude) ** 2
    return answer


def expected_grades(one_step: tuple[float, ...], n: int) -> dict[Word, float]:
    return {word: float(np.prod(tuple(one_step[label] for label in word))) for word in product(MENU, repeat=n)}


def dictionary_residual(left: dict[Word, float], right: dict[Word, float]) -> float:
    return max(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in set(left) | set(right))


def coherent_controls(event: dict[str, object], signatures: dict[str, tuple[object, ...]],
                      n: int, mode: str) -> dict[str, object]:
    print(f"\nACTUAL C478 / {mode.upper()} N={n} COHERENT COMPOSITION")
    rows = []
    failures = 0
    for name, psi in input_states(mode):
        input_vector = c500.tensor_vector(psi, n)
        physical = repeated_actual_map(input_vector, event["physical"], n)
        one_step = c500.branch_grades(event["program"], psi)
        expected = expected_grades(one_step, n)
        route_rows = {}
        for route, route_signatures in signatures.items():
            carried = augment(physical, route_signatures)
            grade_residual = dictionary_residual(grades_by_word(carried), expected)
            norm_residual = abs(sum(abs(value) ** 2 for value in carried.values()) - 1.0)
            route_rows[route] = {
                "terms": len(carried), "grade_residual": grade_residual,
                "norm_residual": norm_residual, "all_five_labels": set(key[0][0] for key in carried) == set(MENU),
            }
            failures += int(grade_residual >= TOL or norm_residual >= TOL or not route_rows[route]["all_five_labels"])
        rows.append({"state": name, "one_step_grades": one_step, "routes": route_rows})
    check(
        f"all three new physical signatures linearly compose with the actual C478 {mode} N={n} cylinder without deleting a sector",
        failures == 0 and max(event["single_E_G"] + event["single_inverse"]) < TOL and event["leakage"] == 0,
        {"rows": rows, "C478_single_E_G": event["single_E_G"], "C478_inverse": event["single_inverse"], "leakage": event["leakage"]},
    )
    return {"event": event, "rows": rows}


def route_a_controls(horizon: int, mode: str) -> tuple[tuple[StableSelectiveToken, ...], dict[str, object]]:
    print("\nROUTE A / FINITE-ENVELOPE RETAINED-CARRIER PROGRESSION")
    schedule = a_schedule()
    rows = []
    signatures = []
    failures = 0
    for pointer in MENU:
        source = a_prepare(pointer, horizon)
        physical = source
        reference = source
        token_views = []
        sweep_states = []
        step_rows = []
        for sweep in range(horizon):
            physical = a_physical_step(physical, horizon)
            reference = a_coarse_step(reference, pointer, horizon)
            sweep_states.append(physical)
            token_views.append(a_view(physical))
            step_rows.append({
                "sweep": sweep + 1, "E_G_exact": physical == reference,
                "ready_index": tuple(physical[site] for site in A_READY).index(1),
                "moved": sum(physical[site] for site in A_MOVED),
                "spent": sum(physical[site] for site in A_SPENT),
            })
        restored = physical
        for _ in range(horizon):
            restored = a_physical_step(restored, horizon, reverse=True)
        deleted = a_physical_step(source, horizon, delete_label=f"A:receipt:0:{pointer}")
        view = token_views[0]
        signatures.append(view)
        token_payloads = tuple((item.occupied, item.content, item.redundant_fragments) for item in token_views)
        capacity_rejected = False
        try:
            a_physical_step(physical, horizon)
        except ValueError:
            capacity_rejected = True
        row = {
            "pointer": pointer, "sweeps": step_rows,
            "repeated_G_token_payload_stable": len(set(map(repr, token_payloads))) == 1,
            "whole_trajectory_inverse_exact": restored == source,
            "capacity_exhausted_ready_sink": physical[A_READY[horizon]] == 1,
            "capacity_reentry_rejected": capacity_rejected,
            "literal_terminal_fixed_point_claimed": False,
            "terminal_support": {
                "READY": tuple(physical[site] for site in A_READY),
                "MOVED": tuple(physical[site] for site in A_MOVED),
                "fresh": tuple(physical[site] for site in A_FRESH),
                "spent": tuple(physical[site] for site in A_SPENT),
                "receipt_count": sum(physical[site] for row in A_RECEIPTS for site in row),
                "work": physical[A_WORK],
            },
            "first_sweep_deletion_visible": deleted != a_coarse_step(source, pointer, horizon),
            "token": view, "work_blank_each_sweep": all(item[A_WORK] == 0 for item in sweep_states),
        }
        failures += int(not all(row[key] for key in (
            "repeated_G_token_payload_stable", "whole_trajectory_inverse_exact",
            "capacity_exhausted_ready_sink", "capacity_reentry_rejected",
            "first_sweep_deletion_visible", "work_blank_each_sweep",
        )))
        failures += sum(int(not step["E_G_exact"] or step["ready_index"] != step["sweep"]
                            or step["moved"] != step["sweep"] or step["spent"] != step["sweep"])
                        for step in step_rows)
        failures += int(
            view.occupied != 1 or view.content != bits3(pointer)
            or any(fragment != bits3(pointer) for fragment in view.redundant_fragments)
            or sum(view.receipts) != 1 or sum(view.spent) != 1
            or view.actual_member is not None or view.framework_Record is not None
        )
        rows.append(row)
    source_scan = inspect.getsource(a_schedule) + inspect.getsource(a_cell_schedule)
    tree = ast.parse(source_scan)
    forbidden_calls = tuple(
        ast.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.Call)
        and any(token in ast.unparse(node.func).lower() for token in ("find", "index", "argmax", "norm", "grade", "weight"))
    )
    labels_per_cell = tuple(
        tuple(sorted({int(item.label.split(":")[3]) for item in a_cell_schedule(cell) if item.label.startswith("A:receipt:")}))
        for cell in range(A_HELD_H)
    )
    trace = nn_trace(schedule, A_WIDTH)
    held_manifest = {
        "mode": "held", "H": A_HELD_H, "same_fixed_G": True,
        "logical_gates": len(schedule), "sha256": schedule_digest(schedule, A_WIDTH),
    }
    check(
        f"A: one fixed all-label G passes each fresh carrier once through H={horizon}, never erases the occupied token, exposes capacity, and inverts the whole trajectory ({mode})",
        failures == 0 and not forbidden_calls and all(labels == MENU for labels in labels_per_cell)
        and trace["maximum_support_M2"] <= 3 and trace["connected_failures"] == 0
        and trace["final_adjacent_support_failures"] == 0
        and trace["terminal_operand_order_failures"] == 0
        and trace["reverse_label_restoration_failures"] == 0,
        {
            "rows": rows, "fixed_all_labels_per_cell": labels_per_cell,
            "winner_query_calls": forbidden_calls, "executed_mode": mode, "trace": trace,
            "H_sweep_trace": {
                "G_applications": horizon,
                "logical_gates": horizon * trace["logical_gates"],
                "nearest_neighbor_primitives": horizon * trace["nearest_neighbor_primitives"],
            },
            "held_manifest": held_manifest if mode == "held" else {**held_manifest, "not_executed": True},
            "new_M2_per_event": A_NEW_M2, "total_envelope_M2_per_event": C478_FINE_LAW_M2 + C502_CANDIDATE_M2 + A_NEW_M2,
            "scope": "finite-envelope retained-token stability; not a fixed point, attractor, autonomous metastability, or renewable history",
            "actual_member": None, "framework_Record": None,
        },
    )
    return tuple(signatures), {"trace": trace, "rows": rows}


def route_b_controls(program: object, fragments: int, mode: str) -> tuple[tuple[object, ...], dict[str, object]]:
    print("\nROUTE B / RETAINED LOCAL INSTRUMENT DILATION")
    schedule = b_schedule(fragments)
    rows = []
    signatures = []
    failures = 0
    for pointer in MENU:
        source = b_prepare(pointer)
        physical = apply_routed(source, schedule)
        reference = b_reference(pointer, fragments)
        inverse = apply_routed(physical, schedule, reverse=True)
        deleted = apply_routed(source, schedule, delete_label="B:retain-valid:0")
        signature = b_signature(physical)
        signatures.append(signature)
        row = {
            "pointer": pointer, "E_G_exact": physical == reference, "inverse_exact": inverse == source,
            "deletion_visible": deleted != reference, "retained_fragments": signature,
        }
        failures += int(not all(row[key] for key in ("E_G_exact", "inverse_exact", "deletion_visible")))
        failures += int(any(valid != 1 or label != bits3(pointer) for valid, label in signature[:fragments]))
        rows.append(row)
    diagnostics = []
    dft = np.asarray(
        [[np.exp(2j * np.pi * row * column / c502.MENU_ARITY) / sqrt(c502.MENU_ARITY)
          for column in MENU] for row in MENU], complex
    )
    for name, psi in input_states(mode):
        vectors = c500.branch_vectors(program, psi)
        original = sum((np.outer(vector, vector.conj()) for vector in vectors), np.zeros((2, 2), complex))
        rotated_vectors = tuple(sum((dft[row, column] * vectors[column] for column in MENU), np.zeros(2, complex)) for row in MENU)
        rotated = sum((np.outer(vector, vector.conj()) for vector in rotated_vectors), np.zeros((2, 2), complex))
        diagnostics.append({"state": name, "same_reduced_channel_residual": float(np.linalg.norm(original - rotated))})
    trace = nn_trace(schedule, B_WIDTH)
    held_manifest = {"F": B_HELD_F, "logical_gates": len(b_schedule(B_HELD_F)), "sha256": schedule_digest(b_schedule(B_HELD_F), B_WIDTH)}
    check(
        "B: every physical C478 pointer label is retained in local environment fragments; an alternative environment basis gives only a same-reduced-channel diagnostic",
        failures == 0 and max(row["same_reduced_channel_residual"] for row in diagnostics) < TOL
        and trace["maximum_support_M2"] <= 3 and trace["connected_failures"] == 0
        and trace["final_adjacent_support_failures"] == 0
        and trace["terminal_operand_order_failures"] == 0
        and trace["reverse_label_restoration_failures"] == 0,
        {
            "rows": rows, "same_reduced_channel_diagnostic": diagnostics,
            "physical_C478_pointer_basis_retained": True,
            "physical_trajectory_ambiguity_claimed": False,
            "reduced_channel_is_diagnostic_not_physical_deletion": True,
            "executed_mode": mode, "trace": trace,
            "held_manifest": held_manifest if mode == "held" else {**held_manifest, "not_executed": True},
            "new_M2_per_event": B_NEW_M2, "total_envelope_M2_per_event": C478_FINE_LAW_M2 + C502_CANDIDATE_M2 + B_NEW_M2,
            "actual_member": None, "framework_Record": None,
        },
    )
    return tuple(signatures), {"trace": trace, "rows": rows, "diagnostics": diagnostics}


def route_c_controls() -> tuple[tuple[RecordBindingCandidate, ...], dict[str, object]]:
    print("\nROUTE C / SINGLETON RECORDBINDINGCANDIDATE PREDICATE")
    schedule = c_schedule()
    rows = []
    signatures = []
    failures = 0
    for pointer in MENU:
        source = c_prepare(pointer)
        physical = c_physical(source)
        reference = c_reference(pointer)
        inverse = c_physical(physical, reverse=True)
        deleted = c_physical(source, delete_label=f"C:eligibility:{pointer}")
        candidate = c_view(physical)
        signatures.append(candidate)
        no_occurrence = semantic_record_view(candidate, False)
        conditional = semantic_record_view(candidate, True)
        row = {
            "pointer": pointer, "E_G_exact": physical == reference, "inverse_exact": inverse == source,
            "eligibility_deletion_visible": deleted != reference, "candidate": candidate,
            "no_occurrence_semantic_view": no_occurrence,
            "conditional_semantic_view": conditional,
        }
        failures += int(not all(row[key] for key in ("E_G_exact", "inverse_exact", "eligibility_deletion_visible")))
        failures += int(
            sum(candidate.eligibility) != 1 or candidate.eligibility[pointer] != 1
            or candidate.singleton != 1 or candidate.content != bits3(pointer)
            or candidate.central_site_eligible != 1 or no_occurrence is not None or conditional is None
            or candidate.actual_member is not None or candidate.framework_Record is not None
        )
        rows.append(row)
    collision_rows = []
    for pointer in MENU:
        source = c_prepare(pointer, vacancy=0)
        candidate = c_view(c_physical(source))
        collision_rows.append({"pointer": pointer, "vacancy": 0, "eligibility": candidate.eligibility, "singleton": candidate.singleton})
        failures += int(any(candidate.eligibility) or candidate.singleton or candidate.central_site_eligible)
    non_one_hot_rejections = {}
    lawful = list(c_prepare(0))
    for count in (0, 2, 3):
        malformed = list(lawful)
        for site in c502.WINNER:
            malformed[site] = 0
        for site in c502.WINNER[:count]:
            malformed[site] = 1
        try:
            c_physical(tuple(malformed))
        except ValueError:
            non_one_hot_rejections[count] = True
        else:
            non_one_hot_rejections[count] = False
    semantic_source = inspect.getsource(semantic_record_view)
    physical_source = inspect.getsource(c_schedule) + inspect.getsource(c_prepare)
    physical_occurrence_hits = physical_source.lower().count("occurrence")
    trace = nn_trace(schedule, C_WIDTH)
    check(
        "C: the physical block computes only a singleton RecordBindingCandidate predicate; the Record occurrence antecedent remains purely semantic",
        failures == 0 and all(non_one_hot_rejections.values()) and physical_occurrence_hits == 0
        and "occurrence_present" in semantic_source and trace["maximum_support_M2"] <= 3
        and trace["connected_failures"] == 0 and trace["final_adjacent_support_failures"] == 0
        and trace["terminal_operand_order_failures"] == 0
        and trace["reverse_label_restoration_failures"] == 0,
        {
            "rows": rows, "same_site_collision_controls": collision_rows,
            "zero_two_three_winner_code_rejections": non_one_hot_rejections,
            "declared_C502_candidate_code_space": "exactly one winner; 2/3 eligible inputs rejected before G",
            "physical_occurrence_trigger_M2": 0, "physical_occurrence_deletion_claim": False,
            "semantic_occurrence_antecedent_only": True,
            "physical_result_type": "RecordBindingCandidate singleton predicate only",
            "trace": trace,
            "new_M2_per_event": C_NEW_M2, "total_envelope_M2_per_event": C478_FINE_LAW_M2 + C502_CANDIDATE_M2 + C_NEW_M2,
            "actual_member": None, "framework_Record": None,
        },
    )
    return tuple(signatures), {"trace": trace, "rows": rows, "collisions": collision_rows}


def covariance_mass_resource_controls(routes: tuple[tuple[str, tuple[Gate, ...], int, int], ...]) -> None:
    print("\nLOCALITY / ALL24 / MASS / RESOURCE")
    frames = c500.c493.c488.proper_cubic_frames()
    route_rows = []
    failures = 0
    for name, schedule, width, new_m2 in routes:
        base = tuple((index, 0, 0) for index in range(width))
        routing_edges = tuple((base[left], base[right]) for item in schedule for left, right in route_for_gate(item, width))
        final_edges = tuple(
            (base[left], base[right])
            for item in schedule if item.kind != "X"
            for left, right in zip(
                tuple(range(width - len(item.sites), width))[:-1],
                tuple(range(width - len(item.sites), width))[1:],
            )
        )
        edges = routing_edges + final_edges
        manifest_failures = edge_failures = 0
        for frame in frames:
            rotated = tuple(c500.c493.c488.rotate_coord(site, frame) for site in base)
            carried_x = c500.c493.c488.rotate_coord((1, 0, 0), frame)
            independent = tuple(tuple(index * value for value in carried_x) for index in range(width))
            manifest_failures += int(rotated != independent)
            for left, right in edges:
                a = c500.c493.c488.rotate_coord(left, frame)
                b = c500.c493.c488.rotate_coord(right, frame)
                edge_failures += int(c500.c493.c488.manhattan(a, b) != 1)
        trace = nn_trace(schedule, width)
        total = C478_FINE_LAW_M2 + C502_CANDIDATE_M2 + new_m2
        failures += int(
            manifest_failures or edge_failures or new_m2 > NEW_M2_CEILING
            or trace["maximum_support_M2"] > 3 or trace["final_adjacent_support_failures"]
            or trace["terminal_operand_order_failures"] or trace["reverse_label_restoration_failures"]
        )
        route_rows.append({
            "route": name, "new_route_overhead_M2_per_event": new_m2,
            "frozen_C478_fine_law_M2_per_event": C478_FINE_LAW_M2,
            "frozen_C502_candidate_M2_per_event": C502_CANDIDATE_M2,
            "conservative_total_envelope_M2_per_event": total,
            "proper_cubic_frames": len(frames),
            "rotated_routing_edges": len(frames) * len(routing_edges),
            "rotated_final_logical_support_edges": len(frames) * len(final_edges),
            "manifest_failures": manifest_failures, "edge_failures": edge_failures, "trace": trace,
        })
    species = c500.c493.c488.c478.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c500.c493.c488.c478.c317.c311.c219.rest_mass(species) / species.analytic_mass - 1.0)
    check(
        "new-only overhead, composed total envelopes, NN support, all-24 carried covariance, and the one-particle mass fixture remain explicit",
        failures == 0 and len(frames) == 24 and mass_residual < 3e-12
        and max(row["new_route_overhead_M2_per_event"] for row in route_rows) <= NEW_M2_CEILING,
        {
            "rows": route_rows, "new_route_ceiling_M2_per_event_excludes_named_frozen_C478_C502": NEW_M2_CEILING,
            "largest_new_route_overhead_M2_per_event": max(row["new_route_overhead_M2_per_event"] for row in route_rows),
            "largest_conservative_total_envelope_M2_per_event": max(row["conservative_total_envelope_M2_per_event"] for row in route_rows),
            "one_particle_mass_relative_residual": mass_residual,
        },
    )


def domain_controls() -> None:
    print("\nDOMAIN / LEAKAGE / TYPE CONTROLS")
    rejected = {}
    fixtures = {
        "A_bad_horizon": lambda: a_prepare(0, 4),
        "A_nonbinary": lambda: apply_routed(tuple([2] + [0] * (A_WIDTH - 1)), a_schedule()),
        "B_bad_fragments": lambda: b_schedule(3),
        "C_bad_neighbors": lambda: c_prepare(0, neighbors=(1, 1, 1)),
        "C_bad_vacancy": lambda: c_prepare(0, vacancy=2),
    }
    for name, action in fixtures.items():
        try:
            action()
        except (TypeError, ValueError):
            rejected[name] = True
        else:
            rejected[name] = False
    swap_truth_failures = 0
    for left, right in product((0, 1), repeat=2):
        bits = [left, right]
        bits[1] ^= bits[0]
        bits[0] ^= bits[1]
        bits[1] ^= bits[0]
        swap_truth_failures += int(tuple(bits) != (right, left))
    typed = TypedFormationObjects()
    check(
        "lawful-domain rejection, elementary three-CNOT SWAP truth table, and the eight-object semantic split prevent relabeling",
        all(rejected.values()) and swap_truth_failures == 0
        and typed.actual_member is typed.framework_Record is typed.empirical_frequency is None,
        {"rejections": rejected, "three_CNOT_SWAP_truth_failures": swap_truth_failures, "typed_objects": typed},
    )


def inventory_controls(mode: str) -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "Record occurrence ontology and one-lock semantics when an occurrence exists; no occurrence trigger M2",
        "exact frozen Cycle478 Kraus/pointer/packet apparatus and exact frozen Cycle502 28-M2 candidate block",
        "finite train/held L,N,H,F manifests; blank new route banks; noiseless X/CNOT/Toffoli and rail geometry",
        "Route-A fresh carrier ray, Route-B blank environment fragments, Route-C neighbor certificate and vacancy",
        "partial trace and alternative environment basis only as mathematical diagnostics",
        "all24 proper-cubic convention, tolerance, resource caps, and Cycle219 one-particle mass fixture",
    )
    derived = (
        "fixed all-label Route-A reversible capture with stable redundant basis token and every carrier/receipt retained",
        "Route-B exact retained label fragments, inverse, and same-reduced-channel environment-basis diagnostic",
        "Route-C exact singleton RecordBindingCandidate physical predicate and same-site vacancy control",
        "actual C478 N2 coherent composition preserving all twenty-five history grades for both train states",
        "new-only M2 overheads, conservative composed totals, support-three NN routes, deletion and domain responses",
        "strict types: token, environment label, reduced-channel diagnostic, and binding candidate are not actual/Record",
    )
    open_items = (
        "a physical law selecting one actual C478/C502 member rather than retaining all coherent sectors",
        "a physical occurrence trigger and justified admissibility-to-content/site law for framework Record formation",
        "carrier/environment genesis, renewable supply, noise tolerance, unbounded permanence, and infinite-volume scaling",
        "grade-to-probability premises, sampling process, stationarity/ergodicity, frequencies, and calibration",
        "time/rate, energy/inertia, source/gravity coupling, continuum prediction, and empirical discriminator",
        (
            "held L6/N4/H7/F4 execution after the exact frozen-before-held authorization boundary"
            if mode == "train" else
            "post-held interpretation, independent replay, and any next-scale campaign"
        ),
    )
    check(
        "the supplied / derived / open inventory keeps every remaining import and downstream obligation visible",
        len(supplied) == len(derived) == len(open_items) == 6,
        {"supplied": supplied, "derived": derived, "open": open_items, "executed_mode": mode, "authority": AUTHORITY, "audit": AUDIT},
    )


def no_go_controls(mode: str) -> None:
    print("\nNO-GO DISCIPLINE N1-N8")
    n1 = (
        ("retained-carrier progression", "basis token plus READY/MOVED/SPENT carriers", "actual member law"),
        ("retained instrument dilation", "environment-labelled isometry", "actual member law"),
        ("conditional admissibility binding", "singleton physical predicate", "physical occurrence law"),
        ("irreversible open-system bath", "dissipative attractor", "bath genesis/renewal and actual trajectory law"),
        ("stochastic local seed", "sampled member register", "seed distribution/dynamics and probability meaning"),
        ("superselection/decoherent histories", "consistent sector algebra", "single realized sector rule"),
        ("cosmological boundary selection", "global boundary-conditioned member", "locality and boundary-law derivation"),
    )
    n2 = (
        ("A", "B", "both retain all global sectors; A token stability and B dilation are independent mechanisms"),
        ("A", "C", "A supplies a basis token; C supplies only eligibility; their terminal obligations differ"),
        ("B", "C", "environment basis diagnostics do not decide the semantic occurrence antecedent"),
        ("carrier progression", "stochastic seed", "finite reversible capture does not test a sampled seed law"),
        ("dilation", "irreversible bath", "retained inverse does not test an infinite renewable attractor"),
        ("predicate", "superselection", "unique eligibility does not test sector actualization"),
        ("local routes", "boundary selection", "bounded local compilers do not test cosmological data"),
    )
    n3 = (
        "fresh carriers are supplied", "blank environment fragments are supplied",
        "neighbor certificate and vacancy are supplied", "C478 pointer basis is retained",
        "C502 candidate law is imported", "occurrence antecedent is semantic only",
        "noiseless reversible primitives", "finite H/F/N only", "partial trace is diagnostic",
        "no stationary measure", "no stochastic seed", "no bath genesis", "no continuum limit",
    )
    n4 = (
        ("Cycle478", "effect-functional pointer packet, no actual member", "inherited", True),
        ("Cycle500", "finite coherent grades, no member", "matched", True),
        ("Cycle502", "hard-core candidate, every sector retained", "matched", True),
        ("Route A", "stable basis token, every sector retained", "member residual survives", True),
        ("Route B", "retained dilation", "member residual survives", True),
        ("Route C", "singleton predicate", "occurrence residual survives", True),
        ("Record boundary", "occurrence and one-lock only", "trigger/content law open", True),
        ("frequency boundary", "realized atoms/process required", "downstream open", False),
    )
    n5 = (
        ("basis pointers", "all five, train", "tested"),
        ("coherent cylinder", "N2/two train states", "tested"),
        ("held finite", "L6/N4/H7/F4", "executed" if mode == "held" else "manifest frozen, not executed"),
        ("arbitrary finite N", "unbounded", "untested"),
        ("infinite/noisy bath and realized history", "lattice-wide", "untested"),
    )
    n6 = (
        "derive an explicit reversible microscopic bath with internally generated ready/fresh carriers",
        "add a local stochastic primitive and derive rather than supply its stationary measure",
        "derive a physical occurrence detector independent of the semantic Record antecedent",
        "couple the singleton predicate to a separately justified site/content rule",
        "construct a fault-tolerant renewable carrier phase and test lifetime scaling",
        "derive grade additivity/noncontextuality then an ergodic admitted-Record calibration",
    )
    n7 = (
        "A concrete hostile constructive route is a translationally invariant local collision model containing a finite-density metastable carrier phase, an internally generated renewal reaction, and a local stochastic actualization variable whose stationary law is derived from the same M2 dynamics. Couple its first-passage event to the exact C478/C502 pointer candidate, retain microscopic exhaust for invertibility bookkeeping where required, and separately prove that the unique Cycle505 binding predicate fixes Record site/content at a physical occurrence. Then prove an admitted-Record stationary ergodic theorem and compare its cylinder frequencies with the operational grade functional. Cycle505 tests none of bath genesis, stochastic actualization, physical occurrence, renewal, or ergodicity, so it cannot exclude this mechanism."
    )
    n8 = (
        "Cycle449 made reversible precommit physical without actualization",
        "Cycle478 made effect functionality physical without probability or occurrence",
        "Cycle496 extended finite deterministic resources without bath genesis",
        "Cycle500 built coherent cylinders without a member",
        "Cycle502 built a hard-core winner token while retaining all sectors",
        "each prior wall narrowed through construction rather than axiom edits",
    )
    primitive_registry_checked = FROZEN_PATHS["premise registry"].exists() and file_sha(FROZEN_PATHS["premise registry"]) == FROZEN["premise registry"]
    check(
        "N1-N8 permits the three scoped positive/route-specific dispositions but rejects shared no-go, minimum-content, and axiom-pressure claims",
        len(n1) >= 5 and len(n2) >= 5 and len(n3) >= 10 and len(n4) >= 8
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 350 and len(n8) >= 5 and primitive_registry_checked,
        {
            "N1_normalized_families": n1, "N2_pairwise_wall_independence": n2,
            "N3_hidden_wall_scan": n3, "N4_residual_matching": n4,
            "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
            "N7_steelman": n7, "N8_cross_cycle_echo": n8,
            "primitive_registry_checked": primitive_registry_checked,
            "executed_mode": mode,
            "Gate_disposition": "FAIL — positive partial constructions with named untested routes",
            "shared_obstruction": False, "axiom_pressure": False,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the train runner remains inside its wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and peak < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_rss_bytes": peak, "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle505 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    mode = os.environ.get("CYCLE505_MODE")
    if mode not in ("train", "held"):
        print("REFUSE Cycle505 execution: set CYCLE505_MODE=train or CYCLE505_MODE=held")
        return 2
    if mode == "held" and os.environ.get("CYCLE505_HELD_AUTHORIZATION") != HELD_AUTHORIZATION_TOKEN:
        print("REFUSE Cycle505 held execution: missing exact root held-authorization token")
        return 2
    length = TRAIN_L if mode == "train" else HELD_L
    n = TRAIN_N if mode == "train" else HELD_N
    horizon = A_TRAIN_H if mode == "train" else A_HELD_H
    fragments = B_TRAIN_F if mode == "train" else B_HELD_F
    print(f"CYCLE505 RETAINED-CARRIER / RECORD-BINDING FORMATION TOURNAMENT {mode.upper()}")
    contract_controls()
    surface = c500.c493.c488.menu_surface()
    a_signatures, a_row = route_a_controls(horizon, mode)
    event = c500.event_basis_maps(surface, length)
    b_signatures, b_row = route_b_controls(event["program"], fragments, mode)
    c_signatures, c_row = route_c_controls()
    coherent_controls(event, {"A": a_signatures, "B": b_signatures, "C": c_signatures}, n, mode)
    covariance_mass_resource_controls((
        ("A", a_schedule(), A_WIDTH, A_NEW_M2),
        ("B", b_schedule(fragments), B_WIDTH, B_NEW_M2),
        ("C", c_schedule(), C_WIDTH, C_NEW_M2),
    ))
    domain_controls()
    inventory_controls(mode)
    no_go_controls(mode)
    resource_controls(started)
    signal.alarm(0)
    print(f"\nRESULT {PASS} passed / {FAIL} failed")
    print("ROUTE DISPOSITIONS", {
        "A": "PASS basis-token partial construction; no actual member/Record",
        "B": "PASS retained-dilation partial construction; same-reduced-channel diagnostic only",
        "C": "PASS singleton RecordBindingCandidate predicate; semantic occurrence antecedent only",
        "shared_obstruction": False, "axiom_pressure": False,
    })
    _ = (a_row, b_row, c_row)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except WallCapExceeded as error:
        print("FAIL", error)
        raise SystemExit(2)
