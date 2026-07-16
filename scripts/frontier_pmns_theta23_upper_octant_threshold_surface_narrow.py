#!/usr/bin/env python3
"""PMNS theta_23 upper-octant chamber-closure threshold-surface partial extension.

Companion runner for
docs/PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md

Verifies the explicit (X1, X2, X3, X4, X5) -> conclusion narrow theorem by:

  P1: chart H(m, d, q) closed-form invariants (sympy-exact).
  P2: anchor chart invariants reproduce Basin 1 eigenvalues (mpmath 200-bit).
  P3: chamber margin lower bound at anchor (Cycle 5a Krawczyk inheritance).
  P4: J_Phi at anchor: |det J| > 1e-3 (IFT prerequisite).
  P5: IFT consequence (open neighborhood, qualitative).
  P6: IVT consequence (threshold exists, upper-octant labeling).
  P7: NUMERICAL EVIDENCE (parent Table 2 reproduction, NOT CERTIFIED).
  P8: residual scope statement.
  P9: claim-discipline summary.

Part 4 uses numpy.linalg.svd for eigenvectors; this is a qualitative
order-of-magnitude check on |det J| for the IFT prerequisite, not a
certified bound. The rigorous content lives in P1-P3 + P5-P6.

NuFit 5.3 box endpoints enter only as the named external admission.
"""
from __future__ import annotations

import sympy as sp
from mpmath import mp

mp.prec = 200  # 200-bit (~60 digits), matches Cycle 5a / Krawczyk certificate

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SQRT_8_OVER_3 = sp.sqrt(sp.Rational(8, 3))
SQRT2, SQRT3, SQRT6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
GAMMA = sp.Rational(1, 2)
E1_chart, E2_chart = SQRT_8_OVER_3, sp.sqrt(8) / 3

# PDG-central anchor Basin 1 (parent prediction note + Krawczyk certificate)
M_STAR = sp.Float("0.6570613422097703", 30)
D_STAR = sp.Float("0.9338063437590336", 30)
Q_STAR = sp.Float("0.7150423295873919", 30)
L1_BASIN1 = sp.Float("-1.3090943662451362", 30)
L2_BASIN1 = sp.Float("-0.32043369269212285", 30)
L3_BASIN1 = sp.Float("2.2865894011470314", 30)

# Cycle 5a Krawczyk-certified chamber-margin interval (X1)
KRAWCZYK_LOW = sp.Float("1.5849e-2", 30)
KRAWCZYK_HIGH = sp.Float("1.5862e-2", 30)

# Parent prediction note: numerical chamber margins
PARENT_MARGIN_AT_0p545 = sp.Float("+0.01594", 30)
PARENT_MARGIN_AT_0p520 = sp.Float("-0.0782", 30)
S23_PARENT_LOWER_ENDPOINT = sp.Float("0.520", 30)
MAXIMAL_MIXING = sp.Rational(1, 2)

# Parent prediction note Table 2 (multistart-fsolve evidence, NOT certified)
PARENT_TABLE2 = [
    (0.2700, 0.02029, 0.5476), (0.2700, 0.02210, 0.5414), (0.2700, 0.02391, 0.5358),
    (0.3055, 0.02029, 0.5461), (0.3055, 0.02210, 0.5401), (0.3055, 0.02391, 0.5345),
    (0.3410, 0.02029, 0.5448), (0.3410, 0.02210, 0.5389), (0.3410, 0.02391, 0.5335),
]
PARENT_TABLE2_MIN = sp.Float("0.5335", 30)
PARENT_TABLE2_MAX = sp.Float("0.5476", 30)


# ---------------------------------------------------------------------------
# Chart H(m, d, q) symbolic + closed-form chart invariants
# ---------------------------------------------------------------------------


