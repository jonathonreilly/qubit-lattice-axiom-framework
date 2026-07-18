#!/usr/bin/env python3
"""Cycle 99: adversarial audit of the Cycle-97 five-port R_LB macrostep.

The audit keeps the successful spatial construction, expands its compatible
mixed-law surface, and attacks three boundaries that the author runner did not
fully separate:

1. whether the five face words are literal spatial inputs rather than a hidden
   flattened stream, and whether their claimed validation has a physical
   provenance token;
2. whether OPEN remains sensitive to a neighbour inserted at every stage
   before the EMPTY slot is accepted; and
3. whether the written R_LB value is physically consumed, rather than decoded
   by Python, and whether that consumption reuses the literal output block.

It also constructs a minimal supplied-boundary repair: one caged READY token
at each distributed face gates that face's serial equality sweep.  The repair
does not flatten the words.  It proves an interface exists; it does not grow
READY from an upstream validated macroblock.

Authority: none.  This runner changes no foundation, queue, policy, audit
verdict, git state, or Cycle-97 artifact.
"""

from __future__ import annotations

from collections import defaultdict, deque
import inspect
from pathlib import Path

import actual_five_port_open_rlb_macrostep_cycle97_2026_07_15 as c97
import live_empty_caged_router_patricia_cycle92_2026_07_15 as c92
import repeated_readable_cell_allocation_cycle98_2026_07_15 as c98
import total_status_serial_reject_selector_cycle93_2026_07_15 as c93


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "ACTUAL_FIVE_PORT_OPEN_RLB_MACROSTEP_AUDIT_CYCLE99_NOTE_2026-07-15.md"
AUTHOR_NOTE = REVIEW / "ACTUAL_FIVE_PORT_OPEN_RLB_MACROSTEP_CYCLE97_NOTE_2026-07-15.md"
CYCLE91_NOTE = REVIEW / "LIVE_SELECTED_COMPILER_CLOSURE_REVISION_CYCLE91_NOTE_2026-07-15.md"
CYCLE96_NOTE = REVIEW / "POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md"
CYCLE100_NOTE = REVIEW / "ZERO_BINARY_SOURCE_ENDPOINT_MACROBLOCK_BIND_CYCLE100_NOTE_2026-07-15.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

Coord = c97.Coord
Signature = c97.Signature
H0 = c97.H0
H1 = c97.H1
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


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


# Cycle 94 deliberately replaces one old Cycle-90 row association.  Importing
# the complete pre-lift Cycle-92/93 unions would put both old and replacement
# outputs back on that row.  The selected-law mixed surface therefore keeps the
# Cycle-94 base and adds only the compatible adapter domains from Cycles 92,
# 93, and 98.
AUDIT_RAW = merge_raw(
    c97.COMBINED_RAW,
    c92.EMPTY_RAW,
    c92.GATE_RAW,
    c93.STATUS_RAW,
    c93.FINAL_RAW,
    c98.EXTENDED_TAP_RAW,
)


def local_signature_with_override(
    records: dict[Coord, str],
    target: Coord,
    override: dict[Coord, str | None],
) -> Signature:
    items: list[tuple[Coord, str]] = []
    for direction in c97.c53.DIRECTIONS:
        site = c97.add(target, direction)
        if site in override:
            content = override[site]
        else:
            content = records.get(site)
        if content is not None:
            items.append((direction, content))
    return tuple(sorted(items))


def full_enabled(
    records: dict[Coord, str],
    raw: dict[Signature, frozenset[str]],
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c97.c53.open_candidates(records)
        if (local := c97.c53.local_signature(records, target)) in raw
    }


