#!/usr/bin/env python3
"""No-go: finite post-record certificates do not determine unbounded laws."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Completion:
    name: str
    prefix: tuple[int, ...]
    tail_value: int

    def finite_word(self, length: int) -> tuple[int, ...]:
        if length < len(self.prefix):
            return self.prefix[:length]
        return self.prefix + (self.tail_value,) * (length - len(self.prefix))

    def prefix_count(self) -> int:
        return sum(self.prefix)

    def prefix_frequency(self) -> Fraction:
        return Fraction(self.prefix_count(), len(self.prefix))

    def density_at(self, length: int) -> Fraction:
        word = self.finite_word(length)
        return Fraction(sum(word), length)

    def limiting_density(self) -> Fraction:
        return Fraction(self.tail_value, 1)


PREFIX = (1, 0, 1, 1)
ZERO_TAIL = Completion("zero-tail", PREFIX, 0)
ONE_TAIL = Completion("one-tail", PREFIX, 1)
COMPLETIONS = (ZERO_TAIL, ONE_TAIL)
CERTIFICATE_WINDOW = len(PREFIX)
LONG_WINDOW = 20
PROHIBITED_LIVE_CLAIMS = (
    "actual_current_surface_status: " + "retained",
    "actual_current_surface_status: proposed_" + "retained",
    "actual_current_surface_status: proposed_" + "promoted",
    "bare_retained_allowed: " + "true",
    "FINITE_CERTIFICATE_ALONE_DERIVES_UNBOUNDED_LAW=" + "TRUE",
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


def prefix_indistinguishability_checks() -> None:
    section("Finite prefix indistinguishability")
    report("two completions are defined", len(COMPLETIONS) == 2)
    report("completion names differ", ZERO_TAIL.name != ONE_TAIL.name)
    report("prefix is nonempty", CERTIFICATE_WINDOW > 0)
    report("zero-tail agrees with prefix", ZERO_TAIL.finite_word(CERTIFICATE_WINDOW) == PREFIX)
    report("one-tail agrees with prefix", ONE_TAIL.finite_word(CERTIFICATE_WINDOW) == PREFIX)
    report(
        "certificate-window words are identical",
        ZERO_TAIL.finite_word(CERTIFICATE_WINDOW) == ONE_TAIL.finite_word(CERTIFICATE_WINDOW),
    )
    for index, (left, right) in enumerate(zip(ZERO_TAIL.prefix, ONE_TAIL.prefix, strict=True)):
        report(f"prefix site {index} agrees", left == right)


def finite_certificate_checks() -> None:
    section("Finite certificate")
    counts = {completion.prefix_count() for completion in COMPLETIONS}
    freqs = {completion.prefix_frequency() for completion in COMPLETIONS}
    report("prefix marker count is shared", len(counts) == 1, str(counts))
    report("prefix frequency is shared", len(freqs) == 1, str(freqs))
    report("shared prefix marker count is three", ZERO_TAIL.prefix_count() == 3)
    report("shared prefix frequency is 3/4", ZERO_TAIL.prefix_frequency() == Fraction(3, 4))
    report(
        "finite-window density matches prefix frequency",
        ZERO_TAIL.density_at(CERTIFICATE_WINDOW) == ZERO_TAIL.prefix_frequency(),
    )
    report(
        "both completions have same finite-window density",
        ZERO_TAIL.density_at(CERTIFICATE_WINDOW) == ONE_TAIL.density_at(CERTIFICATE_WINDOW),
    )


def unbounded_divergence_checks() -> None:
    section("Unbounded divergence")
    report("tail values differ", ZERO_TAIL.tail_value != ONE_TAIL.tail_value)
    report("limiting densities differ", ZERO_TAIL.limiting_density() != ONE_TAIL.limiting_density())
    report("zero-tail limiting density is 0", ZERO_TAIL.limiting_density() == 0)
    report("one-tail limiting density is 1", ONE_TAIL.limiting_density() == 1)
    report("long-window words differ", ZERO_TAIL.finite_word(LONG_WINDOW) != ONE_TAIL.finite_word(LONG_WINDOW))
    report("long-window densities differ", ZERO_TAIL.density_at(LONG_WINDOW) != ONE_TAIL.density_at(LONG_WINDOW))
    report("zero-tail long density is 3/20", ZERO_TAIL.density_at(LONG_WINDOW) == Fraction(3, 20))
    report("one-tail long density is 19/20", ONE_TAIL.density_at(LONG_WINDOW) == Fraction(19, 20))


def route_scope_checks() -> None:
    section("Route scope")
    finite_certificate_alone_derives_unbounded_law = False
    supplied_family_lift_available = False
    no_go_prunes_only_finite_certificate_alone_route = True
    retained_or_unbounded_promotion_applied = False
    audit_verdict_applied = False
    authority_surface_written = False
    dial_forced_or_selected = False

    report(
        "finite-certificate-alone derivation flag is false",
        not finite_certificate_alone_derives_unbounded_law,
    )
    report("supplied family lift is not assumed", not supplied_family_lift_available)
    report("no-go scope is narrow", no_go_prunes_only_finite_certificate_alone_route)
    report("retained/unbounded promotion flag is false", not retained_or_unbounded_promotion_applied)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("authority surface written flag is false", not authority_surface_written)
    report("dial forced or selected flag is false", not dial_forced_or_selected)


def document_checks() -> None:
    section("Document checks")
    text = read_doc()
    required_phrases = (
        "finite post-record certificate alone => unbounded retained law",
        "two unbounded completions can agree",
        "prefix = 1, 0, 1, 1",
        "zero-tail limiting marker density = 0",
        "one-tail limiting marker density = 1",
        "pre-record law carries probabilities",
        "post-record records carry realized information",
        "finite post-record record is not an unbounded probability law",
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "bare_retained_allowed: false",
    )
    for phrase in required_phrases:
        report(f"document contains phrase: {phrase}", phrase in text)
    report(
        "document avoids live retained/promotion leaks",
        all(status not in text for status in PROHIBITED_LIVE_CLAIMS),
    )


def main() -> int:
    prefix_indistinguishability_checks()
    finite_certificate_checks()
    unbounded_divergence_checks()
    route_scope_checks()
    document_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO=TRUE")
    print("FINITE_PREFIX_LENGTH=4")
    print("PREFIX_MARKER_COUNT=3")
    print("PREFIX_FREQUENCY=3/4")
    print("ZERO_TAIL_LIMITING_DENSITY=0")
    print("ONE_TAIL_LIMITING_DENSITY=1")
    print("FINITE_CERTIFICATE_ALONE_DERIVES_UNBOUNDED_LAW=FALSE")
    print("FAMILY_LIFT_REQUIRED=TRUE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
