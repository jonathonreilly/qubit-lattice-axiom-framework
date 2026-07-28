#!/usr/bin/env python3
"""Paired runner for RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md

Verifies (text checks only, no verdicts):
  [NOTE] the note carries the proposal disclaimers and the H1-H4 clauses;
  [C1]   each named field-content-pin instance is in a state the note
         documents -- still pinning (reads the ledger AND asserts
         load_bearing_step_class equality), or narrowed per section 4 to a
         report-only read;
  [C2]   the named exact-state-pin instance is likewise in a documented
         state (exact-state pins, or narrowed);
  [EX]   the named compliant exemplars are in a state the note records;
  [CTL]  the production source-state classifier rejects formatting variants,
         comment-only placeholders, wrong field values, and unhandled pins;
  [CEN]  every named instance is accounted for against a live census scan of
         scripts/ (census printed as context; the count itself is NOT pinned,
         per the note's own H4).

The C1/C2/EX checks assert documented STATES rather than one frozen literal:
a runner pinning another file's current text goes stale by construction in
exactly the way the note says a ledger-field pin does -- which is how the
2026-07-02 tier-exact exemplar pin died when that file was rewritten on
2026-07-16. Accepting either documented state also keeps this runner from
freezing the named instances against section 4's own remediation path.

Deterministic, no randomness, seconds. Exits non-zero on any FAIL.
"""

from __future__ import annotations

import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "docs/RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md",
    "scripts/frontier_thales_right_angle_narrow.py",
    "scripts/frontier_half_plane_chart_equivalence_narrow.py",
    "scripts/frontier_ckm_magnitudes_structural_counts_narrow.py",
    "scripts/frontier_z3_conjugate_support_trichotomy_narrow.py",
    "scripts/audit_companion_ckm_bernoulli_two_ninths_exact.py",
    "scripts/audit_companion_dm_neutrino_cascade_geometry_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_character_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_circulant_nogo_exact.py",
    "scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py",
    "scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py",
    "scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py",
    "scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py",
    "scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    verdict = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}] {verdict}: {label}{suffix}")


def src(rel: str) -> str:
    p = ROOT / rel
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return ""


C1_INSTANCES = [
    # named from the proposal-time sweep
    "scripts/frontier_thales_right_angle_narrow.py",
    "scripts/frontier_half_plane_chart_equivalence_narrow.py",
    "scripts/frontier_ckm_magnitudes_structural_counts_narrow.py",
    "scripts/frontier_z3_conjugate_support_trichotomy_narrow.py",
    # added by the 2026-07-24 re-measurement of the same pattern
    "scripts/audit_companion_ckm_bernoulli_two_ninths_exact.py",
    "scripts/audit_companion_dm_neutrino_cascade_geometry_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_character_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_circulant_nogo_exact.py",
    "scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py",
]
C2_INSTANCE = "scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py"
EX_MEMBERSHIP = "scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py"
EX_TIER_EXACT = "scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py"
EX_REALIGNED = "scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py"

RETAINED_GRADES = frozenset({"retained", "retained_bounded", "retained_no_go"})
AUDIT_STATUS_LITERALS = frozenset({
    "retained",
    "retained_bounded",
    "retained_no_go",
    "unaudited",
    "audit_in_progress",
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
    "retained_pending_chain",
    "open_gate",
})
REPORT_CALLS = frozenset({"check", "print", "record"})


@dataclass(frozen=True)
class SourceFacts:
    parse_error: str | None
    reads_ledger: bool
    field_accesses: frozenset[str]
    reported_fields: frozenset[str]
    field_comparisons: tuple[tuple[str, str, str], ...]
    exact_status_comparisons: tuple[tuple[str, str], ...]
    status_sets: tuple[frozenset[str], ...]
    has_membership_compare: bool


