#!/usr/bin/env python3
"""Cycle 83: lightweight constructive constitutional-delta controls.

This runner verifies the live foundation boundary, selected exact counters
from Cycles 75/78/80/81, and a machine-readable atom/lane disposition.  It
does not select a law, alter an axiom, issue an audit verdict, or rerun the
memory-heavy Cycle-81 all-pairs enumeration.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
sys.path.insert(0, str(SCRIPTS))

import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81  # noqa: E402
import joint_endpoint_mixed_rebind_cycle78_2026_07_14 as c78  # noqa: E402
import seven_bit_physical_role_comparator_cycle75_2026_07_14 as c75  # noqa: E402
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80  # noqa: E402


NOTE = REVIEW / "CONSTRUCTIVE_CONSTITUTIONAL_DELTA_AUDIT_CYCLE83_NOTE_2026-07-14.md"

SOURCES = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle47": REVIEW / "SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md",
    "cycle75": REVIEW / "SEVEN_BIT_PHYSICAL_ROLE_COMPARATOR_CYCLE75_NOTE_2026-07-14.md",
    "cycle78": REVIEW / "JOINT_ENDPOINT_MIXED_REBIND_CYCLE78_NOTE_2026-07-14.md",
    "cycle80": REVIEW / "THREE_PHASE_RECURRENT_APPEND_TUBE_CYCLE80_NOTE_2026-07-14.md",
    "cycle81": REVIEW / "EIGHT_BIT_PHYSICAL_ROLE_COMPARATOR_CYCLE81_NOTE_2026-07-14.md",
    "actuality": REVIEW / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md",
    "born": REVIEW / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "clock": REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    "matter": REVIEW / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md",
    "gravity": REVIEW / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "law_identity": REVIEW / "EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md",
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


SUPPLIED = "SUPPLIED"
CANDIDATE_THEOREM = "CANDIDATE_LAW_THEOREM"
LAW_FIELD = "LAW_FIELD"
LAW_OR_HISTORY = "LAW_OR_HISTORY_FIELD"
CONDITIONAL_THEOREM = "CONDITIONAL_THEOREM"
COMPATIBILITY_GATE = "CONDITIONAL_COMPATIBILITY_GATE"
CONSTITUTIONAL_ID = "CONDITIONAL_CONSTITUTIONAL_IDENTIFICATION"
REJECT_GENERIC = "REJECT_GENERIC_AXIOM"

ATOM_LEDGER = {
    "availability_rule_existence": SUPPLIED,
    "record_occurrence": SUPPLIED,
    "record_lock_uniqueness_permanence": SUPPLIED,
    "record_only_readout_and_finite_additivity": SUPPLIED,
    "physical_continuation_relation": LAW_FIELD,
    "menu_complete_physical_support": LAW_FIELD,
    "finite_causal_formation_certificate": CANDIDATE_THEOREM,
    "append_only_serial_recurrence": CANDIDATE_THEOREM,
    "fixed_site_content_preservation": CANDIDATE_THEOREM,
    "conflicting_record_nonreconnection": CONDITIONAL_THEOREM,
    "record_identity_semantics": COMPATIBILITY_GATE,
    "record_state_future_sufficiency": COMPATIBILITY_GATE,
    "reader_witness_or_clock_trigger": REJECT_GENERIC,
    "every_update_forms_record": REJECT_GENERIC,
    "physical_role_binary_encoding": CANDIDATE_THEOREM,
    "one_actual_history": LAW_OR_HISTORY,
    "normalized_record_weight_law": LAW_FIELD,
    "born_affine_trace_form": CONDITIONAL_THEOREM,
    "commit_count_clock": CONDITIONAL_THEOREM,
    "metric_event_rate": LAW_FIELD,
    "physical_event_equivalence_and_counting": LAW_FIELD,
    "formation_energy_and_mass_map": LAW_FIELD,
    "resource_gravity_response": LAW_FIELD,
    "storage_or_compute_budget_slogan": REJECT_GENERIC,
    "exact_complete_law_identity": CONSTITUTIONAL_ID,
}

LANE_LEDGER = {
    "formation_architecture": "PARTIAL_CONSTRUCTIVE_LAW",
    "actuality": "OPEN_LAW_OR_HISTORY",
    "probability": "CONDITIONAL_THEOREM_PLUS_OPEN_LAW",
    "rate_time": "COUNT_DERIVED_RATE_OPEN",
    "state_composition": "CONDITIONAL_COMPATIBILITY",
    "matter_counting": "CONDITIONAL_THEOREM_PLUS_OPEN_LAW",
    "gravity_resource": "PARTIAL_CONSTRUCTIVE_LAW",
    "exact_law_identity": "CONDITIONAL_CONSTITUTIONAL_NOT_READY",
}

ROUTE_LEDGER = {
    "generic_continuation_append_prose": "DO_NOT_ADD",
    "one_exact_law_identification": "FAVORED_CONDITIONAL_NOT_READY",
    "mechanism_specific_formation_prose": "DO_NOT_ADD",
}


def source_contract() -> None:
    section("A - Live foundation, primitive, and source contract")
    for name, path in {"cycle83": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    texts = {name: normalized(path) for name, path in SOURCES.items()}
    check("A live Admissibility remains availability-only", has_all(texts["axioms"], (
        "there is one fixed nearest-neighbor admissibility rule",
        "admissibility is not a dynamics axiom",
        "does not choose a hamiltonian or transfer operator",
    )))
    check("A live Record supplies occurrence, lock, uniqueness, and permanence", has_all(texts["axioms"], (
        "records form",
        "locks exactly one admissible local possibility",
        "a site never carries more than one record",
        "records are permanent",
    )))
    check("A live Qualification types state as records", "a state is a configuration of records" in texts["axioms"])
    check("A registry has only the approved foundation families", has_all(texts["registry"], (
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    )))
    check("A scale primitive remains units-only", "units conversion, not a physics axiom" in texts["scale"])
    check("A kinetic primitive remains structural", has_all(texts["kinetic"], ("c_t = c_s", "not a new dynamics")))
    check("A realized-state primitive supplies no selector or measure", has_all(texts["realized"], (
        "one realized-state reference",
        "no state, averaging over alternatives, measure",
    )))
    check("A Cycle47 names finite W_C acceptance object", has_all(texts["cycle47"], (
        "frame_retaining_open_quartet_phase_transducer",
        "single-front",
        "renewal_rebinding",
    )))
    check("A Cycle80 preserves four exact residuals", has_all(texts["cycle80"], (
        "next_front_to_tube_nucleation",
        "tube_layer_to_logical_front",
        "eight_bit_rule_port_realization",
        "multi_front_confluence",
    )))


def constructive_contract() -> None:
    section("B - Lightweight constructive delta controls")

    construction78 = c78.CONSTRUCTION
    raw78 = c78.c70.raw_outputs(construction78.new_table)
    union_raw78 = c78.c70.raw_outputs(construction78.union_table)
    check("B Cycle78 has 47 append-only additions", len(construction78.allowed) == 47)
    check("B Cycle78 row counts are 39/870 and 159/3464", (
        len(construction78.new_table), len(raw78),
        len(construction78.union_table), len(union_raw78),
    ) == (39, 870, 159, 3_464))
    graph78 = c78.c63.exact_graph(construction78.source, construction78.union_table, construction78.allowed)
    check("B Cycle78 conditional graph counters are exact", (
        graph78.conditions, len(graph78.states), graph78.edges, len(graph78.terminals)
    ) == (72, 10_568, 49_142, 1))
    check("B Cycle78 graph has no parasite or conflict", not graph78.parasites and not graph78.conflicts)
    check("B Cycle78 next quartet stays open", has_all(normalized(SOURCES["cycle78"]), (
        "next q'/a'/b'/c' stay open",
        "every b record has both",
        "feasible wrong writes 0",
    )))

    raw80 = c80.c59.raw_rule_outputs(c80.CONSTRUCTION.table)
    check("B Cycle80 has 17 sites, 51 canonical rows, and 1170 raw rows", (
        len(c80.CROSS_SECTION), len(c80.CONSTRUCTION.table), len(raw80)
    ) == (17, 51, 1_170))
    transitions = tuple(c80.transition(phase) for phase in c80.PHASES)
    check("B Cycle80 all phase transitions have exact 18/18/18 counters", all(
        (item.states, item.edges, item.conditions) == (18, 18, 18) for item in transitions
    ))
    check("B Cycle80 has no dead, bad, or conflicting phase transition", all(
        not item.dead and not item.bad and not item.conflicts for item in transitions
    ))
    graph80 = c80.horizon_graph(15)
    check("B Cycle80 fifteen-layer horizon is exact", (
        graph80.conditions, len(graph80.states), graph80.edges, len(graph80.parasites), len(graph80.conflicts)
    ) == (460, 256, 256, 1, 0))

    check("B Cycle75 source-preserving inventory needs seven bits", len(c75.FULL_ROLES) == 83 and 2**6 < 83 <= 2**7)
    check("B Cycle75 comparator is three canonical and 56 raw rows", len(c75.NEW_CANONICAL_TABLE) == 3 and len(c75.NEW_RAW_OUTPUTS) == 56)
    check("B Cycle81 source-preserving inventory needs eight bits", len(c81.FULL_ROLES) == 134 and 2**7 < 134 <= 2**8)
    check("B Cycle81 leaves 122 reserved words", len(c81.RESERVED_WORDS) == 122)
    check("B Cycle81 comparator is three canonical and 56 raw rows", len(c81.CANONICAL_TABLE) == 3 and len(c81.RAW_OUTPUTS) == 56)
    check("B Cycle81 selected and provisional unions remain single-valued", (
        len(c81.SELECTED_TABLE), len(c81.SELECTED_RAW_OUTPUTS), len(c81.COMBINED_RAW_OUTPUTS)
    ) == (198, 4_376, 4_564) and all(len(outputs) == 1 for outputs in c81.COMBINED_RAW_OUTPUTS.values()))


def disposition_contract() -> None:
    section("C - Constitutional atom, lane, and route disposition")
    expected_statuses = {
        SUPPLIED,
        CANDIDATE_THEOREM,
        LAW_FIELD,
        LAW_OR_HISTORY,
        CONDITIONAL_THEOREM,
        COMPATIBILITY_GATE,
        CONSTITUTIONAL_ID,
        REJECT_GENERIC,
    }
    check("C every atom status class is populated", set(ATOM_LEDGER.values()) == expected_statuses)
    check("C only exact complete law identity is a constitutional candidate", {
        atom for atom, status in ATOM_LEDGER.items() if status == CONSTITUTIONAL_ID
    } == {"exact_complete_law_identity"})
    check("C continuation and menu support remain law fields", all(
        ATOM_LEDGER[atom] == LAW_FIELD for atom in (
            "physical_continuation_relation", "menu_complete_physical_support"
        )
    ))
    check("C finite certificate, recurrence, preservation, and encoding are candidate theorems", all(
        ATOM_LEDGER[atom] == CANDIDATE_THEOREM for atom in (
            "finite_causal_formation_certificate",
            "append_only_serial_recurrence",
            "fixed_site_content_preservation",
            "physical_role_binary_encoding",
        )
    ))
    check("C witness/read/clock and budget slogans are rejected generically", all(
        ATOM_LEDGER[atom] == REJECT_GENERIC for atom in (
            "reader_witness_or_clock_trigger",
            "storage_or_compute_budget_slogan",
        )
    ))
    check("C no TOE lane is marked axiom-ready", all("AXIOM_READY" not in value for value in LANE_LEDGER.values()))
    check("C exact-law lane is conditional and not ready", LANE_LEDGER["exact_law_identity"] == "CONDITIONAL_CONSTITUTIONAL_NOT_READY")
    check("C route ledger favors only exact-law identification conditionally", ROUTE_LEDGER == {
        "generic_continuation_append_prose": "DO_NOT_ADD",
        "one_exact_law_identification": "FAVORED_CONDITIONAL_NOT_READY",
        "mechanism_specific_formation_prose": "DO_NOT_ADD",
    })
    check("C status census is stable", Counter(ATOM_LEDGER.values()) == {
        SUPPLIED: 4,
        CANDIDATE_THEOREM: 4,
        LAW_FIELD: 7,
        LAW_OR_HISTORY: 1,
        CONDITIONAL_THEOREM: 3,
        COMPATIBILITY_GATE: 2,
        REJECT_GENERIC: 3,
        CONSTITUTIONAL_ID: 1,
    }, str(Counter(ATOM_LEDGER.values())))


def note_and_no_go_contract() -> None:
    section("D - Cycle83 note, scope, and no-go discipline contract")
    note = normalized(NOTE)
    check("D note carries no authority", "authority: none" in note)
    check("D note forbids a live edit", has_all(note, (
        "until that referent exists, make no live edit",
        "no admissibility or record prose is ready for insertion today",
    )))
    check("D note gives the exact-law target schema", "the fixed nearest-neighbor admissibility rule is the exact physical law l." in note)
    check("D note preserves zero-edit derivation route", "if l is uniquely derived, land nothing" in note)
    check("D note names all three route verdicts", has_all(note, (
        "route 1 — generic continuation and append-only prose",
        "route 2 — one exact-law identification",
        "route 3 — mechanism-specific formation language",
    )))
    check("D note includes all N1-N8 sections", all(f"n{index} —" in note for index in range(1, 9)))
    check("D note limits the negative claim", has_all(note, (
        "partial-narrowing-with-live-constructive-routes",
        "not a universal no-go",
        "strongest hostile steelman",
    )))
    check("D note distinguishes current construct from complete TOE law", has_all(note, (
        "valuable components of a law, not a complete toe law",
        "no complete selected l",
    )))
    check("D note keeps Cycle80 attachment walls explicit", has_all(note, (
        "next_front_to_tube_nucleation",
        "tube_layer_to_logical_front",
        "multi_front_confluence",
    )))
    check("D note blocks menu-complete support promotion", "delete from present draft" in note)
    check("D note blocks generic same-site preservation promotion", "redundant on the two successful append architectures" in note)

    scientific_body = note.split("## no-go discipline gate", 1)[0]
    hidden_phrases = (
        "we assume",
        "as is standard",
        "the framework provides",
        "obviously",
        "naturally follows",
        "standard qft",
    )
    check("D scientific body contains no hidden-premise phrase", not any(
        phrase in scientific_body for phrase in hidden_phrases
    ), str([phrase for phrase in hidden_phrases if phrase in scientific_body]))
    check("D note does not claim a required present axiom add", all(phrase not in note for phrase in (
        "a new axiom is required",
        "must add a formation axiom",
        "the exact-law axiom is necessary now",
    )))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_contract()
    constructive_contract()
    disposition_contract()
    note_and_no_go_contract()
    print(f"\nATOMS={len(ATOM_LEDGER)} LANES={len(LANE_LEDGER)} ROUTES={len(ROUTE_LEDGER)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
