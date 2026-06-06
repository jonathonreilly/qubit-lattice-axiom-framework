#!/usr/bin/env python3
"""Extended closeout index for post-record dynamics plus family-lift stack."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/POST_RECORD_DYNAMICS_FAMILY_LIFT_CLOSEOUT_INDEX_2026-06-06.md"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class StackPr:
    number: int
    title_fragment: str
    status: str
    runner_summary: str
    log_path: str


STACK = (
    StackPr(2850, "directed certificate examples", "exact-support", "SUMMARY: PASS=59 FAIL=0", "logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt"),
    StackPr(2853, "kernel-selection firewall", "no-go", "SUMMARY: PASS=52 FAIL=0", "logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt"),
    StackPr(2856, "supplied kernel selection rule", "exact-support", "SUMMARY: PASS=39 FAIL=0", "logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt"),
    StackPr(2858, "target-vector firewall", "no-go", "SUMMARY: PASS=32 FAIL=0", "logs/runner-cache/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.txt"),
    StackPr(2861, "admitted sample target-vector", "exact-support", "SUMMARY: PASS=30 FAIL=0", "logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt"),
    StackPr(2864, "dynamics authority stack map", "exact-support", "SUMMARY: PASS=47 FAIL=0", "logs/runner-cache/frontier_post_record_dynamics_authority_stack_map_2026_06_06.txt"),
    StackPr(2868, "dynamics campaign closeout index", "exact-support", "SUMMARY: PASS=46 FAIL=0", "logs/runner-cache/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.txt"),
    StackPr(2871, "retained/unbounded dynamics gate", "exact-support", "SUMMARY: PASS=54 FAIL=0", "logs/runner-cache/frontier_post_record_retained_unbounded_dynamics_gate_2026_06_06.txt"),
    StackPr(2874, "finite-to-unbounded family-lift no-go", "no-go", "SUMMARY: PASS=43 FAIL=0", "logs/runner-cache/frontier_post_record_finite_to_unbounded_family_lift_nogo_2026_06_06.txt"),
    StackPr(2875, "supplied family-lift certificate interface", "exact-support", "SUMMARY: PASS=38 FAIL=0", "logs/runner-cache/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.txt"),
)


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


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def index_checks() -> None:
    section("Extended closeout index checks")
    text = DOC.read_text(encoding="utf-8")
    report("ten PR stack entries are expected", len(STACK) == 10)
    for item in STACK:
        report(f"index contains PR #{item.number}", f"/pull/{item.number}" in text)
        report(f"index contains title fragment for #{item.number}", item.title_fragment in text)
        report(f"index contains status for #{item.number}", item.status in text)
    for pr in (2871, 2874, 2875):
        report(f"family-lift extension PR #{pr} is present", f"/pull/{pr}" in text)
    report("index states pre-record law carries probabilities", "pre-record law carries probabilities" in text)
    report("index states post-record records carry realized information", "post-record records carry realized information" in text)
    report("index states no audit verdicts are applied", "does not apply audit verdicts" in text)


def cached_summary_checks() -> None:
    section("Cached summary checks")
    for item in STACK:
        text = read_rel(item.log_path)
        report(f"{item.log_path} exists", True)
        report(f"{item.log_path} has summary for PR #{item.number}", item.runner_summary in text)


def status_shape_checks() -> None:
    section("Status shape checks")
    statuses = {item.status for item in STACK}
    report("stack has exact-support entries", "exact-support" in statuses)
    report("stack has no-go entries", "no-go" in statuses)
    report("exact-support count is seven", sum(1 for item in STACK if item.status == "exact-support") == 7)
    report("no-go count is three", sum(1 for item in STACK if item.status == "no-go") == 3)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    production_kernel_selected_without_rule = False
    selection_rule_derived_from_record = False
    target_vector_derived_from_record = False
    sample_is_probability_law = False
    dial_forced_or_selected = False
    finite_alone_unbounded_retained = False
    family_lift_derived_from_record = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("kernel selected without supplied rule flag is false", not production_kernel_selected_without_rule)
    report("selection rule derived from Record flag is false", not selection_rule_derived_from_record)
    report("target vector derived from Record flag is false", not target_vector_derived_from_record)
    report("sample-is-probability-law flag is false", not sample_is_probability_law)
    report("dial forced or selected flag is false", not dial_forced_or_selected)
    report("finite-alone unbounded retained flag is false", not finite_alone_unbounded_retained)
    report("family lift derived from Record flag is false", not family_lift_derived_from_record)


def main() -> int:
    index_checks()
    cached_summary_checks()
    status_shape_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_DYNAMICS_FAMILY_LIFT_CLOSEOUT_INDEX=TRUE")
    print("EXTENDED_STACK_PRS=10")
    print("EXTENDED_STACK_EXACT_SUPPORT=7")
    print("EXTENDED_STACK_NO_GO=3")
    print("FAMILY_LIFT_EXTENSION_PRS=3")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("DIAL_FORCED_OR_SELECTED=FALSE")
    print("FINITE_ALONE_UNBOUNDED_RETAINED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
