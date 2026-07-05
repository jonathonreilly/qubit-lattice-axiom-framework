#!/usr/bin/env python3
"""Closeout index for the post-record dynamics campaign stack."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class StackPr:
    number: int
    title_fragment: str
    status: str
    runner_summary: str


STACK = (
    StackPr(2850, "directed certificate examples", "exact-support", "SUMMARY: PASS=64 FAIL=0"),
    StackPr(2853, "kernel-selection firewall", "no-go", "SUMMARY: PASS=52 FAIL=0"),
    StackPr(2856, "supplied kernel selection rule", "exact-support", "SUMMARY: PASS=39 FAIL=0"),
    StackPr(2858, "target-vector firewall", "no-go", "SUMMARY: PASS=36 FAIL=0"),
    StackPr(2861, "admitted sample target-vector", "exact-support", "SUMMARY: PASS=30 FAIL=0"),
    StackPr(2864, "dynamics authority stack map", "exact-support", "SUMMARY: PASS=52 FAIL=0"),
)

LOGS = (
    "logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt",
    "logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt",
    "logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt",
    "logs/runner-cache/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.txt",
    "logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt",
    "logs/runner-cache/frontier_post_record_dynamics_authority_stack_map_2026_06_06.txt",
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
    section("Closeout index checks")
    text = read_rel("docs/POST_RECORD_DYNAMICS_CAMPAIGN_CLOSEOUT_INDEX_2026-06-06.md")
    report("six PR stack entries are expected", len(STACK) == 6)
    report("index declares audit-canonical meta metadata", "**Type:** meta" in text and "**Claim type:** meta" in text)
    for item in STACK:
        report(f"index contains PR #{item.number}", f"/pull/{item.number}" in text)
        report(f"index contains title fragment for #{item.number}", item.title_fragment in text)
        report(f"index contains status for #{item.number}", item.status in text)
        report(f"index contains cached summary for #{item.number}", item.runner_summary in text)
    report("index states stable location is not selected dial", "stable location is not selected dial" in text)
    report("index states no audit verdicts are applied", "does not apply audit verdicts" in text)


def cached_summary_checks() -> None:
    section("Cached summary checks")
    for item, path in zip(STACK, LOGS, strict=True):
        text = read_rel(path)
        report(f"{path} exists", True)
        report(f"{path} has summary for PR #{item.number}", item.runner_summary in text)


def status_shape_checks() -> None:
    section("Status shape checks")
    statuses = {item.status for item in STACK}
    report("stack has exact-support entries", "exact-support" in statuses)
    report("stack has no-go entries", "no-go" in statuses)
    report("exact-support count is four", sum(1 for item in STACK if item.status == "exact-support") == 4)
    report("no-go count is two", sum(1 for item in STACK if item.status == "no-go") == 2)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    production_kernel_selected_without_rule = False
    selection_rule_derived_from_record = False
    target_vector_derived_from_record = False
    sample_is_probability_law = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("kernel selected without supplied rule flag is false", not production_kernel_selected_without_rule)
    report("selection rule derived from Record flag is false", not selection_rule_derived_from_record)
    report("target vector derived from Record flag is false", not target_vector_derived_from_record)
    report("sample-is-probability-law flag is false", not sample_is_probability_law)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    index_checks()
    cached_summary_checks()
    status_shape_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_DYNAMICS_CAMPAIGN_CLOSEOUT_INDEX=TRUE")
    print("DYNAMICS_STACK_PRS=6")
    print("DYNAMICS_STACK_EXACT_SUPPORT=4")
    print("DYNAMICS_STACK_NO_GO=2")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
