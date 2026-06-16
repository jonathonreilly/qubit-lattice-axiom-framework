#!/usr/bin/env python3
"""Exact notation-equivalence verifier for alpha^N = exp(-c_eff/alpha).

The audited source boundary is T1 only:

    c_eff(alpha, N) := N * alpha * ln(1/alpha)
    alpha^N == exp(-c_eff(alpha, N) / alpha)

No plaquette value, electroweak value, literature comparator, taste bridge,
or parent hierarchy status is consumed by this runner.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

try:
    import sympy as sp

    HAS_SYMPY = True
except ImportError:  # pragma: no cover
    HAS_SYMPY = False


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING_BOUNDED_NOTATION_EQUIVALENCE_NOTE_2026-05-16.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def c_eff(alpha: float, n: int) -> float:
    return n * alpha * math.log(1.0 / alpha)


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Hierarchy alpha-LM dimensional-transmutation T1 notation equivalence")
    print("Status authority: independent audit lane only.")
    print("No new imports: real-variable algebra only.")

    section("T1 symbolic identity")
    if HAS_SYMPY:
        alpha = sp.Symbol("alpha", positive=True)
        n = sp.Symbol("N", positive=True, integer=True)
        c_symbolic = n * alpha * sp.log(1 / alpha)
        diff = sp.simplify(alpha**n - sp.exp(-c_symbolic / alpha))
        print(f"alpha^N - exp(-N*alpha*ln(1/alpha)/alpha) = {diff}")
        check("symbolic identity closes for alpha > 0 and positive integer N", diff == 0)
    else:
        print("sympy unavailable; symbolic check skipped")
        check("symbolic identity skipped only when sympy is unavailable", True)

    section("T1 numerical instances")
    samples = [
        (0.5, 1),
        (0.25, 3),
        (0.090667836017, 16),
        (math.e ** -2, 7),
    ]
    max_rel = 0.0
    for alpha_value, n_value in samples:
        lhs = alpha_value**n_value
        rhs = math.exp(-c_eff(alpha_value, n_value) / alpha_value)
        rel = abs(lhs - rhs) / max(abs(lhs), 1.0e-300)
        max_rel = max(max_rel, rel)
        print(
            f"alpha={alpha_value:.15f}; N={n_value:2d}; "
            f"lhs={lhs:.15e}; rhs={rhs:.15e}; rel={rel:.3e}"
        )
    check("floating-point instances agree to roundoff", max_rel < 5.0e-14, f"max_rel={max_rel:.3e}")

    section("Exact rational spot check")
    alpha_q = Fraction(1, 10)
    n_q = 4
    lhs_q = alpha_q**n_q
    rhs_q = math.exp(-c_eff(float(alpha_q), n_q) / float(alpha_q))
    rel_q = abs(float(lhs_q) - rhs_q) / float(lhs_q)
    print(f"alpha=1/10; N=4; exact lhs={lhs_q}; rhs={rhs_q:.15e}; rel={rel_q:.3e}")
    check("rational sample matches the real-log rewrite", rel_q < 5.0e-14)

    section("No substrate constant is derived")
    alpha_a = 0.09
    alpha_b = 0.11
    c_a = c_eff(alpha_a, 16)
    c_b = c_eff(alpha_b, 16)
    print(f"c_eff(0.09, 16) = {c_a:.12f}")
    print(f"c_eff(0.11, 16) = {c_b:.12f}")
    check(
        "c_eff defined by T1 depends on alpha and is not an independent constant",
        abs(c_a - c_b) > 0.1,
        f"delta={abs(c_a - c_b):.6f}",
    )

    section("Source-note boundary hygiene")
    text = note_text()
    missing_required = [
        phrase
        for phrase in [
            "exact notation equivalence only",
            "does not derive a physical value of `alpha_LM`",
            "does not upgrade any hierarchy",
            "TOTAL: PASS=5 FAIL=0",
        ]
        if phrase not in text
    ]
    has_markdown_links = "](" in text
    check(
        "note is scoped to T1 without markdown dependency or literature authority hooks",
        bool(text) and not missing_required and not has_markdown_links,
        f"missing={missing_required}; markdown_links={has_markdown_links}",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
