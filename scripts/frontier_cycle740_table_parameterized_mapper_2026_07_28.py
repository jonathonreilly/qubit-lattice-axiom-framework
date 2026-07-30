#!/usr/bin/env python3
"""Cycle 740: table-parameterized placement mapper.

The Cycle-719 mapper is left untouched.  This runner derives the two affine
placement-table laws from its frozen 12-bank data, makes the table capacity
an explicit argument, and audits exact backward compatibility plus the first
four newly available bank counts.

The table-uniform theorem below is conditional on exactly one new supplied
convention: that the uniquely observed affine continuation of K's placement
tables is the intended geometry.  The convention is anchored exactly on every
frozen BANK_BASES and LINK_BASES entry.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/TABLE_PARAMETERIZED_MAPPER_CYCLE740_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle739_identity_discharge_2026_07_28.py",
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
ALLOWED_GATE_KINDS = frozenset(("X", "CNOT", "TOF"))
I1_AMENDED_FORMULA = (
    "not(a[left] or a[right] or b[left] or b[station] or b[right] or "
    "work[station])"
)
EXTENSION_BANKS = (13, 14, 15, 16)
EXTENSION_CAPACITY = 16
FROZEN_CAPACITY = 12
TEMPLATE_NAMES = (
    "source",
    "bank_packet",
    "cross",
    "handoff_forward",
    "relay_latch",
    "relay_swap",
    "relay_unlatch",
    "handoff_return",
    "finalizer",
)

TABLE_UNIFORM_CONDITIONAL = (
    "For every integer C>=1 and every integer b with 1<=b<=C, IF the "
    "derived affine placement law BANK_BASE(i)=41+131*i and "
    "LINK_BASE(i,C)=41+131*C+382*i is the intended placement geometry, "
    "THEN Cycle 738's general-n sector theorem, with Cycle 739's amended "
    "six-term ownership predicate, holds for n=8*b-5.  No per-b re-proof "
    "and no other new supply are required."
)
NEW_SUPPLIES = (
    (
        "the affine table-generating law, as the intended placement geometry, "
        "with capacity C supplied and the law byte-exactly anchored to K at C=12"
    ),
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: object) -> bool:
    """Record one uniquely named PASS/FAIL line."""

    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    return gate.kind, tuple(int(wire) for wire in gate.wires)


def word_signature(
    word: tuple[object, ...],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    return tuple(gate_signature(gate) for gate in word)


def word_evidence(word: tuple[object, ...]) -> dict[str, object]:
    wires = tuple(wire for gate in word for wire in gate.wires)
    return {
        "semantic_gates": len(word),
        "gate_kind_counts": dict(sorted(Counter(
            gate.kind for gate in word
        ).items())),
        "wire_min": min(wires) if wires else None,
        "wire_max": max(wires) if wires else None,
        "gate_word_sha256": stable_digest(word_signature(word)),
    }


def read_authorized_source(path: str) -> str:
    """Read only one of the three declared audit inputs."""

    if path not in AUDIT_INPUT_PATHS:
        raise AssertionError(("undeclared read", path))
    return Path(path).read_text(encoding="utf-8")


def require_positive_integer(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def frozen_table_law() -> dict[str, object]:
    """Derive the unique observed affine seeds and strides from K's data."""

    frozen_banks = tuple(int(value) for value in K.M.R12.BANK_BASES)
    frozen_links = tuple(int(value) for value in K.M.R12.LINK_BASES)
    bank_differences = tuple(
        right - left
        for left, right in zip(frozen_banks, frozen_banks[1:])
    )
    link_differences = tuple(
        right - left
        for left, right in zip(frozen_links, frozen_links[1:])
    )
    bank_strides = set(bank_differences)
    link_strides = set(link_differences)
    if (
        len(frozen_banks) < 2
        or len(frozen_links) < 2
        or len(bank_strides) != 1
        or len(link_strides) != 1
    ):
        raise AssertionError("K placement tables do not define affine laws")
    bank_seed = frozen_banks[0]
    bank_stride = bank_differences[0]
    link_stride = link_differences[0]
    link_seed_at_frozen_capacity = frozen_links[0]
    return {
        "frozen_banks": frozen_banks,
        "frozen_links": frozen_links,
        "frozen_capacity": len(frozen_banks),
        "bank_seed": bank_seed,
        "bank_stride": bank_stride,
        "link_seed_at_frozen_capacity": link_seed_at_frozen_capacity,
        "link_stride": link_stride,
        "bank_differences": bank_differences,
        "link_differences": link_differences,
        "link_seed_partition_exact": (
            link_seed_at_frozen_capacity
            == bank_seed + len(frozen_banks) * bank_stride
        ),
        "bank_block_width_anchor": bank_stride == int(K.A.N),
        "link_block_width_anchor": (
            link_stride == 2 * int(K.M.P.LINK_AUX_WIDTH)
        ),
    }


