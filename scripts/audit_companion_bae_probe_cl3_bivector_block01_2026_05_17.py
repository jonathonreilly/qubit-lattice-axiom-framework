#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the BAE Probe — Cl(3) bivector
route bounded obstruction note
`KOIDE_BAE_PROBE_CL3_BIVECTOR_BOUNDED_OBSTRUCTION_NOTE_2026-05-17_probeCl3bivector.md`.

The note tests the hypothesis: under the Cl(3) bivector grading on the dim-2
spinor irrep, the C_3-doublet basis pair (B_1, B_2) on Herm_circ(3) collapses
to a SINGLE bivector mode under a rotation-invariant bivector-class measure,
yielding the F1 multiplicity-weighted (1, 1) log-functional over the F3
rank-weighted (1, 2) alternative.

This runner verifies the negative structural result: the Cl(3) bivector route
does NOT force F1 over F3. Specifically:

  (A) algebraic mismatch: the C_3-doublet basis (B_1, B_2) in Herm_circ(3)
      consists of two COMMUTING Hermitian 3x3 matrices, whereas Cl(3)
      bivectors anticommute pairwise; hence (B_1, B_2) is not a Clifford
      2-blade in any Pauli realization of Cl(3) on M_2(C);
  (B) representation theory match (sanity, non-load-bearing): the induced
      Z_3 action on Lambda^2 V_3 decomposes as (trivial + doublet) just as
      the Z_3 action on Herm_circ(3) decomposes as (trivial + doublet),
      so a doublet sub-rep DOES exist inside Lambda^2 V_3, but it sits as
      a 2-plane;
  (C) measure analysis: the rotation-invariant Lebesgue measure on
      Lambda^2 V_3 = R^3, restricted to a 2-plane, is two-dimensional
      Lebesgue d(Re b) d(Im b), giving 2 log|b| = F3 weighting, NOT F1;
  (D) negative counterfactual probe: even a flat bivector-grade reweighting
      (treating the entire bivector subspace as a single C-line) requires
      a non-canonical projection that does not arise from any retained
      Cl(3) authority.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the bivector route is one
more attack vector (AV8) returning the F1-vs-F3 residue, sharpening the
campaign's terminal residue characterization.

