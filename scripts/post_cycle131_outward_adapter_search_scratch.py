#!/usr/bin/env python3
"""Scratch census/search for the smallest outward Cycle-131 socket adapter.

This intentionally imports the lightweight Cycle-129 construction scratch,
not the official exhaustive runner.  Candidate rows are still closed under
proper-cubic rotations and are screened against the exact Cycle-124 raw law.
"""

from __future__ import annotations

from collections import defaultdict
import post_cycle129_guarded_rail_bridge_graph_scratch as s129


c124 = s129.c124
c112 = s129.c112
c105 = s129.c105
c59 = s129.c59
c53 = s129.c53

Coord = tuple[int, int, int]


def add(a: Coord, b: Coord) -> Coord:
    return tuple(x + y for x, y in zip(a, b, strict=True))  # type: ignore[return-value]


def sub(a: Coord, b: Coord) -> Coord:
    return tuple(x - y for x, y in zip(a, b, strict=True))  # type: ignore[return-value]


def rotate_coord(site: Coord, rotation) -> Coord:
    return c53.matvec(rotation, site)


def transform(site: Coord, rotation, shift: Coord) -> Coord:
    return add(rotate_coord(site, rotation), shift)


def bridge_state():
    table, observed, locals_seen = s129.build_table()
    raw = c59.raw_rule_outputs(table)
    union = c112.merge_raw(c124.FULL_RAW, raw)
    terminal = {
        **c124.positive_terminal_records(),
        **s129.RAIL_OUTPUTS,
        **s129.BRIDGE_OUTPUTS,
    }
    return table, raw, union, terminal, observed, locals_seen


def external_parents(locals_seen):
    """List original non-bridge neighbours each bridge row consumes."""
    prior: dict[Coord, str] = {}
    rows = []
    for (sites, output), local in zip(s129.GROUPS, locals_seen, strict=True):
        target = sites[0]
        consumers = []
        for direction, value in local:
            neighbour = add(target, direction)
            consumers.append((neighbour, value, neighbour in prior))
        rows.append((target, output, tuple(consumers)))
        prior.update({site: output for site in sites})
    return tuple(rows)


def terminal_neighbourhood(terminal, radius: int = 3):
    contact = (-2, 2, -1)
    answer = []
    for site in c53.open_candidates(terminal):
        distance = sum(abs(x) for x in sub(site, contact))
        if distance <= radius:
            local = c53.local_signature(terminal, site)
            answer.append((distance, site, local, c53.canonical_signature(local)))
    return tuple(sorted(answer))


def transformed_bridge_placements(terminal, locals_seen, rail_length: int = 96):
    """Census placements whose frame parent is a later B_0_2 rail record."""
    original_frame = (-2, 2, 0)
    bridge_sites = tuple(s129.BRIDGE_OUTPUTS)
    rail = tuple(c105.RAIL_SEQUENCE[:rail_length])
    grown_terminal = {**terminal, **dict(rail)}
    frame_sites = tuple(site for site, value in rail if value == "B_0_2")
    candidates = []
    for frame in frame_sites:
        for rotation in c53.ROTATIONS:
            shift = sub(frame, rotate_coord(original_frame, rotation))
            mapped = {site: transform(site, rotation, shift) for site in bridge_sites}
            collisions = tuple(sorted(
                (source, target, terminal.get(target), s129.BRIDGE_OUTPUTS[source])
                for source, target in mapped.items()
                if target in grown_terminal
            ))
            if collisions:
                continue
            # Grow only in the intended generation order to classify how many
            # row interfaces differ before exact async screening.
            records = dict(grown_terminal)
            mismatches = []
            for index, ((sites, output), original_local) in enumerate(
                zip(s129.GROUPS, locals_seen, strict=True)
            ):
                mapped_sites = tuple(mapped[site] for site in sites)
                local = c53.local_signature(records, mapped_sites[0])
                expected = c53.rotate_signature(original_local, rotation)
                if local != expected:
                    mismatches.append((index, mapped_sites, local, expected))
                records.update({site: output for site in mapped_sites})
            candidates.append((frame, rotation, shift, mapped, tuple(mismatches)))
    return tuple(candidates)