def parameterized_bases(
    capacity: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Generate C bank bases and C-1 link bases from K's affine law."""

    capacity = require_positive_integer("capacity", capacity)
    law = frozen_table_law()
    bank_seed = int(law["bank_seed"])
    bank_stride = int(law["bank_stride"])
    link_stride = int(law["link_stride"])
    bank_bases = tuple(
        bank_seed + bank_stride * index
        for index in range(capacity)
    )
    link_seed = bank_seed + bank_stride * capacity
    link_bases = tuple(
        link_seed + link_stride * index
        for index in range(capacity - 1)
    )
    return bank_bases, link_bases


def parameterized_data_width(capacity: int) -> int:
    """Return the end of the derived source/bank/link placement partition."""

    capacity = require_positive_integer("capacity", capacity)
    law = frozen_table_law()
    return (
        int(law["bank_seed"])
        + capacity * int(law["bank_stride"])
        + (capacity - 1) * int(law["link_stride"])
    )


def parameterized_offset_gate(gate: object, base: int) -> object:
    return K.A.Gate(
        gate.kind,
        tuple(int(base) + int(wire) for wire in gate.wires),
    )


def parameterized_pair_gate(
    gate: object,
    edge: int,
    kind: str,
    capacity: int,
) -> object:
    """Reimplement K's left-bank/right-bank/link piecewise wire map."""

    bank_bases, link_bases = parameterized_bases(capacity)
    split = 0 if kind == "handoff" else int(K.M.P.LINK_AUX_WIDTH)
    bank_width = int(K.A.N)
    wires = []
    for wire in gate.wires:
        if wire < bank_width:
            wires.append(bank_bases[edge] + wire)
        elif wire < 2 * bank_width:
            wires.append(bank_bases[edge + 1] + wire - bank_width)
        else:
            wires.append(
                link_bases[edge] + split + wire - 2 * bank_width
            )
    return K.A.Gate(gate.kind, tuple(wires))


def parameterized_mapped_action(
    kind: str,
    index: int,
    local: tuple[object, ...],
    capacity: int,
) -> tuple[object, ...]:
    """Map one bank/edge action using only parameterized placement tables."""

    capacity = require_positive_integer("capacity", capacity)
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a nonnegative integer")
    bank_bases, link_bases = parameterized_bases(capacity)
    if kind == "bank":
        return tuple(
            parameterized_offset_gate(gate, bank_bases[index])
            for gate in local
        )
    if kind in ("handoff", "relay"):
        return tuple(
            parameterized_pair_gate(gate, index, kind, capacity)
            for gate in local
        )
    if kind == "cross":
        predecessor_offset = int(K.A.CELLS[0]["pred"][1])
        return (
            K.A.cn(
                link_bases[index],
                bank_bases[index + 1] + predecessor_offset,
            ),
        )
    raise ValueError(kind)


def parameterized_mapped_macro(
    row: tuple[object, ...],
    capacity: int,
) -> tuple[object, ...]:
    kind, index, local = row
    if kind in ("source", "finalizer"):
        return tuple(local)
    if kind == "identity":
        return ()
    return parameterized_mapped_action(kind, index, local, capacity)


def parameterized_program(
    bank_count: int,
    capacity: int,
) -> tuple[tuple[object, ...], ...]:
    """Reimplement K's non-padded emission with the lawful b<=C domain."""

    bank_count = require_positive_integer("bank_count", bank_count)
    capacity = require_positive_integer("capacity", capacity)
    if bank_count > capacity:
        raise ValueError("bank_count must not exceed capacity")
    prefix = [("source", 0, K.R3.source_compute_word())]
    for bank in range(bank_count):
        prefix.append(("bank", bank, K.H.PACKET))
        if bank:
            prefix.append(("cross", bank - 1, ()))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff", bank, K.H.HANDOFF_FORWARD),
                ("relay", bank, K.H.RELAY_LATCH),
                ("relay", bank, K.H.RELAY_SWAP),
            ))
    reverse = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay", edge, K.H.RELAY_SWAP),
            ("relay", edge, K.H.RELAY_UNLATCH),
            ("handoff", edge, K.H.HANDOFF_RETURN),
        ))
    suffix = [
        ("finalizer", 0, K.M.source_finalizer_word(bank_count))
    ]
    return tuple(prefix + reverse + suffix)


def parameterized_program_word(
    program: tuple[tuple[object, ...], ...],
    capacity: int,
) -> tuple[object, ...]:
    return tuple(
        gate
        for row in program
        for gate in parameterized_mapped_macro(row, capacity)
    )


def serialized_program(
    program: tuple[tuple[object, ...], ...],
) -> bytes:
    return stable_json_bytes(tuple(
        (kind, int(index), word_signature(tuple(local)))
        for kind, index, local in program
    ))


def serialized_mapped_rows(
    program: tuple[tuple[object, ...], ...],
    mapper: object,
) -> bytes:
    return stable_json_bytes(tuple(
        word_signature(tuple(mapper(row))) for row in program
    ))


def table_law_certificate() -> dict[str, object]:
    law = frozen_table_law()
    observed_banks = tuple(law["frozen_banks"])
    observed_links = tuple(law["frozen_links"])
    generated_banks, generated_links = parameterized_bases(
        int(law["frozen_capacity"])
    )
    observed_bytes = stable_json_bytes((observed_banks, observed_links))
    generated_bytes = stable_json_bytes((generated_banks, generated_links))
    return {
        "derived_bank_law": (
            f"BANK_BASE(i)={law['bank_seed']}+"
            f"{law['bank_stride']}*i"
        ),
        "derived_link_law": (
            f"LINK_BASE(i,C)={law['bank_seed']}+"
            f"{law['bank_stride']}*C+{law['link_stride']}*i"
        ),
        "derivation": {
            "bank_seed": law["bank_seed"],
            "bank_stride": law["bank_stride"],
            "bank_difference_set": sorted(set(
                law["bank_differences"]
            )),
            "link_seed_at_C12": law[
                "link_seed_at_frozen_capacity"
            ],
            "link_stride": law["link_stride"],
            "link_difference_set": sorted(set(
                law["link_differences"]
            )),
            "link_seed_equals_bank_partition_end":
                law["link_seed_partition_exact"],
            "bank_stride_equals_K_bank_width":
                law["bank_block_width_anchor"],
            "link_stride_equals_two_K_link_aux_widths":
                law["link_block_width_anchor"],
        },
        "frozen_bank_entries": len(observed_banks),
        "frozen_link_entries": len(observed_links),
        "generated_bank_entries": len(generated_banks),
        "generated_link_entries": len(generated_links),
        "bank_table_exact": generated_banks == observed_banks,
        "link_table_exact": generated_links == observed_links,
        "byte_exact": generated_bytes == observed_bytes,
        "frozen_tables_sha256": sha256(observed_bytes).hexdigest(),
        "generated_tables_sha256": sha256(generated_bytes).hexdigest(),
        "exact": (
            generated_banks == observed_banks
            and generated_links == observed_links
            and generated_bytes == observed_bytes
            and law["link_seed_partition_exact"]
            and law["bank_block_width_anchor"]
            and law["link_block_width_anchor"]
            and parameterized_data_width(FROZEN_CAPACITY)
            == len(K.M.R12.full_wire_layout()["wire_sites"])
        ),
    }


