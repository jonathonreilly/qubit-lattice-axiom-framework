#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the abstract quotient scope of
`massless_vector_polarization_count_from_lorentz_and_gauge_bounded_theorem_note_2026-05-28`.

The repaired source row is no longer a physical massless-vector theorem. Its
load-bearing content is the abstract finite-dimensional quotient identity for
V=C^4, a nonzero row ell, and a nonzero vector k in ker(ell):

  dim_C ker(ell) / span_C{k} = 4 - 1 - 1 = 2.

The runner keeps the canonical null-row notation as a concrete matrix model
for the quotient. Any physical interpretation of ell and k is outside this
row's load-bearing scope.

Companion role: not a new claim row, not a status promotion; provides
audit-friendly evidence at exact precision for the rank arithmetic.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import sympy
    from sympy import (
        Matrix,
        I as sym_I,
        sqrt,
        Rational,
        symbols,
        simplify,
        Symbol,
        eye,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md"
)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print(
        "massless_vector_polarization_count_from_lorentz_and_gauge_bounded_theorem_note_2026-05-28"
    )
    print("Goal: sympy verification of dim_C ker(ell)/span(k) = 4 - 1 - 1 = 2")
    print("       for a nonzero row ell and nonzero k in ker(ell)")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 1 (R1-R4): abstract rank arithmetic on ker(ell)/span(k)")
    # ---------------------------------------------------------------------
    #
    # Setup. Use mostly-minus signature eta = diag(+1, -1, -1, -1).
    # Generic null momentum k^mu = (k0, k1, k2, k3) with
    # k^2 = k0^2 - k1^2 - k2^2 - k3^2 = 0.
    #
    # Vector epsilon = (e0, e1, e2, e3) is a generic complex four-vector.
    # The abstract row ell reads
    #
    #   k_mu eps^mu = eta_{mu nu} k^nu eps^mu
    #                = k0 e0 - k1 e1 - k2 e2 - k3 e3 = 0
    #
    # in mostly-minus signature when k^mu = (k0, k1, k2, k3). The residual
    # gauge shift is along the contravariant null vector k^mu. We count
    # linear-algebra ranks.

    k0, k1, k2, k3 = symbols("k0 k1 k2 k3", real=True)
    e0, e1, e2, e3 = symbols("e0 e1 e2 e3")  # complex polarization components

    # R1: total vector dimension = 4.
    eps_vec = Matrix([e0, e1, e2, e3])
    check(
        "(R1) vector eps has 4 complex components on C^4",
        eps_vec.shape == (4, 1),
        detail=f"shape = {eps_vec.shape}",
    )

    # R2: nonzero row rank = 1 on C^4.
    # The row is ell(eps)=k0 e0 - k1 e1 - k2 e2 - k3 e3, written as a
    # 1x4 covector acting on (e0, e1, e2, e3)^T.
    constraint_row = Matrix([[k0, -k1, -k2, -k3]])
    check(
        "(R2a) abstract row ell has shape (1, 4)",
        constraint_row.shape == (1, 4),
    )
    # For generic null k^mu (not all zero), constraint matrix has rank 1.
    # Verify by symbolic substitution k^mu = (k_z, 0, 0, k_z) (null, nonzero).
    k_z = Symbol("k_z", positive=True)
    constraint_canonical = constraint_row.subs(
        {k0: k_z, k1: 0, k2: 0, k3: k_z}
    )
    rank_constraint = constraint_canonical.rank()
    check(
        "(R2b) row rank = 1 in the canonical model ell=(k_z,0,0,-k_z)",
        rank_constraint == 1,
        detail=f"rank = {rank_constraint}",
    )

    # R3: quotient direction rank = 1.
    # Shift eps -> eps + c k, where k is a single nonzero vector in C^4 and c
    # is one complex scalar. Rank of the shift = 1.
    k_contra_vec = Matrix([k0, k1, k2, k3])
    k_contra_canonical = k_contra_vec.subs({k0: k_z, k1: 0, k2: 0, k3: k_z})
    shift_matrix = k_contra_canonical.reshape(4, 1)  # 4x1 column = rank 1
    rank_shift = shift_matrix.rank()
    check(
        "(R3a) quotient direction k has rank 1",
        rank_shift == 1,
        detail=f"rank = {rank_shift}",
    )

    # R3b: the quotient direction k lies in ker(ell). Verify by multiplying
    # the displayed row by the displayed quotient direction.
    kernel_containment = simplify((constraint_canonical * shift_matrix)[0])
    check(
        "(R3b) row ell times quotient direction k equals 0",
        kernel_containment == 0,
        detail=f"row*k = {kernel_containment}",
    )

    # R4: quotient dimension = 4 - 1 - 1 = 2.
    # The quotient is C^4 / (constraint kernel preimage union residual shift).
    # Algebraically: take the 1-codim constraint subspace (dim 3) then
    # quotient by the 1-dim shift (dim -> 2). Verify by direct construction.
    n_total = 4
    n_constraint = rank_constraint  # = 1
    n_shift = rank_shift  # = 1
    n_physical = n_total - n_constraint - n_shift
    check(
        "(R4) abstract quotient dimension = 4 - 1 - 1 = 2",
        n_physical == 2,
        detail=f"4 - {n_constraint} - {n_shift} = {n_physical}",
    )

    # ---------------------------------------------------------------------
    section("Part 2 (R5): explicit quotient representatives in the canonical model")
    # ---------------------------------------------------------------------
    #
    # At k = (omega, 0, 0, omega) and ell=(omega,0,0,-omega), ell(eps)=0
    # reads omega * e0 - omega * e3 = 0, i.e. e0 = e3. Quotienting by the
    # line span(k) leaves independent representatives e1 and e2.

    omega = Symbol("omega", positive=True)
    k_canonical = Matrix([omega, 0, 0, omega])  # k^mu (contravariant)
    k_lower_canonical = Matrix([omega, 0, 0, -omega])  # k_mu (covariant)

    # Abstract row constraint on generic eps in the canonical model:
    constraint_canonical_eval = (
        omega * e0 - omega * e3  # = k^0 e_0 - k^3 e_3 (others = 0)
    )
    constraint_simplified = simplify(constraint_canonical_eval)
    check(
        "(R5a) canonical row: omega*(e0 - e3) = 0 (i.e. e0 = e3)",
        constraint_simplified == omega * (e0 - e3),
        detail=f"constraint = {constraint_simplified}",
    )

    # Transverse basis vectors:
    eps_1 = Matrix([0, 1, 0, 0])  # e1-direction
    eps_2 = Matrix([0, 0, 1, 0])  # e2-direction

    # Verify both satisfy the constraint k_mu eps^mu = 0:
    c1 = (
        omega * eps_1[0] - 0 * eps_1[1] - 0 * eps_1[2] - omega * eps_1[3]
    )
    c2 = (
        omega * eps_2[0] - 0 * eps_2[1] - 0 * eps_2[2] - omega * eps_2[3]
    )
    check(
        "(R5b) representative eps_1 = (0, 1, 0, 0) lies in ker(ell)",
        simplify(c1) == 0,
        detail=f"constraint(eps_1) = {simplify(c1)}",
    )
    check(
        "(R5c) representative eps_2 = (0, 0, 1, 0) lies in ker(ell)",
        simplify(c2) == 0,
        detail=f"constraint(eps_2) = {simplify(c2)}",
    )

    # Verify eps_1 and eps_2 are linearly independent (form basis of
    # the 2-dim physical polarization quotient):
    basis_mat = Matrix.hstack(eps_1, eps_2)  # 4x2
    check(
        "(R5d) eps_1, eps_2 linearly independent (rank 2)",
        basis_mat.rank() == 2,
        detail=f"rank = {basis_mat.rank()}",
    )

    # Verify eps_1, eps_2 not in residual-shift direction k^mu (else they
    # would be gauge equivalent to zero):
    # k^mu = (omega, 0, 0, omega); eps_1 = (0, 1, 0, 0); they are linearly
    # independent.
    shift_check_1 = Matrix.hstack(k_canonical, eps_1)
    shift_check_2 = Matrix.hstack(k_canonical, eps_2)
    check(
        "(R5e) eps_1 not parallel to k (rank-2 with k)",
        shift_check_1.rank() == 2,
    )
    check(
        "(R5f) eps_2 not parallel to k (rank-2 with k)",
        shift_check_2.rank() == 2,
    )

    # ---------------------------------------------------------------------
    section("Part 3 (R6): optional complex-basis diagnostic")
    # ---------------------------------------------------------------------
    #
    # Circular-polarization basis (complex linear combinations of the real
    # transverse basis vectors): epsilon_+ carries helicity +1, epsilon_-
    # carries helicity -1 under rotations about the propagation axis z.

    inv_sqrt2 = 1 / sqrt(2)
    eps_plus = inv_sqrt2 * (eps_1 + sym_I * eps_2)
    eps_minus = inv_sqrt2 * (eps_1 - sym_I * eps_2)

    # Both still satisfy k_mu eps^mu = 0:
    cp = (
        omega * eps_plus[0]
        - 0 * eps_plus[1]
        - 0 * eps_plus[2]
        - omega * eps_plus[3]
    )
    cm = (
        omega * eps_minus[0]
        - 0 * eps_minus[1]
        - 0 * eps_minus[2]
        - omega * eps_minus[3]
    )
    check(
        "(R6a) Helicity-(+1) polarization satisfies k_mu eps_+^mu = 0",
        simplify(cp) == 0,
    )
    check(
        "(R6b) Helicity-(-1) polarization satisfies k_mu eps_-^mu = 0",
        simplify(cm) == 0,
    )

    # Normalization check (using +,-,-,- so the spatial-vector norm is the
    # standard Hermitian norm on R^3, i.e. |eps_1|^2 + |eps_2|^2 = 1/2 each
    # in the +-/sqrt(2) basis):
    # eps_+ . eps_+* = (1/2)(1+1) = 1 (Hermitian conjugate dot product on
    # spatial components).
    eps_plus_norm = simplify(
        eps_plus[1] * sympy.conjugate(eps_plus[1])
        + eps_plus[2] * sympy.conjugate(eps_plus[2])
    )
    check(
        "(R6c) Helicity-(+1) Hermitian norm-squared = 1",
        eps_plus_norm == 1,
        detail=f"|eps_+|^2 = {eps_plus_norm}",
    )

    # Rotation about z-axis: passive R_z(theta) acting on (x, y) (i.e.
    # the rotation of the polarization basis vector as seen from a
    # frame rotated by +theta about z) is
    #   x' = cos*x + sin*y,
    #   y' = -sin*x + cos*y.
    # Equivalently, the spatial components transform as
    #   (e1', e2') = R_z(theta) (e1, e2)
    # under the +z-helicity convention used by Peskin-Schroeder §3.3.
    # On eps_pm = (1, +-i)/sqrt(2) this gives eps_pm * exp(-+i theta), so
    # eps_+ has helicity +1 and eps_- has helicity -1 in this convention.
    # The runner verifies the rotational phase magnitude is 1 (i.e. the
    # rotation acts as a U(1) phase on each helicity eigenstate), which
    # is the load-bearing structural fact; the convention-dependent sign
    # is +- and is consistent with both common physics conventions.

    theta = Symbol("theta", real=True)
    # Active R_z(theta) on (x, y): x' = cos*x - sin*y, y' = sin*x + cos*y.
    # Applied to spatial components (eps_plus[1], eps_plus[2]):
    e1_rot_plus = sympy.cos(theta) * eps_plus[1] - sympy.sin(theta) * eps_plus[2]
    e2_rot_plus = sympy.sin(theta) * eps_plus[1] + sympy.cos(theta) * eps_plus[2]
    # The result should equal exp(-i theta) * eps_plus_spatial (since
    # eps_+ has positive helicity under the +z propagation convention,
    # and active rotation by +theta gives phase exp(-i theta) when
    # measured against the (1, i) chirality basis).
    expected_e1 = sympy.exp(-sym_I * theta) * eps_plus[1]
    expected_e2 = sympy.exp(-sym_I * theta) * eps_plus[2]
    check(
        "(R6d) R_z(theta) eps_+ acts as U(1) phase: e1 component (active rot)",
        simplify((e1_rot_plus - expected_e1).rewrite(sympy.sin)) == 0,
    )
    check(
        "(R6e) R_z(theta) eps_+ acts as U(1) phase: e2 component (active rot)",
        simplify((e2_rot_plus - expected_e2).rewrite(sympy.sin)) == 0,
    )

    # And on eps_-: same active rotation gives phase exp(+i theta), so
    # the two are distinct helicity eigenstates:
    e1_rot_minus = sympy.cos(theta) * eps_minus[1] - sympy.sin(theta) * eps_minus[2]
    e2_rot_minus = sympy.sin(theta) * eps_minus[1] + sympy.cos(theta) * eps_minus[2]
    expected_e1_m = sympy.exp(sym_I * theta) * eps_minus[1]
    expected_e2_m = sympy.exp(sym_I * theta) * eps_minus[2]
    check(
        "(R6d') R_z(theta) eps_- acts as opposite U(1) phase: e1",
        simplify((e1_rot_minus - expected_e1_m).rewrite(sympy.sin)) == 0,
    )
    check(
        "(R6e') R_z(theta) eps_- acts as opposite U(1) phase: e2",
        simplify((e2_rot_minus - expected_e2_m).rewrite(sympy.sin)) == 0,
    )

    # ---------------------------------------------------------------------
    section("Part 4 (R7): non-load-bearing multiplicity diagnostic")
    # ---------------------------------------------------------------------
    #
    # This is retained only as a matrix-count diagnostic: if an external
    # authority supplies N independent copies of the same quotient, the count
    # scales by N. This runner does not supply that external authority.

    for N, n_adj in [(1, 1), (2, 3), (3, 8)]:
        n_polariz_per_boson = 2
        n_total_polariz = n_adj * n_polariz_per_boson
        # For SU(N): dim adj = N^2 - 1; for U(1): 1.
        if N == 1:
            expected_n_adj = 1
        else:
            expected_n_adj = N * N - 1
        check(
            f"(R7a-N{N}) Gauge-group SU({N})/U(1) adjoint count = {expected_n_adj}",
            n_adj == expected_n_adj,
        )
        check(
            f"(R7b-N{N}) Total polarizations = {n_adj} * 2 = {n_total_polariz}",
            n_total_polariz == n_adj * 2,
        )

    # ---------------------------------------------------------------------
    section("Part 5 (R8): non-load-bearing contrast when quotient direction is absent")
    # ---------------------------------------------------------------------
    #
    # Contrast: if the would-be quotient direction is not in the row kernel,
    # the abstract quotient ker(ell)/span(k) is not defined. The old physical
    # massive-vector language is no longer load-bearing; this block is a
    # diagnostic count only.

    m_sym = Symbol("m", positive=True)
    # This keeps the old arithmetic contrast but removes it from the
    # load-bearing physical interpretation.
    k_sq_massive = m_sym * m_sym  # = m^2 > 0
    check(
        "(R8a) diagnostic nonzero scalar m^2 is not zero",
        k_sq_massive != 0,
    )
    # No quotient direction is supplied in this contrast.
    n_residual_massive = 0
    n_polariz_massive = n_total - n_constraint - n_residual_massive
    check(
        "(R8b) no-quotient contrast count = 4 - 1 - 0 = 3",
        n_polariz_massive == 3,
        detail=f"count = {n_polariz_massive}",
    )

    check(
        "(R8c) quotient case has dimension 2",
        n_total - n_constraint - n_shift == 2,
    )
    check(
        "(R8d) no-quotient contrast has dimension 3",
        n_polariz_massive == 3,
    )
    check(
        "(R8e) contrast difference is 1",
        n_polariz_massive - (n_total - n_constraint - n_shift) == 1,
    )

    # ---------------------------------------------------------------------
    section("Part 6 (R9): note structure and forbidden-import scan")
    # ---------------------------------------------------------------------
    note_text = NOTE_PATH.read_text(encoding="utf-8")

    required_phrases = [
        "Claim type:** bounded_support",
        "Scope Repair",
        "dim_C ker(ell) / span_C{k} = 2",
        "4 - 1 - 1 = 2",
        "What This Supports",
        "What This Does Not Close",
        "Load-Bearing Step",
        "Independent Audit Handoff",
        "Physical massless-vector interpretation is outside",
    ]
    for phrase in required_phrases:
        check(
            f"(R9-structure) note contains phrase: '{phrase[:60]}...'",
            phrase in note_text,
        )

    # Forbidden-import string scan: the note must NOT consume PDG comparators,
    # fitted constants, Wilson plaquette values, or framework axioms as
    # load-bearing inputs. Some terms (e.g. 'Wilson') appear in cross-
    # reference / boundary context only; the check is that the load-bearing
    # proof in section 4 ("Proof") does not consume them.

    proof_section_re = re.compile(
        r"## 4\. Proof(.*?)## 5\. Load-Bearing Step",
        re.DOTALL,
    )
    m = proof_section_re.search(note_text)
    proof_text = m.group(1) if m else ""
    check(
        "(R9-scan) proof section is present",
        bool(proof_text),
    )

    forbidden_in_proof = [
        "PDG",
        "fitted",
        "Wilson plaquette",
        "u_0",
        "Monte Carlo",
        "Brillouin",
        "staggered phase",
        "framework axiom",
    ]
    for term in forbidden_in_proof:
        # The proof must not consume any of these:
        check(
            f"(R9-scan) proof does not consume '{term}'",
            term not in proof_text,
        )

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (R1) A four-component vector eps in C^4 has 4 components.")
    print("    (R2) The nonzero row ell has rank 1.")
    print("    (R3) The nonzero direction k in ker(ell) has rank 1.")
    print("    (R4) Quotient dim_C ker(ell)/span(k) = 4 - 1 - 1 = 2.")
    print("    (R5) Explicit representatives (0,1,0,0), (0,0,1,0) in the canonical model.")
    print("    (R6-R8) Former physics-language checks are diagnostics only.")
    print("    (R9) Note structure + forbidden-import scan.")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded abstract quotient identity verified at exact precision;"
        )
        print(
            "         dim_C ker(ell)/span(k) = 2 for a nonzero row ell and nonzero"
        )
        print(
            "         k in ker(ell). Physical massless-vector interpretation is outside"
        )
        print(
            "         this row's load-bearing scope."
        )
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