def one_row_equivalent_launches(terminal, base_union):
    """Every open terminal context that can safely add an OZ launch row."""
    survivors = []
    for target in sorted(c53.open_candidates(terminal)):
        local = c53.local_signature(terminal, target)
        canonical = c53.canonical_signature(local)
        if not canonical:
            continue
        candidate_raw = c59.raw_rule_outputs({canonical: "OZ"})
        try:
            merged = c112.merge_raw(base_union, candidate_raw)
        except RuntimeError:
            continue
        if any(len(values) != 1 for values in merged.values()):
            continue
        images = tuple(sorted(
            site
            for site in c53.open_candidates(terminal)
            if c53.local_signature(terminal, site) in candidate_raw
        ))
        if target not in images:
            continue
        survivors.append((target, local, images, len(candidate_raw)))
    return tuple(survivors)


CONTACT = (-2, 2, -1)
ANCHOR_VALUES = frozenset(("Y2", "T_N0", "B_0_2"))
LAUNCH_ROLES = ("H1", "R_B01")


def distance_from_contact(site: Coord) -> int:
    return sum(abs(value) for value in sub(site, CONTACT))


def add_row(records, union, target: Coord, output: str):
    """Add every currently matched proper-cubic image of one candidate row."""
    local = c53.local_signature(records, target)
    if not local:
        return None
    canonical = c53.canonical_signature(local)
    candidate_raw = c59.raw_rule_outputs({canonical: output})
    merged = c112.merge_raw(union, candidate_raw)
    if any(len(values) != 1 for values in merged.values()):
        return None
    matches = tuple(sorted(
        site
        for site in c53.open_candidates(records)
        if c53.local_signature(records, site) in candidate_raw
    ))
    if target not in matches:
        return None
    future = dict(records)
    future.update({site: output for site in matches})
    return future, merged, canonical, local, matches, candidate_raw


def launch_matches(records, launch_canonical):
    return tuple(sorted(
        site
        for site in c53.open_candidates(records)
        if c53.canonical_signature(c53.local_signature(records, site))
        == launch_canonical
    ))


def socket_search(terminal, union, locals_seen, radius: int = 3):
    """Exhaust one- and two-row H1/R_B01 socket normalizers nearby."""
    launch_canonical = c53.canonical_signature(locals_seen[0])
    one_row = []
    two_row = []
    seen_first = set()
    first_targets = tuple(sorted(
        site
        for site in c53.open_candidates(terminal)
        if distance_from_contact(site) <= radius
        and any(value in ANCHOR_VALUES for _direction, value in c53.local_signature(terminal, site))
    ))
    for first_target in first_targets:
        for first_output in LAUNCH_ROLES:
            first = add_row(terminal, union, first_target, first_output)
            if first is None:
                continue
            records1, union1, canonical1, local1, matches1, raw1 = first
            key1 = (canonical1, first_output)
            if key1 in seen_first:
                continue
            seen_first.add(key1)
            launches1 = launch_matches(records1, launch_canonical)
            if launches1:
                one_row.append((first_target, first_output, local1, matches1, launches1, union1, records1))
            second_targets = tuple(sorted(
                site
                for site in c53.open_candidates(records1)
                if distance_from_contact(site) <= radius + 1
                and any(
                    value in ANCHOR_VALUES or value == first_output
                    for _direction, value in c53.local_signature(records1, site)
                )
            ))
            seen_second = set()
            for second_target in second_targets:
                for second_output in LAUNCH_ROLES:
                    second = add_row(records1, union1, second_target, second_output)
                    if second is None:
                        continue
                    records2, union2, canonical2, local2, matches2, raw2 = second
                    key2 = (canonical2, second_output)
                    if key2 in seen_second or key2 == key1:
                        continue
                    seen_second.add(key2)
                    launches2 = launch_matches(records2, launch_canonical)
                    if launches2:
                        two_row.append((
                            (first_target, first_output, local1, matches1),
                            (second_target, second_output, local2, matches2),
                            launches2,
                            union2,
                            records2,
                        ))
    return tuple(one_row), tuple(two_row)


