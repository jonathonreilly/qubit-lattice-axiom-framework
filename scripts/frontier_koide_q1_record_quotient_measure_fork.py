#!/usr/bin/env python3
"""
Q1 record-quotient measure fork theorem.

This runner tests the next possible bridge after the S-record no-go:

    Can existing source-measure / record-intervention machinery make the
    charged-lepton readout ignore Hilbert rank and count record atoms equally?

Result:
  - The full Hilbert trace/Born push-forward through the sharp record
    S=C+C^2 gives atom weights (1/3, 2/3), hence the Q=1 lane.
  - The abstract quotient record algebra C^2 has a counting/max-entropy
    reference (1/2, 1/2), hence the conditional Q=2/3 lane.
  - Those are different reference laws.  Because the two embedded projectors
    have ranks (1,2), the quotient counting trace is not the pullback of the
    full Hilbert trace.
  - Existing finite sharp-record source-measure theorems justify probability
    interventions on the record algebra, but they do not select the quotient
    reference law.  The missing physical principle is exactly rank-erasing
    recordization / count-on-record-atoms.

No PDG masses, fitted selectors, observed lepton inputs, or unmerged PR
artifacts are used.
"""

from __future__ import annotations

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
    """Return (r*, Q) for singlet/doublet weights (mu, nu)."""
    r_star = sp.simplify(nu / (2 * mu))
    q_value = sp.simplify((1 + 2 * r_star) / 3)
    return r_star, q_value