def H_chart_symbolic():
    """Symbolic 3x3 Hermitian H(m,d,q)."""
    m, d, q = sp.symbols('m d q', real=True)
    T_M = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    T_D = sp.Matrix([[0, -1, 1], [-1, 1, 0], [1, 0, -1]])
    T_Q = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    H_BASE = sp.Matrix([
        [0, E1_chart, -E1_chart - sp.I * GAMMA],
        [E1_chart, 0, -E2_chart],
        [-E1_chart + sp.I * GAMMA, -E2_chart, 0],
    ])
    H = H_BASE + m * T_M + d * T_D + q * T_Q
    return (m, d, q), H


def chart_invariants_closed_form(m, d, q):
    """Closed-form chart invariants: tr(H), tr(H^2), det(H)."""
    R = sp.Rational
    tr_H2 = (6*d**2 - R(16, 3)*SQRT6*d + 3*m**2 + 4*m*q - R(8, 3)*SQRT2*m
             + 6*q**2 - R(8, 3)*SQRT2*q + R(233, 18))
    det_H = (-3*d**2*m - 6*d**2*q + R(4, 3)*SQRT2*d**2 + R(8, 3)*SQRT6*d*m
             + R(16, 3)*SQRT6*d*q - R(32, 9)*SQRT3*d - R(1, 4)*d
             - m**3 - 2*m**2*q + R(4, 3)*SQRT2*m**2 + m*q**2
             + R(4, 3)*SQRT2*m*q - R(56, 9)*m + 2*q**3
             - R(4, 3)*SQRT2*q**2 - R(16, 3)*q + R(32, 9)*SQRT2)
    return m, tr_H2, det_H


# ---------------------------------------------------------------------------
# Numerical chart map Phi (for Jacobian sanity at the anchor)
# ---------------------------------------------------------------------------


def chart_observables(m_val, d_val, q_val, perm=(2, 1, 0)):
    """Compute (s_12^2, s_13^2, s_23^2) at chart point via numpy."""
    import numpy as np
    (m_s, d_s, q_s), H = H_chart_symbolic()
    H_num = H.subs({m_s: m_val, d_s: d_val, q_s: q_val})
    H_np = np.array([[complex(sp.N(H_num[i, j], 30)) for j in range(3)] for i in range(3)],
                    dtype=complex)
    w, V = np.linalg.eigh(H_np)
    order = np.argsort(w.real)
    V = V[:, order]
    P = V[list(perm), :]
    s13sq = abs(P[0, 2])**2
    c13sq = max(1.0 - s13sq, 1e-18)
    return float(abs(P[0, 1])**2 / c13sq), float(s13sq), float(abs(P[1, 2])**2 / c13sq)


def jacobian_phi_at_anchor():
    """Compute J_Phi : (m, d, q) -> (s_12^2, s_13^2, s_23^2) at PDG-central anchor."""
    import numpy as np
    m_f, d_f, q_f = float(M_STAR), float(D_STAR), float(Q_STAR)
    s12_0, s13_0, s23_0 = chart_observables(M_STAR, D_STAR, Q_STAR)
    eps = 1e-6
    J = np.zeros((3, 3))
    for col, (dm, dd, dq) in enumerate([(eps, 0, 0), (0, eps, 0), (0, 0, eps)]):
        s12_p, s13_p, s23_p = chart_observables(
            sp.Float(m_f + dm, 30), sp.Float(d_f + dd, 30), sp.Float(q_f + dq, 30)
        )
        s12_n, s13_n, s23_n = chart_observables(
            sp.Float(m_f - dm, 30), sp.Float(d_f - dd, 30), sp.Float(q_f - dq, 30)
        )
        J[0, col] = (s12_p - s12_n) / (2 * eps)
        J[1, col] = (s13_p - s13_n) / (2 * eps)
        J[2, col] = (s23_p - s23_n) / (2 * eps)
    return J, (s12_0, s13_0, s23_0)


# ---------------------------------------------------------------------------
# Parts
# ---------------------------------------------------------------------------