def compiler_screen(sockets, terminal):
    """Full-source compiler screen including the newly exposed OZ sites."""
    results = []
    base_outputs = {
        **c124.GROWN_OUTPUTS,
        **s129.RAIL_OUTPUTS,
        **s129.BRIDGE_OUTPUTS,
    }
    ignored = {
        c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))
    }
    for first, second, launches, union, records in sockets:
        adapter_outputs = {
            site: first[1] for site in first[3]
        }
        adapter_outputs.update({site: second[1] for site in second[3]})
        overlap = set(adapter_outputs) & set(base_outputs)
        if overlap:
            results.append((first, second, launches, "OUTPUT_OVERLAP", tuple(sorted(overlap))))
            continue
        oz_outputs = {site: "OZ" for site in launches}
        if set(oz_outputs) & (set(base_outputs) | set(adapter_outputs)):
            results.append((first, second, launches, "LAUNCH_OVERLAP", ()))
            continue
        outputs = {**base_outputs, **adapter_outputs, **oz_outputs}
        compiled = c112.compile_conditions(c112.SOURCE, outputs, union, ignored)
        results.append((
            first,
            second,
            launches,
            "COMPILED",
            tuple(sorted(compiled.unexpected_targets)),
            len(compiled.conditions),
            len(adapter_outputs),
            len(oz_outputs),
        ))
    return tuple(results)


def guarded_three_row_search(terminal, union, locals_seen):
    """Guard the unavoidable unary-Y2 outward site, then form a fresh socket."""
    guard_target = (-3, 2, 0)
    outward_target = (-3, 2, -1)
    side_target = (-2, 1, -1)
    launch_canonical = c53.canonical_signature(locals_seen[0])
    base_outputs = {
        **c124.GROWN_OUTPUTS,
        **s129.RAIL_OUTPUTS,
        **s129.BRIDGE_OUTPUTS,
    }
    ignored = {
        c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))
    }
    results = []
    for guard_output in sorted(c105.c89.FULL_ROLES):
        if guard_output in LAUNCH_ROLES:
            continue
        guard = add_row(terminal, union, guard_target, guard_output)
        if guard is None:
            continue
        records1, union1, canonical1, local1, matches1, _raw1 = guard
        for outward_output, side_output in (
            ("H1", "R_B01"),
            ("R_B01", "H1"),
        ):
            outward = add_row(records1, union1, outward_target, outward_output)
            if outward is None:
                continue
            records2, union2, canonical2, local2, matches2, _raw2 = outward
            side = add_row(records2, union2, side_target, side_output)
            if side is None:
                continue
            records3, union3, canonical3, local3, matches3, _raw3 = side
            launches = launch_matches(records3, launch_canonical)
            if not launches:
                continue
            adapter_outputs = {site: guard_output for site in matches1}
            adapter_outputs.update({site: outward_output for site in matches2})
            adapter_outputs.update({site: side_output for site in matches3})
            oz_outputs = {site: "OZ" for site in launches}
            if set(adapter_outputs) & set(base_outputs):
                continue
            if set(oz_outputs) & (set(base_outputs) | set(adapter_outputs)):
                continue
            outputs = {**base_outputs, **adapter_outputs, **oz_outputs}
            compiled = c112.compile_conditions(c112.SOURCE, outputs, union3, ignored)
            results.append((
                guard_output,
                (guard_target, local1, matches1, canonical1),
                (outward_target, outward_output, local2, matches2, canonical2),
                (side_target, side_output, local3, matches3, canonical3),
                launches,
                tuple(sorted(compiled.unexpected_targets)),
                len(compiled.conditions),
                union3,
                adapter_outputs,
                oz_outputs,
            ))
    return tuple(results)


def wrong_value_conditions(compiled, outputs, ignored):
    """Expected targets whose compiled local subsets can demand another value."""
    return tuple(sorted(
        (
            target,
            tuple(sorted({tuple(sorted(values)) for _present, _mask, values in conditions if values != frozenset((outputs[target],))})),
        )
        for target, conditions in compiled.conditions.items()
        if target in outputs
        and any(values != frozenset((outputs[target],)) for _present, _mask, values in conditions)
    ))