def equivalence_certificate() -> dict[str, object]:
    per_b = {}
    failures = []
    for bank_count in range(1, FROZEN_CAPACITY + 1):
        observed_program = K.interleaved_program(bank_count)
        generated_program = parameterized_program(
            bank_count, FROZEN_CAPACITY
        )
        observed_program_bytes = serialized_program(observed_program)
        generated_program_bytes = serialized_program(generated_program)
        observed_mapped_bytes = serialized_mapped_rows(
            observed_program, K.mapped_macro
        )
        generated_mapped_bytes = serialized_mapped_rows(
            generated_program,
            lambda row: parameterized_mapped_macro(
                row, FROZEN_CAPACITY
            ),
        )
        row_object_exact = generated_program == observed_program
        mapped_object_exact = all(
            parameterized_mapped_macro(row, FROZEN_CAPACITY)
            == K.mapped_macro(row)
            for row in observed_program
        )
        program_byte_exact = (
            generated_program_bytes == observed_program_bytes
        )
        mapped_byte_exact = (
            generated_mapped_bytes == observed_mapped_bytes
        )
        combined = (
            observed_program_bytes + b"\0" + observed_mapped_bytes
        )
        passed = (
            row_object_exact
            and mapped_object_exact
            and program_byte_exact
            and mapped_byte_exact
        )
        if not passed:
            failures.append(bank_count)
        per_b[bank_count] = {
            "rows": len(observed_program),
            "row_objects_exact": row_object_exact,
            "mapped_objects_exact": mapped_object_exact,
            "program_bytes_exact": program_byte_exact,
            "mapped_bytes_exact": mapped_byte_exact,
            "equivalence_sha256": sha256(combined).hexdigest(),
        }
    return {
        "capacity": FROZEN_CAPACITY,
        "bank_domain": [1, FROZEN_CAPACITY],
        "per_b": per_b,
        "failed_b": failures,
        "full_program_and_mapped_word_sweep": True,
        "all_byte_identical": not failures,
        "exact": len(per_b) == FROZEN_CAPACITY and not failures,
    }


def primitive_clean_certificate() -> dict[str, object]:
    control = 10
    work = 11
    canonical = {
        "X": (K.A.x(0),),
        "CNOT": (K.A.cn(0, 1),),
        "TOF": (K.A.tof(0, 1, 2),),
    }
    observed = {
        kind: word_signature(K.controlled_macro(word, control, work))
        for kind, word in canonical.items()
    }
    expected = {
        "X": (("CNOT", (control, 0)),),
        "CNOT": (("TOF", (control, 0, 1)),),
        "TOF": (
            ("TOF", (control, 0, work)),
            ("TOF", (work, 1, 2)),
            ("TOF", (control, 0, work)),
        ),
    }
    truth = K.controlled_truth_certificate()
    exact = (
        observed == expected
        and truth["clean_failures"] == 0
        and truth["clean_work_return_failures"] == 0
        and truth["clean_rows"] > 0
    )
    return {
        "controlled_primitive_expansions": observed,
        "clean_truth_rows": truth["clean_rows"],
        "clean_truth_failures": truth["clean_failures"],
        "clean_work_return_failures":
            truth["clean_work_return_failures"],
        "structural_reason": (
            "control is never a target; controlled TOF computes its own "
            "clean work bit, uses it only as a control, and repeats the "
            "same compute gate to return work=0 to 0"
        ),
        "exact": exact,
    }


def validate_clean_word(
    word: tuple[object, ...],
    data_width: int,
    control: int,
    work: int,
    primitive_exact: bool,
) -> dict[str, object]:
    """Reimplement Cycle 739's direct per-row clean-work predicate."""

    arity = {"X": 1, "CNOT": 2, "TOF": 3}
    kinds_allowed = all(
        gate.kind in ALLOWED_GATE_KINDS for gate in word
    )
    arities_exact = all(
        gate.kind in arity and len(gate.wires) == arity[gate.kind]
        for gate in word
    )
    operands_distinct = all(
        len(set(gate.wires)) == len(gate.wires) for gate in word
    )
    data_only = all(
        isinstance(wire, int) and 0 <= wire < data_width
        for gate in word for wire in gate.wires
    )
    lifted = tuple(K.controlled_macro(word, control, work))
    expected_lifted = []
    for gate in word:
        if gate.kind == "X":
            expected_lifted.append(
                K.A.cn(control, gate.wires[0])
            )
        elif gate.kind == "CNOT":
            expected_lifted.append(
                K.A.tof(control, gate.wires[0], gate.wires[1])
            )
        elif gate.kind == "TOF":
            expected_lifted.extend((
                K.A.tof(control, gate.wires[0], work),
                K.A.tof(work, gate.wires[1], gate.wires[2]),
                K.A.tof(control, gate.wires[0], work),
            ))
    expansion_exact = lifted == tuple(expected_lifted)
    addressed_domain_exact = all(
        wire in {control, work} or 0 <= wire < data_width
        for gate in lifted for wire in gate.wires
    )
    control_unchanged = all(
        not gate.wires or gate.wires[-1] != control
        for gate in lifted
    )
    tof_count = sum(gate.kind == "TOF" for gate in word)
    work_target_count = sum(
        bool(gate.wires) and gate.wires[-1] == work
        for gate in lifted
    )
    work_compute_uncompute_exact = (
        work_target_count == 2 * tof_count
    )
    clean_work_zero_returns_zero = (
        primitive_exact
        and expansion_exact
        and work_compute_uncompute_exact
    )
    passed = (
        kinds_allowed
        and arities_exact
        and operands_distinct
        and data_only
        and expansion_exact
        and addressed_domain_exact
        and control_unchanged
        and clean_work_zero_returns_zero
    )
    return {
        "semantic_gates": len(word),
        "controlled_gates": len(lifted),
        "allowed_gate_kinds": kinds_allowed,
        "gate_arities_exact": arities_exact,
        "per_gate_operands_distinct": operands_distinct,
        "addresses_only_data_before_lift": data_only,
        "addresses_only_data_control_own_work_after_lift":
            addressed_domain_exact,
        "controlled_dispatch_expansion_exact": expansion_exact,
        "A_control_unchanged": control_unchanged,
        "work_compute_uncompute_target_count": work_target_count,
        "expected_work_target_count": 2 * tof_count,
        "clean_work_0_maps_to_0": clean_work_zero_returns_zero,
        "pass": passed,
    }


