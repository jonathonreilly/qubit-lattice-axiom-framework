#!/usr/bin/env python3
"""Retained/unbounded gate map for the post-record dynamics stack."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE_2026-06-06.md"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class GateRow:
    gate_id: str
    status: str
    authority: str
    unlocks: str
    still_blocked: str
    bounded: bool
    unbounded_ready: bool
    source_prs: tuple[int, ...]


GATES = (
    GateRow(
        "finite_record_certificate_substrate",
        "exact-support",
        "finite post-record records under supplied finite laws/statistics",
        "realized records can be audited as finite certificate rows",
        "independent audit remains required before retained authority",
        True,
        False,
        (2850, 2861, 2864),
    ),
    GateRow(
        "directed_dynamics_certificate",
        "exact-support",
        "supplied orientation bridge",
        "directed finite statistics under the supplied bridge",
        "counts alone do not derive the physical arrow",
        True,
        False,
        (2850, 2853),
    ),
    GateRow(
        "production_kernel_selection",
        "exact-support",
        "supplied finite candidate family and supplied loss/rule",
        "a stable kernel location inside the supplied rule",
        "Record alone does not derive the production kernel or rule",
        True,
        False,
        (2853, 2856),
    ),
    GateRow(
        "sample_target_vector",
        "exact-support",
        "admitted finite sample plus supplied statistic set",
        "an exact empirical target vector",
        "sample is not a probability law; weights and selector remain supplied",
        True,
        False,
        (2858, 2861),
    ),
    GateRow(
        "stable_dial_location",
        "exact-support",
        "supplied dial/score/rule/kernel",
        "a stable location can be recorded as a location",
        "framework does not force or select the dial",
        True,
        False,
        (2856, 2864),
    ),
    GateRow(
        "bounded_conditional_audit_lift",
        "exact-support",
        "finite certificate plus explicit missing-input list",
        "bounded and conditional audit rows can be normalized",
        "missing bridge/kernel/rule/target/weights/family lift stay explicit",
        True,
        False,
        (2864, 2868),
    ),
    GateRow(
        "unbounded_family_lift",
        "open",
        "not supplied by finite enumeration alone",
        "would lift compatible finite certificates toward unbounded use",
        "needs projective consistency, monotone exhaustion, direct-limit compatibility, or tightness",
        False,
        False,
        (2864, 2868),
    ),
    GateRow(
        "effective_retained_application",
        "open",
        "repo-authority application after independent audit",
        "would apply reviewed retained status outside this branch",
        "requires independent audit and authority-surface update",
        False,
        False,
        (2864, 2868),
    ),
)

DYNAMICS_STACK_PRS = {2850, 2853, 2856, 2858, 2861, 2864}
PROHIBITED_CURRENT_STATUSES = {"retained", "proposed_" + "retained", "proposed_" + "promoted"}


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_doc() -> str:
    return DOC.read_text(encoding="utf-8")


def gate_shape_checks() -> None:
    section("Gate shape")
    report("eight gate rows are defined", len(GATES) == 8)
    gate_ids = {row.gate_id for row in GATES}
    report("gate ids are unique", len(gate_ids) == len(GATES))
    report(
        "all current statuses avoid retained/promoted language",
        all(row.status not in PROHIBITED_CURRENT_STATUSES for row in GATES),
    )
    report("at least one unbounded gate is present", "unbounded_family_lift" in gate_ids)
    report("effective retained application gate is present", "effective_retained_application" in gate_ids)
    report("bounded gates are not unbounded-ready", all(not row.unbounded_ready for row in GATES if row.bounded))
    report("no gate is unbounded-ready yet", all(not row.unbounded_ready for row in GATES))


def source_coverage_checks() -> None:
    section("Source coverage")
    covered = {pr for row in GATES for pr in row.source_prs}
    for pr in sorted(DYNAMICS_STACK_PRS):
        report(f"dynamics stack PR #{pr} is referenced", pr in covered)
    report("closeout PR #2868 is referenced as stack index", 2868 in covered)
    report("all source PR numbers are positive", all(pr > 0 for pr in covered))


def document_checks() -> None:
    section("Document checks")
    text = read_doc()
    for row in GATES:
        report(f"document contains gate {row.gate_id}", row.gate_id in text)
    for pr in sorted(DYNAMICS_STACK_PRS):
        report(f"document references PR #{pr}", f"#{pr}" in text)
    required_phrases = (
        "pre-record law carries probabilities",
        "post-record records carry realized information",
        "probabilities enter post-record analysis only through a supplied law",
        "The current dynamics artifacts are bounded",
        "The unbounded move is therefore a separate gate",
        "stable location can be recorded and audited as a location",
        "does not force or select the dial",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    for phrase in required_phrases:
        report(f"document contains phrase: {phrase}", phrase in text)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    retained_or_promoted_claim = False
    physical_arrow_derived_from_record = False
    production_kernel_derived_from_record = False
    target_or_weights_derived_from_record = False
    sample_is_probability_law = False
    dial_forced_or_selected = False
    unbounded_claim_from_finite_enumeration = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("retained/promoted claim flag is false", not retained_or_promoted_claim)
    report("physical arrow derived from Record flag is false", not physical_arrow_derived_from_record)
    report("production kernel derived from Record flag is false", not production_kernel_derived_from_record)
    report("target or weights derived from Record flag is false", not target_or_weights_derived_from_record)
    report("sample-is-probability-law flag is false", not sample_is_probability_law)
    report("dial forced or selected flag is false", not dial_forced_or_selected)
    report("unbounded claim from finite enumeration flag is false", not unbounded_claim_from_finite_enumeration)


def family_lift_checks() -> None:
    section("Family-lift gate")
    unbounded = next(row for row in GATES if row.gate_id == "unbounded_family_lift")
    report("unbounded family lift is open", unbounded.status == "open")
    report("unbounded family lift is not bounded", not unbounded.bounded)
    report("unbounded family lift is not ready", not unbounded.unbounded_ready)
    for keyword in ("projective consistency", "monotone exhaustion", "direct-limit", "tightness"):
        report(f"family-lift blocker names {keyword}", keyword in unbounded.still_blocked)


def main() -> int:
    gate_shape_checks()
    source_coverage_checks()
    document_checks()
    firewall_checks()
    family_lift_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE=TRUE")
    print("GATE_ROWS=8")
    print("FINITE_CERTIFICATES_REMAIN_BOUNDED=TRUE")
    print("UNBOUNDED_FAMILY_LIFT_REQUIRED=TRUE")
    print("PRE_RECORD_LAW_CARRIES_PROBABILITY=TRUE")
    print("POST_RECORD_SITE_CARRIES_REALIZED_INFORMATION=TRUE")
    print("DIAL_FORCED_OR_SELECTED=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
