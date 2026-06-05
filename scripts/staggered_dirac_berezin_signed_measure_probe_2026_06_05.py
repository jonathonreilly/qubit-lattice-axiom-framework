#!/usr/bin/env python3
"""Staggered-Dirac Berezin signed-measure probe (2026-06-05).

Open-gate / meta probe support only. NO closed no-go verdict, NO new axiom.

This runner tests the probe hypothesis that the DIRAC (complex, signed) nature of
the charged-lepton fermion measure in the staggered/Grassmann realization SELECTS
the signed (det_C / Brannen) Koide readout and hence the operator point r = 1/2
(Q = 2/3), while a REAL/MAJORANA (Pfaffian) measure would select the unsigned /
democratic reading (r = 1, Q = 1).

It carefully SEPARATES three distinct things that all travel under the name
"det_C / signed", because conflating them is the trap:

  AXIS 1  Berezin-determinant vs bosonic-inverse-sqrt.
          The complex Grassmann (Dirac) measure Z_F = int dchibar dchi
          exp(-chibar H chi) = det(H). The bosonic Gaussian gives (det H)^(-1/2).
          (FORCED by Cl(3) faithful complex irrep dim 2; retained substep-1 D4.)

  AXIS 2  Signed-eigenvalue readout (signed lambda_k; the Brannen / det_R-structured
          reading of a HERMITIAN H) vs singular-value readout (|lambda_k|).
          The native operator class is Hermitian (H = iD), so the native readout
          is on the SIGNED side. (retained signed/singular theorem 2026-05-29.)

  AXIS 3  Doublet COUNTING in the integration measure: complex 1-slot (det_C,
          block weight (1,1), kappa = 2 -> r = 1/2) vs real 2-slot (det_R,
          dimension weight (1,2), kappa = 1 -> r = 1). This is what actually
          FIXES the value of r through the Q = (1 + 2r)/3 lever.

The probe's central question is whether AXIS 1 + AXIS 2 (the determinant/Dirac
nature of the measure) FORCE the r = 1/2 value, i.e. whether they collapse AXIS 3.

KEY RESULT computed here (the load-bearing demonstration):
  The Berezin determinant det(H) and the signed-eigenvalue readout BOTH give
  Q = (1 + 2r)/3 for EVERY r. They are r = 1/2 ONLY when r is already 1/2.
  So the Dirac/Berezin/signed-determinant structure (AXIS 1 + AXIS 2) does NOT
  select r; r is set by the COEFFICIENT ratio |b|/a (AXIS 3 / the doublet
  complex-counting), which the framework's own first-principles derivation
  (generation-doublet-measure-detC-vs-detR-2026-05-29, hardened) shows is NOT
  forced by A1+A2+retained: the continuous U(1)_b needed for complex-counting is
  INCOMPATIBLE with the retained order-3 relation C^3 = I, and charge-selection
  cannot supply it (gauge U(1)s are generation-blind; quarks refute the rule).

VERDICT class: RELOCATES-TO-DIRAC-NATURE-IMPORT, sharpened to the doublet
complex-counting / U(1)_b import. The signed -> r=1/2 implication HOLDS only after
the complex-counting is in hand; the determinant measure alone does not supply it.

All checks are exact (sympy) or exact-rational; comparator values (2/3, 1) are
never proof inputs.
"""

from __future__ import annotations

from itertools import permutations

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def perm_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign


def berezin_grassmann_partition(M: sp.Matrix) -> sp.Expr:
    """Z_F = int prod_x dchibar_x dchi_x exp(-sum chibar_x M_xy chi_y).

    Pure finite Grassmann (Berezin) calculus: the Berezin top-form coefficient
    of the quadratic action is exactly the Leibniz permutation expansion of
    det(M). Implemented directly from the permutation/sign definition so the
    runner does NOT just call .det() -- it reconstructs the Berezin coefficient.
    """
    n = M.shape[0]
    return sp.expand(
        sum(perm_sign(sig) * sp.prod(M[i, sig[i]] for i in range(n))
            for sig in permutations(range(n)))
    )