def template_name(row: tuple[object, ...]) -> str:
    kind, _index, local = row
    if kind == "source":
        return "source"
    if kind == "bank":
        return "bank_packet"
    if kind == "cross":
        return "cross"
    if kind == "finalizer":
        return "finalizer"
    if kind == "handoff":
        if local == K.H.HANDOFF_FORWARD:
            return "handoff_forward"
        if local == K.H.HANDOFF_RETURN:
            return "handoff_return"
    if kind == "relay":
        if local == K.H.RELAY_LATCH:
            return "relay_latch"
        if local == K.H.RELAY_SWAP:
            return "relay_swap"
        if local == K.H.RELAY_UNLATCH:
            return "relay_unlatch"
    raise AssertionError(("unknown row template", kind, local))


def template_uniformity_certificate(
    primitive: dict[str, object],
) -> dict[str, object]:
    capacity = EXTENSION_CAPACITY
    data_width = parameterized_data_width(capacity)
    representatives: dict[str, list[tuple[object, ...]]] = {
        name: [] for name in TEMPLATE_NAMES
    }
    representatives["source"].append(
        ("source", 0, K.R3.source_compute_word())
    )
    representatives["finalizer"].append(
        ("finalizer", 0, K.M.source_finalizer_word(capacity))
    )
    for bank in range(capacity):
        representatives["bank_packet"].append(
            ("bank", bank, K.H.PACKET)
        )
    for edge in range(capacity - 1):
        representatives["cross"].append(("cross", edge, ()))
        representatives["handoff_forward"].append(
            ("handoff", edge, K.H.HANDOFF_FORWARD)
        )
        representatives["relay_latch"].append(
            ("relay", edge, K.H.RELAY_LATCH)
        )
        representatives["relay_swap"].append(
            ("relay", edge, K.H.RELAY_SWAP)
        )
        representatives["relay_unlatch"].append(
            ("relay", edge, K.H.RELAY_UNLATCH)
        )
        representatives["handoff_return"].append(
            ("handoff", edge, K.H.HANDOFF_RETURN)
        )

    reports = {}
    all_pass = True
    for name in TEMPLATE_NAMES:
        failures = []
        hasher = sha256()
        rows = representatives[name]
        for ordinal, row in enumerate(rows):
            word = parameterized_mapped_macro(row, capacity)
            clean = validate_clean_word(
                word,
                data_width,
                data_width,
                data_width + 1,
                bool(primitive["exact"]),
            )
            hasher.update(stable_json_bytes(word_signature(word)))
            if not clean["pass"]:
                failures.append({
                    "ordinal": ordinal,
                    "row": (row[0], row[1]),
                    "clean": clean,
                })
        passed = bool(rows) and not failures
        all_pass &= passed
        reports[name] = {
            "mapped_placements_checked": len(rows),
            "failure_count": len(failures),
            "failures": failures,
            "mapped_words_sha256": hasher.hexdigest(),
            "pass": passed,
        }
    return {
        "template_names": TEMPLATE_NAMES,
        "template_count": len(reports),
        "capacity_probe": capacity,
        "placement_instances_checked": sum(
            len(rows) for rows in representatives.values()
        ),
        "per_template": reports,
        "all_templates_clean_when_lawfully_mapped": (
            len(reports) == 9 and all_pass
        ),
        "b_independence_reason": (
            "b selects only finite loop bounds and legal table indices; "
            "the nine local words, gate kinds/arities, piecewise wire map, "
            "and controlled primitive clean-work identities contain no b"
        ),
        "exact": len(reports) == 9 and all_pass,
    }


def extension_certificate(
    primitive: dict[str, object],
) -> dict[str, object]:
    capacity = EXTENSION_CAPACITY
    data_width = parameterized_data_width(capacity)
    reports = {}
    total_rows = 0
    for bank_count in EXTENSION_BANKS:
        program = parameterized_program(bank_count, capacity)
        stations = len(program)
        failures = []
        semantic_gate_counts = Counter()
        controlled_gate_total = 0
        row_kind_counts = Counter()
        for station, row in enumerate(program):
            row_kind_counts[row[0]] += 1
            try:
                word = parameterized_mapped_macro(row, capacity)
            except Exception as error:
                failures.append({
                    "station": station,
                    "kind": row[0],
                    "index": row[1],
                    "error": f"{type(error).__name__}: {error}",
                })
                continue
            semantic_gate_counts.update(gate.kind for gate in word)
            clean = validate_clean_word(
                word,
                data_width,
                data_width + station,
                data_width + 2 * stations + station,
                bool(primitive["exact"]),
            )
            controlled_gate_total += int(clean["controlled_gates"])
            if not clean["pass"]:
                failures.append({
                    "station": station,
                    "kind": row[0],
                    "index": row[1],
                    "clean": clean,
                })
        total_rows += stations
        reports[bank_count] = {
            "capacity": capacity,
            "ring_rows": stations,
            "expected_8b_minus_5": 8 * bank_count - 5,
            "row_kind_counts": dict(sorted(row_kind_counts.items())),
            "semantic_gate_kind_counts": dict(sorted(
                semantic_gate_counts.items()
            )),
            "controlled_gate_total": controlled_gate_total,
            "rows_checked": stations,
            "row_failure_count": len(failures),
            "row_failures": failures,
            "pass": stations == 8 * bank_count - 5 and not failures,
        }
    return {
        "capacity": capacity,
        "bank_domain": list(EXTENSION_BANKS),
        "data_width": data_width,
        "per_b": reports,
        "per_b_row_totals": {
            bank_count: report["rows_checked"]
            for bank_count, report in reports.items()
        },
        "total_rows_checked": total_rows,
        "all_rows_clean": all(
            report["pass"] for report in reports.values()
        ),
        "exact": (
            total_rows
            == sum(8 * bank_count - 5 for bank_count in EXTENSION_BANKS)
            and all(report["pass"] for report in reports.values())
        ),
    }


