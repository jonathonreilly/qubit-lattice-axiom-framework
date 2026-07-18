#!/usr/bin/env python3
"""Cycle 126: executable post-Cycle-124 constitutional/compiler synthesis.

This runner re-reads the unchanged foundation, consumes the cited bounded read,
common-port, writer, and successor results literally, and pins the smallest
remaining recurrence collision.  It does not select a law or edit any source.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

import candidate_selected_common_reference_port_cycle120_2026_07_15 as c120
import directed_payload_reusable_cone_cycle113_2026_07_15 as c113
import fixed_two_value_serial_read_path_cycle118_2026_07_15 as c118
import r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15 as c124
import r_b01_minimal_phase_patch_probe_cycle125_2026_07_15 as c125


AUDIT_TIMEOUT_SEC = 900
ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "POST_CYCLE124_MINIMUM_AXIOM_AND_COMPILER_DELTA_CYCLE126_NOTE_2026-07-15.md"

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
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def foundation_contract() -> None:
    section("A - Unchanged foundation and primitive registry")
    for path, expected in FOUNDATIONS.items():
        actual = digest(path) if path.is_file() else "missing"
        check(f"A foundation hash {path.name}", actual == expected, actual)
    registry = json.loads(
        (ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json").read_text(
            encoding="utf-8"
        )
    )
    check(
        "A registry contains exactly the four canonical nodes",
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
        "A Record still states formation, one lock, permanence, and readout",
        all(
            phrase in axioms
            for phrase in (
                "records form.",
                "a record locks exactly one admissible local possibility",
                "records are permanent",
                "only records are readable",
                "a readout value is determined by record content alone",
            )
        ),
    )
    check(
        "A Admissibility still carries one fixed covariant nearest-neighbour rule",
        "there is one fixed nearest-neighbor admissibility rule" in axioms
        and "available possibilities are determined by, and vary with, the nearest-neighbor conditions" in axioms,
    )


def read_and_selection_contract() -> None:
    section("B - Formed source, downstream read, and literal common port")
    check(
        "B Cycle118 is a zero-new-row two-position reader",
        len(c118.READER_TABLE) == 2
        and len(c118.READER_RAW) == 48
        and c118.READER_GRAPH.states == 73_656
        and c118.READER_GRAPH.edges == 430_754,
    )
    check(
        "B no read-status carrier precedes its source record",
        not c118.READER_GRAPH.violations
        and all(
            source < port
            for earliest in c118.READER_GRAPH.earliest_sizes
            for source, port in ((earliest[0], earliest[1]), (earliest[2], earliest[3]))
        ),
        str(c118.READER_GRAPH.earliest_sizes),
    )
    check(
        "B Cycle120 table is 14 canonical / 318 raw and single-valued",
        len(c120.MUX_TABLE) == 14
        and len(c120.MUX_RAW) == 318
        and len(c120.FULL_RAW) == 8_630
        and all(len(values) == 1 for values in c120.FULL_RAW.values()),
    )
    check(
        "B Cycle120 exhausts to two exact 92-write selector/value terminals",
        c120.POSITIVE.states == 133_270
        and c120.POSITIVE.edges == 790_154
        and len(c120.POSITIVE.terminals) == 2
        and c120.POSITIVE.terminal_sizes == (92,)
        and not c120.POSITIVE.bad
        and not c120.POSITIVE.unexpected
        and not c120.POSITIVE.violations,
    )
    classes = Counter(c120.terminal_class(state) for state in c120.POSITIVE.terminals)
    check(
        "B one literal port carries exactly selector-zero/H0 or selector-one/H1",
        classes
        == Counter(
            {
                (c120.SELECTOR_ZERO, c120.H0): 1,
                (c120.SELECTOR_ONE, c120.H1): 1,
            }
        ),
        str(classes),
    )


def campaign_inventory_contract() -> None:
    section("C - Literal censuses for every campaign-table row through Cycle119")
    c112 = c113.c112
    c114 = c113.c114
    c115 = c113.c115
    c117 = c120.c117
    c119 = c124.c121.c119
    check(
        "C Cycle112 is 73,656 states / 430,754 edges / one 69-write terminal",
        c112.POSITIVE.states == 73_656
        and c112.POSITIVE.edges == 430_754
        and c112.POSITIVE.terminal_sizes == (69,)
        and not c112.POSITIVE.bad
        and not c112.POSITIVE.unexpected_condition_targets,
    )
    check(
        "C Cycle113 is 77,336-state positive plus 22-state typed alternate",
        c113.POSITIVE.states == 77_336
        and c113.POSITIVE.edges == 452_018
        and c113.POSITIVE.terminals == 1
        and c113.POSITIVE.terminal_sizes == (69,)
        and c113.ALTERNATE.states == 22
        and c113.ALTERNATE.edges == 31
        and c113.ALTERNATE.terminals == 1
        and c113.ALTERNATE.terminal_sizes == (11,)
        and not c113.POSITIVE.bad
        and not c113.ALTERNATE.bad,
    )
    check(
        "C Cycle114 is 17,880 states / 88,642 edges / two terminals",
        c114.POSITIVE.states == 17_880
        and c114.POSITIVE.edges == 88_642
        and len(c114.POSITIVE.terminals) == 2
        and c114.POSITIVE.terminal_sizes == (46, 48)
        and not c114.POSITIVE.bad,
    )
    check(
        "C Cycle115 is 74,264 states / 433,682 edges / one 71-write terminal",
        c115.POSITIVE.states == 74_264
        and c115.POSITIVE.edges == 433_682
        and c115.POSITIVE.terminal_sizes == (71,)
        and not c115.POSITIVE.bad
        and not c115.POSITIVE.unexpected_condition_targets,
    )
    check(
        "C Cycle117 is 76,056 states / 441,682 edges / one 82-write terminal",
        c117.POSITIVE.states == 76_056
        and c117.POSITIVE.edges == 441_682
        and c117.POSITIVE.terminal_sizes == (82,)
        and not c117.POSITIVE.bad
        and not c117.POSITIVE.unexpected_condition_targets,
    )
    check(
        "C Cycle119 is 228,296 states / 1,477,702 edges / one 85-write terminal",
        c119.POSITIVE.states == 228_296
        and c119.POSITIVE.edges == 1_477_702
        and c119.POSITIVE.terminal_sizes == (85,)
        and not c119.POSITIVE.bad
        and not c119.POSITIVE.unexpected_condition_targets,
    )


def compiler_contract() -> None:
    section("D - Self-caged writer and next autonomous role port")
    c121 = c124.c121
    check(
        "D Cycle121 writes literal R_B00=10010000",
        c121.DATA_WORD == (1, 0, 0, 1, 0, 0, 0, 0)
        and c121.POSITIVE.states == 247_144
        and c121.POSITIVE.edges == 1_586_166
        and c121.POSITIVE.terminal_sizes == (99,)
        and not c121.POSITIVE.bad
        and not c121.POSITIVE.unexpected_condition_targets,
    )
    check(
        "D Cycle121 completion follows all eight physical data records",
        not c121.completion_barrier_violations(),
    )
    check(
        "D Cycle124 adapter is two canonical / 48 raw rows",
        len(c124.ADAPTER_TABLE) == 2
        and len(c124.ADAPTER_RAW) == 48
        and len(c124.FULL_RAW) == 8_744,
    )
    check(
        "D Cycle124 reaches one complete R_A01/R_B01 terminal",
        c124.POSITIVE.states == 248_680
        and c124.POSITIVE.edges == 1_594_358
        and c124.POSITIVE.terminal_sizes == (101,)
        and not c124.POSITIVE.bad
        and not c124.POSITIVE.unexpected_condition_targets,
    )
    check(
        "D next port is causally downstream of allocator and completed R_B00",
        not c124.ordering_violations(),
    )
    check(
        "D Cycle125 pins the direct-reuse failure without a broad no-go",
        len(c125.CANDIDATE_TABLE) == 12
        and len(c125.CANDIDATE_RAW) == 159
        and c125.CANDIDATE_RAW.get(()) == frozenset((c124.c121.TAIL_OUTPUT,))
        and len(c125.POSITIVE.unexpected_condition_targets) == 130
        and c125.POSITIVE.states == 1
        and c125.POSITIVE.edges == 0
        and c125.POSITIVE.terminals == 0,
    )


def scope_contract() -> None:
    section("E - Exact residual and constitutional firewall")
    note = normalized(NOTE) if NOTE.is_file() else ""
    c120_note = normalized(c120.NOTE) if c120.NOTE.is_file() else ""
    c121_note = normalized(c124.c121.NOTE)
    c124_note = normalized(c124.NOTE)
    c125_note = normalized(c125.NOTE)
    check("E Cycle126 note exists", NOTE.is_file())
    check(
        "E synthesis states zero live constitutional delta",
        "the live constitutional delta is zero" in note,
    )
    check(
        "E note preserves read-after-lock chronology",
        "reading neither forms, revises, nor finally locks the source" in note,
    )
    check(
        "E note includes Cycle115 in the exact bare-metal chronology",
        "cycles 112, 115, 117, 119, 121, and 124" in note
        and "inherited 264-record cycle-100 boundary" in note,
    )
    check(
        "E note names the exact next guarded-writer campaign",
        "frame_retaining_guarded_writer_induction" in note
        and "two-perpendicular-h0" in note,
    )
    check(
        "E note keeps all TOE lanes outside generic axiom prose",
        all(
            word in note
            for word in (
                "formation/actuality",
                "probability",
                "time",
                "quantum dynamics",
                "matter",
                "gravity/resource",
            )
        ),
    )
    check(
        "E note uses campaign status without laundering audit-retained grade",
        "every listed bounded positive above" in note
        and "recorded as cycle 120" in note
        and "already-live candidate table" in note
        and "every retained positive above" not in note
        and "retained as cycle 120" not in note,
    )
    check(
        "E kinetic primitive boundary is structural form, not no-clock rhetoric",
        "supplies structural c_t=c_s form only" in note
        and "no event rate, duration, clock calibration, or dynamics" in note,
    )
    check(
        "E Cycle126 N1-N8 gate is substantive and explicitly narrowed",
        all(f"n{index}" in note for index in range(1, 9))
        and "pass for the bounded cycle-124 literal-reuse" in note
        and "fail for a universal writer no-go" in note
        and "at least six materially distinct routes remain" in note
        and "with one scoped wall there is no pairwise independence table" in note
        and "cited bounded witness" in note
        and "compiler-wide or lattice-wide" in note
        and "strongest steelman against a writer no-go remains unresolved" in note,
    )
    check(
        "E cited campaign notes carry N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9))
        and all(f"n{index}" in c120_note for index in range(1, 9))
        and all(f"n{index}" in c121_note for index in range(1, 9))
        and all(f"n{index}" in c124_note for index in range(1, 9))
        and all(f"n{index}" in c125_note for index in range(1, 9)),
    )
    check(
        "E cited notes make no axiom addition",
        "no axiom addition" in c120_note
        and "no axiom addition" in c121_note
        and "no axiom addition" in c124_note
        and "no axiom addition" in c125_note,
    )
    check(
        "E Cycle126 writes only runner and review note",
        Path(__file__).parent == ROOT / "scripts" and NOTE.parent == REVIEW,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    foundation_contract()
    read_and_selection_contract()
    campaign_inventory_contract()
    compiler_contract()
    scope_contract()
    print(f"\nPASS={PASS} FAIL={FAIL}")
    print("CONSTITUTIONAL_DELTA=ZERO_NOW" if FAIL == 0 else "CONSTITUTIONAL_DELTA=UNRESOLVED")
    print("CLOSED=BOUNDED_READ_SELECT_WRITE_SUCCESSOR_CHAIN" if FAIL == 0 else "CLOSED=FAIL")
    print("NEXT=FRAME_RETAINING_GUARDED_WRITER_INDUCTION")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
