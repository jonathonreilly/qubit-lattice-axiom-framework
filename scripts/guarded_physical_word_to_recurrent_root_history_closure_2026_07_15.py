#!/usr/bin/env python3
"""Bind the guarded physical R_B01 bridge into the first recurrent root.

Remove the direct C->D R_B01 root row.  Retain the two exact JOINT/T_H3
contact variants, rebuild the previously found eleven-record JOINT-to-root
detour, and close only exact schedule-enlarged conditions until the coupled
post-prefix graph passes or exposes a wrong write, conflict, dead wall, or
bounded variant cascade.

Scratch only; no retained or foundation surface changes.
"""

from __future__ import annotations

import guarded_bridge_recurrent_contact_history_closure_2026_07_15 as contact
import recurrent_r_b01_physical_writer_embedding_search_scratch_2026_07_15 as direct


base = contact.base
c141 = base.c141
c112 = base.c112
c53 = base.c53
cell = base.cell
ROOT = direct.c141.transform_site(cell.site(3, cell.ROOT_YZ))
PATH = (
    (-1, 1, -2),
    (-1, 0, -2),
    (-1, 0, -1),
    (-1, -1, -1),
    (-2, -1, -1),
    (-2, -2, -1),
    (-3, -2, -1),
    (-3, -1, -1),
    (-2, -1, 0),
    (-3, -1, 0),
    (-4, -1, 0),
    ROOT,
)
ROLES = (
    "J2", "J2", "T_H1", "T_H1", "T_H2", "T_H3",
    "J2", "R_A13", "R_A22", "R_A21", "R_A22", "R_B01",
)
JOINT = (-1, 2, -2)
SECOND_ROOT = (-8, 0, 0)
SIDECAR_TRUNK = (
    ((-5, -1, 0), "B1"),
    ((-6, -1, 0), "B1"),
    ((-7, -1, 0), "R_A21"),
)
SIDECAR_SHELL = (
    ((-8, -1, 0), "R_A22"),
    ((-7, -2, 0), "R_A22"),
    ((-7, -1, -1), "R_A22"),
)
SIDECAR_ROWS = (
    (
        (((0, 1, 0), "A_0_0"), ((1, 0, 0), "R_A22")),
        "B1",
    ),
    (
        (((0, 1, 0), "R_C10"), ((1, 0, 0), "B1")),
        "B1",
    ),
    (
        (((0, 1, 0), "B0"), ((1, 0, 0), "B1")),
        "R_A21",
    ),
)
ADAPTER_HISTORY_VARIANTS = (
    (
        (
            ((-1, 0, 0), "JOINT"), ((0, 0, -1), "J2"),
            ((0, 0, 1), "A_0_0"), ((0, 1, 0), "W3"),
            ((1, 0, 0), "W5"),
        ),
        "T_H1",
    ),
    (
        (((0, 0, 1), "R_C10"), ((0, 1, 0), "AUXZ"), ((1, 0, 0), "T_H1")),
        "JOINT",
    ),
    (
        (
            ((0, -1, 0), "T_H2"), ((0, 0, 1), "R_C10"),
            ((0, 1, 0), "AUXZ"), ((1, 0, 0), "T_H1"),
        ),
        "JOINT",
    ),
    (
        (((0, 0, -1), "L11"), ((0, 1, 0), "JOINT"), ((1, 0, 0), "T_H1")),
        "T_H2",
    ),
)
CONTACT_VARIANTS = (
    (
        (((0, 0, 1), "T_H3"), ((0, 1, 0), "R_C01"), ((1, 0, 0), "GU")),
        "JOINT",
    ),
    (
        (
            ((0, 0, -1), "JOINT"), ((0, 0, 1), "A_0_2"),
            ((0, 1, 0), "W1"), ((1, 0, 0), "W3"),
        ),
        "T_H3",
    ),
)


