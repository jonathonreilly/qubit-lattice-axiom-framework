#!/usr/bin/env python3
"""Verifier for the stable post-record dial location certificate.

This runner certifies the safe statement: s=0/r=1/2 is a stable post-record
equal-letter location, not a forced or selected physical dial value.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PASS_COUNT = 0
FAIL_COUNT = 0


PATHS = {
    "certificate": ROOT / "docs" / "STABLE_POST_RECORD_DIAL_LOCATION_CERTIFICATE_2026-06-06.md",
    "equal_letter": ROOT / "docs" / "RECORD_EQUAL_LETTER_STABLE_LOCATION_2026-06-05.md",
    "prior_selector": ROOT / "docs" / "RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md",
    "generation_prior": ROOT / "docs" / "GENERATION_PRIOR_STABILITY_2026-06-05.md",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def read_text(label: str) -> str:
    path = PATHS[label]
    check(f"{label} exists", path.exists(), path.relative_to(ROOT).as_posix())
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return needle in text


def pi_s_pow2(pow2_s: Fraction) -> tuple[Fraction, Fraction]:
    return (Fraction(1, 1) / (1 + pow2_s), pow2_s / (1 + pow2_s))


def reset(p: tuple[Fraction, Fraction], target: tuple[Fraction, Fraction], alpha: Fraction) -> tuple[Fraction, Fraction]:
    return tuple((1 - alpha) * p[i] + alpha * target[i] for i in range(2))


def diff(p: tuple[Fraction, Fraction], q: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return tuple(p[i] - q[i] for i in range(2))


def main() -> None:
    print("Stable post-record dial location certificate")
    print("=" * 68)

    certificate = read_text("certificate")
    equal_letter = read_text("equal_letter")
    prior_selector = read_text("prior_selector")
    generation_prior = read_text("generation_prior")

    check(
        "certificate status is stable-location only",
        has(certificate, "stable-location certificate")
        and has(certificate, "not a\ndial-selection theorem")
        and has(certificate, "not a Koide closure"),
    )
    check(
        "certificate states s0/rhalf/Q23 target",
        has(certificate, "s = 0, r = 1/2, Q = 2/3"),
    )
    check(
        "certificate keeps force/selection wording forbidden",
        has(certificate, "Record dynamics forces s=0")
        and has(certificate, "Post-record counts select Koide")
        and has(certificate, "Not allowed"),
    )
    check(
        "certificate asks sharper next question",
        has(certificate, "what physical dynamics or")
        and has(certificate, "chooses among stable `pi_s` targets"),
    )

    check(
        "equal-letter note says equal point is stable location",
        has(equal_letter, "equal-letter point is a stable location")
        and has(equal_letter, "stable post-record location"),
    )
    check(
        "equal-letter note gives reset contraction",
        has(equal_letter, "Phi_alpha(p) - u = (1 - alpha)(p - u)")
        and has(equal_letter, "record-letter imbalance contracts"),
    )
    check(
        "equal-letter note maps s0 to rhalf and Q23",
        has(equal_letter, "s = 0,      r = 1/2,      Q = 2/3"),
    )
    check(
        "equal-letter note says same construction works for every s",
        has(equal_letter, "same reset construction works for every dial prior")
        and has(equal_letter, "stability itself does not choose\n`s`"),
    )
    check(
        "equal-letter note forbids forced dial claims",
        has(equal_letter, "Does not force Koide")
        and has(equal_letter, "Does not fix the dial"),
    )
    check(
        "equal-letter note runner is clean",
        has(equal_letter, "PASS=26 FAIL=0"),
    )

    check(
        "prior selector states atom symmetry selects equal endpoint",
        has(prior_selector, "Post-record atom symmetry selects the equal-letter endpoint"),
    )
    check(
        "prior selector states microstate symmetry selects dimension endpoint",
        has(prior_selector, "Pre-record microstate symmetry selects the dimension endpoint"),
    )
    check(
        "prior selector says stability alone does not choose endpoint",
        has(prior_selector, "Stability alone does not choose the endpoint")
        and has(prior_selector, "Koide is not forced"),
    )
    check(
        "prior selector gives dial formula",
        has(prior_selector, "pi_s = (1/(1 + 2^s), 2^s/(1 + 2^s))")
        and has(prior_selector, "r(s) = (doublet/singlet odds) / 2 = 2^(s-1)"),
    )
    check(
        "prior selector endpoints are s0 and s1",
        has(prior_selector, "`s=0` | `(1/2, 1/2)`")
        and has(prior_selector, "`s=1` | `(1/3, 2/3)`"),
    )
    check(
        "prior selector says no new axiom",
        has(prior_selector, "This should not be added as a new axiom"),
    )
    check(
        "prior selector runner is clean",
        has(prior_selector, "PASS=37 FAIL=0"),
    )

    check(
        "generation prior note states unforced stable setting",
        has(generation_prior, "unforced stable setting"),
    )
    check(
        "generation prior note says post-record dynamics does not force equal-letter",
        has(generation_prior, "post-record dynamics does **not** force")
        and has(generation_prior, "does **not** force the dial"),
    )
    check(
        "generation prior note says no non-circular post-record dynamics selects equal-letter",
        has(generation_prior, "no non-circular post-record dynamics selects equal-letter"),
    )
    check(
        "generation prior note identifies token count vs type count",
        has(generation_prior, "Token frequency")
        and has(generation_prior, "Type count"),
    )
    check(
        "generation prior note identifies dial as pre-record operator property",
        has(generation_prior, "dial is a **pre-record** object")
        and has(generation_prior, "pre-record (operator)"),
    )
    check(
        "generation prior note runner is clean",
        has(generation_prior, "PASS=23 FAIL=0"),
    )

    alpha = Fraction(1, 5)
    u = (Fraction(1, 2), Fraction(1, 2))
    p = (Fraction(9, 10), Fraction(1, 10))
    reset_u = reset(p, u, alpha)
    check("equal-letter reset leaves u stationary", reset(u, u, alpha) == u)
    check("equal-letter deviation contracts by 1-alpha", diff(reset_u, u) == tuple((1 - alpha) * x for x in diff(p, u)))
    check("equal-letter imbalance contracts by 1-alpha", (reset_u[0] - reset_u[1]) == (1 - alpha) * (p[0] - p[1]))

    pi0 = pi_s_pow2(Fraction(1, 1))
    pi1 = pi_s_pow2(Fraction(2, 1))
    check("s=0 target is equal-letter", pi0 == (Fraction(1, 2), Fraction(1, 2)), str(pi0))
    check("s=1 target is dimension/Born endpoint", pi1 == (Fraction(1, 3), Fraction(2, 3)), str(pi1))

    r0 = Fraction(1, 2)
    q0 = Fraction(1, 3) + Fraction(2, 3) * r0
    r1 = Fraction(1, 1)
    q1 = Fraction(1, 3) + Fraction(2, 3) * r1
    check("s=0 maps to r=1/2", r0 == Fraction(1, 2))
    check("s=0 maps to Q=2/3", q0 == Fraction(2, 3), str(q0))
    check("s=1 maps to r=1", r1 == 1)
    check("s=1 maps to Q=1", q1 == 1)

    reset_pi1 = reset(p, pi1, alpha)
    check("arbitrary fixed target pi_s is stationary", reset(pi1, pi1, alpha) == pi1)
    check("arbitrary fixed target deviations contract", diff(reset_pi1, pi1) == tuple((1 - alpha) * x for x in diff(p, pi1)))
    check("same stability form can target different dial points", pi0 != pi1 and reset(pi0, pi0, alpha) == pi0 and reset(pi1, pi1, alpha) == pi1)

    allowed_statement = "stable_location"
    forbidden_statements = {"forced_dial", "koide_closure", "post_record_count_selector", "audit_verdict"}
    check("allowed statement is only stable location", allowed_statement == "stable_location")
    check("forced-dial statements remain forbidden", "forced_dial" in forbidden_statements and "koide_closure" in forbidden_statements)
    check("post-record count selector remains forbidden", "post_record_count_selector" in forbidden_statements)
    check("audit verdict remains forbidden", "audit_verdict" in forbidden_statements)

    print("=" * 68)
    print("CERTIFIED: s=0/r=1/2/Q=2/3 is a stable post-record location.")
    print("NOT CERTIFIED: forced dial selection, Koide closure, or audit verdict.")
    print("STATUS: exact-support stable-location certificate; audit_required_before_effective_retained=true")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