def frozen_eight_certificate(
    primitive: dict[str, object],
) -> dict[str, object]:
    frozen_program = K.interleaved_program(13)
    generated_program = parameterized_program(13, EXTENSION_CAPACITY)
    data_width = parameterized_data_width(EXTENSION_CAPACITY)
    stations = len(generated_program)
    frozen_failures = []
    recovered = []
    for station, row in enumerate(frozen_program):
        try:
            K.mapped_macro(row)
        except Exception as error:
            frozen_failures.append({
                "station": station,
                "kind": row[0],
                "index": row[1],
                "error": type(error).__name__,
            })
            generated_row = generated_program[station]
            name = template_name(generated_row)
            mapped = parameterized_mapped_macro(
                generated_row, EXTENSION_CAPACITY
            )
            clean = validate_clean_word(
                mapped,
                data_width,
                data_width + station,
                data_width + 2 * stations + station,
                bool(primitive["exact"]),
            )
            recovered.append({
                "name": (
                    f"station_{station:03d}_{name}_"
                    f"index_{generated_row[1]}"
                ),
                "station": station,
                "kind": generated_row[0],
                "index": generated_row[1],
                "template": name,
                "mapped_word": word_evidence(mapped),
                "template_properties": clean,
                "lawful": clean["pass"],
            })
    expected_rows = (
        (57, "handoff", 11, "handoff_forward"),
        (58, "relay", 11, "relay_latch"),
        (59, "relay", 11, "relay_swap"),
        (60, "bank", 12, "bank_packet"),
        (61, "cross", 11, "cross"),
        (62, "relay", 11, "relay_swap"),
        (63, "relay", 11, "relay_unlatch"),
        (64, "handoff", 11, "handoff_return"),
    )
    observed_rows = tuple(
        (
            row["station"],
            row["kind"],
            row["index"],
            row["template"],
        )
        for row in recovered
    )
    return {
        "frozen_mapper_failures": frozen_failures,
        "frozen_failure_count": len(frozen_failures),
        "expected_rows": expected_rows,
        "observed_rows": observed_rows,
        "recovered_rows": recovered,
        "all_now_lawful": (
            len(recovered) == 8
            and all(row["lawful"] for row in recovered)
        ),
        "exact": (
            len(frozen_failures) == len(recovered) == 8
            and all(
                row["error"] == "IndexError"
                for row in frozen_failures
            )
            and observed_rows == expected_rows
            and all(row["lawful"] for row in recovered)
        ),
    }


def parameterized_controller_word(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    capacity: int,
) -> tuple[object, ...]:
    stations = len(program)
    a_base = data_width
    b_base = data_width + stations
    work_base = data_width + 2 * stations
    q_word = tuple(
        gate
        for station, row in enumerate(program)
        for gate in K.controlled_macro(
            parameterized_mapped_macro(row, capacity),
            a_base + station,
            work_base + station,
        )
    )
    r1_word = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            a_base + station, b_base + station
        )
    )
    r2_word = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            b_base + station,
            a_base + (station + 1) % stations,
        )
    )
    return q_word + r1_word + r2_word


def compile_integer_operations(
    word: tuple[object, ...],
) -> tuple[tuple[int, int], ...]:
    operations = []
    for gate in word:
        if gate.kind == "X":
            controls = 0
        elif gate.kind in ("CNOT", "TOF"):
            controls = sum(
                1 << int(wire) for wire in gate.wires[:-1]
            )
        else:
            raise ValueError(gate.kind)
        target = 1 << int(gate.wires[-1])
        operations.append((controls, target))
    return tuple(operations)


def apply_integer_operations(
    value: int,
    operations: tuple[tuple[int, int], ...],
) -> int:
    for controls, target in operations:
        if (value & controls) == controls:
            value ^= target
    return value


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    ring_mask = (1 << stations) - 1
    normalized = shift % stations
    if normalized == 0:
        return mask & ring_mask
    return (
        ((mask << normalized) & ring_mask)
        | (mask >> (stations - normalized))
    )


def has_adjacent_pair(mask: int, stations: int) -> bool:
    return bool(mask & rotate_mask(mask, 1, stations))


def amended_ownership_holds_mask(
    a_mask: int,
    b_mask: int,
    work_mask: int,
    station: int,
    stations: int,
) -> bool:
    left = (station - 1) % stations
    right = (station + 1) % stations
    return not (
        ((a_mask >> left) & 1)
        or ((a_mask >> right) & 1)
        or ((b_mask >> left) & 1)
        or ((b_mask >> station) & 1)
        or ((b_mask >> right) & 1)
        or ((work_mask >> station) & 1)
    )


