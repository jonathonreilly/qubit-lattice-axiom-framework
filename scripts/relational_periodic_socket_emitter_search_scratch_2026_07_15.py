#!/usr/bin/env python3
"""Search a period-reused rail-side H1/R_B01 socket emitter.

The Cycle-129 bridge itself is not recurrent: its terminal roles differ from
its launch roles and both immediate common neighbours are occupied.  The
renewable rail, however, contains an R_B01 phase once per translated period.
This scratch asks whether one additional relational helper row plus one H1 row
can expose the inherited H1+R_B01 -> OZ launch at two consecutive periods.

Candidates are generated simultaneously at the first two post-bridge R_B01
phases.  The two periods must use the same canonical helper and H1 rows; every
proper-cubic coimage currently matching either row is retained.  Static
terminal screening precedes the full-source condition compiler.
"""

from __future__ import annotations

from collections import defaultdict

import post_cycle131_outward_adapter_search_scratch as s


Coord = tuple[int, int, int]
PERIOD_SHIFT: Coord = (-4, 0, 0)
RAIL_HORIZON = 65
RB01_INDICES = tuple(
    index
    for index, (_site, value) in enumerate(s.c105.RAIL_SEQUENCE[:RAIL_HORIZON])
    if value == "R_B01" and index >= 12
)


def translate(site: Coord, shift: Coord = PERIOD_SHIFT) -> Coord:
    return s.add(site, shift)


def common_neighbours(left: Coord, right: Coord) -> tuple[Coord, ...]:
    return tuple(sorted(
        set(s.add(left, direction) for direction in s.c53.DIRECTIONS)
        & set(s.add(right, direction) for direction in s.c53.DIRECTIONS)
    ))


def build_base():
    _table, _raw, union, terminal, _observed, locals_seen = s.bridge_state()
    rail_tail = dict(s.c105.RAIL_SEQUENCE[12:RAIL_HORIZON])
    records = {**terminal, **rail_tail}
    outputs = {
        **s.c124.GROWN_OUTPUTS,
        **s.s129.RAIL_OUTPUTS,
        **s.s129.BRIDGE_OUTPUTS,
        **rail_tail,
    }
    ignored_site, ignored_value = s.c105.RAIL_SEQUENCE[RAIL_HORIZON]
    ignored = {ignored_site: frozenset((ignored_value,))}
    return union, records, outputs, ignored, locals_seen


def row_matches(records, canonical) -> tuple[Coord, ...]:
    raw = s.c59.raw_rule_outputs({canonical: "H1"})
    return tuple(sorted(
        site
        for site in s.c53.open_candidates(records)
        if s.c53.local_signature(records, site) in raw
    ))


def socket_shapes(records, locals_seen):
    launch_canonical = s.c53.canonical_signature(locals_seen[0])
    q1 = s.c105.RAIL_SEQUENCE[RB01_INDICES[0]][0]
    q2 = s.c105.RAIL_SEQUENCE[RB01_INDICES[1]][0]
    assert translate(q1) == q2
    shapes = []
    for d1 in s.c53.DIRECTIONS:
        for d2 in s.c53.DIRECTIONS:
            if d1 >= d2 or s.dot(d1, d2) != 0:
                continue
            p1 = s.add(s.add(q1, d1), d2)
            p2 = translate(p1)
            if p1 in records or p2 in records:
                continue
            common1 = common_neighbours(p1, q1)
            common2 = common_neighbours(p2, q2)
            occupied1 = tuple(site for site in common1 if site in records)
            occupied2 = tuple(site for site in common2 if site in records)
            open1 = tuple(site for site in common1 if site not in records)
            open2 = tuple(site for site in common2 if site not in records)
            if len(occupied1) != 1 or len(occupied2) != 1:
                continue
            if len(open1) != 1 or len(open2) != 1:
                continue
            if translate(occupied1[0]) != occupied2[0]:
                continue
            if translate(open1[0]) != open2[0]:
                continue
            trial = {**records, p1: "H1", p2: "H1"}
            if any(
                s.c53.canonical_signature(s.c53.local_signature(trial, launch))
                != launch_canonical
                for launch in (open1[0], open2[0])
            ):
                continue
            local1 = s.c53.local_signature(records, p1)
            local2 = s.c53.local_signature(records, p2)
            if s.c53.canonical_signature(local1) != s.c53.canonical_signature(local2):
                continue
            shapes.append((p1, p2, occupied1[0], occupied2[0], open1[0], open2[0], local1))
    return tuple(shapes)


