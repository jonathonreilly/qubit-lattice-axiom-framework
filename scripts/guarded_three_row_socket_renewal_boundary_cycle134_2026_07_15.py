#!/usr/bin/env python3
"""Cycle 134: bounded guard/socket renewal boundary after Cycle 131.

The runner exhausts the named one-, two-, and three-row outward socket
families around the exact Cycle-129 terminal.  It includes proper-cubic
coimages, full-source unexpected-target checks, and—critically—wrong-value
conditions at expected targets.  No four-row family is searched.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15 as c124


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "GUARDED_THREE_ROW_SOCKET_RENEWAL_BOUNDARY_CYCLE134_NOTE_2026-07-15.md"

c112 = c124.c112
c105 = c124.c105
c59 = c124.c59
c53 = c124.c53
Coord = c124.Coord
Signature = c124.Signature
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


RAIL = tuple(c105.RAIL_SEQUENCE[:12])
RAIL_OUTPUTS = dict(RAIL)
NEXT_RAIL = c105.RAIL_SEQUENCE[12]
IGNORED = {NEXT_RAIL[0]: frozenset((NEXT_RAIL[1],))}

GROUPS: tuple[tuple[tuple[Coord, ...], str], ...] = (
    (((5, 3, -3),), "OZ"),
    (((4, 3, -3),), "W3"),
    (((4, 2, -3),), "A_0_0"),
    (((3, 2, -3),), "A_1_2"),
    (((4, 3, -4),), "A_2_0"),
    (((4, 2, -4),), "A_3_1"),
    (((3, 2, -4),), "A_3_2"),
    (((2, 2, -4),), "COMPLETE"),
    (((1, 2, -4), (2, 3, -4)), "TY"),
    (((0, 2, -4),), "W4"),
    (((0, 2, -3),), "AUXZ"),
    (((0, 2, -2),), "GU"),
    (((-1, 3, -2),), "R_C01"),
    (((-1, 2, -2),), "JOINT"),
    (((-1, 2, -1),), "T_N0"),
    (((-2, 2, -1),), "Y2"),
)
BRIDGE_OUTPUTS = {
    site: output for sites, output in GROUPS for site in sites
}


def build_bridge():
    records = {**c124.positive_terminal_records(), **RAIL_OUTPUTS}
    table: dict[Signature, str] = {}
    locals_seen: list[Signature] = []
    for declared, output in GROUPS:
        local = c53.local_signature(records, declared[0])
        canonical = c53.canonical_signature(local)
        matches = tuple(sorted(
            site
            for site in c53.open_candidates(records)
            if c53.canonical_signature(c53.local_signature(records, site))
            == canonical
        ))
        if matches != tuple(sorted(declared)):
            raise RuntimeError((declared, matches, local))
        table[canonical] = output
        records.update({site: output for site in matches})
        locals_seen.append(local)
    return table, tuple(locals_seen), records


BRIDGE_TABLE, GROUP_LOCALS, TERMINAL = build_bridge()
BRIDGE_RAW = c59.raw_rule_outputs(BRIDGE_TABLE)
BASE_UNION = c112.merge_raw(c124.FULL_RAW, BRIDGE_RAW)
BASE_OUTPUTS = {
    **c124.GROWN_OUTPUTS,
    **RAIL_OUTPUTS,
    **BRIDGE_OUTPUTS,
}

CONTACT = (-2, 2, -1)
LAUNCH_CANONICAL = c53.canonical_signature(GROUP_LOCALS[0])
NEXT_CANONICAL = c53.canonical_signature(GROUP_LOCALS[1])
LAUNCH_ROLES = ("H1", "R_B01")
ANCHORS = frozenset(("Y2", "T_N0", "B_0_2"))


def add(a: Coord, b: Coord) -> Coord:
    return tuple(x + y for x, y in zip(a, b, strict=True))  # type: ignore[return-value]


def sub(a: Coord, b: Coord) -> Coord:
    return tuple(x - y for x, y in zip(a, b, strict=True))  # type: ignore[return-value]


def distance(site: Coord) -> int:
    return sum(abs(value) for value in sub(site, CONTACT))


def dot(a: Coord, b: Coord) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def add_row(records, union, target: Coord, output: str):
    local = c53.local_signature(records, target)
    if not local:
        return None
    canonical = c53.canonical_signature(local)
    raw = c59.raw_rule_outputs({canonical: output})
    merged = c112.merge_raw(union, raw)
    if any(len(values) != 1 for values in merged.values()):
        return None
    matches = tuple(sorted(
        site
        for site in c53.open_candidates(records)
        if c53.local_signature(records, site) in raw
    ))
    if target not in matches:
        return None
    future = dict(records)
    future.update({site: output for site in matches})
    return future, merged, canonical, local, matches, raw


def launch_matches(records) -> tuple[Coord, ...]:
    return tuple(sorted(
        site
        for site in c53.open_candidates(records)
        if c53.canonical_signature(c53.local_signature(records, site))
        == LAUNCH_CANONICAL
    ))


def wrong_value_conditions(compiled, outputs):
    return tuple(sorted(
        (
            target,
            tuple(sorted({
                tuple(sorted(values))
                for _present, _mask, values in conditions
                if values != frozenset((outputs[target],))
            })),
        )
        for target, conditions in compiled.conditions.items()
        if target in outputs
        and any(
            values != frozenset((outputs[target],))
            for _present, _mask, values in conditions
        )
    ))


def one_two_socket_census():
    first_targets = tuple(sorted(
        site
        for site in c53.open_candidates(TERMINAL)
        if distance(site) <= 3
        and any(
            value in ANCHORS
            for _direction, value in c53.local_signature(TERMINAL, site)
        )
    ))
    one = []
    two = []
    seen_first = set()
    for first_target in first_targets:
        for first_output in LAUNCH_ROLES:
            first = add_row(TERMINAL, BASE_UNION, first_target, first_output)
            if first is None:
                continue
            records1, union1, canonical1, local1, matches1, _raw1 = first
            key1 = (canonical1, first_output)
            if key1 in seen_first:
                continue
            seen_first.add(key1)
            launches1 = launch_matches(records1)
            if launches1:
                one.append((first_target, first_output, matches1, launches1))
            second_targets = tuple(sorted(
                site
                for site in c53.open_candidates(records1)
                if distance(site) <= 4
                and any(
                    value in ANCHORS or value == first_output
                    for _direction, value in c53.local_signature(records1, site)
                )
            ))
            seen_second = set()
            for second_target in second_targets:
                for second_output in LAUNCH_ROLES:
                    second = add_row(
                        records1, union1, second_target, second_output
                    )
                    if second is None:
                        continue
                    records2, union2, canonical2, local2, matches2, _raw2 = second
                    key2 = (canonical2, second_output)
                    if key2 in seen_second or key2 == key1:
                        continue
                    seen_second.add(key2)
                    launches2 = launch_matches(records2)
                    if launches2:
                        two.append((
                            (first_target, first_output, matches1),
                            (second_target, second_output, matches2),
                            launches2,
                            union2,
                        ))
    compiler_clean = []
    unexpected_census = []
    for first, second, launches, union in two:
        adapter = {site: first[1] for site in first[2]}
        adapter.update({site: second[1] for site in second[2]})
        oz = {site: "OZ" for site in launches}
        outputs = {**BASE_OUTPUTS, **adapter, **oz}
        compiled = c112.compile_conditions(c112.SOURCE, outputs, union, IGNORED)
        wrong = wrong_value_conditions(compiled, outputs)
        unexpected_census.append(tuple(sorted(compiled.unexpected_targets)))
        if not compiled.unexpected_targets and not wrong:
            compiler_clean.append((first, second, launches))
    return tuple(one), tuple(two), tuple(compiler_clean), tuple(unexpected_census)


def terminal_side_guard_candidates():
    guard_target = (-3, 2, 0)
    outward_target = (-3, 2, -1)
    side_target = (-2, 1, -1)
    candidates = []
    for guard_output in sorted(c105.c89.FULL_ROLES):
        if guard_output in LAUNCH_ROLES:
            continue
        guard = add_row(TERMINAL, BASE_UNION, guard_target, guard_output)
        if guard is None:
            continue
        records1, union1, canonical1, local1, matches1, raw1 = guard
        for outward_output, side_output in (
            ("H1", "R_B01"),
            ("R_B01", "H1"),
        ):
            outward = add_row(
                records1, union1, outward_target, outward_output
            )
            if outward is None:
                continue
            records2, union2, canonical2, local2, matches2, raw2 = outward
            side = add_row(records2, union2, side_target, side_output)
            if side is None:
                continue
            records3, union3, canonical3, local3, matches3, raw3 = side
            launches = launch_matches(records3)
            if not launches:
                continue
            adapter = {site: guard_output for site in matches1}
            adapter.update({site: outward_output for site in matches2})
            adapter.update({site: side_output for site in matches3})
            oz = {site: "OZ" for site in launches}
            outputs = {**BASE_OUTPUTS, **adapter, **oz}
            compiled = c112.compile_conditions(
                c112.SOURCE, outputs, union3, IGNORED
            )
            candidates.append({
                "guard_output": guard_output,
                "outward_output": outward_output,
                "side_output": side_output,
                "union": union3,
                "guard_raw": raw1,
                "adapter": adapter,
                "oz": oz,
                "unexpected": tuple(sorted(compiled.unexpected_targets)),
                "wrong": wrong_value_conditions(compiled, outputs),
                "raw_delta": len(set(union3) - set(BASE_UNION)),
            })
    return tuple(candidates)


def centered_three_row_census():
    terminal_roles = frozenset(TERMINAL.values())
    fresh_roles = tuple(sorted(c105.c89.FULL_ROLES - terminal_roles))
    centers = tuple(sorted(
        site
        for site in c53.open_candidates(TERMINAL)
        if distance(site) <= 3
        and len(c53.local_signature(TERMINAL, site)) >= 2
        and any(
            value == "Y2"
            for _direction, value in c53.local_signature(TERMINAL, site)
        )
    ))
    census = defaultdict(int)
    census["centers"] = len(centers)
    census["fresh_roles"] = len(fresh_roles)
    survivors = []
    for center in centers:
        for guard_role in fresh_roles:
            census["guard_attempts"] += 1
            guard = add_row(TERMINAL, BASE_UNION, center, guard_role)
            if guard is None:
                continue
            census["guard_rows"] += 1
            records1, union1, _canonical1, _local1, matches1, _raw1 = guard
            if matches1 != (center,):
                continue
            census["singleton_guards"] += 1
            for d1 in c53.DIRECTIONS:
                for d2 in c53.DIRECTIONS:
                    if d1 >= d2 or dot(d1, d2) != 0:
                        continue
                    census["direction_pairs"] += 1
                    arm1_target = add(center, d1)
                    arm2_target = add(center, d2)
                    launch_target = add(add(center, d1), d2)
                    if any(
                        site in records1
                        for site in (arm1_target, arm2_target, launch_target)
                    ):
                        continue
                    census["open_geometries"] += 1
                    for arm1_output, arm2_output in (
                        ("H1", "R_B01"),
                        ("R_B01", "H1"),
                    ):
                        census["role_assignments"] += 1
                        arm1 = add_row(
                            records1, union1, arm1_target, arm1_output
                        )
                        if arm1 is None:
                            continue
                        census["arm1_rows"] += 1
                        records2, union2, _c2, _l2, matches2, _r2 = arm1
                        arm2 = add_row(
                            records2, union2, arm2_target, arm2_output
                        )
                        if arm2 is None:
                            continue
                        census["arm2_rows"] += 1
                        records3, union3, _c3, _l3, matches3, _r3 = arm2
                        launches = launch_matches(records3)
                        if launch_target not in launches:
                            continue
                        census["socket_geometries"] += 1
                        adapter = {site: guard_role for site in matches1}
                        adapter.update({site: arm1_output for site in matches2})
                        adapter.update({site: arm2_output for site in matches3})
                        oz = {site: "OZ" for site in launches}
                        factor_outputs = {**adapter, **oz}
                        full_outputs = {**BASE_OUTPUTS, **factor_outputs}
                        factor_compiled = c112.compile_conditions(
                            TERMINAL, factor_outputs, union3, IGNORED
                        )
                        full_compiled = c112.compile_conditions(
                            c112.SOURCE, full_outputs, union3, IGNORED
                        )
                        factor_wrong = wrong_value_conditions(
                            factor_compiled, factor_outputs
                        )
                        full_wrong = wrong_value_conditions(
                            full_compiled, full_outputs
                        )
                        if factor_compiled.unexpected_targets:
                            census["factor_unexpected"] += 1
                        if full_compiled.unexpected_targets:
                            census["full_unexpected"] += 1
                        if factor_wrong:
                            census["factor_wrong_value"] += 1
                        if full_wrong:
                            census["full_wrong_value"] += 1
                        if (
                            factor_compiled.unexpected_targets
                            or full_compiled.unexpected_targets
                            or factor_wrong
                            or full_wrong
                        ):
                            continue
                        census["value_clean"] += 1
                        factor = c112.append_graph(
                            source=TERMINAL,
                            outputs=factor_outputs,
                            raw=union3,
                            ignored=IGNORED,
                            state_limit=10_000,
                        )
                        if (
                            factor.bad
                            or factor.terminals != 1
                            or factor.terminal_sizes
                            != (len(factor_outputs),)
                            or len(factor.reached) != len(factor_outputs)
                        ):
                            census["factor_graph_fail"] += 1
                            continue
                        census["factor_graph_clean"] += 1
                        survivors.append((center, guard_role, factor_outputs))
    return tuple(centers), tuple(fresh_roles), dict(sorted(census.items())), tuple(survivors)


def direct_oz_survivors():
    results = []
    targets = tuple(sorted(
        site
        for site in c53.open_candidates(TERMINAL)
        if distance(site) <= 3
        and len(c53.local_signature(TERMINAL, site)) >= 2
        and any(
            value == "Y2"
            for _direction, value in c53.local_signature(TERMINAL, site)
        )
    ))
    seen = set()
    for target in targets:
        row = add_row(TERMINAL, BASE_UNION, target, "OZ")
        if row is None:
            continue
        records1, union1, canonical, _local, matches, _raw = row
        if canonical in seen:
            continue
        seen.add(canonical)
        outputs = {site: "OZ" for site in matches}
        full_outputs = {**BASE_OUTPUTS, **outputs}
        factor_compiled = c112.compile_conditions(
            TERMINAL, outputs, union1, IGNORED
        )
        full_compiled = c112.compile_conditions(
            c112.SOURCE, full_outputs, union1, IGNORED
        )
        if (
            factor_compiled.unexpected_targets
            or full_compiled.unexpected_targets
            or wrong_value_conditions(factor_compiled, outputs)
            or wrong_value_conditions(full_compiled, full_outputs)
        ):
            continue
        factor = c112.append_graph(
            source=TERMINAL,
            outputs=outputs,
            raw=union1,
            ignored=IGNORED,
            state_limit=1000,
        )
        if (
            not factor.bad
            and factor.terminals == 1
            and factor.terminal_sizes == (len(outputs),)
        ):
            next_matches = tuple(sorted(
                site
                for site in c53.open_candidates(records1)
                if c53.canonical_signature(c53.local_signature(records1, site))
                == NEXT_CANONICAL
            ))
            results.append((target, matches, next_matches))
    return targets, tuple(results)


ONE_ROW, TWO_ROW, TWO_CLEAN, TWO_UNEXPECTED = one_two_socket_census()
SIDE_CANDIDATES = terminal_side_guard_candidates()
SIDE_UNEXPECTED_CLEAN = tuple(
    item for item in SIDE_CANDIDATES if not item["unexpected"]
)
TERMINAL_ROLES = frozenset(TERMINAL.values())
SIDE_FRESH = tuple(
    item
    for item in SIDE_UNEXPECTED_CLEAN
    if item["guard_output"] not in TERMINAL_ROLES
)
SELECTED = min(
    SIDE_FRESH,
    key=lambda item: (
        item["raw_delta"],
        item["guard_output"],
        item["outward_output"],
    ),
)
SELECTED_FACTOR_OUTPUTS = {**SELECTED["adapter"], **SELECTED["oz"]}
SELECTED_FULL_OUTPUTS = {**BASE_OUTPUTS, **SELECTED_FACTOR_OUTPUTS}
SELECTED_FACTOR = c112.append_graph(
    source=TERMINAL,
    outputs=SELECTED_FACTOR_OUTPUTS,
    raw=SELECTED["union"],
    ignored=IGNORED,
    state_limit=1000,
)
SELECTED_FULL = c112.append_graph(
    source=c112.SOURCE,
    outputs=SELECTED_FULL_OUTPUTS,
    raw=SELECTED["union"],
    ignored=IGNORED,
    state_limit=1000,
)
DELETED_UNION = {
    local: values
    for local, values in SELECTED["union"].items()
    if local not in SELECTED["guard_raw"]
}
DELETED_FACTOR = c112.append_graph(
    source=TERMINAL,
    outputs=SELECTED_FACTOR_OUTPUTS,
    raw=DELETED_UNION,
    ignored=IGNORED,
    state_limit=1000,
)
CENTERS, FRESH_ROLES, CENTER_CENSUS, CENTER_SURVIVORS = centered_three_row_census()
DIRECT_TARGETS, DIRECT_SURVIVORS = direct_oz_survivors()


def base_contract() -> None:
    section("A - Exact predecessor and search surface")
    check("A01 Cycle 134 note exists", NOTE.is_file())
    check(
        "A02 exact Cycle-129 bridge reconstructs 16 canonical / 366 raw rows",
        len(BRIDGE_TABLE) == 16 and len(BRIDGE_RAW) == 366,
        f"canonical={len(BRIDGE_TABLE)} raw={len(BRIDGE_RAW)}",
    )
    check(
        "A03 reconstructed terminal is exact 394-record C129 terminal",
        len(TERMINAL) == 394
        and TERMINAL[CONTACT] == "Y2"
        and len(BASE_UNION) == 9_110,
        f"terminal={len(TERMINAL)} union={len(BASE_UNION)}",
    )
    check(
        "A04 old launch remains exact H1 + R_B01 -> OZ",
        set(value for _direction, value in GROUP_LOCALS[0])
        == {"H1", "R_B01"}
        and BRIDGE_TABLE[LAUNCH_CANONICAL] == "OZ",
        str(GROUP_LOCALS[0]),
    )


def small_adapter_contract() -> None:
    section("B - One- and two-row outward socket census")
    check("B01 no one-row fresh H1/R_B01 socket exists", len(ONE_ROW) == 0)
    check(
        "B02 exactly twelve two-row geometric sockets exist",
        len(TWO_ROW) == 12,
        str(len(TWO_ROW)),
    )
    check(
        "B03 no two-row socket survives full-source target/value screening",
        len(TWO_CLEAN) == 0
        and all(bool(item) for item in TWO_UNEXPECTED),
        f"clean={len(TWO_CLEAN)}",
    )
    unexpected_union = frozenset(site for group in TWO_UNEXPECTED for site in group)
    check(
        "B04 two-row failures are exact old/transient alias sites",
        unexpected_union
        == frozenset(((-2, 1, -1), (-2, 2, -2), (-1, 1, -2))),
        str(tuple(sorted(unexpected_union))),
    )


def attractive_guard_contract() -> None:
    section("C - Attractive three-row guard and earliest exact counterexample")
    check(
        "C01 terminal-side topology has 296 candidates / 244 unexpected-target-clean",
        len(SIDE_CANDIDATES) == 296 and len(SIDE_UNEXPECTED_CLEAN) == 244,
        f"candidates={len(SIDE_CANDIDATES)} unexpected_clean={len(SIDE_UNEXPECTED_CLEAN)}",
    )
    check(
        "C02 fresh-label filter leaves sixteen variants",
        len(SIDE_FRESH) == 16
        and {item["guard_output"] for item in SIDE_FRESH}
        == {"R_C11", "R_C13", "R_C21", "R_C23", "R_C30", "R_C32", "R_C33", "R_C41"},
        str(tuple(sorted({item['guard_output'] for item in SIDE_FRESH}))),
    )
    check(
        "C03 declared score/tie-break chooses R_C11 with 54 raw rows",
        SELECTED["guard_output"] == "R_C11"
        and SELECTED["outward_output"] == "H1"
        and SELECTED["side_output"] == "R_B01"
        and SELECTED["raw_delta"] == 54,
        str((SELECTED["guard_output"], SELECTED["raw_delta"])),
    )
    check(
        "C04 terminal-only factor has the misleading 7-state completion",
        SELECTED_FACTOR.states == 7
        and SELECTED_FACTOR.edges == 8
        and SELECTED_FACTOR.terminals == 1
        and SELECTED_FACTOR.terminal_sizes == (4,)
        and SELECTED_FACTOR.max_frontier == 2
        and not SELECTED_FACTOR.bad,
        f"states={SELECTED_FACTOR.states} edges={SELECTED_FACTOR.edges} terminals={SELECTED_FACTOR.terminals}",
    )
    wrong = SELECTED["wrong"]
    check(
        "C05 expected-target screen catches R_C11 demand at future Y2 contact",
        any(
            target == CONTACT and ("R_C11",) in values
            for target, values in wrong
        ),
        str(wrong),
    )
    check(
        "C06 full graph stops at exact earliest wrong-value transition",
        SELECTED_FULL.states == 95
        and SELECTED_FULL.edges == 206
        and SELECTED_FULL.terminals == 0
        and SELECTED_FULL.bad
        == ((25088, CONTACT, frozenset(("R_C11",))),),
        str(SELECTED_FULL.bad),
    )
    check(
        "C07 deleting the guard row removes the false factor completion",
        not DELETED_FACTOR.bad
        and DELETED_FACTOR.terminals >= 1
        and len(SELECTED_FACTOR_OUTPUTS) not in DELETED_FACTOR.terminal_sizes
        and (-3, 1, -1) not in DELETED_FACTOR.reached,
        f"terminal_sizes={DELETED_FACTOR.terminal_sizes} reached={len(DELETED_FACTOR.reached)}",
    )
    delta = {
        local: values
        for local, values in SELECTED["union"].items()
        if local not in BASE_UNION
    }
    covariance_failures = []
    controls = 0
    for local, values in delta.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            if delta.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation))
    check(
        "C08 all 1,296 added-row covariance checks are exact",
        len(delta) == 54 and controls == 1_296 and not covariance_failures,
        f"delta={len(delta)} controls={controls}",
    )


def centered_and_direct_contract() -> None:
    section("D - Causally late centered family and direct launch route")
    expected_census = {
        "arm1_rows": 146,
        "arm2_rows": 102,
        "centers": 5,
        "direction_pairs": 396,
        "factor_unexpected": 32,
        "fresh_roles": 11,
        "full_unexpected": 48,
        "full_wrong_value": 48,
        "guard_attempts": 55,
        "guard_rows": 55,
        "open_geometries": 88,
        "role_assignments": 176,
        "singleton_guards": 33,
        "socket_geometries": 48,
    }
    check(
        "D01 centered search has five late centers and eleven fresh roles",
        len(CENTERS) == 5 and len(FRESH_ROLES) == 11,
        f"centers={CENTERS} fresh={FRESH_ROLES}",
    )
    check(
        "D02 singleton-center/all-arm-coimage census is exact",
        CENTER_CENSUS == expected_census,
        str(CENTER_CENSUS),
    )
    check(
        "D03 none of 48 centered socket geometries survives full value screen",
        CENTER_CENSUS["socket_geometries"] == 48
        and CENTER_CENSUS["full_wrong_value"] == 48
        and not CENTER_SURVIVORS,
        str(CENTER_SURVIVORS),
    )
    check(
        "D04 all five direct late-interface OZ rows also fail exact screen",
        len(DIRECT_TARGETS) == 5 and not DIRECT_SURVIVORS,
        f"targets={DIRECT_TARGETS} survivors={DIRECT_SURVIVORS}",
    )


def scope_contract() -> None:
    section("E - Bounded scope and constitutional boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names guarded three-row socket renewal boundary",
        "guarded three-row socket renewal boundary" in note,
    )
    check(
        "E02 note keeps four-row and bridge redesign routes live",
        "four-row" in note and "bridge redesign" in note,
    )
    check(
        "E03 note preserves bridge-row recurrence separately",
        "bridge-row recurrence" in note and "socket" in note,
    )
    check(
        "E04 note carries complete N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "E05 note denies socket/recurrence no-go and axiom addition",
        "not a socket no-go" in note
        and "not a recurrence no-go" in note
        and "no axiom addition follows" in note,
    )
    check(
        "E06 Cycle 134 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    base_contract()
    small_adapter_contract()
    attractive_guard_contract()
    centered_and_direct_contract()
    scope_contract()
    print(
        f"\nONE_ROW={len(ONE_ROW)} TWO_ROW={len(TWO_ROW)} "
        f"SIDE={len(SIDE_CANDIDATES)} SIDE_UNEXPECTED_CLEAN={len(SIDE_UNEXPECTED_CLEAN)} "
        f"CENTER_SOCKET_GEOMETRIES={CENTER_CENSUS['socket_geometries']}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=GUARDED_THREE_ROW_SOCKET_RENEWAL_BOUNDARY"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
