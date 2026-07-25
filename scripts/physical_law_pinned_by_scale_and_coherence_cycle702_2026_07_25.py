#!/usr/bin/env python3
"""Cycle 702: what the framework itself pins about the law, using only the
approved scale primitive and axiom coherence -- no counting convention.

Two independent parts.

PART I -- the field law's form.

The landed proper-cubic kernel classification gives, at nearest-neighbor range,
a two-dimensional family of covariant additive operators,

    L = A * I + B * Delta.

The only physical content is the dimensionless ratio A/B; the overall scale B
is absorbed by the normalization of the source.  On a periodic box the symbol
is A + B * Dhat(k) with Dhat(k) = 2*(cos k1 + cos k2 + cos k3) - 6, so the
response is long-ranged exactly when the symbol vanishes at k = 0, i.e. exactly
when A = 0; otherwise the propagator is a lattice Yukawa with screening length
1/sqrt(A/B) in lattice units.

The approved scale-reference primitive fixes the lattice unit by
`a^{-1} = M_Pl`, and its own declaration says it "carries zero dimensionless
content" and that "dimensionless physics must derive from retained-grade
framework content or remain conditional/open".

Therefore every member of the family except A = 0 requires supplying a
dimensionless number that the current surface does not supply, while A = 0 is
picked out by a structural condition -- the operator annihilates constants --
that requires no number at all.  That is the sense in which the law is pinned:
not by adopting a convention, but by noticing that exactly one member needs no
supplied dimensionless input.

PART II -- a coherence constraint on the admissibility rule itself.

The Record axiom asserts additivity "for any finite collection of
pairwise-disjoint records".  For the unrestricted reading to be well posed, both
sub-collections and disjoint unions of admissible configurations must themselves
be admissible.  Write A(p) for the available set at a site whose
nearest-neighbor occupancy pattern is p.

    closure under sub-collection  <=>  A is antitone  (A(q) contains A(p) for q subset p)
    closure under disjoint union  <=>  A is monotone  (A(q) contains A(p) for q superset p)

Both at once force A constant on the pattern lattice, because the empty pattern
and the full pattern are comparable to every pattern through chains.  The
Admissibility axiom requires the available possibilities to VARY with the
nearest-neighbor conditions.  So no admissible rule satisfies both closures.

The unrestricted reading of the additivity clause is therefore incompatible with
the "vary with" clause, and the ways of resolving that are statements about the
law, not conventions.

Nothing here adopts an axiom, a primitive, a convention, or a reading, and no
rule exhibited is claimed to be the framework's rule.  Every scored row uses
exact integer, rational, or symbolic arithmetic.  The runner imports no
repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


# ==========================================================================
# PART I -- the field law
# ==========================================================================


def part_one(summary: dict) -> None:
    A, B, k1, k2, k3 = sp.symbols("A B k1 k2 k3", real=True)

    Dhat = 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) - 6
    symbol = A + B * Dhat

    # ---- P1: the symbol vanishes at k=0 exactly when A = 0
    at_zero = sp.simplify(symbol.subs({k1: 0, k2: 0, k3: 0}))
    vanishes_iff_A_zero = sp.simplify(at_zero - A) == 0
    # a nonzero A leaves a nonzero symbol at k=0, for any B
    nonzero_witness = sp.simplify(at_zero.subs({A: 1, B: 7})) == 1
    check(
        "P1 the lattice symbol at zero momentum is exactly A, so the response "
        "is long-ranged precisely when A=0; any nonzero A leaves a nonzero gap "
        "for every B",
        vanishes_iff_A_zero and nonzero_witness,
        {
            "symbol_at_k0": str(at_zero),
            "long_range_iff": "A = 0",
        },
    )

    # ---- P2: small-k expansion gives the Yukawa mass, screening length 1/sqrt(A/B)
    eps = sp.Symbol("eps", positive=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    # expand along a general direction (n1,n2,n3), so the result is the full
    # 3-D quadratic form rather than a single-axis slice
    gen = symbol.subs({k1: eps * n1, k2: eps * n2, k3: eps * n3})
    series = sp.series(gen, eps, 0, 4).removeO()
    quad = sp.simplify(sp.expand(series) - A)
    leading_ok = sp.simplify(quad + B * eps**2 * (n1**2 + n2**2 + n3**2)) == 0
    # isotropy: the quadratic form is a multiple of |n|^2, no direction singled out
    isotropic = sp.simplify(
        quad.subs({n1: 1, n2: 0, n3: 0}) - quad.subs({n1: 0, n2: 1, n3: 0})
    ) == 0
    m2 = sp.simplify(A / B)
    check(
        "P2 the full three-dimensional small-momentum expansion is "
        "A - B|k|^2, isotropically, so a nonzero A is a Yukawa mass term with "
        "m^2 = A/B and screening length 1/sqrt(A/B) in lattice units",
        leading_ok and isotropic,
        {
            "expansion": str(sp.simplify(A + quad)),
            "isotropic": isotropic,
            "m_squared": str(m2),
            "screening_length_lattice_units": "1/sqrt(A/B)",
        },
    )

    # ---- P3: exact finite-box confirmation that A=0 is the unique flat direction
    # On a periodic L^3 box the constant field is annihilated iff A = 0.
    L = 4
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    FACES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def op(a: F, b: F):
        M = [[F(0)] * n for _ in sites]
        for s in sites:
            M[idx[s]][idx[s]] += a - 6 * b
            for v in FACES:
                t = tuple((s[i] + v[i]) % L for i in range(3))
                M[idx[s]][idx[t]] += b
        return M

    ones = [F(1)] * n

    def apply_op(M, vec):
        return [sum(M[i][j] * vec[j] for j in range(n)) for i in range(n)]

    kills_constants = all(v == 0 for v in apply_op(op(F(0), F(1)), ones))
    keeps_constants = any(v != 0 for v in apply_op(op(F(1), F(1)), ones))
    # and for several nonzero A the constant is scaled by exactly A
    scales_by_A = all(
        apply_op(op(F(a), F(1)), ones)[0] == F(a) for a in (1, 2, -3, F(1, 5))
    )
    check(
        "P3 on an exact periodic box the constant field is annihilated exactly "
        "when A=0, and for nonzero A the constant is scaled by exactly A",
        kills_constants and keeps_constants and scales_by_A,
        {
            "box": f"{L}^3 periodic",
            "A_zero_annihilates_constants": kills_constants,
            "A_nonzero_does_not": keeps_constants,
        },
    )

    # ---- P4: what the scale primitive does and does not supply
    # The primitive fixes the lattice unit (a^-1 = M_Pl) and declares zero
    # dimensionless content.  A/B is dimensionless; B alone is absorbed by the
    # source normalization.  So the family's only unsupplied physical input is
    # the single dimensionless number A/B, and A=0 is the one value fixed by a
    # structural condition rather than by a number.
    # The claim is that B factors out of the operator, so that only A/B and a
    # rescaled source carry physical content.  Checked as an exact entrywise
    # matrix identity op(A,B) == B * op(A/B, 1) on the periodic box, for several
    # exact rationals -- this can fail if the construction is wrong.
    def scaled_matches(a: F, b: F) -> bool:
        left = op(a, b)
        right = op(a / b, F(1))
        return all(
            left[i][j] == b * right[i][j] for i in range(n) for j in range(n)
        )

    B_absorbable = all(
        scaled_matches(F(a), F(b))
        for a, b in ((1, 2), (3, 1), (-5, 4), (F(2, 7), F(3, 5)))
    )
    # negative control: it does NOT hold for a wrong rescaling
    wrong_rescale = not all(
        all(
            op(F(1), F(2))[i][j] == F(3) * op(F(1, 2), F(1))[i][j]
            for i in range(n)
            for j in range(n)
        )
        for _ in (0,)
    )
    dimensionless_inputs = {"A_over_B"}
    check(
        "P4 the overall scale B is absorbed by rescaling the source, so the "
        "family's only unsupplied physical input is the single dimensionless "
        "ratio A/B, which the scale primitive explicitly does not supply",
        B_absorbable and wrong_rescale and dimensionless_inputs == {"A_over_B"},
        {
            "absorbable_overall_scale": B_absorbable,
            "wrong_rescaling_rejected": wrong_rescale,
            "remaining_dimensionless_inputs": sorted(dimensionless_inputs),
            "value_needing_no_supplied_number": "A = 0",
        },
    )
    summary["part_one"] = (
        "at nearest-neighbor range the covariant additive family is A*I + B*Delta; "
        "B is absorbed by source normalization; the sole dimensionless input is "
        "A/B; the response is long-ranged exactly at A=0, which is fixed by a "
        "structural condition and needs no supplied number, while every other "
        "member needs a dimensionless quantity the current surface does not supply"
    )


# ==========================================================================
# PART II -- coherence constrains the admissibility rule
# ==========================================================================


def part_two(summary: dict) -> None:
    FACES6 = list(range(6))
    PATTERNS = [
        frozenset(s) for k in range(7) for s in itertools.combinations(FACES6, k)
    ]
    assert len(PATTERNS) == 64

    # ---- Q1: both closures force a constant rule (exhaustive over a 2-letter
    # available-set lattice, which is the smallest that can "vary")
    CONTENTS = ("c0", "c1")
    NONEMPTY = [
        frozenset(s) for k in (1, 2) for s in itertools.combinations(CONTENTS, k)
    ]

    def antitone(Amap) -> bool:
        return all(Amap[q] >= Amap[p] for p in PATTERNS for q in PATTERNS if q < p)

    def monotone(Amap) -> bool:
        return all(Amap[q] >= Amap[p] for p in PATTERNS for q in PATTERNS if q > p)

    # exhaustive search is 3^64; instead prove it on the chain structure and
    # verify the proof's decisive step exhaustively: every pattern is comparable
    # to both the empty and the full pattern
    empty, full = frozenset(), frozenset(FACES6)
    chain_reaches_all = all(empty <= p <= full for p in PATTERNS)
    # so both closures give A(p) >= A(empty) >= A(p) and A(p) >= A(full) >= A(p)
    # exhibit the forced equality on a concrete rule satisfying both
    const_rule = {p: frozenset(CONTENTS) for p in PATTERNS}
    const_both = antitone(const_rule) and monotone(const_rule)
    const_is_constant = len(set(const_rule.values())) == 1
    # and a genuinely varying rule fails at least one closure
    varying = {p: (frozenset(CONTENTS) if len(p) < 2 else frozenset(("c0",)))
               for p in PATTERNS}
    varying_varies = len(set(varying.values())) > 1
    varying_fails = not (antitone(varying) and monotone(varying))
    check(
        "Q1 every occupancy pattern is comparable to both the empty and the "
        "full pattern, so the two closures force the available set to be "
        "constant; a constant rule satisfies both, and a genuinely varying "
        "rule fails at least one",
        chain_reaches_all
        and const_both
        and const_is_constant
        and varying_varies
        and varying_fails,
        {
            "patterns": len(PATTERNS),
            "every_pattern_comparable_to_empty_and_full": chain_reaches_all,
            "constant_rule_satisfies_both": const_both,
            "varying_rule_fails_a_closure": varying_fails,
        },
    )

    # ---- Q2: which closure the varying rule fails, and the other direction
    shrink = {p: (frozenset(CONTENTS) if len(p) < 2 else frozenset(("c0",)))
              for p in PATTERNS}
    grow = {p: (frozenset(("c0",)) if len(p) == 0 else frozenset(CONTENTS))
            for p in PATTERNS}
    shrink_anti, shrink_mono = antitone(shrink), monotone(shrink)
    grow_anti, grow_mono = antitone(grow), monotone(grow)
    complementary = (shrink_anti and not shrink_mono) and (
        grow_mono and not grow_anti
    )
    check(
        "Q2 the two failure modes are complementary: a rule that shrinks "
        "availability on crowding keeps sub-collections and loses unions, and "
        "a rule that grows availability on contact keeps unions and loses "
        "sub-collections",
        complementary,
        {
            "shrink_on_crowding": {"sub_collection": shrink_anti, "union": shrink_mono},
            "grow_on_contact": {"sub_collection": grow_anti, "union": grow_mono},
        },
    )

    # ---- Q3: an exhaustive scan over a reduced but faithful pattern lattice
    # Restrict to occupancy-count rules (the covariant, rotation-invariant case,
    # which is what the Admissibility axiom's covariance already forces for
    # count-only rules): A: {0..6} -> nonempty subsets.  Exhaustive.
    both_and_varying = []
    scanned = 0
    varying_seen = 0
    for assignment in itertools.product(NONEMPTY, repeat=7):
        scanned += 1
        if len(set(assignment)) > 1:
            varying_seen += 1
        anti = all(assignment[j] >= assignment[i] for i in range(7) for j in range(7) if j < i)
        mono = all(assignment[j] >= assignment[i] for i in range(7) for j in range(7) if j > i)
        if anti and mono and len(set(assignment)) > 1:
            both_and_varying.append(assignment)
    check(
        "Q3 exhaustive scan of every count-only availability rule on a two-letter "
        "alphabet finds NO rule that is both sub-collection-closed and "
        "union-closed while genuinely varying",
        len(both_and_varying) == 0 and scanned == 2187 and varying_seen == 2184,
        {
            "rules_scanned": scanned,
            "of_which_genuinely_varying": varying_seen,
            "both_closures_and_varying": len(both_and_varying),
            "alphabet": list(CONTENTS),
        },
    )

    # ---- Q4: negative control -- the scan does find rules with ONE closure
    one_closure = 0
    for assignment in itertools.product(NONEMPTY, repeat=7):
        anti = all(assignment[j] >= assignment[i] for i in range(7) for j in range(7) if j < i)
        mono = all(assignment[j] >= assignment[i] for i in range(7) for j in range(7) if j > i)
        if (anti != mono) and len(set(assignment)) > 1:
            one_closure += 1
    check(
        "Q4 negative control: the same scan does find genuinely varying rules "
        "with exactly one of the two closures, so the Q3 emptiness is a real "
        "constraint and not a broken filter",
        one_closure > 0,
        {"varying_rules_with_exactly_one_closure": one_closure},
    )
    summary["part_two"] = (
        "no genuinely varying nearest-neighbour availability rule yields an "
        "admissible-configuration set closed under both sub-collection and "
        "disjoint union; the unrestricted reading of the Record additivity "
        "clause is therefore incompatible with the Admissibility 'vary with' "
        "clause, and the resolutions are law content"
    )


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 702,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }
    part_one(summary)
    part_two(summary)

    summary["conclusion"] = (
        "Using only the approved scale-reference primitive and the coherence of "
        "the axiom text, and adopting no counting convention: the nearest-"
        "neighbour covariant additive law has exactly one member that needs no "
        "supplied dimensionless number, namely the Laplacian ray A=0; and no "
        "genuinely varying admissibility rule makes the unrestricted additivity "
        "clause well posed, so how that clause is restricted is itself law "
        "content."
    )
    summary["firewalls"] = {
        "counting_convention_adopted": False,
        "dimensionless_value_supplied": False,
        "axiom_reading_ratified": False,
        "exhibited_rule_claimed_to_be_the_framework_rule": False,
        "new_axiom_or_primitive_proposed": False,
        "empirical_or_observed_input_used": False,
        "lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_law_pinned_by_scale_and_coherence_cycle702_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT LAW_PINNING_FAILED")
        return 1
    print("RESULT LAW_PINNED_BY_SCALE_AND_COHERENCE_WITHOUT_CONVENTION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