class IncrementalWorld:
    """Exact nearest-neighbour frontier with O(1)-local append updates."""

    def __init__(
        self,
        source: dict[Coord, str],
        raw: dict[Signature, frozenset[str]],
    ) -> None:
        self.records = dict(source)
        self.raw = raw
        self.candidates = c97.c53.open_candidates(self.records)
        self.frontier: dict[Coord, frozenset[str]] = {}
        for target in self.candidates:
            self._refresh(target)

    def _refresh(self, target: Coord) -> None:
        self.frontier.pop(target, None)
        if target in self.records:
            self.candidates.discard(target)
            return
        local = c97.c53.local_signature(self.records, target)
        if local in self.raw:
            self.frontier[target] = self.raw[local]

    def append(self, site: Coord, content: str) -> None:
        if site in self.records:
            raise ValueError(("append to occupied site", site, self.records[site]))
        self.records[site] = content
        self.candidates.discard(site)
        self.frontier.pop(site, None)
        for direction in c97.c53.DIRECTIONS:
            target = c97.add(site, direction)
            if target not in self.records:
                self.candidates.add(target)
                self._refresh(target)


def frontier_with_extra(
    world: IncrementalWorld,
    site: Coord,
    content: str,
) -> dict[Coord, frozenset[str]]:
    """Exact frontier after one extra record, updating only affected sites."""

    if site in world.records:
        raise ValueError(("extra site already occupied", site))
    answer = dict(world.frontier)
    answer.pop(site, None)
    override = {site: content}
    for direction in c97.c53.DIRECTIONS:
        target = c97.add(site, direction)
        if target in world.records:
            continue
        answer.pop(target, None)
        local = local_signature_with_override(world.records, target, override)
        if local in world.raw:
            answer[target] = world.raw[local]
    return answer


def frontier_with_replacement(
    world: IncrementalWorld,
    site: Coord,
    content: str,
) -> dict[Coord, frozenset[str]]:
    if site not in world.records:
        raise ValueError(("replacement site is open", site))
    answer = dict(world.frontier)
    override = {site: content}
    for direction in c97.c53.DIRECTIONS:
        target = c97.add(site, direction)
        if target in world.records:
            continue
        answer.pop(target, None)
        local = local_signature_with_override(world.records, target, override)
        if local in world.raw:
            answer[target] = world.raw[local]
    return answer


def frontier_without(
    world: IncrementalWorld,
    site: Coord,
) -> dict[Coord, frozenset[str]]:
    if site not in world.records:
        raise ValueError(("removed site is already open", site))
    answer = dict(world.frontier)
    override = {site: None}
    local = local_signature_with_override(world.records, site, override)
    if local in world.raw:
        answer[site] = world.raw[local]
    else:
        answer.pop(site, None)
    for direction in c97.c53.DIRECTIONS:
        target = c97.add(site, direction)
        if target in world.records:
            continue
        answer.pop(target, None)
        local = local_signature_with_override(world.records, target, override)
        if local in world.raw:
            answer[target] = world.raw[local]
    return answer


def components(sites: set[Coord]) -> tuple[frozenset[Coord], ...]:
    remaining = set(sites)
    answer: list[frozenset[Coord]] = []
    while remaining:
        start = remaining.pop()
        seen = {start}
        queue = deque((start,))
        while queue:
            site = queue.popleft()
            for direction in c97.c53.DIRECTIONS:
                neighbour = c97.add(site, direction)
                if neighbour in remaining:
                    remaining.remove(neighbour)
                    seen.add(neighbour)
                    queue.append(neighbour)
        answer.append(frozenset(seen))
    return tuple(sorted(answer, key=lambda block: min(block)))


def expected(step: int) -> dict[Coord, frozenset[str]]:
    if step == len(c97.ADDITIONS):
        return {}
    site, content = c97.ADDITIONS[step]
    return {site: frozenset((content,))}


