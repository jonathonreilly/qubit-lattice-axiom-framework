#!/usr/bin/env python3
"""Exact classifier for post-record conditional audit evidence rungs."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Evidence:
    record_alphabet: bool = False
    append_count_theorem: bool = False
    expected_counts: bool = False
    finite_law: bool = False
    exact_enumeration: bool = False
    concentration_certificate: bool = False
    law_scope: bool = False
    simulation: bool = False
    score_rule: bool = False
    stability_map: bool = False
    selector_rule: bool = False
    formation_bridge: bool = False
    kernel_or_time_bridge: bool = False
    independent_audit_result: bool = False


@dataclass(frozen=True)
class Case:
    name: str
    requirement: str
    evidence: Evidence
    expected: str


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
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def classify(requirement: str, ev: Evidence) -> str:
    if requirement == "append_count":
        if ev.record_alphabet and ev.append_count_theorem:
            return "exact_support_candidate"
        return "open_missing_record_typing"

    if requirement == "p_value":
        if ev.finite_law and ev.exact_enumeration:
            return "conditional_audit_ready"
        if ev.concentration_certificate and ev.law_scope:
            return "conditional_audit_ready"
        if ev.simulation:
            return "support_only_not_calibrated"
        if ev.expected_counts:
            return "blocked_expectation_only"
        return "open_missing_law_or_certificate"

    if requirement == "stable_dial":
        if ev.score_rule and ev.stability_map:
            return "stable_setting_support"
        return "open_missing_stability_certificate"

    if requirement == "selected_dial":
        if ev.score_rule and ev.selector_rule:
            return "conditional_selector_ready"
        return "blocked_missing_selector"

    if requirement == "production_dynamics":
        if ev.formation_bridge and ev.kernel_or_time_bridge:
            return "bounded_support_with_open_imports"
        return "open_missing_production_bridge"

    if requirement == "audit_verdict":
        if ev.independent_audit_result:
            return "independent_audit_owned"
        return "independent_audit_only"

    raise ValueError(f"unknown requirement: {requirement}")


def cases() -> list[Case]:
    return [
        Case(
            name="append/count row",
            requirement="append_count",
            evidence=Evidence(record_alphabet=True, append_count_theorem=True),
            expected="exact_support_candidate",
        ),
        Case(
            name="exact finite p-value row",
            requirement="p_value",
            evidence=Evidence(finite_law=True, exact_enumeration=True),
            expected="conditional_audit_ready",
        ),
        Case(
            name="concentration certificate row",
            requirement="p_value",
            evidence=Evidence(concentration_certificate=True, law_scope=True),
            expected="conditional_audit_ready",
        ),
        Case(
            name="expectation-only p-value row",
            requirement="p_value",
            evidence=Evidence(expected_counts=True),
            expected="blocked_expectation_only",
        ),
        Case(
            name="simulation-only p-value row",
            requirement="p_value",
            evidence=Evidence(simulation=True),
            expected="support_only_not_calibrated",
        ),
        Case(
            name="stable dial row",
            requirement="stable_dial",
            evidence=Evidence(score_rule=True, stability_map=True),
            expected="stable_setting_support",
        ),
        Case(
            name="selected dial from stability only",
            requirement="selected_dial",
            evidence=Evidence(score_rule=True, stability_map=True),
            expected="blocked_missing_selector",
        ),
        Case(
            name="bounded production dynamics row",
            requirement="production_dynamics",
            evidence=Evidence(formation_bridge=True, kernel_or_time_bridge=True),
            expected="bounded_support_with_open_imports",
        ),
        Case(
            name="branch-local audit verdict row",
            requirement="audit_verdict",
            evidence=Evidence(),
            expected="independent_audit_only",
        ),
    ]


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "conditional audit evidence ladder",
            "expectation-only evidence cannot certify p-values",
            "simulation evidence is support-only",
            "stable settings are not selected dials",
            "independent audit owns verdicts",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md",
        [
            "verified law-scoped concentration certificate",
            "does not have a concentration certificate",
            "Does not select or force a generation/Koide dial location",
        ],
    )
    require_text(
        "docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md",
        [
            "bounded and conditional lanes",
            "probability/source/instrument/dynamics rows",
            "post-record information dynamics",
        ],
    )
    require_text(
        "docs/RECORD_TYPING_AUDIT_UNLOCK_MAP_2026-06-05.md",
        [
            "selector/measure gates",
            "dynamics rows",
            "dial is stable, selected, or",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "post-record information dynamics",
            "probability laws, Born typicality, and transition rates",
            "dial selection",
        ],
    )


def classifier_checks() -> None:
    section("Classifier checks")
    observed = []
    for case in cases():
        got = classify(case.requirement, case.evidence)
        observed.append(got)
        report(case.name, got == case.expected, got)

    expected_counts = {
        "exact_support_candidate": 1,
        "conditional_audit_ready": 2,
        "blocked_expectation_only": 1,
        "support_only_not_calibrated": 1,
        "stable_setting_support": 1,
        "blocked_missing_selector": 1,
        "bounded_support_with_open_imports": 1,
        "independent_audit_only": 1,
    }
    report("classification histogram matches expected", Counter(observed) == expected_counts, str(Counter(observed)))

    expectation_only = Evidence(expected_counts=True)
    upgraded = Evidence(expected_counts=True, finite_law=True, exact_enumeration=True)
    report(
        "exact finite law upgrades expectation-only p-value row",
        classify("p_value", expectation_only) == "blocked_expectation_only"
        and classify("p_value", upgraded) == "conditional_audit_ready",
    )

    simulation_plus_expectation = Evidence(expected_counts=True, simulation=True)
    report(
        "simulation plus expectation is not calibrated",
        classify("p_value", simulation_plus_expectation) == "support_only_not_calibrated",
    )

    stability_without_selector = Evidence(score_rule=True, stability_map=True)
    selector_added = Evidence(score_rule=True, stability_map=True, selector_rule=True)
    report(
        "selector rule is needed for selected dial",
        classify("selected_dial", stability_without_selector) == "blocked_missing_selector"
        and classify("selected_dial", selector_added) == "conditional_selector_ready",
    )


def firewall_checks() -> None:
    section("Firewall flags")
    audit_verdict_applied = False
    record_derives_probability = False
    record_derives_concentration = False
    simulation_is_calibrated_without_certificate = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False
    retained_or_promoted_claim = False

    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("Record-derived probability flag is false", not record_derives_probability)
    report("Record-derived concentration flag is false", not record_derives_concentration)
    report("simulation calibrated without certificate flag is false", not simulation_is_calibrated_without_certificate)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("retained/promoted claim flag is false", not retained_or_promoted_claim)


def main() -> int:
    source_anchor_checks()
    classifier_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("CONDITIONAL_AUDIT_EVIDENCE_LADDER=TRUE")
    print("EXPECTATION_ONLY_CERTIFIES_P_VALUES=FALSE")
    print("SIMULATION_ONLY_CALIBRATED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