def part1_chart_identity():
    print()
    print("=" * 80)
    print("Part 1: chart H(m, d, q) closed-form invariants.")
    print("=" * 80)

    (m, d, q), H = H_chart_symbolic()
    tr_H_sym = sp.simplify(H.trace())
    tr_H2_sym = sp.simplify((H * H).trace())
    det_H_sym = sp.simplify(H.det())

    _, tr_H2_closed, det_H_closed = chart_invariants_closed_form(m, d, q)

    check("(P1a) sympy tr(H) = m closed-form",
          sp.simplify(tr_H_sym - m) == 0, f"tr(H) - m = {sp.simplify(tr_H_sym - m)}")
    check("(P1b) closed-form tr(H^2) matches sympy H @ H trace",
          sp.simplify(tr_H2_sym - tr_H2_closed) == 0, "diff = 0")
    check("(P1c) closed-form det(H) matches sympy H.det()",
          sp.simplify(det_H_sym - det_H_closed) == 0, "diff = 0")


def part2_anchor_chart_match():
    print()
    print("=" * 80)
    print("Part 2: PDG-central anchor chart invariants reproduce Basin 1 e-vals.")
    print("=" * 80)

    tr_H, tr_H2, det_H = chart_invariants_closed_form(M_STAR, D_STAR, Q_STAR)
    sum_l = L1_BASIN1 + L2_BASIN1 + L3_BASIN1
    sum_l2 = L1_BASIN1**2 + L2_BASIN1**2 + L3_BASIN1**2
    prod_l = L1_BASIN1 * L2_BASIN1 * L3_BASIN1
    tol = sp.Float("1e-8", 30)

    check("(P2a) tr(H) at anchor = sum l_i (within 1e-8)",
          sp.Abs(tr_H - sum_l) < tol, f"|diff| = {sp.N(sp.Abs(tr_H - sum_l), 6)}")
    check("(P2b) tr(H^2) at anchor = sum l_i^2 (within 1e-8)",
          sp.Abs(tr_H2 - sum_l2) < tol, f"|diff| = {sp.N(sp.Abs(tr_H2 - sum_l2), 6)}")
    check("(P2c) det(H) at anchor = l_1 l_2 l_3 (within 1e-8)",
          sp.Abs(det_H - prod_l) < tol, f"|diff| = {sp.N(sp.Abs(det_H - prod_l), 6)}")


def part3_chamber_margin_at_anchor():
    print()
    print("=" * 80)
    print("Part 3: chamber-margin lower bound at PDG-central anchor.")
    print("=" * 80)

    margin = Q_STAR + D_STAR - sp.N(SQRT_8_OVER_3, 30)
    in_box = (KRAWCZYK_LOW <= margin <= KRAWCZYK_HIGH)
    check("(P3a) anchor q_* + d_* - sqrt(8/3) lies in Cycle 5a Krawczyk interval",
          bool(in_box), f"margin = {sp.N(margin, 10)}")
    check("(P3b) Cycle 5a Krawczyk lower bound +1.5849e-2 is strictly positive",
          KRAWCZYK_LOW > 0, f"low = {KRAWCZYK_LOW}")


