#!/usr/bin/env python3
"""Cycle 91: revise compiler closure against the live Cycle-85 law.

The runner rebuilds the eight-bit role code, six-slot program bank, and
Patricia census for the corrected 236-row/153-role selected route.  It then
rechecks the Cycle-86 openness encoder under that live union and tests the
Cycle-87 router both in isolation and inside one actual arity-five recurrent
row's supplied Cycle-82 pipeline.  The latter exposes a concrete mixed-harness
parasite, so the result is a revised construction boundary, not a no-go.

Authority: none.  No foundation, registry, queue, audit, or git authority is
exercised.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
sys.path.insert(0, str(SCRIPTS))

import constructive_constitutional_delta_audit_cycle83_2026_07_14 as c83  # noqa: E402
import cycle80_recurrence_audit_endpoint_tube_nucleation_cycle85_2026_07_14 as c85  # noqa: E402
import directional_multiword_rule_port_output_cycle82_2026_07_14 as c82  # noqa: E402
import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81  # noqa: E402
import four_open_reservation_comb_cycle59_2026_07_14 as c59  # noqa: E402
import live_directional_program_writer_cycle90_2026_07_15 as c90  # noqa: E402
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89  # noqa: E402
import live_empty_caged_router_patricia_cycle92_2026_07_15 as c92  # noqa: E402
import open_direction_empty_slot_cycle86_2026_07_14 as c86  # noqa: E402
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53  # noqa: E402
import physical_bit_router_patricia_selector_cycle87_2026_07_14 as c87  # noqa: E402
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80  # noqa: E402
import total_status_serial_reject_selector_cycle93_2026_07_15 as c93  # noqa: E402


NOTE = REVIEW / "LIVE_SELECTED_COMPILER_CLOSURE_REVISION_CYCLE91_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle83": REVIEW / "CONSTRUCTIVE_CONSTITUTIONAL_DELTA_AUDIT_CYCLE83_NOTE_2026-07-14.md",
    "cycle84": REVIEW / "SEPARATED_RECURRENT_TUBE_COLLISION_CONTROL_CYCLE84_NOTE_2026-07-14.md",
    "cycle85": REVIEW / "CYCLE80_RECURRENCE_AUDIT_ENDPOINT_TUBE_NUCLEATION_CYCLE85_NOTE_2026-07-14.md",
    "cycle86": REVIEW / "OPEN_DIRECTION_EMPTY_SLOT_CYCLE86_NOTE_2026-07-14.md",
    "cycle87": REVIEW / "PHYSICAL_BIT_ROUTER_PATRICIA_SELECTOR_CYCLE87_NOTE_2026-07-14.md",
    "cycle88": REVIEW / "EXACT_COMPILER_CLOSURE_LEDGER_CYCLE88_NOTE_2026-07-14.md",
    "cycle89": REVIEW / "LIVE_EIGHT_BIT_PHYSICAL_COMPARATOR_CYCLE89_NOTE_2026-07-15.md",
    "cycle90": REVIEW / "LIVE_DIRECTIONAL_PROGRAM_WRITER_CYCLE90_NOTE_2026-07-15.md",
    "cycle92": REVIEW / "LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md",
    "cycle93": REVIEW / "TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md",
}

Coord = tuple[int, int, int]
Signature = c53.Signature
Word = c81.Word
Program = tuple[int, ...]

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


def merge_raw(*tables: dict[Signature, frozenset[str]]) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


# Live selected law and exact current role inventory.
LIVE_TABLE = dict(c85.BRIDGE.union_with_recurrence)
LIVE_SELECTED_RAW = c59.raw_rule_outputs(LIVE_TABLE)
ENDPOINT_ROLES = frozenset(c85.role_inventory(
    c85.c78.CONSTRUCTION.union_table,
    c85.c78.CONSTRUCTION.source,
))
RECURRENT_ROLES = frozenset(c80.CONSTRUCTION.table.values()) | frozenset(
    content for local in c80.CONSTRUCTION.table for _offset, content in local
)
BRIDGE_GUIDE_ROLES = frozenset(
    output for output in c85.BRIDGE.allowed.values() if output.startswith("T_")
)
LIVE_ROLES = ENDPOINT_ROLES | RECURRENT_ROLES | BRIDGE_GUIDE_ROLES
NEW_LIVE_ROLES = LIVE_ROLES - c81.FULL_ROLES


# A deterministic existence witness: preserve every Cycle-81 word and give
# the nineteen new roles the lexicographically first still-free words.
LIVE_ROLE_TO_WORD: dict[str, Word] = dict(c81.ROLE_TO_WORD)
free_words = [
    word for word in c81.ALL_WORDS
    if word not in set(LIVE_ROLE_TO_WORD.values())
]
for role, word in zip(sorted(NEW_LIVE_ROLES), free_words):
    LIVE_ROLE_TO_WORD[role] = word
LIVE_WORD_TO_ROLE = {word: role for role, word in LIVE_ROLE_TO_WORD.items()}
LIVE_RESERVED_WORDS = tuple(
    word for word in c81.ALL_WORDS if word not in LIVE_WORD_TO_ROLE
)
EMPTY_WORD: Word = c86.EMPTY_WORD
STALE_CYCLE82_EMPTY: Word = c82.EMPTY_WORD


def row_program(local: Signature) -> Program:
    contents = dict(local)
    return tuple(
        bit
        for direction in c82.DIRECTION_ORDER
        for bit in (
            LIVE_ROLE_TO_WORD[contents[direction]]
            if direction in contents else EMPTY_WORD
        )
    )


ROW_PROGRAMS = {local: row_program(local) for local in LIVE_TABLE}
PROGRAM_TO_ROW = {program: local for local, program in ROW_PROGRAMS.items()}
PROGRAMS = tuple(PROGRAM_TO_ROW)
PREFIXES = frozenset(
    program[:depth] for program in PROGRAMS for depth in range(49)
)
CHILD_COUNT = {
    prefix: sum(prefix + (bit,) in PREFIXES for bit in (0, 1))
    for prefix in PREFIXES if len(prefix) < 48
}
BRANCH_PREFIXES = frozenset(
    prefix for prefix, count in CHILD_COUNT.items() if count == 2
)
SIGNIFICANT_PREFIXES = frozenset({()}) | BRANCH_PREFIXES | frozenset(PROGRAMS)


def patricia_edges() -> tuple[tuple[Program, Program], ...]:
    edges = []
    for node in SIGNIFICANT_PREFIXES - {()}:
        parent = max(
            (
                prefix for prefix in SIGNIFICANT_PREFIXES
                if len(prefix) < len(node)
                and node[:len(prefix)] == prefix
            ),
            key=len,
        )
        edges.append((parent, node))
    return tuple(edges)


PATRICIA_EDGES = patricia_edges()


# Recompose the constructive mechanisms against the live selected law.  The
# base excludes Cycle 87 so its contextual effect can be measured directly.
BASE_COMPONENTS = {
    "LIVE_SELECTED": LIVE_SELECTED_RAW,
    "C58_BINARY_MACROCODE": c81.c58.RAW_OUTPUTS,
    "C81_COMPARATOR": c81.RAW_OUTPUTS,
    "C82_WRITER": c82.OUTPUT_RAW,
    "C86_OPENNESS": c86.RAW_OUTPUTS,
}
BASE_RAW = merge_raw(*BASE_COMPONENTS.values())
WITH_ROUTER_RAW = merge_raw(BASE_RAW, c87.RAW_OUTPUTS)


# Verified positive fallback repair for the old Cycle-87 contextual parasite.
# The geometry and H0/H1 token/bit/output protocol stay unchanged.  Three live
# bridge-guide roles guard the cage signatures so they cannot masquerade as
# unfilled Cycle-90 comparator/writer sites.
REPAIR_GATE_MARKERS = ("T_G0", c87.H1)  # -z,+z
REPAIR_BRANCH_0_MARKERS = ("T_G1", c87.H0, c87.H1, c87.H1)  # -x,+x,-z,+z
REPAIR_BRANCH_1_MARKERS = ("T_H0", c87.H0, c87.H0, c87.H1)


def repaired_gate_source(bit: str) -> dict[Coord, str]:
    assert bit in (c87.H0, c87.H1)
    return {
        c87.TOKEN: c87.H1,
        c87.BIT: bit,
        (0, 0, -1): REPAIR_GATE_MARKERS[0],
        (0, 0, 1): REPAIR_GATE_MARKERS[1],
        (-1, -1, 0): REPAIR_BRANCH_0_MARKERS[0],
        (1, -1, 0): REPAIR_BRANCH_0_MARKERS[1],
        (0, -1, -1): REPAIR_BRANCH_0_MARKERS[2],
        (0, -1, 1): REPAIR_BRANCH_0_MARKERS[3],
        (-1, 1, 0): REPAIR_BRANCH_1_MARKERS[0],
        (1, 1, 0): REPAIR_BRANCH_1_MARKERS[1],
        (0, 1, -1): REPAIR_BRANCH_1_MARKERS[2],
        (0, 1, 1): REPAIR_BRANCH_1_MARKERS[3],
    }


def build_repaired_gate_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for bit in (c87.H0, c87.H1):
        records = repaired_gate_source(bit)
        table[c53.canonical_signature(c53.local_signature(records, c87.GATE))] = bit
        records[c87.GATE] = bit
        target = c87.BRANCH_0 if bit == c87.H0 else c87.BRANCH_1
        table[c53.canonical_signature(c53.local_signature(records, target))] = c87.H1
    return table


REPAIRED_GATE_TABLE = build_repaired_gate_table()
REPAIRED_GATE_RAW = c59.raw_rule_outputs(REPAIRED_GATE_TABLE)
WITH_REPAIRED_ROUTER_RAW = merge_raw(BASE_RAW, REPAIRED_GATE_RAW)


def enabled_outputs(
    records: dict[Coord, str],
    raw: dict[Signature, frozenset[str]],
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


def assignments(
    records: dict[Coord, str],
    raw: dict[Signature, frozenset[str]],
) -> dict[Coord, str]:
    return {
        target: next(iter(values)) if len(values) == 1 else "CONFLICT"
        for target, values in enabled_outputs(records, raw).items()
    }


def transform(
    records: dict[Coord, str],
    rotation: c53.Matrix,
    shift: Coord,
) -> dict[Coord, str]:
    return {
        c53.add(c53.matvec(rotation, site), shift): content
        for site, content in records.items()
    }


def openness_graph() -> tuple[
    frozenset[frozenset[Coord]],
    int,
    tuple[frozenset[Coord], ...],
    tuple[tuple, ...],
    int,
]:
    initial: frozenset[Coord] = frozenset()
    queue = deque((initial,))
    seen = {initial}
    terminals: list[frozenset[Coord]] = []
    parasites: list[tuple] = []
    edges = 0
    maximum = 0
    while queue:
        state = queue.popleft()
        outputs = enabled_outputs(c86.records_for(state), BASE_RAW)
        maximum = max(maximum, len(outputs))
        if not outputs:
            terminals.append(state)
        for target, values in outputs.items():
            if len(values) != 1 or c86.ALLOWED.get(target) != next(iter(values)):
                parasites.append((state, target, values))
                continue
            future = state | {target}
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return frozenset(seen), edges, tuple(terminals), tuple(parasites), maximum


TARGET_OUTPUT = "R_LB"
TARGET_ROW = next(
    local for local, output in c80.CONSTRUCTION.table.items()
    if output == TARGET_OUTPUT
)
TARGET_PROGRAM = ROW_PROGRAMS[TARGET_ROW]
TARGET_OUTPUT_WORD = LIVE_ROLE_TO_WORD[TARGET_OUTPUT]


def pipeline_audit(raw: dict[Signature, frozenset[str]]) -> dict[str, object]:
    additions = c82.output_additions(TARGET_OUTPUT_WORD, 48)
    states = edges = terminals = 0
    failures = []
    passes = []
    for certificate_count in range(49):
        records = c82.pipeline_records(
            TARGET_PROGRAM,
            TARGET_PROGRAM,
            TARGET_OUTPUT_WORD,
            certificate_count,
        )
        expected = (
            {(certificate_count, 1, 0): c82.H1}
            if certificate_count < 48
            else {additions[0][0]: additions[0][1]}
        )
        actual = assignments(records, raw)
        states += 1
        edges += len(actual)
        item = ("compare", certificate_count, expected, actual)
        (passes if actual == expected else failures).append(item)
    for output_step in range(1, len(additions) + 1):
        records = c82.pipeline_records(
            TARGET_PROGRAM,
            TARGET_PROGRAM,
            TARGET_OUTPUT_WORD,
            48,
            output_step,
        )
        expected = (
            {additions[output_step][0]: additions[output_step][1]}
            if output_step < len(additions) else {}
        )
        actual = assignments(records, raw)
        states += 1
        edges += len(actual)
        terminals += int(not expected)
        item = ("write", output_step, expected, actual)
        (passes if actual == expected else failures).append(item)
    terminal = c82.pipeline_records(
        TARGET_PROGRAM,
        TARGET_PROGRAM,
        TARGET_OUTPUT_WORD,
        48,
        len(additions),
    )
    return {
        "states": states,
        "edges": edges,
        "terminals": terminals,
        "failures": tuple(failures),
        "passes": tuple(passes),
        "decoded": c82.decode_output(terminal, 48),
    }


def all_program_pipeline_audit(
    raw: dict[Signature, frozenset[str]],
) -> dict[str, object]:
    states = edges = terminals = 0
    failures = []
    outputs_seen = set()
    for local, output in LIVE_TABLE.items():
        program = ROW_PROGRAMS[local]
        output_word = LIVE_ROLE_TO_WORD[output]
        additions = c90.output_additions(output_word, 48)
        for certificate_count in range(49):
            records = c90.pipeline_records(
                program, program, output_word, certificate_count
            )
            expected = (
                {(certificate_count, 1, 0): c90.H1}
                if certificate_count < 48
                else {additions[0][0]: additions[0][1]}
            )
            actual = assignments(records, raw)
            states += 1
            edges += len(actual)
            if actual != expected:
                failures.append((output, "compare", certificate_count, expected, actual))
        for output_step in range(1, len(additions) + 1):
            records = c90.pipeline_records(
                program, program, output_word, 48, output_step
            )
            expected = (
                {additions[output_step][0]: additions[output_step][1]}
                if output_step < len(additions) else {}
            )
            actual = assignments(records, raw)
            states += 1
            edges += len(actual)
            terminals += int(not expected)
            if actual != expected:
                failures.append((output, "write", output_step, expected, actual))
            if output_step == len(additions):
                decoded = c90.decode_output(records, 48)
                outputs_seen.add(decoded)
                if decoded != output_word:
                    failures.append((output, "decode", output_word, decoded))
    return {
        "states": states,
        "edges": edges,
        "terminals": terminals,
        "failures": tuple(failures),
        "outputs_seen": frozenset(outputs_seen),
    }


W_BOOT = "W_BOOT"
W_STEP = "W_STEP"
W_MULTI = "W_MULTI"
CLOSED_C85 = "CLOSED_C85_SINGLE_FRONT_NUCLEATION"
CLOSED_CORE = "CLOSED_SUPPLIED_CORE"
CLOSED_ISOLATED = "CLOSED_ISOLATED_SLOT"
STALE_RECOUNT = "STALE_RECOUNT_REPLACED"

RESIDUAL_MAP = {
    "C80:NEXT_FRONT_TO_TUBE_NUCLEATION": (CLOSED_C85,),
    "C80:TUBE_LAYER_TO_LOGICAL_FRONT": (W_STEP,),
    "C80:EIGHT_BIT_RULE_PORT_REALIZATION": (W_BOOT, W_STEP),
    "C80:MULTI_FRONT_CONFLUENCE": (W_MULTI,),
    "C81:SEED_TO_EIGHT_BIT_COMPARATOR_HARNESS": (W_BOOT, W_STEP),
    "C81:DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT": (CLOSED_CORE, W_STEP),
    "C81:RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD": (CLOSED_CORE, W_BOOT, W_STEP),
    "C82:NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM": (W_STEP,),
    "C82:OPEN_DIRECTION_TO_EMPTY_WORD": (CLOSED_ISOLATED, W_STEP),
    "C82:CANDIDATE_FANOUT_TO_198_PROGRAMS": (STALE_RECOUNT, W_STEP),
    "C82:SEED_TO_RULE_PORT_OUTPUT_HARNESS": (W_BOOT, W_STEP),
    "C84:PAIR_NUCLEATION_AND_CONTACT_DOMAIN": (W_MULTI,),
    "C85:SINGLE_FRONT_ENDPOINT_TO_TUBE": (CLOSED_C85,),
    "C86:EMPTY_SLOT_TO_SIX_SLOT_CANDIDATE_GEOMETRY": (W_STEP,),
    "C86:SEED_TO_OPENNESS_ENCODER_HARNESS": (W_BOOT, W_STEP),
    "C87:CANDIDATE_BIT_BUS_TO_ACTIVE_TRIE_NODE": (W_STEP,),
    "C87:PROPER_CUBIC_PATRICIA_EMBEDDING": (W_STEP,),
    "C87:TRIE_LEAF_TO_ASSOCIATED_OUTPUT_PORT": (W_STEP,),
    "C87:SEED_TO_TRIE_SELECTOR_HARNESS": (W_BOOT, W_STEP),
    "C91:ROUTER_ROWS_TO_PIPELINE_ISOLATION": (W_STEP,),
    "C91:VALIDATED_OUTPUT_WORD_TO_LOGICAL_FRONT": (W_STEP,),
    "C93:AUX_GATED_CANDIDATE_TRANSPORT": (W_STEP,),
}

COLLAPSED_WALLS = (W_BOOT, W_STEP, W_MULTI)
INDEPENDENCE = {
    (W_BOOT, W_STEP): (False, False),
    (W_BOOT, W_MULTI): (False, False),
    (W_STEP, W_MULTI): (False, False),
}


def source_and_live_law_contract() -> None:
    section("A - Source, authority, and Cycle-85 correction")
    for name, path in {"cycle91": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    texts = {name: normalized(path) for name, path in SOURCES.items()}
    check("A Cycle85 explicitly closes only single-front endpoint nucleation", has_all(
        texts["cycle85"],
        (
            "next_front_to_tube_nucleation",
            "closed for this exact candidate-law route",
            "nearby multi-tube collision/resource sharing",
        ),
    ))
    check("A Cycle86 keeps packing, routing, selection, and harness open", has_all(
        texts["cycle86"],
        (
            "empty_slot_to_six_slot_candidate_geometry",
            "neighbour_macroblocks_to_ordered_stream",
            "candidate_fanout_to_198_programs",
            "seed_to_openness_encoder_harness",
        ),
    ))
    check("A Cycle87 keeps bus, embedding, leaf binding, and harness open", has_all(
        texts["cycle87"],
        (
            "candidate_bit_bus_to_active_trie_node",
            "proper_cubic_patricia_embedding",
            "trie_leaf_to_associated_output_port",
            "seed_to_trie_selector_harness",
        ),
    ))
    check("A live selected law is exactly 236 canonical / 5240 raw", (
        len(LIVE_TABLE), len(LIVE_SELECTED_RAW)
    ) == (236, 5_240))
    check("A independent live rebuild agrees exactly with Cycles89/90", (
        LIVE_TABLE == c89.LIVE_TABLE
        and LIVE_SELECTED_RAW == c89.LIVE_RAW_OUTPUTS
        and ROW_PROGRAMS == c90.ROW_PROGRAMS
    ))
    check("A live role inventory is 93 endpoint + 51 recurrence + 9 guides", (
        len(ENDPOINT_ROLES), len(RECURRENT_ROLES), len(BRIDGE_GUIDE_ROLES),
        len(LIVE_ROLES),
    ) == (93, 51, 9, 153))
    check("A old 198-row program surfaces are stale bounded routes", (
        len(c81.SELECTED_TABLE), len(c86.ROW_PROGRAMS), len(c87.PROGRAMS)
    ) == (198, 198, 198) and set(c86.ROW_PROGRAMS) != set(LIVE_TABLE))
    check("A Cycle85 bridge has no supplied record and exact first-B handoff", (
        len(c85.BRIDGE.table), len(c85.BRIDGE.allowed)
    ) == (26, 26) and c85.recurrence_phase_parent_contract())


def codebook_and_program_contract() -> None:
    section("B - Corrected 153-role codebook and 236-row program bank")
    expected_new = {
        "G1", "GU", "GY", "J1", "J2", "J3", "M", "MX",
        "T_G0", "T_G1", "T_H0", "T_H1", "T_H2", "T_H3",
        "T_N0", "T_N1", "T_N2", "Y2", "YG0",
    }
    check("B every old Cycle81 role remains live", c81.FULL_ROLES <= LIVE_ROLES)
    check("B live correction adds exactly nineteen named roles", NEW_LIVE_ROLES == expected_new)
    check("B all 134 old words are preserved exactly", all(
        LIVE_ROLE_TO_WORD[role] == word
        for role, word in c81.ROLE_TO_WORD.items()
    ))
    check("B independent corrected codebook equals Cycle89", (
        LIVE_ROLE_TO_WORD == c89.ROLE_TO_WORD
        and LIVE_RESERVED_WORDS == c89.RESERVED_WORDS
    ))
    check("B corrected codebook has 153 unique words and 103 reserved", (
        len(LIVE_ROLE_TO_WORD), len(set(LIVE_ROLE_TO_WORD.values())),
        len(LIVE_RESERVED_WORDS),
    ) == (153, 153, 103))
    check("B corrected route still needs exactly eight bits", 2**7 < len(LIVE_ROLES) <= 2**8)
    check("B deterministic extension begins G1=01010011 and ends YG0=01100101", (
        LIVE_ROLE_TO_WORD["G1"], LIVE_ROLE_TO_WORD["YG0"]
    ) == ((0, 1, 0, 1, 0, 0, 1, 1), (0, 1, 1, 0, 0, 1, 0, 1)))
    check("B Cycle82 first-reserved EMPTY is now the live G1 word", (
        LIVE_WORD_TO_ROLE.get(STALE_CYCLE82_EMPTY) == "G1"
        and STALE_CYCLE82_EMPTY not in LIVE_RESERVED_WORDS
    ))
    check("B Cycle86 all-H1 EMPTY remains genuinely reserved", (
        EMPTY_WORD == (1,) * 8
        and EMPTY_WORD in LIVE_RESERVED_WORDS
        and EMPTY_WORD not in LIVE_WORD_TO_ROLE
    ))

    arities = Counter(map(len, LIVE_TABLE))
    empty_slots = sum(6 - len(local) for local in LIVE_TABLE)
    programs_with_empty = sum(
        EMPTY_WORD in tuple(program[index:index + 8] for index in range(0, 48, 8))
        for program in ROW_PROGRAMS.values()
    )
    distances = [
        sum(left != right for left, right in zip(a, b))
        for index, a in enumerate(ROW_PROGRAMS.values())
        for b in tuple(ROW_PROGRAMS.values())[:index]
    ]
    check("B all 236 current programs are distinct 48-bit words", (
        len(ROW_PROGRAMS), len(set(ROW_PROGRAMS.values()))
    ) == (236, 236) and all(len(program) == 48 for program in ROW_PROGRAMS.values()))
    check("B current arity census is exact", arities == {
        1: 13, 2: 96, 3: 67, 4: 36, 5: 20, 6: 4,
    }, str(arities))
    check("B current bank has 742 EMPTY slots across 232 programs", (
        empty_slots, programs_with_empty
    ) == (742, 232))
    check("B current program minimum Hamming distance is one", min(distances) == 1)


def openness_live_composition_contract() -> None:
    section("C - Cycle86 openness mechanism under the live union")
    check("C live base physical union has 5488 single-valued raw rows", (
        len(BASE_RAW) == 5_488 and all(len(values) == 1 for values in BASE_RAW.values())
    ))
    check("C live selected raw domain is disjoint from every physical mechanism", all(
        set(LIVE_SELECTED_RAW).isdisjoint(table)
        for name, table in BASE_COMPONENTS.items()
        if name != "LIVE_SELECTED"
    ))
    overlap = set(c81.RAW_OUTPUTS) & set(c82.OUTPUT_RAW)
    check("C comparator/writer retain only 24 safe H1 aliases", (
        len(overlap) == 24
        and all(c81.RAW_OUTPUTS[local] == c82.OUTPUT_RAW[local] == frozenset((c82.H1,)) for local in overlap)
    ))

    states, edges, terminals, parasites, maximum = openness_graph()
    check("C live openness graph remains 46 states / 73 edges", (
        len(states), edges
    ) == (46, 73))
    check("C live openness graph has one complete terminal and no parasite", (
        len(terminals) == 1
        and terminals[0] == frozenset(c86.ALLOWED)
        and not parasites
        and maximum == 2
    ), str(parasites[:1]))
    terminal_records = c86.records_for(terminals[0])
    check("C terminal candidate is the live reserved all-H1 word", tuple(
        1 if terminal_records[site] == c86.H1 else 0 for site in c86.CANDIDATE
    ) == EMPTY_WORD)

    extra_failures = []
    shift = (47, -29, 13)
    for extra in tuple(sorted(LIVE_ROLES)) + ("FOREIGN_CONTROL",):
        records = c86.source(extra)
        if enabled_outputs(records, BASE_RAW):
            extra_failures.append(("base", extra, enabled_outputs(records, BASE_RAW)))
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            transformed = transform(records, rotation, shift)
            if enabled_outputs(transformed, BASE_RAW):
                extra_failures.append((rotation_index, extra, enabled_outputs(transformed, BASE_RAW)))
    check("C all 3850 live-role/foreign extra-neighbour controls are quiet", (
        (len(LIVE_ROLES) + 1) * 25 == 3_850 and not extra_failures
    ), str(extra_failures[:1]))

    covariance_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state in states:
            records = c86.records_for(state)
            expected = assignments(records, BASE_RAW)
            transformed = transform(records, rotation, shift)
            transformed_expected = transform(expected, rotation, shift)
            actual = assignments(transformed, BASE_RAW)
            if actual != transformed_expected:
                covariance_failures.append((rotation_index, state, transformed_expected, actual))
    check("C all 1104 live-union rotated openness states are exact", (
        len(states) * 24 == 1_104 and not covariance_failures
    ), str(covariance_failures[:1]))


def trie_router_and_target_probe_contract() -> None:
    section("D - Current trie, isolated router, and actual recurrent-row audit")
    check("D current prefix trie is 8239 nodes / 8238 edges", (
        len(PREFIXES), sum(CHILD_COUNT.values())
    ) == (8_239, 8_238))
    check("D current trie has 235 branches and 7768 unary nodes", Counter(
        CHILD_COUNT.values()
    ) == {1: 7_768, 2: 235})
    width = Counter(map(len, PREFIXES))
    check("D current maximum trie width is 236 at depths 46-48", (
        max(width.values()) == 236
        and {depth for depth, count in width.items() if count == 236} == {46, 47, 48}
    ))
    edge_lengths = tuple(
        len(child) - len(parent) for parent, child in PATRICIA_EDGES
    )
    check("D corrected Patricia census is 471 nodes / 470 edges", (
        len(SIGNIFICANT_PREFIXES), len(PATRICIA_EDGES)
    ) == (471, 470))
    check("D corrected Patricia labels total 8238 bits with longest 43", (
        sum(edge_lengths), max(edge_lengths)
    ) == (8_238, 43))

    check("D adding Cycle87 leaves a 5515-row single-valued raw union", (
        len(WITH_ROUTER_RAW) == 5_515
        and all(len(values) == 1 for values in WITH_ROUTER_RAW.values())
    ))
    router_failures = []
    shift = (19, -13, 7)
    router_cases = 0
    for bit in (c87.H0, c87.H1):
        source = c87.source(bit)
        target = c87.BRANCH_0 if bit == c87.H0 else c87.BRANCH_1
        stages = (
            (source, {c87.GATE: bit}),
            ({**source, c87.GATE: bit}, {target: c87.H1}),
            ({**source, c87.GATE: bit, target: c87.H1}, {}),
        )
        for stage_index, (records, expected) in enumerate(stages):
            router_cases += 1
            if assignments(records, WITH_ROUTER_RAW) != expected:
                router_failures.append(("base", bit, stage_index, expected, assignments(records, WITH_ROUTER_RAW)))
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                router_cases += 1
                transformed = transform(records, rotation, shift)
                transformed_expected = transform(expected, rotation, shift)
                actual = assignments(transformed, WITH_ROUTER_RAW)
                if actual != transformed_expected:
                    router_failures.append((rotation_index, bit, stage_index, transformed_expected, actual))
    check("D isolated router remains exact in all 150 live-union controls", (
        router_cases == 150 and not router_failures
    ), str(router_failures[:1]))

    missing = set(c82.DIRECTION_ORDER) - {direction for direction, _content in TARGET_ROW}
    expected_program = (
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 1, 0, 1, 0, 1,
        1, 0, 0, 1, 1, 0, 0, 0,
        1, 0, 0, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
    )
    check("D target is the real arity-five R_LB launcher with open +x", (
        len(TARGET_ROW) == 5
        and missing == {(1, 0, 0)}
        and c80.role("B", *c80.LAUNCH["B"]) == TARGET_OUTPUT
    ))
    check("D target current program and output word are pinned", (
        TARGET_PROGRAM == expected_program
        and TARGET_OUTPUT_WORD == (1, 0, 1, 1, 0, 0, 0, 1)
    ))

    base = pipeline_audit(BASE_RAW)
    check("D supplied R_LB baseline is exact without Cycle87 rows", (
        base["states"], base["edges"], base["terminals"],
        len(base["failures"]), base["decoded"],
    ) == (66, 65, 1, 0, TARGET_OUTPUT_WORD), str(base["failures"][:1]))
    check("D supplied R_LB baseline still has a 262-record source", len(
        c82.pipeline_records(
            TARGET_PROGRAM, TARGET_PROGRAM, TARGET_OUTPUT_WORD, 0
        )
    ) == 262)

    routed = pipeline_audit(WITH_ROUTER_RAW)
    check("D naive Cycle87 union fails 63 of 66 R_LB pipeline states", (
        routed["states"], len(routed["failures"]), len(routed["passes"])
    ) == (66, 63, 3))
    check("D naive Cycle87 union exposes 1217 aggregate append frontiers", routed["edges"] == 1_217)

    initial = c82.pipeline_records(
        TARGET_PROGRAM, TARGET_PROGRAM, TARGET_OUTPUT_WORD, 0
    )
    base_initial = assignments(initial, BASE_RAW)
    routed_initial = assignments(initial, WITH_ROUTER_RAW)
    extra = {
        site: content for site, content in routed_initial.items()
        if base_initial.get(site) != content
    }
    exclusive = []
    for site in extra:
        local = c53.local_signature(initial, site)
        owners = {
            name for name, table in BASE_COMPONENTS.items() if local in table
        }
        if local in c87.RAW_OUTPUTS:
            owners.add("C87_ROUTER")
        exclusive.append(owners == {"C87_ROUTER"})
    check("D initial target harness gets 32 Cycle87-only parasite writes", (
        len(routed_initial), len(extra), Counter(extra.values()), all(exclusive)
    ) == (33, 32, Counter({c87.H0: 24, c87.H1: 8}), True))

    check("D guarded fallback repair has four canonical / 84 raw rows", (
        len(REPAIRED_GATE_TABLE), len(REPAIRED_GATE_RAW)
    ) == (4, 84))
    check("D independent guarded repair agrees exactly with Cycle92", (
        REPAIRED_GATE_TABLE == c92.GATE_TABLE
        and REPAIRED_GATE_RAW == c92.GATE_RAW
        and WITH_REPAIRED_ROUTER_RAW == c92.COMBINED_RAW
    ))
    check("D guarded repair is disjoint from the live base", set(
        REPAIRED_GATE_RAW
    ).isdisjoint(BASE_RAW))
    check("D guarded repair gives 5572 single-valued raw rows", (
        len(WITH_REPAIRED_ROUTER_RAW) == 5_572
        and all(len(values) == 1 for values in WITH_REPAIRED_ROUTER_RAW.values())
    ))

    repaired_router_failures = []
    shift = (23, -17, 11)
    repaired_router_cases = 0
    for bit in (c87.H0, c87.H1):
        source = repaired_gate_source(bit)
        target = c87.BRANCH_0 if bit == c87.H0 else c87.BRANCH_1
        stages = (
            (source, {c87.GATE: bit}),
            ({**source, c87.GATE: bit}, {target: c87.H1}),
            ({**source, c87.GATE: bit, target: c87.H1}, {}),
        )
        for stage_index, (records, expected) in enumerate(stages):
            repaired_router_cases += 1
            actual = assignments(records, WITH_REPAIRED_ROUTER_RAW)
            if actual != expected:
                repaired_router_failures.append(("base", bit, stage_index, expected, actual))
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                repaired_router_cases += 1
                transformed = transform(records, rotation, shift)
                transformed_expected = transform(expected, rotation, shift)
                actual = assignments(transformed, WITH_REPAIRED_ROUTER_RAW)
                if actual != transformed_expected:
                    repaired_router_failures.append((rotation_index, bit, stage_index, transformed_expected, actual))
    check("D guarded router is exact in all 150 isolated/rotated controls", (
        repaired_router_cases == 150 and not repaired_router_failures
    ), str(repaired_router_failures[:1]))

    repaired_target = pipeline_audit(WITH_REPAIRED_ROUTER_RAW)
    check("D guarded repair preserves the exact 66-state R_LB pipeline", (
        repaired_target["states"], repaired_target["edges"],
        len(repaired_target["failures"]), repaired_target["decoded"],
    ) == (66, 65, 0, TARGET_OUTPUT_WORD), str(repaired_target["failures"][:1]))

    all_repaired = all_program_pipeline_audit(WITH_REPAIRED_ROUTER_RAW)
    check("D guarded repair preserves all 236 supplied program pipelines", (
        all_repaired["states"], all_repaired["edges"],
        all_repaired["terminals"], len(all_repaired["failures"]),
    ) == (15_576, 15_340, 236, 0), str(all_repaired["failures"][:1]))
    check("D all repaired terminals decode to their live output words", all_repaired[
        "outputs_seen"
    ] == frozenset(LIVE_ROLE_TO_WORD[output] for output in LIVE_TABLE.values()))

    check("D Cycle93 status/final decision tables have exact live counts", (
        len(c93.STATUS_TABLE), len(c93.STATUS_RAW),
        len(c93.FINAL_TABLE), len(c93.FINAL_RAW), len(c93.COMBINED_RAW),
    ) == (6, 144, 4, 96, 5_680))
    check("D Cycle93 total-selector union is single-valued", all(
        len(values) == 1 for values in c93.COMBINED_RAW.values()
    ))
    target_additions = c90.output_additions(TARGET_OUTPUT_WORD, 48)
    equal_terminal = c93.records(
        TARGET_PROGRAM, TARGET_PROGRAM, TARGET_OUTPUT_WORD, 48
    )
    mismatch_program = tuple(
        1 - bit if index == 17 else bit
        for index, bit in enumerate(TARGET_PROGRAM)
    )
    mismatch_terminal = c93.records(
        mismatch_program, TARGET_PROGRAM, TARGET_OUTPUT_WORD, 48
    )
    rejected_terminal = c93.records(
        mismatch_program, TARGET_PROGRAM, TARGET_OUTPUT_WORD, 48, reject=True
    )
    check("D Cycle93 R_LB equal status starts the associated writer", c93.assignments(
        equal_terminal
    ) == {target_additions[0][0]: target_additions[0][1]})
    check("D Cycle93 R_LB mismatch writes AUX once then stays quiet", (
        c93.assignments(mismatch_terminal) == {c93.FINAL: c93.REJECT}
        and c93.assignments(rejected_terminal) == {}
    ))


def residual_constitutional_and_note_contract() -> None:
    section("E - Revised walls, probe contract, N1-N8, and constitution")
    check("E Cycle85 single-front nucleation is removed from W_BOOT", (
        RESIDUAL_MAP["C80:NEXT_FRONT_TO_TUBE_NUCLEATION"] == (CLOSED_C85,)
        and RESIDUAL_MAP["C85:SINGLE_FRONT_ENDPOINT_TO_TUBE"] == (CLOSED_C85,)
    ))
    check("E W_BOOT/W_STEP/W_MULTI remain the selected project ledger", COLLAPSED_WALLS == (
        W_BOOT, W_STEP, W_MULTI
    ))
    check("E Cycle86 isolated closure and packing residual are separated", (
        CLOSED_ISOLATED in RESIDUAL_MAP["C82:OPEN_DIRECTION_TO_EMPTY_WORD"]
        and RESIDUAL_MAP["C86:EMPTY_SLOT_TO_SIX_SLOT_CANDIDATE_GEOMETRY"] == (W_STEP,)
    ))
    check("E stale 198-way name is recounted rather than inherited", RESIDUAL_MAP[
        "C82:CANDIDATE_FANOUT_TO_198_PROGRAMS"
    ] == (STALE_RECOUNT, W_STEP))
    check("E new router/pipeline isolation defect is a W_STEP clause", RESIDUAL_MAP[
        "C91:ROUTER_ROWS_TO_PIPELINE_ISOLATION"
    ] == (W_STEP,))
    check("E Cycle93 AUX transport is a narrower W_STEP selector clause", RESIDUAL_MAP[
        "C93:AUX_GATED_CANDIDATE_TRANSPORT"
    ] == (W_STEP,))
    check("E multi-tube reachability/contact remains W_MULTI", RESIDUAL_MAP[
        "C84:PAIR_NUCLEATION_AND_CONTACT_DOMAIN"
    ] == (W_MULTI,))
    check("E all wall pairs retain bidirectional non-implication entries", set(
        INDEPENDENCE
    ) == {
        (W_BOOT, W_STEP), (W_BOOT, W_MULTI), (W_STEP, W_MULTI)
    } and all(value == (False, False) for value in INDEPENDENCE.values()))
    check("E Cycle83 still has exact law identity as sole candidate", {
        atom for atom, status in c83.ATOM_LEDGER.items()
        if status == c83.CONSTITUTIONAL_ID
    } == {"exact_complete_law_identity"})

    note = normalized(NOTE)
    check("E note carries authority none", "authority: none" in note)
    check("E note states the live law and stale inventories", has_all(note, (
        "236 canonical / 5,240 raw / 153 roles",
        "198-row and 134-role inventories are stale",
        "01010011 is now g1",
        "11111111 remains reserved",
    )))
    check("E note distinguishes isolated router success from composition failure", has_all(note, (
        "isolated cycle-87 router remains exact",
        "32 immediate parasite writes",
        "63 of the 66 pipeline states",
        "not a selector no-go",
    )))
    check("E note records the verified guarded repair without seed-growth overclaim", has_all(note, (
        "t_g0/t_g1/t_h0 guarded fallback",
        "84 raw rows",
        "5,572",
        "all 236 supplied program pipelines",
        "not seed-grown",
    )))
    check("E note credits Cycle93 decision but keeps candidate transport open", has_all(note, (
        "cycle 93 total-status serial-reject primitive",
        "55,460 ordered unequal pairs",
        "aux_gated_candidate_transport",
        "not a complete physical selector",
    )))
    check("E note defines the minimum actual R_LB acceptance contract", has_all(note, (
        "p_rlb_5",
        "five validated occupied-neighbour words",
        "genuinely open +x port",
        "consumed by the next c-phase seed step",
        "a supplied 48-bit stream does not pass",
    )))
    check("E note pins narrowed W_BOOT/W_STEP/W_MULTI boundaries", has_all(note, (
        "w_boot — first physical binary compiler harness",
        "w_step — one live 236-row physical macrostep",
        "w_multi — full reachable multi-apparatus domain",
    )))
    check("E note includes every N1-N8 section", all(
        f"n{index} —" in note for index in range(1, 9)
    ))
    check("E note limits every minimum/no-go claim", has_all(note, (
        "selected-route project ledger, not a global lower bound",
        "not a universal compiler or selector impossibility",
        "partial-closure-with-live-repair-routes",
    )))
    check("E note preserves the constitutional conclusion", has_all(note, (
        "no foundation or axiom edit follows",
        "stable exact identity of a complete l",
        "no witness, read-lock, clock-lock, counting, or storage-budget sentence follows",
    )))

    body = note.split("## 8. no-go discipline gate", 1)[0]
    hidden_phrases = (
        "we assume",
        "as is standard",
        "the framework provides",
        "obviously",
        "naturally follows",
        "standard qft",
    )
    check("E scientific body contains no premise-hiding phrase", not any(
        phrase in body for phrase in hidden_phrases
    ), str([phrase for phrase in hidden_phrases if phrase in body]))
    check("E note makes no universal three-wall or router no-go claim", all(
        phrase not in note for phrase in (
            "three walls are universally necessary",
            "no physical selector can compose",
            "a new substrate axiom is required",
            "the router collision is impossible to repair",
        )
    ))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_live_law_contract()
    codebook_and_program_contract()
    openness_live_composition_contract()
    trie_router_and_target_probe_contract()
    residual_constitutional_and_note_contract()
    print("\nLIVE_SELECTED=236 CANONICAL / 5240 RAW / 153 ROLES")
    print("PROGRAMS=236 EMPTY_SLOTS=742 PATRICIA_NODES=471 PATRICIA_EDGES=470")
    print("BASE_RAW=5488 OLD_ROUTER_RAW=5515 REPAIRED_ROUTER_RAW=5572")
    print("OLD_ROUTER_PIPELINE_FAILURES=63/66 REPAIRED_PIPELINES=236/236")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
