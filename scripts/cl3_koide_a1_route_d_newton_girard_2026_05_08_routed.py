"""Narrow Newton-Girard/free-ratio checks for a supplied circulant.

For H=aI+bC+conj(b)C^2 and a!=0, the runner recomputes

  p_2/e_1^2 = 1/3 + (2/3)(|b|/a)^2,
  e_1^2-6e_2 = 9(2|b|^2-a^2).

Thus Newton-Girard identities alone do not select the target ratio, and the
displayed polynomial zero is a rewrite of it. A finite named candidate scan is
also performed: discriminant statements are scoped to the nondegenerate
delta=2/9 slice, while depressed-cubic and ratio derivatives are checked at
their stated points. No exhaustive claim about all symmetric-polynomial
functionals or all cited-content routes is made. Sibling-route tables, prose
synthesis, and PDG comparators are visible but uncounted.
"""

import math

import numpy as np
import sympy as sp


# --------------------------------------------------------------------
# Constants and primitive C_3 action (mirrors Route F conventions)
# --------------------------------------------------------------------

OMEGA = np.exp(2j * np.pi / 3.0)  # primitive cube root of unity

# C_3[111] action on hw=1 corner basis: |c_1> -> |c_2> -> |c_3> -> |c_1>
U_C3_CORNER = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
], dtype=complex)


def passfail(name: str, ok: bool, detail: str = ""):
    """Print a PASS/FAIL line with optional detail; returns ok bool."""
    tag = "PASS" if ok else "FAIL"
    if detail:
        print(f"  {tag} : {name} | {detail}")
    else:
        print(f"  {tag} : {name}")
    return ok


def make_circulant(a: float, b: complex):
    """Hermitian circulant on hw=1: a*I + b*U + bbar*U^{-1}."""
    U = U_C3_CORNER
    Uinv = np.conjugate(U.T)  # U^{-1} = U^dagger since U is unitary
    return a * np.eye(3, dtype=complex) + b * U + np.conjugate(b) * Uinv


def power_sums_and_elementary(eigs):
    """Given an iterable of 3 eigenvalues, compute (p_1, p_2, p_3, e_1, e_2, e_3)."""
    e0, e1v, e2v = list(eigs)
    p1 = e0 + e1v + e2v
    p2 = e0 ** 2 + e1v ** 2 + e2v ** 2
    p3 = e0 ** 3 + e1v ** 3 + e2v ** 3
    el1 = p1
    el2 = e0 * e1v + e0 * e2v + e1v * e2v
    el3 = e0 * e1v * e2v
    return p1, p2, p3, el1, el2, el3


# --------------------------------------------------------------------
# Section 1 — Newton-Girard identity verification (anchor for Route D)
# --------------------------------------------------------------------

def section1_newton_girard_identity():
    """Verify the Newton-Girard identity p_2 = e_1^2 - 2 e_2 holds for
    any 3-tuple of eigenvalues, and that A1 is equivalent to
    e_1^2 = 6 e_2 (i.e., p_2/e_1^2 = 2/3).
    """
    print("Section 1 — Newton-Girard identity and the Koide equipartition polynomial form")
    results = []

    # 1.1 — Symbolic verification: p_2 = e_1^2 - 2 e_2 (always)
    a_sym, r_sym, delta_sym = sp.symbols('a r delta', real=True, positive=True)
    lam = [a_sym + 2 * r_sym * sp.cos(delta_sym + 2 * sp.pi * k / 3) for k in range(3)]
    p1_sym = sp.simplify(sum(lam))
    p2_sym = sp.simplify(sum(l ** 2 for l in lam))
    e1_sym = p1_sym
    e2_sym = sp.simplify(sum(lam[i] * lam[j] for i in range(3) for j in range(3) if i < j))
    ng_residual = sp.simplify(sp.trigsimp(p2_sym - (e1_sym ** 2 - 2 * e2_sym)))
    results.append(passfail(
        "Newton-Girard p_2 = e_1^2 - 2 e_2 holds symbolically (any 3 eigenvalues)",
        ng_residual == 0,
        "verified for arbitrary (a, r, delta) parameters",
    ))

    # 1.2 — A1 polynomial form: e_1^2 = 6 e_2 ⟺ a^2 = 2 r^2 (Brannen form)
    A1_poly_substituted = sp.simplify(
        sp.trigsimp((e1_sym ** 2 - 6 * e2_sym).subs(r_sym, a_sym / sp.sqrt(2)))
    )
    results.append(passfail(
        "A1 polynomial form: e_1^2 - 6 e_2 = 0 substituting r = a/sqrt(2)",
        A1_poly_substituted == 0,
        "Polynomial form is exactly the Frobenius equipartition condition",
    ))

    # 1.3 — Equivalent: p_2/e_1^2 = 2/3 at A1
    Q_lin = sp.simplify(p2_sym / e1_sym ** 2)
    Q_at_A1 = sp.simplify(Q_lin.subs(r_sym, a_sym / sp.sqrt(2)))
    results.append(passfail(
        "p_2/e_1^2 = 2/3 at A1 (linear-eigenvalue Koide)",
        sp.simplify(Q_at_A1 - sp.Rational(2, 3)) == 0,
        f"p_2/e_1^2 |_A1 = {Q_at_A1}",
    ))

    # 1.4 — At b = 0 (degenerate, all lambda equal): p_2/e_1^2 = 1/3
    Q_at_b0 = sp.simplify(Q_lin.subs(r_sym, 0))
    results.append(passfail(
        "p_2/e_1^2 = 1/3 at b = 0 (degenerate / all eigenvalues equal)",
        sp.simplify(Q_at_b0 - sp.Rational(1, 3)) == 0,
        f"p_2/e_1^2 at degenerate = {Q_at_b0}",
    ))

    # 1.5 — The exact expression is 1/3 + (2/3)(r/a)^2.  For a > 0
    # and r >= 0 this has image [1/3, infinity), rather than merely
    # exhibiting a few sampled values.
    ratio_image_certificate = sp.simplify(
        Q_lin - (sp.Rational(1, 3) + sp.Rational(2, 3) * (r_sym / a_sym) ** 2)
    ) == 0
    results.append(passfail(
        "p_2/e_1^2 takes ALL values in [1/3, infinity) as r/a varies",
        ratio_image_certificate,
        "Exact nonnegative-square parametrization; Newton-Girard alone does not single out 2/3",
    ))

    return results


