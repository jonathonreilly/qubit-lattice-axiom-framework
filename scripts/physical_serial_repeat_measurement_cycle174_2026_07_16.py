#!/usr/bin/env python3
"""Cycle 174: exact interface result for serial repeat measurement.

Positive result:
    one generic two-opposite-row ingress schema covers all 32 signed rows,
    closes to 96 proper-cubic raw rows, and merges deterministically with the
    Cycle-169 unified law.

Bounded obstruction:
    that bare ingress does not compose directly with the *stock* Cycle-166
    measured-row two-port reader.  Its lower FRAME/MARK line is a load-bearing
    guard for four physical fork paths.  Protecting the line for a second row
    witness leaves forty cable segments without a legal local guide choice.

This is not a serial-composition no-go and not axiom evidence.  Exterior row
decoders/fanout remain a concrete compiler route (Cycle 176).
"""

from __future__ import annotations

from pathlib import Path

import physical_row_native_signed_membership_cycle169_2026_07_16 as c169
import record_defined_causal_depth_clock_cycle170_2026_07_16 as clock


p = c169.joint
c53 = p.c53
cell = p.cell
cable = p.cable
bound = p.control.bound
twoport = bound.twoport
Coord = tuple[int, int, int]

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_SERIAL_REPEAT_MEASUREMENT_CYCLE174_NOTE_2026-07-16.md"
)

ORIGIN: Coord = (0, 0, 0)
EX: Coord = (1, 0, 0)
NEG_EX: Coord = (-1, 0, 0)
EZ: Coord = (0, 0, 1)
NEG_EZ: Coord = (0, 0, -1)
ROWS = tuple(p.mux.ROW_ROLES)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def ingress_signature(row_role: str):
    return c53.canonical_signature(
        c53.local_signature({EZ: row_role, NEG_EZ: row_role}, ORIGIN)
    )


INGRESS_TABLE = {
    ingress_signature(row_role): row_role
    for row_role in ROWS
}
INGRESS_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in INGRESS_TABLE.items()
))
MERGED_RAW = cell.merge_raw(c169.UNIFIED_RAW, INGRESS_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def orthogonal_signature(row_role: str):
    return c53.canonical_signature(
        c53.local_signature({EZ: row_role, EX: row_role}, ORIGIN)
    )


ORTHOGONAL_TABLE = {
    orthogonal_signature(row_role): row_role
    for row_role in ROWS
}
ORTHOGONAL_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in ORTHOGONAL_TABLE.items()
))
ORTHOGONAL_MERGED = cell.merge_raw(c169.UNIFIED_RAW, ORTHOGONAL_RAW)
ORTHOGONAL_CONFLICTS = {
    signature: outputs
    for signature, outputs in ORTHOGONAL_MERGED.items()
    if len(outputs) != 1
}


def marked_opposite_signature(row_role: str):
    return c53.canonical_signature(
        c53.local_signature(
            {
                EX: row_role,
                NEG_EX: row_role,
                NEG_EZ: p.pivot.ROUTER_MARKER,
            },
            ORIGIN,
        )
    )


MARKED_OPPOSITE_TABLE = {
    marked_opposite_signature(row_role): row_role
    for row_role in ROWS
}
MARKED_OPPOSITE_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in MARKED_OPPOSITE_TABLE.items()
))
MARKED_OPPOSITE_MERGED = cell.merge_raw(
    c169.UNIFIED_RAW,
    MARKED_OPPOSITE_RAW,
)
MARKED_OPPOSITE_CONFLICTS = {
    signature: outputs
    for signature, outputs in MARKED_OPPOSITE_MERGED.items()
    if len(outputs) != 1
}


def role_set(raw):
    return {
        role
        for outputs in raw.values()
        for role in outputs
    }


def stock_lower_guard_certificate() -> tuple[int, tuple[object, ...]]:
    """Return the four lower fork segments and their common center guard."""

    rows = p.CASE_REPRESENTATIVES[(0, 0)]
    measured = rows[2]
    items = bound.path_items(rows[0], rows[1], measured)
    lower_paths = {
        bound.MEASURED_PATHS[(1, term_index)]
        for term_index in range(4)
    }
    certificates = []
    for _value, path in items:
        if path not in lower_paths:
            continue
        target = path[1]
        previous = path[0]
        future = path[2]
        _kind, records = cable.segment_records(
            target,
            previous,
            future,
            twoport.bit(0),
        )
        common_guards = tuple(
            site
            for site in records
            if site[0] == bound.MEASURED_CENTER[0]
            and site[1] == bound.MEASURED_CENTER[1]
        )
        common_guard = common_guards[0] if len(common_guards) == 1 else None
        certificates.append((
            path[0],
            target,
            common_guard,
            records.get(common_guard) if common_guard is not None else None,
        ))
    return len(certificates), tuple(certificates)