def _call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _string_literal(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _field_access(node: ast.AST) -> str | None:
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "get"
        and node.args
    ):
        return _string_literal(node.args[0])
    if isinstance(node, ast.Subscript):
        return _string_literal(node.slice)
    return None


def analyze_source(text: str) -> SourceFacts:
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        return SourceFacts(
            parse_error=f"{exc.msg} at line {exc.lineno}",
            reads_ledger=False,
            field_accesses=frozenset(),
            reported_fields=frozenset(),
            field_comparisons=(),
            exact_status_comparisons=(),
            status_sets=(),
            has_membership_compare=False,
        )

    nodes = list(ast.walk(tree))
    string_literals = {
        value
        for node in nodes
        if (value := _string_literal(node)) is not None
    }
    symbol_names = {
        name
        for node in nodes
        if (name := _call_name(node)) is not None
    }
    reads_ledger = (
        any(
            "audit_ledger.json" in value
            or "docs/audit/data/ledger/" in value
            for value in string_literals
        )
        or "ledger_io" in symbol_names
        or "ledger_status" in symbol_names
    )

    field_accesses = {
        field
        for node in nodes
        if (field := _field_access(node)) is not None
    }
    reported_fields: set[str] = set()
    for node in nodes:
        if not isinstance(node, ast.Call):
            continue
        call_name = _call_name(node.func)
        if call_name not in REPORT_CALLS:
            continue
        if call_name == "print":
            report_nodes = [*node.args, *(keyword.value for keyword in node.keywords)]
        else:
            # `check`/`record` predicates are assertions, not reports. Only
            # their explicit diagnostic detail is a report-only field use.
            report_nodes = [
                *node.args[2:],
                *(
                    keyword.value
                    for keyword in node.keywords
                    if keyword.arg == "detail"
                ),
            ]
        reported_fields.update(
            field
            for report_node in report_nodes
            for child in ast.walk(report_node)
            if (field := _field_access(child)) is not None
        )

    field_comparisons: set[tuple[str, str, str]] = set()
    exact_status_comparisons: set[tuple[str, str]] = set()
    has_membership_compare = False
    for node in nodes:
        if not isinstance(node, ast.Compare):
            continue
        operands = [node.left, *node.comparators]
        for left, op, right in zip(operands, node.ops, operands[1:]):
            if isinstance(op, ast.In):
                has_membership_compare = True
            if isinstance(op, ast.Eq):
                operator = "=="
            elif isinstance(op, ast.NotEq):
                operator = "!="
            else:
                continue
            left_field = _field_access(left)
            right_field = _field_access(right)
            left_literal = _string_literal(left)
            right_literal = _string_literal(right)
            if left_field is not None and right_literal is not None:
                field_comparisons.add((left_field, operator, right_literal))
            if right_field is not None and left_literal is not None:
                field_comparisons.add((right_field, operator, left_literal))
            for literal in (left_literal, right_literal):
                if literal in AUDIT_STATUS_LITERALS:
                    exact_status_comparisons.add((operator, literal))

    status_sets: set[frozenset[str]] = set()
    for node in nodes:
        if not isinstance(node, ast.Set):
            continue
        values = [_string_literal(element) for element in node.elts]
        if values and all(value is not None for value in values):
            status_sets.add(frozenset(value for value in values if value is not None))

    return SourceFacts(
        parse_error=None,
        reads_ledger=reads_ledger,
        field_accesses=frozenset(field_accesses),
        reported_fields=frozenset(reported_fields),
        field_comparisons=tuple(sorted(field_comparisons)),
        exact_status_comparisons=tuple(sorted(exact_status_comparisons)),
        status_sets=tuple(sorted(status_sets, key=lambda values: sorted(values))),
        has_membership_compare=has_membership_compare,
    )


def analyze_path(rel: str) -> SourceFacts | None:
    text = src(rel)
    return analyze_source(text) if text else None


def field_comparison_values(
    facts: SourceFacts,
    field: str,
) -> frozenset[tuple[str, str]]:
    return frozenset(
        (operator, value)
        for key, operator, value in facts.field_comparisons
        if key == field
    )


