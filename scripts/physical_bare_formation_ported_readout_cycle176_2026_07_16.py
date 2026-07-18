#!/usr/bin/env python3
"""Cycle 176: bare two-witness formation followed by ported row readout.

A signed-row record first forms at a genuinely bare exterior site from two
matching opposite physical witnesses.  Only after that record exists does an
ordinary retained row cable carry it into Cycle 173's frozen cable-fed P
interface, whose exterior comb decodes the row for a complete signed
membership apparatus.

This is a finite formation-then-readout probe under the current candidate
local law.  It is not yet a two-stage Cycle-166 stabilizer update, a universal
record-formation theorem, a probability result, or axiom language.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import physical_serial_repeat_measurement_cycle174_2026_07_16 as c174
import shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16 as c173


Coord = tuple[int, int, int]
Row = tuple[int, int, int, int, int]

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BARE_FORMATION_PORTED_READOUT_CYCLE176_NOTE_2026-07-16.md"
)
CYCLE173_SCRIPT = (
    ROOT / "scripts/shared_ancestry_dual_context_peres_mermin_cycle173_2026_07_16.py"
)
CYCLE173_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SHARED_ANCESTRY_DUAL_CONTEXT_PERES_MERMIN_CYCLE173_NOTE_2026-07-16.md"
)
CYCLE174_SCRIPT = (
    ROOT / "scripts/physical_serial_repeat_measurement_cycle174_2026_07_16.py"
)
CYCLE174_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SERIAL_REPEAT_MEASUREMENT_CYCLE174_NOTE_2026-07-16.md"
)

FROZEN_CYCLE173_SCRIPT_SHA = (
    "92afd28e4cf8b36b98b90b8cf919e13052716a056c64377396da304cb42acc11"
)
FROZEN_CYCLE173_NOTE_SHA = (
    "6c241e3f19dace1c67ed48199c04627d446dff64c01f4dde0c8ae76be37d0cc4"
)
FROZEN_CYCLE174_SCRIPT_SHA = (
    "efa8b0f98b9a8f270089b02bffcb5b475ecb7d636cc34750836e7fb3df996dea"
)
FROZEN_CYCLE174_NOTE_SHA = (
    "c381223ec044cd18bda22e2a167163486c1e33bb8c5c184c7fa452b93d282459"
)

ZI: Row = c173.ZI
IZ: Row = c173.IZ
ZZ: Row = c173.ZZ
EXTERIOR_DISTANCE = 80
ROTATION_SHIFT: Coord = (8_009, -8_021, 8_027)

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return c173.add(left, right)


def formation_records(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
) -> dict[Coord, str]:
    records = {
        neighbor: initial[neighbor]
        for direction in c173.c169.c53.DIRECTIONS
        if (neighbor := add(target, direction)) in initial
    }
    records.update(
        {
            parent: expected[parent]
            for parent in dependencies[target]
            if parent in expected
        }
    )
    return records


@dataclass(frozen=True)
class FormationReadout:
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    source: Coord
    witnesses: tuple[Coord, Coord]
    path: tuple[Coord, ...]
    p_input: Coord
    comb_root: Coord
    payload_first: Coord
    payload_guard: Coord
    payload_decoder: Coord
    output: Coord
    role: str
    removed_cage: frozenset[Coord]
    added_furniture: frozenset[Coord]


def unique_fixed_guard(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
    excluded: frozenset[Coord],
) -> Coord:
    premise = formation_records(initial, expected, dependencies, target)
    wanted = expected[target]
    candidates = tuple(
        site
        for site in premise
        if site in initial and site not in excluded
    )
    for site in candidates:
        trial = dict(premise)
        trial.pop(site)
        actual = c174.MERGED_RAW.get(
            c173.c169.c53.local_signature(trial, target),
            frozenset(),
        )
        if wanted not in actual:
            return site
    raise ValueError(("no-load-bearing-fixed-guard", target, candidates))


@lru_cache(maxsize=1)
def apparatus() -> FormationReadout:
    context = c173.context_instance(
        "formation-readout",
        (IZ, ZZ),
        ZI,
        (0, 0, 0),
    )
    plan = c173.ported_plan()
    role = c173.c169.joint.pivot.five.ROW_ROLE[ZI]
    source = add(context.p_input, (-EXTERIOR_DISTANCE, 0, 0))
    path = tuple(
        (x, context.p_input[1], context.p_input[2])
        for x in range(source[0], context.p_input[0] + 1)
    )
    if path[0] != source or path[-1] != context.p_input:
        raise ValueError(("bad-exterior-path", source, context.p_input))

    interface_closed = {
        neighbor
        for site in path
        for neighbor in (
            site,
            *(add(site, direction) for direction in c173.c169.c53.DIRECTIONS),
        )
    }
    opened_cage = context.removable_cage & interface_closed
    initial = dict(context.initial)
    for site in opened_cage:
        initial.pop(site, None)
    before_route = set(initial)

    witness_plus = add(source, c173.EZ)
    witness_minus = add(source, c173.NEG_EZ)
    protected = frozenset(
        set(context.expected)
        | set(context.source_sites.values())
        | set(path)
        | {source, witness_plus, witness_minus}
    )
    routed, _outputs, ports = c173.c169.greedy_path_core(
        ((role, path),),
        constraints=initial,
        extra_protected=protected,
    )
    comb_root = add(context.p_input, c173.EX)
    if ports != frozenset((comb_root,)):
        raise ValueError(("wrong-ported-terminal", ports, comb_root))
    for site in path:
        routed.pop(site, None)
    initial = routed
    added_furniture = frozenset(set(initial) - before_route)

    c173.place(initial, witness_plus, role, "positive-row-witness")
    c173.place(initial, witness_minus, role, "negative-row-witness")

    expected = dict(context.expected)
    dependencies = dict(context.dependencies)
    expected[source] = role
    dependencies[source] = frozenset()
    for previous, target in zip(path, path[1:]):
        prior = expected.get(target)
        if prior is not None and prior != role:
            raise ValueError(("path-expected-conflict", target, prior, role))
        expected[target] = role
        dependencies[target] = frozenset((previous,))

    # Cage only outside the closed support of the new dynamic interface.
    # The six nearest-neighbor sites of the bare source are in external_core,
    # so this shell cannot silently fill the four faces that must remain open.
    interface_dynamic = set(path)
    protected_closed = set(expected) | {
        add(site, direction)
        for site in expected
        for direction in c173.c169.c53.DIRECTIONS
    }
    external_records = set(added_furniture) | {witness_plus, witness_minus}
    external_core = (
        external_records
        | interface_dynamic
        | {
            add(site, direction)
            for site in interface_dynamic
            for direction in c173.c169.c53.DIRECTIONS
        }
    )
    external_cage = {
        add(site, direction)
        for site in external_core
        for direction in c173.c169.c53.DIRECTIONS
        if (
            add(site, direction) not in external_core
            and add(site, direction) not in protected_closed
        )
    }
    for site in external_cage:
        if site not in expected:
            c173.place(initial, site, c173.FRAME, "external-interface-cage")
    for site in expected:
        initial.pop(site, None)

    payload_first = add(comb_root, c173.EY)
    payload_decoder = add(comb_root, c173.c169.scale(11, c173.EY))
    if plan.expected_specs.get(add(plan.p_input, c173.EX)) != ("row", "p"):
        raise ValueError("Cycle-173 root contract drift")
    payload_guard = unique_fixed_guard(
        initial,
        expected,
        dependencies,
        payload_first,
        frozenset((comb_root,)),
    )

    return FormationReadout(
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        source=source,
        witnesses=(witness_plus, witness_minus),
        path=path,
        p_input=context.p_input,
        comb_root=comb_root,
        payload_first=payload_first,
        payload_guard=payload_guard,
        payload_decoder=payload_decoder,
        output=context.output_site,
        role=role,
        removed_cage=frozenset(opened_cage),
        added_furniture=added_furniture,
    )


def enabled(
    records: dict[Coord, str],
) -> dict[Coord, frozenset[str]]:
    return {
        target: c174.MERGED_RAW[signature]
        for target in c173.c169.c53.open_candidates(records)
        if (
            signature := c173.c169.c53.local_signature(records, target)
        ) in c174.MERGED_RAW
    }


def children_map(
    dependencies: dict[Coord, frozenset[Coord]],
) -> dict[Coord, tuple[Coord, ...]]:
    children: dict[Coord, list[Coord]] = defaultdict(list)
    for child, parents in dependencies.items():
        for parent in parents:
            children[parent].append(child)
    return {
        parent: tuple(sorted(values))
        for parent, values in children.items()
    }


def descendants(
    dependencies: dict[Coord, frozenset[Coord]],
    starts: set[Coord],
) -> frozenset[Coord]:
    children = children_map(dependencies)
    seen = set(starts)
    queue = deque(starts)
    while queue:
        parent = queue.popleft()
        for child in children.get(parent, ()):
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return frozenset(seen)


def schedule(
    dependencies: dict[Coord, frozenset[Coord]],
    order: str,
) -> tuple[Coord, ...]:
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
    result = []
    while frontier:
        target = min(frontier) if order == "min" else max(frontier)
        frontier.remove(target)
        result.append(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
    if len(result) != len(dependencies):
        raise ValueError(("dependency-cycle", len(result), len(dependencies)))
    return tuple(result)


@lru_cache(maxsize=1)
def initial_enabled() -> dict[Coord, frozenset[str]]:
    return enabled(apparatus().initial)


def local_compiled_check(
    instance: FormationReadout,
    *,
    rotation=None,
) -> tuple[int, tuple[object, ...]]:
    if rotation is None:
        initial = instance.initial
        expected = instance.expected
        dependencies = instance.dependencies
    else:
        transform = lambda site: add(
            c173.c169.c53.matvec(rotation, site),
            ROTATION_SHIFT,
        )
        initial = {
            transform(site): role
            for site, role in instance.initial.items()
        }
        expected = {
            transform(site): role
            for site, role in instance.expected.items()
        }
        dependencies = {
            transform(site): frozenset(transform(parent) for parent in parents)
            for site, parents in instance.dependencies.items()
        }

    failures = []
    checks = 0
    for target, role in expected.items():
        premise = {
            neighbor: initial[neighbor]
            for direction in c173.c169.c53.DIRECTIONS
            if (neighbor := add(target, direction)) in initial
        }
        premise.update(
            {
                parent: expected[parent]
                for parent in dependencies[target]
            }
        )
        actual = c174.MERGED_RAW.get(
            c173.c169.c53.local_signature(premise, target),
            frozenset(),
        )
        checks += 1
        if actual != frozenset((role,)):
            failures.append((target, role, actual, dependencies[target]))
            if len(failures) >= 10:
                break
    return checks, tuple(failures)


def dynamic_edge_checks(
    instance: FormationReadout,
) -> tuple[int, tuple[object, ...]]:
    attempts = 0
    failures = []
    for target, parents in instance.dependencies.items():
        premise = formation_records(
            instance.initial,
            instance.expected,
            instance.dependencies,
            target,
        )
        wanted = instance.expected[target]
        for parent in parents:
            attempts += 1
            trial = dict(premise)
            trial.pop(parent)
            actual = c174.MERGED_RAW.get(
                c173.c169.c53.local_signature(trial, target),
                frozenset(),
            )
            if wanted in actual:
                failures.append((target, parent, wanted, actual))
                if len(failures) >= 10:
                    return attempts, tuple(failures)
    return attempts, tuple(failures)


def physical_run(
    instance: FormationReadout,
    *,
    order: str,
) -> tuple[bool, object]:
    records = dict(instance.initial)
    actual = dict(initial_enabled())
    linear = schedule(instance.dependencies, order)
    children = children_map(instance.dependencies)
    pending = {
        site: len(parents)
        for site, parents in instance.dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
    formed: set[Coord] = set()
    maximum = 0
    work = 0
    for target in linear:
        wanted = {
            site: frozenset((instance.expected[site],))
            for site in frontier
        }
        maximum = max(maximum, len(frontier))
        work += len(frontier)
        if actual != wanted:
            return False, (
                "frontier",
                len(formed),
                tuple(sorted(set(actual) - set(wanted)))[:5],
                tuple(sorted(set(wanted) - set(actual)))[:5],
            )
        records[target] = instance.expected[target]
        formed.add(target)
        frontier.remove(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
        actual.pop(target, None)
        for direction in c173.c169.c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c173.c169.c53.local_signature(records, candidate)
            values = c174.MERGED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values
    return (
        not actual
        and records.get(instance.source) == instance.role
        and records.get(instance.p_input) == instance.role
        and records.get(instance.output) == c173.H1,
        {
            "initial": len(instance.initial),
            "dynamic": len(instance.expected),
            "work": work,
            "maximum": maximum,
            "source": records.get(instance.source),
            "p_input": records.get(instance.p_input),
            "output": records.get(instance.output),
            "residual": tuple(sorted(actual.items())),
        },
    )


def witness_local_controls(
    instance: FormationReadout,
) -> tuple[tuple[Coord, frozenset[str]], ...]:
    results = []
    premise = formation_records(
        instance.initial,
        instance.expected,
        instance.dependencies,
        instance.source,
    )
    for witness in instance.witnesses:
        trial = dict(premise)
        trial.pop(witness)
        actual = c174.MERGED_RAW.get(
            c173.c169.c53.local_signature(trial, instance.source),
            frozenset(),
        )
        results.append((witness, actual))
    return tuple(results)


def pruned_physical_run(
    instance: FormationReadout,
    *,
    removed_initial: Coord,
    cut: Coord,
    source_expected: bool,
    p_input_expected: bool,
    output_expected: bool,
    full_rescan_control: bool = False,
) -> tuple[bool, object]:
    removed = descendants(instance.dependencies, {cut})
    expected = {
        site: role
        for site, role in instance.expected.items()
        if site not in removed
    }
    dependencies = {
        site: parents
        for site, parents in instance.dependencies.items()
        if site not in removed
    }
    if any(not parents <= expected.keys() for parents in dependencies.values()):
        return False, ("uncollapsed-descendant-cut", cut)

    records = dict(instance.initial)
    records.pop(removed_initial, None)
    actual = dict(initial_enabled())
    affected = {removed_initial} | {
        add(removed_initial, direction)
        for direction in c173.c169.c53.DIRECTIONS
    }
    for candidate in affected:
        if candidate in records or not any(
            add(candidate, direction) in records
            for direction in c173.c169.c53.DIRECTIONS
        ):
            actual.pop(candidate, None)
            continue
        signature = c173.c169.c53.local_signature(records, candidate)
        values = c174.MERGED_RAW.get(signature)
        if values is None:
            actual.pop(candidate, None)
        else:
            actual[candidate] = values

    rescan_equivalent = None
    if full_rescan_control:
        rescanned = enabled(records)
        rescan_equivalent = actual == rescanned
        if not rescan_equivalent:
            return False, (
                "local-reseed-mismatch",
                tuple(sorted(set(actual) - set(rescanned)))[:5],
                tuple(sorted(set(rescanned) - set(actual)))[:5],
            )

    linear = schedule(dependencies, "min")
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {site for site, count in pending.items() if count == 0}
    for step, target in enumerate(linear):
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        if actual != wanted:
            return False, (
                "frontier",
                step,
                tuple(sorted(set(actual) - set(wanted)))[:5],
                tuple(sorted(set(wanted) - set(actual)))[:5],
            )
        records[target] = expected[target]
        frontier.remove(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
        actual.pop(target, None)
        for direction in c173.c169.c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c173.c169.c53.local_signature(records, candidate)
            values = c174.MERGED_RAW.get(signature)
            if values is None:
                actual.pop(candidate, None)
            else:
                actual[candidate] = values

    observed = (
        instance.source in records,
        instance.p_input in records,
        instance.output in records,
    )
    wanted_observed = (
        source_expected,
        p_input_expected,
        output_expected,
    )
    return (
        not actual and observed == wanted_observed,
        {
            "removed": len(removed),
            "remaining": len(expected),
            "observed": observed,
            "wanted": wanted_observed,
            "rescan_equivalent": rescan_equivalent,
            "residual": tuple(sorted(actual.items())),
        },
    )


def causal_certificate(
    instance: FormationReadout,
) -> dict[str, object]:
    children = children_map(instance.dependencies)
    pending = {
        site: len(parents)
        for site, parents in instance.dependencies.items()
    }
    frontier = deque(sorted(site for site, count in pending.items() if count == 0))
    depth: dict[Coord, int] = {}
    profile: Counter[int] = Counter()
    while frontier:
        site = frontier.popleft()
        parents = instance.dependencies[site]
        value = (
            1 + max(depth[parent] for parent in parents)
            if parents
            else 1
        )
        depth[site] = value
        profile[value] += 1
        for child in children.get(site, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.append(child)
    if len(depth) != len(instance.expected):
        raise ValueError(("causal-cycle", len(depth), len(instance.expected)))
    return {
        "depth": max(depth.values()),
        "source": depth[instance.source],
        "p_input": depth[instance.p_input],
        "comb_root": depth[instance.comb_root],
        "payload_first": depth[instance.payload_first],
        "payload_decoder": depth[instance.payload_decoder],
        "output": depth[instance.output],
        "edges": sum(map(len, instance.dependencies.values())),
        "roots": sum(not parents for parents in instance.dependencies.values()),
        "profile_hash": hashlib.sha256(
            ",".join(
                str(profile[index])
                for index in range(1, max(profile) + 1)
            ).encode("utf-8")
        ).hexdigest(),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN AUTHORITY AND LAW")
    check(
        "Cycle 173 frozen runner and note hashes match",
        sha256(CYCLE173_SCRIPT) == FROZEN_CYCLE173_SCRIPT_SHA
        and sha256(CYCLE173_NOTE) == FROZEN_CYCLE173_NOTE_SHA,
        (sha256(CYCLE173_SCRIPT), sha256(CYCLE173_NOTE)),
    )
    check(
        "Cycle 174 frozen runner and note hashes match",
        sha256(CYCLE174_SCRIPT) == FROZEN_CYCLE174_SCRIPT_SHA
        and sha256(CYCLE174_NOTE) == FROZEN_CYCLE174_NOTE_SHA,
        (sha256(CYCLE174_SCRIPT), sha256(CYCLE174_NOTE)),
    )
    check(
        "the only law delta is the clean 96-row ingress",
        len(c173.c169.UNIFIED_RAW) == 101_708
        and len(c174.INGRESS_RAW) == 96
        and set(c173.c169.UNIFIED_RAW).isdisjoint(c174.INGRESS_RAW)
        and len(c174.MERGED_RAW) == 101_804
        and not c174.RAW_CONFLICTS,
        (
            len(c173.c169.UNIFIED_RAW),
            len(c174.INGRESS_RAW),
            len(c174.MERGED_RAW),
            len(c174.RAW_CONFLICTS),
        ),
    )

    print("\nFORMATION-THEN-READOUT GEOMETRY")
    instance = apparatus()
    source_neighbors = {
        direction: instance.initial.get(add(instance.source, direction))
        for direction in c173.c169.c53.DIRECTIONS
    }
    check(
        "the exterior source is genuinely bare except for its two row witnesses",
        source_neighbors[c173.EZ] == instance.role
        and source_neighbors[c173.NEG_EZ] == instance.role
        and all(
            source_neighbors[direction] is None
            for direction in (
                c173.EX,
                c173.NEG_EX,
                c173.EY,
                c173.NEG_EY,
            )
        ),
        source_neighbors,
    )
    p_neighbors = {
        direction: instance.initial.get(add(instance.p_input, direction))
        for direction in c173.c169.c53.DIRECTIONS
    }
    check(
        "the frozen Cycle-173 input remains cable-fed with its functional MARK pair",
        p_neighbors[c173.EY] == c173.FRAME
        and p_neighbors[c173.NEG_EY] == c173.FRAME
        and instance.path[-1] == instance.p_input
        and add(instance.p_input, c173.EX) == instance.comb_root,
        p_neighbors,
    )
    check(
        "ordinary transport bridges the bare source to the exact frozen comb port",
        len(instance.path) == EXTERIOR_DISTANCE + 1
        and instance.path[0] == instance.source
        and instance.path[-1] == instance.p_input
        and len(instance.removed_cage) == 5
        and instance.added_furniture,
        {
            "path_sites": len(instance.path),
            "removed_cage": len(instance.removed_cage),
            "added_furniture": len(instance.added_furniture),
        },
    )

    print("\nLOCAL LAW, CAUSAL ORDER, AND EDGE LOAD")
    local_checks, local_failures = local_compiled_check(instance)
    check(
        "every declared formation and readout site compiles exactly",
        local_checks == len(instance.expected) and not local_failures,
        (local_checks, local_failures[:2]),
    )
    witness_controls = witness_local_controls(instance)
    check(
        "either witness deletion suppresses source formation locally",
        len(witness_controls) == 2
        and all(not actual for _site, actual in witness_controls),
        witness_controls,
    )
    edge_attempts, edge_failures = dynamic_edge_checks(instance)
    check(
        "every declared dynamic parent edge is load-bearing",
        edge_attempts == sum(map(len, instance.dependencies.values()))
        and not edge_failures,
        (edge_attempts, edge_failures[:2]),
    )
    causal = causal_certificate(instance)
    check(
        "causal depth orders witnesses before source, cable, splitter, decoder, and output",
        causal["source"] == 1
        and causal["p_input"] == len(instance.path)
        and causal["comb_root"] == len(instance.path) + 1
        and causal["payload_first"] == len(instance.path) + 2
        and causal["payload_decoder"] > causal["payload_first"]
        and causal["output"] > causal["payload_decoder"],
        causal,
    )

    print("\nFULL PHYSICAL REPLAYS")
    minimum = physical_run(instance, order="min")
    maximum = physical_run(instance, order="max")
    check(
        "minimum and maximum schedules close physically and terminally",
        minimum[0] and maximum[0],
        {"min": minimum, "max": maximum},
    )

    print("\nWITNESS AND PAYLOAD DELETIONS")
    witness_plus = pruned_physical_run(
        instance,
        removed_initial=instance.witnesses[0],
        cut=instance.source,
        source_expected=False,
        p_input_expected=False,
        output_expected=False,
        full_rescan_control=True,
    )
    witness_minus = pruned_physical_run(
        instance,
        removed_initial=instance.witnesses[1],
        cut=instance.source,
        source_expected=False,
        p_input_expected=False,
        output_expected=False,
    )
    payload = pruned_physical_run(
        instance,
        removed_initial=instance.payload_guard,
        cut=instance.payload_first,
        source_expected=True,
        p_input_expected=True,
        output_expected=False,
    )
    check(
        "the optimized witness-deletion reseed equals a global open-candidate rescan",
        witness_plus[0]
        and isinstance(witness_plus[1], dict)
        and witness_plus[1]["rescan_equivalent"] is True,
        witness_plus,
    )
    check(
        "removing either source witness stalls formation and all downstream readout",
        witness_plus[0] and witness_minus[0],
        {"plus": witness_plus, "minus": witness_minus},
    )
    check(
        "removing only the payload branch leaves source and port formation intact",
        payload[0]
        and isinstance(payload[1], dict)
        and payload[1]["observed"] == (True, True, False),
        {
            "payload_guard": instance.payload_guard,
            "payload_first": instance.payload_first,
            "payload_decoder": instance.payload_decoder,
            "result": payload,
        },
    )

    print("\nPROPER-CUBIC COVARIANCE")
    rotation_checks = 0
    rotation_failures = []
    base_sites = set(instance.initial) | set(instance.expected)
    for rotation_index, rotation in enumerate(c173.c169.c53.ROTATIONS):
        transformed = {
            add(c173.c169.c53.matvec(rotation, site), ROTATION_SHIFT)
            for site in base_sites
        }
        checks, failures = local_compiled_check(instance, rotation=rotation)
        rotation_checks += checks
        if len(transformed) != len(base_sites) or failures:
            rotation_failures.append(
                (rotation_index, len(transformed), failures[:2])
            )
    check(
        "all 24 proper-cubic labeled graphs compile by exact isomorphism",
        rotation_checks == 24 * len(instance.expected)
        and not rotation_failures,
        (rotation_checks, rotation_failures[:2]),
    )

    print("\nSCOPE")
    normalized = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "formation then readout",
        "not yet a two-stage cycle-166 stabilizer update",
        "two matching physical witnesses",
        "payload-only deletion",
        "does not choose axiom language",
        "no axiom, primitive, registry, policy, or audit edit follows",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check("the note keeps the exact constitutional boundary", not missing, missing)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "BARE_FORMATION_THEN_PORTED_READOUT" if FAIL == 0 else "FAIL",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
