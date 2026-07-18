#!/usr/bin/env python3
"""Cycle 133: executable minimum-axiom and compiler campaign synthesis.

This runner consumes the exact campaign-local artifacts through Cycle 132,
rechecks the unchanged foundation and registry, and pins the remaining word
and socket interfaces.  It does not select a law or edit any source.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import c129_two_parent_corner_relocated_cage_seed_cycle132_2026_07_15 as c132
import translated_second_rail_frame_join_interface_cycle131_2026_07_15 as c131
import r_b01_cycle129_bridge_orientation13_interface_cycle130_2026_07_15 as c130
import r_b01_orientation13_neighbor_guard_family_cycle128_2026_07_15 as c128
import fixed_two_value_serial_read_path_cycle118_2026_07_15 as c118
import candidate_selected_common_reference_port_cycle120_2026_07_15 as c120
import r_b01_minimal_phase_patch_probe_cycle125_2026_07_15 as c125


c129 = c132.c129
c127 = c128.c127

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "POST_CYCLE132_MINIMUM_AXIOM_AND_COMPILER_CAMPAIGN_CYCLE133_NOTE_2026-07-15.md"
C126_NOTE = REVIEW / "POST_CYCLE124_MINIMUM_AXIOM_AND_COMPILER_DELTA_CYCLE126_NOTE_2026-07-15.md"

FOUNDATIONS = {
    ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md": "814691ce9cc87652feaee7883237ba494314cbbfafccdb0f169d1a5fc2a9a1be",
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}

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


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">", "“", "”"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def foundation_contract() -> None:
    section("A - Unchanged foundation and exact primitive registry")
    for path, expected in FOUNDATIONS.items():
        actual = digest(path) if path.is_file() else "missing"
        check(f"A foundation hash {path.name}", actual == expected, actual)
    registry = json.loads(
        (ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json").read_text(
            encoding="utf-8"
        )
    )
    check(
        "A registry has exactly four canonical nodes",
        set(registry["canonical_ids"])
        == {
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        },
        str(registry["canonical_ids"]),
    )
    axioms = normalized(ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md")
    check(
        "A Record still says form, one lock, permanence, and readout",
        all(
            phrase in axioms
            for phrase in (
                "records form.",
                "a record locks exactly one admissible local possibility",
                "records are permanent",
                "only records are readable",
            )
        ),
    )
    check(
        "A Admissibility still supplies one fixed covariant local-rule slot",
        "there is one fixed nearest-neighbor admissibility rule" in axioms
        and "available possibilities are determined by, and vary with, the nearest-neighbor conditions"
        in axioms,
    )


def predecessor_contract() -> None:
    section("B - Read chronology, common selection port, and compiler chain")
    c124 = c129.c124
    c121 = c124.c121
    check(
        "B Cycle118 keeps both source records before downstream status",
        not c118.READER_GRAPH.violations
        and all(
            source < port
            for earliest in c118.READER_GRAPH.earliest_sizes
            for source, port in ((earliest[0], earliest[1]), (earliest[2], earliest[3]))
        ),
        str(c118.READER_GRAPH.earliest_sizes),
    )
    check(
        "B Cycle120 reaches two exact selector/value common-port terminals",
        c120.POSITIVE.states == 133_270
        and c120.POSITIVE.edges == 790_154
        and len(c120.POSITIVE.terminals) == 2
        and not c120.POSITIVE.bad
        and not c120.POSITIVE.unexpected,
    )
    check(
        "B Cycle121 writes R_B00=10010000 in one 99-write terminal",
        c121.DATA_WORD == (1, 0, 0, 1, 0, 0, 0, 0)
        and c121.POSITIVE.states == 247_144
        and c121.POSITIVE.edges == 1_586_166
        and c121.POSITIVE.terminal_sizes == (99,)
        and not c121.POSITIVE.bad,
    )
    check(
        "B Cycle124 reaches one complete 101-write R_A01/R_B01 terminal",
        c124.POSITIVE.states == 248_680
        and c124.POSITIVE.edges == 1_594_358
        and c124.POSITIVE.terminal_sizes == (101,)
        and not c124.POSITIVE.bad
        and not c124.POSITIVE.unexpected_condition_targets,
    )


def negative_frontier_contract() -> None:
    section("C - Exact bounded negatives and their live boundaries")
    check(
        "C Cycle125 direct patch stops at state zero with 130 unexpected targets",
        len(c125.CANDIDATE_TABLE) == 12
        and len(c125.CANDIDATE_RAW) == 159
        and len(c125.POSITIVE.unexpected_condition_targets) == 130
        and c125.POSITIVE.states == 1
        and c125.POSITIVE.edges == 0
        and c125.POSITIVE.terminals == 0,
    )
    check(
        "C Cycle127 exhausts all 153 literal-chain labels",
        len(c127.ROLES) == 153
        and len(c127.CONFLICT_ROLES) == 18
        and len(c127.EXISTING_H1_ROLES) == 1
        and len(c127.NOVEL_H1_ROLES) == 134
        and len(c127.G0_SOURCE_IMAGES) == 5
        and len(c127.REPRESENTATIVE_UNARY_SHELL) == 19,
    )
    check(
        "C Cycle128 pins three incompatible full-history unary-L6 outputs",
        c128.P_HISTORY_TARGETS and len(c128.P_HISTORY_TARGETS) == 36
        and c128.P_PRIOR_OUTPUT_COLLISIONS
        == (
            ((4, -1, 0), "OPEN_B"),
            ((4, 1, -2), "R_B00"),
            ((5, -1, -1), c128.H0),
        )
        and c128.P_SOURCE_STATE_COLLISIONS
        == c128.P_PRIOR_OUTPUT_COLLISIONS
        and len(c128.ALL_ROLES) == 153,
        str(c128.P_PRIOR_OUTPUT_COLLISIONS),
    )
    check(
        "C Cycle128 terminal indulgence leaves 304 survivors but minimum nine unexpected",
        len(c128.STATIC_SURVIVORS) == 304
        and c128.MIN_STATIC_UNEXPECTED == 9
        and c128.REPRESENTATIVE_GRAPH.states == 701
        and c128.REPRESENTATIVE_GRAPH.edges == 1_330
        and c128.REPRESENTATIVE_GRAPH.terminals == 0,
    )
    check(
        "C Cycle130 exhausts 408 direct bridge placements at the fixed writer",
        c130.PLACEMENT_CENSUS == 408
        and not c130.G0_HITS
        and len(c130.G1_HITS) == 3
        and set(c130.HIT_PREFIX_FAILURES) == {3, 7, 11}
        and c130.HIT_PREFIX_FAILURES[3][:4]
        == ("local-mismatch", 1, "W3", ((6, 3, -3),))
        and c130.HIT_PREFIX_FAILURES[7][:4]
        == ("local-mismatch", 0, "OZ", ((6, 4, -3),))
        and c130.HIT_PREFIX_FAILURES[11][:4]
        == ("occupied", 0, "OZ", ((5, 4, -2),)),
    )
    check(
        "C Cycle131 finds two substitutions and zero open literal socket",
        len(c131.LAUNCH_ROLES - c131.INTERFACE_ROLES) == 2
        and not c131.OPEN_COMMON
        and not c131.ALL_LAUNCH_MATCHES
        and c131.TERMINAL[c131.SECOND_SLOT] == "A_0_2"
        and c131.SECOND_LOCAL not in c129.BRIDGE_RAW,
    )


def positive_frame_and_cage_contract() -> None:
    section("D - Guarded frame join and relocated causal cage")
    check(
        "D Cycle129 table is 16/366 with a 9,110-row single-valued union",
        len(c129.BRIDGE_TABLE) == 16
        and len(c129.BRIDGE_RAW) == 366
        and len(c129.FULL_RAW) == 9_110
        and all(len(values) == 1 for values in c129.FULL_RAW.values()),
    )
    check(
        "D Cycle129 factor is 618/1,653 with one 29-write terminal",
        c129.FACTOR.states == 618
        and c129.FACTOR.edges == 1_653
        and c129.FACTOR.terminal_sizes == (29,)
        and not c129.FACTOR.bad,
    )
    check(
        "D Cycle129 full history is 6,541,456/51,107,588 and complete",
        c129.POSITIVE.states == 6_541_456
        and c129.POSITIVE.edges == 51_107_588
        and c129.POSITIVE.terminal_sizes == (130,)
        and len(c129.POSITIVE.reached) == 130
        and not c129.POSITIVE.bad
        and not c129.POSITIVE.unexpected_condition_targets,
    )
    check(
        "D Cycle129 final contact has literal head and frame parents",
        c129.GROUP_LOCALS[15]
        == (((0, 0, 1), c129.FRAME_PARENT_OUTPUT), ((1, 0, 0), c129.HEAD_PHASE_OUTPUT)),
        str(c129.GROUP_LOCALS[15]),
    )
    check(
        "D Cycle129 unguarded draft exposes one factor and two transient aliases",
        c129.UNGUARDED_FACTOR_COMPILED.unexpected_targets
        == frozenset(((3, 2, 5),))
        and c129.UNGUARDED_COMPILED.unexpected_targets
        == frozenset(((3, 2, 5), (3, 3, 4), (5, 2, 3)))
        and c129.UNGUARDED_GRAPH.states == 1
        and c129.UNGUARDED_GRAPH.edges == 0
        and c129.UNGUARDED_GRAPH.terminals == 0,
    )
    check(
        "D Cycle132 cage is four canonical / 96 raw rows",
        len(c132.CAGE_TABLE) == 4
        and len(c132.CAGE_RAW) == 96
        and len(c132.FULL_RAW) == 9_206
        and all(len(values) == 1 for values in c132.FULL_RAW.values()),
    )
    check(
        "D Cycle132 factor is six states / six edges / one four-write terminal",
        c132.FACTOR.states == 6
        and c132.FACTOR.edges == 6
        and c132.FACTOR.terminal_sizes == (4,)
        and not c132.FACTOR.bad,
    )
    check(
        "D Cycle132 full history is 6,870,416/53,451,460 and complete",
        c132.POSITIVE.states == 6_870_416
        and c132.POSITIVE.edges == 53_451_460
        and c132.POSITIVE.terminal_states == (c132.ALL_GROWN_MASK,)
        and c132.POSITIVE.terminal_sizes == (134,)
        and len(c132.POSITIVE.reached) == 134
        and not c132.POSITIVE.bad
        and not c132.POSITIVE.unexpected_condition_targets,
    )
    check(
        "D Cycle132 rejects the tempting R_C12 strand at two exact aliases",
        c132.REJECTED_COMPILED.unexpected_targets
        == frozenset(((5, 1, -4), (6, 1, -3))),
        str(tuple(sorted(c132.REJECTED_COMPILED.unexpected_targets))),
    )


def scope_contract() -> None:
    section("E - Minimum-axiom verdict and exact next campaign")
    note = normalized(NOTE) if NOTE.is_file() else ""
    c126_note = normalized(C126_NOTE)
    check("E Cycle133 note exists", NOTE.is_file())
    check(
        "E minimum supported axiom update is explicitly empty",
        "the minimum supported axiom update is the empty update" in note,
    )
    check(
        "E bare-metal chronology keeps append actuality honest",
        "if an append occurs" in note
        and "they do not choose which allowed append actually occurs" in note,
    )
    check(
        "E read-lock, clock-lock, witness, and storage promotions are denied",
        all(
            phrase in note
            for phrase in (
                "read-lock and clock-lock wording would contradict",
                "not evidence for inserting two witnesses into record",
                "not an axiom-grade physical statement",
            )
        ),
    )
    check(
        "E all remaining TOE lanes are separated from axiom need",
        all(
            label in note
            for label in (
                "strict local compiler",
                "exact law",
                "formation / actuality",
                "probability",
                "time",
                "quantum dynamics",
                "matter",
                "gravity / resource",
            )
        ),
    )
    check(
        "E next campaign is causally forced socket and relocated word induction",
        "causally_forced_socket_and_relocated_word_induction" in note,
    )
    check(
        "E note carries substantive N1-N8 and broad-negative firewall",
        all(f"n{index}" in note for index in range(1, 9))
        and "fail for a universal compiler no-go" in note
        and "does not mean the axioms derive actuality" in note,
    )
    check(
        "E predecessor synthesis and current note both keep zero generic delta scoped",
        "the live constitutional delta is zero" in c126_note
        and "pass for the bounded cycle-124" in c126_note
        and "fail for a universal writer no-go" in c126_note
        and "no generic sentence was forced here" in note,
    )
    check(
        "E Cycle133 writes only runner and review note",
        Path(__file__).parent == ROOT / "scripts" and NOTE.parent == REVIEW,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    foundation_contract()
    predecessor_contract()
    negative_frontier_contract()
    positive_frame_and_cage_contract()
    scope_contract()
    print(f"\nPASS={PASS} FAIL={FAIL}")
    print("MINIMUM_AXIOM_UPDATE=EMPTY" if FAIL == 0 else "MINIMUM_AXIOM_UPDATE=UNRESOLVED")
    print("COMPILER_STATUS=INCOMPLETE_EXACT_FRONTIER" if FAIL == 0 else "COMPILER_STATUS=FAIL")
    print("NEXT=CAUSALLY_FORCED_SOCKET_AND_RELOCATED_WORD_INDUCTION")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
