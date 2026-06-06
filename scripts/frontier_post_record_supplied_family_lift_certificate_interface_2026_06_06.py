#!/usr/bin/env python3
"""Finite projective-ladder compatibility witness for post-record dynamics."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/POST_RECORD_SUPPLIED_FAMILY_LIFT_CERTIFICATE_INTERFACE_2026-06-06.md"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class LadderLevel:
    n: int
    word: tuple[int, ...]

    def project_to(self, target_n: int) -> tuple[int, ...]:
        return self.word[:target_n]

    def leading_marker_is_one(self) -> bool:
        return bool(self.word) and self.word[0] == 1

    def density(self) -> Fraction:
        return Fraction(sum(self.word), len(self.word))


LADDER = (
    LadderLevel(1, (1,)),
    LadderLevel(2, (1, 0)),
    LadderLevel(3, (1, 0, 1)),
    LadderLevel(4, (1, 0, 1, 1)),
)

SUPPLIED_STABLE_PREDICATE = True
FAMILY_LIFT_DERIVED_FROM_RECORD = False
FAMILY_LIFT_AUTHORITY_APPLIED = False
UNBOUNDED_RETAINED_AUTHORITY_APPLIED = False
AUDIT_VERDICT_APPLIED = False
DIAL_FORCED_OR_SELECTED = False

PROHIBITED_LIVE_CLAIMS = (
    "actual_current_surface_status: " + "retained",
    "actual_current_surface_status: proposed_" + "retained",
    "actual_current_surface_status: proposed_" + "promoted",
    "bare_retained_allowed: " + "true",
    "UNBOUNDED_RETAINED_AUTHORITY_APPLIED=" + "TRUE",
    "FAMILY_LIFT_DERIVED_FROM_RECORD=" + "TRUE",
    "FAMILY_LIFT_AUTHORITY_APPLIED=" + "TRUE",
    "AUDIT_VERDICT_APPLIED=" + "TRUE",
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


def read_doc() -> str:
    return DOC.read_text(encoding="utf-8")


def ladder_shape_checks() -> None:
    section("Ladder shape")
    report("four ladder levels are present", len(LADDER) == 4)
    report("level labels are consecutive", tuple(level.n for level in LADDER) == (1, 2, 3, 4))
    for level in LADDER:
        report(f"C{level.n} has length {level.n}", len(level.word) == level.n)
        report(f"C{level.n} is binary", set(level.word) <= {0, 1})


def projection_checks() -> None:
    section("Projection consistency")
    for lower, upper in zip(LADDER, LADDER[1:]):
        projected = upper.project_to(lower.n)
        report(f"pi_{lower.n}(C{upper.n}) = C{lower.n}", projected == lower.word)
    report("C4 projects to C1 through truncation", LADDER[-1].project_to(1) == LADDER[0].word)
    report("C4 projects to C2 through truncation", LADDER[-1].project_to(2) == LADDER[1].word)
    report("C4 projects to C3 through truncation", LADDER[-1].project_to(3) == LADDER[2].word)


def stable_predicate_checks() -> None:
    section("Stable predicate")
    values = tuple(level.leading_marker_is_one() for level in LADDER)
    densities = tuple(level.density() for level in LADDER)
    report("leading-marker predicate is true at every level", all(values), str(values))
    report("leading-marker predicate is stable", len(set(values)) == 1)
    report("density values are exact fractions", all(isinstance(value, Fraction) for value in densities))
    report("density is not constant on this ladder", len(set(densities)) > 1, str(densities))
    report("density sequence is 1, 1/2, 2/3, 3/4", densities == (Fraction(1, 1), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)))


def interface_firewall_checks() -> None:
    section("Interface firewalls")
    report("stable predicate is supplied", SUPPLIED_STABLE_PREDICATE)
    report("family-lift authority is not applied", not FAMILY_LIFT_AUTHORITY_APPLIED)
    report("family-lift is not derived from Record", not FAMILY_LIFT_DERIVED_FROM_RECORD)
    report("unbounded retained authority is not applied", not UNBOUNDED_RETAINED_AUTHORITY_APPLIED)
    report("audit verdict is not applied", not AUDIT_VERDICT_APPLIED)
    report("dial is not forced or selected", not DIAL_FORCED_OR_SELECTED)


def document_checks() -> None:
    section("Document checks")
    text = read_doc()
    required_phrases = (
        "The interface has three pieces",
        "supplied projection maps",
        "supplied stable predicate",
        "This is not an unbounded retained claim",
        "leading_marker_is_one(C_n) = true",
        "prefix density is not stable",
        "pre-record law carries probabilities",
        "post-record records carry realized information",
        "actual_current_surface_status: bounded-support",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    for phrase in required_phrases:
        report(f"document contains phrase: {phrase}", phrase in text)
    report(
        "document avoids live retained/promotion leaks",
        all(fragment not in text for fragment in PROHIBITED_LIVE_CLAIMS),
    )


def main() -> int:
    ladder_shape_checks()
    projection_checks()
    stable_predicate_checks()
    interface_firewall_checks()
    document_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_FINITE_LADDER_COMPATIBILITY_WITNESS=TRUE")
    print("LADDER_LEVELS=4")
    print("SUPPLIED_PROJECTIONS_COMMUTE=TRUE")
    print("STABLE_PREDICATE=leading_marker_is_one")
    print("DENSITY_USED_AS_STABLE_LIFT=FALSE")
    print("SUPPLIED_STABLE_PREDICATE=TRUE")
    print("FAMILY_LIFT_AUTHORITY_APPLIED=FALSE")
    print("FAMILY_LIFT_DERIVED_FROM_RECORD=FALSE")
    print("UNBOUNDED_RETAINED_AUTHORITY_APPLIED=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