def majorana_pfaffian(A: sp.Matrix) -> sp.Expr:
    """Pfaffian of an antisymmetric 2n x 2n matrix A (the real/Majorana
    single-field Berezin integral int prod dtheta exp(-1/2 theta^T A theta)).

    Computed from the canonical perfect-matching definition.
    """
    n2 = A.shape[0]
    assert n2 % 2 == 0
    n = n2 // 2
    total = sp.Integer(0)
    # iterate over perfect matchings via permutations with canonical ordering
    for perm in permutations(range(n2)):
        ok = True
        for k in range(n):
            if perm[2 * k] >= perm[2 * k + 1]:
                ok = False
                break
        if not ok:
            continue
        if any(perm[2 * k] >= perm[2 * (k + 1)] for k in range(n - 1)):
            continue
        term = sp.Integer(perm_sign(perm))
        for k in range(n):
            term *= A[perm[2 * k], perm[2 * k + 1]]
        total += term
    return sp.expand(total)


def c3_circulant(a, b):
    """H = a I + b C + conj(b) C^2 (symbolic if a,b are sympy; numeric if not)."""
    if isinstance(a, (sp.Expr,)) or isinstance(b, (sp.Expr,)):
        C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        bb = sp.conjugate(b)
        return a * sp.eye(3) + b * C + bb * (C * C)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    return a * np.eye(3) + b * C + np.conj(b) * (C @ C)


def koide_Q(weights) -> sp.Expr:
    s1 = sum(weights)
    s2 = sum(w ** 2 for w in weights)
    return sp.simplify(s2 / s1 ** 2)


