#!/usr/bin/env python3
"""Scratch search for a four-row late-guard/helper/socket topology.

Declared family:
  1. a radius-three open center with a >=2-parent local containing Y2 writes a
     terminal-absent alphabet guard role;
  2. a radius-four neighbour whose local contains that guard writes a distinct
     terminal-absent helper role;
  3-4. two orthogonal neighbours of the declared helper write H1 and R_B01;
     the opposite corner must expose the landed H1+R_B01 -> OZ row.

Every proper-cubic physical coimage is retained.  Full-source unexpected and
expected-target/wrong-value conditions are screened before any graph.
"""

from __future__ import annotations

from collections import defaultdict

import post_cycle131_outward_adapter_search_scratch as s


def socket_pair_launches(records, h_sites, r_sites):
    launches = s.launch_matches(records, s.c53.canonical_signature(LOCALS[0]))
    exact = []
    for launch in launches:
        local = s.c53.local_signature(records, launch)
        neighbours = {
            s.add(launch, direction): value for direction, value in local
        }
        if (
            any(site in neighbours and neighbours[site] == "H1" for site in h_sites)
            and any(site in neighbours and neighbours[site] == "R_B01" for site in r_sites)
        ):
            exact.append(launch)
    return tuple(sorted(exact))


def run_search():
    census = defaultdict(int)
    terminal_roles = frozenset(TERMINAL.values())
    fresh_roles = tuple(sorted(s.c105.c89.FULL_ROLES - terminal_roles))
    centers = tuple(sorted(
        site
        for site in s.c53.open_candidates(TERMINAL)
        if s.distance_from_contact(site) <= 3
        and len(s.c53.local_signature(TERMINAL, site)) >= 2
        and any(
            value == "Y2"
            for _direction, value in s.c53.local_signature(TERMINAL, site)
        )
    ))
    census["centers"] = len(centers)
    census["fresh_roles"] = len(fresh_roles)
    candidates = []
    seen_sequences = set()
    for center in centers:
        center_local = s.c53.local_signature(TERMINAL, center)
        assert len(center_local) >= 2 and "Y2" in {
            value for _direction, value in center_local
        }
        for guard_role in fresh_roles:
            census["guard_attempts"] += 1
            guard = s.add_row(TERMINAL, BASE_UNION, center, guard_role)
            if guard is None:
                continue
            census["guard_rows"] += 1
            records1, union1, guard_canonical, guard_local, guard_matches, _guard_raw = guard
            helper_targets = tuple(sorted(
                site
                for site in s.c53.open_candidates(records1)
                if s.distance_from_contact(site) <= 4
                and any(
                    value == guard_role
                    for _direction, value in s.c53.local_signature(records1, site)
                )
            ))
            census["helper_target_contexts"] += len(helper_targets)
            for helper_target in helper_targets:
                for helper_role in fresh_roles:
                    if helper_role == guard_role:
                        continue
                    census["helper_attempts"] += 1
                    helper = s.add_row(
                        records1, union1, helper_target, helper_role
                    )
                    if helper is None:
                        continue
                    census["helper_rows"] += 1
                    (
                        records2,
                        union2,
                        helper_canonical,
                        helper_local,
                        helper_matches,
                        _helper_raw,
                    ) = helper
                    for d1 in s.c53.DIRECTIONS:
                        for d2 in s.c53.DIRECTIONS:
                            if d1 >= d2 or s.dot(d1, d2) != 0:
                                continue
                            census["direction_pairs"] += 1
                            arm1_target = s.add(helper_target, d1)
                            arm2_target = s.add(helper_target, d2)
                            launch_target = s.add(s.add(helper_target, d1), d2)
                            if max(
                                s.distance_from_contact(arm1_target),
                                s.distance_from_contact(arm2_target),
                            ) > 5 or s.distance_from_contact(launch_target) > 6:
                                continue
                            if any(
                                site in records2
                                for site in (
                                    arm1_target,
                                    arm2_target,
                                    launch_target,
                                )
                            ):
                                continue
                            census["open_geometries"] += 1
                            for arm1_output, arm2_output in (
                                ("H1", "R_B01"),
                                ("R_B01", "H1"),
                            ):
                                census["role_assignments"] += 1
                                arm1 = s.add_row(
                                    records2,
                                    union2,
                                    arm1_target,
                                    arm1_output,
                                )
                                if arm1 is None:
                                    continue
                                census["arm1_rows"] += 1
                                (
                                    records3,
                                    union3,
                                    arm1_canonical,
                                    arm1_local,
                                    arm1_matches,
                                    _arm1_raw,
                                ) = arm1
                                arm2 = s.add_row(
                                    records3,
                                    union3,
                                    arm2_target,
                                    arm2_output,
                                )
                                if arm2 is None:
                                    continue
                                census["arm2_rows"] += 1
                                (
                                    records4,
                                    union4,
                                    arm2_canonical,
                                    arm2_local,
                                    arm2_matches,
                                    _arm2_raw,
                                ) = arm2
                                key = (
                                    (guard_canonical, guard_role),
                                    (helper_canonical, helper_role),
                                    (arm1_canonical, arm1_output),
                                    (arm2_canonical, arm2_output),
                                )
                                if key in seen_sequences:
                                    census["duplicate_sequences"] += 1
                                    continue
                                seen_sequences.add(key)
                                if arm1_output == "H1":
                                    h_sites, r_sites = arm1_matches, arm2_matches
                                else:
                                    h_sites, r_sites = arm2_matches, arm1_matches
                                launches = socket_pair_launches(
                                    records4, h_sites, r_sites
                                )
                                if launch_target not in launches:
                                    continue
                                census["socket_geometries"] += 1
                                adapter_outputs = {
                                    site: guard_role for site in guard_matches
                                }
                                adapter_outputs.update({
                                    site: helper_role for site in helper_matches
                                })
                                adapter_outputs.update({
                                    site: arm1_output for site in arm1_matches
                                })
                                adapter_outputs.update({
                                    site: arm2_output for site in arm2_matches
                                })
                                oz_outputs = {
                                    site: "OZ" for site in launches
                                }
                                factor_outputs = {
                                    **adapter_outputs,
                                    **oz_outputs,
                                }
                                full_outputs = {
                                    **BASE_OUTPUTS,
                                    **factor_outputs,
                                }
                                factor_compiled = s.c112.compile_conditions(
                                    TERMINAL,
                                    factor_outputs,
                                    union4,
                                    IGNORED,
                                )
                                full_compiled = s.c112.compile_conditions(
                                    s.c112.SOURCE,
                                    full_outputs,
                                    union4,
                                    IGNORED,
                                )
                                factor_wrong = s.wrong_value_conditions(
                                    factor_compiled,
                                    factor_outputs,
                                    IGNORED,
                                )
                                full_wrong = s.wrong_value_conditions(
                                    full_compiled,
                                    full_outputs,
                                    IGNORED,
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
                                census["screen_survivors"] += 1
                                candidates.append({
                                    "center": center,
                                    "guard_role": guard_role,
                                    "guard_local": guard_local,
                                    "helper_target": helper_target,
                                    "helper_role": helper_role,
                                    "helper_local": helper_local,
                                    "arm1_target": arm1_target,
                                    "arm1_output": arm1_output,
                                    "arm1_local": arm1_local,
                                    "arm2_target": arm2_target,
                                    "arm2_output": arm2_output,
                                    "arm2_local": arm2_local,
                                    "launches": launches,
                                    "union": union4,
                                    "factor_outputs": factor_outputs,
                                    "raw_delta": len(
                                        set(union4) - set(BASE_UNION)
                                    ),
                                    "full_conditions": len(
                                        full_compiled.conditions
                                    ),
                                })
    return (
        centers,
        fresh_roles,
        dict(sorted(census.items())),
        tuple(candidates),
    )


def main() -> None:
    centers, fresh_roles, census, candidates = run_search()
    print("CENTERS", centers)
    print("FRESH_ROLES", fresh_roles)
    print("CENSUS", census)
    print("SCREEN_SURVIVORS", len(candidates))
    for candidate in sorted(
        candidates,
        key=lambda item: (
            item["raw_delta"],
            item["center"],
            item["guard_role"],
            item["helper_target"],
            item["helper_role"],
        ),
    )[:40]:
        summary = {
            key: value
            for key, value in candidate.items()
            if key not in ("union", "factor_outputs")
        }
        print("SURVIVOR", summary)


TABLE, _BRIDGE_RAW, BASE_UNION, TERMINAL, _OBSERVED, LOCALS = s.bridge_state()
BASE_OUTPUTS = {
    **s.c124.GROWN_OUTPUTS,
    **s.s129.RAIL_OUTPUTS,
    **s.s129.BRIDGE_OUTPUTS,
}
IGNORED = {
    s.c105.RAIL_SEQUENCE[12][0]: frozenset((s.c105.RAIL_SEQUENCE[12][1],))
}


if __name__ == "__main__":
    main()
