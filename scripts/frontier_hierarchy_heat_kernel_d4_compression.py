#!/usr/bin/env python3
"""Finite supplied-spectrum determinant/zeta identities and stipulated readout.

The spectrum is an input, not a derived physical lattice operator. Its finite
count saturates. No Weyl asymptotic, continuum limit, free-energy identification,
or physical mass readout follows from these checks. The quarter-power statistic
uses |det D|^(1/(16 L_t)); det(D†D) requires twice that denominator.
The ordinary geometric mean singular value has a square-root endpoint ratio.
Stefan inversion is a separate supplied-continuum identity only.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

AUDIT_INPUT_PATHS = ['docs/HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md', 'docs/AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md']

from pathlib import Path
from fractions import Fraction
import math
import sys

try:
    import numpy as np
except ImportError:
    print("FAIL: numpy required")
    sys.exit(1)

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy required")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md"
)
PARENT_NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md"
)
SB_NOTE_PATH = (
    ROOT
    / "docs"
    / "AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md"
)


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = ""):
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------------------
# Section 1: Note structure and scope
# ---------------------------------------------------------------------------


def section_1_note_structure():
    print("\n[Section 1] Note structure and scope discipline")
    print("-" * 70)

    if not NOTE_PATH.exists():
        check("note exists", False, str(NOTE_PATH))
        return
    text = NOTE_PATH.read_text()

    for anchor in ["bounded_theorem", "Supplied spectrum", "Finite zeta identity",
                   "R_D = |det D_4|", "R_Q = det Q_4", "C_4/C_2 = R_D^(1/64)",
                   "G_4/G_2 = R_D^(1/32)", "T^3", "mass dimension two",
                   "finite counting function saturates", "physical readout remains open"]:
        check(f"documentary scope anchor: {anchor}", anchor in text)
    print("  INFO: text checks locate the stated scope; they do not prove it.")


# ---------------------------------------------------------------------------
# Section 2: Finite zeta/log-determinant identity
# ---------------------------------------------------------------------------


def staggered_eigenvalues_squared(L_t: int, u_0: float):
    """Return the supplied dimensionless eigenvalues of Q/mu^2 for u_0=u/mu."""
    eigs = []
    for n in range(L_t):
        omega = (2 * n + 1) * math.pi / L_t
        lam_sq = u_0**2 * (3 + math.sin(omega) ** 2)  # eigenvalue of D†D
        # Supplied multiplicity: eight eigenvalues per omega.
        for _ in range(8):
            eigs.append(lam_sq)
    return np.array(eigs)


def section_2_zeta_log_det():
    print("\n[Section 2] Finite zeta/log-determinant identity")
    print("-" * 70)

    u_0 = 0.8776
    for L_t in [2, 4]:
        eigs = staggered_eigenvalues_squared(L_t, u_0)
        log_det_direct = float(np.sum(np.log(eigs)))

        # Zeta-regularized: ζ(s) = sum lam^(-s); -ζ'(0) = sum log lam
        # (For positive finite spectrum, this is exact identity.)
        # Numerically: -d/ds [sum lam^(-s)]_{s=0} = sum log(lam)·lam^0 = sum log lam
        log_det_zeta = float(np.sum(np.log(eigs)))  # by definition equals direct

        check(
            f"same-expression numerical consistency for finite zeta/log-det, L_t={L_t}",
            abs(log_det_direct - log_det_zeta) < 1e-10,
            f"log|det| direct = {log_det_direct:.6f}; -ζ'(0) = {log_det_zeta:.6f}",
        )

    # Cross-check parent narrow source-note closed form
    # |det(D, L_t)|_{m=0} = u_0^(8 L_t) * prod_omega (3 + sin^2 omega)^4
    # |det(D†D, L_t)| = |det(D)|^2
    for L_t in [2, 4]:
        u_0 = sp.Symbol('u', positive=True)
        prod = sp.Integer(1)
        for n in range(L_t):
            omega = sp.Rational(2 * n + 1) * sp.pi / L_t
            prod *= (3 + sp.sin(omega) ** 2) ** 4
        det_D = u_0 ** (8 * L_t) * prod
        det_DD = sp.simplify(det_D ** 2)
        # Reference values:
        if L_t == 2:
            expected = u_0 ** 32 * sp.Rational(4, 1) ** 16  # (4 u_0^2)^8 squared
        else:  # L_t = 4
            expected = u_0 ** 64 * sp.Rational(7, 2) ** 32  # ((7/2) u_0^2)^16 squared
        check(
            f"supplied-spectrum det(Q/mu²), L_t={L_t}, matches exact product",
            sp.simplify(det_DD - expected) == 0,
            f"symbolic equality verified",
        )


# ---------------------------------------------------------------------------
# Section 3: Finite positive spectrum and saturation
# ---------------------------------------------------------------------------


def section_3_weyl_asymptotic():
    print("\n[Section 3] Finite positive spectrum and saturation")
    print("-" * 70)

    # Positivity and cardinality only; no asymptotic inference.
    u_0 = 0.8776
    for L_t in [2, 4]:
        eigs = staggered_eigenvalues_squared(L_t, u_0)
        eigs_sorted = np.sort(eigs)
        n_total = len(eigs_sorted)
        max_lam = eigs_sorted[-1]

        # Counting function: N(lam_max) = n_total
        V_4 = 8 * L_t  # L_s^3 * L_t = 2^3 * L_t
        weyl_form_pos_def = all(eigs_sorted > 0)
        check(
            f"L_t={L_t}: supplied Q/mu² spectrum is positive",
            weyl_form_pos_def,
            f"min eigenvalue = {eigs_sorted[0]:.6f}, max = {eigs_sorted[-1]:.6f}",
        )

        # Verify counting function increases monotonically in lam (trivially true)
        # and that N(lam_max) = n_total
        check(
            f"L_t={L_t}: counting function reaches n_total = {n_total} at lam_max",
            n_total == 8 * L_t,
            f"V_4 = {V_4}, modes per lambda = 8, total = {n_total}",
        )

        above = max_lam + 1.0
        check(f"L_t={L_t}: finite count saturates above maximum",
              int(np.count_nonzero(eigs <= above)) == n_total
              and int(np.count_nonzero(eigs <= 2*above)) == n_total)
    print("  INFO: for each fixed finite spectrum N(lambda) is constant above its maximum.")
    print("  INFO: these checks establish no N(lambda) ~ C lambda² asymptotic.")


# ---------------------------------------------------------------------------
# Section 4: Dimensional consistency (1/D power, Stefan-Boltzmann analog)
# ---------------------------------------------------------------------------


def section_4_dimensional_consistency():
    print("\n[Section 4] Dimensional consistency and (1/D) power")
    print("-" * 70)

    # Rational exponent comparison only; no determinant density identification.

    D = 4
    expected_power = sp.Rational(1, D)
    check(
        "rational identity: 1/4 at the supplied integer D=4",
        expected_power == sp.Rational(1, 4),
        f"1/D = {expected_power}",
    )

    # Identity 1/D = 4/2^D at D=4
    for D_test in [1, 2, 3, 4, 5, 6]:
        N_taste_test = 2 ** D_test
        algebraic = sp.Rational(4, N_taste_test)
        target = sp.Rational(1, D_test)
        equal = (algebraic == target)
        if D_test == 4:
            check(
                f"D={D_test}: 4/2^D = 4/{N_taste_test} = {algebraic} EQUALS 1/D = {target}",
                equal,
                f"identity 1/D = 4/2^D HOLDS at D=4",
            )
        elif D_test in [2, 3, 5]:
            check(
                f"D={D_test}: 4/2^D = {algebraic} ≠ 1/D = {target} (tested integer comparison)",
                not equal,
                f"as expected: identity FAILS at D={D_test}, no uniqueness or physical inference",
            )
        # D=1: 4/2 = 2, 1/1 = 1, so the identity also fails.

    # Stefan-Boltzmann lineage: u(T) = (pi^2/15) T^4 ⟹ T ∝ u^(1/4)
    # This supplied continuum identity does not identify a determinant with density.
    pi2_over_15 = (sp.pi ** 2) / 15
    T = sp.Symbol('T', positive=True)
    u = sp.Symbol('u', positive=True)
    u_of_T = pi2_over_15 * T ** 4
    T_of_u = (15 * u / sp.pi ** 2) ** sp.Rational(1, 4)
    # Verify: u(T(u)) = u
    u_round_trip = sp.simplify(u_of_T.subs(T, T_of_u))
    check(
        "Stefan-Boltzmann inversion T ~ u^(1/4) is consistent (round-trip)",
        sp.simplify(u_round_trip - u) == 0,
        f"u(T(u)) = u verified symbolically",
    )

    # Cross-check numeric: σ_SB constant from the Stefan-Boltzmann source note
    # σ_SB = (π²/60) (k_B = 1) = π²/60 in natural units
    sigma_SB_natural = float(sp.pi ** 2 / 60)
    check(
        "same-formula consistency of supplied continuum σ_SB = π²/60",
        abs(sigma_SB_natural - math.pi ** 2 / 60) < 1e-12,
        f"σ_SB = {sigma_SB_natural:.10f}",
    )


# ---------------------------------------------------------------------------
# Section 5: Cross-endpoint ratio (7/8)^(1/4) at exact rational
# ---------------------------------------------------------------------------


def section_5_cross_endpoint_ratio():
    print("\n[Section 5] Cross-endpoint ratio (7/8)^(1/4) — exact arithmetic")
    print("-" * 70)

    # Supplied-spectrum product: R_D=|det(D_4)|/|det(D_2)|²=(7/8)^16.
    det_4_over_det_2_sq = Fraction(7, 8) ** 16
    direct = Fraction(7, 2) ** 16 / Fraction(4, 1) ** 16
    check(
        "(7/2)^16 / 4^16 = (7/8)^16 (supplied spectrum)",
        direct == det_4_over_det_2_sq,
        f"= {det_4_over_det_2_sq}",
    )

    # Stipulated statistic denominator 16 L_t; the actual mode count is 8 L_t.
    # Cross-endpoint: ((7/8)^16)^(1/64) = (7/8)^(16/64) = (7/8)^(1/4)
    N_taste = 16
    L_t_target = 4
    inv_power = Fraction(1, N_taste * L_t_target)
    final_exponent = 16 * inv_power
    check(
        f"stipulated statistic power 1/(16·L_t) = 1/(16·4) = {inv_power}",
        inv_power == Fraction(1, 64),
        f"= {inv_power}",
    )
    check(
        f"final exponent in cross-endpoint ratio: 16 · (1/64) = 1/4",
        final_exponent == Fraction(1, 4),
        f"= {final_exponent}",
    )

    # Numerical match to (7/8)^(1/4)
    target_numeric = (7 / 8) ** (1 / 4)
    check(
        "numerical (7/8)^(1/4) ≈ 0.96716821",
        abs(target_numeric - 0.96716821013383) < 1e-10,
        f"= {target_numeric:.14f}",
    )

    # Direct numerical staggered Dirac determinant cross-check
    print("\n  Direct numerical staggered Dirac cross-check:")
    u_0 = 0.8776
    for L_t in [2, 4]:
        eigs = staggered_eigenvalues_squared(L_t, u_0)
        # |det(D†D)| = product of eigenvalues
        log_det_DD = float(np.sum(np.log(eigs)))
        # |det(D)|^2 = |det(D†D)|, so log|det(D)| = (1/2) log|det(D†D)|
        log_det_D = log_det_DD / 2
        det_D = math.exp(log_det_D)
        print(f"    L_t={L_t}: |det(D)| = {det_D:.6e}, log|det(D)| = {log_det_D:.6f}")

    # Cross-endpoint ratio numerical
    eigs_2 = staggered_eigenvalues_squared(2, u_0)
    eigs_4 = staggered_eigenvalues_squared(4, u_0)
    log_det_2 = float(np.sum(np.log(eigs_2))) / 2
    log_det_4 = float(np.sum(np.log(eigs_4))) / 2
    log_ratio = log_det_4 - 2 * log_det_2
    target_log = 16 * math.log(7 / 8)
    check(
        "log(|det(L_t=4)| / |det(L_t=2)|²) = 16 log(7/8)",
        abs(log_ratio - target_log) < 1e-9,
        f"diff = {abs(log_ratio - target_log):.3e}",
    )

    # Apply the supplied statistic power 1/64, not a geometric mean mass readout.
    v_ratio_numeric = math.exp(log_ratio / 64)
    check(
        "dimensionless C_4/C_2 = R_D^(1/64) = (7/8)^(1/4)",
        abs(v_ratio_numeric - target_numeric) < 1e-9,
        f"diff = {abs(v_ratio_numeric - target_numeric):.3e}",
    )


# ---------------------------------------------------------------------------
# Section 6: D=4 specificity
# ---------------------------------------------------------------------------


def section_6_d4_specificity():
    print("\n[Section 6] Finite rational exponent comparisons")
    print("-" * 70)

    # These integer comparisons have no continuum or lattice-dimension implication.
    # Here we just verify the algebraic identity for representative D values
    print("  Algebraic identity 1/D = 4/2^D = 4/N_taste:")
    print("  D | 2^D | 4/2^D     | 1/D       | match")
    print("  --|-----|-----------|-----------|------")
    for D in [1, 2, 3, 4, 5, 6]:
        n_taste = 2 ** D
        ratio = Fraction(4, n_taste)
        target = Fraction(1, D)
        match = (ratio == target)
        print(f"  {D} | {n_taste:3d} | {str(ratio):9s} | {str(target):9s} | {'✓' if match else '✗'}")

    check(
        "1/4 = 4/2^4 (other table rows are displayed separately)",
        Fraction(4, 2**4) == Fraction(1, 4),
        "only the displayed rational identity is checked here",
    )


# ---------------------------------------------------------------------------
# Section 7: Stefan-Boltzmann source lineage
# ---------------------------------------------------------------------------


def section_7_stefan_boltzmann_lineage():
    print("\n[Section 7] Stefan-Boltzmann source lineage")
    print("-" * 70)

    if SB_NOTE_PATH.exists():
        sb_text = SB_NOTE_PATH.read_text()
        check(
            "Stefan-Boltzmann source note exists",
            True,
            str(SB_NOTE_PATH.name),
        )
        check(
            "SB source note includes T^4 dependence",
            "T⁴" in sb_text or "T^4" in sb_text,
        )
        check(
            "SB source note includes (π²/15) prefactor",
            "π² / 15" in sb_text or "π²/15" in sb_text or "(π² / 15)" in sb_text or "(pi²/15)" in sb_text,
        )
    else:
        check("Stefan-Boltzmann note exists", False, "missing")

    # Numerical: u(T) = (π²/15) T^4 in natural units
    T_test = 1.0
    u_T = (math.pi ** 2 / 15) * T_test ** 4
    T_back = (15 * u_T / math.pi ** 2) ** (1 / 4)
    check(
        "Stefan-Boltzmann round-trip T ↔ u^(1/4) at T=1",
        abs(T_back - T_test) < 1e-12,
        f"T_back = {T_back:.12f}",
    )

    print("  INFO: equal quarter exponents do not identify the determinant statistic with")
    print("  energy density, temperature, an EWSB scale, or any physical mass.")


# ---------------------------------------------------------------------------
# Section 8: Bounded regime caveat documentation
# ---------------------------------------------------------------------------


def section_8_bounded_caveats():
    print("\n[Section 8] Bounded regime caveats (audit transparency)")
    print("-" * 70)

    text = NOTE_PATH.read_text() if NOTE_PATH.exists() else ""
    for phrase in ["no continuum limit", "not a physical mass", "T^3", "mass dimension two"]:
        check(f"documented withdrawal: {phrase}", phrase in text)
    print("  INFO: these are documentary boundary checks, not scientific certificates.")


def section_9_normalization_and_failed_route():
    print("\n[Section 9] Exact normalization and rejected thermal scaling")
    r_d = sp.Rational(7, 8)**16
    r_q = sp.Rational(7, 8)**32
    check("R_Q = R_D²", r_q == r_d**2)
    check("C ratio uses R_D^(1/64) = R_Q^(1/128)",
          sp.simplify(r_d**sp.Rational(1,64)-r_q**sp.Rational(1,128)) == 0)
    check("geometric mean singular-value ratio is sqrt(7/8)",
          sp.simplify(r_d**sp.Rational(1,32)-sp.sqrt(sp.Rational(7,8))) == 0)
    t, x = sp.symbols('t x', positive=True)
    lam = sp.symbols('lam', positive=True)
    # Formal substitution in the old expression includes d lambda = t dx.
    original_integrand = -t*lam*sp.log(1+sp.exp(-lam/t))/(16*sp.pi**2)
    transformed = sp.simplify(original_integrand.subs(lam,t*x)*t)
    check("old integral substitution has T³ prefactor, not T⁴",
          sp.simplify(transformed + t**3*x*sp.log(1+sp.exp(-x))/(16*sp.pi**2)) == 0)
    print("  INFO: lambda of D†D has mass dimension two, so lambda/T is not")
    print("  a dimensionless thermal energy ratio. The old physical interpretation fails.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("=" * 70)
    print("Finite supplied determinant and stipulated statistic — verification runner")
    print("=" * 70)

    section_1_note_structure()
    section_2_zeta_log_det()
    section_3_weyl_asymptotic()
    section_4_dimensional_consistency()
    section_5_cross_endpoint_ratio()
    section_6_d4_specificity()
    section_7_stefan_boltzmann_lineage()
    section_8_bounded_caveats()
    section_9_normalization_and_failed_route()

    print("\n" + "=" * 70)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 70)
    if FAIL == 0:
        print("Finite supplied-spectrum checks passed; no physical determinant readout is established.")
        print("The old Weyl/thermal derivation is withdrawn; continuum Stefan inversion is separate.")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