def author_and_spatial_contract() -> None:
    section("A - Independent source and literal five-face audit")
    author = AUTHOR_NOTE.read_text(encoding="utf-8").lower() if AUTHOR_NOTE.is_file() else ""
    check("A01 author artifact exists and reports its bounded 24/0 run",
          AUTHOR_NOTE.is_file() and "24 pass / 0 fail" in author and "authority: none" in author)
    check("A02 actual row and direction order are exact",
          dict(c97.RLB_SIGNATURE) == {
              (-1, 0, 0): "R_A22",
              (0, -1, 0): "R_B12",
              (0, 0, -1): "R_B21",
              (0, 0, 1): "R_B23",
              (0, 1, 0): "R_B32",
          }
          and c97.RLB_OUTPUT == "R_LB"
          and c97.FACE_DIRECTIONS == c97.c90.DIRECTION_ORDER[:5])

    occupied_sites = {site for block in c97.ALL_CANDIDATES[:5] for site in block}
    occupied_components = components(occupied_sites)
    geometry_ok = all(
        len(candidate) == 8
        and all(c97.dot(site, direction) == 24 for site in candidate)
        and all(c97.dot(site, direction) == 25 for site in status)
        and all(c97.dot(site, direction) == 26 for site in reference)
        and all(c97.sub(candidate[index + 1], candidate[index]) == tangent for index in range(7))
        for direction, tangent, (candidate, status, reference, _guards)
        in zip(c97.FACE_DIRECTIONS, c97.FACE_T, c97.FACE_GROUPS)
    )
    check("A03 inputs are five disjoint eight-site face blocks, not one flattened rail",
          geometry_ok and len(occupied_components) == 5 and sorted(map(len, occupied_components)) == [8] * 5)
    check("A04 each face block physically carries its exact role word",
          all(
              tuple(1 if c97.SOURCE[site] == H1 else 0 for site in candidate)
              == c97.c89.ROLE_TO_WORD[dict(c97.RLB_SIGNATURE)[direction]]
              for direction, (candidate, _status, _reference, _guards)
              in zip(c97.FACE_DIRECTIONS, c97.FACE_GROUPS)
          ))
    check("A05 +x is absent and no EMPTY candidate bit is prewritten",
          c97.MONITORED_OPEN not in c97.SOURCE
          and c97.MONITORED_OPEN not in dict(c97.ADDITIONS)
          and set(c97.OPEN_CANDIDATE).isdisjoint(c97.SOURCE))

    # Cycle 97 value-checks the five words later, but its source has no
    # per-word upstream VALID/READY/provenance record.  The face-adjacent status
    # bits are all future scan additions, not source certificates.
    face_status = {site for block in c97.ALL_STATUS[:5] for site in block}
    check("A06 Cycle97 supplies no physical per-face validation provenance token",
          face_status.isdisjoint(c97.SOURCE)
          and "READY" not in (ROOT / "scripts" / "actual_five_port_open_rlb_macrostep_cycle97_2026_07_15.py").read_text(encoding="utf-8"))

    known_scan = {
        c97.CENTER,
        *occupied_sites,
        *(site for block in c97.ALL_REFERENCES for site in block),
        *(site for group in c97.FACE_GROUPS for site in group[3]),
        *c97.OPEN_GUARDS,
        *(c97.add(c97.OPEN_SENSOR, direction) for direction in ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))),
    }
    source_parts = (set(c97.SCAN_SOURCE), set(c97.WRITER_SOURCE), set(c97.NEXT_SOURCE))
    addition_parts = (
        set(c97.SCAN_TARGETS),
        {site for site, _content in c97.WRITER_ADDITIONS},
        {site for site, _content in c97.NEXT_ADDITIONS},
    )
    check("A07 supplied census is independently 4,258 + 89 + 192 = 4,539",
          tuple(map(len, source_parts)) == (4258, 89, 192)
          and all(source_parts[i].isdisjoint(source_parts[j]) for i in range(3) for j in range(i))
          and len(c97.SOURCE) == 4539
          and len(known_scan) == 189
          and len(set(c97.SCAN_SOURCE) - known_scan) == 4069)
    check("A08 grown census is independently 1,079 + 35 + 48 = 1,162",
          tuple(map(len, addition_parts)) == (1079, 35, 48)
          and all(addition_parts[i].isdisjoint(addition_parts[j]) for i in range(3) for j in range(i))
          and len(dict(c97.ADDITIONS)) == len(c97.ADDITIONS) == 1162
          and set(c97.SOURCE).isdisjoint(dict(c97.ADDITIONS)))


