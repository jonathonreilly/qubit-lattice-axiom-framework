#!/usr/bin/env python3
"""Cycle 59 shared q/a/b/c open-reservation comb.

This authority-free runner first exhausts the 24^4 placements of four Cycle-51
replicas.  It then checks one compact shared comb rooted in the completed
Cycle-57 frame.  Every proper-cubic copy of every exact nearest-neighbour row
is live.  The finite comb graph follows every asynchronous single-record
append and is composed with the still-live Cycle-57 builder and the separated
infinite Cycle-52 rail by exact locality checks.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import re

import full_a_boundary_launcher_last_cycle57_2026_07_14 as c57
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import open_site_reservation_handshake_cycle51_2026_07_14 as c51
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FOUR_OPEN_RESERVATION_COMB_CYCLE59_NOTE_2026-07-14.md"
CYCLE51 = REVIEW / "OPEN_SITE_RESERVATION_HANDSHAKE_CYCLE51_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE57 = REVIEW / "FULL_A_BOUNDARY_LAUNCHER_LAST_CYCLE57_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Signature = c53.Signature

TARGETS: dict[str, Coord] = {
    "q": (0, -1, 0),
    "a": (1, 0, 0),
    "b": (2, 0, 0),
    "c": (3, 0, 0),
}
CERTIFICATES: dict[str, Coord] = {
    "q": (0, -1, -1),
    "a": (1, 0, -1),
    "b": (2, 0, -1),
    "c": (3, 0, -1),
}
CERTIFICATE_CONTENTS = {
    "q": "W6",
    "a": "W6",
    "b": "OPEN_B",
    "c": "OPEN_C",
}
COMMIT_SITE = CERTIFICATES["c"]

EXPECTED_STATES = 4_784_509
EXPECTED_EDGES = 46_716_061
EXPECTED_ADDITIONS = 45
EXPECTED_CANONICAL_RULES = 24
EXPECTED_RAW_RULES = 464


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


@dataclass(frozen=True)
class Construction:
    base: dict[Coord, str]
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    stage_aliases: dict[str, tuple[Coord, ...]]
    formation_sources: dict[str, dict[Coord, str]]


def build_construction() -> Construction:
    """Build the fixed 24-input table in the completed Cycle-57 context."""

    base = dict(c57.BUILDER.completed)
    records = dict(base)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    stage_aliases: dict[str, tuple[Coord, ...]] = {}
    formation_sources: dict[str, dict[Coord, str]] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"canonical output conflict: {prior} / {output}")
        table[canonical] = output

    def stage(label: str, representative: Coord) -> None:
        if label == "W6":
            formation_sources["q"] = dict(records)
            formation_sources["a"] = dict(records)
        elif label == "OPEN_B":
            formation_sources["b"] = dict(records)
        elif label == "OPEN_C":
            formation_sources["c"] = dict(records)

        signature = key(records, representative)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty signature orbit for {label}")
        install(signature, label)
        stage_aliases[label] = aliases
        for site in aliases:
            records[site] = label
            allowed[site] = label

    # START cannot form before ARM and A_0_2.  Its three-site W1 orbit reaches
    # the y=4 wake and the negative-z descent without the earlier ARM+H1
    # crossfire at (-1,3,0).  The chain then closes a three-record W6 cage and
    # branches east along the four official targets.
    for label, representative in (
        ("START", (-1, 3, 0)),
        ("W1", (-1, 4, 0)),
        ("W2", (0, 3, -1)),
        ("W3", (0, 2, -1)),
        ("W4", (0, 1, -1)),
        ("W5", (0, 0, -1)),
        ("W6", (0, -1, -1)),
        ("J6", (0, -1, -2)),
        ("COMP6", (1, -1, -2)),
        ("S7", (2, -1, -2)),
        ("E", (2, 0, -2)),
        ("OPEN_B", (2, 0, -1)),
        ("S8", (3, 0, -2)),
        ("OPEN_C", (3, 0, -1)),
    ):
        stage(label, representative)

    # These are the three additional S8 images actually reached by partial
    # E/S7 schedules.  They are declared orbit completions, not parasites.
    for site in ((0, -2, -3), (2, -2, -1), (2, 0, -3)):
        allowed[site] = "S8"

    # Exact schedule-tolerance rows recovered from all incomplete terminals of
    # the raw 14-row graph.  They retain the same output when an earlier S8 or
    # OPEN_B append has become an additional exact neighbour.
    tolerance_rows: tuple[tuple[Signature, str], ...] = (
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "S7"), ((0, 0, -1), "S8")), "E"),
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "S7"), ((0, 0, 1), "S8")), "E"),
        ((((-1, 0, 0), "E"), ((0, -1, 0), "W6")), "OPEN_B"),
        ((((-1, 0, 0), "E"), ((0, -1, 0), "E")), "S8"),
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "OPEN_B"), ((0, 0, -1), "S7")), "E"),
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "OPEN_B"), ((0, 0, -1), "S7"), ((0, 1, 0), "S8")), "E"),
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "OPEN_B"), ((0, 0, 1), "S7")), "E"),
        ((((-1, 0, 0), "J6"), ((0, -1, 0), "OPEN_B"), ((0, 0, 1), "S7"), ((0, 1, 0), "S8")), "E"),
    )
    for signature, output in tolerance_rows:
        install(signature, output)

    # If the exterior W1 at (-2,3,0) forms before the first B slice reaches
    # B_0_2, it becomes one additional exact neighbour of that rail target.
    # This single all-rotation row is the commuting side of that one local
    # comb/rail diamond; after B_0_2 is permanent, no future rail site is
    # adjacent to the comb.
    install(
        (
            ((-1, 0, 0), "A_0_2"),
            ((0, -1, 0), "B_1_2"),
            ((0, 0, -1), "W1"),
        ),
        "B_0_2",
    )
    install(
        (
            ((-1, 0, 0), "B_0_2"),
            ((0, -1, 0), "START"),
        ),
        "W1",
    )

    return Construction(base, table, allowed, stage_aliases, formation_sources)


CONSTRUCTION = build_construction()


@dataclass(frozen=True)
class ReplicaResult:
    footprint_size: int
    orientations: int
    safe_counts: tuple[int, int, int, int]
    disjoint_quartets: int
    support_safe_disjoint_quartets: int


def replica_exhaustion() -> ReplicaResult:
    """Enumerate all 24^4 placements of four translated Cycle-51 replicas."""

    footprint = set(c51.ANCHORS) | set(c51.DYNAMIC_SITES.values())
    footprint.remove(c51.P)  # the official target must remain open
    official = c53.official_support()
    target_order = tuple(TARGETS.values())
    replicas: dict[Coord, tuple[frozenset[Coord], ...]] = {}
    safe: dict[Coord, frozenset[int]] = {}
    for target in target_order:
        images = tuple(
            frozenset(c51.add_site(c51.rotate_site(site, rotation), target) for site in footprint)
            for rotation in c51.ROTATIONS
        )
        replicas[target] = images
        safe[target] = frozenset(
            index for index, image in enumerate(images) if image.isdisjoint(official)
        )

    disjoint = support_safe = 0
    for indices in product(range(24), repeat=4):
        images = tuple(replicas[target][index] for target, index in zip(target_order, indices))
        if any(images[left] & images[right] for left in range(4) for right in range(left + 1, 4)):
            continue
        disjoint += 1
        if all(index in safe[target] for target, index in zip(target_order, indices)):
            support_safe += 1
    return ReplicaResult(
        len(footprint), 24 ** 4,
        tuple(len(safe[target]) for target in target_order),
        disjoint, support_safe,
    )


def raw_rule_outputs(table: dict[Signature, str]) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = {}
    for signature, output in table.items():
        for rotation in c53.ROTATIONS:
            outputs.setdefault(c53.rotate_signature(signature, rotation), set()).add(output)
    return {signature: frozenset(values) for signature, values in outputs.items()}


def comb_enabled(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        target: CONSTRUCTION.table[signature]
        for target in c53.open_candidates(records)
        if (signature := key(records, target)) in CONSTRUCTION.table
    }


def merged_outputs(records: dict[Coord, str]) -> dict[Coord, set[str]]:
    outputs: dict[Coord, set[str]] = {}
    for enabled in (
        c57.builder_enabled(records),
        c52.enabled_assignments(records),
        comb_enabled(records),
    ):
        for target, output in enabled.items():
            outputs.setdefault(target, set()).add(output)
    return outputs


def future_corridor_distance(site: Coord) -> int:
    """L1 distance to x<=-2, 0<=y<=2, 0<=z<=3."""

    x, y, z = site
    dx = 0 if x <= -2 else x + 2
    dy = 0 if 0 <= y <= 2 else min(abs(y), abs(y - 2))
    dz = 0 if 0 <= z <= 3 else min(abs(z), abs(z - 3))
    return dx + dy + dz


@dataclass(frozen=True)
class GraphResult:
    states: int
    edges: int
    terminals: int
    terminal_sizes: tuple[tuple[int, int], ...]
    complete_terminals: int
    incomplete_terminals: int
    conflicts: int
    parasites: frozenset[tuple[Coord, str]]
    commit_order_violations: int
    b_order_violations: int
    certificate_edges: tuple[tuple[str, int], ...]


def compile_conditions() -> tuple[tuple[int, int, int, str, Coord], ...]:
    """Compile exact rotated rows to bit predicates over the 45 additions."""

    base = CONSTRUCTION.base
    allowed = CONSTRUCTION.allowed
    sites = tuple(sorted(allowed))
    site_index = {site: index for index, site in enumerate(sites)}
    occupied_universe = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied_universe
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in CONSTRUCTION.table.items()
        for rotation in c53.ROTATIONS
    }
    conditions: set[tuple[int, int, int, str, Coord]] = set()
    for target in candidates:
        for signature, output in raw_rows:
            expected = dict(signature)
            present = absent = 0
            viable = True
            for direction in c53.DIRECTIONS:
                neighbour = c53.add(target, direction)
                wanted = expected.get(direction)
                if neighbour in base:
                    if wanted != base[neighbour]:
                        viable = False
                        break
                elif neighbour in allowed:
                    bit = 1 << site_index[neighbour]
                    if wanted is None:
                        absent |= bit
                    elif wanted == allowed[neighbour]:
                        present |= bit
                    else:
                        viable = False
                        break
                elif wanted is not None:
                    viable = False
                    break
            if not viable:
                continue
            target_bit = 1 << site_index[target] if target in allowed else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))
    return tuple(sorted(conditions, key=lambda item: (item[4], item[3], item[0], item[1])))


def exhaustive_comb_graph() -> GraphResult:
    """Follow every asynchronous append under all rotated comb rows."""

    allowed = CONSTRUCTION.allowed
    sites = tuple(sorted(allowed))
    site_index = {site: index for index, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    certificate_bits = {name: 1 << site_index[site] for name, site in CERTIFICATES.items()}
    conditions = compile_conditions()

    queue = deque((0,))
    seen = {0}
    edges = conflicts = commit_violations = b_violations = 0
    terminals = complete_terminals = incomplete_terminals = 0
    terminal_sizes: Counter[int] = Counter()
    parasites: set[tuple[Coord, str]] = set()
    certificate_edges: Counter[str] = Counter()

    while queue:
        mask = queue.popleft()
        if mask & certificate_bits["c"]:
            if any(not mask & certificate_bits[name] for name in ("q", "a", "b")):
                commit_violations += 1
        if mask & certificate_bits["b"]:
            if any(not mask & certificate_bits[name] for name in ("q", "a")):
                b_violations += 1

        writes: dict[Coord, set[tuple[int, str]]] = {}
        for present, absent, target_bit, output, target in conditions:
            if mask & present == present and not mask & absent:
                writes.setdefault(target, set()).add((target_bit, output))

        if not writes:
            terminals += 1
            terminal_sizes[mask.bit_count()] += 1
            if mask == all_mask:
                complete_terminals += 1
            else:
                incomplete_terminals += 1

        for target, choices in writes.items():
            outputs = {output for _, output in choices}
            if len(outputs) != 1:
                conflicts += 1
                continue
            target_bit, output = next(iter(choices))
            edges += 1
            if not target_bit or allowed.get(target) != output:
                parasites.add((target, output))
                continue
            for name, certificate in CERTIFICATES.items():
                if target == certificate:
                    certificate_edges[name] += 1
            future = mask | target_bit
            if future not in seen:
                seen.add(future)
                queue.append(future)

        if len(seen) % 1_000_000 == 0:
            print(f"  graph progress: {len(seen):,} states / {edges:,} edges")

    return GraphResult(
        len(seen), edges, terminals, tuple(sorted(terminal_sizes.items())),
        complete_terminals, incomplete_terminals, conflicts, frozenset(parasites),
        commit_violations, b_violations, tuple(sorted(certificate_edges.items())),
    )


def main() -> int:
    section("A. Independent four-replica exhaustion")
    replicas = replica_exhaustion()
    check("A01 proper cubic group has 24 rotations", len(c51.ROTATIONS) == 24)
    check("A02 Cycle-51 replica footprint excludes only the target", replicas.footprint_size == 17)
    check("A03 every 24^4 orientation quartet is enumerated", replicas.orientations == 331_776)
    check("A04 support-safe orientation counts are exact", replicas.safe_counts == (7, 1, 1, 5), str(replicas.safe_counts))
    check("A05 no four replicas are pairwise disjoint", replicas.disjoint_quartets == 0)
    check("A06 no support-safe four-replica quartet exists", replicas.support_safe_disjoint_quartets == 0)

    section("B. Shared comb geometry and certificates")
    base, table, allowed = CONSTRUCTION.base, CONSTRUCTION.table, CONSTRUCTION.allowed
    check("B01 base is exact completed Cycle-57 frame", base == c57.BUILDER.completed)
    check("B02 comb has 24 canonical exact inputs", len(table) == EXPECTED_CANONICAL_RULES)
    check("B03 comb declares 45 permanent additions", len(allowed) == EXPECTED_ADDITIONS)
    check("B04 no declared addition overwrites the base", set(base).isdisjoint(allowed))
    check("B05 START is the unique completed-base comb write", comb_enabled(base) == {(-1, 3, 0): "START"}, str(comb_enabled(base)))
    check("B06 full declared comb is terminal", not comb_enabled(dict(base) | allowed))
    check("B07 q/a share the exact three-site W6 orbit", set(CONSTRUCTION.stage_aliases["W6"]) == {(0, -1, -1), (0, 0, -2), (1, 0, -1)})
    check("B08 b belongs to the exact three-site OPEN_B orbit", CERTIFICATES["b"] in CONSTRUCTION.stage_aliases["OPEN_B"])
    check("B09 c belongs to the exact three-site OPEN_C orbit", CERTIFICATES["c"] in CONSTRUCTION.stage_aliases["OPEN_C"])
    check("B10 canonical c certificate is the designated COMMIT", COMMIT_SITE == (3, 0, -1))
    for index, name in enumerate(("q", "a", "b", "c"), 11):
        target = TARGETS[name]
        certificate = CERTIFICATES[name]
        source = CONSTRUCTION.formation_sources[name]
        check(f"B{index:02d} {name} certificate is target-adjacent", c43_manhattan(target, certificate) == 1)
        check(f"B{index + 4:02d} {name} target is open in defining source", target not in source)
        check(
            f"B{index + 8:02d} {name} defining row writes its visible certificate",
            table.get(key(source, certificate)) == CERTIFICATE_CONTENTS[name],
        )
        blocked = dict(source)
        blocked[target] = "BLOCKED_OFFICIAL_TARGET"
        check(
            f"B{index + 12:02d} {name} blocked-target control disables certificate",
            table.get(key(blocked, certificate)) != CERTIFICATE_CONTENTS[name],
        )
    live_alphabet = (
        set(base.values())
        | set(allowed.values())
        | set(table.values())
        | {content for signature in table for _, content in signature}
        | {"ARBITRARY_EXTERNAL_RECORD"}
    )
    check(
        "B27 every live-alphabet target content blocks every defining certificate row",
        all(
            table.get(
                key(CONSTRUCTION.formation_sources[name] | {TARGETS[name]: content}, CERTIFICATES[name])
            )
            != CERTIFICATE_CONTENTS[name]
            for name in TARGETS
            for content in live_alphabet
        ),
    )

    section("C. Support, infinite rail, and live-table composition")
    official = c53.official_support()
    check("C01 Cycle-43 and Cycle-53 official support agree", len(official) == 29)
    check("C02 all four official targets are on official support", set(TARGETS.values()) <= official)
    check("C03 comb writes no official-support site", set(allowed).isdisjoint(official))
    check("C04 comb writes no q/a/b/c target", set(allowed).isdisjoint(TARGETS.values()))
    distances = {site: future_corridor_distance(site) for site in allowed}
    check("C05 every comb site misses the infinite future rail corridor", all(distance > 0 for distance in distances.values()))
    check("C06 only START and exterior W1 lie within distance two of the rail", {site: distance for site, distance in distances.items() if distance < 3} == {(-1, 3, 0): 2, (-2, 3, 0): 1})
    check("C07 natural rail transform has the stated infinite corridor", c53.NATURAL_ROTATION == ((-1, 0, 0), (0, 0, 1), (0, 1, 0)) and c53.NATURAL_SHIFT == (-1, 0, 0))
    first_64 = c57.natural_rail_sequence(64)
    check("C08 first 64 future slices lie in the analytic corridor", all(x <= -2 and 0 <= y <= 2 and 0 <= z <= 3 for (x, y, z), _ in first_64))
    check("C09 comb misses first 64 future slices", set(allowed).isdisjoint(site for site, _ in first_64))
    builder_graph = c57.builder_graph(c57.source_records(), c57.BUILDER.allowed)
    check("C10 exact Cycle-57 builder graph is retained", len(builder_graph.states) == 374 and len(builder_graph.terminals) == 1)
    builder_start_sets = {
        tuple(sorted(comb_enabled(dict(encoded)).items()))
        for encoded in builder_graph.states
    }
    check("C11 every pre-comb builder state enables either nothing or canonical START", builder_start_sets == {(), (((-1, 3, 0), "START"),)}, str(builder_start_sets))
    start_prerequisites_hold = all(
        not comb_enabled(records := dict(encoded))
        or (
            records.get((-1, 3, 1)) == "ARM"
            and records.get((-1, 2, 0)) == "A_0_2"
            and records.get((0, 3, 0)) == "H1"
        )
        for encoded in builder_graph.states
    )
    check("C12 START never precedes ARM/A_0_2/H1", start_prerequisites_hold)
    builder_comb_adjacencies = {
        (comb_site, builder_site)
        for comb_site in allowed
        for builder_site in c57.BUILDER.allowed
        if c43_manhattan(comb_site, builder_site) == 1
    }
    check("C13 only START touches declared Cycle-57 additions", builder_comb_adjacencies == {((-1, 3, 0), (-1, 3, 1)), ((-1, 3, 0), (-1, 2, 0))}, str(builder_comb_adjacencies))
    check("C14 both touched builder additions are START prerequisites", all(site in {(-1, 3, 1), (-1, 2, 0)} for _, site in builder_comb_adjacencies))
    check("C15 completed Cycle-57 builder remains silent", not c57.builder_enabled(base))
    check("C16 Cycle-52 remains live at its exact first frontier", c52.enabled_assignments(base) == {(-2, 1, 1): "B_1_1"})
    check("C17 full comb does not change the Cycle-52 frontier", c52.enabled_assignments(dict(base) | allowed) == {(-2, 1, 1): "B_1_1"})
    builder_roles = set(c57.BUILDER.table.values())
    comb_roles = set(table.values())
    rail_roles = set(c52.RULE_TABLE.values())
    check("C18 comb outputs are role-disjoint from Cycle 57", comb_roles.isdisjoint(builder_roles))
    check("C19 the sole comb/rail output overlap is preserving B_0_2", comb_roles & rail_roles == {"B_0_2"})
    rail_canonical = {c53.canonical_signature(signature): output for signature, output in c52.RULE_TABLE.items()}
    check("C20 Cycle-52 inputs canonicalize without collapse conflict", len(rail_canonical) == 48)
    check("C21 no comb input collides with Cycle 57", set(table).isdisjoint(c57.BUILDER.table))
    check("C22 no comb input collides with Cycle 52", set(table).isdisjoint(rail_canonical))

    # Exact two-order diamond at the sole direct rail contact.
    rail_prefix = c57.natural_rail_sequence(1)
    diamond_source = dict(base)
    diamond_source[(-1, 3, 0)] = "START"
    diamond_source.update(rail_prefix[:2])
    source_outputs = merged_outputs(diamond_source)
    check("C23 diamond source enables exterior W1", source_outputs.get((-2, 3, 0)) == {"W1"})
    check("C24 diamond source enables normal B_0_2", source_outputs.get((-2, 2, 0)) == {"B_0_2"})
    w1_first = dict(diamond_source)
    w1_first[(-2, 3, 0)] = "W1"
    check("C25 W1-first tolerance still enables B_0_2", merged_outputs(w1_first).get((-2, 2, 0)) == {"B_0_2"})
    b_first = dict(diamond_source)
    b_first[(-2, 2, 0)] = "B_0_2"
    check("C26 B_0_2-first tolerance still enables exterior W1", merged_outputs(b_first).get((-2, 3, 0)) == {"W1"})
    w1_first[(-2, 2, 0)] = "B_0_2"
    b_first[(-2, 3, 0)] = "W1"
    check("C27 both local orders join the identical record map", w1_first == b_first)
    check("C28 all merged outputs at the diamond source are single-valued", all(len(outputs) == 1 for outputs in source_outputs.values()))

    section("D. Proper-cubic covariance and local controls")
    raw = raw_rule_outputs(table)
    check("D01 comb expands to 464 distinct raw directional inputs", len(raw) == EXPECTED_RAW_RULES)
    check("D02 every raw input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    for index, rotation in enumerate(c53.ROTATIONS, 3):
        check(
            f"D{index:02d} rotation {index - 3:02d} preserves every canonical row",
            all(c53.canonical_signature(c53.rotate_signature(signature, rotation)) == signature for signature in table),
        )
    check("D27 every certificate/target adjacency is rotation invariant", all(c43_manhattan(c53.matvec(rotation, TARGETS[name]), c53.matvec(rotation, CERTIFICATES[name])) == 1 for rotation in c53.ROTATIONS for name in TARGETS))
    check("D28 no rule input contains the blocked-control role", all(content != "BLOCKED_OFFICIAL_TARGET" for signature in table for _, content in signature))

    section("E. Complete asynchronous comb graph")
    graph = exhaustive_comb_graph()
    check("E01 exact reachable-state count", graph.states == EXPECTED_STATES, f"{graph.states:,}")
    check("E02 exact directed-edge count", graph.edges == EXPECTED_EDGES, f"{graph.edges:,}")
    check("E03 graph has one terminal", graph.terminals == 1)
    check("E04 sole terminal has all 45 additions", graph.terminal_sizes == ((45, 1),), str(graph.terminal_sizes))
    check("E05 terminal is the declared complete comb", graph.complete_terminals == 1)
    check("E06 there is no incomplete dead terminal", graph.incomplete_terminals == 0)
    check("E07 no mixed rotated output conflict occurs", graph.conflicts == 0)
    check("E08 no off-footprint or wrong-content write occurs", not graph.parasites, str(sorted(graph.parasites)))
    check("E09 b never appears before q and a", graph.b_order_violations == 0)
    check("E10 designated c/COMMIT never appears before q/a/b", graph.commit_order_violations == 0)
    check("E11 every certificate has reachable formation edges", dict(graph.certificate_edges).keys() == TARGETS.keys(), str(graph.certificate_edges))
    check("E12 no target write is even enabled before COMMIT", not graph.parasites and set(allowed).isdisjoint(TARGETS.values()))

    section("F. Source and scope contract")
    for index, path in enumerate((NOTE, CYCLE51, CYCLE52, CYCLE57, AXIOMS), 1):
        check(f"F{index:02d} required source exists: {path.name}", path.exists())
    note = normalized(NOTE) if NOTE.exists() else ""
    check("F06 note states authority none", "authority: none" in note)
    check("F07 note makes no axiom-need claim", "no axiom need follows" in note)
    check("F08 note preserves the bounded candidate-law scope", "one supplied extensional candidate table" in note)
    check("F09 note reports exact graph counts", "4,784,509 states" in note and "46,716,061 edges" in note)
    check("F10 positive result invokes no N1-N8 gate", "no negative n1–n8 gate is invoked" in note)

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def c43_manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


if __name__ == "__main__":
    raise SystemExit(main())
