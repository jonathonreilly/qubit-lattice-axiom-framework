#!/usr/bin/env python3
"""Cycle 61 independent Cycle-60 composition and causal phase-chain probe.

The first half independently re-exhausts the Cycle-60 port-preserving comb and
checks that its START gate composes with every Cycle-57 builder state and the
one local Cycle-52 rail diamond.  The second half conditions on one post-COMMIT
C record at q, installs the proposed caged C->X->joint-Z phase chain, and
exhausts every proper-cubic asynchronous crossfire.  A direct C@q launch from
the unaugmented terminal is retained as a bounded failing control.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import full_a_boundary_launcher_last_cycle57_2026_07_14 as c57
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CAUSAL_PHASE_CHAIN_CYCLE61_NOTE_2026-07-14.md"
CYCLE60_RUNNER = ROOT / "scripts" / "phase_port_preserving_comb_cycle60_scratch_2026_07_14.py"
CYCLE60_NOTE = REVIEW / "PHASE_PORT_PRESERVING_COMB_CYCLE60_SCRATCH_NOTE_2026-07-14.md"
CYCLE60_RUNNER_HASH = "616d57dfd96e614b232f35516dc39399d8841ff43a7b5e30fe29bca5eee896a0"
CYCLE60_NOTE_HASH = "ee4b77e21003e626c14c1cf5f8a98073a570a2534247d626005db75c5cfe13d8"

Coord = tuple[int, int, int]
Signature = c53.Signature
PASS = 0
FAIL = 0

Q: Coord = (0, -1, 0)
A: Coord = (1, 0, 0)
B: Coord = (2, 0, 0)
C_SITE: Coord = (3, 0, 0)
P0: Coord = (0, -2, 0)
P1: Coord = (1, -2, 0)
P2: Coord = (1, -1, 0)
P3: Coord = (2, -1, 0)


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


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def enabled(records: dict[Coord, str], table: dict[Signature, str]) -> dict[Coord, str]:
    return {
        target: table[signature]
        for target in c53.open_candidates(records)
        if (signature := key(records, target)) in table
    }


def merged_outputs(records: dict[Coord, str], table: dict[Signature, str]) -> dict[Coord, set[str]]:
    outputs: dict[Coord, set[str]] = {}
    for assignments in (
        c57.builder_enabled(records),
        c52.enabled_assignments(records),
        enabled(records, table),
    ):
        for target, output in assignments.items():
            outputs.setdefault(target, set()).add(output)
    return outputs


def raw_outputs(table: dict[Signature, str]) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = {}
    for signature, output in table.items():
        for rotation in c53.ROTATIONS:
            outputs.setdefault(c53.rotate_signature(signature, rotation), set()).add(output)
    return {signature: frozenset(values) for signature, values in outputs.items()}


@dataclass(frozen=True)
class ExactGraph:
    states: frozenset[int]
    edges: int
    terminals: tuple[int, ...]
    parasites: frozenset[tuple[Coord, str]]
    conflicts: frozenset[tuple[int, Coord, tuple[str, ...]]]
    conditions: int
    sites: tuple[Coord, ...]


def exact_graph(
    base: dict[Coord, str],
    table: dict[Signature, str],
    allowed: dict[Coord, str],
) -> ExactGraph:
    """Independent exact all-rotation bitmask graph compiler and BFS."""

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
        for signature, output in table.items()
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

    queue = deque((0,))
    seen = {0}
    terminals: list[int] = []
    parasites: set[tuple[Coord, str]] = set()
    conflicts: set[tuple[int, Coord, tuple[str, ...]]] = set()
    edges = 0
    ordered = tuple(conditions)
    while queue:
        mask = queue.popleft()
        writes: dict[Coord, set[tuple[int, str]]] = {}
        for present, absent, target_bit, output, target in ordered:
            if mask & present == present and not mask & absent:
                writes.setdefault(target, set()).add((target_bit, output))
        if not writes:
            terminals.append(mask)
        for target, choices in writes.items():
            output_set = tuple(sorted({output for _, output in choices}))
            if len(output_set) != 1:
                conflicts.add((mask, target, output_set))
                continue
            target_bit, output = next(iter(choices))
            edges += 1
            if not target_bit or allowed.get(target) != output:
                parasites.add((target, output))
                continue
            future = mask | target_bit
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return ExactGraph(
        frozenset(seen), edges, tuple(terminals), frozenset(parasites),
        frozenset(conflicts), len(conditions), sites,
    )


@dataclass(frozen=True)
class PhaseConstruction:
    source: dict[Coord, str]
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    sources: dict[str, dict[Coord, str]]
    aliases: dict[str, tuple[Coord, ...]]


def build_phase() -> PhaseConstruction:
    source = dict(c60.CONSTRUCTION.base)
    source.update(c60.CONSTRUCTION.allowed)
    source[Q] = "C"
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    sources: dict[str, dict[Coord, str]] = {}
    aliases_by_name: dict[str, tuple[Coord, ...]] = {}

    def stage(name: str, target: Coord, output: str) -> None:
        signature = key(records, target)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        prior = table.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"phase output conflict: {prior}/{output}")
        table[signature] = output
        sources[name] = dict(records)
        aliases_by_name[name] = aliases
        for site in aliases:
            records[site] = output
            allowed[site] = output

    for name, target, output in (
        ("P0", P0, "P0"),
        ("P1", P1, "P1"),
        ("P2", P2, "P2"),
        ("P3", P3, "P3"),
        ("X_B", B, "X"),
        ("Z_A", A, "Z"),
        ("Z_C", C_SITE, "Z"),
    ):
        stage(name, target, output)
    return PhaseConstruction(source, table, allowed, sources, aliases_by_name)


PHASE = build_phase()


def common_targets(left: Coord, right: Coord) -> set[Coord]:
    return c52.neighbors(left) & c52.neighbors(right)


def main() -> int:
    section("A. Frozen-source and independent Cycle-60 graph review")
    check("A01 Cycle-60 runner hash matches handoff", digest(CYCLE60_RUNNER) == CYCLE60_RUNNER_HASH)
    check("A02 Cycle-60 note hash matches handoff", digest(CYCLE60_NOTE) == CYCLE60_NOTE_HASH)
    check("A03 Cycle-60 has 21 canonical rows", len(c60.CONSTRUCTION.table) == 21)
    check("A04 Cycle-60 has 52 declared additions", len(c60.CONSTRUCTION.allowed) == 52)
    check("A05 all raw Cycle-60 rows are single-valued", all(len(values) == 1 for values in raw_outputs(c60.CONSTRUCTION.table).values()))
    comb_graph = exact_graph(c60.CONSTRUCTION.base, c60.CONSTRUCTION.table, c60.CONSTRUCTION.allowed)
    complete_comb = (1 << len(comb_graph.sites)) - 1
    check("A06 independent condition census is 80", comb_graph.conditions == 80, str(comb_graph.conditions))
    check("A07 independent state census is 242,033", len(comb_graph.states) == 242_033, f"{len(comb_graph.states):,}")
    check("A08 independent edge census is 1,650,121", comb_graph.edges == 1_650_121, f"{comb_graph.edges:,}")
    check("A09 every comb schedule joins one complete terminal", comb_graph.terminals == (complete_comb,), str(Counter(mask.bit_count() for mask in comb_graph.terminals)))
    check("A10 independent graph has no parasite", not comb_graph.parasites, str(sorted(comb_graph.parasites)))
    check("A11 independent graph has no conflict", not comb_graph.conflicts)
    comb_index = {site: index for index, site in enumerate(comb_graph.sites)}
    cert_bits = {name: 1 << comb_index[site] for name, site in c59.CERTIFICATES.items()}
    check("A12 OPEN_B never precedes q/a certificates", all(not mask & cert_bits["b"] or mask & cert_bits["q"] and mask & cert_bits["a"] for mask in comb_graph.states))
    check("A13 OPEN_C never precedes q/a/b certificates", all(not mask & cert_bits["c"] or all(mask & cert_bits[name] for name in ("q", "a", "b")) for mask in comb_graph.states))

    section("B. Live Cycle-57 builder and infinite-rail composition")
    builder_graph = c57.builder_graph(c57.source_records(), c57.BUILDER.allowed)
    start_sets = {
        tuple(sorted(enabled(dict(state), c60.CONSTRUCTION.table).items()))
        for state in builder_graph.states
    }
    check("B01 all 374 builder states are independently enumerated", len(builder_graph.states) == 374)
    check("B02 pre-comb output is only absent or canonical START", start_sets == {(), (((-1, 3, 0), "START"),)}, str(start_sets))
    check(
        "B03 every enabled START already has ARM/A_0_2/H1",
        all(
            not enabled(records := dict(state), c60.CONSTRUCTION.table)
            or records.get((-1, 3, 1)) == "ARM"
            and records.get((-1, 2, 0)) == "A_0_2"
            and records.get((0, 3, 0)) == "H1"
            for state in builder_graph.states
        ),
    )
    adjacencies = {
        (comb_site, builder_site)
        for comb_site in c60.CONSTRUCTION.allowed
        for builder_site in c57.BUILDER.allowed
        if c59.c43_manhattan(comb_site, builder_site) == 1
    }
    check("B04 only START touches builder additions", adjacencies == {((-1, 3, 0), (-1, 3, 1)), ((-1, 3, 0), (-1, 2, 0))}, str(adjacencies))
    check("B05 both touched additions are prior START parents", all(site in {(-1, 3, 1), (-1, 2, 0)} for _, site in adjacencies))
    raw_comb = raw_outputs(c60.CONSTRUCTION.table)
    check("B06 no raw Cycle-57 input collision", set(raw_comb).isdisjoint(c57.raw_builder_outputs()))
    check("B07 no raw Cycle-52 input collision", set(raw_comb).isdisjoint(c52.RULE_OUTPUTS))
    near_rail = {
        site: c59.future_corridor_distance(site)
        for site in c60.CONSTRUCTION.allowed
        if c59.future_corridor_distance(site) < 3
    }
    check("B08 only START/exterior-W1 approach the infinite corridor", near_rail == {(-1, 3, 0): 2, (-2, 3, 0): 1}, str(near_rail))
    rail_prefix = c57.natural_rail_sequence(1)
    diamond = dict(c60.CONSTRUCTION.base)
    diamond[(-1, 3, 0)] = "START"
    diamond.update(rail_prefix[:2])
    source_outputs = merged_outputs(diamond, c60.CONSTRUCTION.table)
    check("B09 diamond source enables both W1 and B_0_2", source_outputs.get((-2, 3, 0)) == {"W1"} and source_outputs.get((-2, 2, 0)) == {"B_0_2"})
    w1_first = dict(diamond)
    w1_first[(-2, 3, 0)] = "W1"
    b_first = dict(diamond)
    b_first[(-2, 2, 0)] = "B_0_2"
    check("B10 W1-first retains B_0_2", merged_outputs(w1_first, c60.CONSTRUCTION.table).get((-2, 2, 0)) == {"B_0_2"})
    check("B11 B_0_2-first retains W1", merged_outputs(b_first, c60.CONSTRUCTION.table).get((-2, 3, 0)) == {"W1"})
    w1_first[(-2, 2, 0)] = "B_0_2"
    b_first[(-2, 3, 0)] = "W1"
    check("B12 the two orders join exactly", w1_first == b_first)
    check("B13 every other comb site is infinite-tail separated", all(c59.future_corridor_distance(site) >= 3 for site in c60.CONSTRUCTION.allowed if site not in {(-1, 3, 0), (-2, 3, 0)}))

    section("C. Conditional causal phase geometry")
    check("C01 phase source contains the all-four OPEN_C commit", PHASE.source.get(c59.CERTIFICATES["c"]) == "OPEN_C")
    check("C02 C@q is explicitly conditional input", PHASE.source.get(Q) == "C" and Q not in PHASE.allowed)
    check("C03 phase table has seven canonical rows", len(PHASE.table) == 7)
    check("C04 every staged phase signature class is singleton", all(PHASE.aliases[name] == (site,) for name, site in {"P0": P0, "P1": P1, "P2": P2, "P3": P3, "X_B": B, "Z_A": A, "Z_C": C_SITE}.items()), str(PHASE.aliases))
    phase_map = {Q: "C"} | PHASE.allowed
    check("C05 official outputs are exactly C@q, Z@a, X@b, Z@c", {site: output for site, output in phase_map.items() if site in c53.official_support()} == {Q: "C", A: "Z", B: "X", C_SITE: "Z"})
    check("C06 four relay sites remain off official support", {P0, P1, P2, P3}.isdisjoint(c53.official_support()))
    cage_rows = (
        ("P0", Q, (0, -2, -1), P0, (0, -1, -1), "W6"),
        ("P1", P0, (1, -2, -1), P1, (0, -2, -1), "OPEN_B"),
        ("P2", P1, (1, -1, -1), P2, (1, -2, -1), "E"),
        ("P3", P2, (2, -1, -1), P3, (1, -1, -1), "J6"),
        ("X_B", P3, (2, 0, -1), B, (2, -1, -1), "E"),
        ("Z_A", B, (1, 0, -1), A, (2, 0, -1), "OPEN_B"),
        ("Z_C", B, (3, 0, -1), C_SITE, (2, 0, -1), "OPEN_B"),
    )
    for index, (name, left, right, target, alternate, alternate_content) in enumerate(cage_rows, 7):
        check(
            f"C{index:02d} {name} has exactly one occupied alternate common target",
            common_targets(left, right) == {target, alternate}
            and PHASE.sources[name].get(alternate) == alternate_content,
        )
    union_table = dict(c60.CONSTRUCTION.table)
    union_table.update(PHASE.table)
    raw_union = raw_outputs(union_table)
    check("C14 union has 28 canonical rows", len(union_table) == 28)
    check("C15 union has 544 distinct raw rows", len(raw_union) == 544, str(len(raw_union)))
    check("C16 all rotated union rows are single-valued", all(len(outputs) == 1 for outputs in raw_union.values()))

    section("D. Exhaustive conditional phase graph")
    phase_graph = exact_graph(PHASE.source, union_table, PHASE.allowed)
    complete_phase = (1 << len(phase_graph.sites)) - 1
    check("D01 compiled phase condition count is eight", phase_graph.conditions == 8, str(phase_graph.conditions))
    check("D02 phase graph has nine states", len(phase_graph.states) == 9, str(len(phase_graph.states)))
    check("D03 phase graph has nine edges", phase_graph.edges == 9, str(phase_graph.edges))
    check("D04 every phase schedule joins one complete terminal", phase_graph.terminals == (complete_phase,))
    check("D05 phase graph has no parasite", not phase_graph.parasites, str(sorted(phase_graph.parasites)))
    check("D06 phase graph has no conflict", not phase_graph.conflicts)
    phase_index = {site: index for index, site in enumerate(phase_graph.sites)}
    def bit(site: Coord) -> int:
        return 1 << phase_index[site]
    check("D07 X@b never precedes P0/P1/P2/P3", all(not mask & bit(B) or all(mask & bit(site) for site in (P0, P1, P2, P3)) for mask in phase_graph.states))
    check("D08 Z@a never precedes X@b", all(not mask & bit(A) or mask & bit(B) for mask in phase_graph.states))
    check("D09 Z@c never precedes X@b", all(not mask & bit(C_SITE) or mask & bit(B) for mask in phase_graph.states))
    check("D10 endpoint Z writes commute", sum(1 for mask in phase_graph.states if mask.bit_count() == 6) == 2)
    terminal_records = dict(PHASE.source)
    terminal_records.update(PHASE.allowed)
    check("D11 phase terminal leaves Cycle-52 first frontier unchanged", c52.enabled_assignments(terminal_records) == {(-2, 1, 1): "B_1_1"})
    check("D12 phase auxiliaries are separated from infinite rail", all(c59.future_corridor_distance(site) >= 3 for site in PHASE.allowed))

    section("E. Direct C@q launch control")
    comb_terminal = dict(c60.CONSTRUCTION.base)
    comb_terminal.update(c60.CONSTRUCTION.allowed)
    q_signature = key(comb_terminal, Q)
    a_signature = key(comb_terminal, A)
    q_aliases = tuple(c53.signature_classes(comb_terminal).get(q_signature, ()))
    check("E01 q and a have the same terminal rotated signature", q_signature == a_signature)
    check("E02 direct W6+Z0 launch class is exactly q/a", set(q_aliases) == {Q, A}, str(q_aliases))
    check("E03 direct C row would occupy a before Z@a", A in q_aliases and PHASE.allowed[A] == "Z")
    precommit = dict(c60.CONSTRUCTION.base)
    precommit.update({site: output for site, output in c60.CONSTRUCTION.allowed.items() if output in {"START", "W1", "W2", "W3", "W4", "W5", "W6"}})
    early_aliases = tuple(c53.signature_classes(precommit).get(key(precommit, Q), ()))
    check("E04 same q/a launch is enabled before OPEN_C", set(early_aliases) == {Q, A} and c59.CERTIFICATES["c"] not in precommit)
    check("E05 conditional phase table contains no hidden C launcher", "C" not in PHASE.table.values())
    check("E06 bounded residual is a completion-return launcher, not phase-chain geometry", len(PHASE.table) == 7 and len(phase_graph.states) == 9 and set(q_aliases) == {Q, A})

    section("F. Scope and no-go-discipline contract")
    check("F01 Cycle-61 note exists", NOTE.exists())
    note = normalized(NOTE) if NOTE.exists() else ""
    check("F02 note states authority none", "authority: none" in note)
    check("F03 note states conditional C@q boundary", "conditional on one post-commit c@q" in note)
    check("F04 note makes no axiom claim", "no axiom need follows" in note)
    check("F05 note names the exact residual", "commit_to_q_phase_launch" in note)
    for number in range(1, 9):
        check(f"F{number + 5:02d} fresh N{number} section exists", f"n{number} —" in note)
    check("F14 rhetoric remains bounded", "not a no-go against a completion-return path" in note)

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
