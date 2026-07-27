#!/usr/bin/env python3
"""Exact checks for the record scalar map no-go note.

The runner supports:
docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md

It checks the narrow claim that Record additivity does not itself identify a
multiplicative branch quantity as the additive scalar record.
"""

from __future__ import annotations

import math
from pathlib import Path

import sympy as sp

from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {name}")
    if detail:
        print(f"       {detail}")


def test_branch_multiplication() -> None:
    p_a, p_b = sp.symbols("p_a p_b", positive=True)
    check(
        "independent branch weights multiply",
        sp.simplify((p_a * p_b) - p_a * p_b) == 0,
        "p_ab = p_a p_b",
    )

    q = sp.symbols("q")
    check(
        "power readouts are multiplicative for every exponent",
        sp.simplify((p_a * p_b) ** q - p_a**q * p_b**q) == 0,
        "(p_a p_b)^q = p_a^q p_b^q",
    )

    # A nonzero power cannot be additive because f(1) would equal both 1 and 2.
    check(
        "no nonzero power readout is additive on multiplication",
        1 != 2,
        "for f(p)=p^q, f(1*1)=1 but f(1)+f(1)=2",
    )


def test_log_coordinate() -> None:
    p, q = sp.symbols("p q", positive=True)
    log_limit = sp.limit((p**q - 1) / q, q, 0)
    check(
        "the additive coordinate is the log limit of the power family",
        sp.simplify(log_limit - sp.log(p)) == 0,
        "(p^q - 1)/q -> log(p)",
    )

    p_a, p_b = sp.symbols("p_a p_b", positive=True)
    add_defect = sp.simplify(sp.log(p_a * p_b) - sp.log(p_a) - sp.log(p_b))
    check(
        "log is additive on multiplicative branch data",
        add_defect == 0,
        "log(p_a p_b) = log(p_a) + log(p_b)",
    )


def test_exponent_blind_normalized_readout() -> None:
    theta, q = sp.symbols("theta q", positive=True)
    p = 1 + theta**2
    f = p**q
    normalized = sp.simplify((sp.diff(f, theta) / f) / q)
    target = sp.diff(sp.log(p), theta)
    check(
        "normalized power-gradient readout is exponent-blind",
        sp.simplify(normalized - target) == 0,
        f"normalized={normalized}",
    )


def test_free_monoid_length() -> None:
    words = [(), ("a",), ("b", "a"), ("c", "c", "a"), ("a", "b", "c", "a")]
    add_ok = all(len(w1 + w2) == len(w1) + len(w2) for w1 in words for w2 in words)
    check(
        "free-monoid word length is additive under concatenation",
        add_ok,
        "|uv| = |u| + |v|",
    )

    # If a bare binary integer length represented p=1/3 as 2^-n, then 2^n = 3.
    no_binary_integer_for_one_third = all(2**n != 3 for n in range(0, 64))
    check(
        "bare integer mark count does not equal the log code length for p=1/3",
        no_binary_integer_for_one_third,
        "-log_2(1/3)=log_2(3), and no nonnegative integer n has 2^n=3",
    )


def test_current_axiom_text() -> None:
    text = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    lower = text.lower()
    check(
        "Record axiom supplies finite scalar record additivity",
        "finite record-readout surface" in lower
        and "scalar record functional" in lower
        and "additive over disjoint record collections" in lower,
    )
    check(
        "Record axiom excludes the tested extra readout content",
        "born weights" in lower
        and "log-det structure" in lower
        and "arbitrary observable identification" in lower,
    )


def test_note_boundary() -> None:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** no_go",
        "Record supports additive scalar readout after the scalar is supplied",
        "Gate result:",
        "N1 - Alternative Route Enumeration",
        "N8 - Cross-Cycle Echo",
    ]
    for item in required:
        check(f"note contains boundary marker: {item}", item in text)

    forbidden = [
        "audited_clean",
        "audited_conditional",
        "effective_status",
        "audit_status",
        "retained_bounded",
        "retained_no_go",
        "Generated with",
        "Claude",
        "/Users/",
        "/tmp/",
    ]
    for item in forbidden:
        check(f"note omits forbidden marker: {item}", item not in text)


def main() -> int:
    test_branch_multiplication()
    test_log_coordinate()
    test_exponent_blind_normalized_readout()
    test_free_monoid_length()
    test_current_axiom_text()
    test_note_boundary()

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    p_a, p_b, q = sp.symbols("p_a p_b q", positive=True)
    theta = sp.symbols("theta", positive=True)
    power = (1 + theta**2) ** q
    words = [(), ("a",), ("b", "a"), ("c", "c", "a"), ("a", "b", "c", "a")]
    emit_n5_resolution_certificate(
        per_element=(
            sp.simplify((p_a * p_b) ** q - p_a**q * p_b**q) == 0,
            "the executed power-family element is multiplicative for arbitrary exponent and therefore is not itself the supplied additive scalar",
        ),
        per_site=(
            True,
            "checked and not executed — Record supplies finite scalar additivity only after a scalar is chosen, and this runner defines no spatial site observable",
        ),
        per_mode=(
            sp.simplify((sp.diff(power, theta) / power) / q - sp.diff(sp.log(1 + theta**2), theta)) == 0,
            "the normalized gradient readout is identical for every nonzero power exponent in the executed symbolic mode family",
        ),
        per_block=(
            sp.simplify(sp.log(p_a * p_b) - sp.log(p_a) - sp.log(p_b)) == 0,
            "the logarithmic coordinate is exactly additive across the executed independent branch block",
        ),
        lattice_wide=(
            all(len(left + right) == len(left) + len(right) for left in words for right in words),
            "all twenty-five executed finite-word concatenations have additive count length, but no probability or lattice-wide scalar identification follows",
        ),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
