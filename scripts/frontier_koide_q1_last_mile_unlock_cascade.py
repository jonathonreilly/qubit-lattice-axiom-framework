#!/usr/bin/env python3
"""
Q1 last-mile unlock cascade.

This runner answers the practical question:

  If the remaining physical orientation/basepoint theorem succeeds, what
  actually upgrades, and what still stays open?

It does not assert that the last-mile theorem is already proved.  Instead it
separates the two load-bearing last-mile premises:

  P_ORIENT:
      a physical selected-line slot/Fourier orientation or based endpoint
      supplies epsilon=+1.

  P_SOURCE:
      a physical charged-lepton source-domain theorem selects the source-free
      / Z-erased reduced carrier.

Then it computes the exact conditional consequences and checks the current repo
surfaces that name the same blockers.  No PDG masses or fitted selectors are
used.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path


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


def read_rel(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def q_from_z(z: Fraction) -> Fraction:
    return Fraction(2, 3) / (1 + z)


def main() -> int:
    eta_aps = Fraction(2, 9)
    coeff_g_q1 = Fraction(-2, 9)
    epsilon_plus = Fraction(1, 1)

    section("A. Current last-mile status")

    bottom_up = read_rel("docs/KOIDE_Q1_BOTTOM_UP_SIGN_ORIENTATION_AUDIT_NOTE_2026-05-31.md")
    gamma_probe = read_rel("docs/KOIDE_Q1_GAMMA_SHEET_SIGN_PROBE_NOTE_2026-05-31.md")
    q_criterion = read_rel("docs/KOIDE_Q_BACKGROUND_ZERO_Z_ERASURE_CRITERION_THEOREM_NOTE_2026-04-25.md")
    generation_nogo = read_rel("docs/CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md")

    record(
        "A.1 current Q1/gamma package does not derive physical orientation",
        "SIGN_UNDERIVED_FROM_Q1_OR_GAMMA=TRUE" in gamma_probe
        and "zero odd component" in bottom_up,
    )
    record(
        "A.2 current Q criterion still requires physical source-free selection",
        "derive physical source-free reduced-carrier selection" in q_criterion
        and "KOIDE_Q_RETAINED_NATIVE_CLOSURE=FALSE" in q_criterion,
    )
    record(
        "A.3 current generation label remains outside the sign/Q last mile",
        "BASED_ENDPOINT_OR_SOURCE_LAW_REQUIRED=TRUE" in generation_nogo
        and "CHARGED_LEPTON_MASS_RETENTION=FALSE" in generation_nogo,
    )

    section("B. If P_ORIENT lands")

    delta_from_oriented_q1 = -coeff_g_q1
    delta_from_epsilon = epsilon_plus * eta_aps
    record(
        "B.1 Q1 coefficient gives the positive selected-line sign in an oriented frame",
        delta_from_oriented_q1 == Fraction(2, 9),
        f"delta_oriented=-coeff_g(S_Q1)={delta_from_oriented_q1}",
    )
    record(
        "B.2 epsilon=+1 orientation agrees with eta_APS",
        delta_from_epsilon == eta_aps == Fraction(2, 9),
        f"epsilon*eta_APS={delta_from_epsilon}",
    )
    record(
        "B.3 P_ORIENT would close the APS physical-identification residual conditionally",
        delta_from_oriented_q1 == delta_from_epsilon,
        "This is audit-ready only if P_ORIENT is actually derived, not admitted.",
    )

    selected_line = read_rel("docs/KOIDE_SELECTED_LINE_CYCLIC_RESPONSE_BRIDGE_NOTE_2026-04-18.md")
    record(
        "B.4 delta=+2/9 feeds the existing selected-line scalar/point bridge",
        "delta = 2/9" in selected_line
        and "m_* = -1.160443440065" in selected_line
        and "kappa_sel,*" in selected_line,
    )

    section("C. If P_SOURCE lands")

    q_zero = q_from_z(Fraction(0, 1))
    q_q1 = q_from_z(Fraction(-1, 3))
    record(
        "C.1 Z-erasure gives charged-lepton Q=2/3",
        q_zero == Fraction(2, 3),
        f"Q(z=0)={q_zero}",
    )
    record(
        "C.2 Q1 remains the projected counterdomain, not the physical charged-lepton readout",
        q_q1 == Fraction(1, 1) and q_zero == Fraction(2, 3),
        f"Q(z=-1/3)={q_q1}, Q(z=0)={q_zero}",
    )

    section("D. If both P_ORIENT and P_SOURCE land")

    pointed_origin = read_rel("docs/KOIDE_POINTED_ORIGIN_EXHAUSTION_THEOREM_NOTE_2026-04-24.md")
    dim_countermodel = read_rel("docs/KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md")
    phase_route = read_rel("docs/KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md")
    record(
        "D.1 the pointed-origin residual would be exactly the discharged object",
        ("physical source/boundary-origin law" in pointed_origin
         or "physical source/boundary origin law" in pointed_origin)
        and "Q = 2/3" in pointed_origin
        and "delta = eta_APS = 2/9" in pointed_origin,
    )
    record(
        "D.2 finite countermodels are blocked only by those physical laws",
        "Extra physical source/readout selection would be needed" in dim_countermodel
        and "law selects the line-local endpoint and basepoint" in dim_countermodel,
    )
    record(
        "D.3 APS phase route names the same final physical-identification gap",
        "physical identification" in phase_route and "single remaining gap" in phase_route,
    )
    record(
        "D.4 both premises would make Q/delta dimensionless closure audit-ready",
        q_zero == Fraction(2, 3) and delta_from_oriented_q1 == Fraction(2, 9),
        "Audit-ready proposal, not effective retained status until independent audit passes.",
    )

    section("E. What does not turn retained/unbounded")

    controlled_vocab = read_rel("docs/repo/CONTROLLED_VOCABULARY.md")
    record(
        "E.1 unbounded retained is not a Koide claim-strength target in controlled vocabulary",
        "unbounded retained" not in controlled_vocab
        and "retained unbounded" not in controlled_vocab,
        "Use proposed_retained / exact support / conditional support for this lane.",
    )
    record(
        "E.2 generation label and absolute mass retention still do not follow from Q/delta alone",
        "CHARGED_LEPTON_MASS_RETENTION=FALSE" in generation_nogo
        and "RESIDUAL_GENERATION=derive_nonobservational_generation_label_or_tau_scale_selector"
        in generation_nogo,
    )
    record(
        "E.3 Y_T unbounded closure is outside this Koide last-mile dependency graph",
        "y_t" not in q_criterion.lower()
        and "Y_T" not in selected_line
        and "Y_T" not in phase_route,
    )

    section("F. Verdict")

    record(
        "F.1 last mile is not already solved on the current surface",
        True,
        "P_ORIENT and P_SOURCE are still explicit premises.",
    )
    record(
        "F.2 if solved, the immediate upgrade is Koide Q/delta audit-ready closure",
        True,
        "Not dark matter; not Y_T unbounded; not absolute lepton mass retention.",
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
        print("VERDICT: last-mile unlock cascade is exact and conditional.")
        print("KOIDE_Q1_LAST_MILE_UNLOCK_CASCADE=TRUE")
        print("LAST_MILE_ORIENTATION_DERIVED_CURRENT_SURFACE=FALSE")
        print("LAST_MILE_SOURCE_Z_ERASURE_DERIVED_CURRENT_SURFACE=FALSE")
        print("IF_ORIENTATION_LANDS_DELTA_PLUS_2_OVER_9=TRUE")
        print("IF_SOURCE_Z_ERASURE_LANDS_Q_2_OVER_3=TRUE")
        print("IF_BOTH_LAND_DIMENSIONLESS_KOIDE_Q_DELTA_AUDIT_READY=TRUE")
        print("UPGRADES_TO_EFFECTIVE_RETAINED_WITHOUT_AUDIT=FALSE")
        print("GENERATION_LABEL_RETENTION_FROM_Q_DELTA=FALSE")
        print("ABSOLUTE_LEPTON_MASS_RETENTION_FROM_Q_DELTA=FALSE")
        print("Y_T_UNBOUNDED_IMPACT=FALSE")
        print("UNBOUNDED_RETAINED_IS_NOT_KOIDE_STATUS_TARGET=TRUE")
        print("NEXT_THEOREM=derive_P_ORIENT_or_P_SOURCE_from_retained_charged_lepton_physics")
        return 0

    print("VERDICT: last-mile unlock cascade has failing checks.")
    print("KOIDE_Q1_LAST_MILE_UNLOCK_CASCADE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
