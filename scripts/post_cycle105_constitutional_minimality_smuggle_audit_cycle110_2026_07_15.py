#!/usr/bin/env python3
"""Cycle 110: post-Cycle-105 constitutional minimality and smuggle audit.

This authority-free runner consumes the exact Cycle-83/96/107/108/105
surfaces, replays the current foundation/primitive boundary, and tests every
previously proposed generic formation/Record/continuation atom by dependency
deletion.  It distinguishes a physical interpretation dependency from a
numerical runner dependency: the current ``Records form.`` sentence supplies
the occurrence slot, while Cycle 105's formation readiness and append map are
owned by its bounded candidate-law rows.

Cycle 106 is inspected only at the literal Cycle-105 seam.  Its independent
Cycle-108 union is not consumed as downstream evidence because the combined
site/content and schedule interface has not landed.

No axiom, primitive, registry, queue, policy, audit, predecessor, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
sys.path.insert(0, str(SCRIPTS))

import constructive_constitutional_delta_audit_cycle83_2026_07_14 as c83  # noqa: E402
import fragment_safe_role_remap_type_integration_cycle108_2026_07_15 as c108  # noqa: E402
import post_cycle94_operational_completeness_audit_cycle96_2026_07_15 as c96  # noqa: E402
import read_status_to_generated_rail_spine_cycle105_2026_07_15 as c105  # noqa: E402
import strict_compiler_toe_ledger_cycle107_2026_07_15 as c107  # noqa: E402


NOTE = REVIEW / "POST_CYCLE105_CONSTITUTIONAL_MINIMALITY_SMUGGLE_AUDIT_CYCLE110_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle31": REVIEW / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md",
    "cycle83": REVIEW / "CONSTRUCTIVE_CONSTITUTIONAL_DELTA_AUDIT_CYCLE83_NOTE_2026-07-14.md",
    "cycle96": REVIEW / "POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md",
    "cycle107": REVIEW / "STRICT_COMPILER_TOE_LEDGER_CYCLE107_NOTE_2026-07-15.md",
    "cycle108": REVIEW / "FRAGMENT_SAFE_ROLE_REMAP_TYPE_INTEGRATION_CYCLE108_NOTE_2026-07-15.md",
    "cycle105": REVIEW / "READ_STATUS_TO_GENERATED_RAIL_SPINE_CYCLE105_NOTE_2026-07-15.md",
    "cycle106_note": REVIEW / "FIRST_SELF_GROWN_SELECTOR_PAYLOAD_BIT0_CYCLE106_NOTE_2026-07-15.md",
    "cycle106_runner": SCRIPTS / "first_self_grown_selector_payload_bit0_cycle106_2026_07_15.py",
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


# The five requested primary classifications.  Constitutional covers both an
# already-supplied axiom atom and a dormant compatibility/identity gate; the
# disposition below prevents those two cases from being conflated.
CANDIDATE_LAW = "CANDIDATE_LAW_FIELD"
THEOREM = "THEOREM_TARGET"
EMPIRICAL = "EMPIRICAL_INPUT"
PRIMITIVE = "APPROVED_PRIMITIVE"
CONSTITUTIONAL = "CONSTITUTIONAL"
CLASSES = {CANDIDATE_LAW, THEOREM, EMPIRICAL, PRIMITIVE, CONSTITUTIONAL}

CURRENT = "CURRENT_SUPPLIED_ATOM"
DELETE_GENERIC = "DELETE_FROM_GENERIC_AXIOM"
KEEP_AS_LAW = "KEEP_IN_EXACT_LAW"
KEEP_AS_THEOREM = "KEEP_AS_THEOREM_TARGET"
KEEP_AS_DATA = "KEEP_AS_EMPIRICAL_INPUT"
KEEP_PRIMITIVE = "KEEP_APPROVED_PRIMITIVE"
DORMANT = "DORMANT_UNTIL_STABLE_NONDERIVED_LSTAR"

USE_CURRENT = "CURRENT_FOUNDATION_USE"
USE_LOCAL_LAW = "BOUNDED_CANDIDATE_LAW_USE"
USE_BOUNDED_THEOREM = "BOUNDED_THEOREM_RESULT"
USE_NONE = "NO_CYCLE105_DEPENDENCY"

DELETE_BREAKS_SEMANTIC = "DELETION_BREAKS_PHYSICAL_RECORD_OCCURRENCE_TYPE"
DELETE_LEAVES_C105 = "DELETION_LEAVES_CYCLE105_CLAIM_CLOSED"
DELETE_NOT_INSTALLED = "CLAUSE_NOT_INSTALLED_GATE_REMAINS_DORMANT"
DELETE_NA = "NOT_A_PROPOSED_CLAUSE"


@dataclass(frozen=True)
class Atom:
    ident: str
    family: str
    test_clause: str
    classification: str
    disposition: str
    c105_use: str
    deletion_result: str
    forced_new: bool
    exact_reason: str


def atom(
    ident: str,
    family: str,
    test_clause: str,
    classification: str,
    disposition: str,
    c105_use: str,
    deletion_result: str,
    exact_reason: str,
    forced_new: bool = False,
) -> Atom:
    return Atom(
        ident, family, test_clause, classification, disposition, c105_use,
        deletion_result, forced_new, exact_reason,
    )


GENERIC_ATOMS = (
    atom(
        "FORMATION_OCCURRENCE", "formation", "Records form.",
        CONSTITUTIONAL, CURRENT, USE_CURRENT, DELETE_BREAKS_SEMANTIC,
        "already in Record; it types occurrence but selects no site, outcome, weight, schedule, or rate",
    ),
    atom(
        "FORMATION_EVENT_RULE", "formation",
        "The rule determines which record forms and when.",
        CANDIDATE_LAW, KEEP_AS_LAW, USE_LOCAL_LAW, DELETE_LEAVES_C105,
        "Cycle 105 gets readiness from its 7,310-row bounded table, not generic Record prose",
    ),
    atom(
        "READ_CAUSES_FORMATION", "read_lock", "A record forms only when read.",
        CANDIDATE_LAW, DELETE_GENERIC, USE_NONE, DELETE_LEAVES_C105,
        "Cycle 105's OUTPUT and TYPE are already locked parents before JOINT; reading gates a later append",
    ),
    atom(
        "LATER_READ_CAUSES_LOCK", "read_lock",
        "An item forms and a later read locks it as a record.",
        CANDIDATE_LAW, DELETE_GENERIC, USE_NONE, DELETE_LEAVES_C105,
        "would require an exact pre-record type or selected-law Record compatibility repair",
    ),
    atom(
        "TWO_INDEPENDENT_WITNESS_TRIGGER", "two_witness",
        "A record forms exactly when two independent witnesses agree.",
        CANDIDATE_LAW, DELETE_GENERIC, USE_NONE, DELETE_LEAVES_C105,
        "the three JOINT parents are causal prerequisites and the three cap images form after JOINT",
    ),
    atom(
        "CLOCK_CAUSES_FINAL_LOCK", "clock",
        "A clock event supplies the final record lock.",
        CANDIDATE_LAW, DELETE_GENERIC, USE_NONE, DELETE_LEAVES_C105,
        "Cycle 105 exhausts asynchronous schedules without a clock record or metric rate",
    ),
    atom(
        "COMMIT_COUNT_IS_CLOCK", "clock",
        "Local time is a record-readable count of completed commit events.",
        THEOREM, KEEP_AS_THEOREM, USE_NONE, DELETE_LEAVES_C105,
        "requires a selected commit-event decoder and schedule-invariant count theorem downstream",
    ),
    atom(
        "GLOBAL_STORAGE_COMPUTE_BUDGET", "storage",
        "The universe has a finite storage or compute budget.",
        CANDIDATE_LAW, DELETE_GENERIC, USE_NONE, DELETE_LEAVES_C105,
        "no invariant, capacity value, renewal/export law, or observable coupling occurs in Cycle 105",
    ),
    atom(
        "RESOURCE_RESPONSE_FROM_RECORD_LOAD", "storage",
        "Record growth consumes a conserved capacity that changes physical response.",
        CANDIDATE_LAW, KEEP_AS_LAW, USE_NONE, DELETE_LEAVES_C105,
        "resource current, coefficients, renewal, and gravity response remain exact-law fields",
    ),
    atom(
        "COUNT_BY_PHYSICAL_POSSIBILITY", "counting",
        "Records are counted by physical possibility, never by presentation.",
        CANDIDATE_LAW, KEEP_AS_LAW, USE_NONE, DELETE_LEAVES_C105,
        "Cycle 105 retains all three proper-cubic cap images and defines no event/effect quotient",
    ),
    atom(
        "MIRROR_CONJUGATE_COUNTS_ONCE", "counting",
        "A mirrored or conjugate presentation counts once.",
        CANDIDATE_LAW, KEEP_AS_LAW, USE_NONE, DELETE_LEAVES_C105,
        "proper rotations do not select mirror/conjugate physical equivalence",
    ),
    atom(
        "PHYSICAL_CONTINUATION_KERNEL", "continuation_separation",
        "The availability rule determines the law-admissible continuations.",
        CANDIDATE_LAW, KEEP_AS_LAW, USE_LOCAL_LAW, DELETE_LEAVES_C105,
        "Cycle 105 supplies a bounded append kernel explicitly; current Admissibility remains availability-only",
    ),
    atom(
        "AVAILABILITY_EQUALS_EVENT_SUPPORT", "continuation_separation",
        "Every available possibility occurs in some physical continuation.",
        THEOREM, KEEP_AS_THEOREM, USE_NONE, DELETE_LEAVES_C105,
        "C96 makes availability projection a theorem of the exact event kernel; Cycle 105 tests only its finite rows",
    ),
    atom(
        "CONTINUATION_COMPOSITION_CONFLUENCE", "continuation_separation",
        "Lawful continuations compose transitively and schedule-confluently.",
        THEOREM, KEEP_AS_THEOREM, USE_BOUNDED_THEOREM, DELETE_LEAVES_C105,
        "Cycle 105 proves one 5,048-state local instance, not a universal continuation axiom",
    ),
    atom(
        "RECORD_STATE_FUTURE_SUFFICIENCY", "continuation_separation",
        "The complete record configuration alone determines every future record law.",
        THEOREM, KEEP_AS_THEOREM, USE_BOUNDED_THEOREM, DELETE_LEAVES_C105,
        "bounded local signatures suffice in Cycle 105; general failure would trigger only the Qualification compatibility gate",
    ),
    atom(
        "ACTUAL_REALIZED_HISTORY", "actuality",
        "This law-admissible history is the realized history.",
        EMPIRICAL, KEEP_AS_DATA, USE_NONE, DELETE_LEAVES_C105,
        "the realized-state primitive supplies only a pointwise slot; the history value remains contingent data",
    ),
    atom(
        "TIME_CALIBRATION_CORPUS", "clock",
        "These physical clock comparisons calibrate the metric rate.",
        EMPIRICAL, KEEP_AS_DATA, USE_NONE, DELETE_LEAVES_C105,
        "Cycle 105 provides no clock-comparison corpus or metric calibration",
    ),
    atom(
        "EXACT_COMPLETE_LAW_IDENTITY", "complete_law_identity",
        "The fixed nearest-neighbor admissibility rule is the exact physical law L*.",
        CONSTITUTIONAL, DORMANT, USE_NONE, DELETE_NOT_INSTALLED,
        "C105 is a bounded 7,310-row construction, not a complete stable L* or uniqueness/selection theorem",
    ),
)


REFERENCE_ROWS = (
    atom(
        "REF_SCALE", "reference", "a^-1=M_Pl units reference",
        PRIMITIVE, KEEP_PRIMITIVE, USE_NONE, DELETE_NA,
        "approved units conversion only; zero dimensionless physics",
    ),
    atom(
        "REF_KINETIC", "reference", "c_t=c_s kinetic-form reference",
        PRIMITIVE, KEEP_PRIMITIVE, USE_NONE, DELETE_NA,
        "approved structural kinetic form only; no dynamics, rate, or clock law",
    ),
    atom(
        "REF_REALIZED_STATE", "reference", "pointwise realized-state reference",
        PRIMITIVE, KEEP_PRIMITIVE, USE_NONE, DELETE_NA,
        "approved pointwise slot only; no history, selector, measure, or weighting",
    ),
)

ALL_ROWS = GENERIC_ATOMS + REFERENCE_ROWS


# Physical-claim dependencies are deliberately separated from the executable
# counter certificate.  Removing occurrence leaves the Python counters intact
# but removes the current axiom-level type under which appends are physical
# records.  None of the unlanded proposal nodes is in either closure.
DEPENDENCIES = {
    "C105_EXECUTABLE_CERTIFICATE": {
        "C101_TERMINAL_SOURCE", "C108_INTEGRATED_ROWS", "C105_BRIDGE_ROWS",
        "LATTICE_NN_COVARIANCE", "FIXED_LOCAL_AVAILABILITY_SLOT",
    },
    "C105_PHYSICAL_RECORD_CLAIM": {
        "C105_EXECUTABLE_CERTIFICATE", "RECORD_OCCURRENCE",
        "RECORD_LOCK_UNIQUENESS_PERMANENCE", "RECORD_CONTENT_READABILITY",
    },
    "C108_INTEGRATED_ROWS": {"C100_BASE_ROWS", "C101_FRAGMENT_ROWS"},
    "C105_BRIDGE_ROWS": {"C101_LITERAL_OUTPUT", "C108_CERT_TYPE", "GENERATED_A_SLICE"},
}

ATOM_PREMISE_NODE = {
    "FORMATION_OCCURRENCE": "RECORD_OCCURRENCE",
}


def dependency_closes(root: str, removed: frozenset[str]) -> bool:
    if root in removed:
        return False
    return all(
        dependency_closes(dependency, removed)
        for dependency in DEPENDENCIES.get(root, set())
    )


def c105_fingerprint() -> tuple[int, ...]:
    product_states = c105.POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        c105.POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + c105.POSITIVE.states * c105.RAIL_HORIZON
    )
    return (
        len(c105.c101.TERMINAL),
        len(c105.PRIMARY_SPINE),
        sum(map(len, c105.SPINE_GROUPS)),
        len(c105.PAYLOAD_SITES),
        len(c105.BRIDGE_TABLE),
        len(c105.BRIDGE_RAW),
        len(c105.FULL_RAW),
        c105.POSITIVE.states,
        c105.POSITIVE.edges,
        c105.POSITIVE.terminals,
        len(c105.POSITIVE.bad),
        len(c105.POSITIVE.premature),
        product_states,
        product_edges,
    )


EXPECTED_C105_FINGERPRINT = (
    264, 16, 17, 3, 18, 414, 7_310, 5_048, 21_426, 1, 0, 0,
    489_656, 2_562_930,
)


def literal_constants(path: Path, names: set[str]) -> dict[str, object]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: dict[str, object] = {}
    for statement in tree.body:
        if not isinstance(statement, ast.AnnAssign):
            continue
        if not isinstance(statement.target, ast.Name) or statement.target.id not in names:
            continue
        try:
            found[statement.target.id] = ast.literal_eval(statement.value)
        except (TypeError, ValueError):
            continue
    return found


def source_and_registry_contract() -> None:
    section("A - Current foundation, approved primitives, and source boundary")
    for name, path in {"cycle110_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registry has exactly the four canonical premise nodes",
        set(nodes) == {
            "minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive",
        },
        str(sorted(nodes)),
    )
    check(
        "A primitive current paths are the three notes read here",
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
        "A current Record supplies occurrence but no formation rule",
        has_all(texts["axioms"], (
            "records form",
            "formation rules (which admissible possibility",
            "does not choose a hamiltonian or transfer operator",
        )),
    )
    check(
        "A current Record locks on presence, not on a later read",
        has_all(texts["axioms"], (
            "when present, a record locks exactly one admissible local possibility",
            "only records are readable",
            "a readout value is determined by record content alone",
        )),
    )
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
        "A no proposed generic mechanism is smuggled into the primitive registry",
        all(row.classification != PRIMITIVE for row in GENERIC_ATOMS),
    )


def predecessor_contract() -> None:
    section("B - Exact Cycle-83/96/107/108/105 evidence")
    check(
        "B Cycle83 classifies physical continuation and menu support as law-owned",
        c83.ATOM_LEDGER["physical_continuation_relation"] == c83.LAW_FIELD
        and c83.ATOM_LEDGER["menu_complete_physical_support"] == c83.LAW_FIELD,
    )
    check(
        "B Cycle83 rejects generic read/witness/clock and storage slogans",
        c83.ATOM_LEDGER["reader_witness_or_clock_trigger"] == c83.REJECT_GENERIC
        and c83.ATOM_LEDGER["storage_or_compute_budget_slogan"] == c83.REJECT_GENERIC,
    )
    check(
        "B Cycle83 keeps exact complete-law identity conditional",
        c83.ATOM_LEDGER["exact_complete_law_identity"] == c83.CONSTITUTIONAL_ID,
    )

    by_id = {entry.ident: entry for entry in c96.INTERFACES}
    check(
        "B Cycle96 pins 75 unique dependency fields",
        len(by_id) == len(c96.INTERFACES) == 75,
    )
    check(
        "B Cycle96 makes availability projection and record contract theorem targets",
        by_id["LAW_AVAILABILITY_PROJECTION"].classification == c96.THEOREM_TARGET
        and by_id["LAW_RECORD_CONTRACT"].classification == c96.THEOREM_TARGET,
    )
    check(
        "B Cycle96 keeps occurrence, rate, counting, and resource maps in exact law",
        all(
            by_id[ident].classification == c96.EXACT_LAW_FIELD
            for ident in (
                "ITERATION_OCCURRENCE_SEMANTICS", "TIME_COMMIT_EVENT",
                "TIME_RELATIVE_RATE_LAPSE", "MATTER_EVENT_QUOTIENT_STATISTICS_CHIRALITY",
                "GR_RESOURCE_SOURCE_COEFFICIENTS",
            )
        ),
    )
    check(
        "B Cycle96 keeps history and clock calibration empirical",
        by_id["ACT_REALIZED_HISTORY_DATA"].classification == c96.EMPIRICAL_INPUT
        and by_id["TIME_CALIBRATION_DATA"].classification == c96.EMPIRICAL_INPUT,
    )

    class_counts = Counter(c107.TOE_FIELD_CLASSES.values())
    check(
        "B Cycle107 preserves the exact five-way 75-field census",
        class_counts == {
            c107.THEOREM_TARGET: 44,
            c107.EXACT_LAW_FIELD: 19,
            c107.EMPIRICAL_INPUT: 8,
            c107.PRIMITIVE: 3,
            c107.CONSTITUTIONAL_GATE: 1,
        },
        str(class_counts),
    )
    check(
        "B Cycle107 leaves one typed-cap-to-harness construction blocker",
        c107.SMALLEST_BLOCKER == "TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS"
        and c107.NEXT_OBJECT == "CAGED_R_B11_CAP_TO_DIRECTED_RENEWABLE_PAYLOAD_LAUNCH",
    )

    check(
        "B Cycle108 provides a 36-role injective reader-safe map and 6,896-row union",
        len(c108.ROLE_MAP) == len(set(c108.ROLE_MAP.values())) == 36
        and len(c108.INTEGRATED_RAW) == 6_896
        and all(len(values) == 1 for values in c108.INTEGRATED_RAW.values()),
    )
    stats108 = c108.integrated_graph()
    check(
        "B Cycle108 exact graph is 22,310 states / 91,338 edges / one terminal / zero bad",
        stats108.states == 22_310 and stats108.edges == 91_338
        and stats108.terminals == 1 and not stats108.bad,
        str(stats108),
    )

    check(
        "B Cycle105 exact fingerprint is unchanged",
        c105_fingerprint() == EXPECTED_C105_FINGERPRINT,
        str(c105_fingerprint()),
    )
    check(
        "B Cycle105 full law is a 7,310-row single-valued bounded union",
        len(c105.FULL_RAW) == 7_310
        and all(len(values) == 1 for values in c105.FULL_RAW.values()),
    )
    check(
        "B Cycle105 grows exactly three proper-cubic R_B11 cap images after JOINT",
        len(c105.PAYLOAD_SITES) == 3
        and c105.PAYLOAD_OUTPUT == "R_B11"
        and c105.POSITIVE.join_reached and c105.POSITIVE.payload_reached,
    )


def clause_deletion_contract() -> None:
    section("C - Clause deletion and Cycle-105 dependency trace")
    ids = {row.ident for row in ALL_ROWS}
    check("C all atom identifiers are unique", len(ids) == len(ALL_ROWS))
    check("C all five requested classifications are populated", {row.classification for row in ALL_ROWS} == CLASSES)
    check("C all eight requested generic families are covered", {
        row.family for row in GENERIC_ATOMS
    } >= {
        "formation", "read_lock", "two_witness", "clock", "storage",
        "counting", "continuation_separation", "complete_law_identity",
    })

    check(
        "C executable Cycle105 certificate has no generic proposal dependency",
        all(
            dependency_closes("C105_EXECUTABLE_CERTIFICATE", frozenset((row.ident,)))
            for row in GENERIC_ATOMS
        ),
    )

    deletion_failures = []
    for row in GENERIC_ATOMS:
        premise = ATOM_PREMISE_NODE.get(row.ident, row.ident)
        physical_closes = dependency_closes(
            "C105_PHYSICAL_RECORD_CLAIM", frozenset((premise,))
        )
        expected = row.ident != "FORMATION_OCCURRENCE"
        if physical_closes != expected:
            deletion_failures.append((row.ident, expected, physical_closes))
    check(
        "C only deleting current formation occurrence breaks Cycle105 physical-claim typing",
        not deletion_failures,
        str(deletion_failures),
    )
    check(
        "C formation occurrence is already supplied and is not a new forced atom",
        next(row for row in GENERIC_ATOMS if row.ident == "FORMATION_OCCURRENCE").disposition == CURRENT
        and not next(row for row in GENERIC_ATOMS if row.ident == "FORMATION_OCCURRENCE").forced_new,
    )
    check(
        "C local readiness and continuation are candidate-law uses, not generic constitutional uses",
        all(
            next(row for row in GENERIC_ATOMS if row.ident == ident).c105_use == USE_LOCAL_LAW
            for ident in ("FORMATION_EVENT_RULE", "PHYSICAL_CONTINUATION_KERNEL")
        ),
    )
    check(
        "C read-lock, witness, clock-lock, storage, and counting clauses delete cleanly",
        all(
            row.deletion_result == DELETE_LEAVES_C105 and row.c105_use == USE_NONE
            for row in GENERIC_ATOMS
            if row.ident in {
                "READ_CAUSES_FORMATION", "LATER_READ_CAUSES_LOCK",
                "TWO_INDEPENDENT_WITNESS_TRIGGER", "CLOCK_CAUSES_FINAL_LOCK",
                "GLOBAL_STORAGE_COMPUTE_BUDGET", "RESOURCE_RESPONSE_FROM_RECORD_LOAD",
                "COUNT_BY_PHYSICAL_POSSIBILITY", "MIRROR_CONJUGATE_COUNTS_ONCE",
            }
        ),
    )
    check(
        "C Cycle105 bounded confluence/state-sufficiency credit remains theorem-grade",
        all(
            next(row for row in GENERIC_ATOMS if row.ident == ident).c105_use == USE_BOUNDED_THEOREM
            for ident in ("CONTINUATION_COMPOSITION_CONFLUENCE", "RECORD_STATE_FUTURE_SUFFICIENCY")
        ),
    )
    check(
        "C no proposed new generic atom is forced",
        not any(row.forced_new for row in GENERIC_ATOMS),
    )

    census = Counter(row.classification for row in ALL_ROWS)
    check(
        "C primary classification census is exact",
        census == {
            CANDIDATE_LAW: 10,
            THEOREM: 4,
            EMPIRICAL: 2,
            PRIMITIVE: 3,
            CONSTITUTIONAL: 2,
        },
        str(census),
    )


def literal_join_and_cycle106_exclusion_contract() -> None:
    section("D - Literal join chronology and Cycle-106 exclusion seam")
    records = dict(c105.c101.TERMINAL)
    records.update(c105.c101.FRAGMENT_OUTPUTS)
    records[c105.NATURAL_TYPE] = c105.NATURAL_TYPE_OUTPUT
    for group, output in zip(c105.SPINE_GROUPS, c105.SPINE_OUTPUTS):
        records.update({site: output for site in group})
    parents = {
        site: records[site]
        for site in c105.neighbors(c105.JOIN)
        if site in records
    }
    check(
        "D Cycle105 JOINT has exactly OUTPUT, TYPE, and generated spine parents",
        parents == {
            c105.c101.OUTPUT: c105.c101.H1,
            c105.NATURAL_TYPE: c105.NATURAL_TYPE_OUTPUT,
            c105.PRIMARY_SPINE[-1]: c105.SPINE_OUTPUTS[-1],
        },
        str(parents),
    )
    check(
        "D payload caps are downstream consequences, not pre-JOINT witnesses",
        set(c105.PAYLOAD_SITES).isdisjoint(records)
        and c105.enabled(records).get(c105.JOIN) == frozenset((c105.JOIN_OUTPUT,)),
    )

    names = {"TYPE_ARM", "JOIN_GUARD", "JOIN", "STATUS", "REJECT"}
    c106_constants = literal_constants(SOURCES["cycle106_runner"], names)
    check(
        "D Cycle106 literal seam coordinates are parsed without importing it downstream",
        c106_constants == {
            "TYPE_ARM": (4, 5, 0),
            "JOIN_GUARD": (4, 6, 0),
            "JOIN": (4, 6, 1),
            "STATUS": (3, 6, 2),
            "REJECT": (4, 6, 2),
        },
        str(c106_constants),
    )
    c105_spine = dict(zip(c105.PRIMARY_SPINE, c105.SPINE_OUTPUTS))
    check(
        "D Cycle105/Cycle106 have two direct spine content conflicts",
        c105_spine[c106_constants["TYPE_ARM"]] == "AUX"
        and c105_spine[c106_constants["JOIN_GUARD"]] == "BTG",
    )
    check(
        "D Cycle105/Cycle106 share JOINT but collide at cap/reject",
        c106_constants["JOIN"] == c105.JOIN
        and c106_constants["REJECT"] in c105.PAYLOAD_SITES
        and c105.PAYLOAD_OUTPUT == "R_B11",
    )
    status = c106_constants["STATUS"]
    occupied_reject = c106_constants["REJECT"]
    check(
        "D Cycle105 cap is a nearest neighbor that can change Cycle106 STATUS signature by schedule",
        c105.c101.manhattan(status, occupied_reject) == 1,
    )
    c106_source = SOURCES["cycle106_runner"].read_text(encoding="utf-8").lower()
    c106_note = normalized(SOURCES["cycle106_note"])
    check(
        "D Cycle106 consumes Cycle105 only to certify the literal integration remains open",
        "import read_status_to_generated_rail_spine_cycle105" in c106_source
        and "disjoint from cycle 108's 6,896 raw inputs" in c106_note
        and "c105_integration_open" in c106_note
        and "does not advance after cycle 105" in c106_note
        and "7,550-input single-valued union" in c106_note,
    )


def dormant_identity_and_smuggle_contract() -> None:
    section("E - Dormant exact-law identity and premise-smuggle controls")
    by_id = {entry.ident: entry for entry in c96.INTERFACES}
    identity = by_id["LAW_IDENTITY_IF_NONDERIVED"]
    complete = by_id["LAW_COMPLETE_REFERENT"]
    check(
        "E L* identity remains the sole Cycle107 constitutional compatibility gate",
        {
            ident for ident, classification in c107.TOE_FIELD_CLASSES.items()
            if classification == c107.CONSTITUTIONAL_GATE
        } == {"LAW_IDENTITY_IF_NONDERIVED"},
    )
    check(
        "E L* identity remains dormant behind complete referent, uniqueness, and selection",
        identity.status == c96.DORMANT
        and set(identity.dependencies) == {
            "LAW_COMPLETE_REFERENT", "LAW_UNIQUENESS_OR_EQUIVALENCE", "LAW_SELECTION_DATA",
        }
        and complete.status == c96.OPEN,
    )
    check(
        "E Cycle105 cannot instantiate L* identity",
        len(c105.FULL_RAW) == 7_310
        and c105.RAIL_HORIZON == 96
        and c107.TOE_FIELD_CLASSES["LAW_COMPLETE_REFERENT"] == c107.EXACT_LAW_FIELD,
    )
    check(
        "E exact-law identity is not present in the registry",
        "exact_complete_law_identity" not in json.loads(
            SOURCES["registry"].read_text(encoding="utf-8")
        )["nodes"],
    )

    axioms = normalized(SOURCES["axioms"])
    absent_phrases = (
        "a record forms only when read",
        "two independent witnesses agree",
        "a clock event supplies the final record lock",
        "finite storage or compute budget",
        "mirrored or conjugate presentation counts once",
        "the exact physical law l",
    )
    check(
        "E current axioms contain none of the tested unlanded mechanism clauses",
        not any(phrase in axioms for phrase in absent_phrases),
        str([phrase for phrase in absent_phrases if phrase in axioms]),
    )
    check(
        "E C105 runner contains no witness/clock/storage/counting mechanism import",
        not any(
            phrase in SOURCES["cycle105"].read_text(encoding="utf-8").lower()
            for phrase in (
                "two-witness", "clock-lock", "storage-budget", "ticket-counting",
            )
        ),
    )


def note_and_no_go_contract() -> None:
    section("F - Cycle110 note and N1-N8 scope contract")
    note = normalized(NOTE) if NOTE.is_file() else ""
    raw = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check(
        "F note has authority none and no live repository action",
        has_all(note, (
            "authority: none", "no foundation edit", "no registry edit",
            "no queue edit", "no commit",
        )),
    )
    check(
        "F every generic atom and exact classification appears",
        all(
            row.ident.lower() in note and row.classification.lower() in note
            for row in GENERIC_ATOMS
        ),
    )
    check(
        "F note records the exact five-class census",
        has_all(note, (
            "10 candidate-law", "4 theorem", "2 empirical",
            "3 approved primitive", "2 constitutional",
        )),
    )
    check(
        "F note reports the only nondeletable current atom and no forced new atom",
        has_all(note, (
            "formation_occurrence", "already supplied",
            "no new generic atom is forced",
        )),
    )
    check(
        "F note distinguishes reading prior records from reading causing lock",
        has_all(note, (
            "reads already-locked parent content",
            "does not make reading the cause of their lock",
        )),
    )
    check(
        "F note excludes unrepaired Cycle106 downstream composition",
        has_all(note, (
            "cycle 106 is not consumed downstream",
            "aux/btg", "t_h2/t_h3", "cap/reject",
        )),
    )
    check(
        "F note keeps L* gate dormant and zero-edit route live",
        has_all(note, (
            "dormant", "no stable l", "zero-edit route remains live",
        )),
    )
    check(
        "F note includes complete N1-N8 discipline",
        all(f"n{index} —" in note for index in range(1, 9))
        and raw.count("`ATTEMPTED`") >= 5,
    )
    check(
        "F negative is explicitly scoped rather than universal",
        has_all(note, (
            "partial-narrowing-with-live-constructive-routes",
            "not a universal no-go", "strongest hostile steelman",
        )),
    )
    check(
        "F primitive scopes are quoted without enlargement",
        has_all(note, (
            "units only", "c_t=c_s form only",
            "pointwise realized-state reference only",
        )),
    )
    scientific_body = note.split("## no-go discipline gate", 1)[0]
    hidden = (
        "we assume", "as is standard", "the framework provides",
        "bridge context", "obviously", "naturally follows", "standard qft",
    )
    check(
        "F scientific body contains no hidden-premise phrase",
        not any(phrase in scientific_body for phrase in hidden),
        str([phrase for phrase in hidden if phrase in scientific_body]),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_registry_contract()
    predecessor_contract()
    clause_deletion_contract()
    literal_join_and_cycle106_exclusion_contract()
    dormant_identity_and_smuggle_contract()
    note_and_no_go_contract()
    print(f"\nGENERIC_ATOMS={len(GENERIC_ATOMS)} REFERENCES={len(REFERENCE_ROWS)} TOTAL_ROWS={len(ALL_ROWS)}")
    print(f"CLASS_CENSUS={dict(sorted(Counter(row.classification for row in ALL_ROWS).items()))}")
    print("FORCED_NEW_ATOMS=0")
    print("LSTAR_GATE=DORMANT_UNTIL_STABLE_NONDERIVED_LSTAR")
    print("CYCLE106_DOWNSTREAM=EXCLUDED_UNTIL_LITERAL_C105_UNION_REPAIRED")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