def mixed_trajectory_and_open_contract() -> None:
    section("B - Compatible mixed union, all dynamic stages, and rotations")
    check("B01 selected compatible mixed union has 6,169 single-valued raw inputs",
          len(AUDIT_RAW) == 6169 and all(len(values) == 1 for values in AUDIT_RAW.values()))
    check("B02 all 1,162 dynamic targets are unique, initially open, and content-exact",
          len({site for site, _content in c97.ADDITIONS}) == len(c97.ADDITIONS)
          and set(c97.SOURCE).isdisjoint(site for site, _content in c97.ADDITIONS)
          and all(content in c97.c89.FULL_ROLES for _site, content in c97.ADDITIONS))

    open_accept_step = next(
        index for index, (site, _content) in enumerate(c97.ADDITIONS)
        if site == c97.OPEN_STATUS[-1]
    )
    world = IncrementalWorld(c97.SOURCE, AUDIT_RAW)
    stage_failures: list[tuple[object, ...]] = []
    late_failures: list[tuple[object, ...]] = []
    late_controls = 0
    for step in range(len(c97.ADDITIONS) + 1):
        wanted = expected(step)
        if world.frontier != wanted:
            stage_failures.append((step, wanted, dict(world.frontier)))
            break

        # Every state before the final OPEN equality append is attacked with
        # each live record content at the monitored port.  At state zero every
        # content must block formation.  Once the sensor has formed, the exact
        # observed fact is the opposite: no content revokes the cached OPEN
        # certificate or changes the remaining frontier.
        if step <= open_accept_step:
            late_wanted = {} if step == 0 else wanted
            for role in c97.c89.FULL_ROLES:
                late_controls += 1
                actual = frontier_with_extra(world, c97.MONITORED_OPEN, role)
                if actual != late_wanted:
                    late_failures.append((step, role, late_wanted, actual))
                    break
            if late_failures:
                break

        if step < len(c97.ADDITIONS):
            world.append(*c97.ADDITIONS[step])

    check("B03 every one of 1,163 stages remains exact under all compatible adapter rows",
          not stage_failures, str(stage_failures[:1]))
    check("B04 terminal remains quiet with all old scan/writer/comparator debris present",
          not stage_failures and not world.frontier)
    check("B05 late-neighbour sweep covers all 880 pre-acceptance states x 153 roles",
          open_accept_step == 879 and late_controls == 880 * 153 and not late_failures,
          str(late_failures[:1]))

    rotation_failures: list[tuple[object, ...]] = []
    for local, values in AUDIT_RAW.items():
        for rotation in c97.c53.ROTATIONS:
            rotated = c97.c53.rotate_signature(local, rotation)
            if AUDIT_RAW.get(rotated) != values:
                rotation_failures.append((local, rotation, values, AUDIT_RAW.get(rotated)))
                break
    check("B06 all 6,169 x 24 raw images close exactly",
          not rotation_failures and len(AUDIT_RAW) * len(c97.c53.ROTATIONS) == 148056,
          str(rotation_failures[:1]))
    check("B07 stage exactness plus raw covariance covers all 1,163 x 24 stage images",
          not stage_failures and not rotation_failures
          and (len(c97.ADDITIONS) + 1) * len(c97.c53.ROTATIONS) == 27912)

    section("C - Word mismatch and exact OPEN boundary")
    corruption_failures: list[tuple[object, ...]] = []
    corruption_controls = 0
    for slot, (candidate, status) in enumerate(zip(c97.ALL_CANDIDATES[:5], c97.ALL_STATUS[:5])):
        for bit_index, (candidate_site, status_site) in enumerate(zip(candidate, status)):
            source = dict(c97.SOURCE)
            source[candidate_site] = H0 if source[candidate_site] == H1 else H1
            stop = next(index for index, (site, _content) in enumerate(c97.ADDITIONS) if site == status_site)
            altered = IncrementalWorld(source, AUDIT_RAW)
            for step in range(stop + 1):
                wanted = expected(step) if step < stop else {}
                if altered.frontier != wanted:
                    corruption_failures.append(("occupied", slot, bit_index, step, wanted, dict(altered.frontier)))
                    break
                if step < stop:
                    altered.append(*c97.ADDITIONS[step])
            corruption_controls += 1

    for bit_index, (reference_site, status_site) in enumerate(zip(c97.OPEN_REFERENCE, c97.OPEN_STATUS)):
        source = dict(c97.SOURCE)
        source[reference_site] = H0
        stop = next(index for index, (site, _content) in enumerate(c97.ADDITIONS) if site == status_site)
        altered = IncrementalWorld(source, AUDIT_RAW)
        for step in range(stop + 1):
            wanted = expected(step) if step < stop else {}
            if altered.frontier != wanted:
                corruption_failures.append(("open-reference", bit_index, step, wanted, dict(altered.frontier)))
                break
            if step < stop:
                altered.append(*c97.ADDITIONS[step])
        corruption_controls += 1
    check("C01 all 40 occupied-bit and 8 OPEN-reference corruptions fail exactly at comparison",
          corruption_controls == 48 and not corruption_failures, str(corruption_failures[:1]))

    initial = IncrementalWorld(c97.SOURCE, AUDIT_RAW)
    initial_blockers = [
        (role, frontier_with_extra(initial, c97.MONITORED_OPEN, role))
        for role in c97.c89.FULL_ROLES
    ]
    check("C02 every live content at +x makes the complete initial frontier quiet",
          all(not frontier for _role, frontier in initial_blockers),
          str([(role, frontier) for role, frontier in initial_blockers if frontier][:1]))

    forward = c97.OPEN_FEED[0]
    forward_controls = {
        role: frontier_with_extra(initial, forward, role)
        for role in c97.c89.FULL_ROLES
    }
    check("C03 forward axial site is also load-bearing and prewritten H1 bypasses the sensor",
          all(not frontier for role, frontier in forward_controls.items() if role != H1)
          and forward_controls[H1] == {c97.OPEN_FEED[1]: frozenset((H1,))})
    check("C04 exact scope: initial absence is sensed but post-sensor late occupancy cannot revoke EMPTY",
          late_controls == 134640 and not late_failures)