def protected_lower_recompile_failure() -> tuple[str, int, tuple[object, ...]]:
    """Attempt the direct stock-interface recompile and preserve its failure."""

    zero = (0, 0, 0, 0, 0)
    fixed = bound.component_records(zero, zero, zero)
    fixed.pop(add(bound.MEASURED_CENTER, NEG_EZ), None)
    expected, _dependencies, _results = bound.base_expected(zero, zero, zero)
    items = bound.path_items(zero, zero, zero)
    final_ports = {
        add(bound.spacious.FINAL_PORT, shift)
        for shift in bound.COMM_SHIFTS
    }
    lower_corridor = {
        add(bound.MEASURED_CENTER, (0, 0, offset))
        for offset in range(-400, 0)
    }
    try:
        bound.sequential_routing_scaffold(
            items,
            fixed,
            frozenset(set(expected) | final_ports | lower_corridor),
        )
    except ValueError as error:
        payload = error.args[0]
        if (
            isinstance(payload, tuple)
            and payload
            and payload[0] == "no-guide-option-against-fixed-records"
        ):
            rows = payload[1]
            return payload[0], len(rows), tuple(rows)
        return "other-value-error", 0, (payload,)
    return "unexpected-success", 0, ()


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


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("POSITIVE TWO-WITNESS LAW")
    check(
        "one generic schema covers all 32 signed rows",
        len(ROWS) == len(INGRESS_TABLE) == 32,
        len(INGRESS_TABLE),
    )
    check(
        "proper-cubic closure is exactly 96 raw rows",
        len(INGRESS_RAW) == 96
        and {
            len(cell.raw_orbit(signature, output))
            for signature, output in INGRESS_TABLE.items()
        }
        == {3},
        len(INGRESS_RAW),
    )
    check(
        "the 96 ingress rows are disjoint from and deterministic with Cycle 169",
        not (set(INGRESS_RAW) & set(c169.UNIFIED_RAW))
        and len(MERGED_RAW) == 101_804
        and not RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in MERGED_RAW.values()),
        {
            "base": len(c169.UNIFIED_RAW),
            "ingress": len(INGRESS_RAW),
            "merged": len(MERGED_RAW),
            "conflicts": len(RAW_CONFLICTS),
        },
    )
    check(
        "the ingress schema adds no onsite role",
        role_set(INGRESS_RAW) <= role_set(c169.UNIFIED_RAW),
        role_set(INGRESS_RAW) - role_set(c169.UNIFIED_RAW),
    )

    print("\nSTOCK P TWO-PORT INTERFACE")
    interface = twoport.interface_source((0, 0, 0, 0, 0))
    check(
        "the stock measured-row interface fixes the lower source face",
        interface.get(NEG_EZ) == p.FRAME
        and twoport.DOWN == NEG_EZ
        and len(twoport.LOWER_PORTS) == 4,
        {
            "lower_role": interface.get(NEG_EZ),
            "lower_ports": twoport.LOWER_PORTS,
        },
    )
    guard_count, guard_certificate = stock_lower_guard_certificate()
    check(
        "all four lower fork departures consume that face as a local guard",
        guard_count == 4
        and all(item[2] is not None and item[3] is not None for item in guard_certificate),
        guard_certificate,
    )
    failure_kind, empty_domains, failure_rows = protected_lower_recompile_failure()
    check(
        "protecting the lower line for a row witness empties forty cable domains",
        failure_kind == "no-guide-option-against-fixed-records"
        and empty_domains == 40,
        {
            "kind": failure_kind,
            "empty_domains": empty_domains,
            "sample": failure_rows[:2],
        },
    )

    print("\nALTERNATIVE INTERFACES")
    check(
        "the unguarded orthogonal-pair shortcut is not a deterministic merge",
        len(ORTHOGONAL_RAW) == 384
        and len(set(ORTHOGONAL_RAW) & set(c169.UNIFIED_RAW)) == 12
        and len(ORTHOGONAL_CONFLICTS) == 12,
        {
            "raw": len(ORTHOGONAL_RAW),
            "overlap": len(set(ORTHOGONAL_RAW) & set(c169.UNIFIED_RAW)),
            "conflicts": len(ORTHOGONAL_CONFLICTS),
        },
    )
    check(
        "a marked opposite-pair compiler interface remains a clean live route",
        len(MARKED_OPPOSITE_RAW) == 384
        and not (set(MARKED_OPPOSITE_RAW) & set(c169.UNIFIED_RAW))
        and not MARKED_OPPOSITE_CONFLICTS,
        {
            "raw": len(MARKED_OPPOSITE_RAW),
            "conflicts": len(MARKED_OPPOSITE_CONFLICTS),
        },
    )

    first_outputs = (
        p.MUX["lane1"]["common"],
        p.MUX["lane2"]["common"],
    )
    second_sources = (
        add(p.SOURCE_CENTERS[0], (0, 2500, 0)),
        add(p.SOURCE_CENTERS[1], (0, 2500, 0)),
    )
    separation_squares = tuple(
        sum((left - right) ** 2 for left, right in zip(output, source))
        for output, source in zip(first_outputs, second_sources, strict=True)
    )
    check(
        "serial composition still requires visible nonzero transport",
        all(value > 0 for value in separation_squares)
        and clock.squared_norm((480, 0, 0)) == 230_400,
        separation_squares,
    )

    print("\nSCOPE AND NO-GO DISCIPLINE")
    note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    for phrase in (
        "partial exact interface result",
        "positive 96-row two-witness ingress",
        "stock p two-port/mark line",
        "not a serial-composition no-go",
        "exterior row-decoder/fanout",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo",
        "status: fail for a broad no-go",
        "no axiom, primitive, registry, policy, or audit edit follows",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "PARTIAL_EXACT_INTERFACE_RESULT" if FAIL == 0 else "FAIL",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
