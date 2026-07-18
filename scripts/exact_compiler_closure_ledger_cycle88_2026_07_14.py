#!/usr/bin/env python3
"""Cycle 88: exact compiler-closure ledger and composition controls.

The runner checks the Cycle-80/Cycle-82 carrier and raw-table interface,
reconciles every named Cycle-80/81/82/84 residual, and pins the selected
three-object constructive dependency path.  It does not construct the missing
objects, select L*, edit a foundation surface, or issue an audit verdict.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
sys.path.insert(0, str(SCRIPTS))

import constructive_constitutional_delta_audit_cycle83_2026_07_14 as c83  # noqa: E402
import directional_multiword_rule_port_output_cycle82_2026_07_14 as c82  # noqa: E402
import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81  # noqa: E402
import joint_endpoint_mixed_rebind_cycle78_2026_07_14 as c78  # noqa: E402
import separated_recurrent_tube_collision_control_cycle84_2026_07_14 as c84  # noqa: E402
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80  # noqa: E402


NOTE = REVIEW / "EXACT_COMPILER_CLOSURE_LEDGER_CYCLE88_NOTE_2026-07-14.md"

SOURCES = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "contract": REVIEW / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md",
    "cycle78": REVIEW / "JOINT_ENDPOINT_MIXED_REBIND_CYCLE78_NOTE_2026-07-14.md",
    "cycle80": REVIEW / "THREE_PHASE_RECURRENT_APPEND_TUBE_CYCLE80_NOTE_2026-07-14.md",
    "cycle81": REVIEW / "EIGHT_BIT_PHYSICAL_ROLE_COMPARATOR_CYCLE81_NOTE_2026-07-14.md",
    "cycle82": REVIEW / "DIRECTIONAL_MULTIWORD_RULE_PORT_OUTPUT_CYCLE82_NOTE_2026-07-14.md",
    "cycle83": REVIEW / "CONSTRUCTIVE_CONSTITUTIONAL_DELTA_AUDIT_CYCLE83_NOTE_2026-07-14.md",
    "cycle84": REVIEW / "SEPARATED_RECURRENT_TUBE_COLLISION_CONTROL_CYCLE84_NOTE_2026-07-14.md",
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


W_BOOT = "W_BOOT"
W_STEP = "W_STEP"
W_MULTI = "W_MULTI"
CLOSED_CORE = "CLOSED_CORE"
THEOREM_GATE = "T_NN_COMPLETE"


ORIGINAL_RESIDUAL_MAP = {
    "C80:NEXT_FRONT_TO_TUBE_NUCLEATION": (W_BOOT,),
    "C80:TUBE_LAYER_TO_LOGICAL_FRONT": (W_STEP,),
    "C80:EIGHT_BIT_RULE_PORT_REALIZATION": (W_BOOT, W_STEP),
    "C80:MULTI_FRONT_CONFLUENCE": (W_MULTI,),
    "C81:SEED_TO_EIGHT_BIT_COMPARATOR_HARNESS": (W_BOOT, W_STEP),
    "C81:DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT": (CLOSED_CORE, W_STEP),
    "C81:RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD": (CLOSED_CORE, W_BOOT, W_STEP),
    "C82:NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM": (W_STEP,),
    "C82:OPEN_DIRECTION_TO_EMPTY_WORD": (W_STEP,),
    "C82:CANDIDATE_FANOUT_TO_198_PROGRAMS": (W_STEP,),
    "C82:SEED_TO_RULE_PORT_OUTPUT_HARNESS": (W_BOOT, W_STEP),
    "C84:ADJACENT_CONTACT_OR_SEPARATION_INVARIANT": (W_MULTI,),
    "C84:TUBE_NUCLEATION": (W_BOOT,),
    "C88:VALIDATED_OUTPUT_WORD_TO_LOGICAL_FRONT": (W_STEP,),
}

COLLAPSED_WALLS = (W_BOOT, W_STEP, W_MULTI)

DEPENDENCY_PATH = (
    "C78_READY_TERMINAL",
    W_BOOT,
    W_STEP,
    W_MULTI,
    THEOREM_GATE,
    "L_NN",
    "CATEGORY_B_LOCAL_LAW_FIELDS",
    "CATEGORY_C_TOE_PREDICTIVE_FIELDS",
    "L_STAR",
)

CATEGORY_A = {
    "A-FIRST": W_BOOT,
    "A-COMP": f"{W_BOOT}/{W_STEP}",
    "A-PROG": f"{W_BOOT}/{W_STEP}",
    "A-ROUTE": W_STEP,
    "A-EMPTY": W_STEP,
    "A-OUT": f"{W_BOOT}/{W_STEP}",
    "A-FRESH": f"{W_BOOT}/{W_STEP}/{W_MULTI}",
}

CATEGORY_B = {
    "DOMAIN",
    "STATE",
    "CONTEXT",
    "ATOMIC_LAW",
    "CONTINUATION",
    "AVAILABILITY",
    "CONCURRENCY",
    "RECORD",
}

CATEGORY_C = {
    "ACTUALITY",
    "STATISTICS",
    "OPERATIONAL",
    "CLOCK",
    "MATTER",
    "RESOURCE",
    "CONTINUUM",
    "GRAVITY",
    "BOUNDARY",
}

CATEGORY_D = {
    "EXACT_LAW_IDENTITY": "CONDITIONAL_CONSTITUTIONAL_CANDIDATE",
    "RECORD_COMPATIBILITY": "CONDITIONAL_SELECTED_LAW_GATE",
    "STATE_COMPATIBILITY": "CONDITIONAL_SELECTED_LAW_GATE",
}

INDEPENDENCE = {
    (W_BOOT, W_STEP): (False, False),
    (W_BOOT, W_MULTI): (False, False),
    (W_STEP, W_MULTI): (False, False),
}


def source_contract() -> None:
    section("A - Source, authority, and completeness-contract boundary")
    for name, path in {"cycle88": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    texts = {name: normalized(path) for name, path in SOURCES.items()}
    check("A live foundation leaves formation rule, weights, and rate open", has_all(texts["axioms"], (
        "formation rules (which admissible possibility a new record locks, at which site, with what weight, or at what rate)",
        "admissibility is not a dynamics axiom",
    )))
    check("A primitive registry has only approved foundation families", has_all(texts["registry"], (
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    )))
    check("A primitive notes grant no compiler or selector", has_all(texts["scale"], (
        "units conversion, not a physics axiom",
    )) and has_all(texts["kinetic"], (
        "c_t = c_s", "not a new dynamics",
    )) and has_all(texts["realized"], (
        "one realized-state reference", "no state, averaging over alternatives, measure",
    )))
    check("A canonical contract exposes ten foundational fields", has_all(texts["contract"], tuple(
        field.lower() for field in (
            "DOMAIN", "STATE", "CONTEXT", "ATOMIC_LAW", "CONTINUATION",
            "AVAILABILITY", "CONCURRENCY", "RECORD", "ACTUALITY", "STATISTICS",
        )
    )))
    check("A Cycle80 source names all four compiler residuals", has_all(texts["cycle80"], (
        "next_front_to_tube_nucleation",
        "tube_layer_to_logical_front",
        "eight_bit_rule_port_realization",
        "multi_front_confluence",
    )))
    check("A Cycle82 source names all four residuals", has_all(texts["cycle82"], (
        "neighbour_macroblocks_to_ordered_stream",
        "open_direction_to_empty_word",
        "candidate_fanout_to_198_programs",
        "seed_to_rule_port_output_harness",
    )))
    check("A Cycle84 source keeps contact and nucleation open", has_all(texts["cycle84"], (
        "does not resolve adjacent collisions",
        "nucleate either tube",
    )))


def exact_composition_contract() -> None:
    section("B - Cycle80/Cycle82 carrier and causal-interface controls")
    recurrence_roles = frozenset(c80.CONSTRUCTION.table.values()) | frozenset(
        content for local in c80.CONSTRUCTION.table for _offset, content in local
    )
    recurrence_outputs = frozenset(c80.CONSTRUCTION.table.values())
    arities = Counter(map(len, c80.CONSTRUCTION.table))

    check("B recurrence uses exactly 51 roles and 51 outputs", len(recurrence_roles) == len(recurrence_outputs) == 51)
    check("B every recurrence role has an eight-bit code", all(role in c81.ROLE_TO_WORD for role in recurrence_roles))
    check("B every recurrence code uses only physical binary bits", all(
        len(c81.ROLE_TO_WORD[role]) == 8 and set(c81.ROLE_TO_WORD[role]) <= {0, 1}
        for role in recurrence_roles
    ))
    check("B all 51 recurrence rows have Cycle82 directional programs", all(
        local in c82.ROW_PROGRAMS for local in c80.CONSTRUCTION.table
    ))
    check("B recurrence arity census is exact and has no full row", arities == {
        1: 3, 2: 31, 3: 10, 4: 4, 5: 3,
    } and 6 not in arities, str(arities))
    check("B Cycle82 executed full-row set is disjoint from recurrence", not (
        {local for local, _output in c82.SIX_ROWS} & set(c80.CONSTRUCTION.table)
    ))

    raw80 = c80.c59.raw_rule_outputs(c80.CONSTRUCTION.table)
    check("B all Cycle80 raw rows occur identically in Cycle82 union", all(
        local in c82.COMBINED_RAW and c82.COMBINED_RAW[local] == outputs
        for local, outputs in raw80.items()
    ))
    check("B Cycle82 raw union remains 4588 single-valued rows", len(c82.COMBINED_RAW) == 4_588 and all(
        len(outputs) == 1 for outputs in c82.COMBINED_RAW.values()
    ))

    writer_failures = []
    writer_states = 0
    for role in sorted(recurrence_outputs):
        word = c81.ROLE_TO_WORD[role]
        source = c82.output_harness(word)
        additions = c82.output_additions(word)
        for step in range(len(additions) + 1):
            records = dict(source)
            records.update(dict(additions[:step]))
            expected = {additions[step][0]: additions[step][1]} if step < len(additions) else {}
            actual = c82.assignments(records)
            writer_states += 1
            if actual != expected:
                writer_failures.append((role, step, expected, actual))
        terminal = dict(source)
        terminal.update(dict(additions))
        if c82.decode_output(terminal) != word:
            writer_failures.append((role, "decode", word, c82.decode_output(terminal)))
    check("B writer executes every recurrent output word exactly", writer_states == 51 * 18 and not writer_failures, str(writer_failures[:1]))

    check("B recurrence one-site outputs are not physical H0/H1 ports", recurrence_outputs.isdisjoint({c82.H0, c82.H1}))
    transition = c80.transition("A")
    check("B exposed recurrence boundary is a symbolic role, not writer H1 port", bool(transition.boundary) and c80.role("C", *c80.SEED["C"]) != c82.H1)
    check("B Cycle82 writer still needs 69 supplied records plus port", all(
        len(c82.output_harness(word, port=False)) == 69 and len(c82.output_harness(word, port=True)) == 70
        for word in (c81.ALL_WORDS[0], c81.ALL_WORDS[-1])
    ))
    check("B validated output is eight DATA sites, not one recurrence site", len(c82.DATA) == 8 and len(set(c82.DATA)) == 8)

    source, allowed = c84.one_tube(3)
    offset = c84.OFFSETS[0]
    shifted_source = c84.translate(source, offset)
    shifted_allowed = c84.translate(allowed, offset)
    support = set(source) | set(allowed)
    shifted_support = set(shifted_source) | set(shifted_allowed)
    joint = c84.c63.exact_graph(
        source | shifted_source,
        c80.CONSTRUCTION.table,
        allowed | shifted_allowed,
    )
    check("B Cycle84 separated support distance is exactly two", c84.minimum_cross_distance(support, shifted_support) == 2)
    check("B Cycle84 h3 joint counters are exact", (
        joint.conditions, len(joint.states), joint.edges, len(joint.parasites), len(joint.conflicts)
    ) == (144, 2_704, 5_408, 2, 0))


def residual_and_dependency_contract() -> None:
    section("C - Original residual map and collapsed dependency path")
    expected_originals = {
        "C80:NEXT_FRONT_TO_TUBE_NUCLEATION",
        "C80:TUBE_LAYER_TO_LOGICAL_FRONT",
        "C80:EIGHT_BIT_RULE_PORT_REALIZATION",
        "C80:MULTI_FRONT_CONFLUENCE",
        "C81:SEED_TO_EIGHT_BIT_COMPARATOR_HARNESS",
        "C81:DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT",
        "C81:RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD",
        "C82:NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM",
        "C82:OPEN_DIRECTION_TO_EMPTY_WORD",
        "C82:CANDIDATE_FANOUT_TO_198_PROGRAMS",
        "C82:SEED_TO_RULE_PORT_OUTPUT_HARNESS",
        "C84:ADJACENT_CONTACT_OR_SEPARATION_INVARIANT",
        "C84:TUBE_NUCLEATION",
        "C88:VALIDATED_OUTPUT_WORD_TO_LOGICAL_FRONT",
    }
    check("C every named original/compiler residual is mapped", set(ORIGINAL_RESIDUAL_MAP) == expected_originals)
    check("C every open original maps into one of three constructive objects", all(
        owner in {*COLLAPSED_WALLS, CLOSED_CORE}
        for owners in ORIGINAL_RESIDUAL_MAP.values()
        for owner in owners
    ))
    check("C selected collapsed constructive set is exactly three objects", COLLAPSED_WALLS == (W_BOOT, W_STEP, W_MULTI))
    check("C Cycle81 comparator and Cycle82 writer cores receive closure credit", all(
        CLOSED_CORE in ORIGINAL_RESIDUAL_MAP[item] for item in (
            "C81:DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT",
            "C81:RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD",
        )
    ))
    check("C output-word/logical-front interface is not double-counted", ORIGINAL_RESIDUAL_MAP[
        "C88:VALIDATED_OUTPUT_WORD_TO_LOGICAL_FRONT"
    ] == (W_STEP,) and ORIGINAL_RESIDUAL_MAP["C80:TUBE_LAYER_TO_LOGICAL_FRONT"] == (W_STEP,))
    check("C tube nucleation is not double-counted", ORIGINAL_RESIDUAL_MAP[
        "C84:TUBE_NUCLEATION"
    ] == (W_BOOT,) and ORIGINAL_RESIDUAL_MAP["C80:NEXT_FRONT_TO_TUBE_NUCLEATION"] == (W_BOOT,))
    check("C shortest selected dependency path is pinned", DEPENDENCY_PATH == (
        "C78_READY_TERMINAL", W_BOOT, W_STEP, W_MULTI, THEOREM_GATE,
        "L_NN", "CATEGORY_B_LOCAL_LAW_FIELDS", "CATEGORY_C_TOE_PREDICTIVE_FIELDS", "L_STAR",
    ))
    check("C all three wall pairs have bidirectional non-implication entries", set(INDEPENDENCE) == {
        (W_BOOT, W_STEP), (W_BOOT, W_MULTI), (W_STEP, W_MULTI)
    } and all(value == (False, False) for value in INDEPENDENCE.values()))


def category_contract() -> None:
    section("D - Harness, local-law, TOE-predictive, and constitutional categories")
    check("D Category A has all seven supplied-harness families", set(CATEGORY_A) == {
        "A-FIRST", "A-COMP", "A-PROG", "A-ROUTE", "A-EMPTY", "A-OUT", "A-FRESH",
    })
    check("D Category A owners use only three constructive objects", all(
        set(owner.split("/")) <= set(COLLAPSED_WALLS) for owner in CATEGORY_A.values()
    ))
    check("D Category B is exactly the eight local-law fields", CATEGORY_B == {
        "DOMAIN", "STATE", "CONTEXT", "ATOMIC_LAW", "CONTINUATION",
        "AVAILABILITY", "CONCURRENCY", "RECORD",
    })
    check("D Category C is actuality/statistics plus seven TOE interfaces", CATEGORY_C == {
        "ACTUALITY", "STATISTICS", "OPERATIONAL", "CLOCK", "MATTER",
        "RESOURCE", "CONTINUUM", "GRAVITY", "BOUNDARY",
    })
    check("D Category D has exactly one conditional universal candidate", {
        item for item, status in CATEGORY_D.items()
        if status == "CONDITIONAL_CONSTITUTIONAL_CANDIDATE"
    } == {"EXACT_LAW_IDENTITY"})
    check("D Record and state changes remain selected-law compatibility gates", all(
        CATEGORY_D[item] == "CONDITIONAL_SELECTED_LAW_GATE"
        for item in ("RECORD_COMPATIBILITY", "STATE_COMPATIBILITY")
    ))
    check("D Cycle83 agrees exact law identity is sole constitutional candidate", {
        atom for atom, status in c83.ATOM_LEDGER.items()
        if status == c83.CONSTITUTIONAL_ID
    } == {"exact_complete_law_identity"})
    check("D all category identifiers are disjoint", not (
        set(CATEGORY_A) & CATEGORY_B or set(CATEGORY_A) & CATEGORY_C or
        CATEGORY_B & CATEGORY_C or set(CATEGORY_D) & (set(CATEGORY_A) | CATEGORY_B | CATEGORY_C)
    ))


def note_and_no_go_contract() -> None:
    section("E - Cycle88 note and N1-N8 scope contract")
    note = normalized(NOTE)
    check("E note carries no authority", "authority: none" in note)
    check("E note states carrier-compatible but causally uncomposed", "carrier-compatible, raw-table-compatible, but not yet causally composed" in note)
    check("E note names all three collapsed constructive objects", has_all(note, (
        "w_boot — grow the first complete physical compiler/recurrent cell",
        "w_step — execute one self-hosted physical macrostep",
        "w_multi — close the reachable multi-front domain",
    )))
    check("E note states no recurrent row reached Cycle82 end-to-end", has_all(note, (
        "cycle 80 has no arity-six rows",
        "none of the recurrent rows has yet run through the physical serializer",
    )))
    check("E note preserves no-new-substrate uncertainty", has_all(note, (
        "no new substrate content is presently indicated",
        "no theorem yet proves that the missing geometry can be built",
    )))
    check("E note distinguishes compiler engine from complete TOE", has_all(note, (
        "l_nn is not yet the toe l",
        "category c — toe-predictive fields",
    )))
    check("E note maps every original named residual", all(
        residual.split(":", 1)[1].lower() in note
        for residual in ORIGINAL_RESIDUAL_MAP
        if residual.startswith(("C80:", "C81:", "C82:"))
    ) and has_all(note, (
        "adjacent/contact collision behavior",
        "proof that selected nucleation always preserves the one-row margin",
        "nucleation of either tube",
    )))
    check("E note includes every N1-N8 section", all(f"n{index} —" in note for index in range(1, 9)))
    check("E note limits shortest-path claim", has_all(note, (
        "shortest dependency ledger found for this selected route",
        "not a global minimality theorem",
        "not a universal compiler, substrate, or toe no-go",
    )))
    check("E note includes hostile monolithic-cell steelman", has_all(note, (
        "strongest hostile steelman",
        "one completed macroblock simultaneously encode its output",
        "defeats a global three-wall lower bound",
    )))
    check("E note denies foundation and axiom edits", has_all(note, (
        "no foundation or axiom edit follows",
        "only eventual constitutional content",
    )))

    body = note.split("## 10. no-go discipline gate", 1)[0]
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
    check("E note makes no universal minimum/no-go claim", all(phrase not in note for phrase in (
        "three walls are universally necessary",
        "composition is impossible on m2(c)",
        "a new substrate axiom is required",
        "no compiler can close",
    )))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_contract()
    exact_composition_contract()
    residual_and_dependency_contract()
    category_contract()
    note_and_no_go_contract()
    print(f"\nORIGINAL_RESIDUALS={len(ORIGINAL_RESIDUAL_MAP)} COLLAPSED_WALLS={len(COLLAPSED_WALLS)}")
    print(f"CATEGORY_A={len(CATEGORY_A)} CATEGORY_B={len(CATEGORY_B)} CATEGORY_C={len(CATEGORY_C)} CATEGORY_D={len(CATEGORY_D)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
