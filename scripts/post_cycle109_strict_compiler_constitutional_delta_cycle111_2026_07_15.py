#!/usr/bin/env python3
"""Cycle 111: post-Cycle-109 strict-compiler and constitutional delta.

This authority-free refresh consumes Cycle 107's strict-compiler/75-field
ledger, Cycle 109's literal status-gated handoff, and Cycle 110's
constitutional clause-deletion audit.  It verifies the executable repair of
the Cycle-105/Cycle-106 seam, updates only the construction rows changed by
that repair, and collapses the remaining compiler work into an ordered chain
without counting an all-bit stream, its reusable harness, and successor
allocation as three simultaneous first blockers.

The only clause-deletion rows replayed are the chronology clauses whose
reading changes under Cycle 109: generic formation-event prose, read-caused
formation, later-read locking, and a two-independent-witness trigger.  The
75-field TOE census, approved primitive scopes, and dormant L* identity gate
remain inherited exactly.

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass, replace
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
sys.path.insert(0, str(SCRIPTS))

import post_cycle105_constitutional_minimality_smuggle_audit_cycle110_2026_07_15 as c110  # noqa: E402
import status_gated_typed_payload_handoff_cycle109_2026_07_15 as c109  # noqa: E402
import strict_compiler_toe_ledger_cycle107_2026_07_15 as c107  # noqa: E402


NOTE = REVIEW / "POST_CYCLE109_STRICT_COMPILER_CONSTITUTIONAL_DELTA_CYCLE111_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle105": REVIEW / "READ_STATUS_TO_GENERATED_RAIL_SPINE_CYCLE105_NOTE_2026-07-15.md",
    "cycle106": REVIEW / "FIRST_SELF_GROWN_SELECTOR_PAYLOAD_BIT0_CYCLE106_NOTE_2026-07-15.md",
    "cycle107_note": REVIEW / "STRICT_COMPILER_TOE_LEDGER_CYCLE107_NOTE_2026-07-15.md",
    "cycle107_runner": SCRIPTS / "strict_compiler_toe_ledger_cycle107_2026_07_15.py",
    "cycle109_note": REVIEW / "STATUS_GATED_TYPED_PAYLOAD_HANDOFF_CYCLE109_NOTE_2026-07-15.md",
    "cycle109_runner": SCRIPTS / "status_gated_typed_payload_handoff_cycle109_2026_07_15.py",
    "cycle110_note": REVIEW / "POST_CYCLE105_CONSTITUTIONAL_MINIMALITY_SMUGGLE_AUDIT_CYCLE110_NOTE_2026-07-15.md",
    "cycle110_runner": SCRIPTS / "post_cycle105_constitutional_minimality_smuggle_audit_cycle110_2026_07_15.py",
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


def has_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle.lower() in text for needle in needles)


# ---------------------------------------------------------------------------
# Exact post-C109 construction refresh.
#
# Cycle 109 changes only one disposition: STEP_SELECTED_OUTPUT_BIND moves from
# a supplied-boundary conditional to a bounded repair positive.  The fixed H1
# history now physically binds one status to one directed payload.  H0 remains
# a fault injection, so neither the general bit stream nor reusable harness is
# closed.
# ---------------------------------------------------------------------------

LEDGER_UPDATES = {
    "BOOT_CAGES": {
        "evidence": ("cycle101", "cycle108", "cycle105", "cycle109"),
        "exact_credit": (
            "zero-source shell growth now includes an independent BACKSTOP/guard/reference/status branch "
            "and a status-gated directed R_B11 site"
        ),
        "residual": (
            "only H1 is lawfully generated; no complete two-valued reusable comparator/selector/writer cage exists"
        ),
    },
    "BOOT_STEADY_HANDOFF": {
        "evidence": ("cycle101", "cycle108", "cycle105", "cycle109"),
        "exact_credit": (
            "literal OUTPUT, grown TYPE, shell tip, JOINT, and grown H1 status reach one directed R_B11 payload"
        ),
        "residual": (
            "the handoff is one fixed lawful bit, not an all-bit reusable same-type harness"
        ),
    },
    "STEP_SELECTED_OUTPUT_BIND": {
        "disposition": c107.REPAIR_POSITIVE,
        "evidence": ("cycle95", "cycle97", "cycle109"),
        "exact_credit": (
            "one self-grown fixed-H1 selection status binds one directed physical R_B11 output; injected H0 rejects at the same site"
        ),
        "residual": (
            "H0 is not lawfully generated and no 48-bit/general program-reference-output association is grown"
        ),
    },
    "STEP_NEXT_CELL_ALLOCATE": {
        "evidence": ("cycle98", "cycle101", "cycle108", "cycle105", "cycle109"),
        "exact_credit": (
            "the residual split, literal status, and one directed typed payload are now physical bounded positives"
        ),
        "residual": (
            "the reusable harness, renewed payload corpus, and successor-cell allocation remain absent"
        ),
    },
    "STEP_FULL_MIXED_DOMAIN": {
        "evidence": ("cycle95", "cycle98", "cycle99", "cycle108", "cycle105", "cycle109"),
        "exact_credit": (
            "bounded unions now include the 11,320-state handoff and its 1,098,040-state 97-prefix product"
        ),
        "residual": (
            "no self-grown all-bit, all-row, late-contact, arbitrary-schedule compiler induction is closed"
        ),
    },
}


def refreshed_entry(entry: c107.ConstructionEntry) -> c107.ConstructionEntry:
    updates = LEDGER_UPDATES.get(entry.ident)
    return replace(entry, **updates) if updates else entry


CONSTRUCTION_LEDGER = tuple(refreshed_entry(entry) for entry in c107.CONSTRUCTION_LEDGER)
CLOSED_ROOTS = c107.CLOSED_ROOTS

# These are ordered project stages.  In particular, ALL_BIT_STATUS_STREAM and
# REUSABLE_HARNESS are one stage at this resolution: a reusable selector
# harness is exactly the consumer/renewal apparatus for the all-bit stream.
# Successor allocation consumes that harness and therefore is downstream, not
# another simultaneous smallest wall.
COLLAPSED_STRICT_COMPILER_CHAIN = (
    (
        "LAWFUL_ALTERNATE_H0_REFERENCE_GENERATION",
        ("BOOT_CAGES", "BOOT_STEADY_HANDOFF", "STEP_SELECTED_OUTPUT_BIND"),
    ),
    (
        "ALL_BIT_STATUS_STREAM_TO_REUSABLE_HARNESS",
        (
            "BOOT_OCCUPIED_ROUTES", "BOOT_PROGRAM_BANK", "BOOT_FRESH_RESERVATION",
            "STEP_NEIGHBOUR_STREAM", "STEP_OPEN_PACK", "STEP_SELECTOR_BANK",
            "STEP_SELECTOR_TRANSPORT",
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

CLOSED_C109_INTERFACES = (
    "C105_INTEGRATION_OPEN",
    "STATUS_GATED_LITERAL_H1_TO_DIRECTED_R_B11_OR_REJECT_HANDOFF",
)
SMALLEST_BLOCKER = "LAWFUL_ALTERNATE_H0_REFERENCE_GENERATION"
NEXT_OBJECT = "SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE"


@dataclass(frozen=True)
class ChronologyRow:
    ident: str
    disposition: str
    c109_use: str
    deletion_result: str
    exact_reason: str


CHRONOLOGY_DELTA = (
    ChronologyRow(
        "FORMATION_EVENT_RULE",
        c110.KEEP_AS_LAW,
        c110.USE_LOCAL_LAW,
        c110.DELETE_LEAVES_C105,
        "the 7,496-row bounded candidate law supplies the actual append condition",
    ),
    ChronologyRow(
        "READ_CAUSES_FORMATION",
        c110.DELETE_GENERIC,
        c110.USE_NONE,
        c110.DELETE_LEAVES_C105,
        "OUTPUT, TYPE, shell, JOINT, CAGE, guard, reference, and STATUS are already records before payload formation",
    ),
    ChronologyRow(
        "LATER_READ_CAUSES_LOCK",
        c110.DELETE_GENERIC,
        c110.USE_NONE,
        c110.DELETE_LEAVES_C105,
        "there is no pre-record payload object; the status-gated append is the payload record's first presence and lock",
    ),
    ChronologyRow(
        "TWO_INDEPENDENT_WITNESS_TRIGGER",
        c110.DELETE_GENERIC,
        c110.USE_NONE,
        c110.DELETE_LEAVES_C105,
        "JOINT and STATUS contain different roles, share literal OUTPUT ancestry, and are prerequisites rather than independent copies",
    ),
)

UNCHANGED_FROM_C110 = (
    "FORMATION_OCCURRENCE",
    "CLOCK_CAUSES_FINAL_LOCK", "COMMIT_COUNT_IS_CLOCK",
    "GLOBAL_STORAGE_COMPUTE_BUDGET", "RESOURCE_RESPONSE_FROM_RECORD_LOAD",
    "COUNT_BY_PHYSICAL_POSSIBILITY", "MIRROR_CONJUGATE_COUNTS_ONCE",
    "PHYSICAL_CONTINUATION_KERNEL", "AVAILABILITY_EQUALS_EVENT_SUPPORT",
    "CONTINUATION_COMPOSITION_CONFLUENCE", "RECORD_STATE_FUTURE_SUFFICIENCY",
    "ACTUAL_REALIZED_HISTORY", "TIME_CALIBRATION_CORPUS",
    "EXACT_COMPLETE_LAW_IDENTITY",
)


def source_and_primitive_contract() -> None:
    section("A - Sources, exact consumption boundary, and approved primitives")
    for name, path in {"cycle111_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registry still has exactly four canonical premise nodes",
        set(nodes) == {
            "minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive",
        },
        str(sorted(nodes)),
    )
    check(
        "A approved primitive paths are unchanged",
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
        "A scale reference remains units-only",
        has_all(texts["scale"], ("units conversion, not a physics axiom", "zero dimensionless content")),
    )
    check(
        "A kinetic reference remains c_t=c_s form-only",
        has_all(texts["kinetic"], ("c_t = c_s", "not a new dynamics", "not a re-axiomatization of time")),
    )
    check(
        "A realized-state reference remains pointwise-only",
        has_all(texts["realized"], ("pointwise evaluation", "no state, averaging over alternatives", "past hypothesis is a separate")),
    )
    check(
        "A current Record supplies formation occurrence and immediate presence-lock semantics",
        has_all(texts["axioms"], (
            "records form",
            "when present, a record locks exactly one admissible local possibility",
            "only records are readable",
        )),
    )
    check(
        "A Cycle107, Cycle109, and Cycle110 are the exact refresh inputs",
        has_all(texts["cycle107_note"], ("strict-compiler", "75", "typed_payload_cap_to_reusable_harness"))
        and has_all(texts["cycle109_note"], ("status-gated substitution", "7,496", "does not close the complete reusable harness"))
        and has_all(texts["cycle110_note"], ("clause-deletion", "no new generic atom is forced", "c105_integration_open")),
    )


def predecessor_exactness_contract() -> None:
    section("B - Exact Cycle107/Cycle109/Cycle110 executable surfaces")
    check(
        "B Cycle107 contains 19 construction interfaces and 75 TOE fields",
        len(c107.CONSTRUCTION_LEDGER) == 19
        and len(c107.TOE_FIELD_CLASSES) == 75,
    )
    check(
        "B Cycle107 predecessor blocker is the undirected cap-to-harness seam",
        c107.SMALLEST_BLOCKER == "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS"
        and c107.NEXT_OBJECT == "CAGED_R_B11_CAP_TO_DIRECTED_RENEWABLE_PAYLOAD_LAUNCH",
    )

    check(
        "B Cycle109 substitutes 17 retained C105 rows for the 18-row bridge",
        len(c109.c105.BRIDGE_TABLE) == 18
        and len(c109.SPINE_JOIN_TABLE) == 17
        and c109.UNARY_CAP_CANONICAL not in c109.SPINE_JOIN_TABLE
        and set(c109.SPINE_JOIN_TABLE) == set(c109.c105.BRIDGE_TABLE) - {c109.UNARY_CAP_CANONICAL}
        and len(c109.SPINE_JOIN_RAW) == 408,
    )
    check(
        "B Cycle109 adds exactly 8 canonical / 192 raw status-handoff rows",
        len(c109.HARNESS_TABLE) == 8 and len(c109.HARNESS_RAW) == 192,
    )
    check(
        "B Cycle109 exact selected union is 7,496 disjoint single-valued rows",
        len(c109.FULL_RAW) == 7_496
        and set(c109.c105.BASE_RAW).isdisjoint(c109.SPINE_JOIN_RAW)
        and set(c109.c105.BASE_RAW).isdisjoint(c109.HARNESS_RAW)
        and set(c109.SPINE_JOIN_RAW).isdisjoint(c109.HARNESS_RAW)
        and all(len(values) == 1 for values in c109.FULL_RAW.values()),
    )
    check(
        "B Cycle109 local graph is exactly 11,320 states / 54,066 edges / one 46-write terminal",
        c109.POSITIVE.states == 11_320
        and c109.POSITIVE.edges == 54_066
        and c109.POSITIVE.terminals == 1
        and c109.POSITIVE.terminal_sizes == (46,)
        and not c109.POSITIVE.bad,
        str(c109.POSITIVE),
    )
    product_states = c109.POSITIVE.states * (c109.c105.RAIL_HORIZON + 1)
    product_edges = (
        c109.POSITIVE.edges * (c109.c105.RAIL_HORIZON + 1)
        + c109.POSITIVE.states * c109.c105.RAIL_HORIZON
    )
    check(
        "B Cycle109 97-prefix product is exactly 1,098,040 states / 6,331,122 edges",
        product_states == 1_098_040 and product_edges == 6_331_122,
        f"states={product_states} edges={product_edges}",
    )
    check(
        "B Cycle109 proper-cubic raw covariance census is 179,904",
        len(c109.FULL_RAW) * 24 == 179_904,
    )

    class_counts = Counter(row.classification for row in c110.ALL_ROWS)
    check(
        "B Cycle110 retains 21 classified rows with zero forced new atoms",
        len(c110.ALL_ROWS) == 21
        and class_counts == {
            c110.CANDIDATE_LAW: 10,
            c110.THEOREM: 4,
            c110.EMPIRICAL: 2,
            c110.PRIMITIVE: 3,
            c110.CONSTITUTIONAL: 2,
        }
        and not any(row.forced_new for row in c110.GENERIC_ATOMS),
        str(class_counts),
    )


def c105_c106_repair_contract() -> None:
    section("C - Literal C105_INTEGRATION_OPEN repair and directed bit-0 handoff")
    c106 = c109.c106
    c105 = c109.c105
    c106_note = normalized(SOURCES["cycle106"])
    c109_note = normalized(SOURCES["cycle109_note"])

    check(
        "C predecessor literally records C105_INTEGRATION_OPEN",
        "c105_integration_open" in c106_note
        and "does not advance after cycle 105" in c106_note,
    )
    check(
        "C C109 keeps C105 AUX/BTG shell contents rather than conflicting C106 T_H2/T_H3 arms",
        c109.GROWN_OUTPUTS[c106.TYPE_ARM] == "AUX"
        and c109.GROWN_OUTPUTS[c106.JOIN_GUARD] == "BTG"
        and c106.CORRECT_NEW[:2] == ((c106.TYPE_ARM, "T_H2"), (c106.JOIN_GUARD, "T_H3")),
    )
    check(
        "C C109 retains the shared JOINT and replaces the occupied cap/reject rule",
        c106.JOIN == c105.JOIN
        and c109.GROWN_OUTPUTS[c106.JOIN] == c105.JOIN_OUTPUT == "JOINT"
        and c109.DIRECTED_PAYLOAD == c106.REJECT == c105.PAYLOAD_SITES[0]
        and c109.UNARY_CAP_CANONICAL not in c109.SPINE_JOIN_TABLE,
    )

    terminal = c109.positive_terminal_records()
    before_payload = dict(terminal)
    before_payload.pop(c109.DIRECTED_PAYLOAD)
    payload_local = c105.c101.c100.c53.local_signature(before_payload, c109.DIRECTED_PAYLOAD)
    check(
        "C correct payload site sees exactly STATUS=H1 west plus JOINT below",
        dict(payload_local) == {(-1, 0, 0): c109.H1, (0, 0, -1): c105.JOIN_OUTPUT}
        and c109.FULL_RAW[payload_local] == frozenset(("R_B11",)),
        str(payload_local),
    )
    check(
        "C correct branch writes one directed R_B11 and no other symmetric cap image",
        terminal[c109.DIRECTED_PAYLOAD] == "R_B11"
        and all(site not in terminal for site in c105.PAYLOAD_SITES[1:]),
    )

    rail_zero = c109.RAIL_ZERO
    fault_fronts = (
        {**rail_zero, c106.STATUS: frozenset((c109.H0,))},
        {**rail_zero, c109.DIRECTED_PAYLOAD: frozenset(("AUX",))},
        {**rail_zero, c109.LAUNCH: frozenset((c109.LAUNCH_OUTPUT,))},
        rail_zero,
    )
    check(
        "C injected H0 traverses STATUS=H0 -> AUX -> A_0_0 at the same decision site",
        all(c109.enabled(c109.fault_records(stage)) == expected for stage, expected in enumerate(fault_fronts)),
    )
    check(
        "C structural substitution closes both named seams at bounded bit-0 resolution",
        CLOSED_C109_INTERFACES == (
            "C105_INTEGRATION_OPEN",
            "STATUS_GATED_LITERAL_H1_TO_DIRECTED_R_B11_OR_REJECT_HANDOFF",
        )
        and "status_gated_literal_h1_to_directed_r_b11_or_reject_handoff" in c109_note,
    )


def construction_refresh_contract() -> None:
    section("D - Post-C109 construction dispositions")
    original = {entry.ident: entry for entry in c107.CONSTRUCTION_LEDGER}
    refreshed = {entry.ident: entry for entry in CONSTRUCTION_LEDGER}
    check(
        "D all 19 Cycle107 construction identities are preserved exactly once",
        len(refreshed) == len(CONSTRUCTION_LEDGER) == 19 and set(refreshed) == set(original),
    )
    changed = {
        ident for ident in refreshed
        if refreshed[ident] != original[ident]
    }
    check(
        "D only five evidence/residual rows change under C109",
        changed == {
            "BOOT_CAGES", "BOOT_STEADY_HANDOFF", "STEP_SELECTED_OUTPUT_BIND",
            "STEP_NEXT_CELL_ALLOCATE", "STEP_FULL_MIXED_DOMAIN",
        },
        str(sorted(changed)),
    )
    disposition_changes = {
        ident for ident in refreshed
        if refreshed[ident].disposition != original[ident].disposition
    }
    check(
        "D only STEP_SELECTED_OUTPUT_BIND changes disposition",
        disposition_changes == {"STEP_SELECTED_OUTPUT_BIND"}
        and original["STEP_SELECTED_OUTPUT_BIND"].disposition == c107.SUPPLIED_BOUNDARY
        and refreshed["STEP_SELECTED_OUTPUT_BIND"].disposition == c107.REPAIR_POSITIVE,
        str(disposition_changes),
    )
    counts = Counter(entry.disposition for entry in CONSTRUCTION_LEDGER)
    check(
        "D refreshed disposition census is exact",
        counts == {
            c107.CLOSED: 1,
            c107.ROLE_CLOSED: 1,
            c107.REPAIR_POSITIVE: 5,
            c107.CONSTRUCTION_GRADE: 4,
            c107.SUPPLIED_BOUNDARY: 4,
            c107.LIVE: 4,
        },
        str(counts),
    )
    check(
        "D roots and live mixed/multi fields remain unchanged",
        tuple(entry.ident for entry in CONSTRUCTION_LEDGER if entry.disposition in {c107.CLOSED, c107.ROLE_CLOSED}) == CLOSED_ROOTS
        and {entry.ident for entry in CONSTRUCTION_LEDGER if entry.disposition == c107.LIVE}
        == {"STEP_FULL_MIXED_DOMAIN", "MULTI_REACHABLE_NUCLEATION", "MULTI_CONTACT_RESOURCE_RULE", "MULTI_CONFLUENCE_RECORD"},
    )
    check(
        "D every changed row cites Cycle109 and states a surviving residual",
        all("cycle109" in refreshed[ident].evidence and refreshed[ident].residual for ident in changed),
    )


def dependency_collapse_contract() -> None:
    section("E - Single smallest blocker and ordered downstream construction")
    covered = {
        ident
        for _stage, identities in COLLAPSED_STRICT_COMPILER_CHAIN
        for ident in identities
    }
    all_ids = {entry.ident for entry in CONSTRUCTION_LEDGER}
    check(
        "E collapsed chain consumes every non-root construction interface once",
        len(covered) == 17 and covered == all_ids - set(CLOSED_ROOTS),
    )
    check(
        "E stage names are unique and the first stage is the exact smallest blocker",
        len({stage for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN}) == 5
        and COLLAPSED_STRICT_COMPILER_CHAIN[0][0] == SMALLEST_BLOCKER,
    )
    check(
        "E next object is one second valid literal history producing lawful H0",
        SMALLEST_BLOCKER == "LAWFUL_ALTERNATE_H0_REFERENCE_GENERATION"
        and NEXT_OBJECT == "SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE",
    )
    check(
        "E all-bit stream and reusable harness are one stage, not two counted walls",
        [stage for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN].count("ALL_BIT_STATUS_STREAM_TO_REUSABLE_HARNESS") == 1
        and not any(stage in {"ALL_BIT_STATUS_STREAM", "REUSABLE_HARNESS"} for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN),
    )
    check(
        "E successor allocation is downstream of the combined stream/harness stage",
        [stage for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN].index("SUCCESSOR_LITERAL_REUSE_AND_ALLOCATION")
        > [stage for stage, _ids in COLLAPSED_STRICT_COMPILER_CHAIN].index("ALL_BIT_STATUS_STREAM_TO_REUSABLE_HARNESS"),
    )

    # Preserve the inherited 75-field dependency DAG exactly.
    by_id = {entry.ident: entry for entry in c107.c96.INTERFACES}
    indegree = {ident: 0 for ident in by_id}
    outgoing: dict[str, list[str]] = defaultdict(list)
    for entry in c107.c96.INTERFACES:
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
    check("E inherited 75-field dependency graph remains acyclic", len(order) == len(by_id) == 75)


def chronology_clause_deletion_contract() -> None:
    section("F - C109 chronology-only clause deletion")
    c110_rows = {row.ident: row for row in c110.GENERIC_ATOMS}
    check(
        "F replay is limited to the four chronology clauses changed by C109",
        {row.ident for row in CHRONOLOGY_DELTA} == {
            "FORMATION_EVENT_RULE", "READ_CAUSES_FORMATION",
            "LATER_READ_CAUSES_LOCK", "TWO_INDEPENDENT_WITNESS_TRIGGER",
        },
    )
    check(
        "F every chronology disposition agrees exactly with Cycle110",
        all(
            row.disposition == c110_rows[row.ident].disposition
            and row.c109_use == c110_rows[row.ident].c105_use
            and row.deletion_result == c110_rows[row.ident].deletion_result
            for row in CHRONOLOGY_DELTA
        ),
    )

    c105 = c109.c105
    c106 = c109.c106
    join_records = dict(c105.c101.TERMINAL)
    join_records.update(c105.c101.FRAGMENT_OUTPUTS)
    join_records[c105.NATURAL_TYPE] = c105.NATURAL_TYPE_OUTPUT
    for group, output in zip(c105.SPINE_GROUPS, c105.SPINE_OUTPUTS):
        join_records.update({site: output for site in group})
    join_parents = {
        site: join_records[site]
        for site in c105.neighbors(c105.JOIN)
        if site in join_records
    }
    check(
        "F JOINT is formed from already-locked OUTPUT, TYPE, and shell-tip records",
        join_parents == {
            c105.c101.OUTPUT: c105.c101.H1,
            c105.NATURAL_TYPE: c105.NATURAL_TYPE_OUTPUT,
            c105.PRIMARY_SPINE[-1]: c105.SPINE_OUTPUTS[-1],
        },
        str(join_parents),
    )

    status_records = c105.positive_terminal_records()
    for site in c105.PAYLOAD_SITES:
        status_records.pop(site)
    for site, output in c106.CORRECT_NEW[3:6]:
        status_records[site] = output
    status_local = c105.c101.c100.c53.local_signature(status_records, c106.STATUS)
    check(
        "F STATUS reads literal OUTPUT plus CAGE and REFERENCE records",
        dict(status_local) == {
            (-1, 0, 0): c109.H1,
            (0, -1, 0): "BACKSTOP",
            (0, 0, -1): c109.H1,
        }
        and c109.FULL_RAW[status_local] == frozenset((c109.H1,)),
        str(status_local),
    )
    check(
        "F JOINT and STATUS are not two independent matching witnesses",
        join_records[c105.c101.OUTPUT] == c109.H1
        and status_records[c105.c101.OUTPUT] == c109.H1
        and c105.JOIN_OUTPUT != c109.H1,
    )
    check(
        "F reading does not cause prior records to lock and no later payload-lock step exists",
        all(
            c109.DIRECTED_PAYLOAD not in c109.records_at(state)
            for state in (0,)
        )
        and c109.positive_terminal_records()[c109.DIRECTED_PAYLOAD] == "R_B11",
    )
    check(
        "F formation occurrence stays current while the event rule stays candidate-law owned",
        c110_rows["FORMATION_OCCURRENCE"].disposition == c110.CURRENT
        and next(row for row in CHRONOLOGY_DELTA if row.ident == "FORMATION_EVENT_RULE").c109_use == c110.USE_LOCAL_LAW,
    )
    check(
        "F clock, storage, counting, continuation, actuality, and L* rows are inherited rather than rerun",
        set(UNCHANGED_FROM_C110) == set(c110_rows) - {row.ident for row in CHRONOLOGY_DELTA},
    )


def toe_census_and_lstar_contract() -> None:
    section("G - Type-correct 75-field TOE census and dormant L* gate")
    counts = Counter(c107.TOE_FIELD_CLASSES.values())
    check(
        "G exact 75-field census remains 44 theorem / 19 law / 8 empirical / 3 primitive / 1 constitutional",
        len(c107.TOE_FIELD_CLASSES) == 75
        and counts == {
            c107.THEOREM_TARGET: 44,
            c107.EXACT_LAW_FIELD: 19,
            c107.EMPIRICAL_INPUT: 8,
            c107.PRIMITIVE: 3,
            c107.CONSTITUTIONAL_GATE: 1,
        },
        str(counts),
    )
    check(
        "G only the three registry-backed references are primitives",
        {ident for ident, value in c107.TOE_FIELD_CLASSES.items() if value == c107.PRIMITIVE}
        == {"REF_SCALE", "REF_KINETIC", "REF_REALIZED_STATE"},
    )
    check(
        "G empirical realized history and clock calibration stay empirical",
        c107.TOE_FIELD_CLASSES["ACT_REALIZED_HISTORY_DATA"] == c107.EMPIRICAL_INPUT
        and c107.TOE_FIELD_CLASSES["TIME_CALIBRATION_DATA"] == c107.EMPIRICAL_INPUT,
    )
    identity = next(entry for entry in c107.c96.INTERFACES if entry.ident == "LAW_IDENTITY_IF_NONDERIVED")
    complete = next(entry for entry in c107.c96.INTERFACES if entry.ident == "LAW_COMPLETE_REFERENT")
    check(
        "G LAW_IDENTITY_IF_NONDERIVED is still the sole constitutional compatibility gate",
        {ident for ident, value in c107.TOE_FIELD_CLASSES.items() if value == c107.CONSTITUTIONAL_GATE}
        == {"LAW_IDENTITY_IF_NONDERIVED"},
    )
    check(
        "G L* identity remains dormant behind complete referent, uniqueness, and selection",
        identity.status == c107.c96.DORMANT
        and set(identity.dependencies) == {
            "LAW_COMPLETE_REFERENT", "LAW_UNIQUENESS_OR_EQUIVALENCE", "LAW_SELECTION_DATA",
        }
        and complete.status == c107.c96.OPEN,
    )
    check(
        "G bounded C109 cannot instantiate a stable complete L*",
        len(c109.FULL_RAW) == 7_496
        and c109.c105.RAIL_HORIZON == 96
        and c107.TOE_FIELD_CLASSES["LAW_COMPLETE_REFERENT"] == c107.EXACT_LAW_FIELD,
    )
    check(
        "G exact-law identity is absent from the primitive registry",
        "exact_complete_law_identity" not in json.loads(SOURCES["registry"].read_text(encoding="utf-8"))["nodes"],
    )


def note_and_no_go_contract() -> None:
    section("H - Cycle111 note, scope, and N1-N8 discipline")
    note = normalized(NOTE) if NOTE.is_file() else ""
    raw = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check(
        "H note has authority none and runner+note-only scope",
        has_all(note, (
            "authority: none", "runner + review note only", "no predecessor edit",
            "no foundation edit", "no registry edit", "no queue edit", "no commit",
        )),
    )
    check(
        "H note records executable C105 seam repair without overstating a quote",
        has_all(note, (
            "c105_integration_open", "executable composition inference",
            "status_gated_literal_h1_to_directed_r_b11_or_reject_handoff",
        )),
    )
    check(
        "H note names the unique blocker and exact next object",
        SMALLEST_BLOCKER.lower() in note
        and NEXT_OBJECT.lower() in note
        and "single smallest construction blocker" in note,
    )
    check(
        "H note does not double-count stream, harness, and successor allocation",
        has_all(note, (
            "all_bit_status_stream_to_reusable_harness",
            "one downstream stage", "successor_literal_reuse_and_allocation",
            "ordered after the reusable harness",
        )),
    )
    check(
        "H note reports the refreshed construction census",
        has_all(note, (
            "1 closed", "1 role_closed", "5 repair_positive",
            "4 construction_grade_only", "4 supplied_boundary_conditional", "4 live",
        )),
    )
    check(
        "H note limits clause deletion to chronology and excludes witness/read-lock semantics",
        has_all(note, (
            "chronology-only clause deletion", "one directed payload",
            "not two independent witnesses", "reading does not cause their lock",
        )),
    )
    check(
        "H note preserves the 75-field census and dormant L* gate",
        has_all(note, (
            "44 theorem", "19 exact-law", "8 empirical", "3 primitive",
            "1 constitutional", "law_identity_if_nonderived", "dormant", "no stable l",
        )),
    )
    check(
        "H primitive scopes are quoted without enlargement",
        has_all(note, (
            "units only", "c_t=c_s form only", "pointwise realized-state reference only",
        )),
    )
    check(
        "H note carries complete N1-N8 discipline and at least five attempted routes",
        all(f"n{index} —" in note for index in range(1, 9))
        and raw.count("`ATTEMPTED`") >= 5,
    )
    check(
        "H scoped negative remains partial and explicitly not universal",
        has_all(note, (
            "partial-narrowing-with-live-constructive-routes",
            "not a universal no-go", "strongest hostile steelman",
        )),
    )
    check(
        "H note records Cycle112 as absent and unconsumed at refresh time",
        has_all(note, ("cycle 112", "absent", "not consumed")),
    )
    scientific_body = note.split("## n1–n8 no-go-discipline gate", 1)[0]
    hidden = (
        "we assume", "as is standard", "the framework provides", "obviously",
        "naturally follows", "standard qft",
    )
    check(
        "H scientific body contains no hidden-premise phrase",
        not any(phrase in scientific_body for phrase in hidden),
        str([phrase for phrase in hidden if phrase in scientific_body]),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_primitive_contract()
    predecessor_exactness_contract()
    c105_c106_repair_contract()
    construction_refresh_contract()
    dependency_collapse_contract()
    chronology_clause_deletion_contract()
    toe_census_and_lstar_contract()
    note_and_no_go_contract()
    print(f"\nCONSTRUCTION_INTERFACES={len(CONSTRUCTION_LEDGER)} TOE_FIELDS={len(c107.TOE_FIELD_CLASSES)}")
    print(f"CONSTRUCTION_DISPOSITIONS={dict(sorted(Counter(entry.disposition for entry in CONSTRUCTION_LEDGER).items()))}")
    print(f"TOE_CLASSES={dict(sorted(Counter(c107.TOE_FIELD_CLASSES.values()).items()))}")
    print("CLOSED_C109_INTERFACES=" + ",".join(CLOSED_C109_INTERFACES))
    print(f"SMALLEST_LIVE_BLOCKER={SMALLEST_BLOCKER}")
    print(f"NEXT_CONSTRUCTIVE_OBJECT={NEXT_OBJECT}")
    print("CYCLE112=ABSENT_NOT_CONSUMED_AT_REFRESH")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
