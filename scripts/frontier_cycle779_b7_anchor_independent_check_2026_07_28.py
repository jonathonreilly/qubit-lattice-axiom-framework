#!/usr/bin/env python3
"""Cycle 779 independent adversarial recount and fast-idiom extension.

The Cycle-779 primary is read only as inert source text and is blocklisted as
an import.  This checker independently recounts the C_51 census, revalidates
all C=7 mapper rows, ports the landed Cycle-761 bit-plane clean-work quotient,
rechecks complete primary strata, and spends the remaining bounded runtime on
additional complete strata in descending feasibility order.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

import numba
import numpy as np


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
PRIMARY_PATH = (
    "scripts/frontier_cycle779_b7_exhaustive_anchor_2026_07_28.py"
)
PRIMARY_MODULE = "frontier_cycle779_b7_exhaustive_anchor_2026_07_28"
BLOCKLIST = (PRIMARY_MODULE,)


class _PrimaryImportBlocker:
    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLIST:
            raise ImportError(f"blocked primary import: {fullname}")
        return None


_PRIMARY_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _PRIMARY_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


BANKS = 7
CAPACITY = 7
STATIONS = 51
EXPECTED_L51 = 45_537_549_124
EXPECTED_FULL_STEPS = 2_322_415_005_324
PRIMARY_K_MAX = 9
PRIMARY_CONFIGURATIONS = 768_807_933
PRIMARY_STEPS = 39_209_204_583
REVERIFY_STRATA = (6, 7)
EXPECTED_COUNTS = (
    1,
    51,
    1_224,
    18_377,
    193_545,
    1_519_749,
    9_231_068,
    44_417_022,
    171_986_841,
    541_440_055,
    1_394_538_288,
    2_947_546_836,
    5_114_119_724,
    7_267_433_292,
    8_417_876_400,
    7_887_861_960,
    5_915_896_470,
    3_500_409_330,
    1_602_881_040,
    553_626_675,
    139_299_615,
    24_322_155,
    2_744_820,
    179_010,
    5_525,
    51,
)
EXPECTED_ROW_KINDS = {
    "bank": 7,
    "cross": 6,
    "finalizer": 1,
    "handoff": 12,
    "relay": 24,
    "source": 1,
}
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "be1d0af8a7dae03b8eff414c1a88ec21fc04c3e92984569a15324b5da2c0fdd3",
    PRIMARY_PATH:
        "2fc8f8f107db4f342d53aab42c35307c26590180c6677762ba9f9d0ee2d850c7",
}
LINEAGE_BLOBS = {
    "cycle756_b5_primary":
        "3f9d019d68ce96dde4c5f1823800a06fc5316518",
    "cycle756_b5_independent":
        "8ef9db87612b0b8b04acff10863e235401f18d1e",
    "cycle761_b6_primary":
        "ce19fef7faf03cb3f336717556409b7b1c24e70e",
    "cycle761_b6_independent":
        "045feb69d405c68bac5aa45293c9d341e60e2755",
}

CHECKS: dict[str, bool] = {}
FINDINGS: dict[str, object] = {}
OUTPUT_LINES: list[str] = []
STDOUT_BYTES = 0
RUN_STARTED = 0.0


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def emit(line: str) -> None:
    global STDOUT_BYTES
    STDOUT_BYTES += len(line.encode()) + 1
    print(line, flush=True)


def check(name: str, condition: object, finding: object) -> bool:
    if name in CHECKS:
        raise AssertionError(("duplicate certificate", name))
    passed = bool(condition)
    CHECKS[name] = passed
    FINDINGS[name] = finding
    line = (
        f"{'PASS' if passed else 'FAIL'} {name} "
        f"FINDINGS={json.dumps(finding, sort_keys=True, separators=(',', ':'), default=str)}"
    )
    OUTPUT_LINES.append(line)
    emit(line)
    if not passed and name in {"CENSUS_RECOUNT", "ROW_RECOUNT"}:
        emit(
            "REFUTES_PRIMARY: "
            f"{name} mismatch "
            f"{json.dumps(finding, sort_keys=True, separators=(',', ':'), default=str)}"
        )
    return passed


def error_text(error: BaseException) -> str:
    return f"{type(error).__name__}: {error}"


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def assigned_literal(tree: ast.Module, name: str) -> object:
    found: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            found.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            found.append(node.value)
    if len(found) != 1:
        raise AssertionError(("literal assignment", name, len(found)))
    return ast.literal_eval(found[0])


def primary_text_certificate() -> dict[str, object]:
    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    extracted = {
        name: assigned_literal(tree, name)
        for name in (
            "AUDIT_INPUT_PATHS",
            "BANKS",
            "CAPACITY",
            "STATIONS",
            "EXPECTED_L51",
            "EXPECTED_FULL_STEPS",
            "EXPECTED_ROW_KINDS",
        )
    }
    observed_sha = {
        path: file_sha256(path)
        for path in (*AUDIT_INPUT_PATHS, PRIMARY_PATH)
    }
    loaded = tuple(name for name in BLOCKLIST if name in sys.modules)
    exact = (
        extracted["AUDIT_INPUT_PATHS"] == AUDIT_INPUT_PATHS
        and extracted["BANKS"] == BANKS
        and extracted["CAPACITY"] == CAPACITY
        and extracted["STATIONS"] == STATIONS
        and extracted["EXPECTED_L51"] == EXPECTED_L51
        and extracted["EXPECTED_FULL_STEPS"] == EXPECTED_FULL_STEPS
        and extracted["EXPECTED_ROW_KINDS"] == EXPECTED_ROW_KINDS
        and observed_sha == EXPECTED_SHA256
        and not loaded
    )
    return {
        "primary_parsed_as_text_only": True,
        "primary_imported": bool(loaded),
        "loaded_blocklist": loaded,
        "module_sha256": observed_sha,
        "extracted": extracted,
        "lineage_blobs_read_for_evaluator_construction": LINEAGE_BLOBS,
        "exact": exact,
    }


def endpoint_cycle_counts(stations: int) -> tuple[int, ...]:
    totals = [0] * (stations // 2 + 1)
    for first in (0, 1):
        states: dict[tuple[int, int], int] = {(first, first): 1}
        for _position in range(1, stations):
            following: dict[tuple[int, int], int] = {}
            for (last, occupied), multiplicity in states.items():
                zero = (0, occupied)
                following[zero] = following.get(zero, 0) + multiplicity
                if not last:
                    one = (1, occupied + 1)
                    following[one] = following.get(one, 0) + multiplicity
            states = following
        for (last, occupied), multiplicity in states.items():
            if not (first and last):
                totals[occupied] += multiplicity
    return tuple(totals)


def polynomial_cycle_counts(stations: int) -> tuple[int, ...]:
    def path(length: int) -> tuple[int, ...]:
        if length == 0:
            return (1,)
        if length == 1:
            return (1, 1)
        older = [1]
        newer = [1, 1]
        for _ in range(2, length + 1):
            current = [0] * max(len(newer), len(older) + 1)
            for degree, value in enumerate(newer):
                current[degree] += value
            for degree, value in enumerate(older):
                current[degree + 1] += value
            older, newer = newer, current
        return tuple(newer)

    absent = path(stations - 1)
    present = path(stations - 3)
    totals = [0] * (stations // 2 + 1)
    for degree, value in enumerate(absent):
        if degree < len(totals):
            totals[degree] += value
    for degree, value in enumerate(present):
        if degree + 1 < len(totals):
            totals[degree + 1] += value
    return tuple(totals)


def closed_cycle_counts(stations: int) -> tuple[int, ...]:
    return (1,) + tuple(
        stations
        * comb(stations - occupied - 1, occupied - 1)
        // occupied
        for occupied in range(1, stations // 2 + 1)
    )


def lucas_number(index: int) -> int:
    older, newer = 2, 1
    if index == 0:
        return older
    for _ in range(2, index + 1):
        older, newer = newer, older + newer
    return newer


def census_recount() -> dict[str, object]:
    endpoint = endpoint_cycle_counts(STATIONS)
    polynomial = polynomial_cycle_counts(STATIONS)
    formula = closed_cycle_counts(STATIONS)
    lucas = lucas_number(STATIONS)
    total = sum(endpoint)
    primary_prefix = sum(endpoint[: PRIMARY_K_MAX + 1])
    exact = (
        endpoint == polynomial == formula == EXPECTED_COUNTS
        and total == lucas == EXPECTED_L51
        and total * STATIONS == EXPECTED_FULL_STEPS
        and primary_prefix == PRIMARY_CONFIGURATIONS
        and primary_prefix * STATIONS == PRIMARY_STEPS
    )
    return {
        "methods": (
            "endpoint-state DP",
            "path-polynomial split",
            "closed cycle formula",
            "scalar Lucas recurrence",
        ),
        "counts_by_k": endpoint,
        "endpoint_total": total,
        "polynomial_total": sum(polynomial),
        "formula_total": sum(formula),
        "lucas_total": lucas,
        "full_station_steps": total * STATIONS,
        "primary_k0_through_k9_configurations": primary_prefix,
        "primary_k0_through_k9_station_steps":
            primary_prefix * STATIONS,
        "counts_sha256": stable_digest(endpoint),
        "exact": exact,
    }


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def own_controlled_signatures(
    word: tuple[object, ...], control: int, work: int
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    output: list[tuple[str, tuple[int, ...]]] = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if gate.kind == "X":
            output.append(("CNOT", (control, wires[0])))
        elif gate.kind == "CNOT":
            output.append(("TOF", (control, wires[0], wires[1])))
        elif gate.kind == "TOF":
            output.extend(
                (
                    ("TOF", (control, wires[0], work)),
                    ("TOF", (work, wires[1], wires[2])),
                    ("TOF", (control, wires[0], work)),
                )
            )
        else:
            raise ValueError(("unsupported semantic gate", gate.kind))
    return tuple(output)


def primitive_truth_failures(kind: str) -> int:
    failures = 0
    if kind == "X":
        for control in (0, 1):
            for target in (0, 1):
                observed = target ^ control
                failures += int(observed != (target ^ control))
    elif kind == "CNOT":
        for control in (0, 1):
            for left in (0, 1):
                for target in (0, 1):
                    observed = target ^ (control & left)
                    failures += int(
                        observed != (target ^ (control & left))
                    )
    elif kind == "TOF":
        for control in (0, 1):
            for left in (0, 1):
                for right in (0, 1):
                    for target in (0, 1):
                        work = 0
                        work ^= control & left
                        observed = target ^ (work & right)
                        work ^= control & left
                        failures += int(
                            observed
                            != (target ^ (control & left & right))
                        )
                        failures += int(work != 0)
    else:
        raise ValueError(kind)
    return failures


def row_recount() -> dict[str, object]:
    """Invoke the C=7 mapper and compare independent per-row gate counts."""

    program = tuple(M740.parameterized_program(BANKS, CAPACITY))
    frozen = tuple(K.interleaved_program(BANKS))
    data_width = int(M740.parameterized_data_width(CAPACITY))
    bank_bases, link_bases = M740.parameterized_bases(CAPACITY)
    arities = {"X": 1, "CNOT": 2, "TOF": 3}
    primitive_failures = {
        kind: primitive_truth_failures(kind) for kind in arities
    }
    primitive_exact = all(
        value == 0 for value in primitive_failures.values()
    )
    kinds: Counter[str] = Counter()
    semantic_kinds: Counter[str] = Counter()
    per_row: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []

    for station, row in enumerate(program):
        kind, index, _local = row
        kinds[str(kind)] += 1
        reasons: list[str] = []
        try:
            word = tuple(
                M740.parameterized_mapped_macro(row, CAPACITY)
            )
            control = data_width + station
            work = data_width + 2 * len(program) + station
            for gate in word:
                semantic_kinds[gate.kind] += 1
                wires = tuple(int(wire) for wire in gate.wires)
                if gate.kind not in arities:
                    reasons.append(f"unsupported_kind:{gate.kind}")
                    continue
                if len(wires) != arities[gate.kind]:
                    reasons.append(f"wrong_arity:{gate.kind}")
                if len(set(wires)) != len(wires):
                    reasons.append(f"repeated_operand:{gate.kind}")
                if any(
                    wire < 0 or wire >= data_width for wire in wires
                ):
                    reasons.append(f"outside_data:{gate.kind}")
            lifted = own_controlled_signatures(word, control, work)
            control_targets = sum(
                bool(wires) and wires[-1] == control
                for _gate_kind, wires in lifted
            )
            work_targets = sum(
                bool(wires) and wires[-1] == work
                for _gate_kind, wires in lifted
            )
            expected_work_targets = 2 * sum(
                gate.kind == "TOF" for gate in word
            )
            if control_targets:
                reasons.append("control_was_target")
            if work_targets != expected_work_targets:
                reasons.append("work_compute_uncompute_count")

            # This is the mapper-side predicate used by the primary.  Only
            # its per-row counts and boolean are compared; the independent
            # checks above do not call through it.
            mapper_clean = M740.validate_clean_word(
                word,
                data_width,
                control,
                work,
                primitive_exact,
            )
            semantic_count = len(word)
            controlled_count = len(lifted)
            counts_agree = (
                int(mapper_clean["semantic_gates"])
                == semantic_count
                and int(mapper_clean["controlled_gates"])
                == controlled_count
            )
            if not counts_agree:
                reasons.append("per_row_count_mismatch")
            if not mapper_clean["pass"]:
                reasons.append("mapper_clean_predicate_failed")
            per_row.append(
                {
                    "station": station,
                    "kind": kind,
                    "index": index,
                    "semantic_gates": semantic_count,
                    "controlled_gates": controlled_count,
                    "work_targets": work_targets,
                    "expected_work_targets": expected_work_targets,
                    "counts_agree": counts_agree,
                    "own_clean": not reasons,
                    "mapper_clean": bool(mapper_clean["pass"]),
                }
            )
        except Exception as error:
            reasons.append(error_text(error))
        if reasons:
            failures.append(
                {
                    "station": station,
                    "kind": kind,
                    "index": index,
                    "reasons": reasons,
                }
            )

    expected_bank_bases = tuple(41 + 131 * i for i in range(CAPACITY))
    expected_link_bases = tuple(
        41 + 131 * CAPACITY + 382 * i
        for i in range(CAPACITY - 1)
    )
    exact = (
        len(program) == STATIONS == 8 * BANKS - 5
        and program == frozen
        and data_width == 3_250
        and bank_bases == expected_bank_bases
        and link_bases == expected_link_bases
        and dict(sorted(kinds.items())) == EXPECTED_ROW_KINDS
        and primitive_exact
        and not failures
        and len(per_row) == STATIONS
        and all(row["counts_agree"] for row in per_row)
    )
    return {
        "banks": BANKS,
        "capacity": CAPACITY,
        "data_width": data_width,
        "rows_checked": len(program),
        "row_kind_counts": dict(sorted(kinds.items())),
        "semantic_gate_kind_counts":
            dict(sorted(semantic_kinds.items())),
        "primitive_truth_failures": primitive_failures,
        "per_row_counts": tuple(
            (
                row["station"],
                row["kind"],
                row["index"],
                row["semantic_gates"],
                row["controlled_gates"],
            )
            for row in per_row
        ),
        "per_row_counts_sha256": stable_digest(tuple(per_row)),
        "per_row_count_agreements": sum(
            bool(row["counts_agree"]) for row in per_row
        ),
        "row_failure_count": len(failures),
        "row_failures": failures,
        "all_51_rows_clean": exact,
        "exact": exact,
    }


# The Cycle-756 pair established arbitrary-width Python-integer bit planes;
# the Cycle-761 independent lineage established this rail-only clean-work
# quotient after every mapper row had been discharged.  The generator below is
# independently JIT-streamed and uses a different (11-bit) dilation table.
BITPLANE_BATCH = 1 << 22
BENCHMARK_BATCHES = 2
DILATION_CHUNK_BITS = 11
DILATION_CHUNK_MASK = (1 << DILATION_CHUNK_BITS) - 1
HEARTBEAT_SECONDS = 30.0
SWEEP_SOFT_DEADLINE_SEC = 1440.0
BUDGET_RATE_NUMERATOR = 5
BUDGET_RATE_DENOMINATOR = 6
BUDGET_FINAL_RESERVE_SEC = 45.0


def _dilate_chunk(value: int) -> int:
    output = 0
    selected_before = 0
    for position in range(DILATION_CHUNK_BITS):
        if (value >> position) & 1:
            output |= 1 << (position + selected_before)
            selected_before += 1
    return output


DILATION_TABLE = np.asarray(
    [
        _dilate_chunk(value)
        for value in range(1 << DILATION_CHUNK_BITS)
    ],
    dtype=np.int64,
)
DILATION_POPCOUNTS = np.asarray(
    [
        value.bit_count()
        for value in range(1 << DILATION_CHUNK_BITS)
    ],
    dtype=np.int64,
)


@numba.njit(cache=False, nogil=True)
def _fill_dilated_combinations(
    output: np.ndarray,
    start: int,
    prefix: int,
    universe: int,
    combination: int,
    limit: int,
    dilation_table: np.ndarray,
    dilation_popcounts: np.ndarray,
) -> tuple[int, int]:
    filled = 0
    while combination < limit and filled < output.size:
        dilated = 0
        earlier_selected = 0
        base = 0
        while base < universe:
            chunk = (
                combination >> base
            ) & DILATION_CHUNK_MASK
            dilated |= int(dilation_table[chunk]) << (
                base + earlier_selected
            )
            earlier_selected += int(dilation_popcounts[chunk])
            base += DILATION_CHUNK_BITS
        output[filled] = np.uint64(prefix | (dilated << start))
        filled += 1
        low = combination & -combination
        raised = combination + low
        combination = raised + (
            ((raised ^ combination) // low) >> 2
        )
    return filled, combination


def cycle_stratum_batches(
    stations: int, occupied: int, batch_size: int
):
    """Stream exactly one independent-set stratum in bounded arrays."""

    cases = [(1, stations - 1, occupied, 0)]
    if occupied:
        cases.append((2, stations - 3, occupied - 1, 1))
    for start, length, selected, prefix in cases:
        if selected < 0 or selected > (length + 1) // 2:
            continue
        if selected == 0:
            yield np.asarray([prefix], dtype="<u8")
            continue
        universe = length - selected + 1
        combination = (1 << selected) - 1
        limit = 1 << universe
        while combination < limit:
            batch = np.empty(batch_size, dtype="<u8")
            filled, combination = _fill_dilated_combinations(
                batch,
                start,
                prefix,
                universe,
                combination,
                limit,
                DILATION_TABLE,
                DILATION_POPCOUNTS,
            )
            if filled <= 0:
                raise AssertionError("dilation stream made no progress")
            yield batch[:filled]


@numba.njit(cache=False, nogil=True)
def _transpose_masks_to_plane_words(
    batch: np.ndarray, stations: int
) -> np.ndarray:
    """Transpose uint64 masks into configuration bit planes, 64 at a time."""

    words = (batch.size + 63) // 64
    packed = np.zeros((stations, words), dtype=np.uint64)
    block = np.empty(64, dtype=np.uint64)
    for word_index in range(words):
        for index in range(64):
            block[index] = np.uint64(0)
        base = word_index * 64
        available = min(64, batch.size - base)
        # The standard in-place transpose reverses both axes.  Reversing the
        # input lane index and selecting output 63-station restores little
        # configuration-bit order without a separate bit reversal.
        for lane in range(available):
            block[63 - lane] = batch[base + lane]
        shift = 32
        mask = np.uint64(0x00000000FFFFFFFF)
        while shift:
            left = 0
            while left < 64:
                temporary = (
                    block[left]
                    ^ (block[left + shift] >> np.uint64(shift))
                ) & mask
                block[left] ^= temporary
                block[left + shift] ^= (
                    temporary << np.uint64(shift)
                )
                left = (left + shift + 1) & ~shift
            shift //= 2
            if shift:
                mask ^= mask << np.uint64(shift)
        for station in range(stations):
            packed[station, word_index] = block[63 - station]
    return packed


def _numpy_reference_planes(
    batch: np.ndarray,
) -> tuple[int, ...]:
    byte_rows = batch.view(np.uint8).reshape(int(batch.size), 8)
    unpacked = np.unpackbits(
        byte_rows, axis=1, bitorder="little"
    )[:, :STATIONS]
    packed = np.packbits(
        unpacked.T, axis=1, bitorder="little"
    )
    return tuple(
        int.from_bytes(packed[station].tobytes(), "little")
        for station in range(STATIONS)
    )


def batch_to_bitplanes(
    batch: np.ndarray, occupied: int
) -> tuple[tuple[int, ...], dict[str, int]]:
    rows = int(batch.size)
    populations = np.bitwise_count(batch)
    population_failures = int(
        np.count_nonzero(populations != occupied)
    )
    ring_mask = np.uint64((1 << STATIONS) - 1)
    rotated = (
        ((batch << np.uint64(1)) & ring_mask)
        | (batch >> np.uint64(STATIONS - 1))
    )
    adjacency_failures = int(np.count_nonzero(batch & rotated))
    outside_mask = np.uint64(((1 << 64) - 1) ^ int(ring_mask))
    range_failures = int(
        np.count_nonzero(batch & outside_mask)
    )

    packed = _transpose_masks_to_plane_words(batch, STATIONS)
    planes = tuple(
        int.from_bytes(
            packed[station].tobytes(order="C"), "little"
        )
        for station in range(STATIONS)
    )
    return planes, {
        "population_failures": population_failures,
        "input_adjacency_failures": adjacency_failures,
        "input_range_failures": range_failures,
    }


ORBIT_FAILURE_KEYS = (
    "translation_failure_config_steps",
    "B_rail_failure_config_steps",
    "work_failure_config_steps",
    "population_failure_config_steps",
    "token_support_failure_config_steps",
    "adjacency_failure_config_steps",
    "ownership_failure_config_steps",
    "distance_transport_failure_config_steps",
    "rail_closure_failures",
)


def bitsliced_population_count(
    planes: list[int] | tuple[int, ...],
) -> tuple[int, ...]:
    digits = [0] * max(1, len(planes).bit_length())
    for plane in planes:
        carry = plane
        digit = 0
        while carry:
            if digit == len(digits):
                digits.append(0)
            overlap = digits[digit] & carry
            digits[digit] ^= carry
            carry = overlap
            digit += 1
    return tuple(digits)


def evaluate_rail_bitplanes(
    original: tuple[int, ...], rows: int, occupied: int
) -> dict[str, int]:
    """Port and hoist the landed rail quotient over all 51 Q boundaries.

    The two literal SWAP layers are first executed on station labels at every
    boundary.  When that schedule is exactly the +1 cyclic permutation with
    blank B rail and exact closure, every tested bit-plane predicate is
    translation invariant.  Its exact configuration-step count is therefore
    one bit-plane count times 51.  A structural mismatch falls back to the
    unhoisted landed evaluator below.
    """

    row_full = (1 << rows) - 1
    a_labels: list[int | None] = list(range(STATIONS))
    b_labels: list[int | None] = [None] * STATIONS
    schedule_exact = True
    for step in range(STATIONS):
        schedule_exact &= all(
            a_labels[station] == (station - step) % STATIONS
            for station in range(STATIONS)
        )
        schedule_exact &= all(label is None for label in b_labels)
        a_labels, b_labels = b_labels, a_labels
        for station in range(STATIONS):
            target = (station + 1) % STATIONS
            b_labels[station], a_labels[target] = (
                a_labels[target],
                b_labels[station],
            )
    schedule_exact &= a_labels == list(range(STATIONS))
    schedule_exact &= all(label is None for label in b_labels)

    if schedule_exact:
        failures = {key: 0 for key in ORBIT_FAILURE_KEYS}
        token_bad = 0
        adjacency_bad = 0
        ownership_bad = 0
        for station in range(STATIONS):
            token_bad |= original[station] & ~row_full
            right = (station + 1) % STATIONS
            left = (station - 1) % STATIONS
            adjacency_bad |= (
                original[station] & original[right]
            )
            ownership_bad |= original[station] & (
                original[left] | original[right]
            )
        population_bad = 0
        actual_count = bitsliced_population_count(original)
        for digit, observed in enumerate(actual_count):
            expected = row_full if (occupied >> digit) & 1 else 0
            population_bad |= observed ^ expected
        failures["token_support_failure_config_steps"] = (
            token_bad.bit_count() * STATIONS
        )
        failures["adjacency_failure_config_steps"] = (
            adjacency_bad.bit_count() * STATIONS
        )
        failures["ownership_failure_config_steps"] = (
            ownership_bad.bit_count() * STATIONS
        )
        failures["population_failure_config_steps"] = (
            population_bad.bit_count() * STATIONS
        )
        return failures

    # Fail-closed general fallback: retain the direct Cycle-761 boundary loop.
    a = list(original)
    b = [0] * STATIONS
    failures = {key: 0 for key in ORBIT_FAILURE_KEYS}
    for step in range(STATIONS):
        translation_bad = 0
        b_bad = 0
        token_support_bad = 0
        adjacency_bad = 0
        ownership_bad = 0
        for station in range(STATIONS):
            expected = original[(station - step) % STATIONS]
            translation_bad |= a[station] ^ expected
            b_bad |= b[station]
            token_support_bad |= (
                (a[station] | b[station]) & ~row_full
            )
            right = (station + 1) % STATIONS
            adjacency_bad |= a[station] & a[right]
            left = (station - 1) % STATIONS
            dirty = (
                a[left]
                | a[right]
                | b[left]
                | b[station]
                | b[right]
            )
            ownership_bad |= a[station] & dirty

        population_bad = 0
        actual_count = bitsliced_population_count(a + b)
        for digit, observed in enumerate(actual_count):
            expected = row_full if (occupied >> digit) & 1 else 0
            population_bad |= observed ^ expected

        failures["translation_failure_config_steps"] += (
            translation_bad.bit_count()
        )
        failures["B_rail_failure_config_steps"] += b_bad.bit_count()
        # Work is quotiented to zero only after all 51 rows independently
        # passed the clean compute/use/uncompute check.
        failures["work_failure_config_steps"] += 0
        failures["population_failure_config_steps"] += (
            population_bad.bit_count()
        )
        failures["token_support_failure_config_steps"] += (
            token_support_bad.bit_count()
        )
        failures["adjacency_failure_config_steps"] += (
            adjacency_bad.bit_count()
        )
        failures["ownership_failure_config_steps"] += (
            ownership_bad.bit_count()
        )
        # Cyclic translation is exhaustively checked as an isometry in the
        # control certificate, so translation_bad is an exact containment.
        failures["distance_transport_failure_config_steps"] += (
            translation_bad.bit_count()
        )

        # Literal action of the two disjoint rail-SWAP layers.
        a, b = b, a
        for station in range(STATIONS):
            target = (station + 1) % STATIONS
            b[station], a[target] = a[target], b[station]

    closure_bad = 0
    for observed, expected in zip(a, original):
        closure_bad |= observed ^ expected
    for plane in b:
        closure_bad |= plane
    failures["rail_closure_failures"] = closure_bad.bit_count()
    return failures


def violation_counts(
    validation: dict[str, int], orbit: dict[str, int]
) -> dict[str, int]:
    return {
        "population_failures": validation["population_failures"],
        "input_adjacency_failures":
            validation["input_adjacency_failures"],
        "input_range_failures": validation["input_range_failures"],
        **{key: orbit[key] for key in ORBIT_FAILURE_KEYS},
    }


EXPECTED_ZERO_VIOLATION_BYTES = (
    b'{"B_rail_failure_config_steps":0,'
    b'"adjacency_failure_config_steps":0,'
    b'"distance_transport_failure_config_steps":0,'
    b'"input_adjacency_failures":0,'
    b'"input_range_failures":0,'
    b'"ownership_failure_config_steps":0,'
    b'"population_failure_config_steps":0,'
    b'"population_failures":0,'
    b'"rail_closure_failures":0,'
    b'"token_support_failure_config_steps":0,'
    b'"translation_failure_config_steps":0,'
    b'"work_failure_config_steps":0}'
)


class BudgetStop(RuntimeError):
    pass


def sweep_one_stratum(
    occupied: int,
    expected_count: int,
    *,
    enforce_deadline: bool,
) -> dict[str, object]:
    started = perf_counter()
    iterator = iter(
        cycle_stratum_batches(
            STATIONS, occupied, BITPLANE_BATCH
        )
    )
    streamed = 0
    station_steps = 0
    batches = 0
    generation_seconds = 0.0
    transpose_seconds = 0.0
    evaluator_seconds = 0.0
    aggregate = {
        key: 0
        for key in (
            "population_failures",
            "input_adjacency_failures",
            "input_range_failures",
            *ORBIT_FAILURE_KEYS,
        )
    }
    evidence = sha256()
    last_heartbeat = started

    while True:
        if (
            enforce_deadline
            and perf_counter() - RUN_STARTED
            >= SWEEP_SOFT_DEADLINE_SEC
        ):
            raise BudgetStop(
                f"k={occupied} stopped after {streamed} configurations"
            )
        marked = perf_counter()
        try:
            batch = next(iterator)
        except StopIteration:
            generation_seconds += perf_counter() - marked
            break
        generation_seconds += perf_counter() - marked

        marked = perf_counter()
        planes, validation = batch_to_bitplanes(batch, occupied)
        transpose_seconds += perf_counter() - marked

        marked = perf_counter()
        orbit = evaluate_rail_bitplanes(
            planes, int(batch.size), occupied
        )
        evaluator_seconds += perf_counter() - marked

        observed = violation_counts(validation, orbit)
        for key, value in observed.items():
            aggregate[key] += value
        evidence.update(
            stable_json_bytes(
                {
                    "batch": batches,
                    "rows": int(batch.size),
                    "first": int(batch[0]),
                    "last": int(batch[-1]),
                    "sum_mod_2_64": int(
                        batch.sum(dtype=np.uint64)
                    ),
                    "violations": observed,
                }
            )
        )
        streamed += int(batch.size)
        station_steps += int(batch.size) * STATIONS
        batches += 1

        now = perf_counter()
        if now - last_heartbeat >= HEARTBEAT_SECONDS:
            emit(
                "SWEEP_HEARTBEAT "
                f"k={occupied} configurations={streamed}/{expected_count} "
                f"elapsed={now - started:.3f}s"
            )
            last_heartbeat = now
        del planes
        del batch

    elapsed = perf_counter() - started
    observed_bytes = stable_json_bytes(aggregate)
    exact = (
        streamed == expected_count
        and station_steps == expected_count * STATIONS
        and observed_bytes == EXPECTED_ZERO_VIOLATION_BYTES
    )
    return {
        "k": occupied,
        "expected_configurations": expected_count,
        "streamed_configurations": streamed,
        "station_steps": station_steps,
        "batches": batches,
        "generation_seconds": round(generation_seconds, 6),
        "transpose_seconds": round(transpose_seconds, 6),
        "evaluator_seconds": round(evaluator_seconds, 6),
        "runtime_seconds": round(elapsed, 6),
        "pipeline_station_steps_per_second": round(
            station_steps / elapsed, 3
        ) if elapsed else 0,
        "violation_counts": aggregate,
        "violation_bytes_hex": observed_bytes.hex(),
        "byte_agreement_with_literal_zero":
            observed_bytes == EXPECTED_ZERO_VIOLATION_BYTES,
        "evidence_sha256": evidence.hexdigest(),
        "complete": streamed == expected_count,
        "exact": exact,
    }


def benchmark_fast_idiom() -> dict[str, object]:
    """Measure the same generator/transpose/evaluator path used by sweeps."""

    warm = next(
        iter(cycle_stratum_batches(STATIONS, 3, 32))
    )
    if int(warm.size) != 32:
        raise AssertionError("JIT generator warm-up failed")
    warm_planes, warm_validation = batch_to_bitplanes(warm, 3)
    reference_agreement = (
        warm_planes == _numpy_reference_planes(warm)
        and all(value == 0 for value in warm_validation.values())
    )
    literal_zero_sane = (
        stable_json_bytes(
            {
                key: 0
                for key in (
                    "population_failures",
                    "input_adjacency_failures",
                    "input_range_failures",
                    *ORBIT_FAILURE_KEYS,
                )
            }
        )
        == EXPECTED_ZERO_VIOLATION_BYTES
    )

    occupied = 10
    iterator = iter(
        cycle_stratum_batches(
            STATIONS, occupied, BITPLANE_BATCH
        )
    )
    rows = 0
    generation_seconds = 0.0
    transpose_seconds = 0.0
    evaluator_seconds = 0.0
    first_fingerprint: dict[str, object] | None = None
    aggregate = {
        key: 0
        for key in (
            "population_failures",
            "input_adjacency_failures",
            "input_range_failures",
            *ORBIT_FAILURE_KEYS,
        )
    }

    for ordinal in range(BENCHMARK_BATCHES):
        marked = perf_counter()
        batch = next(iterator)
        generation_seconds += perf_counter() - marked

        marked = perf_counter()
        planes, validation = batch_to_bitplanes(batch, occupied)
        transpose_seconds += perf_counter() - marked

        marked = perf_counter()
        orbit = evaluate_rail_bitplanes(
            planes, int(batch.size), occupied
        )
        evaluator_seconds += perf_counter() - marked
        observed = violation_counts(validation, orbit)
        for key, value in observed.items():
            aggregate[key] += value
        rows += int(batch.size)
        if ordinal == 0:
            first_fingerprint = {
                "scope": (
                    f"first {int(batch.size)} configurations of k=10"
                ),
                "raw_sha256":
                    sha256(batch.tobytes(order="C")).hexdigest(),
                "violation_bytes_hex":
                    stable_json_bytes(observed).hex(),
            }
        del planes
        del batch

    pipeline_seconds = (
        generation_seconds + transpose_seconds + evaluator_seconds
    )
    measured_steps = rows * STATIONS
    evaluator_rate = measured_steps / evaluator_seconds
    pipeline_rate = measured_steps / pipeline_seconds

    repeat_batch = next(
        iter(
            cycle_stratum_batches(
                STATIONS, occupied, BITPLANE_BATCH
            )
        )
    )
    repeat_planes, repeat_validation = batch_to_bitplanes(
        repeat_batch, occupied
    )
    repeat_orbit = evaluate_rail_bitplanes(
        repeat_planes, int(repeat_batch.size), occupied
    )
    repeated_fingerprint = {
        "scope": (
            f"first {int(repeat_batch.size)} configurations of k=10"
        ),
        "raw_sha256":
            sha256(repeat_batch.tobytes(order="C")).hexdigest(),
        "violation_bytes_hex": stable_json_bytes(
            violation_counts(repeat_validation, repeat_orbit)
        ).hex(),
    }
    deterministic = repeated_fingerprint == first_fingerprint
    zero_violations = (
        stable_json_bytes(aggregate)
        == EXPECTED_ZERO_VIOLATION_BYTES
    )
    exact = (
        literal_zero_sane
        and reference_agreement
        and rows == BENCHMARK_BATCHES * BITPLANE_BATCH
        and rows < EXPECTED_COUNTS[occupied]
        and evaluator_rate > 0
        and pipeline_rate > 0
        and zero_violations
        and deterministic
    )
    return {
        "idiom": (
            "Cycle-756 arbitrary-width bit planes plus Cycle-761 "
            "clean-work rail quotient, ported to C=7/n=51"
        ),
        "benchmark_scope": (
            f"first {rows} configurations of k=10; rate and "
            "determinism only, not coverage"
        ),
        "rows": rows,
        "station_steps": measured_steps,
        "batch_size": BITPLANE_BATCH,
        "batches": BENCHMARK_BATCHES,
        "generation_seconds": round(generation_seconds, 6),
        "transpose_seconds": round(transpose_seconds, 6),
        "evaluator_seconds": round(evaluator_seconds, 6),
        "pipeline_seconds": round(pipeline_seconds, 6),
        "measured_evaluator_station_steps_per_second":
            round(evaluator_rate, 3),
        "measured_pipeline_station_steps_per_second":
            round(pipeline_rate, 3),
        "evaluator_reaches_1_4B_class": evaluator_rate >= 1.4e9,
        "zero_violations": zero_violations,
        "literal_zero_bytes_sane": literal_zero_sane,
        "SWAR_numpy_reference_byte_agreement":
            reference_agreement,
        "first_slice": first_fingerprint,
        "repeated_slice": repeated_fingerprint,
        "slice_byte_identical": deterministic,
        "exact": exact,
    }


def fast_recount_and_extension(
    counts: tuple[int, ...],
    rows: dict[str, object],
) -> dict[str, object]:
    if not rows.get("exact"):
        return {
            "exact": False,
            "error": "row-clean quotient prerequisite failed",
            "full_ring_completed": False,
        }

    benchmark = benchmark_fast_idiom()
    if not benchmark["exact"]:
        return {
            "exact": False,
            "error": "fast-idiom benchmark failed",
            "benchmark": benchmark,
            "full_ring_completed": False,
        }
    emit(
        "FAST_BENCHMARK "
        f"evaluator_rate={benchmark['measured_evaluator_station_steps_per_second']} "
        f"pipeline_rate={benchmark['measured_pipeline_station_steps_per_second']} "
        f"evaluator_1_4B_class={benchmark['evaluator_reaches_1_4B_class']}"
    )

    reverified: dict[int, dict[str, object]] = {}
    for occupied in REVERIFY_STRATA:
        result = sweep_one_stratum(
            occupied,
            counts[occupied],
            enforce_deadline=True,
        )
        reverified[occupied] = result
        emit(
            "REVERIFY_STRATUM "
            f"k={occupied} station_steps={result['station_steps']} "
            f"violations={sum(result['violation_counts'].values())} "
            f"byte_agreement={result['byte_agreement_with_literal_zero']} "
            f"complete={result['complete']} "
            f"seconds={result['runtime_seconds']}"
        )

    extension_order = tuple(
        sorted(
            range(PRIMARY_K_MAX + 1, len(counts)),
            key=lambda occupied: (counts[occupied], -occupied),
        )
    )
    raw_pipeline_rate = float(
        benchmark["measured_pipeline_station_steps_per_second"]
    )
    budget_rate = (
        raw_pipeline_rate
        * BUDGET_RATE_NUMERATOR
        / BUDGET_RATE_DENOMINATOR
    )
    remaining_all_steps = sum(
        counts[occupied] * STATIONS
        for occupied in extension_order
    )
    elapsed_before_extension = perf_counter() - RUN_STARTED
    full_remaining_raw_estimate = (
        remaining_all_steps / raw_pipeline_rate
    )
    full_remaining_fits = (
        elapsed_before_extension
        + full_remaining_raw_estimate
        + BUDGET_FINAL_RESERVE_SEC
        < SWEEP_SOFT_DEADLINE_SEC
    )
    full_upgrade_mode = bool(
        benchmark["evaluator_reaches_1_4B_class"]
        and full_remaining_fits
    )
    emit(
        "EXTENSION_BUDGET "
        f"order={extension_order} budget_rate={budget_rate:.3f} "
        f"full_remaining_raw_estimate={full_remaining_raw_estimate:.3f}s "
        f"full_remaining_fits={full_remaining_fits} "
        f"full_upgrade_mode={full_upgrade_mode}"
    )

    extended: dict[int, dict[str, object]] = {}
    skipped: list[int] = []
    partially_evaluated: list[int] = []
    budget_stop_error = ""
    for ordinal, occupied in enumerate(extension_order):
        predicted_seconds = (
            counts[occupied] * STATIONS / budget_rate
        )
        elapsed_now = perf_counter() - RUN_STARTED
        fits = (
            elapsed_now
            + predicted_seconds
            + BUDGET_FINAL_RESERVE_SEC
            < SWEEP_SOFT_DEADLINE_SEC
        )
        if not full_upgrade_mode and not fits:
            skipped.extend(extension_order[ordinal:])
            break
        try:
            result = sweep_one_stratum(
                occupied,
                counts[occupied],
                enforce_deadline=True,
            )
        except BudgetStop as error:
            partially_evaluated.append(occupied)
            budget_stop_error = error_text(error)
            skipped.extend(extension_order[ordinal + 1 :])
            break
        extended[occupied] = result
        emit(
            "EXTEND_STRATUM "
            f"k={occupied} station_steps={result['station_steps']} "
            f"violations={sum(result['violation_counts'].values())} "
            f"complete={result['complete']} "
            f"seconds={result['runtime_seconds']} "
            f"rate={result['pipeline_station_steps_per_second']}"
        )

    primary_coverage = set(range(PRIMARY_K_MAX + 1))
    extension_coverage = {
        occupied
        for occupied, result in extended.items()
        if result["exact"]
    }
    coverage_union = tuple(
        sorted(primary_coverage | extension_coverage)
    )
    honest_remainder = tuple(
        occupied
        for occupied in range(len(counts))
        if occupied not in coverage_union
    )
    coverage_steps = sum(
        counts[occupied] * STATIONS
        for occupied in coverage_union
    )
    remainder_steps = sum(
        counts[occupied] * STATIONS
        for occupied in honest_remainder
    )
    full_ring_completed = (
        coverage_union == tuple(range(len(counts)))
        and coverage_steps == EXPECTED_FULL_STEPS
        and remainder_steps == 0
    )
    reverify_exact = (
        tuple(sorted(reverified)) == tuple(sorted(REVERIFY_STRATA))
        and all(result["exact"] for result in reverified.values())
        and all(
            bytes.fromhex(result["violation_bytes_hex"])
            == EXPECTED_ZERO_VIOLATION_BYTES
            for result in reverified.values()
        )
    )
    extension_exact = (
        bool(extension_coverage)
        and all(result["exact"] for result in extended.values())
        and not partially_evaluated
    )
    exact = (
        benchmark["exact"]
        and reverify_exact
        and extension_exact
        and coverage_steps + remainder_steps == EXPECTED_FULL_STEPS
        and (
            not full_upgrade_mode
            or full_ring_completed
        )
    )
    emit(
        "FINAL_COVERAGE_UNION "
        f"strata={coverage_union} station_steps={coverage_steps} "
        f"honest_remainder={honest_remainder} "
        f"remainder_steps={remainder_steps} "
        f"full_ring_completed={str(full_ring_completed).lower()}"
    )
    return {
        "benchmark": benchmark,
        "reverified_primary_strata": tuple(sorted(reverified)),
        "reverified_primary": reverified,
        "reverified_violation_byte_agreement": reverify_exact,
        "extension_order_descending_feasibility": extension_order,
        "budget_effective_station_steps_per_second":
            round(budget_rate, 3),
        "full_remaining_raw_estimated_seconds":
            round(full_remaining_raw_estimate, 6),
        "full_remaining_fits_1500s": full_remaining_fits,
        "full_upgrade_mode": full_upgrade_mode,
        "extended_complete_strata":
            tuple(sorted(extension_coverage)),
        "extended": extended,
        "skipped_strata": tuple(skipped),
        "partially_evaluated_strata":
            tuple(partially_evaluated),
        "budget_stop_error": budget_stop_error,
        "primary_declared_coverage": tuple(
            range(PRIMARY_K_MAX + 1)
        ),
        "coverage_union_strata": coverage_union,
        "coverage_union_configurations": sum(
            counts[occupied] for occupied in coverage_union
        ),
        "coverage_union_station_steps": coverage_steps,
        "honest_remainder_strata": honest_remainder,
        "honest_remainder_configurations": sum(
            counts[occupied] for occupied in honest_remainder
        ),
        "honest_remainder_station_steps": remainder_steps,
        "full_ring_completed": full_ring_completed,
        "exact": exact,
    }


def ownership_reasons(
    a_mask: int,
    b_mask: int,
    work_mask: int,
    station: int,
) -> tuple[str, ...]:
    if not ((a_mask >> station) & 1):
        return ()
    left = (station - 1) % STATIONS
    right = (station + 1) % STATIONS
    candidates = (
        ("left_A", (a_mask >> left) & 1),
        ("right_A", (a_mask >> right) & 1),
        ("left_B", (b_mask >> left) & 1),
        ("own_B", (b_mask >> station) & 1),
        ("right_B", (b_mask >> right) & 1),
        ("own_work", (work_mask >> station) & 1),
    )
    return tuple(label for label, present in candidates if present)


def near_miss_recount() -> dict[str, object]:
    rows = []
    rows_passed = 0
    violating_stations = 0
    reason_incidences = 0
    for left in range(STATIONS):
        right = (left + 1) % STATIONS
        a_mask = (1 << left) | (1 << right)
        violations = tuple(
            (
                station,
                ownership_reasons(a_mask, 0, 0, station),
            )
            for station in range(STATIONS)
            if ownership_reasons(a_mask, 0, 0, station)
        )
        sites = tuple(station for station, _reasons in violations)
        reasons = tuple(
            reason
            for _station, station_reasons in violations
            for reason in station_reasons
        )
        exact = (
            sites == tuple(sorted((left, right)))
            and len(violations) == 2
            and len(reasons) == 2
        )
        rows_passed += int(exact)
        violating_stations += len(violations)
        reason_incidences += len(reasons)
        rows.append((left, right, sites, reasons, exact))
    exact = (
        rows_passed == STATIONS
        and violating_stations == 2 * STATIONS
        and reason_incidences == 2 * STATIONS
    )
    return {
        "controls": STATIONS,
        "rows_passed": rows_passed,
        "violating_stations": violating_stations,
        "expected_violating_stations": 2 * STATIONS,
        "reason_incidences": reason_incidences,
        "table_sha256": stable_digest(rows),
        "exact": exact,
    }


def cyclic_distance_isometry_failures(stations: int) -> int:
    failures = 0
    for shift in range(stations):
        for left in range(stations):
            for right in range(left + 1, stations):
                original = min(
                    (right - left) % stations,
                    (left - right) % stations,
                )
                moved_left = (left + shift) % stations
                moved_right = (right + shift) % stations
                moved = min(
                    (moved_right - moved_left) % stations,
                    (moved_left - moved_right) % stations,
                )
                failures += int(original != moved)
    return failures


def run_certificate(function: object, *args: object) -> dict[str, object]:
    try:
        report = function(*args)
        if not isinstance(report, dict):
            raise TypeError("certificate did not return a dict")
        return report
    except Exception as error:
        return {"exact": False, "error": error_text(error)}


def main() -> int:
    global RUN_STARTED
    RUN_STARTED = perf_counter()

    primary_text = run_certificate(primary_text_certificate)
    census = run_certificate(census_recount)
    check(
        "CENSUS_RECOUNT",
        census.get("exact"),
        {
            "L51": census.get("endpoint_total"),
            "full_station_steps":
                census.get("full_station_steps"),
            "primary_k0_k9_station_steps":
                census.get("primary_k0_through_k9_station_steps"),
            "counts_sha256": census.get("counts_sha256"),
            "error": census.get("error"),
        },
    )
    emit(
        "CENSUS_STRATA "
        + ",".join(
            f"k={occupied}:{count}"
            for occupied, count in enumerate(
                census.get("counts_by_k", ())
            )
        )
    )

    rows = run_certificate(row_recount)
    check(
        "ROW_RECOUNT",
        rows.get("exact"),
        {
            "rows_checked": rows.get("rows_checked"),
            "row_kind_counts": rows.get("row_kind_counts"),
            "per_row_count_agreements":
                rows.get("per_row_count_agreements"),
            "per_row_counts_sha256":
                rows.get("per_row_counts_sha256"),
            "row_failure_count": rows.get("row_failure_count"),
            "row_failures": rows.get("row_failures"),
            "error": rows.get("error"),
        },
    )

    if census.get("exact") and rows.get("exact"):
        fast = run_certificate(
            fast_recount_and_extension,
            tuple(census["counts_by_k"]),
            rows,
        )
    else:
        fast = {
            "exact": False,
            "error": "census/row prerequisite failed",
            "full_ring_completed": False,
        }
    benchmark = fast.get("benchmark", {})
    check(
        "FAST_IDIOM_RECOUNT_AND_EXTENSION",
        fast.get("exact"),
        {
            "measured_evaluator_station_steps_per_second":
                benchmark.get(
                    "measured_evaluator_station_steps_per_second"
                ),
            "measured_pipeline_station_steps_per_second":
                benchmark.get(
                    "measured_pipeline_station_steps_per_second"
                ),
            "reverified_primary_strata":
                fast.get("reverified_primary_strata"),
            "reverified_violation_byte_agreement":
                fast.get("reverified_violation_byte_agreement"),
            "extended_complete_strata":
                fast.get("extended_complete_strata"),
            "coverage_union_strata":
                fast.get("coverage_union_strata"),
            "coverage_union_station_steps":
                fast.get("coverage_union_station_steps"),
            "honest_remainder_strata":
                fast.get("honest_remainder_strata"),
            "honest_remainder_station_steps":
                fast.get("honest_remainder_station_steps"),
            "full_ring_completed":
                fast.get("full_ring_completed", False),
            "error": fast.get("error"),
        },
    )

    near_miss = run_certificate(near_miss_recount)
    check(
        "NEAR_MISS_RECOUNT",
        near_miss.get("exact"),
        {
            "controls": near_miss.get("controls"),
            "rows_passed": near_miss.get("rows_passed"),
            "violating_stations":
                near_miss.get("violating_stations"),
            "reason_incidences":
                near_miss.get("reason_incidences"),
            "table_sha256": near_miss.get("table_sha256"),
            "error": near_miss.get("error"),
        },
    )

    elapsed_before_controls = perf_counter() - RUN_STARTED
    distance_failures = cyclic_distance_isometry_failures(STATIONS)
    provisional = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "primary_text": primary_text,
        "census": census,
        "rows": rows,
        "fast": fast,
        "near_miss": near_miss,
        "checks": CHECKS,
    }
    provisional_bytes = len(stable_json_bytes(provisional))
    stdout_bound = (
        STDOUT_BYTES + provisional_bytes + 16 * 1024
        < STDOUT_LIMIT_BYTES
    )
    controls_exact = (
        primary_text.get("exact")
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
        )
        and all(Path(path).is_file() for path in AUDIT_INPUT_PATHS)
        and PRIMARY_MODULE not in sys.modules
        and bool(benchmark.get("slice_byte_identical"))
        and distance_failures == 0
        and elapsed_before_controls < AUDIT_TIMEOUT_SEC
        and stdout_bound
    )
    check(
        "CONTROLS_SHA_BLOCKLIST_DETERMINISM_STDOUT",
        controls_exact,
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "module_sha256": primary_text.get("module_sha256"),
            "primary_text_only": primary_text.get(
                "primary_parsed_as_text_only"
            ),
            "loaded_blocklist":
                primary_text.get("loaded_blocklist"),
            "determinism_declared_slice":
                benchmark.get("benchmark_scope"),
            "slice_byte_identical":
                benchmark.get("slice_byte_identical"),
            "cyclic_distance_isometry_failures":
                distance_failures,
            "runtime_seconds": round(elapsed_before_controls, 6),
            "stdout_bound": stdout_bound,
        },
    )

    elapsed = perf_counter() - RUN_STARTED
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "scope": "Cycle 779 independent b=7/n=51 recount and extension",
        "primary_text_control": primary_text,
        "census_recount": census,
        "row_recount": rows,
        "fast_idiom_recount_and_extension": fast,
        "near_miss_recount": near_miss,
        "controls": FINDINGS.get(
            "CONTROLS_SHA_BLOCKLIST_DETERMINISM_STDOUT"
        ),
        "checks": dict(CHECKS),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "full_ring_completed":
            bool(fast.get("full_ring_completed", False)),
        "runtime_seconds": round(elapsed, 6),
    }
    report["pass"] = all(CHECKS.values()) and elapsed < AUDIT_TIMEOUT_SEC
    report["terminal"] = (
        "CYCLE779_B7_ANCHOR_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE779_B7_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = stable_digest(report)
    final_json = stable_json_bytes(report)
    if STDOUT_BYTES + len(final_json) + 1 >= STDOUT_LIMIT_BYTES:
        fallback = {
            "checks": CHECKS,
            "pass": False,
            "reason": "stdout bound exceeded at final serialization",
            "runtime_seconds": round(elapsed, 6),
            "terminal":
                "CYCLE779_B7_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL",
        }
        emit(stable_json_bytes(fallback).decode())
        return 1
    emit(final_json.decode())
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
