#!/usr/bin/env python3
"""Cycle 175: replace the signed-row alphabet on the common physical law.

The existing 32-role signed-row codebook has seven labels that are executable
tokens elsewhere in the common onsite namespace.  Cycle 171 found 117 roles
that are individually clean on the recurrent carrier.  This probe keeps the
25 already-clean row labels, injectively replaces the seven aliases with the
seven least-exposed clean non-row labels, removes every retained row-parametric
raw family, and recompiles those families under the one replacement codebook.

The probe has no authority.  It edits no axiom, primitive, registry, policy,
audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import autonomous_signed_row_recurrent_sidecar_cycle171_2026_07_16 as c171
import physical_row_native_signed_membership_cycle169_2026_07_16 as c169


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CLEAN_ROW_ALPHABET_COMPONENT_REPLACEMENT_CYCLE175_NOTE_2026-07-16.md"
)

joint = c169.joint
signed = c169.signed
tap = c169.tap
ported = c169.ported
twoport = tap.twoport
five = joint.pivot.five
row_machine = joint.mult.c150.p.alu.compact
multiply = joint.mult
pivot = joint.pivot
fanout = ported.cable.fanout
row_cable = joint.mux.transport
mux = joint.mux
cell = joint.cell
c53 = joint.c53

Signature = c53.Signature
RawTable = dict[Signature, frozenset[str]]

OLD_ROW_ROLE = dict(five.ROW_ROLE)
OLD_ROLE_ROW = dict(five.ROLE_ROW)
OLD_ROW_ROLES = tuple(OLD_ROW_ROLE.values())

# Keep all 25 rows already certified by Cycle 171.  Replace only the exact
# seven aliases, using the seven lowest-exposure clean non-row roles under the
# Cycle-166 law.  None has a unary inherited firing.
ALIAS_REPLACEMENT = {
    "A_0_1": "PAIR",
    "A_0_2": "Z0",
    "BTG": "Z_A",
    "BTQ": "Z_C",
    "B_0_2": "RING",
    "COMP6": "R_A02",
    "DONE": "R_A00",
}
ROLE_MAP = {
    role: ALIAS_REPLACEMENT.get(role, role)
    for role in OLD_ROW_ROLES
}
NEW_ROW_ROLE = {
    row: ROLE_MAP[role]
    for row, role in OLD_ROW_ROLE.items()
}
NEW_ROLE_ROW = {
    role: row
    for row, role in NEW_ROW_ROLE.items()
}
NEW_ROW_ROLES = tuple(NEW_ROW_ROLE.values())


@dataclass(frozen=True)
class Component:
    name: str
    lane: str
    raw: RawTable


# These are the atomic raw families whose generators iterate over the signed
# row domain or consume a row-role lookup.  The Cycle-169 comparator is
# deliberately absent: it is literal-bit-parametric and needs fixture replay,
# but zero raw-row replacement.
COMPONENTS = (
    Component("cycle149_tableau_row_gate", "tableau", row_machine.ROW_GATE_RAW),
    Component("cycle151_commuting_multiplier", "multiplier", multiply.MULTIPLY_RAW),
    Component("cycle152_pivot_router", "router", pivot.ROUTER_RAW),
    Component("cycle153_row_literal_fanout", "reader", fanout.FANOUT_RAW),
    Component("cycle155_ported_row_reader", "reader", ported.PORTED_RAW),
    Component("cycle158_two_port_row_reader", "reader", twoport.TWO_PORT_RAW),
    Component("cycle162_row_transport", "transport", row_cable.ROW_CABLE_RAW),
    Component("cycle163_mux_gate", "mux", mux.GATE_RAW),
    Component("cycle163_mux_join", "mux", mux.JOIN_RAW),
    Component("cycle163_mux_terminal", "mux", mux.TERMINAL_RAW),
    Component("cycle165_payload_tap", "tap", tap.TAP_RAW),
    Component("cycle166_row_splitter", "update", joint.SPLITTER_RAW),
    Component("cycle166_integrated_gate", "update", joint.INTEGRATED_GATE_RAW),
    Component("cycle167_sign_reader", "sign", signed.SIGN_RAW),
)

CYCLE166_COMPONENTS = tuple(
    component
    for component in COMPONENTS
    if component.name != "cycle167_sign_reader"
)

BASE166_RAW = joint.MERGED_RAW
BASE169_RAW = c169.UNIFIED_RAW

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


def role_references(
    signature: Signature,
    values: frozenset[str],
    roles: set[str],
) -> bool:
    return (
        any(role in roles for _direction, role in signature)
        or any(role in roles for role in values)
    )


def remap_signature(signature: Signature) -> Signature:
    return tuple(
        (direction, ROLE_MAP.get(role, role))
        for direction, role in signature
    )


def remap_raw(raw: RawTable) -> RawTable:
    mapped: dict[Signature, set[str]] = defaultdict(set)
    for signature, values in raw.items():
        mapped[remap_signature(signature)].update(
            ROLE_MAP.get(value, value)
            for value in values
        )
    return {
        signature: frozenset(values)
        for signature, values in mapped.items()
    }


def merge_raw(*tables: RawTable) -> RawTable:
    return cell.merge_raw(*tables)


def component_union(components: tuple[Component, ...]) -> RawTable:
    return merge_raw(*(component.raw for component in components))


def replace_components(
    original: RawTable,
    components: tuple[Component, ...],
) -> tuple[RawTable, dict[str, object]]:
    old_union = component_union(components)
    missing = set(old_union) - set(original)
    remainder = {
        signature: values
        for signature, values in original.items()
        if signature not in old_union
    }
    mapped = tuple(
        (component.name, remap_raw(component.raw))
        for component in components
    )
    mapped_union = merge_raw(*(raw for _name, raw in mapped))
    candidate = merge_raw(
        remainder,
        mapped_union,
    )
    conflicts = {
        signature: values
        for signature, values in candidate.items()
        if len(values) != 1
    }
    changed_roles = set(ALIAS_REPLACEMENT)
    inventory = {
        "component_sum": sum(len(component.raw) for component in components),
        "component_union": len(old_union),
        "component_overlap": (
            sum(len(component.raw) for component in components) - len(old_union)
        ),
        "removed_signatures": len(set(old_union) - set(mapped_union)),
        "added_signatures": len(set(mapped_union) - set(old_union)),
        "changed_at_same_signature": sum(
            old_union[signature] != mapped_union[signature]
            for signature in set(old_union) & set(mapped_union)
        ),
        "unchanged_signatures": sum(
            old_union[signature] == mapped_union[signature]
            for signature in set(old_union) & set(mapped_union)
        ),
        "missing": len(missing),
        "remainder": len(remainder),
        "affected_by_component": {
            component.name: sum(
                role_references(signature, values, changed_roles)
                for signature, values in component.raw.items()
            )
            for component in components
        },
        "mapped_sizes": {
            name: len(raw)
            for name, raw in mapped
        },
        "candidate_size": len(candidate),
        "conflicts": conflicts,
    }
    return candidate, inventory


CANDIDATE166_RAW, INVENTORY166 = replace_components(
    BASE166_RAW,
    CYCLE166_COMPONENTS,
)
CANDIDATE169_RAW, INVENTORY169 = replace_components(
    BASE169_RAW,
    COMPONENTS,
)


def clear_known_caches() -> None:
    # Only resolved apparatus records depend on the row-value codebook.  The
    # structural scaffolds are codebook-independent because their dummy row is
    # the unchanged all-zero role.  Retaining those caches avoids rebuilding
    # the very large Cycle-169 routing cage while still preventing old resolved
    # payload values from leaking into the replacement fixture.
    joint.apparatus.cache_clear()
    c169.apparatus.cache_clear()


@contextmanager
def replacement_codebook():
    old_joint_raw = joint.MERGED_RAW
    old_row_role = dict(five.ROW_ROLE)
    old_role_row = dict(five.ROLE_ROW)
    five.ROW_ROLE.clear()
    five.ROW_ROLE.update(NEW_ROW_ROLE)
    five.ROLE_ROW.clear()
    five.ROLE_ROW.update(NEW_ROLE_ROW)
    joint.MERGED_RAW = CANDIDATE166_RAW
    clear_known_caches()
    try:
        yield
    finally:
        joint.MERGED_RAW = old_joint_raw
        five.ROW_ROLE.clear()
        five.ROW_ROLE.update(old_row_role)
        five.ROLE_ROW.clear()
        five.ROLE_ROW.update(old_role_row)
        clear_known_caches()


def remap_nested(value):
    if isinstance(value, str):
        return ROLE_MAP.get(value, value)
    if isinstance(value, tuple):
        return tuple(remap_nested(item) for item in value)
    if isinstance(value, list):
        return [remap_nested(item) for item in value]
    if isinstance(value, dict):
        return {
            remap_nested(key): remap_nested(item)
            for key, item in value.items()
        }
    if isinstance(value, frozenset):
        return frozenset(remap_nested(item) for item in value)
    if isinstance(value, set):
        return {remap_nested(item) for item in value}
    return value


def membership_hard_fixture():
    return next(
        (g1, g2, measured)
        for g1, g2, measured, should_accept in c169.transcripts()
        if should_accept
        and measured == c169.algebra.multiply_commuting(g1, g2)
        and measured[4] == 1
    )


def mapped_fixture_results():
    joint_rows = tuple(
        joint.CASE_REPRESENTATIVES[case]
        for case in sorted(joint.CASE_REPRESENTATIVES)
    )
    membership_rows = membership_hard_fixture()
    baseline_joint = tuple(
        joint.deterministic_run(*rows)
        for rows in joint_rows
    )
    baseline_membership = (
        c169.deterministic_run(*membership_rows, order="min"),
        c169.deterministic_run(*membership_rows, order="max"),
    )
    with replacement_codebook():
        mapped_joint = tuple(
            joint.deterministic_run(*rows)
            for rows in joint_rows
        )
        mapped_membership = (
            c169.deterministic_run(
                *membership_rows,
                order="min",
                law=CANDIDATE169_RAW,
            ),
            c169.deterministic_run(
                *membership_rows,
                order="max",
                law=CANDIDATE169_RAW,
            ),
        )
    return {
        "joint_rows": joint_rows,
        "membership_rows": membership_rows,
        "baseline_joint": baseline_joint,
        "mapped_joint": mapped_joint,
        "baseline_membership": baseline_membership,
        "mapped_membership": mapped_membership,
    }


def carrier_probe():
    table = c171.canonical_sidecar_table(NEW_ROW_ROLES)
    raw = merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    law = merge_raw(CANDIDATE169_RAW, raw)
    conflicts = {
        signature: values
        for signature, values in law.items()
        if len(values) != 1
    }
    results = {}
    old_full_raw = c171.FULL_RAW
    c171.FULL_RAW = law
    try:
        if not conflicts:
            for row, old_role in OLD_ROW_ROLE.items():
                new_role = NEW_ROW_ROLE[row]
                result = c171.causal_certificate(
                    c171.source(new_role),
                    c171.outputs(new_role),
                    c171.IGNORED,
                )
                results[(row, old_role, new_role)] = result
    finally:
        c171.FULL_RAW = old_full_raw
    return {
        "table": table,
        "raw": raw,
        "law": law,
        "conflicts": conflicts,
        "results": results,
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND CODEBOOK")
    check("Cycle-175 review note exists", NOTE.is_file())
    check(
        "the replacement codebook is injective and keeps exactly 25 labels",
        len(OLD_ROW_ROLES) == 32
        and len(NEW_ROW_ROLES) == 32
        and len(set(NEW_ROW_ROLES)) == 32
        and sum(
            old == new
            for old, new in zip(OLD_ROW_ROLES, NEW_ROW_ROLES, strict=True)
        ) == 25,
        tuple(
            (row, OLD_ROW_ROLE[row], NEW_ROW_ROLE[row])
            for row in OLD_ROW_ROLE
            if OLD_ROW_ROLE[row] != NEW_ROW_ROLE[row]
        ),
    )
    check(
        "all seven replacement labels are Cycle-171 carrier-clean existing roles",
        set(ALIAS_REPLACEMENT.values()) <= set(c171.cell.FULL_ROLES)
        and not set(ALIAS_REPLACEMENT.values()) & set(OLD_ROW_ROLES)
        and set(ALIAS_REPLACEMENT.values()) == {
            "PAIR", "Z0", "Z_A", "Z_C", "RING", "R_A02", "R_A00"
        },
    )

    print("\nCOMPONENT REPLACEMENT INVENTORY")
    affected = INVENTORY169["affected_by_component"]
    for component in COMPONENTS:
        print(
            "COMPONENT",
            component.name,
            component.lane,
            len(component.raw),
            affected[component.name],
        )
    check(
        "fourteen atomic row-parametric families are replaced, not duplicated",
        len(COMPONENTS) == 14
        and INVENTORY166["missing"] == 0
        and INVENTORY169["missing"] == 0
        and all(affected[name] > 0 for name in affected),
        (INVENTORY166, INVENTORY169),
    )
    check(
        "literal membership comparators require fixture replay but no raw rewrite",
        len(c169.COMPARATOR_RAW) == 288
        and not any(
            role_references(signature, values, set(OLD_ROW_ROLES))
            for signature, values in c169.COMPARATOR_RAW.items()
        ),
        len(c169.COMPARATOR_RAW),
    )

    print("\nRAW DETERMINISM GATE")
    check(
        "the replacement Cycle-166 law is deterministic",
        not INVENTORY166["conflicts"],
        (
            len(CANDIDATE166_RAW),
            len(INVENTORY166["conflicts"]),
            tuple(INVENTORY166["conflicts"].items())[:3],
        ),
    )
    check(
        "the replacement Cycle-169 unified law is deterministic",
        not INVENTORY169["conflicts"],
        (
            len(CANDIDATE169_RAW),
            len(INVENTORY169["conflicts"]),
            tuple(INVENTORY169["conflicts"].items())[:3],
        ),
    )

    print("\nHARD FIXTURE REPRODUCTION")
    fixtures = None
    if not INVENTORY166["conflicts"] and not INVENTORY169["conflicts"]:
        fixtures = mapped_fixture_results()
    check(
        "all four Cycle-166 hard cases reproduce under the replacement codebook",
        fixtures is not None
        and all(result[0] for result in fixtures["mapped_joint"])
        and fixtures["mapped_joint"]
        == tuple(remap_nested(result) for result in fixtures["baseline_joint"]),
        None if fixtures is None else (
            fixtures["baseline_joint"],
            fixtures["mapped_joint"],
        ),
    )
    check(
        "the Cycle-169 min/max hard fixture reproduces exactly",
        fixtures is not None
        and all(result[0] for result in fixtures["mapped_membership"])
        and fixtures["mapped_membership"]
        == fixtures["baseline_membership"],
        None if fixtures is None else (
            fixtures["baseline_membership"],
            fixtures["mapped_membership"],
        ),
    )

    print("\nALL-32 RECURRENT CARRIER GATE")
    carrier = None
    if not INVENTORY169["conflicts"]:
        carrier = carrier_probe()
    carrier_failures = {}
    if carrier is not None and not carrier["conflicts"]:
        carrier_failures = {
            key: result
            for key, result in carrier["results"].items()
            if not result["ok"]
        }
    check(
        "the replacement carrier delta is deterministic on the Cycle-169 union",
        carrier is not None and not carrier["conflicts"],
        None if carrier is None else (
            len(carrier["raw"]),
            len(carrier["law"]),
            tuple(carrier["conflicts"].items())[:3],
        ),
    )
    check(
        "all 32 replacement row values close through G1-G3",
        carrier is not None
        and not carrier["conflicts"]
        and len(carrier["results"]) == 32
        and not carrier_failures,
        tuple(carrier_failures.items())[:3],
    )

    print("\nSCOPE")
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check(
        "review note prices the table reset and denies axiom pressure",
        "component replacement" in note
        and "not duplicate semantics" in note
        and "compiler-table reset" in note
        and "No axiom addition follows" in note,
    )

    print("\nACCOUNTING")
    print("OLD_ROW_ROLES", OLD_ROW_ROLES)
    print("NEW_ROW_ROLES", NEW_ROW_ROLES)
    print("ALIAS_REPLACEMENT", ALIAS_REPLACEMENT)
    print("INVENTORY166", INVENTORY166)
    print("INVENTORY169", INVENTORY169)
    if fixtures is not None:
        print("FIXTURE_ROWS", fixtures["joint_rows"], fixtures["membership_rows"])
    if carrier is not None:
        print(
            "CARRIER",
            len(carrier["table"]),
            len(carrier["raw"]),
            len(carrier["law"]),
            len(carrier["results"]),
            len(carrier_failures),
        )
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CLEAN_ROW_ALPHABET_REPLACEMENT"
        if FAIL == 0
        else "CYCLE175_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