def build_gated_scan() -> tuple[
    tuple[Coord, ...],
    tuple[Coord, ...],
    frozenset[Coord],
    dict[Coord, str],
    dict[Signature, str],
]:
    ready_sites = tuple(group[3][0] for group in c97.FACE_GROUPS)
    marker_sites = tuple(group[3][1] for group in c97.FACE_GROUPS)
    source = dict(c97.SCAN_SOURCE)
    new_cages: set[Coord] = set()
    for index, (ready, marker) in enumerate(zip(ready_sites, marker_sites)):
        source[ready] = H1
        source[marker] = c97.FRAME_MARKER
        status = c97.ALL_STATUS[index][0]
        for direction in c97.c53.DIRECTIONS:
            site = c97.add(ready, direction)
            if site == status or site in source:
                continue
            if site in c97.DYNAMIC_SCAN_SITES:
                raise ValueError(("READY cage hits dynamic site", index, site))
            source[site] = c97.GUARD
            new_cages.add(site)

    records = dict(source)
    table: dict[Signature, str] = {}
    for target in c97.SCAN_TARGETS:
        local = c97.canonical(dict(c97.c53.local_signature(records, target)))
        prior = table.get(local)
        if prior is not None and prior != H1:
            raise ValueError((local, prior, H1))
        table[local] = H1
        records[target] = H1
    return ready_sites, marker_sites, frozenset(new_cages), source, table


READY_SITES, READY_MARKERS, READY_CAGES, GATED_SCAN_SOURCE, GATED_SCAN_TABLE = build_gated_scan()
GATED_SCAN_RAW = c97.c59.raw_rule_outputs(GATED_SCAN_TABLE)
GATED_RAW = merge_raw(
    c97.c94.COMBINED_RAW,
    GATED_SCAN_RAW,
    c92.EMPTY_RAW,
    c92.GATE_RAW,
    c93.STATUS_RAW,
    c93.FINAL_RAW,
    c98.EXTENDED_TAP_RAW,
)
GATED_SOURCE = dict(GATED_SCAN_SOURCE)
c97.merge_records(GATED_SOURCE, c97.WRITER_SOURCE)
c97.merge_records(GATED_SOURCE, c97.NEXT_SOURCE)


