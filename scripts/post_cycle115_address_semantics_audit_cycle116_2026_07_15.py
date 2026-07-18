#!/usr/bin/env python3
"""Cycle 116: post-Cycle-115 address-semantics audit.

This runner separates three interfaces that the word ``addressable`` can hide:

1. one fixed selected output writer;
2. one relational-position-indexed fixed reference stream; and
3. a grown candidate/program selector controlling one common output port.

It consumes Cycle 112 literally for the fixed eight-bit word layout, Cycle 114
for the lawful two-valued schedule fork, and Cycle 115 for the first fixed
successor-role port.  It also distinguishes a
bounded probe-law union from a selected compiler law: compatibility or
membership in the probe union does not promote a row to Nature's L*.

The residual is a constructive exact-law target, not a universal no-go or an
axiom request.  No predecessor, foundation, axiom, primitive, registry, queue,
policy, audit, or git state is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
sys.path.insert(0, str(SCRIPTS))

import eight_bit_status_completion_front_cycle112_2026_07_15 as c112  # noqa: E402
import first_autonomous_successor_role_port_cycle115_2026_07_15 as c115  # noqa: E402
import lawful_h0_reference_fork_cycle114_2026_07_15 as c114  # noqa: E402
import live_empty_caged_router_patricia_cycle92_2026_07_15 as c92  # noqa: E402
import aux_gated_candidate_transport_cycle95_2026_07_15 as c95  # noqa: E402
import post_cycle109_strict_compiler_constitutional_delta_cycle111_2026_07_15 as c111  # noqa: E402
import strict_compiler_toe_ledger_cycle107_2026_07_15 as c107  # noqa: E402


NOTE = REVIEW / "POST_CYCLE115_ADDRESS_SEMANTICS_AUDIT_CYCLE116_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle92": REVIEW / "LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md",
    "cycle95": REVIEW / "AUX_GATED_CANDIDATE_TRANSPORT_CYCLE95_NOTE_2026-07-15.md",
    "cycle107": REVIEW / "STRICT_COMPILER_TOE_LEDGER_CYCLE107_NOTE_2026-07-15.md",
    "cycle111": REVIEW / "POST_CYCLE109_STRICT_COMPILER_CONSTITUTIONAL_DELTA_CYCLE111_NOTE_2026-07-15.md",
    "cycle112": REVIEW / "EIGHT_BIT_STATUS_COMPLETION_FRONT_CYCLE112_NOTE_2026-07-15.md",
    "cycle114": REVIEW / "LAWFUL_H0_REFERENCE_FORK_CYCLE114_NOTE_2026-07-15.md",
    "cycle115": REVIEW / "FIRST_AUTONOMOUS_SUCCESSOR_ROLE_PORT_CYCLE115_NOTE_2026-07-15.md",
}

H0 = "H0"
H1 = "H1"
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


def merge_raw(*tables):
    outputs = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


@dataclass(frozen=True)
class Interface:
    ident: str
    exact_meaning: str
    disposition: str
    evidence: tuple[str, ...]
    missing_for_next: str


I1 = "FIXED_SELECTED_OUTPUT_WRITER"
I2 = "RELATIONAL_POSITION_INDEXED_FIXED_REFERENCE_STREAM"
I3 = "CANDIDATE_SELECTED_COMMON_REFERENCE_PORT"
I4 = "GROWN_236_PROGRAM_ASSOCIATION_SOURCE"

INTERFACES = (
    Interface(
        I1,
        "one particular grown status/source history binds one designated physical output",
        "BOUNDED_POSITIVE",
        ("cycle109", "cycle112", "cycle114", "cycle115"),
        "none at fixed-writer resolution",
    ),
    Interface(
        I2,
        "one fixed word grows stable relative positions and a physical reader routes a named position to a common port",
        "LAYOUT_POSITIVE_READ_PATH_OPEN",
        ("cycle112", "cycle115"),
        "a grown address or fixed decoder path from a relative bit position to a common port",
    ),
    Interface(
        I3,
        "a grown candidate/address record controls the value at one common logical port",
        "OPEN_CONSTRUCTION",
        ("cycle92", "cycle95", "cycle112", "cycle114", "cycle115"),
        "two grown address histories, selector ancestry, and per-address schedule exhaustion",
    ),
    Interface(
        I4,
        "a grown physical source binds all 236 program identities to references and outputs",
        "DOWNSTREAM_STRENGTHENING",
        ("cycle92", "cycle95", "cycle107"),
        "physical program bank, bus, association source, and full-bank induction",
    ),
)


def source_and_primitive_contract() -> None:
    section("A - Sources, freshness boundary, and approved primitives")
    for name, path in {"cycle116_note": NOTE, **SOURCES}.items():
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
        "A registered primitive current paths are the consumed source notes",
        all(
            ROOT / nodes[node]["current_path"] == SOURCES[key]
            for node, key in (
                ("scale_reference_primitive", "scale"),
                ("kinetic_isotropy_primitive", "kinetic"),
                ("realized_state_primitive", "realized"),
            )
        ),
    )

    texts = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "A scale primitive remains units-only",
        has_all(texts["scale"], ("units conversion, not a physics axiom", "zero dimensionless content")),
    )
    check(
        "A kinetic primitive remains c_t=c_s form-only",
        has_all(texts["kinetic"], ("c_t = c_s", "not a new dynamics", "not a re-axiomatization of time")),
    )
    check(
        "A realized-state primitive remains pointwise-only",
        has_all(texts["realized"], ("pointwise evaluation", "no state, averaging over alternatives", "past hypothesis is a separate")),
    )
    check(
        "A Record still supplies presence-lock/readability but no address selector",
        has_all(texts["axioms"], (
            "records form",
            "when present, a record locks exactly one admissible local possibility",
            "only records are readable",
        ))
        and "address selector" not in texts["axioms"],
    )


def predecessor_resolution_contract() -> None:
    section("B - Predecessor evidence at the four resolutions")
    ledger107 = {entry.ident: entry for entry in c107.CONSTRUCTION_LEDGER}
    ledger111 = {entry.ident: entry for entry in c111.CONSTRUCTION_LEDGER}

    check(
        "B Cycle107 pins exactly 19 construction interfaces and 236 live programs",
        len(ledger107) == 19 and len(c92.c90.ROW_PROGRAMS) == 236,
    )
    check(
        "B Cycle92 classifier inventory is exact but physically unembedded",
        len(c92.c90.ROW_PROGRAMS) == 236
        and len(c92.PREFIXES) == 8_239
        and len(c92.SIGNIFICANT_PREFIXES) == 471
        and len(c92.PATRICIA_EDGES) == 470,
        (
            f"programs={len(c92.c90.ROW_PROGRAMS)} "
            f"prefixes={len(c92.PREFIXES)} patricia={len(c92.SIGNIFICANT_PREFIXES)}"
        ),
    )
    check(
        "B Cycle95 executes all 236 protocols with an explicit supplied apparatus boundary",
        len(c95.PROGRAM_ITEMS) == 236
        and ledger107["BOOT_PROGRAM_BANK"].disposition == c107.SUPPLIED_BOUNDARY
        and ledger107["STEP_SELECTOR_BANK"].disposition == c107.SUPPLIED_BOUNDARY,
    )
    check(
        "B Cycle109/111 raises only the one fixed selected-output bind",
        ledger107["STEP_SELECTED_OUTPUT_BIND"].disposition == c107.SUPPLIED_BOUNDARY
        and ledger111["STEP_SELECTED_OUTPUT_BIND"].disposition == c107.REPAIR_POSITIVE,
    )
    check(
        "B Cycle111's alternate-H0 object is exactly the one Cycle114 closes",
        c111.NEXT_OBJECT == "SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE"
        and "ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM" in SOURCES["cycle114"].read_text(encoding="utf-8"),
    )
    check(
        "B interface ladder is unique and ordered without collapsing bank selection into one bit",
        tuple(interface.ident for interface in INTERFACES) == (I1, I2, I3, I4)
        and len({interface.ident for interface in INTERFACES}) == 4,
    )


def cycle112_literal_contract() -> None:
    section("C - Literal Cycle112 fixed word layout and completion front")
    check(
        "C Cycle112 writer is exactly 13 canonical / 312 raw rows",
        len(c112.WRITER_TABLE) == 13 and len(c112.WRITER_RAW) == 312,
    )
    check(
        "C Cycle112 completion is exactly 4 canonical / 96 raw rows",
        len(c112.COMPLETION_TABLE) == 4 and len(c112.COMPLETION_RAW) == 96,
    )
    check(
        "C writer and completion additions are disjoint",
        set(c112.WRITER_RAW).isdisjoint(c112.COMPLETION_RAW),
    )
    check(
        "C full probe law is output-single-valued and alphabet-closed",
        all(len(values) == 1 for values in c112.FULL_RAW.values())
        and all(
            output in c112.c105.c89.FULL_ROLES
            for values in c112.FULL_RAW.values()
            for output in values
        ),
    )

    writer_bits = {
        site: output
        for site, output in c112.WRITER_OUTPUTS.items()
        if output in {H0, H1}
    }
    check(
        "C one fixed writer grows exactly eight ordered bit records containing both values",
        len(writer_bits) == 8
        and set(writer_bits.values()) == {H0, H1},
        str(Counter(writer_bits.values())),
    )
    check(
        "C all fixed writer and completion outputs are physically grown",
        set(c112.WRITER_OUTPUTS.items()).issubset(c112.GROWN_OUTPUTS.items())
        and set(c112.COMPLETION_OUTPUTS.items()).issubset(c112.GROWN_OUTPUTS.items()),
    )
    check(
        "C exhaustive graph is 73,656 states / 430,754 edges / one 69-write terminal",
        c112.POSITIVE.states == 73_656
        and c112.POSITIVE.edges == 430_754
        and c112.POSITIVE.terminals == 1
        and c112.POSITIVE.terminal_sizes == (69,)
        and not c112.POSITIVE.bad,
        str(c112.POSITIVE),
    )
    terminal = c112.positive_terminal_records()
    check(
        "C the unique terminal contains every pinned grown output",
        all(terminal.get(site) == output for site, output in c112.GROWN_OUTPUTS.items()),
    )
    check(
        "C Cycle112 source is one fixed record corpus rather than a candidate family",
        isinstance(c112.SOURCE, dict)
        and c112.SOURCE
        and not isinstance(c112.SOURCE, (list, tuple)),
        f"source_records={len(c112.SOURCE)}",
    )


def cycle114_literal_contract() -> None:
    section("D - Literal Cycle114 lawful alternate-value availability")
    check(
        "D Cycle114 selected route is exactly 3 canonical / 72 raw rows",
        len(c114.FORK_TABLE) == 3 and len(c114.FORK_RAW) == 72,
    )
    check(
        "D Cycle114 graph has the exact two lawful terminal histories",
        c114.POSITIVE.states == 17_880
        and c114.POSITIVE.edges == 88_642
        and len(c114.POSITIVE.terminals) == 2
        and c114.POSITIVE.terminal_sizes == (46, 48)
        and not c114.POSITIVE.bad,
        str(c114.POSITIVE),
    )
    terminal_records = c114.terminal_records()
    terminal_classes = Counter(c114.branch_label(records) for records in terminal_records)
    check(
        "D terminals are one unchanged H1 payload and one lawful H0 reject",
        terminal_classes == {"H1_PAYLOAD": 1, "H0_REJECT": 1},
        str(terminal_classes),
    )
    check(
        "D lawful H0 terminal contains copied source bit through reference/status/output",
        any(
            records.get(c114.FORK_COPY) == H0
            and records.get(c114.c106.REFERENCE) == H0
            and records.get(c114.c106.STATUS) == H0
            for records in terminal_records
        ),
    )
    check(
        "D Cycle114 itself names schedule selection rather than address selection",
        "ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM" in SOURCES["cycle114"].read_text(encoding="utf-8"),
    )


def cycle115_literal_contract() -> None:
    section("E - Literal Cycle115 fixed successor-role port")
    check(
        "E Cycle115 adapter is exactly 2 canonical / 48 raw rows",
        len(c115.SUCCESSOR_TABLE) == 2
        and len(c115.SUCCESSOR_RAW) == 48
        and set(c115.SUCCESSOR_RAW).isdisjoint(c112.FULL_RAW),
    )
    check(
        "E Cycle115 complete 8,096-row union is output-single-valued",
        len(c115.FULL_RAW) == 8_096
        and all(len(values) == 1 for values in c115.FULL_RAW.values()),
    )
    check(
        "E Cycle115 graph is 74,264 states / 433,682 edges / one 71-write terminal",
        c115.POSITIVE.states == 74_264
        and c115.POSITIVE.edges == 433_682
        and c115.POSITIVE.terminals == 1
        and c115.POSITIVE.terminal_sizes == (71,)
        and not c115.POSITIVE.bad
        and not c115.POSITIVE.unexpected_condition_targets,
        str(c115.POSITIVE),
    )
    terminal = c115.positive_terminal_records()
    check(
        "E terminal contains the fresh allocator and first successor role",
        terminal[c115.ALLOCATOR] == "R_A10"
        and terminal[c115.SUCCESSOR_PORT] == "R_B10",
    )
    before_successor = dict(terminal)
    before_successor.pop(c115.SUCCESSOR_PORT)
    successor_local = c115.c53.local_signature(
        before_successor,
        c115.SUCCESSOR_PORT,
    )
    check(
        "E successor is fixed-role gating, not forwarding an address bit value",
        successor_local
        == (
            ((-1, 0, 0), H0),
            ((0, 0, 1), "R_B11"),
            ((0, 1, 0), "R_A10"),
        )
        and c115.FULL_RAW[successor_local] == frozenset(("R_B10",)),
        str(successor_local),
    )
    cycle115_note = normalized(SOURCES["cycle115"])
    check(
        "E Cycle115 explicitly leaves coordinate readout and candidate selection open",
        has_all(cycle115_note, (
            "does not establish candidate-selected common-port addressability",
            "does not construct a coordinate-indexed read path",
            "cycle 114 contributes zero rows",
        )),
    )
    product_states = c115.POSITIVE.states * (c115.c105.RAIL_HORIZON + 1)
    product_edges = (
        c115.POSITIVE.edges * (c115.c105.RAIL_HORIZON + 1)
        + c115.POSITIVE.states * c115.c105.RAIL_HORIZON
    )
    check(
        "E Cycle115 rail product and covariance censuses are exact",
        product_states == 7_203_608
        and product_edges == 49_196_498
        and len(c115.FULL_RAW) * 24 == 194_304,
        f"states={product_states} edges={product_edges} rotations={len(c115.FULL_RAW) * 24}",
    )
    check(
        "E Cycle115 note pins corrupt, H0, rail, and rotation controls",
        has_all(cycle115_note, (
            "all eight one-bit changes",
            "wrong valid",
            "wrong ready",
            "typed-h0 reject history",
            "96-append repaired rail",
            "194,304 proper-cubic raw images",
        )),
    )


def interface_semantics_contract() -> None:
    section("F - Exact semantic ladder")
    dispositions = {interface.ident: interface.disposition for interface in INTERFACES}
    check(
        "F I1 fixed selected writer is a bounded positive",
        dispositions[I1] == "BOUNDED_POSITIVE"
        and c111.CLOSED_C109_INTERFACES[-1]
        == "STATUS_GATED_LITERAL_H1_TO_DIRECTED_R_B11_OR_REJECT_HANDOFF",
    )
    check(
        "F I2 has a complete fixed layout but no executable positional read path",
        dispositions[I2] == "LAYOUT_POSITIVE_READ_PATH_OPEN"
        and len({v for v in c112.WRITER_OUTPUTS.values() if v in {H0, H1}}) == 2
        and "address" in next(i for i in INTERFACES if i.ident == I2).missing_for_next,
    )
    check(
        "F I3 requires a grown selector ancestor at one common port",
        dispositions[I3] == "OPEN_CONSTRUCTION"
        and "selector ancestry" in next(i for i in INTERFACES if i.ident == I3).missing_for_next,
    )
    check(
        "F I4 is explicitly downstream of the one-bit common-port construction",
        dispositions[I4] == "DOWNSTREAM_STRENGTHENING"
        and len(c92.c90.ROW_PROGRAMS) == 236,
    )
    check(
        "F one fixed mixed word is not counted as two candidate histories",
        isinstance(c112.SOURCE, dict)
        and c112.POSITIVE.terminals == 1,
    )
    check(
        "F two schedule terminals are not counted as a candidate address",
        len(c114.POSITIVE.terminals) == 2
        and c114.FORK_COPY not in c114.COMMON_RECORDS,
    )


def probe_union_contract() -> None:
    section("G - Probe-law union versus selected compiler")
    overlap = set(c115.FULL_RAW) & set(c114.FORK_RAW)
    union = merge_raw(c115.FULL_RAW, c114.FORK_RAW)
    conflicts = {
        local: values
        for local, values in union.items()
        if len(values) != 1
    }
    check(
        "G selected Cycle115 and Cycle114 fork are table-disjoint and output-compatible",
        not overlap and not conflicts and len(union) == 8_168,
        f"overlap={len(overlap)} conflicts={len(conflicts)} union={len(union)}",
    )
    check(
        "G Cycles112/115 compile without importing Cycle114 as a predecessor",
        c112.__name__ != c114.__name__
        and "lawful_h0_reference_fork_cycle114" not in Path(c112.__file__).read_text(encoding="utf-8")
        and "lawful_h0_reference_fork_cycle114" not in Path(c115.__file__).read_text(encoding="utf-8"),
    )
    check(
        "G Cycle114 fork rows are not silently identified with the Cycle115 selected addition",
        set(c114.FORK_RAW) != set(c115.SUCCESSOR_RAW),
    )
    check(
        "G interface status does not depend on promoting the combined probe union",
        INTERFACES[1].evidence == ("cycle112", "cycle115")
        and "cycle114" in INTERFACES[2].evidence,
    )


def constitutional_and_note_contract() -> None:
    section("H - Constitutional delta and no-go discipline")
    note = normalized(NOTE)
    check(
        "H note distinguishes all three address resolutions and the bank strengthening",
        has_all(note, (I1.lower(), I2.lower(), I3.lower(), I4.lower())),
    )
    check(
        "H note separates probe union from selected L*",
        has_all(note, ("probe-law union is not the selected compiler", "u_probe", "nature's final law l")),
    )
    check(
        "H note grants the fixed layout but not an unbuilt positional reader",
        has_all(note, ("layout half", "stable relative bit position", "operational positional readout")),
    )
    check(
        "H note names the narrow common-port residual and zero constitutional delta",
        has_all(note, ("candidate_selected_common_reference_port", "constitutional delta is exactly zero")),
    )
    check(
        "H note consumes the Cycle115 successor without laundering it into address selection",
        has_all(note, (
            "literal cycle-115 credit",
            "74,264",
            "433,682",
            "port records the fixed role r_b10, not the value of d2",
            "r_b10_port_to_zero_source_word_and_completion",
        )),
    )
    check(
        "H note keeps LAW_IDENTITY_IF_NONDERIVED dormant",
        has_all(note, ("law_identity_if_nonderived", "remains dormant")),
    )
    check(
        "H note contains the complete N1-N8 discipline gate",
        all(f"n{index}" in note for index in range(1, 9))
        and note.count("attempted") >= 5,
    )
    check(
        "H residual is partial narrowing rather than universal no-go",
        has_all(note, ("fail for any universal no-go", "partial-narrowing-with-live-constructive-routes")),
    )
    check(
        "H note excludes occurrence/probability/clock/read-lock promotion",
        has_all(note, ("no occurrence", "probability", "clock", "read-lock", "final-law selection result follows")),
    )
    check(
        "H final disposition pins I1 positive, I2 partial, I3 open, and constitutional delta zero",
        has_all(note, (
            "i1 fixed_selected_output_writer bounded positive",
            "i2 relational_position_indexed_fixed_reference_stream layout positive / read path open",
            "i3 candidate_selected_common_reference_port open construction",
            "constitutional_delta zero",
        )),
    )


def main() -> int:
    source_and_primitive_contract()
    predecessor_resolution_contract()
    cycle112_literal_contract()
    cycle114_literal_contract()
    cycle115_literal_contract()
    interface_semantics_contract()
    probe_union_contract()
    constitutional_and_note_contract()
    print("\n" + "=" * 79)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print(f"I1={I1}:BOUNDED_POSITIVE")
    print(f"I2={I2}:LAYOUT_POSITIVE_READ_PATH_OPEN")
    print(f"I3={I3}:OPEN_CONSTRUCTION")
    print(f"I4={I4}:DOWNSTREAM_STRENGTHENING")
    print("PROBE_UNION_EQUALS_SELECTED_LSTAR=FALSE")
    print("CONSTITUTIONAL_DELTA=ZERO")
    print(f"NEXT={I3}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