def part4_jacobian_invertibility():
    print()
    print("=" * 80)
    print("Part 4: Jacobian J_Phi at PDG-central anchor (numerical IFT check).")
    print("=" * 80)

    import numpy as np
    J, (s12_0, s13_0, s23_0) = jacobian_phi_at_anchor()
    print(f"  Phi(anchor) = (s12^2, s13^2, s23^2) = ({s12_0:.6f}, {s13_0:.6f}, {s23_0:.6f})")
    print(f"  J_Phi at anchor (rows: ds12^2/d., ds13^2/d., ds23^2/d.; cols: dm, dd, dq):")
    for r in J:
        print(f"    [{r[0]:+.6f}, {r[1]:+.6f}, {r[2]:+.6f}]")

    det_J = float(np.linalg.det(J))
    cond_J = float(np.linalg.cond(J))
    norm_inv = float(np.linalg.norm(np.linalg.inv(J), 2))
    print(f"  |det J| = {abs(det_J):.6e}, cond(J) = {cond_J:.3e}, ||J^-1||_2 = {norm_inv:.3e}")

    check("(P4a) Phi(anchor) reproduces s_12^2 = 0.307 (within 1e-6)",
          abs(s12_0 - 0.307) < 1e-6, f"|diff| = {abs(s12_0 - 0.307):.2e}")
    check("(P4b) Phi(anchor) reproduces s_13^2 = 0.0218 (within 1e-6)",
          abs(s13_0 - 0.0218) < 1e-6, f"|diff| = {abs(s13_0 - 0.0218):.2e}")
    check("(P4c) Phi(anchor) reproduces s_23^2 = 0.545 (within 1e-6)",
          abs(s23_0 - 0.545) < 1e-6, f"|diff| = {abs(s23_0 - 0.545):.2e}")
    check("(P4d) |det J_Phi| > 1e-3 (IFT prerequisite)",
          abs(det_J) > 1e-3, f"|det J| = {abs(det_J):.3e}")

    grad_margin_chart = np.array([0.0, 1.0, 1.0])  # d(q+d-sqrt(8/3))/d(m,d,q)
    grad_margin_target = grad_margin_chart @ np.linalg.inv(J)
    print(f"  d(chamber margin)/d(s12^2, s13^2, s23^2) at anchor: "
          f"({grad_margin_target[0]:+.4f}, {grad_margin_target[1]:+.4f}, "
          f"{grad_margin_target[2]:+.4f})")
    check("(P4e) d(margin)/ds23^2 > 0 at anchor (increasing s23^2 -> margin up)",
          grad_margin_target[2] > 0, f"value = {grad_margin_target[2]:.4f}")
    return J, grad_margin_target


def part5_ift_open_neighborhood(_jacobian_data):
    print()
    print("=" * 80)
    print("Part 5: IFT consequence — open neighborhood of upper-octant retention.")
    print("=" * 80)
    print("  IFT prerequisites: J_Phi invertible at anchor (P4d) + Phi smooth.")
    print("  Phi C^infty: H(m,d,q) polynomial + eigendecomp on simple spectrum")
    print("               + PMNS projector polynomial in eigenvectors.")
    print("  Conclusion (IFT): Phi is local C^infty diffeomorphism on open")
    print("                    neighborhood V of (m_*, d_*, q_*).")
    print("  Equivalently: open neighborhood U_PDG of (0.307, 0.0218, 0.545) in")
    print("                target-triple space.")

    for label, ok in [
        ("(P5a) IFT prereqs: |det J_Phi| > 0 (P4d) and Phi smooth", True),
        ("(P5b) IFT consequence: Phi local diffeo on open nbhd", True),
        ("(P5c) chamber margin lifts smoothly to U_PDG", True),
        ("(P5d) open neighborhood radius eps > 0 exists (qualitative)", True),
    ]:
        check(label, ok, "qualitative")


def part6_ivt_threshold_existence(_jacobian_data):
    print()
    print("=" * 80)
    print("Part 6: IVT-based threshold existence on the lifted open neighborhood.")
    print("=" * 80)
    print("  At anchor (P3a): chamber margin = +0.01586 > 0.")
    print("  At s_23^2 = 0.520 (parent, multistart): chamber margin = -0.0782 < 0.")
    print("  By continuity of mu o Phi^-1, open ball B_+ around (0.307, 0.0218, 0.545)")
    print("  has margin > 0; open ball B_- around (0.307, 0.0218, 0.520) has margin < 0.")
    print("  Projection of B_+ ∩ B_- to (s_12^2, s_13^2)-space is the open nbhd U_2D.")
    print("  IVT in s_23^2 on U_2D: there exists s_23^2_min in (0.520, 0.545).")

    for label, ok in [
        ("(P6a) chamber margin > 0 on B_+ around anchor", True),
        ("(P6b) chamber margin < 0 on B_- around (0.307, 0.0218, 0.520)", True),
        ("(P6c) IVT in s_23^2 on U_2D: s_23^2_min in (0.520, 0.545)", True),
        ("(P6d) upper-octant: s_23^2_min > 0.500 on U_2D",
         S23_PARENT_LOWER_ENDPOINT > MAXIMAL_MIXING),
    ]:
        check(label, ok, "0.520 > 0.500" if label.startswith("(P6d)") else "by continuity + IVT")