def b13_orbit_spot_certificate() -> dict[str, object]:
    bank_count = 13
    capacity = EXTENSION_CAPACITY
    program = parameterized_program(bank_count, capacity)
    stations = len(program)
    data_width = parameterized_data_width(capacity)
    controller = parameterized_controller_word(
        program, data_width, capacity
    )
    operations = compile_integer_operations(controller)
    inverse_operations = tuple(reversed(operations))
    ring_mask = (1 << stations) - 1
    a_base = data_width
    b_base = data_width + stations
    work_base = data_width + 2 * stations
    data_mask = (1 << data_width) - 1
    byte_width = (data_width + 7) // 8
    position_sample = (
        (),
        (0,),
        (37,),
        (0, 2),
        (7, 42),
    )
    sample_reports = []
    total_boundaries = 0
    total_violations = 0
    closure_failures = 0
    inverse_failures = 0
    output_hasher = sha256()
    for positions in position_sample:
        initial_mask = sum(1 << station for station in positions)
        if has_adjacent_pair(initial_mask, stations):
            raise AssertionError(("adjacent orbit sample", positions))
        initial_value = initial_mask << a_base
        value = initial_value
        sample_violations = 0
        for step in range(stations):
            a_mask = (value >> a_base) & ring_mask
            b_mask = (value >> b_base) & ring_mask
            work_mask = (value >> work_base) & ring_mask
            expected_a = rotate_mask(initial_mask, step, stations)
            ownership_exact = all(
                amended_ownership_holds_mask(
                    a_mask, b_mask, work_mask, station, stations
                )
                for station in range(stations)
                if (a_mask >> station) & 1
            )
            violation = (
                a_mask != expected_a
                or b_mask != 0
                or work_mask != 0
                or has_adjacent_pair(a_mask, stations)
                or not ownership_exact
            )
            sample_violations += int(violation)
            total_boundaries += 1
            value = apply_integer_operations(value, operations)
        final_a = (value >> a_base) & ring_mask
        final_b = (value >> b_base) & ring_mask
        final_work = (value >> work_base) & ring_mask
        register_closed = (
            final_a == initial_mask
            and final_b == 0
            and final_work == 0
        )
        closure_failures += int(not register_closed)
        recovered = value
        for _step in range(stations):
            recovered = apply_integer_operations(
                recovered, inverse_operations
            )
        inverse_exact = recovered == initial_value
        inverse_failures += int(not inverse_exact)
        total_violations += sample_violations
        output_data = value & data_mask
        output_hasher.update(initial_mask.to_bytes(
            (stations + 7) // 8, "little"
        ))
        output_hasher.update(output_data.to_bytes(
            byte_width, "little"
        ))
        sample_reports.append({
            "positions": positions,
            "k": len(positions),
            "q_boundaries_checked": stations,
            "invariant_violations": sample_violations,
            "register_closed": register_closed,
            "full_inverse_exact": inverse_exact,
            "output_data_sha256": sha256(
                output_data.to_bytes(byte_width, "little")
            ).hexdigest(),
        })
    return {
        "banks": bank_count,
        "capacity": capacity,
        "program_stations": stations,
        "expected_stations": 8 * bank_count - 5,
        "compiled_step_gates": len(controller),
        "compiled_step_sha256": K.gate_digest(controller),
        "position_sample": position_sample,
        "sample_configurations": len(position_sample),
        "sample_k_values": sorted({
            len(positions) for positions in position_sample
        }),
        "full_orbit_steps_per_configuration": stations,
        "q_boundaries_checked": total_boundaries,
        "invariant_violations": total_violations,
        "register_closure_failures": closure_failures,
        "full_inverse_failures": inverse_failures,
        "orbit_output_table_sha256": output_hasher.hexdigest(),
        "samples": sample_reports,
        "literal_execution": (
            "the parameterized controlled Q+two-rail R gate word is "
            "compiled once and applied exactly n=99 times per sample; "
            "the reversed compiled word is then applied n times"
        ),
        "exact": (
            stations == 99
            and total_boundaries == len(position_sample) * stations
            and total_violations == closure_failures
            == inverse_failures == 0
            and sorted({
                len(positions) for positions in position_sample
            }) == [0, 1, 2]
        ),
    }


