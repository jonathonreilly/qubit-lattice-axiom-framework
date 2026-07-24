#!/usr/bin/env python3
"""Finite retained-counter and co-registration identities.

This self-contained runner checks a supplied finite counter model.  It does
not import another repository runner.  The model consists of supplied tick
streams, a K=16 rotor with persistent carry counts, predecessor-linked cells,
four supplied co-registration labels, and a supplied one-refill reset
procedure.  Within that declared model the runner checks exact integer
telescoping, orientation reversal, missing-label undefinedness, and invariance
under one reset that preserves the carry count.  It also executes one supplied
cross-order predicate on ordinary and adversarial finite inputs.

One separate diagnostic converts exact count ratios to binary floating point
and compares their finite-segment spread with a disclosed two-count tolerance.
That diagnostic is not an exact identity and does not infer a continuum rate.

The shared generator coordinate orders the supplied ticks; it is not decoded.
The displayed decoders do use cell indices and predecessor links to verify
lineage and orientation.  "Retained" means only that carry_count is unchanged
through the one supplied refill.  Nothing here constructs physical time, a
clock, a framework Record, a physical M_2(C) site compiler, or a resource,
noise, leakage, or scaling result.  Authority: none.  Audit: unset.
"""

from __future__ import annotations

import copy
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = (
    ROOT
    / "outputs"
    / "finite_retained_counter_coregistration_identities_receipt_2026_07_24.json"
)

EXECUTION_IMPORTS = [
    "__future__.annotations",
    "copy",
    "dataclasses.dataclass",
    "fractions.Fraction",
    "hashlib.sha256",
    "itertools.combinations",
    "json",
    "math",
    "pathlib.Path",
    "sys",
    "typing.Iterable",
    "typing.Sequence",
]

SUPPLIED_FIXTURE: dict[str, object] = {
    "generator_span": [0, 4096],
    "piecewise_split": 2048,
    "co_registration_coordinates": {
        "S1": 512,
        "S2": 1500,
        "S3": 2600,
        "S4": 3800,
    },
    "signed_tick_slopes": {
        "A": "-296/625",
        "B": "-5/16",
        "C": "-287/1250",
        "D_first": "-296/625",
        "D_second": "-5/16",
    },
    "counter_modulus": 16,
    "position_decoder": (
        "P(label) = counter_modulus * carry_count(label) + rotor(label); "
        "a missing label returns None"
    ),
    "interval_decoder": (
        "Delta(label_a,label_b) = P(label_b) - P(label_a) only when both labels "
        "exist and predecessor traversal connects the later-index cell to the "
        "earlier-index cell; otherwise return None"
    ),
    "large_bank_capacity": 1_000_000_000,
    "large_bank_reset_allowance": 0,
    "reset_test_bank_capacity": 700,
    "reset_test_allowance": 1,
    "crossing_convention": (
        "positive integer crossings of accumulated absolute slope; segment "
        "upper endpoints excluded"
    ),
    "tie_convention": (
        "tick before label in forward order; label before tick in reverse order"
    ),
    "label_convention": (
        "a co-registration label snapshots counter state without consuming a bank slot"
    ),
    "reset_convention": (
        "on exhaustion, restore the supplied bank capacity and reset bank_slot; "
        "retain rotor and carry_count"
    ),
    "cell_topology": (
        "each cell index is its zero-based list position; each noninitial cell's "
        "predecessor is the preceding cell index and the initial predecessor is None"
    ),
    "lineage_convention": (
        "cell.index orients the requested endpoints and predecessor links must connect them"
    ),
    "missing_label_convention": "a missing label decodes to None, not zero",
    "floating_diagnostic_tolerance": (
        "2 / min(abs(nonzero decoded segment count)); infinity if there is no "
        "nonzero decoded segment count"
    ),
    "cross_order_devices": ["A", "B", "C"],
    "cross_order_initial_state": (
        "every device position is 0 and the shared-snapshot list is empty"
    ),
    "cross_order_local_operation": (
        "append_local(device) increments only that device position by 1"
    ),
    "cross_order_predicate": (
        "for current snapshot s, accept iff for every prior shared snapshot p and "
        "every device d, p[d] < s[d]"
    ),
    "cross_order_accept_mutation": (
        "on acceptance increment every device position by 1, append the "
        "pre-increment current snapshot, and return accepted"
    ),
    "cross_order_refusal_mutation": (
        "on refusal return refused_inverted without changing device positions or "
        "the shared-snapshot list"
    ),
    "ordinary_cross_order_fixture": (
        "increment every device twice, then call the supplied predicate four times"
    ),
    "adversarial_cross_order_fixture": (
        "increment every device four times; accept once; append the supplied prior "
        "snapshot A=1,B=9,C=1 without applying the predicate; call the predicate once"
    ),
}