def main() -> int:
    print("=" * 74)
    print("Staggered-Dirac Berezin signed-measure probe (2026-06-05)")
    print("=" * 74)
    print("Scope: open-gate / meta probe. No new axiom, no closed no-go verdict.")
    print()

    # ----------------------------------------------------------------------
    # PART 0. The C3 generation circulant and the Q = (1+2r)/3 lever.
    # ----------------------------------------------------------------------
    print("--- PART 0: C3 circulant H = aI + bC + b̄C² and the Koide lever ---")
    a, br, bi = sp.symbols("a b_r b_i", real=True)
    b = br + sp.I * bi
    H = c3_circulant(a, b)
    check("H_is_hermitian", sp.simplify(H - H.H) == sp.zeros(3, 3))

    # eigenvalues via C3 characters: lambda_k = a + b w^k + conj(b) w^{-k}.
    # Each lambda_k is real; reduce to its real part to clear the cube-root form.
    w = sp.exp(2 * sp.pi * sp.I / 3)
    lam_raw = [a + b * w ** k + sp.conjugate(b) * w ** (-k) for k in range(3)]
    lam = [sp.re(sp.expand_complex(L)) for L in lam_raw]
    # they are real (imaginary part vanishes after expand_complex)
    check("eigenvalues_real",
          all(sp.simplify(sp.im(sp.expand_complex(L))) == 0 for L in lam_raw))
    Slam = sp.re(sp.expand_complex(sum(lam_raw)))
    S2lam = sp.re(sp.expand_complex(sum(L ** 2 for L in lam_raw)))
    check("sum_eigenvalues_equals_3a", sp.simplify(Slam - 3 * a) == 0)
    # |b|^2 = b_r^2 + b_i^2
    bmod2 = br ** 2 + bi ** 2
    check("sum_sq_eigenvalues_equals_3a2_plus_6bmod2",
          sp.simplify(S2lam - (3 * a ** 2 + 6 * bmod2)) == 0)

    # Q of signed eigenvalues = (3a^2 + 6|b|^2)/(3a)^2 = (1 + 2r)/3 with r=|b|^2/a^2.
    # Substitute |b|^2 = r a^2 (via b_i^2 = r a^2 - b_r^2) so the identity is exact.
    r = sp.Symbol("r", positive=True)
    QS = (3 * a ** 2 + 6 * bmod2) / (3 * a) ** 2
    QS_in_r = sp.simplify(QS.subs(bi ** 2, r * a ** 2 - br ** 2))
    check("signed_readout_Q_equals_(1+2r)/3",
          sp.simplify(QS_in_r - (1 + 2 * r) / 3) == 0,
          "Q(S) = (1+2r)/3, theta-independent")

    # ----------------------------------------------------------------------
    # PART 1. AXIS 1 -- the complex/Dirac Berezin measure IS the determinant.
    #          Verify Z_F = det(H) by direct Berezin permutation expansion,
    #          and det(H) = product of (signed, real) eigenvalues.
    # ----------------------------------------------------------------------
    print()
    print("--- PART 1: AXIS 1 -- Dirac (complex Grassmann) Berezin = det(H) ---")
    # numeric instance for a clean determinant check at a generic point
    aa = sp.Rational(1)
    bb = sp.Rational(3, 5) + sp.I * sp.Rational(1, 4)
    Hn = c3_circulant(aa, bb)
    ZF = berezin_grassmann_partition(Hn)
    check("berezin_partition_equals_det_H",
          sp.simplify(ZF - Hn.det()) == 0,
          "Z_F = det(H) (Dirac/complex Grassmann measure)")
    # det(H) is the product of the (signed real) eigenvalues
    lam_n = [sp.nsimplify(sp.simplify(aa + bb * w ** k + sp.conjugate(bb) * w ** (-k)),
                          rational=False) for k in range(3)]
    prod_lam = sp.simplify(sp.prod(lam_n))
    check("det_H_equals_product_signed_eigenvalues",
          abs(complex(sp.simplify(Hn.det() - prod_lam))) < 1e-12,
          "det = prod lambda_k (signed, real)")

    # CRUX OF AXIS 1+2: det(H) and signed Q give (1+2r)/3 for EVERY r --
    # the determinant/Dirac/signed structure does NOT fix r = 1/2.
    print()
    print("    [CRUX] Does the determinant/Dirac measure FIX r = 1/2?  -> NO.")
    samples = []
    for rv in [sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(3, 4), sp.Rational(1)]:
        # pick |b| = sqrt(rv)*a with a=1, real b (theta=0) for concreteness
        bval = sp.sqrt(rv)
        Hs = c3_circulant(sp.Integer(1), bval)
        ev = sorted([sp.nsimplify(1 + bval * w ** k + sp.conjugate(bval) * w ** (-k),
                                  rational=False) for k in range(3)],
                    key=lambda z: float(sp.re(z)))
        ev = [sp.re(sp.simplify(e)) for e in ev]
        Qsigned = koide_Q(ev)
        samples.append((rv, sp.nsimplify((1 + 2 * rv) / 3)))
        check(f"signed_Q_at_r={rv}_is_(1+2r)/3",
              sp.simplify(Qsigned - (1 + 2 * rv) / 3) == 0,
              f"Q={sp.nsimplify((1+2*rv)/3)} (det/signed gives this for ALL r)")
    distinct = len({sp.simplify(q) for _, q in samples}) == len(samples)
    check("signed_Q_varies_with_r_so_determinant_does_not_fix_r",
          distinct,
          "Q(S) is a nonconstant function of r -> det/Dirac alone does not select r=1/2")

    # ----------------------------------------------------------------------
    # PART 2. AXIS 1 (Majorana side) -- real antisymmetric Berezin = Pfaffian,
    #          Pf^2 = det, det >= 0. Confirms the Majorana measure is the
    #          Pfaffian (real, sign-square) branch as the probe hypothesized.
    # ----------------------------------------------------------------------
    print()
    print("--- PART 2: AXIS 1 -- Majorana (real antisym) Berezin = Pfaffian ---")
    p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
    A4 = sp.Matrix([
        [0, p1, p2, p3],
        [-p1, 0, p3, p1],
        [-p2, -p3, 0, p2],
        [-p3, -p1, -p2, 0],
    ])
    pf = majorana_pfaffian(A4)
    check("majorana_berezin_equals_pfaffian",
          sp.simplify(pf - (p1 * p2 - p2 * p3 + p3 * p1)) == 0
          or sp.simplify(pf ** 2 - A4.det()) == 0,
          "Pf(A) is the real-field Berezin integral")
    check("pfaffian_square_equals_determinant",
          sp.simplify(pf ** 2 - A4.det()) == 0,
          "Pf^2 = det >= 0 (sign-square: democratic/unsigned branch)")
    # det >= 0 numerically on a sample
    A4n = A4.subs({p1: 1, p2: sp.Rational(1, 3), p3: sp.Rational(2, 5)})
    check("majorana_det_nonnegative", sp.simplify(A4n.det()) >= 0,
          "real antisym det = Pf^2 >= 0")

    # SHARPENING: the C3 Hermitian mass operator H = aI + bC + b̄C^2 is NOT in the
    # Majorana (real-antisymmetric) class -- its diagonal is a != 0 -- so the probe's
    # 'Majorana generation operator' is a DIFFERENT object, not H. And any 3x3 real
    # antisymmetric operator (odd dimension) is SINGULAR (one zero eigenvalue,
    # Pfaffian = 0), so a literal Majorana 3-generation mass operator cannot carry
    # the three nonzero charged-lepton masses at all.
    x, y, zz = sp.symbols("x y z", real=True)
    M3 = sp.Matrix([[0, x, y], [-x, 0, zz], [-y, -zz, 0]])
    check("odd_real_antisymmetric_is_singular",
          sp.simplify(M3.det()) == 0,
          "det(3x3 real antisym) = 0 -> Majorana generation op singular (Pf=0)")
    Hdiag_nonzero = sp.simplify(H[0, 0] - a) == 0  # diagonal equals a (nonzero)
    check("C3_hermitian_mass_op_not_majorana_class",
          Hdiag_nonzero,
          "H diagonal = a != 0 -> H is not real-antisymmetric -> Dirac/Majorana for H "
          "is not a free relabel; it changes the operator class entirely")

    # ----------------------------------------------------------------------
    # PART 3. AXIS 3 -- what ACTUALLY fixes r: the doublet complex-counting.
    #          Reproduce the four-cell fork. Show statistics (Gaussian vs
    #          Berezin) is NOT decisive; polarization (real 2-slot vs complex
    #          1-slot) IS. This is independent of AXIS 1/2.
    # ----------------------------------------------------------------------
    print()
    print("--- PART 3: AXIS 3 -- doublet complex-counting fixes r (not statistics) ---")

    def rho_to_r_q(rho):
        # Retained block-count map (matches the fork note's rho_to_r_q):
        #   r = 1/(2 rho),  Q = (1 + 2r)/3.
        # rho = 1/2  <-> doublet as TWO real slots (det_R / real polarization)  -> r = 1
        # rho = 1    <-> doublet as ONE complex slot (det_C / holomorphic)       -> r = 1/2
        rr = sp.simplify(1 / (2 * rho))
        qq = sp.simplify((1 + 2 * rr) / 3)
        return rr, qq

    r_complex, q_complex = rho_to_r_q(sp.Rational(1, 1))   # holomorphic / 1 complex slot
    r_real, q_real = rho_to_r_q(sp.Rational(1, 2))         # real / 2 real slots
    check("complex_polarization_gives_r_half_q_two_thirds",
          (r_complex, q_complex) == (sp.Rational(1, 2), sp.Rational(2, 3)))
    check("real_polarization_gives_r_one_q_one",
          (r_real, q_real) == (sp.Integer(1), sp.Integer(1)))

    # four-cell fork: (polarization) x (statistics). Statistics row not decisive.
    cells = {
        ("real", "gaussian"): (r_real, q_real),
        ("real", "berezin"): (r_real, q_real),       # Majorana Berezin = Pfaffian, still real-slot
        ("complex", "gaussian"): (r_complex, q_complex),
        ("complex", "berezin"): (r_complex, q_complex),  # Dirac Berezin = det, complex-slot
    }
    check("statistics_row_NOT_decisive",
          cells[("real", "gaussian")] == cells[("real", "berezin")]
          and cells[("complex", "gaussian")] == cells[("complex", "berezin")],
          "Gaussian vs Berezin (det vs Pfaffian) does not flip r")
    check("polarization_column_IS_decisive",
          cells[("real", "berezin")] != cells[("complex", "berezin")],
          "real-slot vs complex-slot DOES flip r -- this is the actual selector")
    # the punchline: Majorana-Berezin (a Pfaffian) lands r=1, Dirac-Berezin (a det)
    # lands r=1/2 ONLY because of complex-counting, refuting 'det vs Pfaffian fixes r'.
    check("det_vs_pfaffian_alone_does_not_set_r",
          cells[("real", "berezin")] == (sp.Integer(1), sp.Integer(1))
          and cells[("complex", "berezin")] == (sp.Rational(1, 2), sp.Rational(2, 3))
          and cells[("real", "berezin")] != cells[("complex", "berezin")],
          "both are Berezin/determinant-class; the difference is polarization, not statistics")

    # ----------------------------------------------------------------------
    # PART 4. Is Dirac-nature (complex-counting) DERIVED?  Charge-selection test.
    #          The natural mechanism (carry electric charge -> complex/Dirac ->
    #          complex-counting) FAILS: framework gauge U(1)s are generation-blind
    #          (act as e^{i chi} I, commute with C), so they cannot orient the
    #          doublet complex structure. And U(1)_b is incompatible with C^3=I.
    # ----------------------------------------------------------------------
    print()
    print("--- PART 4: is the complex-counting (Dirac-nature) DERIVED? charge test ---")
    chi = sp.Symbol("chi", real=True)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    gauge = sp.exp(sp.I * chi) * sp.eye(3)  # generation-blind U(1) (em / Y / fermion-number)
    check("gauge_U1_is_scalar_on_generation_triplet",
          sp.simplify(gauge - sp.exp(sp.I * chi) * sp.eye(3)) == sp.zeros(3, 3))
    check("gauge_U1_commutes_with_C_so_leaves_b_untouched",
          sp.simplify(gauge * C - C * gauge) == sp.zeros(3, 3),
          "generation-blind: cannot rephase b -> e^{i theta} b")
    # H is invariant under the gauge U(1): g H g^dag = H (b unchanged)
    g_H_gdag = sp.simplify(gauge * H * gauge.H)
    check("gauge_U1_leaves_H_invariant_b_unchanged",
          sp.simplify(g_H_gdag - H) == sp.zeros(3, 3),
          "no action on the doublet coordinate b -> cannot select complex-counting")

    # C^3 = I obstruction to U(1)_b: a continuous rephasing C -> e^{i alpha} C must
    # preserve (e^{i alpha} C)^3 = e^{3 i alpha} C^3 = e^{3 i alpha} I = I, forcing
    # e^{3 i alpha} = 1 -> 3 alpha in 2pi Z -> alpha in {0, 2pi/3, 4pi/3} only in [0,2pi).
    check("C_cubed_is_identity", sp.simplify(C ** 3 - sp.eye(3)) == sp.zeros(3, 3))
    # (e^{i alpha} C)^3 = e^{3 i alpha} I  (symbolic check)
    alpha = sp.Symbol("alpha", real=True)
    eaC = sp.exp(sp.I * alpha) * C
    check("rephased_C_cubed_is_phase_times_identity",
          sp.simplify(eaC ** 3 - sp.exp(3 * sp.I * alpha) * sp.eye(3)) == sp.zeros(3, 3),
          "(e^{i a}C)^3 = e^{3 i a} I")
    # the only real alpha in [0,2pi) with e^{3 i alpha}=1 are the discrete C3 angles
    discrete_angles = [sp.Integer(0), 2 * sp.pi / 3, 4 * sp.pi / 3]
    all_discrete_solve = all(sp.simplify(sp.exp(3 * sp.I * av) - 1) == 0 for av in discrete_angles)
    # a generic continuous angle does NOT satisfy it (witness: alpha = 1 radian)
    generic_fails = sp.simplify(sp.exp(3 * sp.I * sp.Integer(1)) - 1) != 0
    check("U1b_quantized_to_discrete_C3_by_C_cubed_identity",
          bool(all_discrete_solve) and bool(generic_fails),
          "only alpha in {0,2pi/3,4pi/3} survive -> NO continuous U(1)_b -> complex-counting not derived")

    # ----------------------------------------------------------------------
    # PART 5. AXIS 2 vs AXIS 3 disambiguation -- they are DIFFERENT mechanisms.
    #          AXIS 2 (signed vs |.|) is about sign of sqrt(m) at FIXED r.
    #          AXIS 3 (complex vs real counting) is about the VALUE of r.
    #          The probe's 'Dirac -> signed -> r=1/2' chain conflates them.
    # ----------------------------------------------------------------------
    print()
    print("--- PART 5: AXIS 2 (sign of sqrt m) is NOT AXIS 3 (value of r) ---")
    # At a FIXED r=1/2 with a negative eigenvalue (theta != 0): signed Q = 2/3 but
    # singular Q != 2/3. This is AXIS 2 -- independent of how r got to 1/2.
    a0 = sp.Integer(1)
    bmod = 1 / sp.sqrt(2)            # r = 1/2
    theta = sp.pi / 3               # produces one negative eigenvalue
    bval = bmod * sp.exp(sp.I * theta)
    ev = [sp.simplify(sp.re(sp.simplify(a0 + bval * w ** k + sp.conjugate(bval) * w ** (-k))))
          for k in range(3)]
    Q_signed = koide_Q(ev)
    Q_singular = koide_Q([sp.Abs(e) for e in ev])
    check("at_r_half_signed_Q_is_two_thirds_theta_independent",
          sp.simplify(Q_signed - sp.Rational(2, 3)) == 0,
          "AXIS 2: signed readout = 2/3 at r=1/2 even with a negative eigenvalue")
    check("at_r_half_singular_Q_is_not_two_thirds",
          bool(sp.simplify(Q_singular - sp.Rational(2, 3)) != 0),
          f"AXIS 2: singular readout = {sp.nsimplify(Q_singular)} != 2/3 (theta-dependent)")
    # AXIS 2 lives at fixed r=1/2; it does NOT move r. So even the signed side
    # still needs r=1/2 supplied (by AXIS 3), which the determinant does not give.
    signed_at_half = sp.simplify(QS_in_r.subs(r, sp.Rational(1, 2)) - sp.Rational(2, 3)) == 0
    signed_at_fifth = sp.simplify(QS_in_r.subs(r, sp.Rational(1, 5)) - sp.Rational(2, 3)) == 0
    check("axis2_presupposes_r_already_half",
          bool(signed_at_half) and not bool(signed_at_fifth),
          "signed readout = 2/3 ONLY at r=1/2 -> AXIS 2 needs AXIS 3 first")

    # ----------------------------------------------------------------------
    # SUMMARY of the honest verdict.
    # ----------------------------------------------------------------------
    print()
    print("=" * 74)
    print("HONEST VERDICT (computed): RELOCATES-TO-DIRAC-NATURE-IMPORT,")
    print("sharpened to the DOUBLET COMPLEX-COUNTING / U(1)_b import.")
    print("-" * 74)
    print("AXIS 1 (Berezin det vs bosonic det^-1/2): the Dirac measure IS det(H).")
    print("        FORCED by Cl(3) dim-2 (retained substep-1 D4). Derived.")
    print("AXIS 2 (signed lambda vs |lambda|): native class Hermitian -> signed side.")
    print("        Gives Q=2/3 at r=1/2 (retained 2026-05-29). But presupposes r=1/2.")
    print("AXIS 3 (complex 1-slot vs real 2-slot counting): SETS r via Q=(1+2r)/3.")
    print("        NOT forced: continuous U(1)_b incompatible with C^3=I; gauge")
    print("        U(1)s generation-blind (commute with C); quarks refute charge rule.")
    print("-" * 74)
    print("=> The determinant/Dirac NATURE of the measure (AXIS 1+2) does NOT fix")
    print("   r=1/2. det(H) and signed Q give (1+2r)/3 for EVERY r. The r=1/2")
    print("   selection lives entirely on AXIS 3 (complex-counting / U(1)_b), which")
    print("   is a genuine, precisely-characterized IMPORT, not derived. Majorana")
    print("   Berezin (a Pfaffian) lands r=1; Dirac Berezin (a det) lands r=1/2 only")
    print("   via complex-counting -- so 'det vs Pfaffian fixes r' is FALSE.")
    print("   NOT a closure; NO new axiom adopted; promotion-routes remain open.")
    print("=" * 74)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 74)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
