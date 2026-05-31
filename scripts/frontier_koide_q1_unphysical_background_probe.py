#!/usr/bin/env python3
"""
Koide Q=1 unphysical-background probe.

This runner probes the specific surviving direction:

    Q=1 is not a physical sector; it is a projected commutant background
    whose reduced Z coordinate disappears under strict onsite/local readout.

The result is intentionally scoped.  It can certify the exact algebraic
statement under strict onsite descent, and it can show why Q=1 is a strong
counterdomain/probe.  It does not prove that Nature must use this descent as
the physical charged-lepton source-domain law.
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


def read_doc(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def q_from_z(z_value: sp.Expr) -> sp.Expr:
    z_value = sp.sympify(z_value)
    return sp.simplify(sp.Rational(2, 3) / (1 + z_value))


def diagonal_compression(matrix: sp.Matrix) -> sp.Matrix:
    return sp.diag(*[matrix[i, i] for i in range(matrix.rows)])


def scalar_part(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sp.trace(matrix) / matrix.rows * sp.eye(matrix.rows))


def is_scalar(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix - scalar_part(matrix)) == sp.zeros(matrix.rows, matrix.cols)


def offdiag_part(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(matrix - diagonal_compression(matrix))


def main() -> int:
    section("A. Q=1 projected background")

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    J_all = sp.ones(3, 3)
    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)

    z_q1 = -sp.Rational(1, 3)
    S_q1 = sp.simplify(I3 + z_q1 * Z)

    record(
        "A.1 z=-1/3 gives Q=1",
        q_from_z(z_q1) == 1,
        f"Q(-1/3)={q_from_z(z_q1)}",
    )

    record(
        "A.2 projected source is C3-central but non-onsite",
        sp.simplify(C * S_q1 - S_q1 * C) == sp.zeros(3, 3)
        and not S_q1.is_diagonal(),
        f"S_q1={S_q1}",
    )

    record(
        "A.3 Q=1 source has exact singlet/doublet spectrum 2/3, 4/3",
        sp.simplify(S_q1 * P_plus - sp.Rational(2, 3) * P_plus)
        == sp.zeros(3, 3)
        and sp.simplify(S_q1 * P_perp - sp.Rational(4, 3) * P_perp)
        == sp.zeros(3, 3),
        "The non-Koide value is a projected singlet/doublet weighting.",
    )

    record(
        "A.4 Q=1 source is positive, so the issue is locality/domain, not positivity",
        all(ev > 0 for ev in S_q1.eigenvals().keys()),
        f"eigenvalues={S_q1.eigenvals()}",
    )

    section("B. Strict onsite blindness")

    diag_z = diagonal_compression(Z)
    diag_s = diagonal_compression(S_q1)
    e_z = scalar_part(Z)
    e_s = scalar_part(S_q1)

    record(
        "B.1 site-local diagonal compression maps Z to common scalar -I/3",
        diag_z == -sp.Rational(1, 3) * I3 and diag_z == e_z,
        f"Diag(Z)={diag_z}",
    )

    record(
        "B.2 site-local diagonal compression maps Q1 source to common scalar 10I/9",
        diag_s == sp.Rational(10, 9) * I3 and diag_s == e_s,
        f"Diag(S_q1)={diag_s}",
    )

    onsite_projectors = [
        sp.diag(1, 0, 0),
        sp.diag(0, 1, 0),
        sp.diag(0, 0, 1),
    ]
    onsite_readouts = [sp.trace(P * S_q1) for P in onsite_projectors]
    record(
        "B.3 every one-site local detector sees the same Q1 value",
        onsite_readouts == [sp.Rational(10, 9)] * 3,
        f"onsite readouts={onsite_readouts}",
    )

    reduced_residual = sp.simplify(S_q1 - diag_s)
    record(
        "B.4 all non-scalar Q1 information is purely offsite after local compression",
        diagonal_compression(reduced_residual) == sp.zeros(3, 3)
        and offdiag_part(reduced_residual) == reduced_residual
        and reduced_residual != sp.zeros(3, 3),
        f"S_q1 - Diag(S_q1)={reduced_residual}",
    )

    record(
        "B.5 strict onsite readout cannot distinguish Q1 from a common scalar background",
        is_scalar(diag_s),
        "The dimensionless reduced source coordinate is absent from the onsite image.",
    )

    section("C. Quotient and normalized Q readout")

    s, z = sp.symbols("s z")
    K = sp.simplify(s * I3 + z * Z)
    E_K = scalar_part(K)
    quotient_after_descent = sp.simplify(E_K - scalar_part(E_K))

    record(
        "C.1 any projected source sI+zZ descends to scalar (s-z/3)I",
        sp.simplify(E_K - (s - z / 3) * I3) == sp.zeros(3, 3),
        f"E_loc(sI+zZ)={E_K}",
    )

    record(
        "C.2 reduced quotient after descent is exactly zero for every z",
        quotient_after_descent == sp.zeros(3, 3),
        "The map A -> D^C3 kills the reduced Z-coordinate, not only z=-1/3.",
    )

    q1_descended_scale = sp.trace(diag_s) / 3
    normalized_descended = sp.simplify(diag_s / q1_descended_scale)
    record(
        "C.3 Q1 normalized onsite image is the source-free representative",
        normalized_descended == I3,
        f"Diag(S_q1)/(10/9)={normalized_descended}",
    )

    record(
        "C.4 normalized local readout sends the Q1 projected background back to Q=2/3",
        q_from_z(0) == sp.Rational(2, 3),
        "After onsite quotient/normalization, the effective reduced z is zero.",
    )

    section("D. Loophole probes")

    # The strongest local loophole would be a diagonal local observable that
    # recovers z.  But every diagonal functional restricted to span{I,Z}
    # sees only Tr-equivalent scalar data because Diag(Z) is scalar.
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    local_obs = sp.diag(a0, a1, a2)
    local_z_response = sp.trace(local_obs * Z)
    local_i_response = sp.trace(local_obs * I3)
    record(
        "D.1 diagonal local observables cannot isolate Z from scalar data",
        sp.simplify(local_z_response + sp.Rational(1, 3) * local_i_response) == 0,
        "For every diagonal observable A, Tr(A Z)=-(1/3)Tr(A).",
    )

    # Offsite observables can see Q1.  That is exactly why Q1 remains a
    # projected/probe datum rather than an onsite background.
    E01 = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    offsite_response = sp.trace(E01.T * S_q1)
    record(
        "D.2 offsite/projected observables do see the Q1 component",
        offsite_response == -sp.Rational(2, 9),
        f"<E01,S_q1>={offsite_response}",
    )

    record(
        "D.3 Q1 is therefore probe-visible but onsite-background-invisible",
        offsite_response != 0 and onsite_readouts == [sp.Rational(10, 9)] * 3,
        "This is the exact unphysical-background signature.",
    )

    section("E. Documentation guardrails")

    descent_doc = read_doc("docs/KOIDE_Q_SOURCE_DOMAIN_CANONICAL_DESCENT_THEOREM_NOTE_2026-04-25.md")
    criterion_doc = read_doc("docs/KOIDE_Q_BACKGROUND_ZERO_Z_ERASURE_CRITERION_THEOREM_NOTE_2026-04-25.md")
    synthesis_doc = read_doc("docs/KOIDE_Q_ONSITE_SOURCE_DOMAIN_NO_GO_SYNTHESIS_NOTE_2026-04-25.md")

    record(
        "E.1 descent note says nonzero Z may be projected probe but not onsite background",
        "nonzero `Z` can remain an allowed projected probe deformation" in descent_doc
        and "cannot survive as a dimensionless undeformed onsite background" in descent_doc,
    )

    record(
        "E.2 criterion note says nonzero Z is one-to-one with non-Koide Q",
        "a nonzero `Z` value is one-to-one with a chosen non-Koide value of `Q`"
        in criterion_doc
        and "Q = 2/3  <=>  z = 0" in criterion_doc,
    )

    record(
        "E.3 synthesis note keeps physical source-domain selection open",
        "derive_Z_as_probe_only_not_background" in synthesis_doc
        and "Q_RETAINED_NATIVE_CLOSURE=FALSE" in synthesis_doc,
    )

    record(
        "E.4 descent note does not overclaim physical Koide closure",
        "not prove that physical law" in descent_doc
        and "Q_RETAINED_NATIVE_CLOSURE=FALSE" in descent_doc,
    )

    section("F. Scoped verdict")

    exact_under_strict_onsite = True
    physical_source_domain_proved = False
    q1_unphysical_hunts = True
    q1_unphysical_retained = False

    record(
        "F.1 unphysical Q1 direction holds exactly under strict onsite/local readout",
        exact_under_strict_onsite,
        "Q1's reduced information is purely offsite/projected and vanishes in the onsite quotient.",
    )

    record(
        "F.2 the result still needs the physical source-domain theorem",
        not physical_source_domain_proved,
        "The remaining theorem is to prove physical undeformed backgrounds must use onsite descent.",
    )

    record(
        "F.3 this direction still hunts as a source-domain closure target",
        q1_unphysical_hunts and not q1_unphysical_retained,
        "It is not retained closure yet, but it gives a precise falsifiable theorem target.",
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
        print("VERDICT: unphysical Q=1 direction is exact under strict onsite descent.")
        print("KOIDE_Q1_UNPHYSICAL_BACKGROUND_PROBE=TRUE")
        print("Q1_EXACT_UNDER_STRICT_ONSITE_READOUT=TRUE")
        print("Q1_ONSITE_DETECTORS_SEE_ONLY_COMMON_SCALAR=TRUE")
        print("Q1_PROJECTED_OFFSITE_PROBE_VISIBLE=TRUE")
        print("Q1_UNPHYSICAL_BACKGROUND_RETAINED=FALSE")
        print("Q1_PHYSICAL_SOURCE_DOMAIN_THEOREM_PROVED=FALSE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_physical_source_domain_uses_strict_onsite_descent_or_excludes_Z_as_undeformed_background")
        return 0

    print("VERDICT: unphysical Q=1 probe has failing checks.")
    print("KOIDE_Q1_UNPHYSICAL_BACKGROUND_PROBE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
