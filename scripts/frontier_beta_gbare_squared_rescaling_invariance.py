#!/usr/bin/env python3
"""Conditional bounded arithmetic runner for beta * g_bare^2 = 2 N_c.

This runner supports
docs/BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md.
It verifies, at exact rational precision, that once the Wilson
action-surface matching premise

    WM: beta = 2 N_c / g_bare^2

is assumed explicitly, the product beta * g_bare^2 is invariant under the
joint rescaling beta -> c^2 beta and g_bare^2 -> g_bare^2 / c^2.

The runner deliberately does not treat any Ward-route coupling-closure
note as a Wilson-matching authority. The algebraic core is cross-checked
against the already audited abstract polynomial identity note, while the
generator-rescaling interpretation is bounded by the Wilson-action
transformation boundary note.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTE_PATH = DOCS / "BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md"
ABSTRACT_IDENTITY_PATH = DOCS / "BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md"
RESCALING_PATH = DOCS / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"
BOUNDARY_PATH = DOCS / "WILSON_ACTION_GENERATOR_RESCALING_BETA_TRANSFORMATION_BOUNDARY_NOTE_2026-06-17.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


NOTE_TEXT = NOTE_PATH.read_text()
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)


def normalized(text: str) -> str:
    return text.replace("β", "beta").replace("²", "^2").replace("·", "*")


def beta_from_wm(n_c: Fraction, g_bare_sq: Fraction) -> Fraction:
    return Fraction(2) * n_c / g_bare_sq


def check_note_structure() -> None:
    section("note structure and repaired scope")
    required = [
        "Claim type:** bounded_theorem",
        "Type:** conditional / support",
        "explicitly conditional arithmetic lemma",
        "WM:  β = 2 N_c / g_bare²",
        "not imported from any Ward-route coupling-closure note",
        "BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10",
        "WILSON_ACTION_GENERATOR_RESCALING_BETA_TRANSFORMATION_BOUNDARY_NOTE_2026-06-17",
        "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03",
        "coupling-coordinate WM route",
        "not the fixed-component Wilson-action compensation law",
        "conditional bounded arithmetic lemma",
        "fractions.Fraction",
    ]
    for marker in required:
        check(
            f"contains marker: {marker[:62]}",
            marker in NOTE_TEXT or marker in NOTE_FLAT,
        )

    forbidden = [
        "Type:** bounded_theorem",
        "Proposal allowed:",
        "source-note proposal only",
        "G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18",
        "carried by G_BARE_TWO_WARD_CLOSURE",
        "canonical `g_bare² = 1` value carried",
        "is a retained conclusion of this row",
        "Wilson matching is proved here",
        "This row claims `beta -> c^2 beta` as fixed-component Wilson-action compensation",
    ]
    for marker in forbidden:
        check(
            f"forbidden old authority/framing absent: {marker[:54]}",
            marker not in NOTE_TEXT and marker not in NOTE_FLAT,
            "" if marker not in NOTE_TEXT and marker not in NOTE_FLAT else "found",
        )

    forbidden_framing = [
        "continuum-limit class",
        "Wilson asymptotic universality",
        "lattice-realization-invariant",
        "promote any status row",
    ]
    lower = NOTE_TEXT.lower()
    for marker in forbidden_framing:
        if marker == "promote any status row":
            check("boundary says no status promotion", marker in NOTE_FLAT.lower())
        else:
            check(
                f"forbidden framing absent: {marker}",
                marker.lower() not in lower,
                "" if marker.lower() not in lower else "found",
            )


def check_dependencies_exist_and_are_scoped() -> None:
    section("dependency files and scoped authority checks")
    for path in [ABSTRACT_IDENTITY_PATH, BOUNDARY_PATH, RESCALING_PATH]:
        check(f"dependency exists: docs/{path.name}", path.exists())

    abstract = ABSTRACT_IDENTITY_PATH.read_text()
    abstract_norm = normalized(abstract)
    check(
        "abstract identity states pure polynomial algebra",
        "pure polynomial algebra" in abstract.lower()
        or "pure polynomial-algebra" in abstract.lower(),
    )
    check(
        "abstract identity has no load-bearing dependencies",
        "zero load-bearing dependencies" in abstract.lower()
        or "Cited dependencies\n\nNone" in abstract,
    )
    check(
        "abstract identity proves beta(g/c,N)=c^2 beta(g,N)",
        "beta(g / c, N)  =  c^2 * beta(g, N)" in abstract_norm
        or "beta(g/c,N)=c^2*beta(g,N)" in abstract_norm.replace(" ", ""),
    )
    check(
        "abstract identity proves product invariance",
        "product beta(g, N) * g^2 = 2 N is invariant" in abstract_norm
        or "beta * g^2" in abstract_norm,
    )

    boundary = BOUNDARY_PATH.read_text()
    boundary_norm = normalized(boundary)
    check(
        "boundary note separates fixed-component compensation",
        "beta'_fixed / beta = 1 / c^2" in boundary
        or "beta'_fixed / beta = 1 / c^2" in boundary_norm,
    )
    check(
        "boundary note separates pure basis relabeling",
        "beta'_basis = beta" in boundary,
    )
    check(
        "boundary note separates coupling-coordinate c^2 law",
        "beta'_WM / beta = c^2" in boundary
        or "beta'_WM / beta = c^2" in boundary_norm,
    )

    rescaling = RESCALING_PATH.read_text()
    rescaling_flat = " ".join(rescaling.split())
    check(
        "Gram-only note is not consumed as beta-routing authority",
        "This note remains the Gram-only lemma" in rescaling_flat
        and "should not be cited as a beta-routing authority" in rescaling_flat,
    )


def check_explicit_premise_firewall() -> None:
    section("explicit Wilson-matching premise firewall")
    norm = normalized(NOTE_TEXT)
    check(
        "WM is stated as an assumption, not a theorem",
        "Wilson action-surface matching premise" in NOTE_TEXT
        and "not proved here" in NOTE_TEXT,
    )
    check(
        "WM formula is present in normalized text",
        "WM:  beta = 2 N_c / g_bare^2" in norm
        or "WM: beta = 2 N_c / g_bare^2" in norm,
    )
    check(
        "Ward-route closure is not a load-bearing authority",
        "No Ward-route coupling-closure result is used as authority for `WM`" in NOTE_FLAT,
    )
    check(
        "physical interpretation remains conditional",
        "physical Wilson-surface interpretation remains conditional" in NOTE_FLAT,
    )


def check_arithmetic_identity_table() -> None:
    section("representative exact rational table at N_c = 3, g_bare^2 = 1")
    n_c = Fraction(3)
    q = Fraction(1)
    beta = beta_from_wm(n_c, q)
    target = 2 * n_c
    check("assuming WM gives beta = 6 at representative q=1", beta == 6, str(beta))
    check("assuming WM gives beta * q = 2 N_c", beta * q == target, str(beta * q))

    expected_pairs = {
        Fraction(1, 2): (Fraction(3, 2), Fraction(4)),
        Fraction(1): (Fraction(6), Fraction(1)),
        Fraction(2): (Fraction(24), Fraction(1, 4)),
        Fraction(3): (Fraction(54), Fraction(1, 9)),
    }
    for c, (expected_beta_prime, expected_q_prime) in expected_pairs.items():
        c_sq = c * c
        beta_prime = c_sq * beta
        q_prime = q / c_sq
        product_prime = beta_prime * q_prime
        check(
            f"c = {c}: beta'(c) matches note table",
            beta_prime == expected_beta_prime,
            f"beta'={beta_prime}",
        )
        check(
            f"c = {c}: g_bare'^2(c) matches note table",
            q_prime == expected_q_prime,
            f"g_bare'^2={q_prime}",
        )
        check(
            f"c = {c}: beta'(c) * g_bare'^2(c) = 2 N_c",
            product_prime == target,
            f"product={product_prime}",
        )
        check(
            f"c = {c}: c^2 powers cancel exactly",
            c_sq * (Fraction(1) / c_sq) == 1,
            f"c^2={c_sq}",
        )


def check_arbitrary_positive_rational_instances() -> None:
    section("conditional identity for arbitrary positive rational g_bare^2")
    n_c_values = [Fraction(3), Fraction(5), Fraction(7, 2)]
    q_values = [Fraction(1), Fraction(3, 4), Fraction(5, 7), Fraction(11, 13), Fraction(1, 100)]
    c_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(7, 5)]

    for n_c in n_c_values:
        target = 2 * n_c
        for q in q_values:
            beta = beta_from_wm(n_c, q)
            check(
                f"WM product at N_c={n_c}, g_bare^2={q}",
                beta * q == target,
                f"product={beta * q}",
            )
            for c in c_values:
                c_sq = c * c
                beta_prime = c_sq * beta
                q_prime = q / c_sq
                check(
                    f"joint rescaling invariance at N_c={n_c}, q={q}, c={c}",
                    beta_prime * q_prime == target,
                    f"product={beta_prime * q_prime}",
                )


def check_boundary_clauses() -> None:
    section("boundary clauses present")
    boundaries = [
        "conditional bounded arithmetic lemma only",
        "Wilson matching `β = 2 N_c / g_bare²` from the framework axioms",
        "Wilson plaquette action selector",
        "any retention or promotion",
        "Ward-route coupling-closure theorem carries the Wilson matching",
        "imported abstract polynomial identity",
        "`c^2` beta law is the fixed-component Wilson-action",
        "Wilson-action generator-rescaling boundary theorem",
        "canonical Cl(3) connection normalization",
        "parent theorem/status promotion",
    ]
    for marker in boundaries:
        check(f"boundary clause present: {marker[:62]}", marker in NOTE_TEXT)


def main() -> int:
    print("frontier_beta_gbare_squared_rescaling_invariance.py")
    check_note_structure()
    check_dependencies_exist_and_are_scoped()
    check_explicit_premise_firewall()
    check_arithmetic_identity_table()
    check_arbitrary_positive_rational_instances()
    check_boundary_clauses()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: conditional bounded arithmetic lemma passes; assuming WM,"
        )
        print(
            "beta * g_bare^2 = 2 N_c is invariant under the scoped joint rescaling"
        )
        print("for c in {1/2, 1, 2, 3} at exact rational precision.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