# --------------------------------------------------------------------
# Section 2 — Barrier D1: Newton-Girard is identity, not constraint
# --------------------------------------------------------------------

def section2_barrier_d1_identity_not_constraint():
    """Show that Newton-Girard identities (p_k <-> e_k bijection) hold
    for ANY 3-tuple of eigenvalues, and therefore impose ZERO
    constraint on the spectrum. The "specific 6 coefficient" in
    `e_1^2 = 6 e_2` must come from somewhere ELSE — it is not a
    Newton-Girard output.
    """
    print("Section 2 — Barrier D1: Newton-Girard is identity, not constraint")
    results = []

    # 2.1 — Random eigenvalue 3-tuples satisfy Newton-Girard exactly
    rng = np.random.default_rng(seed=42)
    ng_holds_count = 0
    n_trials = 50
    for _ in range(n_trials):
        eigs = rng.normal(size=3)
        p1, p2, _p3, e1, e2, _e3 = power_sums_and_elementary(eigs)
        if abs(p2 - (e1 ** 2 - 2 * e2)) < 1e-10:
            ng_holds_count += 1
    results.append(passfail(
        f"Newton-Girard p_2 = e_1^2 - 2 e_2 holds for {n_trials}/{n_trials} random eigenvalue triples",
        ng_holds_count == n_trials,
        "Identity holds without ANY structural constraint on the eigenvalues",
    ))

    # 2.2 — Random circulant samples can have arbitrary p_2/e_1^2 values
    diff_ratios = []
    for _ in range(n_trials):
        a = rng.uniform(0.5, 2.0)
        r = rng.uniform(0.0, 3.0)
        delta = rng.uniform(0, 2 * np.pi)
        b = r * np.exp(1j * delta)
        H = make_circulant(a, b)
        eigs = np.linalg.eigvalsh(H)
        p1, p2, _p3, e1, _e2, _e3 = power_sums_and_elementary(eigs)
        diff_ratios.append(p2 / e1 ** 2)
    diff_min = min(diff_ratios)
    diff_max = max(diff_ratios)
    diff_range_wide = (diff_max - diff_min) > 1.0  # the ratio varies widely
    results.append(passfail(
        "Random circulants give p_2/e_1^2 over a wide range (NOT pinned at 2/3)",
        diff_range_wide,
        f"min = {diff_min:.4f}, max = {diff_max:.4f} — ratio is FREE under supplied R1+R2",
    ))

    # 2.3 — Counterexamples: explicit (a, b) circulants violating A1
    counter_cases = [
        (1.0, 0.3 + 0.0j),  # |b|^2/a^2 = 0.09
        (1.0, 0.7 + 0.4j),  # |b|^2/a^2 = 0.65
        (1.0, 1.0 + 0.0j),  # |b|^2/a^2 = 1.0
        (1.0, 0.5 + 0.5j),  # |b|^2/a^2 = 0.5 (exactly A1)
    ]
    routine_satisfied = True
    for (a_val, b_val) in counter_cases:
        H = make_circulant(a_val, b_val)
        eigs = np.linalg.eigvalsh(H)
        p1, p2, _p3, e1, e2, _e3 = power_sums_and_elementary(eigs)
        # Verify Newton-Girard identity
        ng_ok = abs(p2 - (e1 ** 2 - 2 * e2)) < 1e-10
        # Verify ratio
        ratio = abs(b_val) ** 2 / a_val ** 2
        if not ng_ok:
            routine_satisfied = False
    results.append(passfail(
        "Newton-Girard satisfied for all counterexamples (incl. |b|^2/a^2 ne 1/2)",
        routine_satisfied,
        "p_2/e_1^2 ratio is unconstrained by Newton-Girard",
    ))

    return results