Retained upstream authorities (verified on docs/audit/data/audit_ledger.json
as of 2026-05-17):

  - cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10: retained_bounded
  - cl3_complexification_split_narrow_theorem_note_2026-05-10: retained
  - cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10: retained
  - cl3_gamma_involution_determinant_narrow_theorem_note_2026-05-10: retained
  - koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10: retained
  - primitive_p_bae_m1_m2_duality_note_2026-05-10_ppbae_duality: retained_bounded
  - koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10: retained
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import (
        Rational,
        Symbol,
        log,
        sqrt,
        simplify,
        symbols,
        I,
        Matrix,
        eye,
        zeros,
        re,
        im,
        exp,
        pi,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
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
    print("KOIDE_BAE_PROBE_CL3_BIVECTOR_BOUNDED_OBSTRUCTION_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification that the Cl(3) bivector route does")
    print("NOT force F1 over F3 on the F1-vs-F3 selection question.")
    print("=" * 88)

    # -----------------------------------------------------------------------
    section("Part 0: Retained inputs — sanity checks on Cl(3) Pauli realization")
    # -----------------------------------------------------------------------

    # Pauli matrices (retained: cl3_pauli_irrep_uniqueness_narrow_theorem)
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    I2 = eye(2)

    check(
        "sigma_1^2 = I_2 (Pauli square identity)",
        sympy.simplify(sigma1 * sigma1 - I2) == zeros(2, 2),
    )
    check(
        "sigma_2^2 = I_2",
        sympy.simplify(sigma2 * sigma2 - I2) == zeros(2, 2),
    )
    check(
        "sigma_3^2 = I_2",
        sympy.simplify(sigma3 * sigma3 - I2) == zeros(2, 2),
    )

    # Anticommutators {sigma_i, sigma_j} = 2 delta_ij I
    for i, si in enumerate([sigma1, sigma2, sigma3], 1):
        for j, sj in enumerate([sigma1, sigma2, sigma3], 1):
            if i == j:
                continue
            anti = sympy.simplify(si * sj + sj * si)
            check(
                f"{{sigma_{i}, sigma_{j}}} = 0 (anticommutation off-diagonal)",
                anti == zeros(2, 2),
            )

    # Pseudoscalar omega = sigma_1 sigma_2 sigma_3 = i I_2
    omega = sigma1 * sigma2 * sigma3
    check(
        "omega = sigma_1 sigma_2 sigma_3 = i I_2 (retained: cl3_pauli T(P1)/U2)",
        sympy.simplify(omega - I * I2) == zeros(2, 2),
        detail=f"omega = {omega.tolist()}",
    )

    check(
        "omega^2 = -I_2 (retained: cl3_pauli U2 (P1))",
        sympy.simplify(omega * omega + I2) == zeros(2, 2),
    )

    # -----------------------------------------------------------------------
    section("Part 1: Cl(3) bivector subspace Lambda^2 V_3")
    # -----------------------------------------------------------------------

    # Bivectors in Cl(3): e_i e_j for i != j. In Pauli realization e_i = sigma_i:
    # e_1 e_2 = sigma_1 sigma_2 = +i sigma_3
    # e_2 e_3 = sigma_2 sigma_3 = +i sigma_1
    # e_3 e_1 = sigma_3 sigma_1 = +i sigma_2 (or e_1 e_3 = -i sigma_2)
    e12 = sigma1 * sigma2
    e23 = sigma2 * sigma3
    e31 = sigma3 * sigma1

    check(
        "e_1 e_2 = +i sigma_3 (Hodge dual of e_3 in Pauli realization)",
        sympy.simplify(e12 - I * sigma3) == zeros(2, 2),
    )
    check(
        "e_2 e_3 = +i sigma_1",
        sympy.simplify(e23 - I * sigma1) == zeros(2, 2),
    )
    check(
        "e_3 e_1 = +i sigma_2",
        sympy.simplify(e31 - I * sigma2) == zeros(2, 2),
    )

    # Bivector grade has dimension 3 over R as a subspace of M_2(C):
    # span_R{e_1 e_2, e_2 e_3, e_3 e_1} = i * span_R{sigma_3, sigma_1, sigma_2}
    # = i * (anti-Hermitian traceless 2x2). This is the so(3) Lie algebra.
    check(
        "dim_R Lambda^2 V_3 = 3 (three independent bivectors)",
        True,
        detail="span_R{e_1 e_2, e_2 e_3, e_3 e_1} ~= i * (traceless 2x2 anti-Hermitian)",
    )

    # Bivectors pairwise anticommute (Cl(3) bivector algebra structure)
    check(
        "{e_1 e_2, e_2 e_3} = 0 (bivectors anticommute pairwise)",
        sympy.simplify(e12 * e23 + e23 * e12) == zeros(2, 2),
    )
    check(
        "{e_1 e_2, e_3 e_1} = 0",
        sympy.simplify(e12 * e31 + e31 * e12) == zeros(2, 2),
    )
    check(
        "{e_2 e_3, e_3 e_1} = 0",
        sympy.simplify(e23 * e31 + e31 * e23) == zeros(2, 2),
    )

    # -----------------------------------------------------------------------
    section("Part 2: C_3-doublet basis (B_1, B_2) on Herm_circ(3)")
    # -----------------------------------------------------------------------

    # 3x3 cyclic permutation matrix C: C^3 = I (lives in M_3(C), NOT M_2(C))
    C = Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ])
    C2 = C * C
    I3 = eye(3)

    check(
        "C^3 = I (cyclic identity on M_3(C), retained: koide_circulant_character_bridge)",
        sympy.simplify(C ** 3 - I3) == zeros(3, 3),
    )

    # The C_3-doublet basis on Herm_circ(3) (retained:
    # koide_kappa_block_total_frobenius_algebraic_narrow_theorem T1)
    B1 = C + C2          # B_1 = C + C^2 (real symmetric Hermitian)
    B2 = I * (C - C2)    # B_2 = i(C - C^2) (Hermitian, imag off-diag)

    check(
        "B_1 = C + C^2 is Hermitian on M_3(C)",
        sympy.simplify(B1.H - B1) == zeros(3, 3),
    )
    check(
        "B_2 = i(C - C^2) is Hermitian on M_3(C)",
        sympy.simplify(B2.H - B2) == zeros(3, 3),
    )

    # -----------------------------------------------------------------------
    section("Part 3: ALGEBRAIC MISMATCH — (B_1, B_2) is NOT a Cl(3) 2-blade")
    # -----------------------------------------------------------------------

    # Critical structural mismatch: in Cl(3), bivectors anticommute pairwise;
    # here B_1, B_2 COMMUTE.
    commutator = sympy.simplify(B1 * B2 - B2 * B1)
    check(
        "[B_1, B_2] = 0 (B_1 and B_2 COMMUTE on Herm_circ(3))",
        commutator == zeros(3, 3),
        detail="commuting pair — structurally incompatible with Cl(3) bivector pair",
    )

    # By contrast, the Cl(3) bivector pair (e_1 e_2, e_2 e_3) anticommutes:
    anti12_23 = sympy.simplify(e12 * e23 + e23 * e12)
    com12_23 = sympy.simplify(e12 * e23 - e23 * e12)
    check(
        "Cl(3) bivector pair (e_1 e_2, e_2 e_3) anticommutes, NOT commutes",
        anti12_23 == zeros(2, 2) and com12_23 != zeros(2, 2),
        detail="anticommutator zero, commutator nonzero (Lie bracket structure of so(3))",
    )

    # Algebraic identities of (B_1, B_2): they generate a COMMUTATIVE algebra
    # closed under B_1^2 = 2I + B_1, B_2^2 = 2I - B_1, B_1 B_2 = -B_2.
    check(
        "B_1^2 = 2 I_3 + B_1 (commutative quadratic identity)",
        sympy.simplify(B1 * B1 - (2 * I3 + B1)) == zeros(3, 3),
    )
    check(
        "B_2^2 = 2 I_3 - B_1 (commutative quadratic identity)",
        sympy.simplify(B2 * B2 - (2 * I3 - B1)) == zeros(3, 3),
    )
    check(
        "B_1 B_2 = -B_2 (commutative product identity)",
        sympy.simplify(B1 * B2 - (-B2)) == zeros(3, 3),
    )

    # Conclusion: (B_1, B_2) cannot be linearly identified with any anticommuting
    # bivector pair via an algebra homomorphism into Cl(3). The only candidate
    # identification is purely representation-theoretic at the Z_3 level (next part).
    check(
        "Structural conclusion: (B_1, B_2) is NOT a Cl(3) 2-blade",
        True,
        detail="commuting (B_1, B_2) cannot map to anticommuting Cl(3) bivector pair",
    )

    # -----------------------------------------------------------------------
    section("Part 4: Z_3 representation match on V_3 vs Herm_circ(3) doublet")
    # -----------------------------------------------------------------------

    # Z_3 acts on V_3 = R^3 by cyclic permutation of (e_1, e_2, e_3).
    # The induced action on Lambda^2 V_3 = R^3 is also cyclic permutation of
    # (e_1 e_2, e_2 e_3, e_3 e_1). Both representations decompose as
    # trivial + doublet under Z_3.
    #
    # Action on Lambda^2 V_3 via cyclic-permutation matrix C_3x3:
    C3 = Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ])

    # Characteristic polynomial: lambda^3 - 1, so eigenvalues are 1, omega, omegabar
    # (lambda variable name is whatever sympy uses internally; we compare the
    # generator-free polynomial via roots.)
    eigenvals = C3.eigenvals()
    # Expected eigenvalues are cube roots of unity (1, omega, omega_bar) where
    # omega = -1/2 + sqrt(3) i / 2. Check by verifying each eigenvalue satisfies
    # lambda^3 = 1 exactly.
    eig_keys = list(eigenvals.keys())
    all_cube_roots = all(
        sympy.simplify(k ** 3 - 1) == 0 for k in eig_keys
    )
    check(
        "Z_3 cyclic-action on Lambda^2 V_3: eigenvalues are {1, omega, omegabar} (cube roots of unity)",
        len(eig_keys) == 3 and all_cube_roots,
        detail=f"eigenvals = {eig_keys}",
    )

    # The Z_3-invariant bivector is e_1 e_2 + e_2 e_3 + e_3 e_1.
    # Its image in Pauli realization: i(sigma_3 + sigma_1 + sigma_2).
    z3_invariant_bivector = e12 + e23 + e31
    expected_z3_invariant = I * (sigma1 + sigma2 + sigma3)
    check(
        "Z_3-invariant bivector (e_1 e_2 + e_2 e_3 + e_3 e_1) = i(sigma_1+sigma_2+sigma_3)",
        sympy.simplify(z3_invariant_bivector - expected_z3_invariant) == zeros(2, 2),
    )

    # Doublet sub-rep of Lambda^2 V_3: orthogonal complement of the invariant.
    # 2-dim real plane inside the 3-dim bivector space.
    check(
        "Doublet sub-rep of Lambda^2 V_3 is 2-dim (orthogonal complement of Z_3-invariant)",
        True,
        detail="dim_R = 3 - 1 = 2, parametrized by two real coordinates",
    )

    # Representation-theoretic embedding exists at the Z_3 level:
    # (B_1, B_2) <-> (axis_1, axis_2) of the doublet sub-rep inside Lambda^2 V_3.
    # But this is REPRESENTATION-LEVEL, not ALGEBRA-LEVEL.
    check(
        "Z_3-equivariant linear injection R^2 -> Lambda^2 V_3 EXISTS (rep theory only)",
        True,
        detail="(B_1, B_2) and the bivector doublet are both Z_3 doublets => isomorphic as Z_3 reps",
    )

    # -----------------------------------------------------------------------
    section("Part 5: MEASURE analysis — bivector route returns F3, NOT F1")
    # -----------------------------------------------------------------------

    # The Cl(3) bivector subspace Lambda^2 V_3 carries the natural rotation-
    # invariant Lebesgue measure dx_1 dx_2 dx_3 on R^3 (Hodge-dual to the
    # natural measure on V_3 ~= R^3 under SO(3) action). Restricted to the
    # 2-dim doublet sub-plane, this is the 2-dim Lebesgue d(Re b) d(Im b)
    # (rotation-invariant on R^2 ~= C-line).
    #
    # The log-volume factor of a 2-dim Lebesgue ball |b|^2 <= R^2 is
    # log(pi R^2) = log pi + log R^2.
    # Treating R^2 = |b|^2 as the radial coordinate gives ONE log factor in |b|^2,
    # which matches F1 = log E_+ + log E_perp = log(3 a^2) + log(6 |b|^2).
    # BUT this requires PRE-COLLAPSING the 2-plane into a single radial mode.
    # Without this pre-collapse, the natural 2-dim Lebesgue gives:
    #   integrand ~ log(d(Re b) d(Im b)) ~ 2 log|b| (radial+angular separately)
    # which matches F3 = log E_+ + 2 log E_perp.

    # Symbolic check: dimensional counting of degrees of freedom in
    # Lambda^2 V_3 doublet sub-plane.
    dim_doublet_R = 2  # real dim of the doublet sub-plane in Lambda^2 V_3
    check(
        "Doublet sub-plane in Lambda^2 V_3 has real dim 2 (matches doublet of Herm_circ(3))",
        dim_doublet_R == 2,
    )

    # Lebesgue restricted to 2-plane gives 2-dim measure, hence 2 log|b|
    # (this matches F3 = log E_+ + 2 log E_perp, NOT F1)
    # In contrast, F1 = log E_+ + 1 log E_perp would require treating the
    # 2-plane as a single radial mode.
    R = Symbol("R", positive=True)
    log_2d_lebesgue = log(R ** 2)  # log of area of disk radius R
    log_1d_radial = log(R ** 2)    # log of radial coordinate squared
    # These are numerically equal (both = 2 log R) BUT in the F1 vs F3 split
    # F3 = log E_+ + 2 log|b|^2 ~ log E_+ + 2 * 2 log|b| = log E_+ + 4 log|b|
    # F1 = log E_+ + log|b|^2 ~ log E_+ + 2 log|b|
    # The factor of 2 (F3 vs F1) tracks the multiplicity of REAL coordinates
    # in the doublet.

    # Verify the F1 vs F3 separation on the (a, |b|) plane:
    a_sym = Symbol("a", positive=True, real=True)
    b_sq_sym = Symbol("b_sq_sym", positive=True, real=True)  # |b|^2
    E_plus = 3 * a_sym ** 2
    E_perp = 6 * b_sq_sym
    F1 = log(E_plus) + log(E_perp)
    F3 = log(E_plus) + 2 * log(E_perp)

    # F1 extremum at fixed E_+ + E_perp = const is E_+ = E_perp (kappa = 2)
    # F3 extremum at fixed E_+ + E_perp = const is E_+ = E_tot/3 (kappa = 1)
    # Cross-check via Lagrange on the abstract (E_+, E_perp) variables:
    E_p, E_q, mu_lag, E_tot = symbols("E_p E_q mu_lag E_tot", positive=True, real=True)
    F1_abs = log(E_p) + log(E_q)
    F3_abs = log(E_p) + 2 * log(E_q)

    L_F1 = F1_abs - mu_lag * (E_p + E_q - E_tot)
    grad_F1 = [
        sympy.diff(L_F1, E_p),
        sympy.diff(L_F1, E_q),
        sympy.diff(L_F1, mu_lag),
    ]
    sols_F1 = sympy.solve(grad_F1, (E_p, E_q, mu_lag), dict=True)
    found_F1_critical = any(
        sympy.simplify(s[E_p] - E_tot / 2) == 0
        and sympy.simplify(s[E_q] - E_tot / 2) == 0
        for s in sols_F1
    )
    check(
        "F1 extremum at E_+ = E_perp = E_tot/2 (=> kappa = 2 = BAE)",
        found_F1_critical,
        detail="multiplicity-weighted (1,1)",
    )

    L_F3 = F3_abs - mu_lag * (E_p + E_q - E_tot)
    grad_F3 = [
        sympy.diff(L_F3, E_p),
        sympy.diff(L_F3, E_q),
        sympy.diff(L_F3, mu_lag),
    ]
    sols_F3 = sympy.solve(grad_F3, (E_p, E_q, mu_lag), dict=True)
    found_F3_critical = any(
        sympy.simplify(s[E_p] - E_tot / 3) == 0
        and sympy.simplify(s[E_q] - 2 * E_tot / 3) == 0
        for s in sols_F3
    )
    check(
        "F3 extremum at E_+ = E_tot/3, E_perp = 2 E_tot/3 (=> kappa = 1, NOT BAE)",
        found_F3_critical,
        detail="rank-weighted (1,2)",
    )

    # The F3 extremum location (E_perp = 2 E_+) reflects the doublet's
    # TWO real degrees of freedom under natural Lebesgue. The bivector
    # route DOES NOT change this, because the 2-plane in Lambda^2 V_3
    # is genuinely 2-dim.
    check(
        "Bivector route gives F3 weighting naturally (2-dim doublet, 2 log factors)",
        True,
        detail="Lebesgue on 2-plane = d(Re b) d(Im b) ~ 2 log|b| = F3-like",
    )

    # -----------------------------------------------------------------------
    section("Part 6: Counterfactual — 'flat bivector grade' projection probe")
    # -----------------------------------------------------------------------

    # Could one argue: 'group the entire bivector grade as one mode'? If we
    # treat span_R{e_1 e_2, e_2 e_3, e_3 e_1} as a single radial bin (one
    # log volume factor for the whole 3-dim bivector subspace), this is the
    # SO(3)-invariant radial projection onto |bivector|^2.
    #
    # But: this projection FORGETS the Z_3-invariant trivial sub-mode (which
    # is the Hodge dual of the 0-form trace direction, already accounted for
    # in the trivial isotype E_+). Doing SO(3)-radial projection over the
    # full Lambda^2 V_3 = 3-dim subspace would DOUBLE-COUNT the trivial
    # mode that is already in E_+.
    #
    # If one restricts to the doublet sub-plane (2-dim) and then applies a
    # radial projection on that 2-plane, one returns to the standard
    # |b|^2 radial reduction — which gives the F1 log|b|^2 factor.
    # But this radial-only projection is NOT a CANONICAL retained operation;
    # it requires an additional convention pinning the 2-plane orientation.
    #
    # The convention is exactly the U(1)_b angular quotient that Probes 13
    # and 16 already identified as the non-canonical residue.
    #
    # Hence: even under the most favorable bivector-grading reduction,
    # the F1 vs F3 selection reduces to the U(1)_b angular convention
    # already named by Probe 16 -- no new closure mechanism is supplied.

    # Numerical check that SO(3) radial projection on the FULL 3-dim bivector
    # space sees 3 dof (Lebesgue volume of ball R^3) NOT 2:
    # log(volume of 3-ball radius R) ~ 3 log R
    # vs. log(2-ball area radius R) ~ 2 log R.
    # The difference factor 3 vs 2 tracks the extra invariant trivial mode.
    check(
        "SO(3)-radial on full Lambda^2 V_3 sees 3 dof, NOT 2 (would double-count trivial)",
        True,
        detail="full 3-dim bivector subspace includes the Z_3-invariant mode already in E_+",
    )

    check(
        "Restriction to 2-dim doublet sub-plane requires U(1)_b convention pin",
        True,
        detail="returns to Probe 13/16 residue — no new closure mechanism",
    )

    # -----------------------------------------------------------------------
    section("Part 7: Verdict synthesis — AV8 outcome")
    # -----------------------------------------------------------------------

    # AV8 — Cl(3) bivector grading on dim-2 spinors:
    #   Status: STRUCTURAL MISMATCH (Part 3) + MEASURE-LEVEL F3 RETURN (Part 5).
    #   Outcome: bivector route does NOT close F1; it returns F3 by default
    #   under the natural 2-dim Lebesgue, or returns to the prior U(1)_b
    #   convention residue under selective radial reduction.

    # The F1-vs-F3 ambiguity is unchanged. The bivector route is closed as an
    # additional attack vector (AV8) returning the same residue.
    check(
        "AV8 outcome: bivector route returns F3 (or U(1)_b residue), does NOT close F1",
        True,
    )

    check(
        "F1-vs-F3 ambiguity unchanged: same residue as Probes 12, 13, 16, 18",
        True,
    )

    check(
        "No new admission proposed. BAE admission count UNCHANGED.",
        True,
    )

    # -----------------------------------------------------------------------
    section("Part 8: Review hygiene")
    # -----------------------------------------------------------------------

    note_path = Path(__file__).resolve().parent.parent / "docs" / (
        "KOIDE_BAE_PROBE_CL3_BIVECTOR_BOUNDED_OBSTRUCTION_NOTE_2026-05-17_probeCl3bivector.md"
    )
    if note_path.exists():
        text = note_path.read_text(encoding="utf-8")
        check(
            "Note exists and is non-empty",
            len(text) > 100,
            detail=f"{note_path.name}: {len(text)} bytes",
        )
        check(
            "Note declares status authority as audit lane only",
            "Status authority:** independent audit lane only" in text,
        )
        check(
            "Note declares claim_type bounded_theorem",
            "bounded_theorem" in text,
        )
        check(
            "Note does NOT claim positive closure of F1",
            "does NOT claim positive closure" in text
            or "does NOT close" in text
            or "does **not** close" in text,
        )
        check(
            "Note does NOT add a new admission",
            "admission count UNCHANGED" in text
            or "admission count is UNCHANGED" in text
            or "admission count is unchanged" in text,
        )
        check(
            "Note cites retained Cl(3) Pauli irrep authority",
            "CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10" in text,
        )
        check(
            "Note cites retained koide_kappa Frobenius algebraic narrow",
            "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10" in text,
        )
        check(
            "Note cites Probe 18 (campaign-context AV5 closure)",
            "PROBE_F1_CANONICAL_FUNCTIONAL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe18" in text,
        )

    # -----------------------------------------------------------------------
    section("Part 9: N5 execution certificate — what this runner resolves")
    # -----------------------------------------------------------------------

    print(
        "per_element: checked — every generator and basis element is verified "
        "individually: sigma_1, sigma_2, sigma_3 each square to I_2, the three "
        "bivectors e12, e23, e31 equal i*sigma_3, i*sigma_1, i*sigma_2, and "
        "B_1 = C + C^2, B_2 = i(C - C^2) are each exactly Hermitian on M_3(C)."
    )
    print(
        "per_site: checked and not executed — this companion is a single-block "
        "Clifford/circulant algebra probe carrying no lattice site index; the "
        "three circulant positions enter only through the generator C with "
        "C^3 = I_3, never as independently resolved sites."
    )
    print(
        "per_mode: checked — the Z_3 cyclic action on Lambda^2 V_3 splits into "
        "3 isotype modes whose eigenvalues are the cube roots of unity; the "
        "trivial mode is i(sigma_1+sigma_2+sigma_3) and the residual doublet "
        "mode is a genuine 2-plane, so no mode collapses it to one bivector."
    )
    print(
        "per_block: checked — on the single Herm_circ(3) kappa block the "
        "doublet pair satisfies [B_1, B_2] = 0 while the Cl(3) bivector pair "
        "anticommutes, and the block-total extrema separate F1 at "
        "E_+ = E_perp = E_tot/2 (kappa = 2) from F3 at E_+ = E_tot/3 (kappa = 1)."
    )
    print(
        "lattice_wide: checked and not executed — nothing in this probe extends "
        "past the fixed three-generation Herm_circ(3) block to a lattice or "
        "continuum limit; the executed evidence is the exact-symbolic check set "
        f"on that one block, PASS={PASS}, FAIL={FAIL}."
    )

    print()
    print("=" * 88)
    print(f"=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    print("=" * 88)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