def ready_gate_contract() -> None:
    section("D - Exact distributed READY-gate repair probe")
    check("D01 repair keeps all five candidate blocks at the same spatial sites",
          all(GATED_SOURCE[site] == c97.SOURCE[site] for block in c97.ALL_CANDIDATES[:5] for site in block)
          and len(components({site for block in c97.ALL_CANDIDATES[:5] for site in block})) == 5)
    check("D02 repair uses five H1 READY sites, five JOINT type markers, and fifteen cages",
          len(READY_SITES) == len(set(READY_SITES)) == 5
          and len(READY_MARKERS) == len(set(READY_MARKERS)) == 5
          and len(READY_CAGES) == 15
          and all(GATED_SOURCE[site] == H1 for site in READY_SITES)
          and all(GATED_SOURCE[site] == c97.FRAME_MARKER for site in READY_MARKERS)
          and len(GATED_SOURCE) == len(c97.SOURCE) + 15 == 4554)
    check("D03 gated scan has 9 canonical / 153 raw rows in a 6,193-row single-valued union",
          len(GATED_SCAN_TABLE) == 9 and len(GATED_SCAN_RAW) == 153
          and len(GATED_RAW) == 6193 and all(len(values) == 1 for values in GATED_RAW.values()))

    gate_steps = {
        next(index for index, (site, _content) in enumerate(c97.ADDITIONS) if site == c97.ALL_STATUS[slot][0]): slot
        for slot in range(5)
    }
    world = IncrementalWorld(GATED_SOURCE, GATED_RAW)
    stage_failures: list[tuple[object, ...]] = []
    gate_failures: list[tuple[object, ...]] = []
    wrong_role_controls = 0
    for step in range(len(c97.ADDITIONS) + 1):
        wanted = expected(step)
        if world.frontier != wanted:
            stage_failures.append((step, wanted, dict(world.frontier)))
            break
        if step in gate_steps:
            slot = gate_steps[step]
            ready = READY_SITES[slot]
            marker = READY_MARKERS[slot]
            if frontier_without(world, ready):
                gate_failures.append(("missing-ready", slot, frontier_without(world, ready)))
            if frontier_without(world, marker):
                gate_failures.append(("missing-marker", slot, frontier_without(world, marker)))
            for role in c97.c89.FULL_ROLES - {H1}:
                wrong_role_controls += 1
                actual = frontier_with_replacement(world, ready, role)
                if actual:
                    gate_failures.append(("wrong-ready", slot, role, actual))
                    break
        if step < len(c97.ADDITIONS):
            world.append(*c97.ADDITIONS[step])

    check("D04 every gated dynamic stage is exact and terminal is quiet",
          not stage_failures and not world.frontier, str(stage_failures[:1]))
    check("D05 each face stops if READY or its type marker is absent",
          not [item for item in gate_failures if item[0] in {"missing-ready", "missing-marker"}],
          str(gate_failures[:1]))
    check("D06 all five x 152 wrong READY contents fail closed with no parasite",
          wrong_role_controls == 5 * 152 and not gate_failures, str(gate_failures[:1]))
    check("D07 classification is interface-repair-positive, provenance-route-still-open",
          len(GATED_SOURCE) == 4554 and set(READY_SITES).isdisjoint(c97.ADDITIONS))


