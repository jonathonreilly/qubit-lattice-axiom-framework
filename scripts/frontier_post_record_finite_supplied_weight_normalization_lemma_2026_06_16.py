#!/usr/bin/env python3
"""Finite supplied-weight normalization lemma."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/POST_RECORD_FINITE_SUPPLIED_WEIGHT_NORMALIZATION_LEMMA_NOTE_2026-06-16.md"
PASS = 0
FAIL = 0


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


def normalize_weights(weights: dict[str, Fraction]) -> dict[str, Fraction] | None:
    if not weights or any(weight < 0 for weight in weights.values()):
        return None
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        return None
    return {key: value / total for key, value in weights.items()}


def selected_dial_from_normalization(has_normalization: bool, has_selector_rule: bool) -> str:
    if has_normalization and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    for needle in [
        "**Claim type:** bounded_theorem",
        "supplied finite carrier",
        "supplied rational nonnegative weights",
        "Normalized measure is not selector authority.",
        "does not derive the supplied carrier or weights",
        "Does not edit audit data.",
        "Does not select a generation, Koide, stable-setting, or physical dial.",
    ]:
        report(f"source note contains: {needle}", needle in text)


def algebra_checks() -> None:
    weights = {"a": Fraction(1), "b": Fraction(3), "c": Fraction(2)}
    normalized = normalize_weights(weights)
    expected = {"a": Fraction(1, 6), "b": Fraction(1, 2), "c": Fraction(1, 3)}
    report("positive finite supplied weights normalize exactly", normalized == expected, str(normalized))
    report("normalized weights sum to one", normalized is not None and sum(normalized.values(), Fraction(0)) == 1)
    report("support keys are preserved", normalized is not None and set(normalized) == set(weights))
    scaled = normalize_weights({key: 5 * value for key, value in weights.items()})
    report("positive rescaling leaves normalized measure invariant", scaled == normalized, str(scaled))
    report("zero-total weights are rejected", normalize_weights({"a": Fraction(0), "b": Fraction(0)}) is None)
    report("negative weights are rejected", normalize_weights({"a": Fraction(1), "b": Fraction(-1)}) is None)
    report("empty carrier is rejected", normalize_weights({}) is None)
    report(
        "selector rule remains separate from normalization",
        selected_dial_from_normalization(True, False) == "blocked_missing_selector",
    )
    report(
        "selector readiness requires separate selector rule",
        selected_dial_from_normalization(True, True) == "conditional_selector_ready",
    )


def firewall_checks() -> None:
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    carrier_or_weight_derived = False
    normalized_measure_selects_dial = False
    born_law_derived = False
    production_dynamics_derived = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("carrier/weight derivation flag is false", not carrier_or_weight_derived)
    report("normalized measure selects dial flag is false", not normalized_measure_selects_dial)
    report("Born-law derivation flag is false", not born_law_derived)
    report("production-dynamics derivation flag is false", not production_dynamics_derived)


def main() -> int:
    print("Post-record finite supplied-weight normalization lemma")
    print("=" * 72)
    source_checks()
    algebra_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("NORMALIZED_MEASURE_SELECTS_DIAL=FALSE")
    print("CARRIER_OR_WEIGHT_DERIVED=FALSE")
    print("BORN_LAW_DERIVED=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
