#!/usr/bin/env python3
"""Cycle561: causal endpoint-count to S3 contraction-semigroup bridge.

The constructive route expresses Cycle498 fine/k2/k3 endpoint words in one
declared common four-cell reference word, forms the extensive dimensionless
parameter tau = dK_probe / 4, and feeds the unchanged Cycle469 Route-2
generator/seed/exponential constructor.  Circuit opportunity, schedule depth,
phase, and update ordinal are not decoder inputs or time observables.  A
generator element is not assigned an operational frequency interpretation.

The raw interval ratio, pair-valued sufficient statistic, signed contrast, and
Cycle504 carry-certified endpoint chain are tested as separate routes.  Narrow
route failures are not universal time no-gos or axiom pressure.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
import inspect
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy.linalg import eigh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_relational_interval_s3_slice_seed_bridge_cycle469_2026_07_19 as c469
import physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20 as c498
import physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20 as c504


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ENDPOINT_COUNT_SEMIGROUP_BRIDGE_CYCLE561_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
STANDARD_REFERENCE_CELLS = 4
COUNT_WORD_BITS = 6
MAX_SEGMENTS = 3
BLOCK_MODES = c469.BLOCK_MODES
SLICE_MODES = c469.SLICE_MODES
TOL = 8e-10
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

DEPENDENCY_SHA256 = {
    "physical_relational_interval_s3_slice_seed_bridge_cycle469_2026_07_19.py":
        "ac706716229b81876c2a730a524d0610dee0b41c2fb92dc95a22f6a4260b0fa1",
    "physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20.py":
        "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20.py":
        "fe1e96fbed14befd235b7799deecbf471f4862130d5fb0a1f905d75246bc226e",
}

Word = tuple[int, ...]
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class RouteFixture:
    name: str
    probe_counts: tuple[int, ...]
    held: bool

    @property
    def reference_counts(self) -> tuple[int, ...]:
        return (STANDARD_REFERENCE_CELLS,) * len(self.probe_counts)

    @property
    def tau(self) -> Fraction:
        return Fraction(sum(self.probe_counts), STANDARD_REFERENCE_CELLS)


TRAIN_FIXTURES = (
    RouteFixture("train-delay", (3,), False),
    RouteFixture("train-equal", (4,), False),
    RouteFixture("train-delay-equal", (3, 4), False),
)
HELD_FIXTURES = (
    RouteFixture("held-advance", (5,), True),
    RouteFixture("held-delay-advance", (3, 5), True),
    RouteFixture("held-three-law-chain", (3, 4, 5), True),
    RouteFixture("held-double-advance", (5, 5), True),
)
FIXTURES = TRAIN_FIXTURES + HELD_FIXTURES


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class CodecEvidence:
    base_count: int
    refinement: int
    fine_count: int
    common_word: Word
    coarse_word: Word
    eg_exact: bool
    logical_nn_exact: bool
    inverse_exact: bool
    decoded_fine: int
    decoded_common: int


@dataclass(frozen=True)
class SeedProgram:
    tau: Fraction
    target: np.ndarray
    slice_seed: np.ndarray
    schedule: tuple[object, ...]
    offset: int
    compile_row: dict[str, object]


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


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> None:
    observed = {
        name: file_sha(ROOT / "scripts" / name)
        for name in DEPENDENCY_SHA256
    }
    check(
        "the executable Cycle469, Cycle498, and Cycle504 shores are exact-pinned",
        observed == DEPENDENCY_SHA256,
        {"expected": DEPENDENCY_SHA256, "observed": observed},
    )


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset",
        "physical endpoint-count / contraction-semigroup bridge",
        "tau = dk_probe / 4", "raw ratio", "pair-valued",
        "signed contrast", "carry-certified endpoint chain",
        "cycle-469 prediction seed without refitting",
        "composition under concatenation", "refinement",
        "all 24 proper-cubic frames", "n1 — normalized alternative routes",
        "n8 — cross-cycle echo", "no universal time no-go",
        "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle561 note freezes the additive bridge and claim boundary", not missing, missing)


def one_hot(position: int, width: int) -> Word:
    if position not in range(width):
        raise ValueError("one-hot position leaves its declared word")
    return tuple(int(index == position) for index in range(width))


def hot_position(word: Word) -> int:
    if not isinstance(word, tuple) or not word or any(bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("word leaves its one-hot code")
    return word.index(1)


@lru_cache(maxsize=None)
def codec_evidence(base_count: int, refinement: int) -> CodecEvidence:
    """Execute the Cycle498 physical codec and expose the selected common word."""
    if base_count not in (3, 4, 5) or refinement not in (1, 2, 3):
        raise ValueError("count/refinement leaves the Cycle561 code")
    fine_count = base_count * refinement
    start_endpoint = c498.make_candidate_endpoint(0, 1, None)
    end_endpoint = c498.make_candidate_endpoint(fine_count, 2, start_endpoint)
    start_initial = c498.refinement_initial(start_endpoint, 0)
    end_initial = c498.refinement_initial(end_endpoint, 1)
    start_logical = c498.physical_refinement(start_initial)
    end_logical = c498.physical_refinement(end_initial)
    start_physical = c498.physical_refinement_nn(start_initial)
    end_physical = c498.physical_refinement_nn(end_initial)
    start_coarse = c498.coarse_refinement(start_initial)
    end_coarse = c498.coarse_refinement(end_initial)
    decoded = c498.decode_refinement_interval(start_physical, end_physical)
    if decoded is None:
        raise RuntimeError("Cycle498 codec failed to decode a lawful Cycle561 interval")
    if refinement == 1:
        start_word = start_physical.endpoint_payload[: c498.CLOCK_BITS]
        end_word = end_physical.endpoint_payload[: c498.CLOCK_BITS]
    elif refinement == 2:
        start_word, end_word = start_physical.k2_word, end_physical.k2_word
    else:
        start_word, end_word = start_physical.k3_word, end_physical.k3_word
    start_common = hot_position(start_word)
    end_common = hot_position(end_word)
    common_count = end_common - start_common
    common_word = one_hot(common_count, COUNT_WORD_BITS)
    return CodecEvidence(
        base_count,
        refinement,
        fine_count,
        common_word,
        tuple(end_word[:COUNT_WORD_BITS]),
        start_physical == start_coarse and end_physical == end_coarse,
        start_physical == start_logical and end_physical == end_logical,
        c498.physical_refinement_nn(start_physical, reverse=True) == start_initial
        and c498.physical_refinement_nn(end_physical, reverse=True) == end_initial,
        decoded.fine,
        common_count,
    )


def codec_and_refinement_controls() -> dict[tuple[int, int], CodecEvidence]:
    print("\nCYCLE498 PHYSICAL ENDPOINT CODEC / COMMON-REFERENCE REFINEMENT")
    rows = {(count, q): codec_evidence(count, q) for count in (3, 4, 5) for q in (1, 2, 3)}
    invariance = {
        count: tuple(rows[(count, q)].decoded_common for q in (1, 2, 3))
        for count in (3, 4, 5)
    }
    check(
        "actual Cycle498 fine/k2/k3 endpoint words encode the same common-unit counts 3,4,5 under refinements one,two,three",
        all(row.eg_exact and row.logical_nn_exact and row.inverse_exact for row in rows.values())
        and all(row.decoded_fine == row.base_count * row.refinement for row in rows.values())
        and invariance == {3: (3, 3, 3), 4: (4, 4, 4), 5: (5, 5, 5)},
        {
            "rows": tuple(rows.values()),
            "common_count_invariance": invariance,
            "executed_NN_primitives_per_endpoint": len(c498.refinement_nn_manifest()),
            "standard_reference_word_cells": STANDARD_REFERENCE_CELLS,
        },
    )
    return rows


# Physical bridge bit layout.
_cursor = 0


def take(width: int) -> tuple[int, ...]:
    global _cursor
    sites = tuple(range(_cursor, _cursor + width))
    _cursor += width
    return sites


ACTIVE = take(MAX_SEGMENTS)
REFERENCE_WORDS = tuple(take(COUNT_WORD_BITS) for _ in range(MAX_SEGMENTS))
PROBE_WORDS = tuple(take(COUNT_WORD_BITS) for _ in range(MAX_SEGMENTS))
PROFILE = take(3)
REFERENCE_DEVICE = take(2)
PROBE_DEVICE = take(2)
LINEAGE = take(1)[0]
CODEC_VALID = take(1)[0]
STANDARD_WORD = take(COUNT_WORD_BITS)
FRESH = take(1)[0]
COMMIT = take(1)[0]
RECEIPTS = take(len(FIXTURES))
PREFIX_WORK = take(18)
BRIDGE_BITS = _cursor


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def write(bits: list[int], sites: tuple[int, ...], value: Word) -> None:
    if len(sites) != len(value):
        raise ValueError("bridge field width mismatch")
    for site, bit in zip(sites, value):
        bits[site] = bit


def fixture_index_from_bits(bits: Word) -> int | None:
    for index, fixture in enumerate(FIXTURES):
        if bits == encode_fixture(fixture):
            return index
    return None


def validate_bridge_bits(bits: Word, *, require_initial: bool = False) -> None:
    if not isinstance(bits, tuple) or len(bits) != BRIDGE_BITS or any(bit not in (0, 1) for bit in bits):
        raise ValueError("bridge word leaves its bounded binary M2 code")
    active = selected(bits, ACTIVE)
    count = sum(active)
    if count not in range(1, MAX_SEGMENTS + 1) or active != (1,) * count + (0,) * (MAX_SEGMENTS - count):
        raise ValueError("active segment word is not a prefix")
    for lane in range(MAX_SEGMENTS):
        ref = selected(bits, REFERENCE_WORDS[lane])
        probe = selected(bits, PROBE_WORDS[lane])
        if lane < count:
            if hot_position(ref) != STANDARD_REFERENCE_CELLS or hot_position(probe) not in (3, 4, 5):
                raise ValueError("segment count word leaves the declared common-reference code")
        elif any(ref + probe):
            raise ValueError("inactive segment words must be blank")
    if (
        selected(bits, PROFILE) != one_hot(2, 3)
        or selected(bits, REFERENCE_DEVICE) != (1, 0)
        or selected(bits, PROBE_DEVICE) != (0, 1)
        or bits[LINEAGE] != 1
        or bits[CODEC_VALID] != 1
        or selected(bits, STANDARD_WORD) != one_hot(STANDARD_REFERENCE_CELLS, COUNT_WORD_BITS)
        or any(bits[index] for index in PREFIX_WORK)
        or sum(selected(bits, RECEIPTS)) > 1
    ):
        raise ValueError("profile/device/lineage/codec/calibration sidecar is malformed")
    if require_initial and (bits[FRESH] != 1 or bits[COMMIT] != 0 or any(selected(bits, RECEIPTS))):
        raise ValueError("classifier resources must enter fresh and blank")


def encode_fixture(fixture: RouteFixture) -> Word:
    bits = [0] * BRIDGE_BITS
    for lane, probe_count in enumerate(fixture.probe_counts):
        bits[ACTIVE[lane]] = 1
        write(bits, REFERENCE_WORDS[lane], one_hot(STANDARD_REFERENCE_CELLS, COUNT_WORD_BITS))
        write(bits, PROBE_WORDS[lane], one_hot(probe_count, COUNT_WORD_BITS))
    write(bits, PROFILE, one_hot(2, 3))
    write(bits, REFERENCE_DEVICE, (1, 0))
    write(bits, PROBE_DEVICE, (0, 1))
    bits[LINEAGE] = bits[CODEC_VALID] = bits[FRESH] = 1
    write(bits, STANDARD_WORD, one_hot(STANDARD_REFERENCE_CELLS, COUNT_WORD_BITS))
    word = tuple(bits)
    validate_bridge_bits(word, require_initial=True)
    return word


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "FREDKIN": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle561 gate")
    return Gate(kind, sites, label)


def route_conditions(fixture: RouteFixture) -> tuple[int, ...]:
    conditions = list(ACTIVE)
    for lane, probe_count in enumerate(fixture.probe_counts):
        conditions.extend((REFERENCE_WORDS[lane][STANDARD_REFERENCE_CELLS], PROBE_WORDS[lane][probe_count]))
    conditions.extend((PROFILE[2], REFERENCE_DEVICE[0], PROBE_DEVICE[1], LINEAGE, CODEC_VALID,
                       STANDARD_WORD[STANDARD_REFERENCE_CELLS], FRESH, COMMIT))
    return tuple(conditions)


@lru_cache(maxsize=1)
def classifier_schedule() -> tuple[Gate, ...]:
    output: list[Gate] = []
    for route_index, fixture in enumerate(FIXTURES):
        prefix = fixture.name
        inactive = tuple(ACTIVE[index] for index in range(len(fixture.probe_counts), MAX_SEGMENTS))
        for site in inactive:
            output.append(gate("X", (site,), prefix + ":inactive-open"))
        output.append(gate("X", (COMMIT,), prefix + ":commit-open"))
        conditions = route_conditions(fixture)
        if len(conditions) > len(PREFIX_WORK):
            raise RuntimeError("Cycle561 prefix-work budget is too small")
        output.append(gate("CNOT", (conditions[0], PREFIX_WORK[0]), prefix + ":prefix:0"))
        for lane, condition in enumerate(conditions[1:], start=1):
            output.append(gate("TOFFOLI", (PREFIX_WORK[lane - 1], condition, PREFIX_WORK[lane]), f"{prefix}:prefix:{lane}"))
        output.append(gate("CNOT", (PREFIX_WORK[len(conditions) - 1], RECEIPTS[route_index]), prefix + ":receipt"))
        for lane in reversed(range(1, len(conditions))):
            output.append(gate("TOFFOLI", (PREFIX_WORK[lane - 1], conditions[lane], PREFIX_WORK[lane]), f"{prefix}:clear:{lane}"))
        output.append(gate("CNOT", (conditions[0], PREFIX_WORK[0]), prefix + ":clear:0"))
        output.append(gate("X", (COMMIT,), prefix + ":commit-close"))
        for site in reversed(inactive):
            output.append(gate("X", (site,), prefix + ":inactive-close"))
        output.append(gate("FREDKIN", (RECEIPTS[route_index], COMMIT, FRESH), prefix + ":commit-fresh"))
    return tuple(output)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown Cycle561 gate")


def apply_classifier(bits: Word, *, reverse: bool = False, delete_label: str | None = None) -> Word:
    validate_bridge_bits(bits)
    output = list(bits)
    for item in reversed(classifier_schedule()) if reverse else classifier_schedule():
        if item.label != delete_label:
            apply_gate(output, item)
    result = tuple(output)
    validate_bridge_bits(result)
    return result


def coarse_classifier(bits: Word) -> Word:
    validate_bridge_bits(bits, require_initial=True)
    route_index = fixture_index_from_bits(bits)
    if route_index is None:
        return bits
    output = list(bits)
    output[RECEIPTS[route_index]] = 1
    output[COMMIT], output[FRESH] = output[FRESH], output[COMMIT]
    return tuple(output)


@lru_cache(maxsize=None)
def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(BRIDGE_BITS))
    targets = tuple(range(BRIDGE_BITS - len(item.sites), BRIDGE_BITS))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("restored-line operand order failed")
    return tuple(swaps)


def apply_classifier_nn(bits: Word) -> Word:
    validate_bridge_bits(bits, require_initial=True)
    output = list(bits)
    for item in classifier_schedule():
        if item.kind == "X":
            apply_gate(output, item)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            output[left], output[right] = output[right], output[left]
        width = len(item.sites)
        apply_gate(output, Gate(item.kind, tuple(range(BRIDGE_BITS - width, BRIDGE_BITS)), item.label))
        for left, right in reversed(swaps):
            output[left], output[right] = output[right], output[left]
    result = tuple(output)
    validate_bridge_bits(result)
    return result


def classifier_trace() -> dict[str, object]:
    digest = sha256()
    primitives = 0
    maximum = 0
    failures = 0
    for item in classifier_schedule():
        if item.kind == "X":
            digest.update(f"X:{item.sites[0]}\n".encode())
            primitives += 1
            maximum = max(maximum, 1)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            for direction in ((left, right), (right, left), (left, right)):
                digest.update(f"CNOT:{direction}\n".encode())
                primitives += 1
                maximum = max(maximum, 2)
                failures += int(abs(direction[0] - direction[1]) != 1)
        support = tuple(range(BRIDGE_BITS - len(item.sites), BRIDGE_BITS))
        digest.update(f"{item.kind}:{support}\n".encode())
        primitives += 1
        maximum = max(maximum, len(support))
        failures += int(any(right != left + 1 for left, right in zip(support, support[1:])))
        for left, right in reversed(swaps):
            for direction in ((left, right), (right, left), (left, right)):
                digest.update(f"CNOT:{direction}\n".encode())
                primitives += 1
                maximum = max(maximum, 2)
                failures += int(abs(direction[0] - direction[1]) != 1)
    return {
        "logical_gates": len(classifier_schedule()),
        "nearest_neighbor_primitives": primitives,
        "maximum_support_M2": maximum,
        "connected_support_failures": failures,
        "sha256": digest.hexdigest(),
    }


def restored_route(sites: tuple[int, ...], width: int) -> tuple[tuple[int, int], ...]:
    """Deterministically route named operands to the contiguous right edge."""
    labels = list(range(width))
    targets = tuple(range(width - len(sites), width))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("combined restored-route order failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != sites:
        raise RuntimeError("combined restored-route operand identity failed")
    return tuple(swaps)


def seed_route_compiler_truth(programs: dict[Fraction, SeedProgram]) -> dict[str, object]:
    """Execute every local truth column through the literal restored route."""
    width = BRIDGE_BITS + total_modes(programs)
    truth_rows = 0
    failures = 0
    route_swaps = 0
    digest = sha256()
    for route_index, fixture in enumerate(FIXTURES):
        sites = (
            RECEIPTS[route_index],
            BRIDGE_BITS,
            BRIDGE_BITS + programs[fixture.tau].offset,
        )
        swaps = restored_route(sites, width)
        route_swaps += 2 * len(swaps)
        digest.update(f"{fixture.name}|{sites}|{swaps}\n".encode())
        for column in range(8):
            inputs = tuple((column >> lane) & 1 for lane in range(3))
            line = [0] * width
            for site, bit in zip(sites, inputs):
                line[site] = bit
            for left, right in swaps:
                line[left], line[right] = line[right], line[left]
            control, left, right = range(width - 3, width)
            if line[control]:
                line[left], line[right] = line[right], line[left]
            for left_site, right_site in reversed(swaps):
                line[left_site], line[right_site] = line[right_site], line[left_site]
            expected = list(inputs)
            if expected[0]:
                expected[1], expected[2] = expected[2], expected[1]
            failures += int(tuple(line[site] for site in sites) != tuple(expected))
            failures += int(sum(line) != sum(inputs))
            failures += int(any(line[index] for index in range(width) if index not in sites))
            truth_rows += 1
    return {
        "routes": len(FIXTURES),
        "truth_rows": truth_rows,
        "truth_failures": failures,
        "forward_and_reverse_adjacent_SWAPS": route_swaps,
        "terminal_support_M2": 3,
        "sha256": digest.hexdigest(),
    }


def second_column(first: np.ndarray) -> np.ndarray:
    index = int(np.argmin(np.abs(first)))
    basis = np.zeros_like(first)
    basis[index] = 1
    candidate = basis - first * np.vdot(first, basis)
    return candidate / np.linalg.norm(candidate)


def seed_from_eigensystem(eigenvalues: np.ndarray, eigenvectors: np.ndarray,
                          seed: np.ndarray, amount: Fraction) -> np.ndarray:
    return eigenvectors @ (np.exp(-float(amount) * eigenvalues) * (eigenvectors.T @ seed))


def dilated_target(slice_seed: np.ndarray) -> np.ndarray:
    norm2 = float(np.vdot(slice_seed, slice_seed).real)
    if not 0 < norm2 <= 1 + TOL:
        raise ValueError("candidate seed leaves the contraction-dilation domain")
    target = np.concatenate((slice_seed.astype(complex), np.asarray((math.sqrt(max(0.0, 1 - norm2)),), complex)))
    return target / np.linalg.norm(target)


def build_programs():
    print("\nUNCHANGED CYCLE469 GENERATOR/SEED AND FUNCTIONAL PROGRAMS")
    backbone, original_programs = c469.build_programs()
    eigenvalues, eigenvectors = eigh(backbone.lambda_sym)
    taus = tuple(dict.fromkeys(fixture.tau for fixture in FIXTURES)) + (Fraction(4),)
    programs: dict[Fraction, SeedProgram] = {}
    rows = []
    old_by_tau = {program.ratio: program for program in original_programs.values()}
    for index, tau in enumerate(taus):
        slice_seed = seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, tau)
        target = dilated_target(slice_seed)
        offset = 1 + index * BLOCK_MODES
        isometry = np.column_stack((target, second_column(target)))
        schedule, compile_row = c469.c460.compile_adjacent_isometry(isometry, offset, f"Cycle561:tau={tau}")
        old = old_by_tau.get(tau)
        old_seed_residual = None if old is None else float(np.linalg.norm(slice_seed - old.slice_seed))
        old_target_residual = None if old is None else float(np.linalg.norm(target - old.target))
        programs[tau] = SeedProgram(tau, target, slice_seed, schedule, offset, compile_row)
        rows.append({
            "tau": str(tau), "held_only": tau not in (Fraction(3, 4), Fraction(1)),
            "old_Cycle469_seed_residual": old_seed_residual,
            "old_Cycle469_target_residual": old_target_residual,
            "adjacent_Givens": len(schedule),
        })
    check(
        "the unchanged Cycle469 Lambda_R, u_star, exponential law and contraction sink reproduce all three original seeds before extrapolating to concatenated counts",
        backbone.lambda_sym.shape == (SLICE_MODES, SLICE_MODES)
        and all(row["old_Cycle469_seed_residual"] is None or row["old_Cycle469_seed_residual"] < TOL for row in rows)
        and all(row["old_Cycle469_target_residual"] is None or row["old_Cycle469_target_residual"] < TOL for row in rows)
        and all(
            item.sites[1] == item.sites[0] + 1
            for program in programs.values() for item in program.schedule
        ),
        {"rows": rows, "fit_parameters_added": 0, "generator_or_seed_replaced": False},
    )
    return backbone, eigenvalues, eigenvectors, programs


def total_modes(programs: dict[Fraction, SeedProgram]) -> int:
    return 1 + len(programs) * BLOCK_MODES


def all_seed_schedule(programs: dict[Fraction, SeedProgram]) -> tuple[object, ...]:
    return tuple(gate for program in programs.values() for gate in program.schedule)


def route_seed(classified: Word, state: np.ndarray, programs: dict[Fraction, SeedProgram],
               *, reverse: bool = False, delete_route: int | None = None) -> np.ndarray:
    output = state.copy()
    indices = tuple(range(len(FIXTURES)))
    if reverse:
        indices = tuple(reversed(indices))
    for index in indices:
        if index == delete_route:
            continue
        if classified[RECEIPTS[index]]:
            offset = programs[FIXTURES[index].tau].offset
            output[0], output[offset] = output[offset], output[0]
    return output


def physical_bridge(bits: Word, programs: dict[Fraction, SeedProgram], *,
                    delete_classifier_label: str | None = None, delete_route: int | None = None,
                    delete_last_givens_for: Fraction | None = None) -> tuple[Word, np.ndarray]:
    classified = apply_classifier(bits, delete_label=delete_classifier_label)
    state = np.zeros(total_modes(programs), dtype=complex)
    state[0] = 1
    state = route_seed(classified, state, programs, delete_route=delete_route)
    schedule = all_seed_schedule(programs)
    if delete_last_givens_for is not None:
        victim = programs[delete_last_givens_for].schedule[-1]
        removed = False
        kept = []
        for item in schedule:
            if not removed and item == victim:
                removed = True
                continue
            kept.append(item)
        schedule = tuple(kept)
    return classified, c469.c460.apply_schedule(state, schedule)


def bridge_forward(bits: Word, programs: dict[Fraction, SeedProgram], **kwargs) -> tuple[Word, np.ndarray]:
    return physical_bridge(bits, programs, **kwargs)


def bridge_inverse(classified: Word, output: np.ndarray,
                   programs: dict[Fraction, SeedProgram]) -> tuple[Word, np.ndarray]:
    state = c469.c460.apply_schedule(output, c469.c460.inverse_schedule(all_seed_schedule(programs)))
    state = route_seed(classified, state, programs, reverse=True)
    return apply_classifier(classified, reverse=True), state


def expected_excitation(fixture: RouteFixture, programs: dict[Fraction, SeedProgram]) -> np.ndarray:
    output = np.zeros(total_modes(programs), dtype=complex)
    program = programs[fixture.tau]
    output[program.offset : program.offset + BLOCK_MODES] = program.target
    return output


def bridge_eg_inverse_controls(programs: dict[Fraction, SeedProgram]) -> None:
    print("\nBOUNDED PHYSICAL COUNT-WORD CLASSIFIER / SEED E-G / INVERSE")
    rows = []
    maximum = 0.0
    seed = np.zeros(total_modes(programs), dtype=complex)
    seed[0] = 1
    for fixture in FIXTURES:
        encoded = encode_fixture(fixture)
        logical_classifier = apply_classifier(encoded)
        routed_classifier = apply_classifier_nn(encoded)
        coarse = coarse_classifier(encoded)
        classified, output = bridge_forward(encoded, programs)
        restored_bits, restored_seed = bridge_inverse(classified, output, programs)
        expected = expected_excitation(fixture, programs)
        residual = float(np.linalg.norm(output - expected))
        inverse = float(np.linalg.norm(restored_seed - seed))
        norm = abs(float(np.linalg.norm(output)) - 1)
        maximum = max(maximum, residual, inverse, norm)
        rows.append({
            "fixture": fixture.name, "held": fixture.held,
            "probe_counts": fixture.probe_counts, "tau": str(fixture.tau),
            "classifier_EG": logical_classifier == coarse,
            "routed_classifier_exact": routed_classifier == logical_classifier,
            "seed_EG_residual": residual, "inverse_residual": inverse,
            "norm_drift": norm, "bits_inverse_exact": restored_bits == encoded,
            "work_leakage": sum(restored_bits[index] for index in PREFIX_WORK),
        })
    check(
        "one fixed count-word classifier and all unconditional adjacent-Givens blocks realize E561 Gcoarse = Gphysical E561 on train and held ledgers",
        maximum < TOL and all(
            row["classifier_EG"] and row["routed_classifier_exact"] and row["bits_inverse_exact"]
            and row["work_leakage"] == 0 for row in rows
        ),
        {"rows": rows, "maximum_residual": maximum, "classifier_trace": classifier_trace()},
    )


def raw_ratio(fixture: RouteFixture) -> Fraction:
    return Fraction(sum(fixture.probe_counts), sum(fixture.reference_counts))


def extensive_tau(fixture: RouteFixture) -> Fraction:
    return Fraction(sum(fixture.probe_counts), STANDARD_REFERENCE_CELLS)


def pair_value(fixture: RouteFixture) -> tuple[Fraction, Fraction]:
    return Fraction(sum(fixture.reference_counts)), raw_ratio(fixture)


def compose_pair(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    extent = left[0] + right[0]
    return extent, (left[0] * left[1] + right[0] * right[1]) / extent


def pair_to_tau(value: tuple[Fraction, Fraction]) -> Fraction:
    return value[0] * value[1] / STANDARD_REFERENCE_CELLS


def signed_contrast(fixture: RouteFixture) -> Fraction:
    return Fraction(sum(fixture.probe_counts) - sum(fixture.reference_counts), STANDARD_REFERENCE_CELLS)


def parameter_tournament(backbone, eigenvalues, eigenvectors, programs) -> None:
    print("\nFIVE-ROUTE PARAMETER TOURNAMENT / CONCATENATION / REFINEMENT")
    rows = []
    extensive_residuals = []
    raw_failures = []
    for fixture in FIXTURES:
        direct = seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, extensive_tau(fixture))
        sequential = backbone.seed.copy()
        for count in fixture.probe_counts:
            sequential = seed_from_eigensystem(eigenvalues, eigenvectors, sequential, Fraction(count, STANDARD_REFERENCE_CELLS))
        extensive_residual = float(np.linalg.norm(direct - sequential))
        extensive_residuals.append(extensive_residual)
        raw_sum = sum((Fraction(count, STANDARD_REFERENCE_CELLS) for count in fixture.probe_counts), Fraction())
        ratio = raw_ratio(fixture)
        raw_additive = ratio == raw_sum
        raw_seed = seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, ratio)
        raw_composition_residual = float(np.linalg.norm(raw_seed - sequential))
        if len(fixture.probe_counts) > 1:
            raw_failures.append(not raw_additive and raw_composition_residual > 1e-7)
        value = pair_value(fixture)
        projected = pair_to_tau(value)
        contrast = signed_contrast(fixture)
        rows.append({
            "fixture": fixture.name, "held": fixture.held,
            "raw_ratio": str(ratio), "sum_of_segment_ratios": str(raw_sum),
            "raw_additive": raw_additive,
            "raw_semigroup_composition_residual": raw_composition_residual,
            "extensive_tau": str(extensive_tau(fixture)),
            "extensive_semigroup_residual": extensive_residual,
            "pair": tuple(map(str, value)), "pair_projection_tau": str(projected),
            "signed_contrast": str(contrast),
        })

    a, b, c = (pair_value(FIXTURES[index]) for index in (0, 1, 3))
    pair_associative = compose_pair(compose_pair(a, b), c) == compose_pair(a, compose_pair(b, c))
    pair_homomorphic = pair_to_tau(compose_pair(a, b)) == pair_to_tau(a) + pair_to_tau(b)
    # Since Lambda_R is symmetric, this is the full-operator residual in its
    # common eigenbasis, not merely a seed-orbit comparison.
    operator_residuals = []
    for left, right in ((Fraction(3, 4), Fraction(1)), (Fraction(3, 4), Fraction(5, 4)),
                        (Fraction(7, 4), Fraction(5, 4))):
        lhs = np.exp(-float(right) * eigenvalues) * np.exp(-float(left) * eigenvalues)
        rhs = np.exp(-float(left + right) * eigenvalues)
        operator_residuals.append(float(np.max(np.abs(lhs - rhs))))
    held_order_a = (3, 4, 5)
    held_order_b = (5, 3, 4)
    held_order_tau = (
        Fraction(sum(held_order_a), STANDARD_REFERENCE_CELLS),
        Fraction(sum(held_order_b), STANDARD_REFERENCE_CELLS),
    )
    held_order_outputs = tuple(
        seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, value)
        for value in held_order_tau
    )
    held_resegmentation_residual = float(np.linalg.norm(held_order_outputs[0] - held_order_outputs[1]))
    refinement_rows = []
    for fixture in FIXTURES:
        for q in (1, 2, 3):
            fine_probe = sum(count * q for count in fixture.probe_counts)
            fine_reference = sum(STANDARD_REFERENCE_CELLS * q for _ in fixture.probe_counts)
            refinement_rows.append({
                "fixture": fixture.name, "q": q,
                "raw_ratio": Fraction(fine_probe, fine_reference),
                "tau_after_common_word_decode": Fraction(fine_probe, STANDARD_REFERENCE_CELLS * q),
            })
    refinement_exact = all(
        row["raw_ratio"] == raw_ratio(next(item for item in FIXTURES if item.name == row["fixture"]))
        and row["tau_after_common_word_decode"] == extensive_tau(next(item for item in FIXTURES if item.name == row["fixture"]))
        for row in refinement_rows
    )

    negative = signed_contrast(FIXTURES[0])
    expanded = seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, negative)
    expanded_norm = float(np.linalg.norm(expanded))
    check(
        "the extensive common-unit count and pair projection compose, while raw ratio failure and negative signed contrast remain route-specific",
        max(extensive_residuals) < TOL and max(operator_residuals) < 2e-15
        and raw_failures and all(raw_failures)
        and pair_associative and pair_homomorphic and refinement_exact
        and held_order_tau == (Fraction(3), Fraction(3))
        and held_resegmentation_residual < TOL
        and negative == Fraction(-1, 4) and expanded_norm > 1 + 1e-6,
        {
            "rows": rows,
            "pair_associative": pair_associative,
            "pair_to_tau_homomorphism": pair_homomorphic,
            "full_operator_spectral_semigroup_residuals": operator_residuals,
            "held_nonidentical_profile_orders": (held_order_a, held_order_b),
            "held_resegmentation_order_residual": held_resegmentation_residual,
            "refinement_rows": refinement_rows,
            "signed_delay_contrast": str(negative),
            "signed_delay_seed_norm": expanded_norm,
            "signed_route_contraction_dilation_defined": False,
            "raw_ratio_disposition": "single-cell compatible; concatenation nonadditive",
            "signed_contrast_disposition": "additive but not a nonnegative contraction parameter on delay",
        },
    )


def carry_chain_route(backbone, eigenvalues, eigenvectors, programs) -> None:
    print("\nDISTINCT CYCLE504 CARRY-CERTIFIED ENDPOINT-CHAIN ROUTE")
    initial, first_endpoint = c504.prepare(1, c504.TRAIN_N, 1)
    installed = c504.apparatus(1, c504.TRAIN_N)
    terminal, _history = c504.run_repeated(initial, installed, c504.TRAIN_N)
    decoded = c504.decode_history(c504.history_view(terminal, first_endpoint))
    restored = c504.reverse_history(terminal, installed, c504.TRAIN_N * 2)
    if decoded is None:
        raise RuntimeError("Cycle504 train endpoint chain failed to decode")
    tau = Fraction(decoded.total_cells, STANDARD_REFERENCE_CELLS)
    direct = seed_from_eigensystem(eigenvalues, eigenvectors, backbone.seed, tau)
    sequential = backbone.seed.copy()
    for cells in decoded.interval_cells:
        sequential = seed_from_eigensystem(eigenvalues, eigenvectors, sequential, Fraction(cells, STANDARD_REFERENCE_CELLS))
    check(
        "the distinct Cycle504 carry-certified endpoint chain supplies an additive local clock route into the same unchanged seed family",
        decoded.interval_cells == (2,) * c504.TRAIN_N
        and decoded.total_cells == 16 and decoded.physical_carries == 1
        and decoded.carry_classifier and tau == Fraction(4)
        and float(np.linalg.norm(direct - sequential)) < TOL
        and float(np.linalg.norm(direct - programs[Fraction(4)].slice_seed)) < TOL
        and restored == initial
        and all(value == 0 for value in c504.decoder_ast_audit().values()),
        {
            "decoded": decoded, "tau": str(tau),
            "semigroup_residual": float(np.linalg.norm(direct - sequential)),
            "inverse_exact": restored == initial,
            "decoder_forbidden_name_hits": c504.decoder_ast_audit(),
            "supplied_opportunity_interval_used_by_decoder": False,
            "held_status": "Cycle504 held evidence is inherited, not re-executed in Cycle561",
        },
    )


def deletion_domain_controls(programs, codec_rows) -> None:
    print("\nDELETION / LEAKAGE / LAWFUL DOMAIN")
    fixture = next(item for item in FIXTURES if item.name == "held-three-law-chain")
    encoded = encode_fixture(fixture)
    baseline_bits, baseline = bridge_forward(encoded, programs)
    route_index = FIXTURES.index(fixture)
    classifier_deleted_bits, classifier_deleted = bridge_forward(
        encoded, programs, delete_classifier_label=fixture.name + ":receipt"
    )
    _route_bits, route_deleted = bridge_forward(encoded, programs, delete_route=route_index)
    _gate_bits, gate_deleted = bridge_forward(encoded, programs, delete_last_givens_for=fixture.tau)

    sidecar_refusals = {}
    for name, site in (
        ("lineage", LINEAGE), ("codec", CODEC_VALID), ("profile", PROFILE[2]),
        ("reference_device", REFERENCE_DEVICE[0]), ("probe_device", PROBE_DEVICE[1]),
        ("standard_reference_word", STANDARD_WORD[STANDARD_REFERENCE_CELLS]),
    ):
        damaged = list(encoded)
        damaged[site] = 0
        try:
            validate_bridge_bits(tuple(damaged))
            sidecar_refusals[name] = False
        except ValueError:
            sidecar_refusals[name] = True

    count = 5
    q = 3
    start_endpoint = c498.make_candidate_endpoint(0, 1, None)
    end_endpoint = c498.make_candidate_endpoint(count * q, 2, start_endpoint)
    start_initial = c498.refinement_initial(start_endpoint, 0)
    end_initial = c498.refinement_initial(end_endpoint, 1)
    damaged_end = c498.physical_refinement_nn(end_initial, delete_logical_label=f"fine-to-k3:{count*q}")
    codec_deleted = c498.decode_refinement_interval(
        c498.physical_refinement_nn(start_initial), damaged_end
    ) is None

    malformed = 0
    actions = (
        lambda: codec_evidence(2, 1),
        lambda: codec_evidence(5, 4),
        lambda: encode_fixture(RouteFixture("too-long", (3, 4, 5, 3), True)),
        lambda: hot_position((1, 1, 0, 0, 0, 0)),
    )
    for action in actions:
        try:
            action()
        except (ValueError, IndexError):
            malformed += 1
    check(
        "endpoint codec, lineage/profile/device/calibration, classifier, route, and one-Givens deletions are visible and malformed domains refuse",
        all(sidecar_refusals.values()) and codec_deleted
        and baseline_bits[COMMIT] == 1 and classifier_deleted_bits[COMMIT] == 0
        and float(np.linalg.norm(classifier_deleted - baseline)) > 1e-6
        and float(np.linalg.norm(route_deleted - baseline)) > 1e-6
        and float(np.linalg.norm(gate_deleted - baseline)) > 1e-6
        and malformed == len(actions)
        and all(row.eg_exact and row.inverse_exact for row in codec_rows.values()),
        {
            "sidecar_refusals": sidecar_refusals,
            "deleted_q3_codec_refused": codec_deleted,
            "classifier_deletion_residual": float(np.linalg.norm(classifier_deleted - baseline)),
            "route_deletion_residual": float(np.linalg.norm(route_deleted - baseline)),
            "one_Givens_deletion_residual": float(np.linalg.norm(gate_deleted - baseline)),
            "malformed_refusals": malformed,
        },
    )


def proper_frames() -> tuple[np.ndarray, ...]:
    return c498.c444.FRAMES


def covariance_locality_controls(programs) -> None:
    print("\nALL24 PROPER-CUBIC COVARIANCE / LOCALITY / M2 STATUS")
    trace = classifier_trace()
    schedule = all_seed_schedule(programs)
    non_adjacent_givens = sum(item.sites[1] != item.sites[0] + 1 for item in schedule)
    frames = proper_frames()
    line_length = BRIDGE_BITS + total_modes(programs)
    base_line = tuple((index, 0, 0) for index in range(line_length))
    failures = 0
    for frame in frames:
        moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in base_line)
        failures += sum(
            sum(abs(a - b) for a, b in zip(left, right)) != 1
            for left, right in zip(moved[:-1], moved[1:])
        )
        failures += int(round(np.linalg.det(frame)) != 1)
    route_trace = seed_route_compiler_truth(programs)
    check(
        "the Cycle498 codec, bounded count classifier, restored seed routes and adjacent-Givens blocks are finite-M2 and carried through all24 frames",
        len(frames) == 24 and failures == 0
        and trace["maximum_support_M2"] <= 3 and trace["connected_support_failures"] == 0
        and non_adjacent_givens == 0 and route_trace["truth_failures"] == 0,
        {
            "proper_cubic_frames": len(frames), "frame_failures": failures,
            "bridge_word_M2": BRIDGE_BITS,
            "seed_modes_including_sinks": total_modes(programs),
            "joined_bridge_M2": line_length,
            "Cycle498_codec_M2_per_endpoint": c498.refinement_trace()["logical_M2"],
            "Cycle498_NN_primitives_per_endpoint": len(c498.refinement_nn_manifest()),
            "maximum_classifier_or_route_terminal_support_M2": 3,
            "adjacent_Givens": len(schedule), "nonadjacent_Givens": non_adjacent_givens,
            "executed_seed_route_compiler": route_trace,
            "classifier_trace": trace,
            "size_uniform_arbitrary_history_QCA_claimed": False,
        },
    )


def ast_firewall_controls() -> None:
    print("\nDECODER / INTERPRETATION FIREWALL")
    functions = (raw_ratio, extensive_tau, pair_value, signed_contrast)
    forbidden = ("update", "layer", "depth", "schedule", "phase", "iteration", "rate")
    hits = {}
    for function in functions:
        tree = ast.parse(inspect.getsource(function))
        names = tuple(
            node.id.lower() if isinstance(node, ast.Name) else node.attr.lower()
            for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute))
        )
        hits[function.__name__] = {token: sum(token in name for name in names) for token in forbidden}
    check(
        "candidate parameter decoders consume endpoint counts only and do not rename a schedule, phase, or generator entry as time or frequency",
        all(value == 0 for row in hits.values() for value in row.values()),
        {"AST_forbidden_name_hits": hits, "generator_entry_assigned_operational_frequency": False,
         "candidate_parameter_called_proper_time": False},
    )


def no_go_inventory_controls(started: float, programs) -> None:
    print("\nSUPPLIED/DERIVED/OPEN / FULL N1-N8 CLAIM GATE")
    n1 = (
        ("raw relational ratio", "endpoint pair / quotient / scalar semigroup parameter", "ATTEMPTED — single-cell positive, concatenation negative"),
        ("extensive common-unit count", "refined probe endpoint word / additive count divided by fixed four-cell standard / semigroup homomorphism", "ATTEMPTED — POSITIVE"),
        ("pair-valued sufficient statistic", "(reference extent,ratio) / weighted composition then projection / retain relative and extensive data", "ATTEMPTED — POSITIVE WITH EXPLICIT PROJECTION"),
        ("signed contrast", "probe-minus-reference endpoints / additive difference / contraction parameter", "ATTEMPTED — delay sector leaves nonnegative contraction domain"),
        ("carry-certified endpoint chain", "Cycle504 endpoint/carry lineage / sum decoded local intervals / renewed finite clock bridge", "ATTEMPTED — POSITIVE ON N8 TRAIN"),
    )
    walls = (
        "standard-clock/profile calibration", "endpoint formation/actuality",
        "bounded-local renewal/scaling", "generator-seed-law selection",
        "continuum/proper-time interpretation",
    )
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "four-cell Cycle451 reference word", "common profile and equal cell scale",
        "Cycle498 fine/k2/k3 codec and refinement tag", "event identities and predecessor lineage",
        "distinct reference/probe device words", "candidate endpoint formation",
        "finite three-segment bridge domain", "noiseless fresh/work/receipt words",
        "Route2 Lambda_R and u_star", "exponential law and contraction sink",
        "compile-time eigensystem/Givens synthesis", "Cycle504 G, delta, and blank finite bank",
    )
    n4 = (
        ("Cycle451 note lines 161-187", "common-profile relational ratio and scale cancellation", "four-cell standard is imported rather than hidden", True),
        ("Cycle469 note lines 105-136", "ratio-to-seed law and seed semigroup identities", "same Lambda/seed/exponential; parameter composition newly tested", True),
        ("Cycle498 note lines 184-226", "endpoint-only count and physical refinement additivity", "actual fine/k2/k3 physical words consumed", True),
        ("Cycle479 note lines 56-71", "local-3D provenance but ratio-as-parameter supplied", "generator retained unchanged; calibration residual attacked", True),
        ("Cycle504 note lines 27-61", "finite physical carry/epoch endpoint chain with supplied G/delta", "distinct N8 endpoint-chain route only", True),
    )
    n5 = (
        ("single 3:4,4:4,5:4 cells", "tested train/held", "exact Cycle469 recovery"),
        ("two/three-cell concatenations", "tested train/held", "extensive/pair positive; raw ratio negative"),
        ("q=1,2,3 endpoint refinements", "tested", "common-unit invariance"),
        ("N8 Cycle504 carry chain", "tested train only", "finite distinct route"),
        ("arbitrary length/noisy/continuum clocks", "untested", "no negative claim"),
    )
    n6 = (
        "derive the four-cell standard from a jointly prepared reference apparatus",
        "transport the common-profile certificate through Cycle504 rollover",
        "extend the finite count classifier to a size-uniform local unary accumulator",
        "calibrate another physical clock against the same endpoint chain",
        "compile the full arbitrary-input contraction operator",
        "prove an operational refinement/continuum limit before proper-time language",
    )
    n7 = (
        "The strongest constructive challenge is to replace the supplied four-cell standard and finite class menu with one jointly prepared dual-clock automorphism. It should emit matched reference/probe endpoint words, carry their common profile through rollover, accumulate an arbitrary finite prefix in a translation-covariant local register, and drive a full contraction dilation. The current extensive homomorphism shows exactly where that construction can attach; the raw-ratio failure does not exclude it."
    )
    n8 = (
        "Cycle451 made co-registered ratios physical but did not test composition",
        "Cycle456 made three ratio classes local but retained a finite menu",
        "Cycle469 connected that menu to one seed orbit but supplied t=ratio",
        "Cycle498 supplied physical endpoint refinement and additivity",
        "Cycles479/504 supplied local generator provenance and finite rollover routes without selecting physical time",
    )
    supplied = (
        "Cycle451 four-cell reference word, common profile, oscillator orientation and equal cell scale",
        "Cycle498 endpoint formation, fine/k2/k3 codec, event/predecessor grammar and finite words",
        "reference/probe device identities, finite route menu, blank work/receipt/excitation resources",
        "Cycle469/479 Lambda_R, u_star, exponential candidate law, sink, E-shell scope and compile-time Givens synthesis",
        "Cycle504 finite G, opportunity interval delta, blank carry/endpoint banks and N8 apparatus",
    )
    derived = (
        "exact physical refinement to common counts 3,4,5 at q=1,2,3",
        "tau=dK_probe/4 semigroup homomorphism on frozen train/held concatenations",
        "exact recovery of original Cycle469 seeds without refit",
        "associative pair composition and projection to tau",
        "raw-ratio nonadditivity, signed-delay contraction failure, and positive N8 carry-chain route",
        "bounded classifier E/G/inverse, NN trace, deletions, lawful domain and all24 carriage",
    )
    open_items = (
        "physical genesis/selection of the standard reference word and common-profile certificate",
        "candidate endpoint FORM admission, framework Record actuality and realized history",
        "size-uniform bounded-radius accumulation, renewal, noise protection and arbitrary duration",
        "selection/derivation of the exponential law, seed, full operator and empirical calibration",
        "universal clock equivalence, continuum/Lorentz/proper-time theorem, lapse and physical c",
        "energy/stress/source/gravity and Born probability",
    )
    elapsed = time.monotonic() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw_rss if sys.platform == "darwin" else raw_rss * 1024)
    check(
        "full N1-N8 retains route-specific failures, exact imports and live constructive paths; no shared obstruction or axiom pressure is promoted",
        len(n1) == 5 and len(n2) == 10 and len(n3) >= 10 and len(n4) == 5
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 300 and len(n8) == 5
        and len(supplied) == 5 and len(derived) == len(open_items) == 6
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {
            "N1_normalized_routes": n1, "N2_pairwise_walls": n2,
            "N3_hidden_condition_scan": n3, "N4_residual_matching": n4,
            "N5_resolution_rhetoric": n5, "N6_partial_closure_paths": n6,
            "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
            "supplied": supplied, "derived": derived, "open": open_items,
            "broad_no_go": "FAIL / DO NOT SHIP", "shared_obstruction": False,
            "axiom_pressure": False, "authority": AUTHORITY, "audit": AUDIT,
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "peak_rss_bytes": rss, "rss_cap_bytes": RSS_CAP_BYTES,
            "six_wall_ledger": {
                "C_ref": "narrowed by an additive operational bridge; standard/profile/formation still supplied",
                "C_num": "exact rational train/held/refinement residuals; no empirical duration scale",
                "C_wrap": "materially narrowed by compositional count-to-seed map; arbitrary renewal/proper time open",
                "C_int": "unchanged; no phase is energy and no generator entry receives frequency meaning",
                "C_local": "bounded classifier/codec/Givens positive; size-uniform accumulator and full operator open",
                "C_source": "unchanged; E-shell scope only, no stress/source/gravity law",
            },
        },
    )


def install_wall_cap() -> None:
    if hasattr(signal, "SIGALRM"):
        def alarm(_signum, _frame):
            raise TimeoutError("Cycle561 exceeded its wall cap")
        signal.signal(signal.SIGALRM, alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    install_wall_cap()
    print("Cycle561 physical endpoint-count / contraction-semigroup bridge")
    print("authority", AUTHORITY, "audit", AUDIT)
    try:
        dependency_controls()
        note_contract()
        codec_rows = codec_and_refinement_controls()
        backbone, eigenvalues, eigenvectors, programs = build_programs()
        bridge_eg_inverse_controls(programs)
        parameter_tournament(backbone, eigenvalues, eigenvectors, programs)
        carry_chain_route(backbone, eigenvalues, eigenvectors, programs)
        deletion_domain_controls(programs, codec_rows)
        covariance_locality_controls(programs)
        ast_firewall_controls()
        no_go_inventory_controls(started, programs)
    except Exception as exc:
        check("Cycle561 runner completed without exception", False, repr(exc))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
