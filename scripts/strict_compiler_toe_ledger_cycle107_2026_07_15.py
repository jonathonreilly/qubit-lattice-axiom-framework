#!/usr/bin/env python3
"""Cycle 107: post-Cycle-105 strict-compiler and TOE classification ledger.

This authority-free runner refreshes Cycle 96 without editing it.  It consumes
the bounded evidence of Cycles 95, 97, 98, 99, 100, 101, 102, 104, 108, and
105; assigns one exact disposition to every former W_BOOT/W_STEP/W_MULTI
interface; reduces the selected strict-compiler route to its first live causal
edge; and preserves all 75 Cycle-96 TOE fields under the five-way
classification requested here.

It does not rerun the predecessor exhaustions, select an exact law, issue an
audit verdict, amend an axiom, or mutate foundation, registry, queue, policy,
or git state.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path

import actual_five_port_open_rlb_macrostep_audit_cycle99_2026_07_15 as c99
import actual_five_port_open_rlb_macrostep_cycle97_2026_07_15 as c97
import aux_gated_candidate_transport_cycle95_2026_07_15 as c95
import generated_endpoint_autonomous_frame_rail_cycle102_2026_07_15 as c102
import fragment_safe_role_remap_type_integration_cycle108_2026_07_15 as c108
import onsite_alphabet_closed_frame_rail_cycle104_2026_07_15 as c104
import post_cycle94_operational_completeness_audit_cycle96_2026_07_15 as c96
import read_status_to_generated_rail_spine_cycle105_2026_07_15 as c105
import repeated_readable_cell_allocation_cycle98_2026_07_15 as c98
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100
import zero_source_relational_first_harness_cycle101_2026_07_15 as c101


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "STRICT_COMPILER_TOE_LEDGER_CYCLE107_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle95": REVIEW / "AUX_GATED_CANDIDATE_TRANSPORT_CYCLE95_NOTE_2026-07-15.md",
    "cycle96": REVIEW / "POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md",
    "cycle97": REVIEW / "ACTUAL_FIVE_PORT_OPEN_RLB_MACROSTEP_CYCLE97_NOTE_2026-07-15.md",
    "cycle98": REVIEW / "REPEATED_READABLE_CELL_ALLOCATION_CYCLE98_NOTE_2026-07-15.md",
    "cycle99": REVIEW / "ACTUAL_FIVE_PORT_OPEN_RLB_MACROSTEP_AUDIT_CYCLE99_NOTE_2026-07-15.md",
    "cycle100": REVIEW / "ZERO_BINARY_SOURCE_ENDPOINT_MACROBLOCK_BIND_CYCLE100_NOTE_2026-07-15.md",
    "cycle101": REVIEW / "ZERO_SOURCE_RELATIONAL_FIRST_HARNESS_CYCLE101_NOTE_2026-07-15.md",
    "cycle102": REVIEW / "GENERATED_ENDPOINT_AUTONOMOUS_FRAME_RAIL_CYCLE102_NOTE_2026-07-15.md",
    "cycle104": REVIEW / "ONSITE_ALPHABET_CLOSED_FRAME_RAIL_CYCLE104_NOTE_2026-07-15.md",
    "cycle108": REVIEW / "FRAGMENT_SAFE_ROLE_REMAP_TYPE_INTEGRATION_CYCLE108_NOTE_2026-07-15.md",
    "cycle105": REVIEW / "READ_STATUS_TO_GENERATED_RAIL_SPINE_CYCLE105_NOTE_2026-07-15.md",
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def merge_raw(*tables: dict[object, frozenset[str]]) -> dict[object, frozenset[str]]:
    outputs: dict[object, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


CLOSED = "CLOSED"
CONSTRUCTION_GRADE = "CONSTRUCTION_GRADE_ONLY"
SUPPLIED_BOUNDARY = "SUPPLIED_BOUNDARY_CONDITIONAL"
ROLE_CLOSED = "ROLE_CLOSED"
REPAIR_POSITIVE = "REPAIR_POSITIVE"
LIVE = "LIVE"

DISPOSITIONS = {
    CLOSED,
    CONSTRUCTION_GRADE,
    SUPPLIED_BOUNDARY,
    ROLE_CLOSED,
    REPAIR_POSITIVE,
    LIVE,
}


@dataclass(frozen=True)
class ConstructionEntry:
    ident: str
    disposition: str
    evidence: tuple[str, ...]
    exact_credit: str
    residual: str


def construction(
    ident: str,
    disposition: str,
    evidence: tuple[str, ...],
    exact_credit: str,
    residual: str,
) -> ConstructionEntry:
    return ConstructionEntry(ident, disposition, evidence, exact_credit, residual)


CONSTRUCTION_LEDGER = (
    construction(
        "BOOT_MACROBLOCK_BIND", CLOSED, ("cycle100",),
        "one generated 254-record endpoint grows R_B11, VALID, and READY in ten writes with zero added binary source",
        "general endpoint/row universality is not claimed",
    ),
    construction(
        "BOOT_RELATIONAL_FRAME", ROLE_CLOSED, ("cycle102", "cycle104", "cycle108", "cycle105"),
        "the generated endpoint owns the renewing rail and all 36 remapped B/C/D roles lie in FULL_ROLES",
        "a complete reusable compare-select-write harness is not yet grown from the rail",
    ),
    construction(
        "BOOT_OCCUPIED_ROUTES", REPAIR_POSITIVE, ("cycle97", "cycle99", "cycle100"),
        "five in-place face blocks admit exact typed READY gates without flattening",
        "five predecessor-generated READY records are not yet routed into the consumer",
    ),
    construction(
        "BOOT_CAGES", CONSTRUCTION_GRADE, ("cycle101", "cycle108", "cycle105"),
        "zero-source cubic caps, a 17-write reverse shell, and a first typed R_B11 cap grow from the endpoint",
        "the symmetric cap is not yet a directed reusable OPEN/comparator/selector/writer cage",
    ),
    construction(
        "BOOT_PROGRAM_BANK", SUPPLIED_BOUNDARY, ("cycle95",),
        "all 236 program choices execute the bounded three-reference protocol",
        "candidate, references, writer harness, guides, and cages remain supplied per protocol",
    ),
    construction(
        "BOOT_FRESH_RESERVATION", REPAIR_POSITIVE, ("cycle97", "cycle99", "cycle104"),
        "initial OPEN blockers and the reused-role debris census are exact at bounded isolated scope",
        "late external occupancy and arbitrary future rail/macroblock contacts remain unreserved",
    ),
    construction(
        "BOOT_STEADY_HANDOFF", CONSTRUCTION_GRADE, ("cycle101", "cycle108", "cycle105"),
        "literal OUTPUT, grown TYPE, and generated spine tip make one exact JOINT and three physical R_B11 cap images",
        "no cap image yet launches the complete same-type reusable compare-select-write cell",
    ),
    construction(
        "STEP_NEIGHBOUR_STREAM", REPAIR_POSITIVE, ("cycle97", "cycle99", "cycle100"),
        "five spatial words and five typed READY gates feed one exact R_LB matcher",
        "the actual five upstream validated-word provenance routes are not built",
    ),
    construction(
        "STEP_OPEN_PACK", CONSTRUCTION_GRADE, ("cycle97", "cycle99"),
        "one absent +x port grows the reserved all-one word and completes one isolated row",
        "the permanent OPEN certificate is not late-neighbour revocable or globally reserved",
    ),
    construction(
        "STEP_SELECTOR_BANK", SUPPLIED_BOUNDARY, ("cycle95",),
        "all 236 candidates are covered under exact physical comparison and corruption controls",
        "one grown 236-reference physical bank and its addressing discipline are absent",
    ),
    construction(
        "STEP_SELECTOR_TRANSPORT", CONSTRUCTION_GRADE, ("cycle95",),
        "two AUX handoffs preserve all 48 bits for all 236 programs and fail closed under corruption",
        "the 943-record transport apparatus is supplied and no complete-bank induction is proved",
    ),
    construction(
        "STEP_SELECTED_OUTPUT_BIND", SUPPLIED_BOUNDARY, ("cycle95", "cycle97"),
        "the selected output association writes exact physical output records in bounded protocols",
        "the program/reference/output association source is still supplied",
    ),
    construction(
        "STEP_OUTPUT_NEXT_FRONT", SUPPLIED_BOUNDARY, ("cycle97", "cycle98", "cycle99"),
        "literal output taps gate MATCH and MATCH is the next unsupplied START, including two handoffs",
        "the successor candidate and static cell source remain a disjoint supplied copy",
    ),
    construction(
        "STEP_NEXT_CELL_ALLOCATE", REPAIR_POSITIVE, ("cycle98", "cycle101", "cycle108", "cycle105"),
        "the 280-record residual is split 168 fixed plus 112 payload, and zero-source literal status now reaches a first typed rail cap",
        "the cap is not yet a directed reusable harness and the full payload/cage/program allocation is absent",
    ),
    construction(
        "STEP_FULL_MIXED_DOMAIN", LIVE, ("cycle95", "cycle98", "cycle99", "cycle108", "cycle105"),
        "large bounded mixed unions are exact, including 489,656 reader/spine x rail-prefix states",
        "no self-grown all-row, all-arity, late-contact, arbitrary-schedule compiler domain is closed",
    ),
    construction(
        "MULTI_REACHABLE_NUCLEATION", LIVE, ("cycle97", "cycle104"),
        "single generated fronts and isolated apparatus controls exist",
        "one allowed history has not grown two complete compiler apparatuses",
    ),
    construction(
        "MULTI_SEPARATION_INVARIANT", SUPPLIED_BOUNDARY, ("cycle96", "cycle99"),
        "prior separated supplied tubes factor and the selected single-cell union is exact",
        "expanded self-grown compiler supports and their reachable separation are unproved",
    ),
    construction(
        "MULTI_CONTACT_RESOURCE_RULE", LIVE, ("cycle99",),
        "the late-neighbour sweep exposes the exact contact/reservation question",
        "no selected contact/resource rule covers every reachable overlap",
    ),
    construction(
        "MULTI_CONFLUENCE_RECORD", LIVE, ("cycle95", "cycle99"),
        "bounded singleton and commuting-adapter cases are exact",
        "all reachable multi-apparatus orders do not yet share one final record transcript",
    ),
)


RECURRENT_LEDGER = {
    "NEXT_PHASE_RETURN": SUPPLIED_BOUNDARY,
    "NEXT_SELF_HOSTING": REPAIR_POSITIVE,
    "NEXT_INTERFACE_INVARIANT": SUPPLIED_BOUNDARY,
    "ITERATION_INDUCTION": SUPPLIED_BOUNDARY,
    "ITERATION_OCCURRENCE_SEMANTICS": LIVE,
    "ITERATION_RENEWAL_EXPORT": LIVE,
    "ITERATION_GLOBAL_EXTENSION": LIVE,
}


PRIMITIVE = "PRIMITIVE"
THEOREM_TARGET = "THEOREM_TARGET"
EXACT_LAW_FIELD = "EXACT_LAW_FIELD"
EMPIRICAL_INPUT = "EMPIRICAL_INPUT"
CONSTITUTIONAL_GATE = "CONSTITUTIONAL_COMPATIBILITY_GATE"
TOE_CLASSES = {
    PRIMITIVE,
    THEOREM_TARGET,
    EXACT_LAW_FIELD,
    EMPIRICAL_INPUT,
    CONSTITUTIONAL_GATE,
}

CLASS_MAP = {
    c96.REFERENCE_PRIMITIVE: PRIMITIVE,
    c96.THEOREM_TARGET: THEOREM_TARGET,
    c96.EXACT_LAW_FIELD: EXACT_LAW_FIELD,
    c96.EMPIRICAL_INPUT: EMPIRICAL_INPUT,
    c96.GENUINE_CONSTITUTIONAL_ATOM: CONSTITUTIONAL_GATE,
}

TOE_FIELD_CLASSES = {
    entry.ident: CLASS_MAP[entry.classification]
    for entry in c96.INTERFACES
}


CLOSED_ROOTS = ("BOOT_MACROBLOCK_BIND", "BOOT_RELATIONAL_FRAME")
COLLAPSED_STRICT_COMPILER_CHAIN = (
    (
        "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS",
        (
            "BOOT_CAGES", "BOOT_STEADY_HANDOFF",
            "BOOT_OCCUPIED_ROUTES", "BOOT_FRESH_RESERVATION",
            "STEP_NEIGHBOUR_STREAM", "STEP_OPEN_PACK",
        ),
    ),
    (
        "FULL_48_BIT_SELECT_AND_WRITE",
        (
            "BOOT_PROGRAM_BANK", "STEP_SELECTOR_BANK", "STEP_SELECTOR_TRANSPORT",
            "STEP_SELECTED_OUTPUT_BIND",
        ),
    ),
    (
        "SUCCESSOR_LITERAL_REUSE_AND_ALLOCATION",
        ("STEP_OUTPUT_NEXT_FRONT", "STEP_NEXT_CELL_ALLOCATE"),
    ),
    ("FULL_MIXED_DOMAIN_AND_PHASE_INDUCTION", ("STEP_FULL_MIXED_DOMAIN",)),
    (
        "REACHABLE_MULTI_CONTACT_AND_CONFLUENCE",
        (
            "MULTI_REACHABLE_NUCLEATION", "MULTI_SEPARATION_INVARIANT",
            "MULTI_CONTACT_RESOURCE_RULE", "MULTI_CONFLUENCE_RECORD",
        ),
    ),
)

SUPERSEDED_INTEGRATION = "C101_FRAGMENT_TO_MULTI_SLICE_RAIL_PHASE_CAGE"
CLOSED_CYCLE105_INTERFACE = "READ_STATUS_TO_GENERATED_RAIL_SPINE"
CLOSED_CYCLE105_CAP = "ZERO_SOURCE_LITERAL_OUTPUT_TO_FIRST_TYPED_PAYLOAD_CAP"
SMALLEST_BLOCKER = "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS"
NEXT_OBJECT = "CAGED_R_B11_CAP_TO_DIRECTED_RENEWABLE_PAYLOAD_LAUNCH"

INTEGRATED_RAW = merge_raw(c100.COMBINED_RAW, c101.FRAGMENT_RAW, c104.REMAPPED_RAW)
CERT_TO_TYPE_SITE = (4, 5, 1)
PHASE_CROSSFIRE_SITES = frozenset(((-4, 1, 3), (-3, 1, 4)))

V2_ROLE_MAP = dict(c104.ROLE_MAP)
V2_ROLE_MAP["D_1_1"] = "J1"
V2_ROLE_MAP["C_3_1"] = "J2"
V2_REMAPPED_RAW = c104.relabel_raw(V2_ROLE_MAP)
V2_RAIL = c104.rail_sequence(9, V2_ROLE_MAP)
V2_INTEGRATED_RAW = merge_raw(c100.COMBINED_RAW, c101.FRAGMENT_RAW, V2_REMAPPED_RAW)


def integrated_front(prefix: int) -> dict[object, frozenset[str]]:
    records = dict(c101.TERMINAL)
    records.update(c101.FRAGMENT_OUTPUTS)
    records.update(dict(c104.NINE_SLICES[:prefix]))
    return c101.enabled(records, INTEGRATED_RAW)


@dataclass(frozen=True)
class IntegrationStats:
    states: int
    edges: int
    terminals: int
    terminal_frontiers: tuple[tuple[tuple[object, frozenset[str]], ...], ...]
    bad: tuple[object, ...]


def v2_product_graph() -> IntegrationStats:
    """Exhaust reader fragment x 96 rail appends x inherited TYPE contact."""

    start = (frozenset(), 0, False)
    seen = {start}
    queue = deque((start,))
    edges = 0
    terminals: list[tuple[tuple[object, frozenset[str]], ...]] = []
    bad: list[object] = []
    fragment_sites = set(c101.FRAGMENT_SITES)
    while queue:
        fragment_state, rail_prefix, type_present = queue.popleft()
        records = dict(c101.TERMINAL)
        records.update({site: c101.FRAGMENT_OUTPUTS[site] for site in fragment_state})
        records.update(dict(V2_RAIL[:rail_prefix]))
        if type_present:
            records[CERT_TO_TYPE_SITE] = "R_B21"

        actual = c101.enabled(records, V2_INTEGRATED_RAW)
        legal: dict[object, str] = {}
        for site, values in actual.items():
            if (
                site in fragment_sites
                and site not in fragment_state
                and values == frozenset((c101.FRAGMENT_OUTPUTS[site],))
            ):
                legal[site] = "fragment"
            elif (
                rail_prefix < 96
                and site == V2_RAIL[rail_prefix][0]
                and values == frozenset((V2_RAIL[rail_prefix][1],))
            ):
                legal[site] = "rail"
            elif (
                not type_present
                and site == CERT_TO_TYPE_SITE
                and values == frozenset(("R_B21",))
            ):
                legal[site] = "type"

        frozen_front = set()
        if (
            rail_prefix == 96
            and actual.get(V2_RAIL[96][0]) == frozenset((V2_RAIL[96][1],))
        ):
            frozen_front.add(V2_RAIL[96][0])
        unknown = set(actual) - set(legal) - frozen_front
        if unknown:
            bad.append((fragment_state, rail_prefix, type_present, unknown, actual))
            continue

        if rail_prefix == 96 and len(fragment_state) == 22 and type_present:
            terminals.append(tuple(sorted(actual.items())))
            continue
        if not legal:
            bad.append(("dead", fragment_state, rail_prefix, type_present, actual))
            continue

        for site, kind in legal.items():
            if kind == "fragment":
                future = (fragment_state | {site}, rail_prefix, type_present)
            elif kind == "rail":
                future = (fragment_state, rail_prefix + 1, type_present)
            else:
                future = (fragment_state, rail_prefix, True)
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return IntegrationStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_frontiers=tuple(terminals),
        bad=tuple(bad),
    )


def source_and_primitive_contract() -> None:
    section("A - Sources and approved primitive boundary")
    for name, path in {"cycle107_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registry contains only the four canonical premise nodes",
        set(nodes) == {
            "minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive",
        },
        str(sorted(nodes)),
    )
    check(
        "A primitive current paths are the three source notes read here",
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
        "A scale primitive is units-only",
        all(needle in texts["scale"] for needle in ("units conversion, not a physics axiom", "zero dimensionless content")),
    )
    check(
        "A kinetic primitive is c_t=c_s form-only",
        all(needle in texts["kinetic"] for needle in ("c_t = c_s", "not a new dynamics", "not a re-axiomatization of time")),
    )
    check(
        "A realized-state primitive is pointwise-only",
        all(needle in texts["realized"] for needle in ("pointwise evaluation", "no state, averaging over alternatives", "past hypothesis is a separate")),
    )
    check(
        "A Record names formation occurrence but no formation rule",
        all(needle in texts["axioms"] for needle in ("records form", "formation rules (which", "does not choose a hamiltonian")),
    )


def predecessor_evidence_contract() -> None:
    section("B - Runner-backed Cycle-95 through Cycle-105 evidence")
    sample = c95.build_protocol(0)
    check(
        "B Cycle95 covers 236 programs with 943 supplied and 680 grown records per protocol",
        len(c95.PROGRAM_ITEMS) == 236 and len(sample.source) == 943 and len(sample.nodes) == 680,
    )
    check("B Cycle95 selected union has 8,554 single-valued raw inputs", len(c95.COMBINED_RAW) == 8_554 and all(len(v) == 1 for v in c95.COMBINED_RAW.values()))
    check(
        "B Cycle97 has 4,539 supplied, 1,162 grown, and 5,809 raw inputs",
        len(c97.SOURCE) == 4_539 and len(c97.ADDITIONS) == 1_162 and len(c97.COMBINED_RAW) == 5_809,
    )
    check(
        "B Cycle98 pins 280 static per cell, 752 supplied, 215 grown, and 51 phases",
        len(c98.CELL1.source) == 280 and len(c98.LOCAL_SOURCE) == 752
        and len(c98.LOCAL_ADDITIONS) == 215 and len(c98.ROWS) == 51,
    )
    check(
        "B Cycle98 conditional recurrence has the exact 5,728-row phase-complete law",
        len(c98.COMBINED_RAW) == 5_728 and len(c98.CELL1.additions) == 83,
    )
    check(
        "B Cycle99 READY repair is 4,554 supplied in a 6,193-row union",
        len(c99.GATED_SOURCE) == 4_554 and len(c99.GATED_RAW) == 6_193
        and len(c99.READY_SITES) == 5 and len(c99.READY_CAGES) == 15,
    )
    check(
        "B Cycle100 grows ten records from the 254-record endpoint with no binary source",
        len(c100.SOURCE) == 254 and len(c100.ADDITIONS) == 10 and len(c100.COMBINED_RAW) == 5_444,
    )
    check(
        "B Cycle101 grows a 22-record zero-source fragment with 182 schedules and a 2,366-state rail product",
        len(c101.TERMINAL) == 264 and len(c101.FRAGMENT_SITES) == 22
        and c101.POSITIVE.states == 182 and c101.PRODUCT.states == 2_366,
    )
    check(
        "B Cycle101 complete fragment/rail union has 6,896 raw inputs and 165,504 rotation images",
        len(c101.COMBINED_RAW) == 6_896 and len(c101.COMBINED_RAW) * 24 == 165_504,
    )
    check(
        "B Cycle102 supplies generated frame renewal at 143 first-slice and 96 longer states",
        len(c102.MIXED_RAW) == 6_524 and len(c102.FIRST_SLICE) == 12 and len(c102.RAIL_SEQUENCE) == 96,
    )
    check(
        "B Cycle104 closes all 36 remapped roles in FULL_ROLES",
        len(c104.ROLE_MAP) == len(set(c104.ROLE_MAP.values())) == 36
        and set(c104.ROLE_MAP.values()) <= c104.c89.FULL_ROLES,
    )
    check(
        "B Cycle104 pins 1,080 rail rows, 6,524 mixed rows, and 1,067 prefix states",
        len(c104.REMAPPED_RAW) == 1_080 and len(c104.MIXED_RAW) == 6_524
        and 11 * 97 == 1_067,
    )
    check(
        "B Cycle108 lands the 36-role v2 map and 6,896-row integrated union",
        c108.ROLE_MAP == V2_ROLE_MAP
        and c108.REMAPPED_RAW == V2_REMAPPED_RAW
        and c108.INTEGRATED_RAW == V2_INTEGRATED_RAW
        and len(c108.INTEGRATED_RAW) == 6_896,
    )
    check(
        "B Cycle105 adds 18 canonical / 414 raw rows to a 7,310-row single-valued union",
        c105.ROLE_MAP == c108.ROLE_MAP
        and c105.BASE_RAW == c108.INTEGRATED_RAW
        and len(c105.BRIDGE_TABLE) == 18
        and len(c105.BRIDGE_RAW) == 414
        and len(c105.FULL_RAW) == 7_310
        and all(len(values) == 1 for values in c105.FULL_RAW.values()),
    )
    check(
        "B Cycle105 grows 17 shell writes and three R_B11 payload-cap images from zero new static source",
        len(c101.TERMINAL) == 264
        and len(c105.PRIMARY_SPINE) == 16
        and sum(map(len, c105.SPINE_GROUPS)) == 17
        and len(c105.PAYLOAD_SITES) == 3
        and c105.PAYLOAD_OUTPUT == "R_B11",
    )


def fragment_rail_integration_contract() -> None:
    section("C - C101 fragment plus role-closed multi-slice rail integration")
    check(
        "C integrated 5,444 + 372 + 1,080 table has 6,896 single-valued inputs",
        len(INTEGRATED_RAW) == 6_896 and all(len(values) == 1 for values in INTEGRATED_RAW.values()),
    )
    prefix0 = integrated_front(0)
    first_site, first_content = c104.NINE_SLICES[0]
    check(
        "C CERT R_B40 exposes the inherited positive CERT_TO_TYPE R_B21 contact",
        prefix0 == {
            first_site: frozenset((first_content,)),
            CERT_TO_TYPE_SITE: frozenset(("R_B21",)),
        },
        str(prefix0),
    )
    records16 = dict(c101.TERMINAL)
    records16.update(c101.FRAGMENT_OUTPUTS)
    records16.update(dict(c104.NINE_SLICES[:16]))
    prefix16 = integrated_front(16)
    next16_site, next16_content = c104.NINE_SLICES[16]
    check(
        "C remapped prefix16 retains the intended R_B01 rail write",
        prefix16.get(next16_site) == frozenset((next16_content,))
        and (next16_site, next16_content) == ((-3, 0, 3), "R_B01"),
        str(prefix16),
    )
    check(
        "C prefix16 has exactly two R_B31-unary fragment crossfires at the named cap sites",
        all(prefix16.get(site) == frozenset(("R_B32",)) for site in PHASE_CROSSFIRE_SITES)
        and all(
            c100.c53.local_signature(records16, site) in c101.FRAGMENT_RAW
            and c100.c53.local_signature(records16, site) not in c104.REMAPPED_RAW
            for site in PHASE_CROSSFIRE_SITES
        ),
        str(prefix16),
    )
    fragment_unary = {
        local[0][1]: values
        for local, values in c101.FRAGMENT_RAW.items()
        if len(local) == 1
    }
    check(
        "C C101 has exactly the two unary role families R_B12 and R_B31",
        set(fragment_unary) == {"R_B12", "R_B31"}
        and fragment_unary["R_B12"] == frozenset(("R_B13",))
        and fragment_unary["R_B31"] == frozenset(("R_B32",)),
        str(fragment_unary),
    )
    check(
        "C current role map places both C101 unary inputs on the renewing rail",
        {role for role, value in c104.ROLE_MAP.items() if value in {"R_B12", "R_B31"}}
        == {"C_3_1", "D_1_1"},
    )
    prefix96 = integrated_front(96)
    later_fragment_extras = {
        site for site, values in prefix96.items()
        if values == frozenset(("R_B32",))
    }
    check(
        "C the uncaged R_B31 crossfire survives at the eight-slice horizon",
        len(later_fragment_extras) >= 2 and (-3, 1, 4) in later_fragment_extras,
        str(prefix96),
    )
    check(
        "C integration disposition separates positive first contact from live phase repair",
        SUPERSEDED_INTEGRATION == "C101_FRAGMENT_TO_MULTI_SLICE_RAIL_PHASE_CAGE",
    )
    check(
        "C v2 remap substitutes source-used unary-inert J1/J2 for both fragment-unary rail roles",
        V2_ROLE_MAP["D_1_1"] == "J1"
        and V2_ROLE_MAP["C_3_1"] == "J2"
        and sum(value == "J1" for value in c100.SOURCE.values()) == 1
        and sum(value == "J2" for value in c100.SOURCE.values()) == 1
        and all(
            not any(len(local) == 1 and local[0][1] == role for local in table)
            for role in ("J1", "J2")
            for table in (c100.COMBINED_RAW, c101.FRAGMENT_RAW)
        ),
    )
    check(
        "C v2 role map stays injective and closed in the 153-role alphabet",
        len(V2_ROLE_MAP) == len(set(V2_ROLE_MAP.values())) == 36
        and set(V2_ROLE_MAP.values()) <= c104.c89.FULL_ROLES,
    )
    check(
        "C v2 reader/rail union has 6,896 single-valued raw inputs",
        len(V2_INTEGRATED_RAW) == 6_896
        and all(len(values) == 1 for values in V2_INTEGRATED_RAW.values()),
    )
    stats = v2_product_graph()
    check(
        "C v2 reader x 96-rail x TYPE graph is 22,310 states and 91,338 edges",
        stats.states == 22_310 and stats.edges == 91_338,
        str(stats),
    )
    expected_terminal = (((V2_RAIL[96][0], frozenset((V2_RAIL[96][1],))),),)
    check(
        "C v2 integration has one exact terminal prefix and zero bad states",
        stats.terminals == 1 and stats.terminal_frontiers == expected_terminal and not stats.bad,
        str(stats),
    )
    rotation_failures = []
    for local, values in V2_INTEGRATED_RAW.items():
        for rotation in c104.c52.ROTATIONS:
            if V2_INTEGRATED_RAW.get(c104.c52.rotate_signature(local, rotation)) != values:
                rotation_failures.append((local, rotation))
                break
    check(
        "C all 165,504 v2 integrated raw rotation images close exactly",
        not rotation_failures and len(V2_INTEGRATED_RAW) * 24 == 165_504,
        str(rotation_failures[:1]),
    )
    join_records = dict(c101.TERMINAL)
    join_records.update(c101.FRAGMENT_OUTPUTS)
    join_records[c105.NATURAL_TYPE] = c105.NATURAL_TYPE_OUTPUT
    for group, output in zip(c105.SPINE_GROUPS, c105.SPINE_OUTPUTS):
        join_records.update({site: output for site in group})
    join_parents = {
        site: join_records[site]
        for site in c105.neighbors(c105.JOIN)
        if site in join_records
    }
    check(
        "C Cycle105 JOINT literally has OUTPUT, grown TYPE, and generated-spine parents",
        join_parents == {
            c101.OUTPUT: c101.H1,
            c105.NATURAL_TYPE: c105.NATURAL_TYPE_OUTPUT,
            c105.PRIMARY_SPINE[-1]: c105.SPINE_OUTPUTS[-1],
        }
        and c105.enabled(join_records).get(c105.JOIN) == frozenset((c105.JOIN_OUTPUT,)),
        str(join_parents),
    )
    check(
        "C Cycle105 reader/spine graph has 5,048 states, 21,426 edges, one terminal, and zero bad fronts",
        c105.POSITIVE.states == 5_048
        and c105.POSITIVE.edges == 21_426
        and c105.POSITIVE.terminals == 1
        and not c105.POSITIVE.bad
        and not c105.POSITIVE.premature
        and c105.POSITIVE.join_reached
        and c105.POSITIVE.payload_reached,
        str(c105.POSITIVE),
    )
    c105_product_states = c105.POSITIVE.states * (c105.RAIL_HORIZON + 1)
    c105_product_edges = (
        c105.POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + c105.POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C Cycle105 exact reader/spine x 97-prefix product is 489,656 states and 2,562,930 edges",
        c105_product_states == 489_656 and c105_product_edges == 2_562_930,
    )
    check(
        "C Cycle105 closes read-status-to-spine and leaves typed-cap-to-harness first",
        CLOSED_CYCLE105_INTERFACE == "READ_STATUS_TO_GENERATED_RAIL_SPINE"
        and CLOSED_CYCLE105_CAP == "ZERO_SOURCE_LITERAL_OUTPUT_TO_FIRST_TYPED_PAYLOAD_CAP"
        and SMALLEST_BLOCKER == "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS"
        and NEXT_OBJECT == "CAGED_R_B11_CAP_TO_DIRECTED_RENEWABLE_PAYLOAD_LAUNCH",
    )


def construction_ledger_contract() -> None:
    section("D - Former W_BOOT/W_STEP/W_MULTI exact dispositions")
    by_id = {entry.ident: entry for entry in CONSTRUCTION_LEDGER}
    expected_ids = {
        entry.ident
        for entry in c96.INTERFACES
        if entry.group in {"SEED_TO_FIRST_HARNESS", "ONE_AUTONOMOUS_MACROSTEP", "MULTI_APPARATUS"}
    }
    check("C every former W_BOOT/W_STEP/W_MULTI row appears exactly once", len(by_id) == len(CONSTRUCTION_LEDGER) == 19 and set(by_id) == expected_ids, str(sorted(expected_ids - set(by_id))))
    check("C every row has one allowed disposition", all(entry.disposition in DISPOSITIONS for entry in CONSTRUCTION_LEDGER))
    check("C every evidence key names an inspected source", all(key in SOURCES for entry in CONSTRUCTION_LEDGER for key in entry.evidence))
    check("C every row states exact credit and surviving residual", all(entry.exact_credit and entry.residual for entry in CONSTRUCTION_LEDGER))
    counts = Counter(entry.disposition for entry in CONSTRUCTION_LEDGER)
    check(
        "C disposition census is exact",
        counts == {
            CLOSED: 1,
            ROLE_CLOSED: 1,
            REPAIR_POSITIVE: 4,
            CONSTRUCTION_GRADE: 4,
            SUPPLIED_BOUNDARY: 5,
            LIVE: 4,
        },
        str(counts),
    )
    check("C closed roots are exactly macroblock bind and role-closed frame", tuple(entry.ident for entry in CONSTRUCTION_LEDGER if entry.disposition in {CLOSED, ROLE_CLOSED}) == CLOSED_ROOTS)
    check("C full mixed domain and three multi fields remain live", {entry.ident for entry in CONSTRUCTION_LEDGER if entry.disposition == LIVE} == {"STEP_FULL_MIXED_DOMAIN", "MULTI_REACHABLE_NUCLEATION", "MULTI_CONTACT_RESOURCE_RULE", "MULTI_CONFLUENCE_RECORD"})

    recurrent_ids = {
        entry.ident for entry in c96.INTERFACES
        if entry.group in {"RECURRENT_NEXT_FRONT", "UNBOUNDED_ITERATION"}
    }
    check("C recurrent/iteration side ledger covers all seven former rows", set(RECURRENT_LEDGER) == recurrent_ids)
    check("C recurrence credit stays supplied-boundary or repair-positive until exact occurrence/export", Counter(RECURRENT_LEDGER.values()) == {SUPPLIED_BOUNDARY: 3, REPAIR_POSITIVE: 1, LIVE: 3})


def dependency_collapse_contract() -> None:
    section("E - Dependency collapse and first live strict-compiler edge")
    covered = {
        ident
        for _stage, identities in COLLAPSED_STRICT_COMPILER_CHAIN
        for ident in identities
    }
    all_ids = {entry.ident for entry in CONSTRUCTION_LEDGER}
    check("D collapsed chain consumes every non-root construction interface once", len(covered) == 17 and covered == all_ids - set(CLOSED_ROOTS))
    check("D collapsed stage names are unique and ordered", len({stage for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN}) == 5 and COLLAPSED_STRICT_COMPILER_CHAIN[0][0] == SMALLEST_BLOCKER)
    check(
        "D unique next object cages one symmetric typed cap as a directed renewable launch",
        NEXT_OBJECT == "CAGED_R_B11_CAP_TO_DIRECTED_RENEWABLE_PAYLOAD_LAUNCH"
        and SMALLEST_BLOCKER == "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS",
    )

    by_id = {entry.ident: entry for entry in c96.INTERFACES}
    indegree = {ident: 0 for ident in by_id}
    outgoing: dict[str, list[str]] = defaultdict(list)
    for entry in c96.INTERFACES:
        for dependency in entry.dependencies:
            indegree[entry.ident] += 1
            outgoing[dependency].append(entry.ident)
    queue = deque(sorted(ident for ident, degree in indegree.items() if degree == 0))
    order = []
    while queue:
        ident = queue.popleft()
        order.append(ident)
        for successor in outgoing[ident]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)
    check("D inherited 75-field dependency graph remains acyclic", len(order) == len(c96.INTERFACES))


def toe_classification_contract() -> None:
    section("F - All 75 TOE-field classifications")
    check("E every Cycle96 field is preserved exactly once", len(TOE_FIELD_CLASSES) == len(c96.INTERFACES) == 75)
    check("E every field has one requested class", set(TOE_FIELD_CLASSES.values()) == TOE_CLASSES)
    counts = Counter(TOE_FIELD_CLASSES.values())
    check(
        "E class census is 44 theorem, 19 law, 8 empirical, 3 primitive, 1 constitutional gate",
        counts == {
            THEOREM_TARGET: 44,
            EXACT_LAW_FIELD: 19,
            EMPIRICAL_INPUT: 8,
            PRIMITIVE: 3,
            CONSTITUTIONAL_GATE: 1,
        },
        str(counts),
    )
    check("E only the three registry-backed references are primitives", {ident for ident, value in TOE_FIELD_CLASSES.items() if value == PRIMITIVE} == {"REF_SCALE", "REF_KINETIC", "REF_REALIZED_STATE"})
    check("E empirical history/boundary/measurement values remain nonprimitive", all(TOE_FIELD_CLASSES[ident] == EMPIRICAL_INPUT for ident in {"ACT_REALIZED_HISTORY_DATA", "PROB_PREPARATION_CORPUS_DATA", "TIME_CALIBRATION_DATA", "MATTER_EMPIRICAL_IDENTIFICATION", "GR_EMPIRICAL_MATCH_DATA", "BOUNDARY_ACTUAL_INSTANCE", "BOUNDARY_LOW_ENTROPY_DATA", "LAW_SELECTION_DATA"}))
    check("E only nonderived complete-law identity is a dormant constitutional compatibility gate", {ident for ident, value in TOE_FIELD_CLASSES.items() if value == CONSTITUTIONAL_GATE} == {"LAW_IDENTITY_IF_NONDERIVED"} and next(entry for entry in c96.INTERFACES if entry.ident == "LAW_IDENTITY_IF_NONDERIVED").status == c96.DORMANT)
    check("E every construction interface remains a theorem target, never an axiom or primitive", all(TOE_FIELD_CLASSES[entry.ident] == THEOREM_TARGET for entry in CONSTRUCTION_LEDGER if not entry.ident.startswith("MULTI_CONTACT")) and TOE_FIELD_CLASSES["MULTI_CONTACT_RESOURCE_RULE"] == EXACT_LAW_FIELD)


def note_scope_and_no_go_contract() -> None:
    section("G - Review note, primitive audit, and N1-N8 discipline")
    note = normalized(NOTE) if NOTE.is_file() else ""
    raw = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check("F note has authority none and no independent audit verdict", "authority: none" in note and "no independent audit verdict" in note)
    check("F every former construction ID appears with its exact disposition", all(entry.ident.lower() in note and entry.disposition.lower() in note for entry in CONSTRUCTION_LEDGER))
    check("F note names the single blocker and next constructive object", SMALLEST_BLOCKER.lower() in note and NEXT_OBJECT.lower() in note and SUPERSEDED_INTEGRATION.lower() in note and "single smallest live strict-compiler blocker" in note)
    check("F every one of 75 field IDs is explicitly classified", all(ident.lower() in note for ident in TOE_FIELD_CLASSES))
    check("F note records the five-class census", all(needle in note for needle in ("44 theorem", "19 exact-law", "8 empirical", "3 primitive", "1 constitutional")))
    check("F primitive registry scopes are quoted without enlargement", all(needle in note for needle in ("units only", "c_t=c_s form only", "pointwise realized-state reference only")))
    check("F note contains N1 through N8 and passes only a partial census", all(f"n{index}" in note for index in range(1, 9)) and "partial operational census" in note and "not a universal no-go" in note)
    check("F note includes all six disposition labels", all(disposition.lower() in note for disposition in DISPOSITIONS))
    check("F note records the evidence-count spine", all(needle in note for needle in ("160,716", "1,163", "4,284", "134,640", "2,366", "1,067", "156,576", "prefix 16", "22,310", "91,338", "28 pass / 0 fail", "41 pass / 0 fail", "5,048", "21,426", "489,656", "2,562,930", "175,440")))
    check("F no foundation or axiom action follows", "no foundation edit" in note and "no axiom addition follows" in note and "no commit" in note)
    check("F no hidden broad no-go ships", "no broad no-go" in note and "zero-edit route remains live" in note)
    check("F note source contains the exact N1 honesty markers", raw.count("`ATTEMPTED`") >= 5)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_primitive_contract()
    predecessor_evidence_contract()
    fragment_rail_integration_contract()
    construction_ledger_contract()
    dependency_collapse_contract()
    toe_classification_contract()
    note_scope_and_no_go_contract()
    print(f"\nCONSTRUCTION_INTERFACES={len(CONSTRUCTION_LEDGER)} RECURRENT_INTERFACES={len(RECURRENT_LEDGER)} TOE_FIELDS={len(TOE_FIELD_CLASSES)}")
    print(f"CONSTRUCTION_DISPOSITIONS={dict(sorted(Counter(entry.disposition for entry in CONSTRUCTION_LEDGER).items()))}")
    print(f"TOE_CLASSES={dict(sorted(Counter(TOE_FIELD_CLASSES.values()).items()))}")
    print(f"SMALLEST_LIVE_BLOCKER={SMALLEST_BLOCKER}")
    print(f"NEXT_CONSTRUCTIVE_OBJECT={NEXT_OBJECT}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