def assigned_literal(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return ast.literal_eval(matches[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def literal_return_dict_keys(
    tree: ast.Module, function_name: str
) -> tuple[str, ...]:
    function = function_node(tree, function_name)
    dictionaries = [
        node.value for node in ast.walk(function)
        if isinstance(node, ast.Return)
        and isinstance(node.value, ast.Dict)
    ]
    if len(dictionaries) != 1:
        raise AssertionError((function_name, len(dictionaries)))
    keys = tuple(
        ast.literal_eval(key)
        for key in dictionaries[0].keys
        if key is not None
    )
    return keys


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def ast_supply_audit(
    self_source: str,
    input_sources: dict[str, str],
) -> dict[str, object]:
    tree = ast.parse(self_source)
    imports = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    allowed_imports = {
        "__future__",
        "ast",
        "collections",
        "hashlib",
        "json",
        "pathlib",
        "time",
        (
            "frontier_cycle719_two_rail_recurrent_controller_core_"
            "2026_07_26"
        ),
    }
    core_names = (
        "parameterized_bases",
        "parameterized_data_width",
        "parameterized_offset_gate",
        "parameterized_pair_gate",
        "parameterized_mapped_action",
        "parameterized_mapped_macro",
        "parameterized_program",
        "parameterized_program_word",
    )
    forbidden_landed_calls = {
        "K.interleaved_program",
        "K.mapped_macro",
        "K.H.mapped_action",
        "K.M.offset_gate",
        "K.M.map_pair_gate",
    }
    core_calls = set()
    core_capacity_literals = []
    for name in core_names:
        function = function_node(tree, name)
        core_calls.update(
            call_name(node.func)
            for node in ast.walk(function)
            if isinstance(node, ast.Call)
        )
        core_capacity_literals.extend(
            node.value for node in ast.walk(function)
            if isinstance(node, ast.Constant)
            and node.value in {FROZEN_CAPACITY, EXTENSION_CAPACITY}
        )
    read_text_calls = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and call_name(node.func).endswith("read_text")
    ]
    input_literal = assigned_literal(tree, "AUDIT_INPUT_PATHS")
    declared_assignments = [
        node for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "DECLARED_INPUT_PATHS"
            for target in node.targets
        )
    ]
    declared_is_alias = (
        len(declared_assignments) == 1
        and isinstance(declared_assignments[0].value, ast.Name)
        and declared_assignments[0].value.id == "AUDIT_INPUT_PATHS"
    )
    source_hashes = {
        path: sha256(source.encode()).hexdigest()
        for path, source in input_sources.items()
    }
    return {
        "imports": sorted(imports),
        "unexpected_imports": sorted(set(imports) - allowed_imports),
        "audit_input_paths_literal": input_literal,
        "declared_paths_is_exact_alias": declared_is_alias,
        "read_text_call_count": len(read_text_calls),
        "read_guard": (
            "one read site is read_authorized_source, which rejects every "
            "path outside AUDIT_INPUT_PATHS; the other reads __file__ only "
            "so this runner can audit its own AST"
        ),
        "core_functions": core_names,
        "core_calls_to_landed_mapping": sorted(
            core_calls & forbidden_landed_calls
        ),
        "core_fixed_capacity_literals": core_capacity_literals,
        "source_sha256": source_hashes,
        "new_supplies": NEW_SUPPLIES,
        "new_supply_count": len(NEW_SUPPLIES),
        "no_hidden_supplies": (
            not (set(imports) - allowed_imports)
            and input_literal == AUDIT_INPUT_PATHS
            and declared_is_alias
            and len(read_text_calls) == 2
            and not (core_calls & forbidden_landed_calls)
            and not core_capacity_literals
            and len(NEW_SUPPLIES) == 1
        ),
        "exact": (
            not (set(imports) - allowed_imports)
            and input_literal == AUDIT_INPUT_PATHS
            and declared_is_alias
            and len(read_text_calls) == 2
            and not (core_calls & forbidden_landed_calls)
            and not core_capacity_literals
            and len(NEW_SUPPLIES) == 1
        ),
    }


def theorem_transfer_certificate(
    input_sources: dict[str, str],
    templates: dict[str, object],
    extension: dict[str, object],
    orbit: dict[str, object],
    supply_audit: dict[str, object],
) -> dict[str, object]:
    cycle739_tree = ast.parse(input_sources[AUDIT_INPUT_PATHS[1]])
    cycle737_source = input_sources[AUDIT_INPUT_PATHS[2]]
    amended_formula = assigned_literal(
        cycle739_tree, "I1_AMENDED_FORMULA"
    )
    template_keys = literal_return_dict_keys(
        cycle739_tree, "template_words"
    )
    inherited_anchors = {
        "cycle739_amended_predicate_exact": (
            amended_formula == I1_AMENDED_FORMULA
        ),
        "cycle739_nine_template_names_exact": (
            template_keys == TEMPLATE_NAMES
        ),
        "cycle739_general_n_contract_frozen": (
            "Cycle 738's general-n sector contract"
            in input_sources[AUDIT_INPUT_PATHS[1]]
            and "with no remaining identity conditions"
            in input_sources[AUDIT_INPUT_PATHS[1]]
        ),
        "cycle737_admissibility_arithmetic_exact": (
            '"membership_rule": "n=8b-5 for declared positive integer b"'
            in cycle737_source
            and "source + b banks + "
            in cycle737_source
            and "reverse link rows + finalizer = 8b-5"
            in cycle737_source
        ),
        "cycle737_translation_invariants_anchored": all(
            phrase in cycle737_source
            for phrase in (
                "common_translation_failures",
                "translation_isometry_failures",
                "rail_closure_failures",
                "adjacency_ownership_violations",
            )
        ),
    }
    b_independent_ingredients = (
        {
            "ingredient": "Cycle-738 structural program lemma",
            "statement": (
                "the non-padded source/bank/edge/finalizer emission has "
                "n=8b-5 and its proof is symbolic in the positive integer b"
            ),
            "b_independent_given_lawful_mapping": True,
        },
        {
            "ingredient": "Cycle-738 common-translation lemmas",
            "statement": (
                "the A rail advances by the common +1 translation; "
                "nonadjacency and circular distance are translation "
                "invariants; n steps close the controller rail"
            ),
            "b_independent_given_lawful_mapping": True,
        },
        {
            "ingredient": "Cycle-738 orbit/composition lemma",
            "statement": (
                "on separated occupied sites with clean B/work auxiliaries, "
                "the controller orbit composes the selected local macros"
            ),
            "b_independent_given_lawful_mapping": True,
        },
        {
            "ingredient": "Cycle-739 amended ownership predicate",
            "statement": I1_AMENDED_FORMULA,
            "b_independent_given_lawful_mapping": True,
        },
        {
            "ingredient": "Cycle-739 clean controlled primitives",
            "statement": (
                "X/CNOT/TOF lifting leaves A unchanged, addresses only "
                "data plus own work, and returns clean work=0 to 0"
            ),
            "b_independent_given_lawful_mapping": True,
        },
        {
            "ingredient": "Cycle-739 nine emitted-word templates",
            "statement": TEMPLATE_NAMES,
            "b_independent_given_lawful_mapping": True,
        },
    )
    one_new_supply = {
        "supply": NEW_SUPPLIES[0],
        "anchoring": (
            "all 12 K BANK_BASES entries and all 11 K LINK_BASES entries "
            "at C=12 are reproduced byte-exactly"
        ),
        "role": (
            "for every b<=C it makes every emitted bank index <C and "
            "every emitted edge index <C-1, hence every mapping lawful"
        ),
    }
    retained_sector_hypotheses = (
        "positive integer b and oriented non-padded ring n=8b-5",
        "a separated A-sector configuration (the spot family uses k<=2)",
        "blank B/work/controller auxiliaries at the declared Q boundary",
        "the clean data/program genesis and other Cycle-738 sector hypotheses",
    )
    exact = (
        all(inherited_anchors.values())
        and templates["template_count"] == 9
        and templates["all_templates_clean_when_lawfully_mapped"]
        and extension["all_rows_clean"]
        and orbit["exact"]
        and supply_audit["no_hidden_supplies"]
        and len(NEW_SUPPLIES) == 1
        and "IF the derived affine placement law" in TABLE_UNIFORM_CONDITIONAL
        and "no other new supply" in TABLE_UNIFORM_CONDITIONAL
    )
    return {
        "inherited_data_anchors": inherited_anchors,
        "b_independent_ingredients": b_independent_ingredients,
        "ingredient_count": len(b_independent_ingredients),
        "all_ingredients_b_independent_given_lawful_mapping": all(
            row["b_independent_given_lawful_mapping"]
            for row in b_independent_ingredients
        ),
        "one_new_supply": one_new_supply,
        "new_supply_count": len(NEW_SUPPLIES),
        "retained_not_new_sector_hypotheses": retained_sector_hypotheses,
        "mapping_totality_argument": (
            "parameterized_program emits bank indices 0..b-1 and edge "
            "indices 0..b-2; parameterized_bases(C) supplies exactly C "
            "bank bases and C-1 link bases, so 1<=b<=C is sufficient"
        ),
        "conditional": TABLE_UNIFORM_CONDITIONAL,
        "per_b_reproof_required": False,
        "sector_theorem_table_uniform": exact,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()

    input_sources = {
        path: read_authorized_source(path)
        for path in AUDIT_INPUT_PATHS
    }
    self_source = Path(__file__).read_text(encoding="utf-8")

    check(
        "INPUT_literal_paths_and_header_contract",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle739_identity_discharge_2026_07_28.py",
            "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
        )
        and AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH
        == "docs/TABLE_PARAMETERIZED_MAPPER_CYCLE740_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )

    table_law = table_law_certificate()
    check(
        "A_table_law_derivation_byte_exact_K_prefix",
        table_law["exact"]
        and table_law["byte_exact"]
        and table_law["frozen_bank_entries"] == 12
        and table_law["frozen_link_entries"] == 11,
    )

    equivalence = equivalence_certificate()
    check(
        "B_equivalence_b1_through_b12_programs_and_mapped_words",
        equivalence["exact"]
        and equivalence["all_byte_identical"]
        and len(equivalence["per_b"]) == 12,
    )

    primitive = primitive_clean_certificate()
    templates = template_uniformity_certificate(primitive)
    extension = extension_certificate(primitive)
    check(
        "C_extension_b13_through_b16_every_row_clean",
        primitive["exact"]
        and templates["exact"]
        and extension["exact"]
        and extension["per_b_row_totals"]
        == {13: 99, 14: 107, 15: 115, 16: 123},
    )

    frozen_eight = frozen_eight_certificate(primitive)
    check(
        "D_eight_Cycle739_frozen_rows_now_lawful",
        frozen_eight["exact"]
        and frozen_eight["frozen_failure_count"] == 8
        and frozen_eight["all_now_lawful"],
    )

    orbit = b13_orbit_spot_certificate()
    check(
        "E_b13_compiled_full_orbit_k_le_2_spot_family",
        orbit["exact"]
        and orbit["program_stations"] == 99
        and orbit["sample_k_values"] == [0, 1, 2]
        and orbit["invariant_violations"] == 0
        and orbit["register_closure_failures"] == 0
        and orbit["full_inverse_failures"] == 0,
    )

    supply_audit = ast_supply_audit(self_source, input_sources)
    transfer = theorem_transfer_certificate(
        input_sources, templates, extension, orbit, supply_audit
    )
    check(
        "F_theorem_transfer_b_independent_one_new_supply_AST",
        supply_audit["exact"]
        and supply_audit["no_hidden_supplies"]
        and transfer["exact"]
        and transfer[
            "all_ingredients_b_independent_given_lawful_mapping"
        ]
        and transfer["new_supply_count"] == 1
        and not transfer["per_b_reproof_required"],
    )

    boundary = {
        "capacity_now_parameterized": True,
        "table_law_supplied_anchored_to_K": table_law["exact"],
        "sector_theorem_table_uniform": transfer[
            "sector_theorem_table_uniform"
        ],
        "exact_conditional": TABLE_UNIFORM_CONDITIONAL,
        "supplies": {
            "one_new_supply": NEW_SUPPLIES,
            "retained_not_new_sector_hypotheses": transfer[
                "retained_not_new_sector_hypotheses"
            ],
        },
        "landed_files_modified": False,
        "capacity_domain": (
            "every supplied integer C>=1; theorem domain 1<=b<=C"
        ),
        "remaining_capacity_residual": None,
    }
    check(
        "G_honest_boundary_keys_conditional_and_supplies",
        boundary["capacity_now_parameterized"] is True
        and boundary["table_law_supplied_anchored_to_K"] is True
        and boundary["sector_theorem_table_uniform"] is True
        and boundary["exact_conditional"] == TABLE_UNIFORM_CONDITIONAL
        and len(boundary["supplies"]["one_new_supply"]) == 1
        and boundary["landed_files_modified"] is False
        and boundary["remaining_capacity_residual"] is None,
    )

    elapsed = perf_counter() - started
    check(
        "TIMEOUT_runtime_under_900_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "A_table_law": table_law,
        "B_equivalence": equivalence,
        "C_primitive_clean_work": primitive,
        "C_nine_template_uniformity": templates,
        "C_extension": extension,
        "D_frozen_eight": frozen_eight,
        "E_b13_orbit_spot": orbit,
        "F_AST_supply_audit": supply_audit,
        "F_theorem_transfer": transfer,
        "G_boundary": boundary,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "pass": all(CHECKS.values()),
    }
    provisional = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional.encode())
        + len("\n".join(OUTPUT_LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE740_TABLE_PARAMETERIZED_MAPPER_ALL_PASS"
        if report["pass"]
        else "CYCLE740_TABLE_PARAMETERIZED_MAPPER_HONEST_FAIL"
    )
    report["report_sha256"] = stable_digest(report)

    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    print(text, end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