def helper_positions(records, p1: Coord, p2: Coord):
    answers = []
    for direction in s.c53.DIRECTIONS:
        h1 = s.add(p1, direction)
        h2 = translate(h1)
        if h1 in records or h2 in records or h1 == p2:
            continue
        local1 = s.c53.local_signature(records, h1)
        local2 = s.c53.local_signature(records, h2)
        if not local1 or not local2:
            continue
        if s.c53.canonical_signature(local1) != s.c53.canonical_signature(local2):
            continue
        answers.append((h1, h2, local1))
    return tuple(answers)


def wrong_value_conditions(compiled, outputs, ignored):
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
        and target not in ignored
        and any(
            values != frozenset((outputs[target],))
            for _present, _mask, values in conditions
        )
    ))


def wrong_value_details(compiled, outputs, ignored):
    def sites(mask: int):
        return tuple(
            site
            for index, site in enumerate(compiled.sites)
            if mask >> index & 1
        )

    return tuple(sorted(
        (target, sites(present), sites(neighbourhood), tuple(sorted(values)))
        for target, conditions in compiled.conditions.items()
        if target in outputs and target not in ignored
        for present, neighbourhood, values in conditions
        if values != frozenset((outputs[target],))
    ))


def required_parent_sites(records, target: Coord) -> frozenset[Coord]:
    return frozenset(
        s.add(target, direction)
        for direction, _value in s.c53.local_signature(records, target)
    )


def transitive_ancestors(parent_map, site: Coord) -> frozenset[Coord]:
    answer: set[Coord] = set()
    stack = list(parent_map.get(site, ()))
    while stack:
        parent = stack.pop()
        if parent in answer:
            continue
        answer.add(parent)
        stack.extend(parent_map.get(parent, ()))
    return frozenset(answer)