# --------------------------------------------------------------------
# Section 3 — Barrier D2: block-counting weight ambiguity (1,1) vs (1,2)
# --------------------------------------------------------------------

def section3_barrier_d2_weight_ambiguity():
    """Compare the polynomial coefficient '6' in `e_1^2 = 6 e_2`
    with the distinct (1, 1) and (1, 2) block-total log laws.

    The (1, 2) log law lands at kappa=1, but it is not represented by
    `e_1^2 - 3e_2 = 0`; the checks below explicitly prevent that false
    one-to-one identification.
    The cited KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM
    (Section 4 "Residue") flags this exact same ambiguity.
    """
    print("Section 3 — Barrier D2: (1,1) vs (1,2) weight ambiguity in polynomial form")
    results = []

    # 3.1 — Two natural log-laws on Herm_circ(3) give different kappa values
    # Block-total log-law (multiplicity weighting): mu = nu = 1
    #   S_(1,1) = log E_+ + log E_perp, extremum at E_+ = E_perp ⟹ kappa = 2
    # Det log-law (dimensional weighting): mu = 1, nu = 2 (rank P_+ = 1, rank P_perp = 2)
    #   S_(1,2) = log E_+ + 2 log E_perp, extremum at 2 E_+ = E_perp ⟹ kappa = 1

    # Verify (1, 1) extremum at kappa = 2
    a_sym, r_sym = sp.symbols('a r', positive=True)
    Eplus = 3 * a_sym ** 2
    Eperp = 6 * r_sym ** 2
    # Constrain Eplus + Eperp = 1
    constraint = Eplus + Eperp - 1
    # Lagrangian for (1, 1) law with constraint
    # d/da [log E_+ + log E_perp - lam*(E_+ + E_perp - 1)] = 0
    # 1/E_+ * dE_+/da = lam * dE_+/da -> 1/E_+ = lam
    # similarly 1/E_perp = lam, so E_+ = E_perp ⟹ a^2 = 2 r^2 ⟹ |b|^2/a^2 = 1/2 ✓ A1

    # Verify (1, 2) extremum at kappa = 1
    # 1/E_+ = lam, 2/E_perp = lam ⟹ E_perp = 2 E_+ ⟹ 6 r^2 = 6 a^2 ⟹ |b|^2/a^2 = 1 ✗ NOT A1

    # 3.2 — Polynomial form V_(1,1) = (e_1^2 - 6 e_2)^2 versus V_(1,2) = (e_1^2 - 3 e_2)^2
    delta_sym = sp.symbols('delta', real=True)
    lam = [a_sym + 2 * r_sym * sp.cos(delta_sym + 2 * sp.pi * k / 3) for k in range(3)]
    e1_sym = sp.simplify(sum(lam))
    e2_sym = sp.simplify(sum(lam[i] * lam[j] for i in range(3) for j in range(3) if i < j))

    V_11 = sp.simplify(sp.trigsimp(e1_sym ** 2 - 6 * e2_sym))  # (1, 1) -> A1
    V_12 = sp.simplify(sp.trigsimp(e1_sym ** 2 - 3 * e2_sym))  # (1, 2) -> kappa = 1

    # V_(1, 1) at A1
    V11_at_A1 = sp.simplify(V_11.subs(r_sym, a_sym / sp.sqrt(2)))
    results.append(passfail(
        "Polynomial form V_(1,1) = e_1^2 - 6 e_2 vanishes at A1 (multiplicity weights)",
        V11_at_A1 == 0,
        f"V_(1,1) |_A1 = {V11_at_A1}",
    ))

    # V_(1, 2) at A1
    V12_at_A1 = sp.simplify(V_12.subs(r_sym, a_sym / sp.sqrt(2)))
    # At A1, r^2 = a^2/2, e_2 = 3a^2 - 3r^2 = 3a^2 - 3a^2/2 = 3a^2/2
    # e_1^2 - 3 e_2 = 9a^2 - 9a^2/2 = 9a^2/2 ne 0
    results.append(passfail(
        "Polynomial form V_(1,2) = e_1^2 - 3 e_2 does NOT vanish at A1 (dimensional weights)",
        V12_at_A1 != 0,
        f"V_(1,2) |_A1 = {V12_at_A1}",
    ))

    # V_(1, 2) at kappa = 1 (i.e., r = a) gives e_2 = 0 (degenerate eigenvalue manifold);
    # V_(1, 2) does NOT vanish there either, illustrating that polynomial coefficient
    # forms don't directly correspond to (mu, nu) Lagrangian extrema in a 1-1 manner.
    V12_at_kappa1 = sp.simplify(V_12.subs(r_sym, a_sym))
    # V_(1,2) at kappa=1 is e_1^2 - 3*0 = 9 a^2 ≠ 0. The (1,2) Lagrangian extremum is a
    # DIFFERENT object than the polynomial coefficient zero of V_(1,2).
    results.append(passfail(
        "Polynomial form V_(1,2) at kappa=1 does NOT vanish — polynomial zeros and "
        "Lagrangian extrema are different objects",
        V12_at_kappa1 != 0,
        f"V_(1,2) |_kappa=1 = {V12_at_kappa1}; the (1,2) Lagrangian extremum (κ=1) is a "
        f"different polynomial structure than V_(1,1) zero (κ=2 = A1)",
    ))

    print("  [BOUNDARY — not counted] The two block-total weightings select")
    print("       different extrema. The tested polynomial coefficient zeros are")
    print("       not in one-to-one correspondence with those extrema.")

    return results