def has_status_membership(
    facts: SourceFacts,
    required: frozenset[str],
) -> bool:
    return (
        facts.has_membership_compare
        and any(required <= values for values in facts.status_sets)
    )


def classify_c1(facts: SourceFacts | None) -> str:
    if facts is None:
        return "gone"
    if facts.parse_error is not None:
        return f"syntax-error: {facts.parse_error}"
    comparisons = field_comparison_values(facts, "load_bearing_step_class")
    if facts.reads_ledger and comparisons == {("==", "A")}:
        return "pins"
    if (
        facts.reads_ledger
        and "load_bearing_step_class" in facts.reported_fields
        and not comparisons
    ):
        return "narrowed"
    if comparisons:
        return f"undocumented field comparison {sorted(comparisons)}"
    return "unhandled"


def classify_c2(facts: SourceFacts | None) -> str:
    if facts is None:
        return "gone"
    if facts.parse_error is not None:
        return f"syntax-error: {facts.parse_error}"
    legacy = frozenset({
        ("==", "open_gate"),
        ("==", "audited_conditional"),
    })
    comparisons = frozenset(facts.exact_status_comparisons)
    if facts.reads_ledger and comparisons == legacy:
        return "exact-state pins, as named in 2026-07-02"
    if comparisons:
        return (
            "undocumented exact status comparison "
            f"{sorted(comparisons)}"
        )
    if (
        facts.reads_ledger
        and (
            "effective_status" in facts.reported_fields
            or has_status_membership(facts, RETAINED_GRADES)
        )
    ):
        return "narrowed (report-only or retained-grade membership)"
    return "unhandled"