FIXTURE_SHA256 = sha256(
    json.dumps(SUPPLIED_FIXTURE, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

GENERATOR_END = Fraction(4096)
PIECEWISE_SPLIT = Fraction(2048)
COREGISTRATION_COORDINATES = {
    "S1": Fraction(512),
    "S2": Fraction(1500),
    "S3": Fraction(2600),
    "S4": Fraction(3800),
}
SLOPES = {
    "A": Fraction(-296, 625),
    "B": Fraction(-5, 16),
    "C": Fraction(-287, 1250),
    "D_first": Fraction(-296, 625),
    "D_second": Fraction(-5, 16),
}
EXPECTED_CONSTANT_PREFIXES = {
    "A": {"S1": 242, "S2": 710, "S3": 1231, "S4": 1799},
    "B": {"S1": 160, "S2": 468, "S3": 812, "S4": 1187},
    "C": {"S1": 117, "S2": 344, "S3": 596, "S4": 872},
}
EXPECTED_CONSTANT_TOTALS = {"A": 1939, "B": 1279, "C": 940}
COUNTER_MODULUS = 16
LARGE_BANK_CAPACITY = 1_000_000_000
RESET_TEST_BANK_CAPACITY = 700

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object) -> bool:
    """Print and count one deterministic check."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS" if ok else "FAIL"), label, "::", detail)
    return ok


@dataclass(slots=True)
class Cell:
    """One predecessor-linked snapshot in a finite counter chain."""

    index: int
    predecessor: int | None
    rotor: int
    carry_count: int
    bank_slot: int
    label: str
    generator_coordinate: Fraction


class RetainedCounterChain:
    """K=16 rotor/carry state plus a supplied finite bank reset procedure."""

    def __init__(self, bank_capacity: int, resets_allowed: int):
        if bank_capacity <= 0 or resets_allowed < 0:
            raise ValueError("bank_capacity must be positive and resets_allowed nonnegative")
        self.cells: list[Cell] = []
        self.marks: dict[str, int] = {}
        self.rotor = 0
        self.carry_count = 0
        self.bank_capacity = bank_capacity
        self.blanks_left = bank_capacity
        self.bank_slot = 0
        self.resets_allowed = resets_allowed
        self.resets_used = 0
        self.reset_cell_indices: list[int] = []
        self.tick_count = 0

    def _consume_blank(self) -> None:
        if self.blanks_left == 0:
            if self.resets_used >= self.resets_allowed:
                raise RuntimeError("supplied reset allowance exhausted")
            self.blanks_left = self.bank_capacity
            self.bank_slot = 0
            self.resets_used += 1
            self.reset_cell_indices.append(len(self.cells))
        self.blanks_left -= 1
        self.bank_slot += 1

    def append_tick(self, coordinate: Fraction) -> None:
        self._consume_blank()
        self.tick_count += 1
        self.rotor += 1
        if self.rotor == COUNTER_MODULUS:
            self.rotor = 0
            self.carry_count += 1
        predecessor = self.cells[-1].index if self.cells else None
        self.cells.append(
            Cell(
                index=len(self.cells),
                predecessor=predecessor,
                rotor=self.rotor,
                carry_count=self.carry_count,
                bank_slot=self.bank_slot,
                label="tick",
                generator_coordinate=coordinate,
            )
        )

    def mark(self, label: str, coordinate: Fraction) -> None:
        predecessor = self.cells[-1].index if self.cells else None
        cell = Cell(
            index=len(self.cells),
            predecessor=predecessor,
            rotor=self.rotor,
            carry_count=self.carry_count,
            bank_slot=self.bank_slot,
            label=label,
            generator_coordinate=coordinate,
        )
        self.cells.append(cell)
        self.marks[label] = cell.index


def decode_position(chain: RetainedCounterChain, label: str) -> int | None:
    """Decode one marked integer position from rotor and carry state."""
    index = chain.marks.get(label)
    if index is None:
        return None
    cell = chain.cells[index]
    return COUNTER_MODULUS * cell.carry_count + cell.rotor


def decode_interval(
    chain: RetainedCounterChain,
    label_a: str,
    label_b: str,
) -> int | None:
    """Decode an oriented difference after verifying predecessor lineage."""
    index_a = chain.marks.get(label_a)
    index_b = chain.marks.get(label_b)
    if index_a is None or index_b is None:
        return None
    cell_a = chain.cells[index_a]
    cell_b = chain.cells[index_b]
    later = cell_b if cell_b.index >= cell_a.index else cell_a
    earlier = cell_a if cell_b.index >= cell_a.index else cell_b
    cursor: Cell | None = later
    while cursor is not None and cursor is not earlier:
        if cursor.predecessor is None:
            cursor = None
        else:
            cursor = chain.cells[cursor.predecessor]
    if cursor is None:
        return None
    position_a = COUNTER_MODULUS * cell_a.carry_count + cell_a.rotor
    position_b = COUNTER_MODULUS * cell_b.carry_count + cell_b.rotor
    return position_b - position_a


def exact_ratio(
    numerator_chain: RetainedCounterChain,
    denominator_chain: RetainedCounterChain,
    label_a: str,
    label_b: str,
) -> Fraction | None:
    numerator = decode_interval(numerator_chain, label_a, label_b)
    denominator = decode_interval(denominator_chain, label_a, label_b)
    if numerator is None or denominator in (None, 0):
        return None
    return Fraction(numerator, denominator)


def piecewise_tick_coordinates(
    segments: Sequence[tuple[Fraction, Fraction, Fraction]],
    generator_end: Fraction,
) -> list[Fraction]:
    """Return exact coordinates of the supplied accumulated-slope crossings."""
    ticks: list[Fraction] = []
    accumulated = Fraction(0)
    next_level = 1
    for signed_slope, start, stop in segments:
        magnitude = abs(signed_slope)
        segment_stop = min(stop, generator_end)
        while True:
            coordinate = start + (Fraction(next_level) - accumulated) / magnitude
            if start <= coordinate < segment_stop:
                ticks.append(coordinate)
                next_level += 1
            else:
                break
        accumulated += magnitude * (segment_stop - start)
        if segment_stop >= generator_end:
            break
    return ticks


def constant_tick_coordinates(slope: Fraction) -> list[Fraction]:
    return piecewise_tick_coordinates(
        [(slope, Fraction(0), GENERATOR_END)],
        GENERATOR_END,
    )


def constant_prefix_count_oracle(slope: Fraction, coordinate: Fraction) -> int:
    """Count positive integer levels at or before a coordinate by exact division."""
    accumulated = abs(slope) * coordinate
    return accumulated.numerator // accumulated.denominator


def constant_strict_total_oracle(slope: Fraction) -> int:
    """Count positive integer levels strictly before the excluded upper endpoint."""
    accumulated = abs(slope) * GENERATOR_END
    return (accumulated.numerator - 1) // accumulated.denominator


def constant_crossing_coordinates_oracle(slope: Fraction) -> list[Fraction]:
    """Enumerate the exact constant-slope crossings from independent level bounds."""
    total = constant_strict_total_oracle(slope)
    return [Fraction(level, abs(slope)) for level in range(1, total + 1)]


def ordered_items(
    ticks: Sequence[Fraction],
    labels: dict[str, Fraction],
    reverse: bool,
) -> list[tuple[Fraction, int, str, str | None]]:
    items = [(coordinate, 0, "tick", None) for coordinate in ticks]
    items.extend(
        (coordinate, 1, "label", label) for label, coordinate in labels.items()
    )
    if reverse:
        items.sort(key=lambda item: (-item[0], -item[1]))
    else:
        items.sort(key=lambda item: (item[0], item[1]))
    return items


def build_chain(
    ticks: Sequence[Fraction],
    labels: dict[str, Fraction],
    bank_capacity: int,
    resets_allowed: int,
    reverse: bool = False,
) -> RetainedCounterChain:
    chain = RetainedCounterChain(bank_capacity, resets_allowed)
    for coordinate, _priority, kind, label in ordered_items(ticks, labels, reverse):
        if kind == "tick":
            chain.append_tick(coordinate)
        else:
            assert label is not None
            chain.mark(label, coordinate)
    return chain


def two_count_tolerance(counts: Iterable[int | None]) -> float:
    nonzero = [abs(value) for value in counts if value not in (None, 0)]
    return 2.0 / min(nonzero) if nonzero else math.inf


class SuppliedCrossOrderPredicate:
    """Finite per-device position predicate supplied as part of the fixture."""

    def __init__(self, devices: Sequence[str]):
        self.positions = {device: 0 for device in devices}
        self.shared_snapshots: list[dict[str, int]] = []

    def append_local(self, device: str) -> None:
        self.positions[device] += 1

    def try_shared(self) -> str:
        snapshot = dict(self.positions)
        if any(
            not all(previous[device] < snapshot[device] for device in self.positions)
            for previous in self.shared_snapshots
        ):
            return "refused_inverted"
        for device in self.positions:
            self.positions[device] += 1
        self.shared_snapshots.append(snapshot)
        return "accepted"

    def inject_snapshot(self, positions: dict[str, int]) -> None:
        """Supply the declared adversarial input without applying the predicate."""
        self.shared_snapshots.append(dict(positions))


def fraction_payload(value: Fraction | None) -> object:
    if value is None:
        return None
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def all_label_pairs() -> list[tuple[str, str]]:
    labels = list(COREGISTRATION_COORDINATES)
    return list(combinations(labels, 2))


def main() -> int:
    receipt: dict[str, object] = {
        "authority": "none",
        "audit": "unset",
        "fixture_sha256": FIXTURE_SHA256,
        "supplied_fixture": SUPPLIED_FIXTURE,
        "dependencies": [],
        "execution_imports": EXECUTION_IMPORTS,
    }

    ticks = {name: constant_tick_coordinates(SLOPES[name]) for name in ("A", "B", "C")}
    forward = {
        name: build_chain(values, COREGISTRATION_COORDINATES, LARGE_BANK_CAPACITY, 0)
        for name, values in ticks.items()
    }
    reverse = {
        name: build_chain(
            values,
            COREGISTRATION_COORDINATES,
            LARGE_BANK_CAPACITY,
            0,
            reverse=True,
        )
        for name, values in ticks.items()
    }
    pairs = all_label_pairs()

    # 1. Exact counter snapshots equal independent exact tick-prefix oracles.
    oracle_totals = {
        name: constant_strict_total_oracle(SLOPES[name]) for name in ("A", "B", "C")
    }
    oracle_prefixes = {
        name: {
            label: constant_prefix_count_oracle(SLOPES[name], coordinate)
            for label, coordinate in COREGISTRATION_COORDINATES.items()
        }
        for name in ("A", "B", "C")
    }
    generated_crossings_match_oracle = all(
        ticks[name] == constant_crossing_coordinates_oracle(SLOPES[name])
        for name in ("A", "B", "C")
    )
    b_s1_tie_exact = (
        Fraction(EXPECTED_CONSTANT_PREFIXES["B"]["S1"], abs(SLOPES["B"]))
        == COREGISTRATION_COORDINATES["S1"]
    )
    b_endpoint_excluded_exact = (
        Fraction(EXPECTED_CONSTANT_TOTALS["B"] + 1, abs(SLOPES["B"]))
        == GENERATOR_END
        and ticks["B"][-1] < GENERATOR_END
    )
    prefix_details: dict[str, dict[str, int | None]] = {}
    prefix_ok = (
        oracle_totals == EXPECTED_CONSTANT_TOTALS
        and oracle_prefixes == EXPECTED_CONSTANT_PREFIXES
        and generated_crossings_match_oracle
        and b_s1_tie_exact
        and b_endpoint_excluded_exact
    )
    for name, chain in forward.items():
        prefix_details[name] = {}
        for label in COREGISTRATION_COORDINATES:
            expected = oracle_prefixes[name][label]
            observed = decode_position(chain, label)
            prefix_details[name][label] = observed
            prefix_ok = (
                prefix_ok
                and observed == expected
                and observed == EXPECTED_CONSTANT_PREFIXES[name][label]
            )
    check(
        "exact counter snapshots equal supplied tick-prefix counts",
        prefix_ok,
        prefix_details,
    )

    # 2. Exact telescoping on every ordered label triple for every stream.
    telescoping_rows: list[dict[str, object]] = []
    telescoping_ok = True
    for name, chain in forward.items():
        for label_a, label_b, label_c in combinations(COREGISTRATION_COORDINATES, 3):
            first = decode_interval(chain, label_a, label_b)
            second = decode_interval(chain, label_b, label_c)
            total = decode_interval(chain, label_a, label_c)
            row_ok = first is not None and second is not None and first + second == total
            telescoping_ok = telescoping_ok and row_ok
            telescoping_rows.append(
                {
                    "stream": name,
                    "labels": [label_a, label_b, label_c],
                    "first": first,
                    "second": second,
                    "total": total,
                }
            )
    check(
        "exact integer telescoping holds on all supplied label triples",
        telescoping_ok,
        {"rows": len(telescoping_rows)},
    )

    # 3. Exact orientation reversal, including exact rational count ratios.
    reversal_ok = all(
        decode_interval(reverse[name], label_a, label_b)
        == -decode_interval(forward[name], label_a, label_b)
        for name in forward
        for label_a, label_b in pairs
    )
    ratio_forward_ab = exact_ratio(forward["B"], forward["A"], "S1", "S4")
    ratio_reverse_ab = exact_ratio(reverse["B"], reverse["A"], "S1", "S4")
    ratio_forward_bc = exact_ratio(forward["C"], forward["B"], "S1", "S4")
    ratio_reverse_bc = exact_ratio(reverse["C"], reverse["B"], "S1", "S4")
    ratio_invariance_ok = (
        ratio_forward_ab == ratio_reverse_ab and ratio_forward_bc == ratio_reverse_bc
    )
    check(
        "exact reversal negates decoded intervals and preserves rational count ratios",
        reversal_ok and ratio_invariance_ok,
        {
            "interval_pairs_checked": len(forward) * len(pairs),
            "ratio_B_over_A": fraction_payload(ratio_forward_ab),
            "ratio_C_over_B": fraction_payload(ratio_forward_bc),
        },
    )

    # 4. One supplied reset preserves every marked position and interval.
    reset_chain = build_chain(
        ticks["B"],
        COREGISTRATION_COORDINATES,
        RESET_TEST_BANK_CAPACITY,
        1,
    )
    control_chain = forward["B"]
    reset_index = reset_chain.reset_cell_indices[0] if reset_chain.reset_cell_indices else -1
    positions_equal = all(
        decode_position(reset_chain, label) == decode_position(control_chain, label)
        for label in COREGISTRATION_COORDINATES
    )
    intervals_equal = all(
        decode_interval(reset_chain, *pair) == decode_interval(control_chain, *pair)
        for pair in pairs
    )
    reset_inside = (
        reset_chain.marks["S2"] < reset_index < reset_chain.marks["S3"]
    )
    reset_ok = (
        reset_chain.resets_used == 1
        and reset_inside
        and positions_equal
        and intervals_equal
    )
    carry_erasure_mutant = copy.deepcopy(reset_chain)
    carry_offset = carry_erasure_mutant.cells[reset_index].carry_count
    for cell in carry_erasure_mutant.cells[reset_index:]:
        cell.carry_count -= carry_offset
    carry_retention_load_bearing = (
        decode_interval(carry_erasure_mutant, "S1", "S3")
        != decode_interval(control_chain, "S1", "S3")
    )
    check(
        "exact marked counts are invariant under the supplied one-reset procedure",
        reset_ok and carry_retention_load_bearing,
        {
            "resets_used": reset_chain.resets_used,
            "reset_cell_index": reset_index,
            "inside_S2_S3": reset_inside,
            "positions_equal": positions_equal,
            "intervals_equal": intervals_equal,
            "carry_erasure_control_changes_S1_S3": carry_retention_load_bearing,
        },
    )

    # 5. A missing label is undefined; an interval not using it is unchanged.
    missing = copy.deepcopy(forward["B"])
    surviving_before = decode_interval(missing, "S1", "S3")
    del missing.marks["S2"]
    missing_results = [
        decode_interval(missing, "S1", "S2"),
        decode_interval(missing, "S2", "S3"),
        decode_position(missing, "S2"),
    ]
    surviving_after = decode_interval(missing, "S1", "S3")
    check(
        "missing-label queries return None while an unrelated marked interval is unchanged",
        all(value is None for value in missing_results)
        and surviving_before == surviving_after,
        {
            "missing_results": missing_results,
            "surviving_S1_S3": surviving_after,
        },
    )

    # 6. Exact decoded-count additivity across the supplied piecewise stream.
    ticks_d = piecewise_tick_coordinates(
        [
            (SLOPES["D_first"], Fraction(0), PIECEWISE_SPLIT),
            (SLOPES["D_second"], PIECEWISE_SPLIT, GENERATOR_END),
        ],
        GENERATOR_END,
    )
    piecewise_labels = {
        "D0": Fraction(0),
        "D_split": PIECEWISE_SPLIT,
        "D_end": GENERATOR_END,
    }
    chain_d = build_chain(ticks_d, piecewise_labels, LARGE_BANK_CAPACITY, 0)
    d_first = decode_interval(chain_d, "D0", "D_split")
    d_second = decode_interval(chain_d, "D_split", "D_end")
    d_total = decode_interval(chain_d, "D0", "D_end")
    accumulated_split = abs(SLOPES["D_first"]) * PIECEWISE_SPLIT
    accumulated_end = accumulated_split + abs(SLOPES["D_second"]) * (
        GENERATOR_END - PIECEWISE_SPLIT
    )
    floor_first = accumulated_split.numerator // accumulated_split.denominator
    floor_total = accumulated_end.numerator // accumulated_end.denominator
    piecewise_ok = (
        d_first is not None
        and d_second is not None
        and d_first + d_second == d_total
        and d_first == floor_first
        and d_total == floor_total
        and d_second == floor_total - floor_first
    )
    check(
        "exact decoded-count additivity holds across the supplied slope change",
        piecewise_ok,
        {
            "first": d_first,
            "second": d_second,
            "total": d_total,
            "accumulated_at_split": str(accumulated_split),
            "accumulated_at_end": str(accumulated_end),
        },
    )

    # 7. Execute the supplied finite cross-order predicate and adversarial row.
    ordinary = SuppliedCrossOrderPredicate(["A", "B", "C"])
    for _ in range(2):
        for device in ordinary.positions:
            ordinary.append_local(device)
    ordinary_results = [ordinary.try_shared() for _ in range(4)]
    ordinary_mutation_ok = ordinary.positions == {"A": 6, "B": 6, "C": 6} and (
        ordinary.shared_snapshots
        == [
            {"A": 2, "B": 2, "C": 2},
            {"A": 3, "B": 3, "C": 3},
            {"A": 4, "B": 4, "C": 4},
            {"A": 5, "B": 5, "C": 5},
        ]
    )
    adversarial = SuppliedCrossOrderPredicate(["A", "B", "C"])
    for _ in range(4):
        for device in adversarial.positions:
            adversarial.append_local(device)
    first_result = adversarial.try_shared()
    first_accept_mutation_ok = (
        adversarial.positions == {"A": 5, "B": 5, "C": 5}
        and adversarial.shared_snapshots == [{"A": 4, "B": 4, "C": 4}]
    )
    adversarial.inject_snapshot({"A": 1, "B": 9, "C": 1})
    positions_before_refusal = dict(adversarial.positions)
    snapshots_before_refusal = copy.deepcopy(adversarial.shared_snapshots)
    adversarial_result = adversarial.try_shared()
    refusal_state_unchanged = (
        adversarial.positions == positions_before_refusal
        and adversarial.shared_snapshots == snapshots_before_refusal
    )
    check(
        "supplied cross-order predicate accepts ordinary rows and refuses the injected inversion",
        ordinary_results == ["accepted"] * 4
        and ordinary_mutation_ok
        and first_result == "accepted"
        and first_accept_mutation_ok
        and adversarial_result == "refused_inverted"
        and refusal_state_unchanged,
        {
            "ordinary": ordinary_results,
            "ordinary_accept_mutation_exact": ordinary_mutation_ok,
            "first_adversarial_fixture_call": first_result,
            "first_accept_mutation_exact": first_accept_mutation_ok,
            "after_injected_snapshot": adversarial_result,
            "refusal_state_unchanged": refusal_state_unchanged,
        },
    )

    # 8. Decoder boundary control: metadata ignored, index/lineage retained.
    metadata_mutant = copy.deepcopy(forward["B"])
    baseline_interval = decode_interval(metadata_mutant, "S1", "S3")
    for cell in metadata_mutant.cells:
        cell.bank_slot = -999
        cell.generator_coordinate = Fraction(999_999)
    metadata_interval = decode_interval(metadata_mutant, "S1", "S3")
    broken_lineage = copy.deepcopy(forward["B"])
    broken_lineage.cells[broken_lineage.marks["S3"]].predecessor = None
    broken_interval = decode_interval(broken_lineage, "S1", "S3")
    check(
        "displayed decoders ignore bank/generator metadata but retain index-oriented predecessor lineage",
        metadata_interval == baseline_interval and broken_interval is None,
        {
            "baseline_S1_S3": baseline_interval,
            "metadata_mutant_S1_S3": metadata_interval,
            "broken_predecessor_S1_S3": broken_interval,
            "index_lineage_remains_used": True,
        },
    )

    # 9. Explicitly non-exact finite floating diagnostic.
    adjacent_pairs = [("S1", "S2"), ("S2", "S3"), ("S3", "S4")]
    exact_ab = [exact_ratio(forward["B"], forward["A"], *pair) for pair in adjacent_pairs]
    exact_bc = [exact_ratio(forward["C"], forward["B"], *pair) for pair in adjacent_pairs]
    float_ab = [float(value) for value in exact_ab if value is not None]
    float_bc = [float(value) for value in exact_bc if value is not None]
    count_values_ab = [
        decode_interval(chain, *pair)
        for chain in (forward["A"], forward["B"])
        for pair in adjacent_pairs
    ]
    count_values_bc = [
        decode_interval(chain, *pair)
        for chain in (forward["B"], forward["C"])
        for pair in adjacent_pairs
    ]
    spread_ab = max(float_ab) - min(float_ab)
    spread_bc = max(float_bc) - min(float_bc)
    tolerance_ab = two_count_tolerance(count_values_ab)
    tolerance_bc = two_count_tolerance(count_values_bc)
    float_ok = spread_ab <= tolerance_ab and spread_bc <= tolerance_bc
    check(
        "finite floating diagnostic only: segment-ratio spreads fit disclosed two-count tolerances",
        float_ok,
        {
            "B_over_A": float_ab,
            "spread_B_over_A": spread_ab,
            "tolerance_B_over_A": tolerance_ab,
            "C_over_B": float_bc,
            "spread_C_over_B": spread_bc,
            "tolerance_C_over_B": tolerance_bc,
            "classification": "finite floating diagnostic, not exact identity",
        },
    )

    receipt["exact_results"] = {
        "counter_positions": prefix_details,
        "telescoping_rows_checked": len(telescoping_rows),
        "reversal_interval_pairs_checked": len(forward) * len(pairs),
        "ratio_B_over_A": fraction_payload(ratio_forward_ab),
        "ratio_C_over_B": fraction_payload(ratio_forward_bc),
        "one_reset": {
            "reset_cell_index": reset_index,
            "inside_S2_S3": reset_inside,
            "positions_equal": positions_equal,
            "intervals_equal": intervals_equal,
        },
        "missing_label_results": missing_results,
        "piecewise_counts": {
            "first": d_first,
            "second": d_second,
            "total": d_total,
        },
        "cross_order_results": {
            "ordinary": ordinary_results,
            "ordinary_accept_mutation_exact": ordinary_mutation_ok,
            "first_accept_mutation_exact": first_accept_mutation_ok,
            "injected_inversion": adversarial_result,
            "refusal_state_unchanged": refusal_state_unchanged,
        },
    }
    receipt["controls"] = {
        "constant_crossing_oracle": {
            "strict_totals": oracle_totals,
            "literal_prefixes_match": oracle_prefixes == EXPECTED_CONSTANT_PREFIXES,
            "generated_crossings_match": generated_crossings_match_oracle,
            "B_S1_tie_exact": b_s1_tie_exact,
            "B_generator_endpoint_excluded": b_endpoint_excluded_exact,
        },
        "carry_erasure_changes_cross_reset_interval": carry_retention_load_bearing,
        "bank_and_generator_metadata_mutation_preserves_interval": (
            metadata_interval == baseline_interval
        ),
        "predecessor_break_makes_interval_undefined": broken_interval is None,
        "index_lineage_remains_used": True,
        "cross_order_accept_mutation_exact": (
            ordinary_mutation_ok and first_accept_mutation_ok
        ),
        "cross_order_refusal_state_unchanged": refusal_state_unchanged,
    }
    receipt["floating_diagnostic"] = {
        "classification": "finite floating diagnostic, not exact identity",
        "B_over_A": float_ab,
        "spread_B_over_A": spread_ab,
        "tolerance_B_over_A": tolerance_ab,
        "C_over_B": float_bc,
        "spread_C_over_B": spread_bc,
        "tolerance_C_over_B": tolerance_bc,
    }
    receipt["boundaries"] = [
        "The tick streams, slopes, generator span, labels, decoder, counter modulus, bank sizes, reset procedure, cell topology, diagnostic tolerance, and cross-order predicate are supplied.",
        "The generator coordinate orders the fixture and is not decoded.",
        "Cell indices and predecessor links remain load-bearing for lineage and orientation.",
        "Retained means only that carry_count is unchanged through the one supplied refill; it is not audit retained status or physical persistence.",
        "The cross-order result executes the supplied finite predicate; it does not select or derive that predicate.",
        "Binary floating-point segment-ratio checks are finite diagnostics with disclosed tolerances; the integer and Fraction identities are exact.",
        "No tick, count, coordinate, label order, or decoded interval is identified with physical time, elapsed duration, a time metric, causal order, chronology, evolution, or an update law.",
        "The finite counter is not a physical clock; no count or count ratio is a clock rate, frequency, calibration, detector observable, or empirical measurement.",
        "No label, snapshot, cell, rotor, or carry count is a framework Record; no Record formation, locking, permanence, readout, or realized-history mechanism is constructed.",
        "No encoding into physical M_2(C) sites is supplied, so this is not a physical-site compiler or a resource-overhead, noise, leakage, deletion, held-out-size, or scaling result.",
        "These construction-scope boundaries leave downstream physical bridges open and assert no route-independent no-go or axiom pressure.",
    ]
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0

    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("RESULT", PASS, FAIL)
    print("RECEIPT", RECEIPT.relative_to(ROOT))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