# --------------------------------------------------------------------
# Section 4 — Barrier D3: requires R1+R2 (Brannen ansatz) plus extra input
# --------------------------------------------------------------------

def section4_barrier_d3_brannen_ansatz_required():
    """Show that the polynomial-coefficient derivation only yields
    p_2/e_1^2 = 2/3 on the Brannen circulant ansatz lambda_k = a + 2|b|cos(...).
    On a generic Hermitian operator (NOT cyclic-equivariant), Newton-Girard
    relations don't single out any specific ratio. Thus Route D requires
    R1+R2 (supplied C_3-equivariance and circulant form) PLUS an additional
    principle to fix |b|/a.
    """
    print("Section 4 — Barrier D3: Newton-Girard alone needs Brannen ansatz + extra input")
    results = []

    # 4.1 — Generic Hermitian 3x3 (not circulant): p_2/e_1^2 takes any value
    rng = np.random.default_rng(seed=137)
    p2_e1sq_values = []
    for _ in range(20):
        # Random Hermitian 3x3
        M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        H = (M + M.conj().T) / 2
        eigs = np.linalg.eigvalsh(H)
        p1, p2, _p3, e1, _e2, _e3 = power_sums_and_elementary(eigs)
        if abs(e1) > 1e-9:
            p2_e1sq_values.append(p2 / e1 ** 2)
    p2_e1sq_min = min(p2_e1sq_values)
    p2_e1sq_max = max(p2_e1sq_values)
    wide_range_generic = (p2_e1sq_max - p2_e1sq_min) > 0.5
    results.append(passfail(
        "Generic Hermitian 3x3 (non-circulant): p_2/e_1^2 ranges widely",
        wide_range_generic,
        f"min = {p2_e1sq_min:.3f}, max = {p2_e1sq_max:.3f} — Newton-Girard gives NO constraint",
    ))

    # 4.2 — Circulant Hermitian on hw=1 STILL has p_2/e_1^2 free in [1/3, infinity)
    a_sym, r_sym = sp.symbols('a r', positive=True)
    Q_lin = (3 * a_sym ** 2 + 6 * r_sym ** 2) / (9 * a_sym ** 2)
    # 1/3 + (2/3) * (r/a)^2  -> takes any value in [1/3, infinity)
    Q_at_b0 = sp.simplify(Q_lin.subs(r_sym, 0))
    Q_at_A1 = sp.simplify(Q_lin.subs(r_sym, a_sym / sp.sqrt(2)))
    Q_at_r2 = sp.simplify(Q_lin.subs(r_sym, 2 * a_sym))
    results.append(passfail(
        "Circulant Hermitian on hw=1 has p_2/e_1^2 = 1/3 + (2/3)(r/a)^2",
        sp.simplify(Q_lin - (sp.Rational(1, 3) + sp.Rational(2, 3) * (r_sym / a_sym) ** 2)) == 0,
        f"min (b=0) = {Q_at_b0}, A1 (r=a/sqrt(2)) = {Q_at_A1}, r=2a = {Q_at_r2}",
    ))

    print("  [BOUNDARY — not counted] The computed free-ratio family shows that")
    print("       the displayed circulant ansatz plus Newton-Girard identities do")
    print("       not by themselves impose the value 2/3.")

    return results


# --------------------------------------------------------------------
# Section 5 — Barrier D4: polynomial-coefficient circularity
# --------------------------------------------------------------------