def main() -> int:
    print("runner ledger-field pin hygiene convention check (2026-07-02)")
    note = NOTE.read_text(encoding="utf-8")

    # [NOTE] proposal disclaimers and clauses
    for phrase in [
        "**Type:** meta",
        "**Claim type:** meta",
        "metadata proposal only",
        "does not set or predict an audit outcome",
        "independent audit lane determines whether the convention is adopted",
        "(H1) No equality pins on audit-authored field content",
        "(H2) Status freshness checks use the retained-grade membership set",
        "(H3) Report-only ledger reads are unrestricted",
        "(H4) Ledger-census snapshots need a maintenance pattern",
        "Sets, promotes, or changes **no** row's effective status",
        "Neither a question to the owner nor landing this note adopts the convention",
        "cache fingerprint binds this note and every named C1/C2/EX source",
        "census count is deliberately contextual rather than load-bearing",
    ]:
        check("NOTE", f"note contains: {phrase.splitlines()[0]}",
              re.search(r"\s+".join(re.escape(w) for w in phrase.split()), note) is not None)

    # [C1] named field-content-pin instances, in either documented state.
    # Per the note's section 4 these get narrowed to report-only prints in
    # follow-up repair PRs, so pinning "still pins" here would freeze the class
    # against its own remediation path. Passing states: "pins" (as described)
    # and "narrowed" (field read, no equality pin). A file that vanished, or
    # that stopped handling the field entirely, is not a documented state.
    states: dict[str, str] = {}
    for rel in C1_INSTANCES:
        facts = analyze_path(rel)
        base = rel.split("/")[-1]
        state = classify_c1(facts)
        states[rel] = state
        named = base in note
        why = state if state in ("pins", "narrowed") else f"UNDOCUMENTED STATE {state}"
        if not named:
            why += "; NOT NAMED IN NOTE"
        check("C1", base, state in ("pins", "narrowed") and named, why)
    tally = {s: sum(1 for v in states.values() if v == s) for s in sorted(set(states.values()))}
    print(f"  C1 states: {tally}")

    # [C2] the named exact-state-pin instance, in either documented state
    # (section 4 narrows it to membership checks or a justified exception).
    c2_state = classify_c2(analyze_path(C2_INSTANCE))
    c2_allowed = (
        c2_state == "exact-state pins, as named in 2026-07-02"
        or c2_state.startswith("narrowed ")
    )
    check("C2", "extensivity runner state + named in note",
          c2_allowed and C2_INSTANCE.split("/")[-1] in note, c2_state)

    # [EX] compliant exemplars
    facts = analyze_path(EX_MEMBERSHIP)
    check("EX", "lh_doublet companion uses the retained-grade membership set",
          facts is not None and has_status_membership(facts, RETAINED_GRADES))
    # The 2026-07-02 tier-exact exemplar was rewritten on 2026-07-16 and its
    # ledger reads removed, so the note records both states rather than the
    # literal that happened to hold when it was written.
    facts = analyze_path(EX_TIER_EXACT)
    if facts is None:
        state = "gone"
    elif facts.parse_error is not None:
        state = f"syntax-error: {facts.parse_error}"
    elif (
        facts.reads_ledger
        and ("==", "retained_bounded") in facts.exact_status_comparisons
    ):
        state = "tier-exact pin, as named in 2026-07-02"
    elif not facts.reads_ledger:
        state = "no ledger read (repaired 2026-07-16)"
    else:
        state = "UNDOCUMENTED: reads ledger, no tier-exact pin"
    check("EX", "staggered substep-1 check is in a state the note records",
          state.startswith(("tier-exact", "no ledger")), state)
    facts = analyze_path(EX_REALIGNED)
    check("EX", "dirac_weyl companion carries the realigned retained-grade set",
          facts is not None
          and has_status_membership(
              facts,
              frozenset({"retained", "retained_bounded"}),
          ))

    # [CTL] Production-classifier controls. These are deliberately synthetic:
    # they verify that formatting variants are recognized and that comments,
    # placeholders, unhandled exact pins, and wrong field values cannot pass.
    expected_input_paths = {
        NOTE.relative_to(ROOT).as_posix(),
        *C1_INSTANCES,
        C2_INSTANCE,
        EX_MEMBERSHIP,
        EX_TIER_EXACT,
        EX_REALIGNED,
    }
    check(
        "CTL",
        "cache fingerprint covers the note and every named source exactly once",
        set(AUDIT_INPUT_PATHS) == expected_input_paths
        and len(AUDIT_INPUT_PATHS) == len(expected_input_paths),
    )
    c1_pins = analyze_source("""
from pathlib import Path
row = {}
ledger = Path("docs/audit/data/audit_ledger.json")
print(row.get("load_bearing_step_class"))
assert "A" == row["load_bearing_step_class"]
""")
    c1_narrowed = analyze_source("""
from pathlib import Path
row = {}
ledger = Path("docs/audit/data/audit_ledger.json")
print(row.get("load_bearing_step_class"))
""")
    c1_comment_only = analyze_source("""
# docs/audit/data/audit_ledger.json
# print(row.get("load_bearing_step_class"))
pass
""")
    c1_exact_inequality = analyze_source("""
from pathlib import Path
row = {}
ledger = Path("docs/audit/data/audit_ledger.json")
print(row.get("load_bearing_step_class"))
assert row.get("load_bearing_step_class") != "A"
""")
    c2_legacy_single_quotes = analyze_source("""
import ledger_io
row = ledger_io.load_ledger()["rows"]["example"]
assert row.get("effective_status") == 'open_gate'
assert row.get("audit_status") == 'audited_conditional'
""")
    c2_narrowed = analyze_source("""
import ledger_io
row = ledger_io.load_ledger()["rows"]["example"]
check("context", True, detail=f"{row.get('effective_status')!r}")
""")
    c2_membership = analyze_source("""
import ledger_io
row = ledger_io.load_ledger()["rows"]["example"]
retained_grades = {"retained", "retained_bounded", "retained_no_go"}
assert row.get("effective_status") in retained_grades
""")
    c2_placeholder = analyze_source("pass")
    c2_other_exact = analyze_source("""
import ledger_io
row = ledger_io.load_ledger()["rows"]["example"]
assert row.get("effective_status") != "retained"
""")
    c2_comment_only = analyze_source("""
# import ledger_io
# row.get("effective_status") == "open_gate"
pass
""")
    controls = [
        ("C1 reversed/single-quoted legacy pin is detected",
         classify_c1(c1_pins) == "pins"),
        ("C1 report-only narrowed state is accepted",
         classify_c1(c1_narrowed) == "narrowed"),
        ("C1 comment-only placeholder is rejected",
         classify_c1(c1_comment_only) == "unhandled"),
        ("C1 exact-inequality variant is rejected",
         classify_c1(c1_exact_inequality).startswith("undocumented field comparison")),
        ("C2 single-quoted legacy pair is detected",
         classify_c2(c2_legacy_single_quotes)
         == "exact-state pins, as named in 2026-07-02"),
        ("C2 report-only narrowed state is accepted",
         classify_c2(c2_narrowed).startswith("narrowed ")),
        ("C2 retained-grade membership state is accepted",
         classify_c2(c2_membership).startswith("narrowed ")),
        ("C2 unhandled placeholder is rejected",
         classify_c2(c2_placeholder) == "unhandled"),
        ("C2 other exact status comparison is rejected",
         classify_c2(c2_other_exact).startswith("undocumented exact status")),
        ("C2 comment-only placeholder is rejected",
         classify_c2(c2_comment_only) == "unhandled"),
    ]
    for label, ok in controls:
        check("CTL", label, ok)

    # [CEN] census: ledger-reading scripts with equality pins (context print).
    # Per (H4) the count is printed, never pinned. The per-file listing is
    # omitted: the C1 inventory above names the field-content-pin members,
    # which is the subpopulation the note's section 1 is about.
    census = []
    field_pins = 0
    for p in sorted((ROOT / "scripts").glob("*.py")):
        if p.name == Path(__file__).name:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        # Keep the repo-wide scan sub-second in the common case: only parse
        # files that textually mention both a ledger access route and a field
        # or status token that could participate in a pin. The AST remains the
        # authority for classification, so comments cannot create a PASS.
        if not any(
            token in text
            for token in (
                "audit_ledger.json",
                "docs/audit/data/ledger/",
                "ledger_io",
                "ledger_status",
            )
        ):
            continue
        if (
            "load_bearing_step_class" not in text
            and not any(status in text for status in AUDIT_STATUS_LITERALS)
        ):
            continue
        facts = analyze_source(text)
        equality_pin = bool(
            facts.field_comparisons
            or facts.exact_status_comparisons
            or frozenset({"retained"}) in facts.status_sets
        )
        if facts.parse_error is None and facts.reads_ledger and equality_pin:
            census.append(f"scripts/{p.name}")
            if field_comparison_values(facts, "load_bearing_step_class"):
                field_pins += 1
    print(f"  census: {len(census)} ledger-reading scripts with equality-pin patterns; "
          f"{field_pins} carry the load_bearing_step_class field pin (context, not pinned)")
    # A named instance LEAVES this census when section 4 narrows it, so the
    # invariant is accounted-for, not present: either still in the census, or
    # still on disk with the pin removed. Only a vanished file is unaccounted.
    unaccounted = sorted(
        [
            rel
            for rel, state in states.items()
            if state not in {"pins", "narrowed"}
            or (state == "pins" and rel not in census)
        ]
        + (
            [C2_INSTANCE]
            if (
                not c2_allowed
                or (
                    c2_state == "exact-state pins, as named in 2026-07-02"
                    and C2_INSTANCE not in census
                )
            )
            else []
        )
    )
    check("CEN", "every named instance accounted for (in census, or narrowed on disk)",
          not unaccounted, "unaccounted: " + ", ".join(unaccounted) if unaccounted else "")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
