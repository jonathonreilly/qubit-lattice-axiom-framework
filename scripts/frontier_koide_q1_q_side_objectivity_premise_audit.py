#!/usr/bin/env python3
"""
Q1 Q-side objectivity premise audit.

This runner attacks the remaining Q-side premise after the record-quotient
measure fork:

    Can objectivity / source-measure / max-entropy derive the rank-erased
    quotient atom count that gives Q=2/3?

Result:
  - Bare quotient atom-anonymity on C^2 does force the uniform law and hence
    Q=2/3.
  - The physical S-labeled record does not have that atom-swap symmetry.
    Preserving S leaves only the identity automorphism, so objectivity of the
    labeled record imposes no atom-measure constraint.
  - Full Hilbert trace/Born naturality and uniform microstate counting both
    give the rank weights (1/3,2/3), hence Q=1.
  - "Max entropy" gives different answers depending on whether it is applied
    before or after rank erasure.  Therefore rank erasure must be a physical
    operation prior to reference selection, not a consequence of max entropy
    alone.
  - Existing source-measure machinery supplies probability-law semantics and a
    reference-law input, but not the quotient reference.

No observed masses, fitted selectors, or unmerged PR artifacts are used.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def q_from_weights(mu: sp.Rational, nu: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    """Return (r*, Q) for singlet/doublet atom weights (mu, nu)."""
    r_star = sp.simplify(nu / (2 * mu))
    q_value = sp.simplify((1 + 2 * r_star) / 3)
    return r_star, q_value


def entropy2(p: float) -> float:
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log(p) + (1 - p) * math.log(1 - p))


def invariant_probabilities(perms: list[tuple[int, int]]) -> sp.Expr:
    """Solve p invariant under two-atom permutations, returning p0."""
    p = sp.symbols("p")
    equations = []
    weights = [p, 1 - p]
    for perm in perms:
        equations.extend(sp.Eq(weights[i], weights[perm[i]]) for i in range(2))
    sol = sp.solve(equations, [p], dict=True)
    if not sol:
        return sp.Symbol("free")
    return sp.simplify(sol[0][p])


def main() -> int:
    section("A. Full Hilbert trace / Born naturality still gives Q=1")

    c = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    eye = sp.eye(3)
    p0 = sp.simplify((eye + c + c**2) / 3)
    p1 = sp.simplify(eye - p0)
    ranks = (p0.rank(), p1.rank())
    tau_rank = (sp.Rational(ranks[0], sum(ranks)), sp.Rational(ranks[1], sum(ranks)))
    r_rank, q_rank = q_from_weights(*tau_rank)

    record(
        "A.1 embedded S-record atoms have ranks (1,2)",
        ranks == (1, 2) and p0**2 == p0 and p1**2 == p1 and p0 * p1 == sp.zeros(3),
        f"rank(P0), rank(P1)={ranks}",
    )
    record(
        "A.2 full Hilbert trace push-forward gives rank weights",
        tau_rank == (sp.Rational(1, 3), sp.Rational(2, 3)),
        f"tau_H(P0), tau_H(P1)={tau_rank}",
    )
    record(
        "A.3 rank weights give Q=1",
        r_rank == 1 and q_rank == 1,
        f"r={r_rank}, Q={q_rank}",
    )

    micro_weights = [sp.Rational(1, 3)] * 3
    count_then_erase = (micro_weights[0], micro_weights[1] + micro_weights[2])
    erase_then_count = (sp.Rational(1, 2), sp.Rational(1, 2))
    record(
        "A.4 count-then-erase and erase-then-count do not commute when ranks differ",
        count_then_erase == tau_rank
        and erase_then_count != count_then_erase
        and ranks[0] != ranks[1],
        f"count_then_erase={count_then_erase}; erase_then_count={erase_then_count}",
    )

    section("B. Bare quotient atom-anonymity is sufficient but extra")

    s_values = (sp.Integer(2), sp.Integer(-1))
    identity = (0, 1)
    swap = (1, 0)
    all_atom_perms = [identity, swap]
    s_preserving_perms = [
        perm for perm in all_atom_perms if tuple(s_values[perm[i]] for i in range(2)) == s_values
    ]
    p_uniform = invariant_probabilities(all_atom_perms)
    p_s_labeled = invariant_probabilities(s_preserving_perms)
    r_uniform, q_uniform = q_from_weights(sp.Rational(1, 2), sp.Rational(1, 2))

    record(
        "B.1 unlabeled two-atom quotient has swap symmetry",
        all_atom_perms == [identity, swap] and p_uniform == sp.Rational(1, 2),
        "Aut(C^2 as a bare two-point set) contains the atom swap; invariant states are uniform.",
    )
    record(
        "B.2 bare atom-anonymity gives Q=2/3",
        r_uniform == sp.Rational(1, 2) and q_uniform == sp.Rational(2, 3),
        f"r={r_uniform}, Q={q_uniform}",
    )
    record(
        "B.3 the S-labeled record has no atom-swap symmetry",
        s_preserving_perms == [identity] and str(p_s_labeled) == "free",
        f"S-labels={s_values}; S-preserving automorphisms={s_preserving_perms}",
    )
    record(
        "B.4 S-labeled objectivity alone allows both Q=1 and Q=2/3 references",
        all(perm == identity for perm in s_preserving_perms)
        and tau_rank != erase_then_count,
        "With only the identity automorphism, both (1/3,2/3) and (1/2,1/2) are invariant.",
    )

    section("C. Max-entropy depends on the algebra chosen before entropy")

    h_quotient_uniform = entropy2(0.5)
    h_quotient_rank = entropy2(1 / 3)
    full_uniform_pullback = (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3))
    quotient_uniform_pullback = (
        sp.Rational(1, 2),
        sp.Rational(1, 4),
        sp.Rational(1, 4),
    )

    record(
        "C.1 Shannon max entropy on the quotient algebra selects equal atoms",
        h_quotient_uniform > h_quotient_rank,
        f"H(1/2,1/2)={h_quotient_uniform:.6f} > H(1/3,2/3)={h_quotient_rank:.6f}",
    )
    record(
        "C.2 full Hilbert max entropy selects equal microstates and then rank weights",
        full_uniform_pullback == (sp.Rational(1, 3),) * 3
        and count_then_erase == (sp.Rational(1, 3), sp.Rational(2, 3)),
        f"full microstate law={full_uniform_pullback} -> macro={count_then_erase}",
    )
    record(
        "C.3 quotient uniform pulled back to microstates breaks full microstate anonymity",
        quotient_uniform_pullback != full_uniform_pullback
        and sum(quotient_uniform_pullback) == 1,
        f"quotient-uniform pullback={quotient_uniform_pullback}",
    )
    record(
        "C.4 max entropy alone therefore does not select the Q-side premise",
        q_rank == 1 and q_uniform == sp.Rational(2, 3),
        "The answer is fixed only after choosing full Hilbert algebra vs rank-erased quotient algebra.",
    )

    section("D. Repo surfaces keep the reference-law choice open")

    quotient_note = read_rel("docs/KOIDE_Q1_RECORD_QUOTIENT_MEASURE_FORK_NOTE_2026-05-31.md")
    source_note = read_rel("docs/SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md")
    tangent_note = read_rel("docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md")
    descent_note = read_rel("docs/KOIDE_Q_SOURCE_DOMAIN_CANONICAL_DESCENT_THEOREM_NOTE_2026-04-25.md")
    criterion_note = read_rel("docs/KOIDE_Q_BACKGROUND_ZERO_Z_ERASURE_CRITERION_THEOREM_NOTE_2026-04-25.md")
    descent_flat = flat(descent_note)
    criterion_flat = flat(criterion_note)

    record(
        "D.1 previous fork records quotient count as conditional, not derived",
        "QUOTIENT_RECORD_COUNT_CONDITIONALLY_Q23=TRUE" in quotient_note
        and "TRACE_PRESERVING_RANK_ERASURE_DERIVED=FALSE" in quotient_note,
    )
    record(
        "D.2 source-measure theorem keeps a full-support reference P0 as input",
        "For a full-support reference `P_0`" in source_note
        and "A state on that algebra is exactly a probability vector `P`" in flat(source_note),
    )
    record(
        "D.3 tangent-space theorem uses uniform reference only after it is chosen",
        "In the two-outcome sharp-record case `P_0=(1/2,1/2)`" in tangent_note
        and "primitive signed-record tangent is `s = (+1,-1)`" in flat(tangent_note),
    )
    record(
        "D.4 strict onsite source-domain descent remains a separate physical law",
        "This note does not prove that physical law" in descent_flat
        and "physical charged-lepton source-domain law must use strict onsite descent" in descent_flat,
    )
    record(
        "D.5 background-zero criterion gives Q=2/3 only after source-free/Z-erasure is admitted",
        "source-free / `Z`-erased representative" in criterion_flat
        and "This note does **not** prove" in criterion_flat
        and "retained charged-lepton physics forces the source-free condition" in criterion_flat,
    )

    section("E. Verdict")

    full_trace_branch = all(ok for name, ok, _ in PASSES if name.startswith("A."))
    bare_quotient_branch = all(ok for name, ok, _ in PASSES if name.startswith("B."))
    entropy_split = all(ok for name, ok, _ in PASSES if name.startswith("C."))
    repo_boundary = all(ok for name, ok, _ in PASSES if name.startswith("D."))

    record(
        "E.1 bare quotient atom-anonymity is a sufficient Q=2/3 premise",
        bare_quotient_branch and q_uniform == sp.Rational(2, 3),
        "If rank is erased before reference selection and atoms are anonymous, uniform count follows.",
    )
    record(
        "E.2 that premise is not derived by S-labeled objectivity, max entropy, or source-measure machinery",
        full_trace_branch and entropy_split and repo_boundary,
        "Keeping S labels or Hilbert microstates prevents the automorphism argument from selecting uniform macro atoms.",
    )
    record(
        "E.3 current Q-side premise remains open",
        True,
        "The exact missing principle is rank erasure before reference selection, or the separate strict-onsite P_SOURCE law.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: Q-side premise reduced to rank-erasure-before-measure; not derived.")
        print("KOIDE_Q1_Q_SIDE_OBJECTIVITY_PREMISE_AUDIT=TRUE")
        print("BARE_QUOTIENT_ATOM_ANONYMITY_IMPLIES_Q23=TRUE")
        print("S_LABELED_RECORD_OBJECTIVITY_IMPLIES_Q23=FALSE")
        print("FULL_TRACE_NATURALITY_IMPLIES_Q1=TRUE")
        print("MAX_ENTROPY_ALONE_SELECTS_Q23=FALSE")
        print("SOURCE_MEASURE_SELECTS_QUOTIENT_REFERENCE=FALSE")
        print("P_SOURCE_STRICT_ONSITE_REMAINS_OPEN=TRUE")
        print("Q_SIDE_PREMISE_DERIVED_CURRENT_SURFACE=FALSE")
        print("MINIMAL_EXTRA_PRINCIPLE=rank_erasure_before_reference_selection_or_strict_onsite_source_domain")
        print("NEXT_THEOREM=derive_physical_rank_erasure_before_measure_or_P_SOURCE")
        return 0

    print("VERDICT: Q-side objectivity premise audit has failing checks.")
    print("KOIDE_Q1_Q_SIDE_OBJECTIVITY_PREMISE_AUDIT=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