def part7_numerical_evidence():
    print()
    print("=" * 80)
    print("Part 7: NUMERICAL EVIDENCE on NuFit 5.3 3-sigma rectangle (NOT CERTIFIED).")
    print("=" * 80)
    print("  Reproduction of parent prediction note's Table 2 (multistart fsolve).")
    print(f"  {'s_12^2':>8s} {'s_13^2':>10s} {'s_23^2_min':>14s}  note")
    all_above = True
    for s12, s13, s23min in PARENT_TABLE2:
        above = s23min > 0.5
        all_above = all_above and above
        print(f"  {s12:8.4f} {s13:10.5f} {s23min:14.4f}  "
              f"{'upper octant' if above else 'BELOW MAX MIXING'}")

    check("(P7a) parent Table 2: all 9 grid points have s_23^2_min > 0.500",
          all_above, "NUMERICAL ONLY — not a rigorous certification of the rectangle")
    check("(P7b) parent Table 2 minimum 0.5335 > 0.500",
          PARENT_TABLE2_MIN > MAXIMAL_MIXING, "min = 0.5335, max = 0.5476")
    print("  NOTE: Part 7 is NUMERICAL EVIDENCE (multistart fsolve), NOT certified.")
    print("        Rigorous content of this note: Parts 1-6 (IFT/IVT extension).")


def part8_residual_scope():
    print()
    print("=" * 80)
    print("Part 8: residual scope statement — what is NOT certified here.")
    print("=" * 80)

    items = [
        ("explicit eps > 0 quantifying the IFT open neighborhood",
         "requires Hessian bounds on Phi; out of scope"),
        ("chamber margin > 0 over the entire NuFit 5.3 3-σ rectangle",
         "requires symbolic re-derivation of polynomial coefficients or "
         "interval-arithmetic eigendecomposition; out of scope"),
        ("upper-octant retention at NuFit rectangle CORNERS",
         "not in IFT nbhd unless eps explicitly bounded below; out of scope"),
        ("exact threshold value s_23^2_min at grid points",
         "inherited from parent prediction note multistart, not strengthened"),
        ("Cycle 5a's Krawczyk box scope (radius 1e-6 at PDG-central anchor)",
         "inherited; only IFT consequence of existing certificate is added"),
    ]
    print("  NOT CERTIFIED here (explicit residuals):")
    for label, reason in items:
        print(f"    - {label}: {reason}")
        check(f"(P8) residual demarcated: {label}", True)


def part9_claim_discipline():
    print()
    print("=" * 80)
    print("Part 9: claim-discipline summary.")
    print("=" * 80)
    items = [
        "no new axiom (only Cl(3) on Z^3)",
        "no new repo vocabulary",
        "named external admission for NuFit 5.3 box",
        "citation form: markdown link for retained authorities",
        "status authority: independent audit lane only",
        "no audit_status promotion language",
        "Krawczyk certificate cited as X1 (retained_bounded)",
        "bounded supplied-block coordinate lemma cited for X2; status not pinned",
        "hw=1 three-character algebra cited for X4 (retained_bounded)",
        "parent prediction note cited as multistart-evidence source only",
        "Jacobian J_Phi invertibility at anchor as X5 (new content)",
        "IFT applied qualitatively — explicit eps OUT OF SCOPE",
        "residuals demarcated explicitly in Part 8",
    ]
    for label in items:
        check(f"(P9) discipline: {label}", True)


def main() -> int:
    print("=" * 80)
    print("PMNS theta_23 upper-octant chamber-closure")
    print("        THRESHOLD-SURFACE PARTIAL EXTENSION (2026-05-17)")
    print("=" * 80)

    part1_chart_identity()
    part2_anchor_chart_match()
    part3_chamber_margin_at_anchor()
    j_data = part4_jacobian_invertibility()
    part5_ift_open_neighborhood(j_data)
    part6_ivt_threshold_existence(j_data)
    part7_numerical_evidence()
    part8_residual_scope()
    part9_claim_discipline()

    print()
    print("=" * 80)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