def dot(a: Coord, b: Coord) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def centered_three_row_socket_search(
    terminal,
    union,
    locals_seen,
    *,
    return_census: bool = False,
):
    """Grow one causally late center, then two orthogonal socket arms."""
    launch_canonical = c53.canonical_signature(locals_seen[0])
    terminal_roles = frozenset(terminal.values())
    fresh_roles = tuple(sorted(c105.c89.FULL_ROLES - terminal_roles))
    base_outputs = {
        **c124.GROWN_OUTPUTS,
        **s129.RAIL_OUTPUTS,
        **s129.BRIDGE_OUTPUTS,
    }
    ignored = {
        c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))
    }
    centers = tuple(sorted(
        site
        for site in c53.open_candidates(terminal)
        if distance_from_contact(site) <= 3
        and len(c53.local_signature(terminal, site)) >= 2
        and any(value == "Y2" for _direction, value in c53.local_signature(terminal, site))
    ))
    results = []
    census = defaultdict(int)
    census["centers"] = len(centers)
    census["fresh_roles"] = len(fresh_roles)
    for center in centers:
        for guard_role in fresh_roles:
            census["guard_attempts"] += 1
            guard = add_row(terminal, union, center, guard_role)
            if guard is None:
                continue
            census["guard_rows"] += 1
            records1, union1, canonical1, local1, matches1, _raw1 = guard
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
                    if (
                        arm1_target in records1
                        or arm2_target in records1
                        or launch_target in records1
                    ):
                        continue
                    census["open_geometries"] += 1
                    for arm1_output, arm2_output in (
                        ("H1", "R_B01"),
                        ("R_B01", "H1"),
                    ):
                        census["role_assignments"] += 1
                        arm1 = add_row(records1, union1, arm1_target, arm1_output)
                        if arm1 is None:
                            continue
                        census["arm1_rows"] += 1
                        records2, union2, canonical2, local2, matches2, _raw2 = arm1
                        arm2 = add_row(records2, union2, arm2_target, arm2_output)
                        if arm2 is None:
                            continue
                        census["arm2_rows"] += 1
                        records3, union3, canonical3, local3, matches3, _raw3 = arm2
                        launches = launch_matches(records3, launch_canonical)
                        if launch_target not in launches:
                            continue
                        census["socket_geometries"] += 1
                        adapter_outputs = {site: guard_role for site in matches1}
                        adapter_outputs.update({site: arm1_output for site in matches2})
                        adapter_outputs.update({site: arm2_output for site in matches3})
                        oz_outputs = {site: "OZ" for site in launches}
                        factor_outputs = {**adapter_outputs, **oz_outputs}
                        full_outputs = {**base_outputs, **factor_outputs}
                        factor_compiled = c112.compile_conditions(
                            terminal, factor_outputs, union3, ignored
                        )
                        full_compiled = c112.compile_conditions(
                            c112.SOURCE, full_outputs, union3, ignored
                        )
                        factor_wrong = wrong_value_conditions(
                            factor_compiled, factor_outputs, ignored
                        )
                        full_wrong = wrong_value_conditions(
                            full_compiled, full_outputs, ignored
                        )
                        if (
                            factor_compiled.unexpected_targets
                            or full_compiled.unexpected_targets
                            or factor_wrong
                            or full_wrong
                        ):
                            if factor_compiled.unexpected_targets:
                                census["factor_unexpected"] += 1
                            if full_compiled.unexpected_targets:
                                census["full_unexpected"] += 1
                            if factor_wrong:
                                census["factor_wrong_value"] += 1
                            if full_wrong:
                                census["full_wrong_value"] += 1
                            continue
                        census["value_clean"] += 1
                        factor = c112.append_graph(
                            source=terminal,
                            outputs=factor_outputs,
                            raw=union3,
                            ignored=ignored,
                            state_limit=10_000,
                        )
                        if (
                            factor.bad
                            or factor.terminals != 1
                            or factor.terminal_sizes != (len(factor_outputs),)
                            or len(factor.reached) != len(factor_outputs)
                        ):
                            census["factor_graph_fail"] += 1
                            continue
                        census["factor_graph_clean"] += 1
                        results.append((
                            center,
                            guard_role,
                            local1,
                            (arm1_target, arm1_output, local2),
                            (arm2_target, arm2_output, local3),
                            launch_target,
                            len(set(union3) - set(union)),
                            len(full_compiled.conditions),
                            factor,
                            union3,
                            adapter_outputs,
                            oz_outputs,
                        ))
    answer = tuple(results)
    if return_census:
        return answer, dict(sorted(census.items()))
    return answer