def section5_barrier_d4_circularity():
    """Show that the polynomial form V(Phi) = [e_1^2 - 6 e_2]^2 is
    ALGEBRAICALLY EQUIVALENT to the Frobenius equipartition condition
    `3 a^2 = 6 |b|^2`. The two are the same statement in different
    coordinates. Substituting Brannen parameters into the polynomial
    gives `81 (a^2 - 2|b|^2)^2`. So "deriving 2/3 from polynomial
    structure" reduces to "deriving a^2 = 2|b|^2 from Frobenius
    structure", which is exactly the open equipartition condition this route
    was supposed to close.
    """
    print("Section 5 — Barrier D4: polynomial-coefficient form rewrites equipartition")
    results = []

    # 5.1 — Symbolic identity: e_1^2 - 6 e_2 = 9 (2 r^2 - a^2)
    # (Note sign: e_1^2 = 9 a^2; 6 e_2 = 18 a^2 - 18 r^2; so e_1^2 - 6 e_2 = -9a^2 + 18 r^2 = 9(2r^2 - a^2))
    a_sym, r_sym, delta_sym = sp.symbols('a r delta', real=True)
    lam = [a_sym + 2 * r_sym * sp.cos(delta_sym + 2 * sp.pi * k / 3) for k in range(3)]
    e1_sym = sp.simplify(sum(lam))
    e2_sym = sp.simplify(sum(lam[i] * lam[j] for i in range(3) for j in range(3) if i < j))
    poly_form = sp.simplify(sp.trigsimp(e1_sym ** 2 - 6 * e2_sym))
    expected = 9 * (2 * r_sym ** 2 - a_sym ** 2)
    # check via expansion
    diff = sp.simplify(sp.expand(poly_form - expected))
    results.append(passfail(
        "Polynomial form e_1^2 - 6 e_2 = 9 (2 r^2 - a^2) on Brannen ansatz",
        diff == 0,
        "Polynomial coefficient '6' is exactly the Frobenius factor in disguise (vanishes at a^2 = 2r^2 = A1)",
    ))

    # 5.2 — V(Phi) = [e_1^2 - 6 e_2]^2 = 81 (a^2 - 2|b|^2)^2
    V_form = sp.simplify(sp.expand((e1_sym ** 2 - 6 * e2_sym) ** 2))
    V_expected = 81 * (a_sym ** 2 - 2 * r_sym ** 2) ** 2
    diff_V = sp.simplify(sp.expand(V_form - V_expected))
    results.append(passfail(
        "V(Phi) = [e_1^2 - 6 e_2]^2 = 81 (a^2 - 2|b|^2)^2 (Frobenius equipartition squared)",
        diff_V == 0,
        "Vanishing of V is exactly the Frobenius condition ‖aI‖_F^2 = ‖bC + bbarC^2‖_F^2",
    ))

    print("  [BOUNDARY — not counted] These two computed identities show that")
    print("       imposing the displayed polynomial zero is equivalent to imposing")
    print("       a^2 = 2|b|^2; the rewrite itself supplies no selection premise.")

    return results


# --------------------------------------------------------------------
# Section 6 — Tested symmetric-polynomial extremizations do not pick A1
# --------------------------------------------------------------------

