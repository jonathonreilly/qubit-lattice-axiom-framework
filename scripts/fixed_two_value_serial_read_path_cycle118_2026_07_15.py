#!/usr/bin/env python3
"""Cycle 118: fixed-position two-value serial read path.

Cycle 112 already contains the smallest possible row delta for a bounded
operational positional read: zero.  Its completion table has one row which
consumes indexed D5=H1 and records T_H2 at a read-port cell, followed by one
row which consumes indexed D4=H0 plus that T_H2 port and records T_N1 at the
next port.  Two proper-cubic-equivalent copies of this serial path are present.

This runner extracts that path and exhausts the complete Cycle-112 graph to
verify causal ordering in every reachable state.  It then replays rail,
proper-cubic, corrupted-boundary, and typed-H0 controls.  The result closes a
two-position fixed serial status path only.  It does not select an index, vary
one common port with a candidate, cover all eight positions, or select L*.

Authority: none.  No predecessor, foundation, axiom, primitive, registry,
queue, policy, audit, or git state is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
sys.path.insert(0, str(SCRIPTS))

import eight_bit_status_completion_front_cycle112_2026_07_15 as c112  # noqa: E402


NOTE = REVIEW / "FIXED_TWO_VALUE_SERIAL_READ_PATH_CYCLE118_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle112": REVIEW / "EIGHT_BIT_STATUS_COMPLETION_FRONT_CYCLE112_NOTE_2026-07-15.md",
    "cycle114": REVIEW / "LAWFUL_H0_REFERENCE_FORK_CYCLE114_NOTE_2026-07-15.md",
    "cycle115": REVIEW / "FIRST_AUTONOMOUS_SUCCESSOR_ROLE_PORT_CYCLE115_NOTE_2026-07-15.md",
    "cycle116": REVIEW / "POST_CYCLE115_ADDRESS_SEMANTICS_AUDIT_CYCLE116_NOTE_2026-07-15.md",
}

Coord = c112.Coord
Signature = c112.Signature
H0 = c112.H0
H1 = c112.H1
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def has_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle.lower() in text for needle in needles)


# ---------------------------------------------------------------------------
# Two exact serial read paths already present in Cycle 112.
#
# Each path reads the fixed positional pair D5=H1 then D4=H0.  T_H2 and T_N1
# are distinct carrier records.  The carrier interpretation is local and
# injective: T_H2 records completion of the H1 read, while T_N1 records the
# subsequent H0 read in the presence of T_H2.
# ---------------------------------------------------------------------------

SOURCE_H1 = c112.D5
SOURCE_H0 = c112.D4

CHAIN_A: tuple[Coord, Coord, Coord, Coord] = (
    SOURCE_H1,
    c112.PAIR_IMAGES[0],
    SOURCE_H0,
    c112.SIGNAL_D4_IMAGES[0],
)
CHAIN_B: tuple[Coord, Coord, Coord, Coord] = (
    SOURCE_H1,
    c112.PAIR_IMAGES[2],
    SOURCE_H0,
    c112.SIGNAL_D4_IMAGES[1],
)
CHAINS = (CHAIN_A, CHAIN_B)

PORT_H1_OUTPUT = c112.PAIR_OUTPUT
PORT_H0_OUTPUT = c112.SIGNAL_D4_OUTPUT
PORT_CODE = {PORT_H1_OUTPUT: H1, PORT_H0_OUTPUT: H0}

READER_TABLE = {
    local: output
    for local, output in c112.COMPLETION_TABLE.items()
    if output in PORT_CODE
}
READER_RAW = c112.c59.raw_rule_outputs(READER_TABLE)

CHAIN_A_H1_LOCAL: Signature = (
    ((-1, 0, 0), H1),
    ((0, 1, 0), c112.RELAY_IMAGE_OUTPUT),
)
CHAIN_A_H0_LOCAL: Signature = (
    ((-1, 0, 0), H0),
    ((0, 1, 0), PORT_H1_OUTPUT),
)
CHAIN_B_H1_LOCAL: Signature = (
    ((0, 0, -1), H1),
    ((0, 1, 0), c112.RELAY_IMAGE_OUTPUT),
)
CHAIN_B_H0_LOCAL: Signature = (
    ((0, 0, -1), H0),
    ((0, 1, 0), PORT_H1_OUTPUT),
)
CHAIN_LOCALS = (
    (CHAIN_A_H1_LOCAL, CHAIN_A_H0_LOCAL),
    (CHAIN_B_H1_LOCAL, CHAIN_B_H0_LOCAL),
)

CLOSED = "FIXED_POSITION_TWO_VALUE_SERIAL_STATUS_PATH"
NEXT = "CANDIDATE_SELECTED_COMMON_REFERENCE_PORT"


@dataclass(frozen=True)
class ReaderGraphStats:
    states: int
    edges: int
    terminals: int
    terminal_sizes: tuple[int, ...]
    bad: tuple[object, ...]
    violations: tuple[object, ...]
    chain_counts: tuple[tuple[int, int, int, int], ...]
    earliest_sizes: tuple[tuple[int, int, int, int], ...]
    completed_counts: tuple[int, ...]
    port_edge_counts: tuple[tuple[int, int], ...]


def exhaust_reader_graph() -> ReaderGraphStats:
    """Re-exhaust Cycle 112 while auditing both serial read causal chains."""

    compiled = c112.compile_conditions(
        c112.SOURCE,
        c112.GROWN_OUTPUTS,
        c112.FULL_RAW,
        c112.RAIL_ZERO,
    )
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals: list[int] = []
    bad: list[object] = []
    edge_counts: Counter[Coord] = Counter()

    while queue:
        state = queue.popleft()
        legal: list[int] = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present_mask, neighbourhood_mask, values in conditions:
                if state & neighbourhood_mask != present_mask:
                    continue
                if target in c112.RAIL_ZERO and values == c112.RAIL_ZERO[target]:
                    break
                if (
                    index is not None
                    and values == frozenset((c112.GROWN_OUTPUTS[target],))
                ):
                    legal.append(index)
                    break
                bad.append((state, target, values))
                break
            if bad:
                break
        if bad:
            break
        if not legal:
            terminals.append(state)
        for index in legal:
            edge_counts[compiled.sites[index]] += 1
            future = state | 1 << index
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    violations: list[object] = []
    chain_counts: list[tuple[int, int, int, int]] = []
    earliest_sizes: list[tuple[int, int, int, int]] = []
    completed_counts: list[int] = []
    port_edge_counts: list[tuple[int, int]] = []
    for chain_index, (source_h1, port_h1, source_h0, port_h0) in enumerate(CHAINS):
        sites = (source_h1, port_h1, source_h0, port_h0)
        indices = tuple(compiled.index[site] for site in sites)
        counts = tuple(
            sum(bool(state >> index & 1) for state in seen)
            for index in indices
        )
        earliest = tuple(
            min(state.bit_count() for state in seen if state >> index & 1)
            for index in indices
        )
        for state in seen:
            source_h1_present = bool(state >> indices[0] & 1)
            port_h1_present = bool(state >> indices[1] & 1)
            source_h0_present = bool(state >> indices[2] & 1)
            port_h0_present = bool(state >> indices[3] & 1)
            if port_h1_present and not source_h1_present:
                violations.append((chain_index, "H1-port-before-source", state))
            if port_h0_present and not (
                source_h0_present and port_h1_present
            ):
                violations.append((chain_index, "H0-port-before-source-or-H1-port", state))
        chain_counts.append(counts)
        earliest_sizes.append(earliest)
        completed_counts.append(
            sum(
                bool(state >> indices[1] & 1 and state >> indices[3] & 1)
                for state in seen
            )
        )
        port_edge_counts.append((edge_counts[port_h1], edge_counts[port_h0]))

    return ReaderGraphStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_sizes=tuple(sorted(state.bit_count() for state in terminals)),
        bad=tuple(bad),
        violations=tuple(violations),
        chain_counts=tuple(chain_counts),
        earliest_sizes=tuple(earliest_sizes),
        completed_counts=tuple(completed_counts),
        port_edge_counts=tuple(port_edge_counts),
    )


READER_GRAPH = exhaust_reader_graph()


def source_and_primitive_contract() -> None:
    section("A - Sources, retained boundary, and primitive registry")
    for name, path in {"cycle118_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registry contains only the four canonical premise nodes",
        set(nodes) == {
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        },
        str(sorted(nodes)),
    )
    check(
        "A primitive current paths are consumed literally",
        all(
            ROOT / nodes[node]["current_path"] == SOURCES[key]
            for node, key in (
                ("scale_reference_primitive", "scale"),
                ("kinetic_isotropy_primitive", "kinetic"),
                ("realized_state_primitive", "realized"),
            )
        ),
    )
    texts = {key: normalized(path) for key, path in SOURCES.items()}
    check(
        "A primitive scopes remain units-only, form-only, and pointwise-only",
        has_all(texts["scale"], ("units conversion, not a physics axiom", "zero dimensionless content"))
        and has_all(texts["kinetic"], ("c_t = c_s", "not a new dynamics", "no mass ratio"))
        and has_all(texts["realized"], ("pointwise evaluation", "no state, averaging over alternatives", "measure, weighting")),
    )
    check(
        "A Record makes only records readable and content determines readout",
        has_all(texts["axioms"], (
            "only records are readable",
            "a readout value is determined by record content alone",
            "records are permanent",
        )),
    )
    check(
        "A Cycle116 names exactly the I2 read-path residual now tested",
        has_all(texts["cycle116"], (
            "layout positive / read path open",
            "operational positional readout",
            "candidate_selected_common_reference_port",
        )),
    )


def literal_reader_contract() -> None:
    section("B - Zero-row two-value serial reader extraction")
    check(
        "B Cycle112 source and full table remain exact",
        len(c112.SOURCE) == 264
        and len(c112.FULL_RAW) == 8_048
        and len(c112.GROWN_OUTPUTS) == 69,
    )
    check(
        "B fixed indexed sources are generated D5=H1 and D4=H0 records",
        SOURCE_H1 == c112.DATA_SITES[5]
        and SOURCE_H0 == c112.DATA_SITES[4]
        and c112.GROWN_OUTPUTS[SOURCE_H1] == H1
        and c112.GROWN_OUTPUTS[SOURCE_H0] == H0
        and SOURCE_H1 not in c112.SOURCE
        and SOURCE_H0 not in c112.SOURCE,
    )
    check(
        "B selected ports are generated records and disjoint from their sources",
        all(
            port not in c112.SOURCE
            and c112.GROWN_OUTPUTS[port] == output
            for chain in CHAINS
            for port, output in (
                (chain[1], PORT_H1_OUTPUT),
                (chain[3], PORT_H0_OUTPUT),
            )
        )
        and all(len(set(chain)) == 4 for chain in CHAINS),
    )
    check(
        "B reader is exactly two inherited canonical / 48 raw rows",
        len(READER_TABLE) == 2
        and len(READER_RAW) == 48
        and set(READER_TABLE.items()).issubset(c112.COMPLETION_TABLE.items())
        and set(READER_RAW).issubset(c112.FULL_RAW),
    )
    check(
        "B each H1 port consumes indexed H1 plus R_A31 and records T_H2",
        all(c112.FULL_RAW[locals_[0]] == frozenset((PORT_H1_OUTPUT,)) for locals_ in CHAIN_LOCALS),
    )
    check(
        "B each H0 port consumes indexed H0 plus prior T_H2 and records T_N1",
        all(c112.FULL_RAW[locals_[1]] == frozenset((PORT_H0_OUTPUT,)) for locals_ in CHAIN_LOCALS),
    )
    check(
        "B port code is an injective content-only two-role carrier",
        PORT_CODE == {"T_H2": H1, "T_N1": H0}
        and len(PORT_CODE) == len(set(PORT_CODE.values())) == 2,
    )
    check(
        "B Cycle118 adds zero law rows and zero supplied records",
        READER_TABLE.keys() <= c112.COMPLETION_TABLE.keys()
        and READER_RAW.keys() <= c112.FULL_RAW.keys(),
    )
    terminal = c112.positive_terminal_records()
    check(
        "B every direct D5 neighbour is already occupied in the retained terminal",
        all(
            c112.c53.add(SOURCE_H1, direction) in terminal
            for direction in c112.c53.DIRECTIONS
        ),
    )


def exhaustive_causality_contract() -> None:
    section("C - Every-schedule causal-order exhaustion")
    check(
        "C reader graph exactly replays Cycle112's complete graph",
        READER_GRAPH.states == c112.POSITIVE.states == 73_656
        and READER_GRAPH.edges == c112.POSITIVE.edges == 430_754
        and READER_GRAPH.terminals == c112.POSITIVE.terminals == 1
        and READER_GRAPH.terminal_sizes == c112.POSITIVE.terminal_sizes == (69,)
        and not READER_GRAPH.bad,
        str(READER_GRAPH),
    )
    check(
        "C no reachable state contains a port before its indexed prerequisite",
        not READER_GRAPH.violations,
        str(READER_GRAPH.violations[:1]),
    )
    check(
        "C chain A state counts and first reachable sizes are pinned",
        READER_GRAPH.chain_counts[0] == (4_672, 2_464, 2_176, 768)
        and READER_GRAPH.earliest_sizes[0] == (50, 52, 54, 57)
        and READER_GRAPH.completed_counts[0] == 768
        and READER_GRAPH.port_edge_counts[0] == (1_472, 640),
        (
            f"counts={READER_GRAPH.chain_counts[0]} "
            f"earliest={READER_GRAPH.earliest_sizes[0]} "
            f"completed={READER_GRAPH.completed_counts[0]} "
            f"edges={READER_GRAPH.port_edge_counts[0]}"
        ),
    )
    check(
        "C chain B state counts and first reachable sizes are pinned",
        READER_GRAPH.chain_counts[1] == (4_672, 1_920, 2_176, 544)
        and READER_GRAPH.earliest_sizes[1] == (50, 52, 54, 57)
        and READER_GRAPH.completed_counts[1] == 544
        and READER_GRAPH.port_edge_counts[1] == (1_376, 544),
        (
            f"counts={READER_GRAPH.chain_counts[1]} "
            f"earliest={READER_GRAPH.earliest_sizes[1]} "
            f"completed={READER_GRAPH.completed_counts[1]} "
            f"edges={READER_GRAPH.port_edge_counts[1]}"
        ),
    )
    terminal = c112.positive_terminal_records()
    check(
        "C unique terminal contains both complete serial reader copies",
        all(
            terminal[chain[0]] == H1
            and terminal[chain[1]] == PORT_H1_OUTPUT
            and terminal[chain[2]] == H0
            and terminal[chain[3]] == PORT_H0_OUTPUT
            for chain in CHAINS
        ),
    )


def equivalent_geometry_contract() -> None:
    section("D - Proper-cubic-equivalent fixed read-port geometry")
    matching = []
    for rotation in c112.c53.ROTATIONS:
        rotated_source = c112.c53.matvec(rotation, SOURCE_H1)
        shift = tuple(SOURCE_H1[index] - rotated_source[index] for index in range(3))
        transformed = tuple(
            tuple(
                c112.c53.matvec(rotation, site)[index] + shift[index]
                for index in range(3)
            )
            for site in CHAIN_A
        )
        if transformed == CHAIN_B:
            matching.append((rotation, shift))
    check(
        "D the two serial paths are related by a proper cubic motion",
        len(matching) >= 1,
        f"matches={len(matching)}",
    )
    check(
        "D both H1 locals share one canonical signature orbit",
        c112.c53.canonical_signature(CHAIN_A_H1_LOCAL)
        == c112.c53.canonical_signature(CHAIN_B_H1_LOCAL)
        in READER_TABLE
        and READER_TABLE[c112.c53.canonical_signature(CHAIN_A_H1_LOCAL)]
        == PORT_H1_OUTPUT,
    )
    check(
        "D both H0 locals share one canonical signature orbit",
        c112.c53.canonical_signature(CHAIN_A_H0_LOCAL)
        == c112.c53.canonical_signature(CHAIN_B_H0_LOCAL)
        in READER_TABLE
        and READER_TABLE[c112.c53.canonical_signature(CHAIN_A_H0_LOCAL)]
        == PORT_H0_OUTPUT,
    )
    failures = []
    for local, values in READER_RAW.items():
        for rotation in c112.c53.ROTATIONS:
            if READER_RAW.get(c112.c53.rotate_signature(local, rotation)) != values:
                failures.append((local, rotation, values))
                break
    check(
        "D all 1,152 reader-row proper-cubic images preserve output",
        len(READER_RAW) * 24 == 1_152 and not failures,
        str(failures[:1]),
    )


def rail_contract() -> None:
    section("E - Rail separation and exact locality product")
    terminal = c112.positive_terminal_records()
    completed, failures = c112.append_rail(terminal)
    check(
        "E completed reader retains all 96 exact singleton rail appends",
        not failures
        and c112.enabled(completed)
        == {c112.c105.NEXT_RAIL[0]: frozenset((c112.c105.NEXT_RAIL[1],))},
        str(failures[:1]),
    )

    rail_only = dict(c112.SOURCE)
    hits = []
    for prefix in range(c112.c105.RAIL_HORIZON + 1):
        for target in c112.c53.open_candidates(rail_only):
            local = c112.c53.local_signature(rail_only, target)
            if local in READER_RAW:
                hits.append((prefix, target, local))
        if prefix < c112.c105.RAIL_HORIZON:
            site, output = c112.c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    reader_sites = {
        site
        for chain in CHAINS
        for site in chain
    }
    rail_sites = {
        site
        for site, _output in c112.c105.RAIL_SEQUENCE[: c112.c105.RAIL_HORIZON]
    }
    distance = min(
        c112.c101.manhattan(left, right)
        for left in reader_sites
        for right in rail_sites
    )
    check(
        "E reader support is rail-separated with zero 97-prefix aliases",
        distance >= 7 and not hits,
        f"distance={distance} hits={hits[:1]}",
    )
    product_states = c112.POSITIVE.states * (c112.c105.RAIL_HORIZON + 1)
    product_edges = (
        c112.POSITIVE.edges * (c112.c105.RAIL_HORIZON + 1)
        + c112.POSITIVE.states * c112.c105.RAIL_HORIZON
    )
    check(
        "E exact reader x 97-prefix product is 7,144,632 states / 48,854,114 edges",
        product_states == 7_144_632 and product_edges == 48_854_114,
        f"states={product_states} edges={product_edges}",
    )


def corruption_contract() -> None:
    section("F - Wrong-word and typed-H0 fail-closed controls")
    failures = []
    observed = []
    corrupt_terminals = []
    reader_ports = {chain[1] for chain in CHAINS} | {chain[3] for chain in CHAINS}
    for index, site in enumerate(c112.c100.CODE_SITES):
        source = dict(c112.SOURCE)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(c112.GROWN_OUTPUTS)
        if index == 5:
            outputs[c112.c101.BIT5_REJECT] = H1
        stats = c112.append_graph(source, outputs)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or reader_ports & stats.reached
            or {SOURCE_H1, SOURCE_H0} & stats.reached
        ):
            failures.append((f"bit-{index}", stats))
            continue
        corrupt_terminals.append(
            c112.records_at(stats.terminal_states[0], source, outputs)
        )

    for label, site in (("valid", c112.c100.VALID), ("ready", c112.c100.READY)):
        source = dict(c112.SOURCE)
        source[site] = H0
        stats = c112.append_graph(source)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or reader_ports & stats.reached
            or {SOURCE_H1, SOURCE_H0} & stats.reached
        ):
            failures.append((label, stats))
            continue
        corrupt_terminals.append(
            c112.records_at(stats.terminal_states[0], source, c112.GROWN_OUTPUTS)
        )

    expected = [
        (1_080, 3_522, (30,)),
        (920, 2_938, (29,)),
        (760, 2_354, (28,)),
        (520, 1_438, (27,)),
        (120, 238, (20,)),
        (200, 490, (20,)),
        (80, 152, (18,)),
        (60, 109, (17,)),
        (40, 66, (16,)),
        (20, 23, (15,)),
    ]
    check(
        "F all eight bit flips plus wrong VALID/READY stop before either read source or port",
        len(corrupt_terminals) == 10 and not failures,
        str(failures[:1]),
    )
    check(
        "F corrupted graph census remains exact",
        observed == expected,
        str(observed),
    )
    rail_failures = []
    for index, terminal in enumerate(corrupt_terminals):
        _completed, local_failures = c112.append_rail(terminal)
        if local_failures:
            rail_failures.append((index, local_failures[0]))
    check(
        "F all ten corrupt terminals retain 96 exact rail appends",
        not rail_failures,
        str(rail_failures[:1]),
    )

    fault_source = c112.c109.fault_records(3)
    fault_outputs = {
        site: output
        for site, output in c112.EXTENSION_OUTPUTS.items()
        if site not in fault_source
    }
    fault_outputs[c112.GUARD_SPINE[1]] = H1
    fault_outputs[c112.GUARD_SPINE[2]] = H1
    fault_stats = c112.append_graph(fault_source, fault_outputs)
    check(
        "F typed-H0 reject exhausts to two partial terminals with no selected reader port",
        fault_stats.states == 44
        and fault_stats.edges == 97
        and fault_stats.terminals == 2
        and fault_stats.terminal_sizes == (6, 7)
        and not fault_stats.bad
        and not (reader_ports & fault_stats.reached),
        (
            f"states={fault_stats.states} edges={fault_stats.edges} "
            f"sizes={fault_stats.terminal_sizes} reached_ports={reader_ports & fault_stats.reached}"
        ),
    )


def rotated_terminal_contract() -> None:
    section("G - Rotated completed-history controls")
    completed, failures = c112.append_rail(c112.positive_terminal_records())
    shift = (181, -113, 97)
    rotated_failures = []
    for rotation in c112.c53.ROTATIONS:
        transformed = c112.c105.transform_records(completed, rotation, shift)
        next_site = c112.c101.transform_site(
            c112.c105.NEXT_RAIL[0],
            rotation,
            shift,
        )
        expected = {next_site: frozenset((c112.c105.NEXT_RAIL[1],))}
        actual = c112.enabled(transformed)
        if actual != expected:
            rotated_failures.append((rotation, expected, actual))
            break
        for chain in CHAINS:
            for site, output in (
                (chain[0], H1),
                (chain[1], PORT_H1_OUTPUT),
                (chain[2], H0),
                (chain[3], PORT_H0_OUTPUT),
            ):
                rotated_site = c112.c101.transform_site(site, rotation, shift)
                if transformed.get(rotated_site) != output:
                    rotated_failures.append((rotation, site, output))
                    break
            if rotated_failures:
                break
        if rotated_failures:
            break
    check(
        "G all 24 rotated complete readers expose only the rotated next rail",
        not failures and not rotated_failures,
        str(rotated_failures[:1]),
    )
    full_failures = []
    controls = 0
    for local, values in c112.FULL_RAW.items():
        for rotation in c112.c53.ROTATIONS:
            controls += 1
            if c112.FULL_RAW.get(c112.c53.rotate_signature(local, rotation)) != values:
                full_failures.append((local, rotation, values))
                break
    check(
        "G all 193,152 full-law proper-cubic images preserve output",
        controls == len(c112.FULL_RAW) * 24 == 193_152
        and not full_failures,
        str(full_failures[:1]),
    )


def scope_and_note_contract() -> None:
    section("H - I2 closure, I3 firewall, and constitutional delta")
    note = normalized(NOTE)
    check(
        "H note states the exact zero-row bounded I2 closure",
        has_all(note, (
            "fixed_position_two_value_serial_status_path",
            "zero new rows",
            "d5=h1",
            "d4=h0",
            "t_h2",
            "t_n1",
        )),
    )
    check(
        "H note keeps candidate-selected same-port I3 open",
        has_all(note, (
            "candidate_selected_common_reference_port",
            "different successive port cells",
            "no candidate chooses",
        )),
    )
    check(
        "H note distinguishes status transport from literal H-bit copying",
        has_all(note, (
            "serial status path",
            "carrier code",
            "does not claim a literal h1/h0 copy",
        )),
    )
    check(
        "H note records zero constitutional delta and read-after-formation chronology",
        has_all(note, (
            "constitutional delta is zero",
            "source record forms first",
            "reading does not cause the source record to form",
            "no axiom addition follows",
        )),
    )
    check(
        "H note carries complete N1-N8 discipline with at least five routes",
        all(f"n{index}" in note for index in range(1, 9))
        and note.count("attempted") >= 5,
    )
    check(
        "H broad no-go is rejected and exact next object is retained",
        has_all(note, (
            "fail for any universal no-go",
            "partial-narrowing-with-live-constructive-routes",
            "next candidate_selected_common_reference_port",
        )),
    )
    check(
        "H primitive scopes and selected-law firewall remain explicit",
        has_all(note, (
            "units only",
            "c_t=c_s form only",
            "pointwise realized-state reference only",
            "probe table is not nature's selected law",
        )),
    )


def main() -> int:
    source_and_primitive_contract()
    literal_reader_contract()
    exhaustive_causality_contract()
    equivalent_geometry_contract()
    rail_contract()
    corruption_contract()
    rotated_terminal_contract()
    scope_and_note_contract()
    print("\n" + "=" * 79)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print(f"READER_CANONICAL={len(READER_TABLE)} READER_RAW={len(READER_RAW)} NEW_ROWS=0")
    print(
        f"LOCAL_STATES={READER_GRAPH.states} LOCAL_EDGES={READER_GRAPH.edges} "
        f"TERMINALS={READER_GRAPH.terminals}"
    )
    print(f"CLOSED={CLOSED}")
    print(f"NEXT={NEXT}")
    print("I2=BOUNDED_TWO_POSITION_SERIAL_STATUS_PATH")
    print("I3=OPEN_CANDIDATE_SELECTED_COMMON_PORT")
    print("CONSTITUTIONAL_DELTA=ZERO")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