def direct_terminal_oz_search(terminal, union, locals_seen):
    """One new row consuming a late terminal context and writing OZ directly."""
    next_canonical = c53.canonical_signature(locals_seen[1])
    base_outputs = {
        **c124.GROWN_OUTPUTS,
        **s129.RAIL_OUTPUTS,
        **s129.BRIDGE_OUTPUTS,
    }
    ignored = {
        c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))
    }
    results = []
    targets = tuple(sorted(
        site
        for site in c53.open_candidates(terminal)
        if distance_from_contact(site) <= 3
        and len(c53.local_signature(terminal, site)) >= 2
        and any(value == "Y2" for _direction, value in c53.local_signature(terminal, site))
    ))
    seen = set()
    for target in targets:
        candidate = add_row(terminal, union, target, "OZ")
        if candidate is None:
            continue
        records1, union1, canonical, local, matches, _raw = candidate
        key = canonical
        if key in seen:
            continue
        seen.add(key)
        outputs = {site: "OZ" for site in matches}
        full_outputs = {**base_outputs, **outputs}
        factor_compiled = c112.compile_conditions(
            terminal, outputs, union1, ignored
        )
        full_compiled = c112.compile_conditions(
            c112.SOURCE, full_outputs, union1, ignored
        )
        factor_wrong = wrong_value_conditions(factor_compiled, outputs, ignored)
        full_wrong = wrong_value_conditions(full_compiled, full_outputs, ignored)
        if (
            factor_compiled.unexpected_targets
            or full_compiled.unexpected_targets
            or factor_wrong
            or full_wrong
        ):
            continue
        factor = c112.append_graph(
            source=terminal,
            outputs=outputs,
            raw=union1,
            ignored=ignored,
            state_limit=1000,
        )
        if (
            factor.bad
            or factor.terminals != 1
            or factor.terminal_sizes != (len(outputs),)
            or len(factor.reached) != len(outputs)
        ):
            continue
        next_matches = tuple(sorted(
            site
            for site in c53.open_candidates(records1)
            if c53.canonical_signature(c53.local_signature(records1, site))
            == next_canonical
        ))
        results.append((
            target,
            local,
            len(set(union1) - set(union)),
            len(full_compiled.conditions),
            next_matches,
            factor,
            union1,
            outputs,
        ))
    return tuple(results)


def main() -> None:
    table, bridge_raw, union, terminal, observed, locals_seen = bridge_state()
    print("BASE", len(table), len(bridge_raw), len(union), len(terminal))
    print("GROUP_LOCALS")
    for row in external_parents(locals_seen):
        print(row)
    print("NEAR_TERMINAL")
    for item in terminal_neighbourhood(terminal):
        print(item)
    launches = one_row_equivalent_launches(terminal, union)
    print("ONE_ROW_OZ", len(launches))
    one_socket, two_socket = socket_search(terminal, union, locals_seen)
    print("ONE_ROW_SOCKET", len(one_socket))
    for item in one_socket[:40]:
        print(item[:5])
    print("TWO_ROW_SOCKET", len(two_socket))
    for item in two_socket[:20]:
        print(item[:3])
    screened = compiler_screen(two_socket, terminal)
    print("TWO_ROW_COMPILER_SCREEN", len(screened))
    for item in screened[:20]:
        print(item)
    guarded = guarded_three_row_search(terminal, union, locals_seen)
    print("THREE_ROW_GUARDED", len(guarded))
    clean_guarded = tuple(item for item in guarded if not item[5])
    print("THREE_ROW_GUARDED_CLEAN", len(clean_guarded))
    for item in clean_guarded[:120]:
        print(item[:7])
    if not clean_guarded:
        print("THREE_ROW_BEST")
        for item in sorted(guarded, key=lambda row: len(row[5]))[:40]:
            print(item[:7])
    placements = transformed_bridge_placements(terminal, locals_seen)
    print("OPEN_TRANSFORMED_PLACEMENTS", len(placements))
    census = defaultdict(int)
    for _frame, _rotation, _shift, _mapped, mismatches in placements:
        census[tuple(index for index, *_rest in mismatches)] += 1
    print("MISMATCH_CENSUS")
    for pattern, count in sorted(census.items(), key=lambda item: (len(item[0]), item[0])):
        print(count, pattern)
    print("BEST_PLACEMENTS")
    for frame, rotation, shift, mapped, mismatches in sorted(
        placements, key=lambda item: len(item[-1])
    )[:6]:
        print(
            "FRAME", frame,
            "ROT", rotation,
            "SHIFT", shift,
            "MISMATCHES", len(mismatches),
            tuple((index, sites, local) for index, sites, local, _expected in mismatches),
        )


if __name__ == "__main__":
    main()