def section6_barrier_d5_no_extremization():
    """Test a named finite family of symmetric-polynomial functionals.

    Candidate symmetric-polynomial-only functionals tested:
      - Discriminant of the characteristic polynomial
      - Tschirnhaus depressed-cubic coefficients
      - Vandermonde product squared
      - Various rational ratios e_k^a / e_l^b

    None of these tested candidates has a critical-point equation that
    uniquely lands at A1.  This is not an exhaustive no-go over all
    symmetric-polynomial functionals.
    """
    print("Section 6 — Tested symmetric-polynomial extremizations do not pick equipartition")
    results = []

    a_sym, r_sym, delta_sym = sp.symbols('a r delta', real=True, positive=True)
    lam = [a_sym + 2 * r_sym * sp.cos(delta_sym + 2 * sp.pi * k / 3) for k in range(3)]
    p1_sym = sp.simplify(sum(lam))
    p2_sym = sp.simplify(sum(l ** 2 for l in lam))
    p3_sym = sp.simplify(sum(l ** 3 for l in lam))
    e1_sym = p1_sym
    e2_sym = sp.simplify(sum(lam[i] * lam[j] for i in range(3) for j in range(3) if i < j))
    e3_sym = sp.simplify(lam[0] * lam[1] * lam[2])

    # 6.1 — Discriminant of characteristic polynomial
    # Disc(lambda^3 - e_1 lambda^2 + e_2 lambda - e_3) = e_1^2 e_2^2 - 4 e_2^3 - 4 e_1^3 e_3 + 18 e_1 e_2 e_3 - 27 e_3^2
    disc = e1_sym ** 2 * e2_sym ** 2 - 4 * e2_sym ** 3 - 4 * e1_sym ** 3 * e3_sym + 18 * e1_sym * e2_sym * e3_sym - 27 * e3_sym ** 2
    disc_at_A1 = sp.simplify(sp.trigsimp(disc.subs(r_sym, a_sym / sp.sqrt(2))))
    # Discriminant nonzero at generic A1 means eigenvalues are non-degenerate
    # Check by using a specific delta
    disc_at_A1_specific = sp.simplify(disc_at_A1.subs(delta_sym, sp.Rational(2, 9)))
    results.append(passfail(
        "Discriminant is nonzero at A1 on the chosen nondegenerate delta=2/9 slice",
        sp.simplify(disc_at_A1_specific) != 0,
        f"Disc |_(A1, delta=2/9) = {disc_at_A1_specific}",
    ))

    # 6.2 — Discriminant has its own extremum, NOT at A1
    # ∂/∂r [Disc] = 0 at A1? Check numerically
    disc_func = sp.lambdify((a_sym, r_sym, delta_sym), disc, 'numpy')
    d_disc_dr = sp.diff(disc, r_sym)
    d_disc_dr_at_A1 = sp.simplify(sp.trigsimp(d_disc_dr.subs(r_sym, a_sym / sp.sqrt(2))))
    d_disc_at_A1_specific = sp.simplify(d_disc_dr_at_A1.subs([(a_sym, 1), (delta_sym, sp.Rational(2, 9))]))
    results.append(passfail(
        "d(Disc)/dr is nonzero at A1 on the chosen delta=2/9 slice",
        sp.simplify(d_disc_at_A1_specific) != 0,
        f"d(Disc)/dr |_(A1) ≈ {float(d_disc_at_A1_specific):.4f}; A1 is not a critical point",
    ))

    # 6.3 — Vandermonde product squared
    # V^2 = prod (lambda_i - lambda_j)^2 = Disc ✓ (same as discriminant)
    # So no new content here

    # 6.4 — Tschirnhaus depressed-cubic coefficients
    # x = lambda - p_1/3 (depressing translation)
    # depressed cubic: x^3 + p x + q = 0 with p = e_2 - e_1^2/3, q = ...
    p_depressed = sp.simplify(sp.trigsimp(e2_sym - e1_sym ** 2 / 3))
    p_at_A1 = sp.simplify(sp.trigsimp(p_depressed.subs(r_sym, a_sym / sp.sqrt(2))))
    # At A1, p_depressed = e_2 - e_1^2/3 = 3a^2 - 3r^2 - 9a^2/3 = -3r^2 = -3 a^2/2
    results.append(passfail(
        "Tschirnhaus 'p' = e_2 - e_1^2/3 takes value -3 r^2 at A1 (no special vanishing)",
        sp.simplify(p_at_A1 - (-sp.Rational(3, 2) * a_sym ** 2)) == 0,
        f"p_depressed |_A1 = {p_at_A1} (free parameter)",
    ))

    # 6.5 — Various ratios e_k^a / e_l^b — symbolic check that none have
    # critical points at A1
    # e_1^2 / e_2 = 3 / (1 - r^2/a^2) → infinity as r/a → 1
    e1sq_over_e2 = sp.simplify(sp.trigsimp(e1_sym ** 2 / e2_sym))
    e1sq_over_e2_at_A1 = sp.simplify(sp.trigsimp(e1sq_over_e2.subs(r_sym, a_sym / sp.sqrt(2))))
    # = 9 a^2 / (3 a^2 - 3 a^2/2) = 9 a^2 / (3a^2/2) = 6 ✓
    results.append(passfail(
        "e_1^2 / e_2 = 6 at A1 — but this is by construction (definition of A1)",
        sp.simplify(e1sq_over_e2_at_A1 - 6) == 0,
        f"e_1^2/e_2 |_A1 = {e1sq_over_e2_at_A1}; the value 6 is the Frobenius factor",
    ))

    # 6.6 — d/dr [e_1^2 / e_2] is NOT zero at A1 — so e_1^2/e_2 is not extremized there
    d_ratio_dr = sp.diff(e1sq_over_e2, r_sym)
    d_ratio_at_A1 = sp.simplify(sp.trigsimp(d_ratio_dr.subs(r_sym, a_sym / sp.sqrt(2))))
    d_ratio_specific = sp.simplify(d_ratio_at_A1.subs([(a_sym, 1)]))
    results.append(passfail(
        "d/dr [e_1^2 / e_2] is NOT zero at A1 — e_1^2/e_2 is not extremized at A1",
        sp.simplify(d_ratio_specific) != 0,
        f"d/dr [e_1^2/e_2] |_A1 ≈ {float(d_ratio_specific):.4f}",
    ))

    print("  [SCOPE — not counted] The named candidates tested above do not")
    print("       extremize at A1. No exhaustive statement about every possible")
    print("       symmetric-polynomial functional is claimed.")

    return results


# --------------------------------------------------------------------
# Section 7 — Comparison with Routes E and F (trap-profile contrast)
# --------------------------------------------------------------------

