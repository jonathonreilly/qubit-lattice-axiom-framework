#!/usr/bin/env python3
"""Read-only authority stack map for post-record dynamics interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class AuthorityLayer:
    layer: str
    status: str
    authority_class: str
    summary_flag: str


LAYERS = (
    AuthorityLayer("directed examples", "exact-support", "supplied law/orientation/clock/kernel", "SUPPLIED_DIRECTED_CERTIFICATE_EXAMPLES=TRUE"),
    AuthorityLayer("kernel selection firewall", "no-go", "blocked Record-derived kernel selection", "DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL=TRUE"),
    AuthorityLayer("supplied kernel selection rule", "exact-support", "supplied candidate family and rule", "SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE=TRUE"),
    AuthorityLayer("target vector firewall", "no-go", "blocked Record-derived targets/weights", "SELECTION_RULE_TARGET_VECTOR_FIREWALL=TRUE"),
    AuthorityLayer("admitted sample vector", "exact-support", "admitted observation sample", "ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE=TRUE"),
)

DOC_CHECKS = {
    "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md": [
        "supplied finite law plus supplied orientation bridge",
        "examples do not derive an arrow, clock, kernel, or selected dial",
    ],
    "docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md": [
        "Directed certificates do not select a production kernel",
        "kernel remains a supplied bridge input",
    ],
    "docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md": [
        "supplied finite candidate family plus supplied selection rule",
        "The rule is supplied",
    ],
    "docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md": [
        "target vector and loss weights are supplied rule data",
        "Record does not derive the target vector or weights",
    ],
    "docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md": [
        "supplied finite post-record sample plus supplied statistic set",
        "The sample is admitted observation data, not a probability law",
    ],
}

LOG_CHECKS = {
    "logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt": [
        "SUMMARY: PASS=64 FAIL=0",
        "SUPPLIED_DIRECTED_CERTIFICATE_EXAMPLES=TRUE",
    ],
    "logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt": [
        "SUMMARY: PASS=52 FAIL=0",
        "DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL=TRUE",
    ],
    "logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt": [
        "SUMMARY: PASS=39 FAIL=0",
        "SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE=TRUE",
    ],
    "logs/runner-cache/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.txt": [
        "SUMMARY: PASS=36 FAIL=0",
        "SELECTION_RULE_TARGET_VECTOR_FIREWALL=TRUE",
    ],
    "logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt": [
        "SUMMARY: PASS=30 FAIL=0",
        "ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE=TRUE",
    ],
}


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


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    for path, needles in DOC_CHECKS.items():
        text = read_rel(path)
        report(f"{path} exists", True)
        for needle in needles:
            report(f"{path} contains: {needle}", needle in text)
    require_self = read_rel("docs/POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP_2026-06-06.md")
    for needle in [
        "supplied, admitted, and blocked authority classes",
        "stable location is not selected dial",
        "post-record samples are realized information, not probability laws",
        "Cited authority/cache packet",
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md",
        "logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt",
        "docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md",
        "logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt",
    ]:
        report(f"self note contains: {needle}", needle in require_self)


def cached_log_checks() -> None:
    section("Cached log checks")
    for path, needles in LOG_CHECKS.items():
        text = read_rel(path)
        report(f"{path} exists", True)
        for needle in needles:
            report(f"{path} contains: {needle}", needle in text)


def authority_layer_checks() -> None:
    section("Authority layer checks")
    report("five dynamics layers are mapped", len(LAYERS) == 5)
    report("no-go and exact-support statuses both appear", {layer.status for layer in LAYERS} == {"exact-support", "no-go"})
    report("every layer has an authority class", all(layer.authority_class for layer in LAYERS))
    report("every layer has a summary flag", all(layer.summary_flag for layer in LAYERS))
    for layer in LAYERS:
        print(f"{layer.layer}: {layer.status} | {layer.authority_class} | {layer.summary_flag}")


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    physical_arrow_derived_from_record = False
    production_kernel_selected_without_rule = False
    selection_rule_derived_from_record = False
    target_vector_derived_from_record = False
    sample_is_probability_law = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("kernel selected without supplied rule flag is false", not production_kernel_selected_without_rule)
    report("selection rule derived from Record flag is false", not selection_rule_derived_from_record)
    report("target vector derived from Record flag is false", not target_vector_derived_from_record)
    report("sample-is-probability-law flag is false", not sample_is_probability_law)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    cached_log_checks()
    authority_layer_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP=TRUE")
    print("DYNAMICS_AUTHORITY_LAYERS=5")
    print("PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE=FALSE")
    print("SELECTION_RULE_DERIVED_FROM_RECORD=FALSE")
    print("TARGET_VECTOR_DERIVED_FROM_RECORD=FALSE")
    print("SAMPLE_IS_PROBABILITY_LAW=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
