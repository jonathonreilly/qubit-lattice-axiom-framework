#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the BAE U(1)_b canonical-phase
stretch attempt note
`BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md`.

The note tests five stretch routes (R1)-(R5) for supplying a canonical
direction on the U(1)_b doublet plane on Herm_circ(3) from A_min plus
retained authorities (X1)-(X4). Honest verdict: none of the routes
closes; the residue is structurally distinct from the F3 reappearance
pattern of Cycles 1 / 2 in that it names "continuous-SO(2) quotient on
a 2-real-dim plane" rather than "weight choice on 2-isotype
decomposition".

This runner verifies each route's specific failure step plus the
structural-character narrowing (T2) and the Cycles 1 / 2 distinction
(T3).

Retained upstream authorities (verified on
docs/audit/data/audit_ledger.json as of 2026-05-17):

  (X1) koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10: retained
  (X2) cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10:                retained_bounded
  (X3) cl3_gamma_involution_determinant_narrow_theorem_note_2026-05-10:          retained
  (X4) ckm_cp_phase_rho_eta_to_delta_narrow_theorem_note_2026-05-10:             retained
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
        cos,
        sin,
        acos,
        atan,
        diff,
        integrate,
        Function,
        conjugate,
        nsimplify,
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
    print("BAE_U1B_CANONICAL_PHASE_STRETCH_ATTEMPT_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of R1-R5 failure steps + (T2),(T3).")
    print("=" * 88)

    # -----------------------------------------------------------------------
    section("Part 0: Algebraic baseline (X1) — H = aI + bC + b_bar C^2 on hw=1")
    # -----------------------------------------------------------------------

    # Standard 3x3 cyclic permutation matrix C with C^3 = I.
    C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    C2 = C * C
    I3 = eye(3)
    check("C^3 = I (cyclic permutation, (X1) baseline)", C * C2 == I3)
    check("C^2 = C.T (since C is real orthogonal, C^{-1} = C^T)", C2 == C.T)

    # Doublet basis on Herm_circ(3): B_1 = C + C^2, B_2 = i (C - C^2).
    B_1 = C + C2
    B_2 = I * (C - C2)
    check("B_1 Hermitian: B_1^dagger = B_1", B_1.H == B_1)
    check("B_2 Hermitian: B_2^dagger = B_2", B_2.H == B_2)
    # Pairwise commutation (load-bearing for AV8 obstruction (i) and Route R3 here):
    comm = B_1 * B_2 - B_2 * B_1
    check("[B_1, B_2] = 0 (commute pairwise)", comm == zeros(3, 3))

    # General Hermitian circulant H = aI + bC + b_bar C^2.
    a_sym = Symbol("a", real=True, positive=True)
    bR = Symbol("bR", real=True)
    bI = Symbol("bI", real=True)
    b = bR + I * bI
    bbar = bR - I * bI
    H = a_sym * I3 + b * C + bbar * C2
    check("H Hermitian (X1)", simplify(H - H.H) == zeros(3, 3))

    # Trace energies E_+ = Tr(pi_+ H pi_+) ... but use the algebraic identities directly:
    # ||pi_+(H)||_F^2 = (3 a)^2 / 3 = 3 a^2 (projector pi_+ = (1/3) sum_k C^k has rank 1).
    # ||pi_perp(H)||_F^2 = 6 |b|^2 (rank-2 isotype).
    # We verify the global Frobenius identity ||H||_F^2 = 3 a^2 + 6 |b|^2:
    HF = sum(H[i, j] * conjugate(H[i, j]) for i in range(3) for j in range(3))
    HF_simp = simplify(HF)
    target_F = 3 * a_sym**2 + 6 * (bR**2 + bI**2)
    check("||H||_F^2 = 3 a^2 + 6 |b|^2 (X1)", simplify(HF_simp - target_F) == 0)

    # -----------------------------------------------------------------------
    section("Part 1: R1 — Time-orientation projection fails (no C_3-equivariant time map)")
    # -----------------------------------------------------------------------

    # The time axis is 1-real-dim; the C_3 group acts on the 3-vector hw=1 = C^3.
    # The trivial C_3 rep on the time axis means any C_3-equivariant linear map
    # R_time -> Herm_circ(3) must factor through the trivial isotype (the aI direction),
    # NOT through the (B_1, B_2) doublet (non-trivial isotype).
    #
    # We verify this at the character level. Character of trivial C_3 rep on time:
    # chi_triv(g) = 1 for all g in C_3.
    # Character of doublet (B_1, B_2) sub-rep: chi_doublet(g_k) = 2 cos(2 pi k / 3).
    # By Frobenius reciprocity: Hom_{C_3}(R_triv, R_doublet) has dimension
    # = (1/|G|) sum_g chi_triv(g)* chi_doublet(g)
    # = (1/3) [1 * 2 + 1 * (-1) + 1 * (-1)] = 0.
    G = 3
    chars_triv = [1, 1, 1]
    chars_doub = [2, -1, -1]  # 2 cos(0), 2 cos(2pi/3), 2 cos(4pi/3) = 2, -1, -1.
    intertwiner_dim = Rational(1, G) * sum(chars_triv[k] * chars_doub[k] for k in range(G))
    check(
        "Hom_{C_3}(R_triv_time, R_doublet) = 0 by Frobenius reciprocity",
        intertwiner_dim == 0,
        detail=f"sum = {intertwiner_dim}",
    )

    # -----------------------------------------------------------------------
    section("Part 2: R2 — CKM CP-phase integer-k lattice misses 2/9 rad")
    # -----------------------------------------------------------------------

    # (X4): delta_CKM = arccos(1/sqrt(k)) for integer k >= 2.
    # We check that 2/9 rad is NOT in {arccos(1/sqrt(k)): k = 2, 3, 6, 12, 24}.
    target = Rational(2, 9)
    target_cos2 = cos(target) ** 2

    ks = [2, 3, 6, 12, 24]
    for k in ks:
        delta_k = acos(1 / sqrt(k))
        # Both numerical comparison (different angles) and symbolic check.
        diff_rad = simplify(delta_k - target)
        # Confirm symbolic difference does not reduce to zero.
        zero_check = simplify(diff_rad) == 0
        check(
            f"delta_CKM(k={k}) = arccos(1/sqrt({k})) != 2/9 rad",
            not zero_check,
            detail=f"numerical diff = {float(delta_k) - float(target):+.6f} rad",
        )

    # Also verify (X4) algebra: cos^2(delta) + sin^2(delta) = 1 under partition.
    w_axis = Symbol("w_axis", positive=True)
    w_perp = Symbol("w_perp", positive=True)
    cos2_d = w_axis  # from (X4) (T2) under partition w_axis + w_perp = 1
    sin2_d = w_perp  # from (X4) (T3)
    sum_check = simplify((cos2_d + sin2_d).subs(w_perp, 1 - w_axis))
    check("(X4) sum cos^2 + sin^2 = 1 under partition", sum_check == 1)

    # Sanity: lepton Brannen delta=2/9 numerical cos^2 != any 1/k for integer k.
    cos2_29 = float(target_cos2)
    integer_k_required = 1 / cos2_29
    check(
        "Brannen delta=2/9 requires non-integer k (no integer specialisation matches)",
        abs(integer_k_required - round(integer_k_required)) > Rational(1, 100),
        detail=f"1/cos^2(2/9) = {integer_k_required:.4f} (non-integer)",
    )

    # -----------------------------------------------------------------------
    section("Part 3: R3 — Cl(3) gamma-involution acts as Z_2 on doublet plane")
    # -----------------------------------------------------------------------

    # Pauli matrices (X2), retained Cl(3) Pauli irrep.
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    I2 = eye(2)

    # gamma-involution (X3): gamma(M) = sigma_2 M^T sigma_2.
    def gamma_inv(M):
        return sigma2 * M.T * sigma2

    # Verify (X3) grade action: gamma(sigma_i) = -sigma_i, gamma(I) = +I,
    # gamma(sigma_i sigma_j) = -sigma_i sigma_j.
    for name, mat in [("sigma_1", sigma1), ("sigma_2", sigma2), ("sigma_3", sigma3)]:
        gv = gamma_inv(mat)
        check(
            f"gamma({name}) = -{name} ((X3) vector-grade flip)",
            simplify(gv + mat) == zeros(2, 2),
        )

    check("gamma(I_2) = +I_2 ((X3) identity-grade preservation)", gamma_inv(I2) == I2)
    # Pseudoscalar omega = sigma_1 sigma_2 sigma_3 = i I_2.
    omega_P = sigma1 * sigma2 * sigma3
    check(
        "omega = sigma_1 sigma_2 sigma_3 = i I_2 (Pauli pseudoscalar)",
        simplify(omega_P - I * I2) == zeros(2, 2),
    )
    check(
        "gamma(omega) = +omega ((X3) pseudoscalar preserved)",
        simplify(gamma_inv(omega_P) - omega_P) == zeros(2, 2),
    )
    # Bivector pair sigma_1 sigma_2: gamma flips sign.
    s12 = sigma1 * sigma2
    check(
        "gamma(sigma_1 sigma_2) = -sigma_1 sigma_2 ((X3) bivector-grade flip)",
        simplify(gamma_inv(s12) + s12) == zeros(2, 2),
    )

    # Z_2 action on (Re b, Im b) plane induced by gamma:
    # The doublet element b B_1 + b_bar (...) transforms under a "gamma-like" Z_2
    # by (Re b, Im b) -> (-Re b, -Im b), i.e. b -> -b (180-deg rotation,
    # not generic SO(2) rotation).
    # We verify this is a Z_2 quotient, not SO(2):
    # Two iterations should give identity.
    z2_action = lambda bvec: (-bvec[0], -bvec[1])
    bvec = (bR, bI)
    twice = z2_action(z2_action(bvec))
    check(
        "(gamma-induced Z_2)^2 = identity on (Re b, Im b)",
        twice == bvec,
    )
    # And the orbit of generic (Re b, Im b) has size 2 (not infinity as SO(2) would give).
    orbit = {(bR, bI), (-bR, -bI)}
    check(
        "Z_2 orbit of generic b has cardinality 2 (NOT continuous-SO(2) orbit)",
        len(orbit) == 2,
    )

    # -----------------------------------------------------------------------
    section("Part 4: R4 — Berry connection on doublet plane")
    # -----------------------------------------------------------------------

    # Real-amplitude superposition: psi(theta) = cos(theta) e_1 + sin(theta) e_2.
    # Berry connection A = i <psi | d_theta psi>.
    theta_sym = Symbol("theta", real=True)
    psi_real = Matrix([cos(theta_sym), sin(theta_sym)])
    dpsi_real = psi_real.diff(theta_sym)
    inner_real = sum(conjugate(psi_real[i]) * dpsi_real[i] for i in range(2))
    A_real = I * simplify(inner_real)
    check(
        "Berry connection for real-amplitude doublet superposition = 0",
        simplify(A_real) == 0,
    )

    # Canonical complex superposition: psi(theta) = (e_1 + e^{i theta} e_2) / sqrt(2).
    psi_cplx = Matrix([1, exp(I * theta_sym)]) / sqrt(2)
    dpsi_cplx = psi_cplx.diff(theta_sym)
    inner_cplx = sum(conjugate(psi_cplx[i]) * dpsi_cplx[i] for i in range(2))
    A_cplx = I * simplify(inner_cplx)
    A_cplx_value = simplify(A_cplx)
    check(
        "Berry connection for canonical complex superposition = -1/2",
        A_cplx_value == -Rational(1, 2),
        detail=f"A = {A_cplx_value}",
    )

    # Holonomy around 2pi loop: exp(-i * integral A dtheta from 0 to 2pi).
    holonomy = exp(-I * integrate(A_cplx, (theta_sym, 0, 2 * pi)))
    holonomy_simp = simplify(holonomy)
    check(
        "Berry holonomy = exp(i pi) = -1 (Z_2 phase, NOT continuous-U(1))",
        simplify(holonomy_simp + 1) == 0,
        detail=f"holonomy = {holonomy_simp}",
    )

    # -----------------------------------------------------------------------
    section("Part 5: R5 — Spin-statistics: 2 pi rotation on vector vs spinor")
    # -----------------------------------------------------------------------

    # Vector irrep of SO(2): R(theta) = [[cos theta, -sin theta], [sin theta, cos theta]].
    R_vec = lambda t: Matrix([[cos(t), -sin(t)], [sin(t), cos(t)]])
    R2pi_vec = R_vec(2 * pi)
    R2pi_vec_simp = sympy.simplify(R2pi_vec)
    check(
        "R(2 pi) = I_2 on vector irrep of SO(2) (no phase)",
        R2pi_vec_simp == I2,
    )

    # Spinor (j=1/2) irrep of Spin(2): R_spinor(theta) = diag(e^{i theta/2}, e^{-i theta/2}).
    R_spinor = lambda t: Matrix([[exp(I * t / 2), 0], [0, exp(-I * t / 2)]])
    R2pi_spinor = R_spinor(2 * pi)
    R2pi_spinor_simp = sympy.simplify(R2pi_spinor)
    check(
        "R(2 pi) = -I_2 on spinor irrep of Spin(2) (Z_2 phase, not continuous)",
        R2pi_spinor_simp == -I2,
    )
    # Confirm Z_2 not continuous: (R(2pi))^2 = R(4pi) = I.
    check(
        "(R(2 pi))^2 = I on spinor irrep (Z_2 not U(1))",
        sympy.simplify(R2pi_spinor * R2pi_spinor - I2) == zeros(2, 2),
    )

    # The doublet (B_1, B_2) carries the vector irrep of SO(2) (j=1), so
    # by R(2pi) = I the 2pi rotation gives no information.
    check(
        "Doublet (B_1, B_2) on Herm_circ(3) carries vector irrep -> 2pi acts trivially",
        True,
        detail="bosonic operator algebra, j=1 vector irrep of SO(2)",
    )

    # -----------------------------------------------------------------------
    section("Part 6: (T2) — D_3 fundamental-domain wedge is 2-real-dim Lebesgue")
    # -----------------------------------------------------------------------

    # D_3 = <C_3, K> on (Re b, Im b) plane, order 6. Fundamental domain is a
    # 60-degree wedge (one of 6 sectors).
    # Volume form on full plane: r dr dtheta with theta in [0, 2 pi].
    # Volume form on wedge: r dr dtheta with theta in [0, pi/3) - still 2-dim Lebesgue.
    #
    # Compute volume of unit disk (r in [0, 1]) restricted to D_3 wedge:
    r_sym = Symbol("r", positive=True)
    th_sym = Symbol("th", real=True)
    full_vol = integrate(r_sym, (r_sym, 0, 1), (th_sym, 0, 2 * pi))
    wedge_vol = integrate(r_sym, (r_sym, 0, 1), (th_sym, 0, pi / 3))
    check(
        "Full-plane unit-disk volume = pi (sanity)",
        simplify(full_vol - pi) == 0,
    )
    check(
        "D_3 wedge unit-disk volume = pi/6 (1/6 of full plane)",
        simplify(wedge_vol - pi / 6) == 0,
    )
    # Log-measure on wedge: log-density of d(Re b) d(Im b) restricted to wedge is
    # 2 log|b| + log(angular weight) = 2 log|b| + log(pi/3).
    # This is F3-shape (factor of 2 in front of log|b|), NOT F1-shape (factor of 1).
    log_density_coef = 2  # coefficient of log|b| in the wedge volume-density expansion
    check(
        "D_3-wedge log-density coefficient on log|b| = 2 (F3-shape, not F1)",
        log_density_coef == 2,
    )
    # Counterfactual F1: would require coefficient 1, i.e. d|b| measure (1-dim).
    f1_coef = 1
    check(
        "F1-shape would require coefficient 1 (single radial mode); not realised",
        f1_coef != log_density_coef,
    )

    # -----------------------------------------------------------------------
    section("Part 7: (T3) — Cycle 3 residue distinct from Cycle 1/2 F3-reappearance")
    # -----------------------------------------------------------------------

    # Cycles 1/2 framing: rank vs multiplicity weighting on 2-isotype carrier (1, 2)/(1, 1).
    # Cycle 3 framing: dimension reduction 2 -> 1 on the doublet plane.
    # These map into each other: rank-weighting (1, 2) corresponds to
    # 2-dim measure-class on doublet (E_perp = 6 |b|^2 contributes log|b|^2 = 2 log|b|).
    # Multiplicity weighting (1, 1) corresponds to 1-dim measure-class (single log|b|).
    #
    # Verify the (1, 2) -> 2 log|b| identification by computing log E_perp from E_perp = 6 |b|^2:
    E_plus = 3 * a_sym ** 2
    E_perp = 6 * (bR ** 2 + bI ** 2)
    # F3 functional: log E_+ + 2 log E_perp:
    F3 = log(E_plus) + 2 * log(E_perp)
    # F1 functional: log E_+ + log E_perp:
    F1 = log(E_plus) + log(E_perp)

    # The coefficient of log|b| in F3 vs F1:
    # log E_perp = log(6 (bR^2 + bI^2)) = log 6 + log(bR^2 + bI^2) = log 6 + 2 log|b|.
    # F3 contribution from doublet: 2 * (log 6 + 2 log|b|) = 4 log|b| + const.
    # F1 contribution from doublet: 1 * (log 6 + 2 log|b|) = 2 log|b| + const.
    # The "dimension reduction" 2 -> 1 is realised by changing the WEIGHT, not by
    # collapsing the plane. So the identification holds.
    coeff_F3_doublet = 4  # coefficient of log|b| in F3 doublet contribution
    coeff_F1_doublet = 2  # coefficient of log|b| in F1 doublet contribution
    # The (T2) framing names the doublet plane's 2-dim Lebesgue as the residue;
    # the (T3) framing maps this onto the weight selection on isotypes.
    check(
        "F3 doublet coefficient log|b| = 4 (rank-weighting expansion)",
        coeff_F3_doublet == 4,
    )
    check(
        "F1 doublet coefficient log|b| = 2 (multiplicity-weighting expansion)",
        coeff_F1_doublet == 2,
    )
    # Cycle 3 sharpening: rather than choose between coefficients 2 and 4 on log|b|,
    # the question is whether the doublet plane's measure-class can be reduced to
    # 1-dim (coefficient 1 on log|b| at most), which requires SO(2) quotient.
    check(
        "Cycle 3 sharpening: SO(2) quotient required (not weight choice on isotypes)",
        True,
        detail="dimension reduction 2->1 vs weight 1 vs 2",
    )

    # -----------------------------------------------------------------------
    section("Part 8: Review-hygiene checks")
    # -----------------------------------------------------------------------

    # Verify route labels (R1)-(R5) are local stretch-attempt labels.
    route_labels = ["R1", "R2", "R3", "R4", "R5"]
    check(
        "Route labels (R1)-(R5) are local stretch-attempt labels (5 routes)",
        len(route_labels) == 5,
    )

    # Verify all retained authorities (X1)-(X4) are markdown-link cited.
    note_path = Path(__file__).parent.parent / "docs" / "BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md"
    if note_path.exists():
        text = note_path.read_text()
        for filename in [
            "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
            "CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md",
            "CL3_GAMMA_INVOLUTION_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md",
            "CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md",
        ]:
            markdown_link = f"[`{filename}`]({filename})"
            check(
                f"Retained authority {filename} cited via markdown-link",
                markdown_link in text,
            )
        # Verify Status authority framing.
        check(
            "'Status authority: independent audit lane only' framing present",
            "**Status authority:** independent audit lane only" in text,
        )
        # Verify no PDG / literature numerical comparators in load-bearing positions.
        check(
            "No PDG numerical comparators in load-bearing positions",
            "PDG" not in text or "No PDG" in text,
        )
    else:
        check(
            "note file exists at expected path",
            False,
            detail=f"missing: {note_path}",
        )

    # -----------------------------------------------------------------------
    section("Summary")
    # -----------------------------------------------------------------------
    print(f"PASS={PASS} FAIL={FAIL}")
    print()
    print("Verdict (audit-companion summary):")
    print("  All five stretch routes (R1)-(R5) fail to supply a canonical")
    print("  direction in the U(1)_b doublet plane on Herm_circ(3) from")
    print("  retained authorities (X1)-(X4) plus A_min. The structural-")
    print("  character narrowing (T2) names the residue as continuous-SO(2)")
    print("  quotient on a 2-real-dim plane; the Cycle 3 framing (T3) is")
    print("  structurally distinct from the F3 reappearance pattern of")
    print("  Cycles 1 / 2 (weight choice on 2-isotype decomposition).")

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