def section7_comparison_routes_e_f():
    """Compare Route D's trap profile to Routes E (Kostant) and F (Casimir).
    The polynomial-coefficient profile is materially DIFFERENT from
    norm-convention profile, but falls to a structurally analogous trap.
    """
    print("Section 7 — Comparison with Routes E (Kostant) and F (Casimir-difference)")
    results = []

    # 7.1 — The sibling-route tables are imported context from their source
    # notes, not recomputed by this runner and therefore not counted here.
    print("  [CONTEXT — not counted] Route E/F normalization tables belong to")
    print("       their sibling sources; this runner does not certify those values.")

    # 7.2 — Route D's trap: weight-class (1, 1) vs (1, 2)
    # multiplicity weighting: (1, 1) -> e_1^2 = 6 e_2 -> kappa = 2 (A1)
    # dimensional weighting: (1, 2) -> e_1^2 = 3 e_2 -> kappa = 1 (NOT A1)
    weight_choices = [(1, 1), (1, 2)]
    # Coefficient in V_(mu, nu) = e_1^2 - C(mu, nu) e_2:
    # Lagrangian: max{mu log E_+ + nu log E_perp s.t. E_+ + E_perp = const}
    # ⟹ E_perp = (nu/mu) E_+ ⟹ 6 r^2 = (nu/mu) 3 a^2 ⟹ kappa = a^2/r^2 = nu/(2 mu)... wait
    # Let me recompute: max gives mu/E_+ = nu/E_perp ⟹ E_perp/E_+ = nu/mu
    # So 6 r^2 / (3 a^2) = nu/mu ⟹ 2 r^2 / a^2 = nu/mu ⟹ kappa = a^2/r^2 = 2 mu/nu
    # For (mu, nu) = (1, 1): kappa = 2 ✓
    # For (mu, nu) = (1, 2): kappa = 1 ✓
    # Coefficient C(mu, nu) such that V = e_1^2 - C e_2 vanishes at the extremum:
    # At extremum: r^2/a^2 = mu/nu, so e_2 = 3a^2 - 3r^2 = 3a^2(1 - mu/nu) = 3a^2(nu-mu)/nu
    # e_1^2 = 9a^2; want 9a^2 = C * 3a^2 (nu-mu)/nu ⟹ C = 3 nu / (nu - mu)
    # For (1, 1): nu - mu = 0 ⟹ C → infinity (degenerate, b = 0)
    # Wait — that's wrong. Let me redo.
    #
    # Actually for (mu, nu) = (1, 1) with E_+ = E_perp ⟹ 3a^2 = 6r^2 ⟹ r^2 = a^2/2
    # Then e_2 = 3a^2 - 3r^2 = 3a^2 - 3a^2/2 = 3a^2/2
    # e_1^2 = 9a^2; e_1^2 / e_2 = 9a^2 / (3a^2/2) = 6 ✓
    # So C(1,1) = 6, V_(1,1) = e_1^2 - 6 e_2 ✓ A1
    #
    # For (mu, nu) = (1, 2): E_perp = 2 E_+ ⟹ 6r^2 = 6a^2 ⟹ r^2 = a^2
    # Then e_2 = 3a^2 - 3a^2 = 0 — DEGENERATE!
    # Actually e_1^2 / e_2 → infinity in this case. So the (1, 2) extremum
    # is NOT representable as a single polynomial coefficient C.
    # Let me instead use: V_(mu, nu) ∝ (mu E_+ - nu * something) at the extremum
    # The extremum equation is mu E_perp = nu E_+, i.e., 6 mu r^2 = 3 nu a^2
    # ⟹ 2 mu r^2 = nu a^2 ⟹ a^2 - (2 mu / nu) r^2 = 0
    # In polynomial form: e_1^2 - C e_2 vanishes when r^2 / a^2 = mu/nu
    # e_2 = 3 a^2 (1 - mu/nu) — Want 9 a^2 = C * 3 a^2 (1 - mu/nu)
    # ⟹ C = 3/(1 - mu/nu) = 3 nu / (nu - mu)
    # For (1, 1): C = 3 * 1 / 0 — division by zero
    # For (1, 2): C = 3 * 2 / 1 = 6
    # Hmm, that gives the OPPOSITE assignment. Let me re-examine.
    #
    # Actually wait — I need to be careful about which direction.
    # MRU is "equal block totals" E_+ = E_perp. That's (mu=1, nu=1) extremum.
    # At E_+ = E_perp, 3a^2 = 6r^2, so r^2/a^2 = 1/2 (A1).
    # e_2 = 3a^2 - 3r^2 = 3a^2 - 3*a^2/2 = 3a^2/2
    # e_1^2 / e_2 = 9a^2 / (3a^2/2) = 6 ✓
    #
    # The (1, 2) law (det law) gives extremum at E_perp = 2 E_+, i.e., 6r^2 = 6a^2, r = a (κ=1).
    # e_2 = 3a^2 - 3a^2 = 0 — so e_1^2/e_2 → infinity at (1,2)-extremum. Polynomial form
    # V_(1,2) = e_1^2 - 3 e_2 vanishes when 9a^2 = 3(3a^2 - 3r^2) = 9a^2 - 9r^2 ⟹ r^2 = 0, NOT r=a!
    # So V_(1, 2) = e_1^2 - 3 e_2 has its ZERO at b=0, NOT at the det-law extremum!
    # The det-law extremum at r=a gives e_2 = 0 (degenerate manifold), not a polynomial zero.
    # The point: polynomial "C" coefficient and (mu, nu) weight don't have a clean linear relation.

    # The key takeaway: BOTH choices V_(1,1) = e_1^2 - 6 e_2 and V_(1,2)-related
    # forms exist as natural polynomial forms; the framework does not select among them.

    print("  [BOUNDARY — not counted] The (1,1) and (1,2) log laws select")
    print("       different block-energy extrema; no polynomial-zero identification")
    print("       for the (1,2) extremum is asserted.")

    # 7.3 — Materially different trap profile but structurally analogous
    # Route E/F trap: norm-convention dependence (continuous family of conventions)
    # Route D trap: weight-class choice (discrete family — multiplicity vs dimensional)
    print("  [COMPARISON — not counted] E/F vary normalization conventions;")
    print("       the tested block-total laws vary discrete weights. This is a")
    print("       descriptive comparison, not theorem evidence.")

    return results


# --------------------------------------------------------------------
# Section 8 — Falsifiability anchor (PDG values, anchor-only)
# --------------------------------------------------------------------

