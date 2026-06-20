#!/usr/bin/env python3
"""Abstract joint-rescaling algebra runner for beta * g_bare^2 = 2 N_c.

This runner supports
docs/BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md
after the 2026-06-20 abstract-algebra narrowing.

The load-bearing content is the abstract joint-rescaling algebra: on
abstract symbolic variables (g, N) with g > 0, defining the rational
function beta(g, N) := 2 N / g^2, the product beta * g^2 = 2 N is invariant
under the abstract joint rescaling (g, beta) -> (g/c, c^2 * beta). Naming
the abstract variables (g, N) = (g_bare, N_c) is a symbolic relabeling only.

The runner verifies this abstract identity at exact rational precision. It
does NOT assert the physical Wilson action-surface induction
T_a -> c T_a => (g_bare^2 -> g_bare^2/c^2, beta -> c^2 beta); that induction
is the OPEN bridge requiring the named retained authority, not supplied by
this row. The runner therefore also checks that the row's narrowed scope
quarantines the physical Wilson-surface reading as open, and that the scoped
rescaling note (now a Gram-only lemma) does not supply the beta-routing.
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


def beta_from_naming(n_c: Fraction, g_bare_sq: Fraction) -> Fraction:
    """Abstract definition beta(g_bare, N_c) = 2 N_c / g_bare^2 (symbolic naming)."""
    return Fraction(2) * n_c / g_bare_sq


def check_note_structure() -> None:
    section("note structure and narrowed (abstract-algebra) scope")
    required = [
        "Abstract Joint-Rescaling Algebra Lemma",
        "abstract-algebra\nnarrowing: 2026-06-20",
        "Status authority:** independent audit lane only",
        "abstract joint-rescaling algebra",
        "symbolic relabeling only",
        "conditional bounded arithmetic lemma",
        "fractions.Fraction",
    ]
    for marker in required:
        check(
            f"contains marker: {marker[:62]}",
            marker in NOTE_TEXT or marker in NOTE_FLAT,
        )

    forbidden = [
        "Proposal allowed:",
        "source-note proposal only",
        "G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18",
        "carried by G_BARE_TWO_WARD_CLOSURE",
        "canonical `g_bare² = 1` value carried",
        "Wilson matching is proved here",
    ]
    for marker in forbidden:
        ok = marker not in NOTE_TEXT and marker not in NOTE_FLAT
        check(
            f"forbidden old authority/framing absent: {marker[:54]}",
            ok,
            "" if ok else "found",
        )

    # Firewall: g_bare physical value must not be asserted as derived.
    norm = normalized(NOTE_TEXT)
    for marker in ["g_bare = 1 follows", "derives g_bare = 1", "g_bare = 1 is forced"]:
        ok = marker not in norm
        check(f"no g_bare=1 derivation claim: {marker}", ok, "" if ok else "found")

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
            ok = marker.lower() not in lower
            check(
                f"forbidden framing absent: {marker}",
                ok,
                "" if ok else "found",
            )


def check_narrowing_to_abstract_algebra() -> None:
    section("narrowing: physical Wilson-surface induction quarantined as open")
    # The load-bearing content is the abstract joint-rescaling algebra; the
    # physical Wilson-action-surface induction is the open bridge and is NOT
    # supplied here.
    check(
        "2026-06-20 repair section present",
        "2026-06-20 Narrowing (abstract joint-rescaling algebra)"
        in NOTE_TEXT,
    )
    check(
        "abstract joint-rescaling algebra named as load-bearing",
        "abstract joint-rescaling algebra" in NOTE_FLAT
        and "load-bearing content" in NOTE_FLAT,
    )
    check(
        "physical Wilson action-surface induction marked open / not supplied",
        "physical Wilson-surface reading therefore remains" in NOTE_FLAT
        and "not supplied" in NOTE_FLAT.replace("**", ""),
    )
    check(
        "open bridge names the T_a -> c T_a Wilson-surface induction",
        "generator-basis rescaling `T_a -> c · T_a` actually" in NOTE_TEXT
        or "induces `g_bare² -> g_bare²/c²` and `β -> c²·β` *on the Wilson plaquette"
        in NOTE_TEXT,
    )
    check(
        "WM kept as symbolic naming only, not physical action-surface statement",
        "symbolic naming" in NOTE_FLAT
        and "As a *physical* Wilson action-surface matching statement it is not proved"
        in NOTE_TEXT,
    )
    check(
        "physical Wilson-surface interpretation stated conditional and open",
        "physical Wilson-surface interpretation therefore remains" in NOTE_FLAT
        and "conditional and open" in NOTE_FLAT,
    )


def check_dependencies_exist_and_are_scoped() -> None:
    section("load-bearing dependency and reader-context file checks")
    for path in [ABSTRACT_IDENTITY_PATH, RESCALING_PATH]:
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

    # The scoped rescaling note is reader-context only and (after its own
    # 2026-06-16 gram-only narrowing) does NOT supply the beta-routing that
    # would constitute the open physical Wilson-surface induction.
    rescaling = RESCALING_PATH.read_text()
    rescaling_flat = re.sub(r"\s+", " ", rescaling)
    rescaling_lower = rescaling_flat.lower()
    check(
        "reader-context rescaling note carries T_a -> c T_a scalar rescaling map",
        "T_a -> c" in rescaling
        or "T_a → c" in rescaling
        or "c * T_a" in rescaling
        or "c T_a" in rescaling
        or "(c T_a)" in rescaling,
    )
    check(
        "rescaling note does NOT supply the beta-routing (open bridge stays open)",
        "is no longer a beta-routing lemma" in rescaling_lower
        and "normalization theorem not supplied by this row" in rescaling_flat
        and "does not derive any `beta_new / beta_old`" in rescaling_flat,
    )
    check(
        "rescaling note does not claim to derive Wilson matching / action-surface uniqueness",
        "Wilson matching is not consumed by the narrowed lemma" in rescaling_flat
        and "does not prove action-surface uniqueness" in rescaling_flat,
    )


def check_explicit_premise_firewall() -> None:
    section("symbolic-naming / Wilson-surface firewall")
    norm = normalized(NOTE_TEXT)
    check(
        "physical WM stated as not proved here",
        "is not proved\nhere" in NOTE_TEXT or "is not proved here" in NOTE_FLAT,
    )
    check(
        "WM formula is present in normalized text",
        "WM: beta = 2 N_c / g_bare^2" in norm or "WM:  beta = 2 N_c / g_bare^2" in norm,
    )
    check(
        "Ward-route closure is not a load-bearing authority for the Wilson reading",
        "No Ward-route coupling-closure result is used as authority for the Wilson reading"
        in NOTE_FLAT,
    )


def check_arithmetic_identity_table() -> None:
    section("representative exact rational table at N_c = 3, g_bare^2 = 1")
    n_c = Fraction(3)
    q = Fraction(1)
    beta = beta_from_naming(n_c, q)
    target = 2 * n_c
    check("abstract naming gives beta = 6 at representative q=1", beta == 6, str(beta))
    check("abstract naming gives beta * q = 2 N_c", beta * q == target, str(beta * q))

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
    section("abstract joint-rescaling invariance for arbitrary positive rational g^2")
    n_c_values = [Fraction(3), Fraction(5), Fraction(7, 2)]
    q_values = [Fraction(1), Fraction(3, 4), Fraction(5, 7), Fraction(11, 13), Fraction(1, 100)]
    c_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(7, 5)]

    for n_c in n_c_values:
        target = 2 * n_c
        for q in q_values:
            beta = beta_from_naming(n_c, q)
            check(
                f"abstract product at N_c={n_c}, g^2={q}",
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
        "physical Wilson action-surface induction",
        "Wilson plaquette action selector",
        "any retention or promotion",
        "Ward-route coupling-closure theorem carries the Wilson matching",
        "imported abstract polynomial identity",
        "scoped generator-basis rescaling theorem",
        "canonical Cl(3) connection normalization",
        "parent theorem/status promotion",
    ]
    for marker in boundaries:
        check(f"boundary clause present: {marker[:62]}", marker in NOTE_TEXT)


def main() -> int:
    print("frontier_beta_gbare_squared_rescaling_invariance.py")
    check_note_structure()
    check_narrowing_to_abstract_algebra()
    check_dependencies_exist_and_are_scoped()
    check_explicit_premise_firewall()
    check_arithmetic_identity_table()
    check_arbitrary_positive_rational_instances()
    check_boundary_clauses()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: abstract joint-rescaling algebra lemma passes; with the abstract")
        print("naming (g, N) = (g_bare, N_c), beta * g_bare^2 = 2 N_c is invariant under")
        print("the abstract joint rescaling for c in {1/2, 1, 2, 3} at exact rational")
        print("precision; the physical Wilson-action-surface induction is the open bridge")
        print("and is not asserted.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