def search():
    census = defaultdict(int)
    union, records, base_outputs, ignored, locals_seen = build_base()
    base_compiled = s.c112.compile_conditions(
        s.c112.SOURCE,
        base_outputs,
        union,
        ignored,
    )
    base_wrong_details = set(wrong_value_details(base_compiled, base_outputs, ignored))
    shapes = socket_shapes(records, locals_seen)
    census["socket_shapes"] = len(shapes)
    candidate_roles = tuple(sorted(
        s.c105.c89.FULL_ROLES - frozenset(("H1", "R_B01"))
    ))
    survivors = []
    best_failures = []
    for shape in shapes:
        p1, p2, _block1, _block2, launch1, launch2, _local = shape
        helpers = helper_positions(records, p1, p2)
        census["helper_geometries"] += len(helpers)
        for h1, h2, helper_local in helpers:
            helper_canonical = s.c53.canonical_signature(helper_local)
            for helper_role in candidate_roles:
                census["helper_role_attempts"] += 1
                helper_raw = s.c59.raw_rule_outputs({helper_canonical: helper_role})
                try:
                    union1 = s.c112.merge_raw(union, helper_raw)
                except RuntimeError:
                    census["helper_merge_conflicts"] += 1
                    continue
                helper_matches = tuple(sorted(
                    site
                    for site in s.c53.open_candidates(records)
                    if s.c53.local_signature(records, site) in helper_raw
                ))
                if h1 not in helper_matches or h2 not in helper_matches:
                    continue
                helper_outputs = {site: helper_role for site in helper_matches}
                records1 = {**records, **helper_outputs}
                h1_local = s.c53.local_signature(records1, p1)
                h2_local = s.c53.local_signature(records1, p2)
                h1_canonical = s.c53.canonical_signature(h1_local)
                if h1_canonical != s.c53.canonical_signature(h2_local):
                    continue
                h1_raw = s.c59.raw_rule_outputs({h1_canonical: "H1"})
                try:
                    union2 = s.c112.merge_raw(union1, h1_raw)
                except RuntimeError:
                    census["h1_merge_conflicts"] += 1
                    continue
                h1_matches = tuple(sorted(
                    site
                    for site in s.c53.open_candidates(records1)
                    if s.c53.local_signature(records1, site) in h1_raw
                ))
                if p1 not in h1_matches or p2 not in h1_matches:
                    continue
                h1_outputs = {site: "H1" for site in h1_matches}
                records2 = {**records1, **h1_outputs}
                launches = s.launch_matches(
                    records2,
                    s.c53.canonical_signature(locals_seen[0]),
                )
                if launch1 not in launches or launch2 not in launches:
                    continue
                oz_outputs = {site: "OZ" for site in launches}
                if set(helper_outputs) & set(base_outputs):
                    census["helper_output_overlap"] += 1
                    continue
                if set(h1_outputs) & (set(base_outputs) | set(helper_outputs)):
                    census["h1_output_overlap"] += 1
                    continue
                if set(oz_outputs) & (set(base_outputs) | set(helper_outputs) | set(h1_outputs)):
                    census["oz_output_overlap"] += 1
                    continue
                outputs = {
                    **base_outputs,
                    **helper_outputs,
                    **h1_outputs,
                    **oz_outputs,
                }
                census["static_socket_survivors"] += 1
                compiled = s.c112.compile_conditions(
                    s.c112.SOURCE,
                    outputs,
                    union2,
                    ignored,
                )
                wrong = wrong_value_conditions(compiled, outputs, ignored)
                details = wrong_value_details(compiled, outputs, ignored)
                unexpected = tuple(sorted(compiled.unexpected_targets))
                new_sites = frozenset(
                    set(helper_outputs) | set(h1_outputs) | set(oz_outputs)
                )
                projected_base = {
                    (
                        target,
                        present,
                        tuple(site for site in neighbourhood if site not in new_sites),
                        values,
                    )
                    for target, present, neighbourhood, values in details
                    if target not in new_sites and not (set(present) & new_sites)
                }
                baseline_projected = {
                    item for item in base_wrong_details if item[0] not in new_sites
                }
                new_pre = tuple(sorted(projected_base - baseline_projected))
                new_target_wrong = tuple(sorted(
                    item for item in details if item[0] in new_sites
                ))

                parent_map = {
                    site: required_parent_sites(records, site)
                    for site in helper_outputs
                }
                parent_map.update({
                    site: required_parent_sites(records1, site)
                    for site in h1_outputs
                })
                parent_map.update({
                    site: required_parent_sites(records2, site)
                    for site in oz_outputs
                })
                unsafe_post = []
                for item in details:
                    target, present, _neighbourhood, _values = item
                    present_new = set(present) & new_sites
                    if target in new_sites or not present_new:
                        continue
                    if not all(
                        target in transitive_ancestors(parent_map, new_site)
                        for new_site in present_new
                    ):
                        unsafe_post.append(item)
                unsafe_post = tuple(sorted(unsafe_post))
                if unexpected:
                    census["unexpected_failures"] += 1
                if new_pre:
                    census["new_pre_wrong_failures"] += 1
                if new_target_wrong:
                    census["new_target_wrong_failures"] += 1
                if unsafe_post:
                    census["unsafe_post_wrong_failures"] += 1
                if wrong:
                    census["wrong_value_failures"] += 1
                if not unexpected and not new_pre and not new_target_wrong and not unsafe_post:
                    census["compiler_survivors"] += 1
                    survivors.append({
                        "shape": shape,
                        "helper": (h1, h2, helper_role, helper_local, helper_matches),
                        "h1": (p1, p2, h1_local, h1_matches),
                        "launches": launches,
                        "helper_raw": helper_raw,
                        "h1_raw": h1_raw,
                        "union": union2,
                        "outputs": outputs,
                        "ignored": ignored,
                        "compiled": compiled,
                        "absolute_wrong": wrong,
                    })
                else:
                    best_failures.append((
                        len(unexpected) + len(new_pre) + len(new_target_wrong) + len(unsafe_post),
                        len(unexpected),
                        len(new_pre),
                        len(new_target_wrong),
                        len(unsafe_post),
                        shape,
                        (h1, h2, helper_role, helper_local, helper_matches),
                        (p1, p2, h1_local, h1_matches),
                        launches,
                        unexpected,
                        new_pre,
                        new_target_wrong,
                        unsafe_post,
                    ))
    return census, survivors, tuple(sorted(best_failures, key=lambda item: item[:5]))


def main() -> None:
    print("RB01_INDICES", RB01_INDICES)
    census, survivors, best_failures = search()
    print("CENSUS", dict(sorted(census.items())))
    print("SURVIVORS", len(survivors))
    for index, survivor in enumerate(survivors[:20]):
        print("SURVIVOR", index)
        print(" SHAPE", survivor["shape"])
        print(" HELPER", survivor["helper"])
        print(" H1", survivor["h1"])
        print(" LAUNCHES", survivor["launches"])
        print(" RAW", len(survivor["helper_raw"]), len(survivor["h1_raw"]), len(survivor["union"]))
    print("BEST_FAILURES", len(best_failures))
    for failure in best_failures[:20]:
        print(
            " FAILURE",
            failure[:9],
            "DETAIL_COUNTS",
            tuple(len(items) for items in failure[9:]),
        )
    if best_failures:
        print("BEST_NEW_PRE", best_failures[0][10])


if __name__ == "__main__":
    main()