def section8_falsifiability_anchor():
    """Anchor-only: confirm that PDG charged-lepton masses are consistent
    with A1 (Brannen circulant fits at 0.1% precision). This is
    FALSIFIABILITY anchor, NOT derivation input.

    Per `STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`,
    PDG values are forbidden as load-bearing in any positive theorem.
    They appear ONLY as anchor for falsification.
    """
    print("Section 8 — Falsifiability anchor (PDG values are NOT derivation input)")
    results = []

    # PDG charged-lepton masses (anchor only)
    m_e = 0.5109989
    m_mu = 105.6583745
    m_tau = 1776.86

    sqrt_me = math.sqrt(m_e)
    sqrt_mmu = math.sqrt(m_mu)
    sqrt_mtau = math.sqrt(m_tau)

    # Compute Koide Q from anchors
    sum_m = m_e + m_mu + m_tau
    sum_sqrt_m = sqrt_me + sqrt_mmu + sqrt_mtau
    Q_anchor = sum_m / (sum_sqrt_m ** 2)
    Q_target = 2.0 / 3.0
    fit_ok = abs(Q_anchor - Q_target) < 1e-3

    # In linear-eigenvalue convention, Q_lin = (Σ sqrt m)^2 / (3 Σ m) at A1 = 1/2
    # That's just (sum_sqrt_m)^2 / (3 sum_m) = 1/(3 * Q_anchor)
    Q_lin_anchor = (sum_sqrt_m ** 2) / (3 * sum_m)
    Q_lin_target = 0.5
    fit_lin_ok = abs(Q_lin_anchor - Q_lin_target) < 1e-3

    print(f"  [ANCHOR — not counted] Q(PDG) = {Q_anchor:.6f}; "
          f"within 1e-3 of 2/3: {fit_ok}")
    print(f"  [ANCHOR — not counted] Q_lin(PDG) = {Q_lin_anchor:.6f}; "
          f"within 1e-3 of 1/2: {fit_lin_ok}")

    print("       NOTE: PDG match (Q ~ 2/3) confirms A1 is OBSERVATIONALLY consistent")
    print("       but does NOT derive equipartition from the supplied premises. Premise surface unchanged.")
    print()

    return results


# --------------------------------------------------------------------
# Section 9 — Bounded-obstruction theorem statement (verification)
# --------------------------------------------------------------------

def section9_obstruction_theorem():
    """State the narrow conclusion supported by Sections 1-7."""
    print("Section 9 — Narrow obstruction synthesis")
    results = []
    print("       VERDICT: Newton-Girard identities and the named candidate")
    print("       functionals tested here do not select A1. The polynomial coefficient")
    print("       '6' (in V = e_1^2 - 6 e_2) is the Frobenius equipartition condition")
    print("       in different coordinates, NOT a derivation-from-axioms.")
    print()
    print("       The Newton-Girard formulation has a MATERIALLY DIFFERENT trap")
    print("       profile from the tested Routes E/F examples (discrete block weights")
    print("       versus normalization choices). No exhaustive cited-source no-go")
    print("       is inferred from that comparison.")
    print()
    print("       AC_φλ residual (from substep 4) is unaffected. The equipartition condition")
    print("       count remains UNCHANGED.")
    print()

    return results


# --------------------------------------------------------------------
# Main runner
# --------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Newton-Girard Polynomial Candidate (historical Koide Route D) — Bounded Obstruction")
    print("Source note:")
    print("  docs/KOIDE_A1_ROUTE_D_NEWTON_GIRARD_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routed.md")
    print("=" * 70)

    all_results = []
    all_results += section1_newton_girard_identity()
    all_results += section2_barrier_d1_identity_not_constraint()
    all_results += section3_barrier_d2_weight_ambiguity()
    all_results += section4_barrier_d3_brannen_ansatz_required()
    all_results += section5_barrier_d4_circularity()
    all_results += section6_barrier_d5_no_extremization()
    all_results += section7_comparison_routes_e_f()
    all_results += section8_falsifiability_anchor()
    all_results += section9_obstruction_theorem()

    n_total = len(all_results)
    n_pass = sum(all_results)
    n_fail = n_total - n_pass

    print()
    print("=" * 70)
    print(f"COMPUTED   : PASS = {n_pass}, FAIL = {n_fail}")
    print(f"BOUNDED    : PASS = 0, FAIL = 0")
    print(f"TOTAL      : PASS = {n_pass}, FAIL = {n_fail}")
    print("=== TOTAL: PASS=" + str(n_pass) + ", FAIL=" + str(n_fail) + " ===")
    print("=" * 70)
    print()
    print("Bounded-obstruction verdict:")
    if n_fail == 0:
        print("  Newton-Girard identities and the named candidate functionals")
        print("  tested here do not select |b|^2/a^2 = 1/2. The exact identities")
        print("  expose rewrites of the target condition, not a selection rule.")
        print()
        print("  The imported sibling-route comparison is descriptive and")
        print("  uncounted; this runner certifies no universal trap-profile claim.")
        print()
        print("  Premise and registry surfaces UNCHANGED. No new axiom proposed.")
        print()
        print("  Falsifiability anchor: PDG charged-lepton masses fit A1 at")
        print("  0.1% precision (consistent but NOT derivation).")
    else:
        print("  Verification has FAIL items — see runner output above.")

    if n_fail != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