def fisher_unit_for_binary_reference(p0: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    """Unit Fisher score in the binary direction for reference (p0, 1-p0)."""
    p1 = 1 - p0
    return sp.sqrt(p1 / p0), -sp.sqrt(p0 / p1)


def main() -> int:
    section("A. Embedded S-record algebra and full-Hilbert trace")

    c = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    c2 = c**2
    eye = sp.eye(3)
    s = c + c2
    p_singlet = sp.simplify((eye + c + c2) / 3)
    p_doublet = sp.simplify(eye - p_singlet)

    tau_h_p0 = sp.simplify(sp.trace(p_singlet) / 3)
    tau_h_p1 = sp.simplify(sp.trace(p_doublet) / 3)
    r_rank, q_rank = q_from_weights(tau_h_p0, tau_h_p1)

    record(
        "A.1 S=C+C^2 embeds the abstract two-atom record algebra by projectors",
        s == 2 * p_singlet - p_doublet
        and p_singlet**2 == p_singlet
        and p_doublet**2 == p_doublet
        and p_singlet * p_doublet == sp.zeros(3),
        "iota(e0)=P0, iota(e1)=P1.",
    )
    record(
        "A.2 the embedded atoms have unequal Hilbert ranks (1,2)",
        p_singlet.rank() == 1 and p_doublet.rank() == 2,
        f"rank(P0)={p_singlet.rank()}, rank(P1)={p_doublet.rank()}",
    )
    record(
        "A.3 full-Hilbert normalized trace pushes forward to rank weights",
        tau_h_p0 == sp.Rational(1, 3) and tau_h_p1 == sp.Rational(2, 3),
        f"tau_H(P0), tau_H(P1)=({tau_h_p0}, {tau_h_p1})",
    )
    record(
        "A.4 rank/Born weights give r=1 and Q=1",
        r_rank == 1 and q_rank == 1,
        f"r={r_rank}, Q={q_rank}",
    )

    section("B. Abstract quotient record algebra and equal atom count")

    tau_q_e0 = sp.Rational(1, 2)
    tau_q_e1 = sp.Rational(1, 2)
    r_count, q_count = q_from_weights(tau_q_e0, tau_q_e1)
    x0, x1 = sp.symbols("x0 x1")
    tau_h_pullback = sp.simplify(tau_h_p0 * x0 + tau_h_p1 * x1)
    tau_q_count = sp.simplify((x0 + x1) / 2)

    record(
        "B.1 quotient counting/max-entropy law on two record atoms is uniform",
        tau_q_e0 == tau_q_e1 == sp.Rational(1, 2),
        "This is the abstract C^2 record-atom count, not the embedded Hilbert trace.",
    )
    record(
        "B.2 equal record-atom count gives r=1/2 and Q=2/3",
        r_count == sp.Rational(1, 2) and q_count == sp.Rational(2, 3),
        f"r={r_count}, Q={q_count}",
    )
    record(
        "B.3 quotient count is not the pullback of full-Hilbert trace",
        sp.simplify(tau_h_pullback - tau_q_count) != 0
        and tau_h_p0 != tau_q_e0
        and tau_h_p1 != tau_q_e1,
        f"tau_H o iota = {tau_h_pullback}; tau_count = {tau_q_count}",
    )
    record(
        "B.4 no trace-preserving rank-erasing embedding exists for this fixed S record",
        tau_h_p0 != sp.Rational(1, 2) and tau_h_p1 != sp.Rational(1, 2),
        "Preserving the embedded projectors P0,P1 keeps their ranks; erasing rank changes the reference law.",
    )

    section("C. Source-measure tangent geometry exposes the reference-law choice")

    eps = sp.Matrix([1, -1])
    p_uniform = (sp.Rational(1, 2), sp.Rational(1, 2))
    p_rank = (sp.Rational(1, 3), sp.Rational(2, 3))
    eps_mean_uniform = sp.simplify(sum(p_uniform[i] * eps[i] for i in range(2)))
    eps_norm_uniform = sp.simplify(sum(p_uniform[i] * eps[i] ** 2 for i in range(2)))
    eps_mean_rank = sp.simplify(sum(p_rank[i] * eps[i] for i in range(2)))
    eps_norm_rank = sp.simplify(sum(p_rank[i] * eps[i] ** 2 for i in range(2)))
    unit_rank = fisher_unit_for_binary_reference(p_rank[0])
    unit_rank_mean = sp.simplify(p_rank[0] * unit_rank[0] + p_rank[1] * unit_rank[1])
    unit_rank_norm = sp.simplify(p_rank[0] * unit_rank[0] ** 2 + p_rank[1] * unit_rank[1] ** 2)

    record(
        "C.1 signed record epsilon=(+1,-1) is unit only for the uniform atom reference",
        eps_mean_uniform == 0 and eps_norm_uniform == 1,
        f"uniform mean={eps_mean_uniform}, norm={eps_norm_uniform}",
    )
    record(
        "C.2 under rank/Born reference epsilon is not a valid zero-mean score tangent",
        eps_mean_rank == sp.Rational(-1, 3) and eps_norm_rank == 1,
        f"rank mean={eps_mean_rank}, norm={eps_norm_rank}",
    )
    record(
        "C.3 the rank/Born unit score is asymmetric, not (+1,-1)",
        unit_rank == (sp.sqrt(2), -sp.sqrt(2) / 2)
        and unit_rank_mean == 0
        and unit_rank_norm == 1,
        f"unit score for (1/3,2/3) is ({unit_rank[0]}, {unit_rank[1]}).",
    )
    record(
        "C.4 Fisher geometry therefore does not hide the measure choice",
        eps != sp.Matrix(unit_rank),
        "Uniform record reference and rank/Born reference produce different primitive score directions.",
    )

    section("D. Existing source-measure notes support record probabilities, not quotient selection")

    record_intervention = read_rel("docs/SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md")
    tangent_note = read_rel("docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md")
    pre_record = read_rel("docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md")
    q1_record_no_go = read_rel(
        "docs/KOIDE_Q1_SOURCE_ENDPOINT_RECORD_MEASURE_NO_GO_NOTE_2026-05-31.md"
    )
    record_intervention_flat = flat(record_intervention)
    pre_record_flat = flat(pre_record)

    record(
        "D.1 record-intervention theorem makes record-facing states probability laws",
        "record algebra is the commutative algebra of functions on `Omega`" in record_intervention_flat
        and "A state on that algebra is exactly a probability vector `P`" in record_intervention_flat,
    )
    record(
        "D.2 record-intervention theorem keeps a full-support reference P0 as input",
        "For a full-support reference `P_0`" in record_intervention,
    )
    record(
        "D.3 sharp-record tangent theorem's primitive epsilon uses uniform two-outcome reference",
        "In the two-outcome sharp-record case `P_0=(1/2,1/2)`" in tangent_note
        and "primitive signed-record tangent is `s = (+1,-1)`" in flat(tangent_note),
    )
    record(
        "D.4 current tracial theorem demotes physical pre-record identification to an open admission",
        "unique tracial state" in pre_record_flat
        and "pre-record identification half remains an open admission" in pre_record_flat
        and "demoted to a separate open admission" in pre_record_flat,
    )
    record(
        "D.5 Q1 S-record no-go already leaves the measure unforced",
        "C3_SHARP_RECORD_FORCES_WEIGHT_MEASURE=FALSE" in q1_record_no_go
        and "EQUAL_ATOM_Q23_AND_RANK_BORN_Q1_BOTH_C3_INVARIANT=TRUE" in q1_record_no_go,
    )

    section("E. Verdict")

    full_trace_default = all(ok for name, ok, _ in PASSES if name.startswith("A."))
    quotient_conditional = all(ok for name, ok, _ in PASSES if name.startswith("B."))
    tangent_exposes_choice = all(ok for name, ok, _ in PASSES if name.startswith("C."))
    repo_boundary = all(ok for name, ok, _ in PASSES if name.startswith("D."))

    record(
        "E.1 full-Hilbert trace gives the Q=1 branch",
        full_trace_default,
        "This is the rank/Born push-forward of the embedded sharp record.",
    )
    record(
        "E.2 quotient record counting would give Q=2/3, conditionally",
        quotient_conditional,
        "This requires rank-erasing recordization / count-on-atoms.",
    )
    record(
        "E.3 existing source-measure tangent geometry does not erase the choice",
        tangent_exposes_choice and repo_boundary,
        "It exposes P0 as the reference-law input.",
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
        print("VERDICT: record quotient isolates the exact measure bridge, but does not close it.")
        print("KOIDE_Q1_RECORD_QUOTIENT_MEASURE_FORK=TRUE")
        print("FULL_HILBERT_TRACE_PUSHFORWARD_Q1=TRUE")
        print("QUOTIENT_RECORD_COUNT_CONDITIONALLY_Q23=TRUE")
        print("TRACE_PRESERVING_RANK_ERASURE_DERIVED=FALSE")
        print("SOURCE_MEASURE_THEOREMS_SELECT_QUOTIENT_REFERENCE=FALSE")
        print("MISSING_PRINCIPLE=rank_erasing_recordization_or_count_on_record_atoms")
        print("P_SOURCE_CURRENT_SURFACE_CLOSURE=FALSE")
        print("P_ORIENT_FULL_CURRENT_SURFACE_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_physical_rank_erasing_record_quotient_or_strict_onsite_source_domain")
        return 0

    print("VERDICT: record quotient measure fork has failing checks.")
    print("KOIDE_Q1_RECORD_QUOTIENT_MEASURE_FORK=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
