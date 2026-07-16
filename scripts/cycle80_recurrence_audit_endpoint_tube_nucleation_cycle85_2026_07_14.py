#!/usr/bin/env python3
"""Cycle 85: audit Cycle 80 and attach it to the live Cycle-78 endpoint.

The runner independently certifies Cycle 80's scoped 17-site lower bound and
replaces bounded-horizon evidence by a finite strict-NN/period-three induction
quotient.  It then corrects Cycle 80's stale Cycle-75/Cycle-72 composition and
constructs a no-supplied-record bridge from the current live-safe Cycle-78
terminal to one transformed A layer.  An existing joint-endpoint D1 record is
the rear cap.  The launcher has every bridge record in its mandatory ancestry.

Authority: none.  No foundation, registry, or selected-law status follows.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import numpy as np

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import cycle60_cycle67_mixed_composition_audit_cycle70_2026_07_14 as c70
import cycle67_terminal_bdh_rebind_cycle72_2026_07_14 as c72
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import joint_endpoint_mixed_rebind_cycle78_2026_07_14 as c78
import mixed_cycle72_guide_repair_cycle77_2026_07_14 as c77
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import seven_bit_physical_role_comparator_cycle75_2026_07_14 as c75
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CYCLE80_RECURRENCE_AUDIT_ENDPOINT_TUBE_NUCLEATION_CYCLE85_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

# Standard tube coordinates are sent by R to physical coordinates and shifted.
# R(x,y,z)=(-z,x,-y); the tube grows in physical +y from the endpoint boundary.
ROTATION = c53.ROTATIONS[11]
SHIFT: Coord = (3, 4, 1)
CAP: Coord = (2, 3, 0)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def transform(site: Coord) -> Coord:
    return c53.add(c53.matvec(ROTATION, site), SHIFT)


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def transformed_layer(x: int, phase: str) -> dict[Coord, str]:
    return {transform(site): output for site, output in c80.layer(x, phase).items()}


# The nine T_* records are finite bridge guides.  The A roles themselves are
# Cycle 80's exact physical roles.  The displayed order only defines the rows;
# the exact graph below keeps every row live from state zero.
BRIDGE_ROWS: tuple[tuple[str, Coord | tuple[int, int], str | None], ...] = (
    ("N1", (3, 3, 1), "T_N1"),
    ("N2", (2, 3, -1), "T_N2"),
    ("H0", (3, 2, -1), "T_H0"),
    ("H1", (3, 3, -1), "T_H1"),
    ("H2", (3, 3, -2), "T_H2"),
    ("H3", (3, 3, -3), "T_H3"),
    ("A02", (0, 2), None),
    ("A12", (1, 2), None),
    ("A13", (1, 3), None),
    ("A23", (2, 3), None),
    ("G0", (1, 3, -1), "T_G0"),
    ("G1", (1, 3, -2), "T_G1"),
    ("N0", (0, 3, -2), "T_N0"),
    ("A33", (3, 3), None),
    ("A32", (3, 2), None),
    ("A22", (2, 2), None),
    ("A21", (2, 1), None),
    ("A31", (3, 1), None),
    ("A41", (4, 1), None),
    ("A40", (4, 0), None),
    ("A30", (3, 0), None),
    ("A20", (2, 0), None),
    ("A10", (1, 0), None),
    ("A00", (0, 0), None),
    ("A01", (0, 1), None),
    ("LA", (1, 1), None),
)


@dataclass(frozen=True)
class Bridge:
    source: dict[Coord, str]
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    aliases: dict[str, tuple[Coord, ...]]
    parents: dict[Coord, frozenset[Coord]]
    must: dict[Coord, frozenset[Coord]]
    union_with_recurrence: dict[Signature, str]


def bridge_target(position: Coord | tuple[int, int]) -> Coord:
    if len(position) == 2:
        y, z = position
        return transform((0, y, z))
    return position  # type: ignore[return-value]


def bridge_output(position: Coord | tuple[int, int], supplied: str | None) -> str:
    if supplied is not None:
        return supplied
    y, z = position
    return c80.role("A", y, z)


def build_bridge() -> Bridge:
    source = {**c78.CONSTRUCTION.source, **c78.CONSTRUCTION.allowed}
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    aliases: dict[str, tuple[Coord, ...]] = {}
    parents: dict[Coord, frozenset[Coord]] = {}

    for name, position, supplied in BRIDGE_ROWS:
        target = bridge_target(position)
        output = bridge_output(position, supplied)
        raw_signature = c53.local_signature(records, target)
        signature = c53.canonical_signature(raw_signature)
        sites = tuple(c53.signature_classes(records).get(signature, ()))
        if sites != (target,):
            raise ValueError(f"non-singleton bridge stage {name}: {sites}")
        prior = table.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"bridge conflict {name}: {prior}/{output}")
        table[signature] = output
        aliases[name] = sites
        parents[target] = frozenset(
            neighbour
            for direction, _ in raw_signature
            if (neighbour := c53.add(target, direction)) in allowed
        )
        allowed[target] = output
        records[target] = output

    must: dict[Coord, frozenset[Coord]] = {
        site: frozenset((site,)) for site in allowed
    }
    for _ in range(len(allowed) + 1):
        updated = {
            site: frozenset(
                {site}.union(*(must[parent] for parent in parents[site]))
            )
            for site in allowed
        }
        if updated == must:
            must = updated
            break
        must = updated
    else:
        raise RuntimeError("bridge ancestry did not converge")

    union = dict(c78.CONSTRUCTION.union_table)
    for component in (table, c80.CONSTRUCTION.table):
        for signature, output in component.items():
            prior = union.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"composed canonical conflict: {prior}/{output}")
            union[signature] = output
    return Bridge(source, table, allowed, aliases, parents, must, union)


BRIDGE = build_bridge()


def composite_construction() -> c77.Construction:
    """Cycle-67 terminal -> live Cycle-78 endpoint -> Cycle-85 A boundary."""

    new_table = dict(c78.CONSTRUCTION.new_table)
    new_table.update(BRIDGE.table)
    union = dict(c78.CONSTRUCTION.union_table)
    union.update(BRIDGE.table)
    allowed = {**c78.CONSTRUCTION.allowed, **BRIDGE.allowed}
    aliases = dict(c78.CONSTRUCTION.stage_aliases)
    aliases.update({f"TUBE_{name}": sites for name, sites in BRIDGE.aliases.items()})
    return c77.Construction(
        c78.CONSTRUCTION.source, new_table, union, allowed, aliases
    )


def big_downstream_availability(
    states: tuple[int, ...],
    phase_availability: c70.Availability,
    model: c77.DownModel,
) -> c77.DownAvailability:
    """Cycle-77 availability with Python big-int masks beyond 64 records."""

    comb_sites = tuple(sorted(c60.CONSTRUCTION.allowed))
    comb_index = {site: bit for bit, site in enumerate(comb_sites)}
    phase_index = phase_availability.phase_index
    metadata = []
    for site in model.sites:
        parent = model.parents[site]
        metadata.append((
            sum(1 << comb_index[item] for item in parent.comb),
            sum(1 << phase_index[item] for item in parent.phase),
            sum(1 << model.index[item] for item in parent.downstream),
        ))

    ids = np.empty(len(states), dtype=np.uint16)
    masks: list[int] = []
    unique: list[int] = []
    mask_ids: dict[int, int] = {}
    for state_index, comb_mask in enumerate(states):
        phase_mask = phase_availability.availability_masks[
            int(phase_availability.availability_ids[state_index])
        ]
        down_mask = 0
        for bit, (comb_required, phase_required, down_required) in enumerate(metadata):
            if (
                comb_mask & comb_required == comb_required
                and phase_mask & phase_required == phase_required
                and down_mask & down_required == down_required
            ):
                down_mask |= 1 << bit
        if down_mask not in mask_ids:
            mask_ids[down_mask] = len(unique)
            unique.append(down_mask)
        masks.append(down_mask)
        ids[state_index] = mask_ids[down_mask]
    return c77.DownAvailability(
        np.array(masks, dtype=object), ids, tuple(unique)
    )


def transverse_neighbours(site: tuple[int, int]) -> frozenset[tuple[int, int]]:
    y, z = site
    return frozenset(((y + 1, z), (y - 1, z), (y, z + 1), (y, z - 1)))


def scoped_launcher_neighbour_minimum() -> tuple[int, int]:
    """Exact three-launcher cage bound after fixing one launcher at zero.

    If the union had fewer than eight opposite-colour neighbours, the overlap
    graph of the three degree-four neighbourhoods would have to be connected.
    Same-colour square-lattice vertices overlap only within L1 distance two;
    hence every connected triple lies within L1 distance four of the anchor.
    The finite [-4,4]^2 enumeration is therefore exhaustive.
    """

    anchor = (0, 0)
    candidates = tuple(
        (y, z)
        for y in range(-4, 5)
        for z in range(-4, 5)
        if (y + z) % 2 == 0 and (y, z) != anchor
    )
    minimum = 10**9
    minimizers = 0
    for left, right in combinations(candidates, 2):
        union = set().union(*(
            transverse_neighbours(site) for site in (anchor, left, right)
        ))
        if len(union) < minimum:
            minimum = len(union)
            minimizers = 1
        elif len(union) == minimum:
            minimizers += 1
    return minimum, minimizers


def window_graph(phase: str) -> c63.ExactGraph:
    """Four completed layers plus cap, followed by one exhaustive layer."""

    phases = [phase]
    for _ in range(3):
        phases.append(c80.PREVIOUS[phases[-1]])
    base: dict[Coord, str] = {}
    for offset, layer_phase in enumerate(phases):
        base.update(c80.layer(-offset, layer_phase))
    oldest = phases[-1]
    base[(-4, *c80.LAUNCH[oldest])] = "Z0"
    return c63.exact_graph(
        base, c80.CONSTRUCTION.table, c80.layer(1, c80.NEXT[phase])
    )


def completed_tube_enabled(horizon: int) -> dict[Coord, frozenset[str]]:
    records = {**c80.layer(0, "A"), (-1, *c80.LAUNCH["A"]): "Z0"}
    for x in range(1, horizon + 1):
        records.update(c80.layer(x, c80.PHASES[x % 3]))
    raw = c70.raw_outputs(c80.CONSTRUCTION.table)
    return {
        target: raw[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in raw
    }


def recurrence_phase_parent_contract() -> bool:
    """Nonseed rows cannot create the first record of a new phase."""

    for signature, output in c80.CONSTRUCTION.table.items():
        output_phase = next(
            phase for phase in c80.PHASES
            if output in set(c80.layer(0, phase).values())
        )
        seed_output = c80.role(output_phase, *c80.SEED[output_phase])
        values = {content for _, content in signature}
        if output == seed_output:
            if len(signature) != 1:
                return False
        elif not values.intersection(c80.layer(0, output_phase).values()):
            return False
    return True


def role_inventory(table: dict[Signature, str], source: dict[Coord, str]) -> set[str]:
    return (
        set(table.values())
        | {content for signature in table for _, content in signature}
        | set(source.values())
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A03 Cycle 80 baseline runner remains internally green", len(c80.CONSTRUCTION.table) == 51 and len(c70.raw_outputs(c80.CONSTRUCTION.table)) == 1_170)

    minimum, minimizers = scoped_launcher_neighbour_minimum()
    colour_counts = {
        parity: sum((y + z) % 2 == parity for y, z in c80.CROSS_SECTION)
        for parity in (0, 1)
    }
    launcher_neighbours = set().union(*(
        transverse_neighbours(c80.LAUNCH[phase]) for phase in c80.PHASES
    ))
    check("B01 exact connected-triple enumeration gives eight opposite-colour neighbours", minimum == 8, str((minimum, minimizers)))
    check("B02 Cycle-80 launcher triple attains the eight-neighbour bound", len(launcher_neighbours) == 8)
    check("B03 footprint has the forced 9:8 bipartite census", colour_counts == {0: 9, 1: 8}, str(colour_counts))
    check("B04 all three phase paths have same-colour launcher endpoints", all((sum(c80.SEED[p]) - sum(c80.LAUNCH[p])) % 2 == 0 for p in c80.PHASES))
    check("B05 scoped lower bound is exactly 2*8+1=17 and is attained", len(c80.CROSS_SECTION) == 2 * minimum + 1 == 17)

    check("C01 every Cycle-80 rule is strict nearest-neighbour", all(offset in c53.DIRECTIONS for signature in c80.CONSTRUCTION.table for offset, _ in signature))
    for phase in c80.PHASES:
        graph = window_graph(phase)
        following = c80.NEXT[phase]
        after = c80.NEXT[following]
        expected = ((2, *c80.SEED[after]), c80.role(after, *c80.SEED[after]))
        check(f"C{phase}2 four-layer induction window is 18 states / 18 edges", (graph.conditions, len(graph.states), graph.edges) == (18, 18, 18), str((graph.conditions, len(graph.states), graph.edges)))
        check(f"C{phase}3 window reaches the complete next layer", (1 << 17) - 1 in graph.states)
        check(f"C{phase}4 only the exact following seed crosses the window", graph.parasites == frozenset((expected,)), str(graph.parasites))
        check(f"C{phase}5 induction window has no conflict or dead terminal", not graph.conflicts and not graph.terminals)
    for horizon in (6, 7, 8):
        phase = c80.PHASES[(horizon + 1) % 3]
        expected = {
            (horizon + 1, *c80.SEED[phase]): frozenset((
                c80.role(phase, *c80.SEED[phase]),
            ))
        }
        check(f"D{horizon} completed rear/interior/front quotient is quiet except next seed", completed_tube_enabled(horizon) == expected, str(completed_tube_enabled(horizon)))
    check("D09 phase-local nonseed rows require an existing same-phase predecessor", recurrence_phase_parent_contract())

    # Cycle 80's exact raw collision result is correct, but Cycle 75 selected
    # Cycle 72.  Cycle 72 is no longer a live-safe endpoint composition.
    check("E01 Cycle 75 literally imports the Cycle-72 union", c75.UNION_TABLE == c72.CONSTRUCTION.union_table)
    check("E02 current live-safe joint endpoint is Cycle 78", len(c78.CONSTRUCTION.allowed) == 47)
    _, _, phase_must, _, _ = c67.causal_safety_certificate(c67.compile_conditions())
    endpoint_model = c77.downstream_model(c78.CONSTRUCTION, phase_must)
    za = next(iter(c67.ROLE_SITES["Z_A"]))
    zc = next(iter(c67.ROLE_SITES["Z_C"]))
    check("E03 chosen D1 rear cap is generated, not supplied", CAP in c78.CONSTRUCTION.allowed and BRIDGE.source[CAP] == "D1")
    check("E04 rear cap has both endpoint records in mandatory ancestry", {za, zc}.issubset(endpoint_model.must[CAP]))

    standard_cap = (-1, *c80.LAUNCH["A"])
    launcher = transform((0, *c80.LAUNCH["A"]))
    check("F01 transform maps the standard rear cap onto the live D1 record", transform(standard_cap) == CAP)
    check("F02 bridge has exactly 17 A records plus nine finite guides", len(BRIDGE.allowed) == 26 and sum(output.startswith("R_A") or output == "R_LA" for output in BRIDGE.allowed.values()) == 17)
    check("F03 all 26 staged bridge classes are singleton", len(BRIDGE.aliases) == 26 and all(len(sites) == 1 for sites in BRIDGE.aliases.values()))
    check("F04 launcher is five-neighbour caged", len(c53.local_signature({**BRIDGE.source, **BRIDGE.allowed}, launcher)) == 5)
    check("F05 every bridge record is a mandatory ancestor of the launcher", BRIDGE.must[launcher] == frozenset(BRIDGE.allowed), f"{len(BRIDGE.must[launcher])}/{len(BRIDGE.allowed)}")

    selected_raw = c70.raw_outputs(c78.CONSTRUCTION.union_table)
    bridge_raw = c70.raw_outputs(BRIDGE.table)
    recurrent_raw = c70.raw_outputs(c80.CONSTRUCTION.table)
    raw_domains = (set(selected_raw), set(bridge_raw), set(recurrent_raw))
    check("G01 selected/bridge/recurrent raw domains are pairwise disjoint", all(raw_domains[i].isdisjoint(raw_domains[j]) for i in range(3) for j in range(i + 1, 3)))
    union_raw = c70.raw_outputs(BRIDGE.union_with_recurrence)
    check("G02 corrected composed law is 236 canonical / 5,240 raw rows", (len(BRIDGE.union_with_recurrence), len(union_raw)) == (236, 5_240), str((len(BRIDGE.union_with_recurrence), len(union_raw))))
    check("G03 corrected composed law is raw single-valued", all(len(outputs) == 1 for outputs in union_raw.values()))

    terminal_graph = c63.exact_graph(
        BRIDGE.source, BRIDGE.union_with_recurrence, BRIDGE.allowed
    )
    first_b_phase = "B"
    expected_first_seed = (
        transform((1, *c80.SEED[first_b_phase])),
        c80.role(first_b_phase, *c80.SEED[first_b_phase]),
    )
    check("H01 terminal-to-tube graph is 30 conditions / 291 states / 780 edges", (terminal_graph.conditions, len(terminal_graph.states), terminal_graph.edges) == (30, 291, 780), str((terminal_graph.conditions, len(terminal_graph.states), terminal_graph.edges)))
    check("H02 complete bridge state is reachable", (1 << len(terminal_graph.sites)) - 1 in terminal_graph.states)
    check("H03 only the exact first B seed crosses the bridge", terminal_graph.parasites == frozenset((expected_first_seed,)), str(terminal_graph.parasites))
    check("H04 bridge graph has no conflict", not terminal_graph.conflicts)

    full_allowed = {**c78.CONSTRUCTION.allowed, **BRIDGE.allowed}
    full_graph = c63.exact_graph(
        c78.CONSTRUCTION.source, BRIDGE.union_with_recurrence, full_allowed
    )
    check("I01 endpoint/bridge interleaving graph is pinned", (full_graph.conditions, len(full_graph.states), full_graph.edges) == (109, 1_305_172, 8_753_059), str((full_graph.conditions, len(full_graph.states), full_graph.edges)))
    check("I02 complete endpoint plus bridge is reachable", (1 << len(full_graph.sites)) - 1 in full_graph.states)
    check("I03 endpoint/bridge graph has only the exact first B frontier", full_graph.parasites == frozenset((expected_first_seed,)), str(full_graph.parasites))
    check("I04 endpoint/bridge graph has no conflict", not full_graph.conflicts)

    states = c70.reachable_cycle60_states()
    phase_availability = c70.phase_availability(states)
    composite = composite_construction()
    composite_model = c77.downstream_model(composite, phase_must)
    down_availability = big_downstream_availability(
        states, phase_availability, composite_model
    )
    mixed = c77.mixed_scan(
        states, phase_availability, composite_model, down_availability
    )
    print("MIXED", mixed)
    check("J01 composite has 73 downstream records / 18 availability masks", len(composite_model.sites) == 73 and len(down_availability.unique_masks) == 18, str((len(composite_model.sites), len(down_availability.unique_masks))))
    check("J02 full mixed scan exhausts 115,957 contexts", mixed.contexts == 115_957, f"{mixed.contexts:,}")
    check("J03 all 1,143 apparent wrong contexts are ancestry-certified", (mixed.certified_wrong_contexts, mixed.certified_wrong_classes) == (1_143, 60), str((mixed.certified_wrong_contexts, mixed.certified_wrong_classes)))
    check("J04 no feasible mixed wrong/off-footprint write remains", mixed.feasible_wrong_contexts == 0, str(mixed.feasible_wrong_classes))
    check("J05 no feasible mixed conflict or blocker remains", mixed.feasible_conflicts == mixed.feasible_comb_blockers == mixed.feasible_phase_blockers == 0)

    # Once the A-only bridge begins, the recurrent table cannot introduce B
    # except through its one-parent seed, and that seed requires the launcher.
    check("K00 recurrence is quiescent before the all-ancestor launcher", recurrence_phase_parent_contract() and BRIDGE.must[launcher] == frozenset(BRIDGE.allowed))
    for horizon, expected_counts in {
        1: (54, 308, 797),
        2: (86, 325, 814),
        3: (119, 342, 831),
        6: (216, 393, 882),
        9: (313, 444, 933),
    }.items():
        allowed = dict(BRIDGE.allowed)
        for x in range(1, horizon + 1):
            allowed.update(transformed_layer(x, c80.PHASES[x % 3]))
        graph = c63.exact_graph(
            BRIDGE.source, BRIDGE.union_with_recurrence, allowed
        )
        next_phase = c80.PHASES[(horizon + 1) % 3]
        expected = (
            transform((horizon + 1, *c80.SEED[next_phase])),
            c80.role(next_phase, *c80.SEED[next_phase]),
        )
        check(f"K{horizon:02d} transformed horizon counters are exact", (graph.conditions, len(graph.states), graph.edges) == expected_counts, str((graph.conditions, len(graph.states), graph.edges)))
        check(f"K{horizon:02d} transformed horizon exposes only its next seed", graph.parasites == frozenset((expected,)) and not graph.conflicts)

    c78_roles = role_inventory(
        c78.CONSTRUCTION.union_table, c78.CONSTRUCTION.source
    )
    recurrent_roles = (
        set(c80.CONSTRUCTION.table.values())
        | {content for signature in c80.CONSTRUCTION.table for _, content in signature}
    )
    guide_roles = {
        output for output in BRIDGE.allowed.values() if output.startswith("T_")
    }
    total_roles = c78_roles | recurrent_roles | guide_roles
    check("L01 live selected endpoint inventory is 93 roles", len(c78_roles) == 93)
    check("L02 recurrence and endpoint alphabets are disjoint", c78_roles.isdisjoint(recurrent_roles))
    check("L03 corrected endpoint/bridge/recurrence inventory is 153 roles", len(total_roles) == 153, str(len(total_roles)))
    check("L04 corrected selected route still requires exactly eight bits", 2**7 < len(total_roles) <= 2**8)

    print(f"\nBRIDGE_ROWS={len(BRIDGE.table)} BRIDGE_RECORDS={len(BRIDGE.allowed)}")
    print(f"COMPOSED_ROWS={len(BRIDGE.union_with_recurrence)} RAW={len(union_raw)} ROLES={len(total_roles)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