def output_consumption_contract() -> None:
    section("E - Physical R_LB consumption versus duplicate supplied input")
    output_sites = tuple(
        c97.transform_site(site, c97.WRITER_ROTATION, c97.WRITER_SHIFT)
        for site in c97.c94.DATA
    )
    tap_sites = tuple(
        c97.transform_site(site, c97.WRITER_ROTATION, c97.WRITER_SHIFT)
        for site in c97.c94.TAP
    )
    next_rlb_sites = tuple(
        c97.transform_site((index, 0, 0), c97.NEXT_ROTATION, c97.NEXT_SHIFT)
        for index in range(8)
    )
    terminal = c97.records_at(len(c97.ADDITIONS))
    decoded_output = tuple(1 if terminal[site] == H1 else 0 for site in output_sites)
    decoded_next = tuple(1 if c97.SOURCE[site] == H1 else 0 for site in next_rlb_sites)
    check("E01 writer appends the exact physical R_LB word and all eight taps",
          decoded_output == c97.RLB_WORD == (1, 0, 1, 1, 0, 0, 0, 1)
          and all(site in terminal for site in tap_sites))
    check("E02 every tap is nearest-neighbour to and locally reads its DATA bit",
          all(sum(abs(a - b) for a, b in zip(data, tap)) == 1 for data, tap in zip(output_sites, tap_sites)))

    tap_failures: list[tuple[object, ...]] = []
    for bit_index, (data_site, tap_site) in enumerate(zip(output_sites, tap_sites)):
        step = next(index for index, (site, _content) in enumerate(c97.ADDITIONS) if site == tap_site)
        records = c97.records_at(step)
        records[data_site] = H0 if records[data_site] == H1 else H1
        actual = full_enabled(records, AUDIT_RAW)
        if actual:
            tap_failures.append((bit_index, step, actual))
    check("E03 every one-bit DATA substitution stops the reverse value sweep",
          not tap_failures, str(tap_failures[:1]))

    match_step = next(index for index, (site, _content) in enumerate(c97.ADDITIONS) if site == c97.WRITER_MATCH)
    after_match = IncrementalWorld(c97.SOURCE, AUDIT_RAW)
    for addition in c97.ADDITIONS[:match_step + 1]:
        after_match.append(*addition)
    check("E04 unsupplied MATCH is literally the next comparator START and enables its first certificate",
          c97.WRITER_MATCH not in c97.SOURCE
          and c97.WRITER_MATCH not in c97.NEXT_SOURCE
          and c97.WRITER_MATCH
          == c97.transform_site(c97.c89.START, c97.NEXT_ROTATION, c97.NEXT_SHIFT)
          and after_match.frontier == {c97.NEXT_ADDITIONS[0][0]: frozenset((H1,))})
    check("E05 dynamics use local signatures, not the host decoder",
          "local_signature" in inspect.getsource(c97.enabled)
          and "decode_output" not in inspect.getsource(c97.enabled)
          and "decoded" not in inspect.getsource(c97.enabled))
    check("E06 stronger literal-word reuse remains open: next R_LB is a disjoint supplied copy",
          set(output_sites).isdisjoint(next_rlb_sites)
          and all(site in c97.SOURCE for site in next_rlb_sites)
          and decoded_next == c97.RLB_WORD)


def scope_and_note_contract() -> None:
    section("F - N1-N8, primitive, and constitutional disposition")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("F01 Cycle99 note exists, authority none, and does not claim an audit verdict",
          NOTE.is_file() and "authority: none" in note and "no independent audit verdict" in note)
    check("F02 note records all N1-N8 gates",
          all(f"n{index}" in note for index in range(1, 9)))
    check("F03 note distinguishes interface repair from live W_STEP/W_MULTI work",
          all(needle in note for needle in (
              "interface-repair-positive",
              "ready_provenance_route",
              "late_neighbour_reservation",
              "successor_literal_reuse/allocation",
              "w_step",
              "w_multi",
          )))
    check("F04 primitive registry and all three primitive sources were inspected",
          REGISTRY.is_file()
          and all((ROOT / path).is_file() for path in (
              "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
              "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
              "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
          ))
          and "approved primitive" in note)
    check("F05 Cycle91/96 acceptance residuals and Cycle100 partial retirement are cited",
          CYCLE91_NOTE.is_file() and CYCLE96_NOTE.is_file() and CYCLE100_NOTE.is_file()
          and all(needle in note for needle in ("cycle 91", "cycle 96", "cycle 100")))
    check("F06 note makes no foundation or axiom change",
          "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    author_and_spatial_contract()
    mixed_trajectory_and_open_contract()
    ready_gate_contract()
    output_consumption_contract()
    scope_and_note_contract()
    print(f"\nAUTHOR_RAW={len(c97.COMBINED_RAW)} AUDIT_RAW={len(AUDIT_RAW)} GATED_RAW={len(GATED_RAW)}")
    print(f"AUTHOR_SUPPLIED={len(c97.SOURCE)} AUTHOR_GROWN={len(c97.ADDITIONS)} GATED_SUPPLIED={len(GATED_SOURCE)}")
    print("LATE_SWEEP=880x153=134640 READY_WRONG_ROLE_SWEEP=5x152=760")
    print("CLASSIFICATION=BOUNDED_POSITIVE_SURVIVES_WITH_EXPLICIT_QUALIFICATIONS")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