def add_table_row(table, local, output):
    canonical = cell.canonical(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise RuntimeError((canonical, prior, output))
    table[canonical] = output


def initial_table_and_outputs():
    table = dict(base.TABLE)
    for local, output in CONTACT_VARIANTS:
        add_table_row(table, local, output)

    records = {**base.RECORDS, **direct.first_pre_root_records()}
    records.pop(ROOT, None)
    outputs = {}
    origins = []
    for target, output in zip(PATH, ROLES):
        local = c53.local_signature(records, target)
        canonical = cell.canonical(local)
        inherited = base.prefix.FULL_RAW.get(local)
        prior = table.get(canonical)
        if inherited is not None:
            if inherited != frozenset((output,)):
                raise RuntimeError(("inherited", target, local, inherited, output))
            origin = "inherited"
        elif prior is not None:
            if prior != output:
                raise RuntimeError(("prior", target, canonical, prior, output))
            origin = "reused"
        else:
            table[canonical] = output
            origin = "new"
        records[target] = output
        outputs[target] = output
        origins.append((target, output, origin, local))
    for local, output in SIDECAR_ROWS:
        add_table_row(table, local, output)
    for target, output in (*SIDECAR_TRUNK, *SIDECAR_SHELL):
        outputs[target] = output
    origins.extend(
        (target, output, "sidecar", local)
        for (target, output), (local, _row_output)
        in zip(SIDECAR_TRUNK, SIDECAR_ROWS)
    )
    origins.append((tuple(site for site, _output in SIDECAR_SHELL), "R_A22", "sidecar-shell", (((1, 0, 0), "R_A21"),)))
    return table, outputs, tuple(origins)


INITIAL_TABLE, ADAPTER_OUTPUTS, ORIGINS = initial_table_and_outputs()


def raw_from(table):
    extension = c141.replacement_probe.merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    with_direct = c141.replacement_probe.merge_raw(
        base.prefix.FULL_RAW, extension
    )
    return {
        local: values
        for local, values in with_direct.items()
        if local not in direct.DIRECT_ROOT_ROW
    }


FACTOR_SOURCE = dict(base.FACTOR_SOURCE)
FACTOR_OUTPUTS = {
    **base.FACTOR_OUTPUTS,
    **ADAPTER_OUTPUTS,
}
BIND_IGNORED = {
    **base.prefix.payload.IGNORED,
    (-9, -1, 0): frozenset(("B1",)),
}


def records_at(state, index, outputs):
    records = dict(FACTOR_SOURCE)
    records.update({
        site: outputs[site]
        for site, bit in index.items()
        if state >> bit & 1
    })
    return records


def add_variant(table, records, target, outputs, raw):
    output = outputs[target]
    local = c53.local_signature(records, target)
    if not local:
        return False, ("empty", target)
    canonical = cell.canonical(local)
    inherited = raw.get(local)
    if inherited is not None and inherited != frozenset((output,)):
        return False, ("raw-conflict", target, local, inherited, output)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        return False, ("table-conflict", target, canonical, prior, output)
    if inherited == frozenset((output,)) or prior == output:
        return False, ("already-present", target, local, output)
    table[canonical] = output
    return True, (target, output, local)


def next_adapter_variant(records):
    predecessor = JOINT
    for target, output in zip(PATH, ROLES):
        if target in records:
            predecessor = target
            continue
        if predecessor not in records:
            return None
        return target, output
    predecessor = PATH[-2]
    for target, output in SIDECAR_TRUNK:
        if target in records:
            predecessor = target
            continue
        local = c53.local_signature(records, target)
        if predecessor in records and len(local) >= 2:
            return target, output
        return None
    for target, output in SIDECAR_SHELL:
        if target in records:
            continue
        if SIDECAR_TRUNK[-1][0] in records:
            return target, output
        return None
    return None


def main():
    collisions = tuple(sorted(
        (site, base.FACTOR_OUTPUTS[site], ADAPTER_OUTPUTS[site])
        for site in set(base.FACTOR_OUTPUTS) & set(ADAPTER_OUTPUTS)
        if base.FACTOR_OUTPUTS[site] != ADAPTER_OUTPUTS[site]
    ))
    print("ROOT", ROOT, "DIRECT_RAW_REMOVED", len(direct.DIRECT_ROOT_ROW))
    print("COLLISIONS", collisions)
    print("ORIGINS")
    for item in ORIGINS:
        print(item[:3], item[3])

    table = dict(INITIAL_TABLE)
    outputs = dict(FACTOR_OUTPUTS)
    added = []
    for iteration in range(64):
        raw = raw_from(table)
        conflicts = tuple(
            (local, values) for local, values in raw.items() if len(values) != 1
        )
        if conflicts:
            print("RAW_CONFLICTS", conflicts[:3])
            break
        graph = base.compiled_exact_graph(
            FACTOR_SOURCE,
            outputs,
            raw,
            BIND_IGNORED,
            state_limit=5_000_000,
        )
        print(
            "ITER", iteration, "ROWS", len(table), "RAW", len(raw),
            "OUTPUTS", len(outputs), "GRAPH", graph["states"], graph["edges"],
            graph["terminals"], graph["max_frontier"],
            "BAD", graph["bad"][:2], "REACHED", len(graph["reached"]),
        )
        if not graph["bad"]:
            root_mandatory = graph["mandatory"][ROOT]
            root_requires_adapter = all(
                root_mandatory >> graph["index"][site] & 1
                for site in PATH[:-1]
            )
            second_mandatory = graph["mandatory"][SECOND_ROOT]
            second_requires_sidecar = all(
                second_mandatory >> graph["index"][site] & 1
                for site in (
                    ROOT,
                    *(site for site, _output in SIDECAR_TRUNK),
                    SIDECAR_SHELL[0][0],
                )
            )
            print(
                "ROOT_REQUIRES_ALL_ADAPTER", root_requires_adapter,
                "SECOND_REQUIRES_SIDECAR", second_requires_sidecar,
            )
            print("ADDED", added)
            print(
                "RESULT",
                "PHYSICAL_R_B01_CAUSALLY_BOUND_RECURRENT_ROOT"
                if root_requires_adapter and second_requires_sidecar and not collisions
                else "ROOT_BIND_REJECTED",
            )
            return
        failure = graph["failure"]
        if failure is None:
            break
        kind = failure[0]
        if kind == "diamond":
            _, state, left_index, left_target, right_index, right_target = failure
            records = records_at(state, graph["index"], outputs)
            repairs = []
            for written_target, target in (
                (left_target, right_target), (right_target, left_target)
            ):
                after = {**records, written_target: outputs[written_target]}
                okay, detail = add_variant(table, after, target, outputs, raw)
                print("DIAMOND_VARIANT", written_target, "THEN", target, okay, detail)
                if okay:
                    repairs.append(detail)
                elif detail[0] != "already-present":
                    print("ADDED", added)
                    print("RESULT ROOT_BIND_REJECTED")
                    return
            if not repairs:
                print("NO_NEW_DIAMOND_REPAIR")
                break
            added.extend(repairs)
            continue
        if kind == "dead":
            state = failure[1]
            records = records_at(state, graph["index"], outputs)
            variant = next_adapter_variant(records)
            if variant is None:
                print("DEAD_WITH_NO_READY_ADAPTER")
                print("MISSING_OUTPUT_LOCALS")
                for target in sorted(outputs):
                    if target in records:
                        continue
                    local = c53.local_signature(records, target)
                    print(target, outputs[target], local, raw.get(local))
                break
            target, output = variant
            okay, detail = add_variant(table, records, target, outputs, raw)
            print("DEAD_VARIANT", okay, detail)
            if not okay:
                break
            added.append(detail)
            continue
        if kind == "wrong":
            print("WRONG", failure[2])
            state = failure[1]
            records = records_at(state, graph["index"], outputs)
            for target, values in failure[2]:
                print("WRONG_LOCAL", target, values, c53.local_signature(records, target))
            break
        print("UNHANDLED_FAILURE", failure)
        break
    print("ADDED", added)
    print("RESULT ROOT_BIND_REJECTED")


if __name__ == "__main__":
    main()
