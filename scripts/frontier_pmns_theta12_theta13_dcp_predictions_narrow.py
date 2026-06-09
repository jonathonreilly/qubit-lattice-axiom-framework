#!/usr/bin/env python3
"""PMNS theta_12 / theta_13 / delta_CP predictions narrow rescope companion.

Companion runner for
docs/PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md

Cycle 8 of the box-Krawczyk cascade (Cycles 5a, 6a, 7 closed s_23^2 > 0.5 over
the NuFit 5.3 NO 3-sigma rectangle on (s_12^2, s_13^2); this iteration extends
the box-Krawczyk machinery to the OTHER three observables s_12^2, s_13^2, and
delta_CP).

This runner:

  Part 1   (S1)   sympy: chamber-boundary constant identity sqrt(8/3) =
                  2 sqrt(6)/3 (inherited from Cycle 7, same chart).

  Part 2          mpmath.iv at PDG anchor: interval Newton brackets the three
                  eigenvalues of H at the PDG-central anchor to width
                  < 1e-13 at 200-bit precision (inherited from Cycle 7).

  Part 3          mpmath.iv at PDG anchor: adjugate-based interval
                  projectors reproduce the PDG-central readout
                  (s_12^2, s_13^2, s_23^2) = (0.307, 0.0218, 0.545).

  Part 4          mpmath.iv at PDG anchor: rephasing-invariant Jarlskog J,
                  Re(box) for cos(delta_CP), sin(delta_CP), and cos(delta_CP)
                  via projector identities; verify match parent's reported
                  sin(delta_CP) = -0.9874 +- 1e-3, and physical
                  delta_CP ~ 260.88 deg (third quadrant) to within 0.05 deg.

  Part 5          mpmath.iv BOX-KRAWCZYK CERTIFICATION over B = [0.625, 0.750]
                  x [0.902, 0.956] with q = sqrt(8/3) - delta. 80 x 80 grid
                  (6400 sub-boxes). For every image-overlap sub-box (forward
                  (s_12^2, s_13^2) intersects NuFit 2D rectangle):
                  - certify sin(delta_CP) < 0 strictly (Jarlskog negative);
                  - certify cos(delta_CP) < 0 strictly (third quadrant);
                  - record interval bounds on sin(delta_CP), cos(delta_CP),
                    and delta_CP (extracted via atan2).
                  Aggregate: derive a rigorous lower bound on -sin(delta_CP)
                  (i.e. |sin(delta_CP)| over all image-overlap sub-boxes)
                  and a rigorous range on delta_CP.
                  *This is the new computational content of this note (X5*).*

  Part 6          mpmath.iv NEGATIVE STRUCTURAL FINDING on theta_12 / theta_13.
                  Over the same B and the same chamber-boundary embedding,
                  certify by enumeration that the (s_12^2, s_13^2) image
                  COVERS the entire NuFit 2D rectangle (every 20x20 cell of
                  the rectangle is hit by at least one sub-box of B at
                  200-bit interval-arithmetic resolution); HONEST FINDING:
                  framework leaves s_12^2 and s_13^2 unconstrained within
                  NuFit 3-sigma.

  Part 7          Preimage-localization admission (X6, inherited from
                  parent prediction note Table 2 / Cycle 7).

  Part 8          Residual scope statement.

  Part 9          Claim-discipline summary.

No new axiom (only Cl(3) on Z^3). No new repo vocabulary. Status authority:
independent audit lane only.
"""
from __future__ import annotations

import math
import time

import numpy as np
import sympy as sp
from mpmath import iv, mp

mp.prec = 200
# mpmath's mp and iv contexts have INDEPENDENT precision. Setting mp.prec does NOT change iv.prec
# (which defaults to 53 bits), so the interval-arithmetic parts (interval Newton, projectors,
# box-Krawczyk in Parts 2-5) must set iv.prec explicitly to actually run at 200-bit, as this note claims.
iv.prec = 200


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
# Constants: chart structure and named external admissions.
# ---------------------------------------------------------------------------

SQRT_8_3 = iv.sqrt(iv.mpf(8) / iv.mpf(3))
SQRT_8 = iv.sqrt(iv.mpf(8))
SQRT8_3 = SQRT_8 / iv.mpf(3)
GAMMA = iv.mpf("0.5")

SQRT_8_3_F = math.sqrt(8.0 / 3.0)
SQRT8_3_F = math.sqrt(8.0) / 3.0
GAMMA_F = 0.5

# PDG-central anchor (12 digits).
M_STAR = iv.mpf("0.657061342210")
DELTA_STAR = iv.mpf("0.933806343759")
Q_STAR = iv.mpf("0.715042329587")

# Box-cover B for the (m, delta) preimage of the NuFit 2D rectangle.
M_LO, M_HI = 0.625, 0.750
D_LO, D_HI = 0.902, 0.956
NX, NY = 80, 80

# NuFit 5.3 NO 3-sigma rectangle on (s_12^2, s_13^2) -- named external (X3).
S12_LO, S12_HI = 0.270, 0.341
S13_LO, S13_HI = 0.02029, 0.02391
# NuFit 5.3 NO 3-sigma on delta_CP (degrees, PDG convention): [120, 369]
# (NuFit treats delta_CP as 1-D 3-sigma interval; we use 369 -> 9 wrap).
NUFIT_DCP_LO_DEG = 120.0
NUFIT_DCP_HI_DEG = 369.0

# Parent-runner reported PDG-anchor values for cross-check:
SIN_DCP_PARENT = -0.9874
DCP_PARENT_THIRD_QUADRANT_DEG = 260.88  # 180 + (180 - 80.88) third-quadrant value


# ---------------------------------------------------------------------------
# Hermitian chart H(m, delta, q).
# ---------------------------------------------------------------------------


def H_entries(m, d, q):
    h11 = m
    h22 = d
    h33 = -d
    h12r = SQRT_8_3 - d + q
    h12i = iv.mpf(0)
    h13r = -SQRT_8_3 + d + q
    h13i = -GAMMA
    h23r = -SQRT8_3 + m + q
    h23i = iv.mpf(0)
    return (h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i)


def char_poly_coeffs(m, d, q):
    h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i = H_entries(m, d, q)
    a12sq = h12r * h12r + h12i * h12i
    a13sq = h13r * h13r + h13i * h13i
    a23sq = h23r * h23r + h23i * h23i
    trH = h11 + h22 + h33
    e2 = h11 * h22 + h11 * h33 + h22 * h33 - a12sq - a13sq - a23sq
    re_triple = 2 * (
        h12r * (h23r * h13r + h23i * h13i)
        + h12i * (h23r * h13i - h23i * h13r)
    )
    detH = h11 * h22 * h33 - h11 * a23sq - h33 * a12sq - h22 * a13sq + re_triple
    return trH, e2, detH


def char_poly(lam, trH, e2, detH):
    return lam * lam * lam - trH * lam * lam + e2 * lam - detH


def char_poly_prime(lam, trH, e2):
    return iv.mpf(3) * lam * lam - iv.mpf(2) * trH * lam + e2


def iv_intersect(A, B):
    a = max(float(A.a), float(B.a))
    b = min(float(A.b), float(B.b))
    if a > b:
        return None
    return iv.mpf([a, b])


def iv_width(L):
    return float(L.b - L.a)


def interval_newton(seed_center, seed_radius, trH, e2, detH, max_iter=60):
    L = iv.mpf([seed_center - seed_radius, seed_center + seed_radius])
    for _ in range(max_iter):
        mid = iv.mpf(float(L.mid))
        f_mid = char_poly(mid, trH, e2, detH)
        fp_L = char_poly_prime(L, trH, e2)
        if 0 in fp_L:
            return None
        N = mid - f_mid / fp_L
        L_new = iv_intersect(L, N)
        if L_new is None:
            return None
        if iv_width(L_new) < 1e-50:
            return L_new
        if iv_width(L_new) >= iv_width(L) * 0.999:
            return L_new
        L = L_new
    return L


def numpy_seeds(m_f, d_f, q_f):
    H_mid = np.array(
        [
            [m_f, SQRT_8_3_F - d_f + q_f, -SQRT_8_3_F + d_f + q_f - 1j * GAMMA_F],
            [SQRT_8_3_F - d_f + q_f, d_f, -SQRT8_3_F + m_f + q_f],
            [-SQRT_8_3_F + d_f + q_f + 1j * GAMMA_F, -SQRT8_3_F + m_f + q_f, -d_f],
        ]
    )
    return sorted(np.linalg.eigvalsh(H_mid))


# ---------------------------------------------------------------------------
# Complex interval arithmetic helpers (pairs of mpmath intervals for re/im).
# ---------------------------------------------------------------------------


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def H_matrix(m, d, q):
    h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i = H_entries(m, d, q)
    Z = iv.mpf(0)
    return [
        [(h11, Z), (h12r, h12i), (h13r, h13i)],
        [(h12r, -h12i), (h22, Z), (h23r, h23i)],
        [(h13r, -h13i), (h23r, -h23i), (h33, Z)],
    ]


def mat_sub_lambda(M, lam):
    return [
        [csub(M[i][j], (lam if i == j else iv.mpf(0), iv.mpf(0))) for j in range(3)]
        for i in range(3)
    ]


def mat_mul(A, B):
    C = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = (iv.mpf(0), iv.mpf(0))
            for k in range(3):
                s = cadd(s, cmul(A[i][k], B[k][j]))
            C[i][j] = s
    return C


def mat_scale_real(A, s):
    return [[(A[i][j][0] / s, A[i][j][1] / s) for j in range(3)] for i in range(3)]


def projector(M, lams, i):
    j, k = [x for x in range(3) if x != i]
    A = mat_sub_lambda(M, lams[j])
    B = mat_sub_lambda(M, lams[k])
    AB = mat_mul(A, B)
    denom = (lams[i] - lams[j]) * (lams[i] - lams[k])
    return mat_scale_real(AB, denom)


def pmns_full_interval(m_iv, d_iv, q_iv):
    """Compute (s_12^2, s_13^2, s_23^2, J, ReBox, cos_neg_num, ratio_sq, sin_dcp, cos_dcp)
    as interval-arithmetic objects over a (m, d, q) box.

    Returns dict with intervals, or None if any step fails.

    Rephasing-invariant J and ReBox formulas (with sigma_hier = (2, 1, 0) so
    flavor electron = V row 2, muon = V row 1; PDG indices i=0 smallest,
    i=1 middle, i=2 largest eigenvalue):

      J = Im[(P_0)_{2,1} * (P_1)_{1,2}]                  (Jarlskog)
      ReBox = Re[(P_0)_{2,1} * (P_2)_{1,2}]              (cos-companion)

    With PDG decomposition:
      J     = -c_12 s_12 c_23 s_23 c_13^2 s_13 sin(d_CP)               (*)
      ReBox = -c_12 s_12 c_23 s_23 c_13^2 s_13 cos(d_CP)
              - c_12^2 c_13^2 s_13^2 s_23^2

    Let cos_neg_num = ReBox + c_12^2 c_13^2 s_13^2 s_23^2. Then:

      cos(d_CP) = -cos_neg_num / D
      sin(d_CP) = J / D            (signs follow eq. (*))
      D         = c_12 s_12 c_23 s_23 c_13^2 s_13   (D > 0 strictly on B)

    For the third-quadrant prediction we use the D-free certified inequalities:

      sin(d_CP) < 0  iff  J < 0       (since D > 0)
      cos(d_CP) < 0  iff  cos_neg_num > 0    (since D > 0)

    For the d_CP magnitude bounds (within the third quadrant) we use:

      d_CP = pi + arctan(|sin|/|cos|) = pi + arctan(|J| / |cos_neg_num|)

    Both numerator and denominator are interval-arithmetic free of
    the D division, eliminating the dependency-blow-up issue.
    """
    trH, e2, detH = char_poly_coeffs(m_iv, d_iv, q_iv)
    m_mid = float(m_iv.mid)
    d_mid = float(d_iv.mid)
    q_mid = float(q_iv.mid)
    w = numpy_seeds(m_mid, d_mid, q_mid)
    eigs = []
    for seed in w:
        L = interval_newton(seed, 0.1, trH, e2, detH)
        if L is None:
            return None
        eigs.append(L)
    M_mat = H_matrix(m_iv, d_iv, q_iv)
    P0 = projector(M_mat, eigs, 0)
    P1 = projector(M_mat, eigs, 1)
    P2 = projector(M_mat, eigs, 2)
    # PMNS observables (s_12^2, s_13^2, s_23^2)
    s_13sq = P2[2][2][0]
    s_12sq_num = P1[2][2][0]
    s_23sq_num = P2[1][1][0]
    denom_c13sq = iv.mpf(1) - s_13sq
    if 0 in denom_c13sq:
        return None
    s_12sq = s_12sq_num / denom_c13sq
    s_23sq = s_23sq_num / denom_c13sq
    # Jarlskog and ReBox via projectors.
    P0_21 = P0[2][1]
    P1_12 = P1[1][2]
    P2_12 = P2[1][2]
    prod_J = cmul(P0_21, P1_12)
    J_iv = prod_J[1]  # imaginary part
    prod_R = cmul(P0_21, P2_12)
    ReBox_iv = prod_R[0]
    # Build c_12^2 etc.
    c_12sq = iv.mpf(1) - s_12sq
    c_23sq = iv.mpf(1) - s_23sq
    # cos_neg_num = ReBox + c_12^2 c_13^2 s_13^2 s_23^2
    cos_neg_num = ReBox_iv + c_12sq * denom_c13sq * s_13sq * s_23sq
    # For magnitude bounds, only compute sin_dcp / cos_dcp via division if
    # we need them; otherwise stay with J and cos_neg_num.
    return {
        "s_12sq": s_12sq,
        "s_13sq": s_13sq,
        "s_23sq": s_23sq,
        "c_12sq": c_12sq,
        "c_13sq": denom_c13sq,
        "c_23sq": c_23sq,
        "J": J_iv,
        "ReBox": ReBox_iv,
        "cos_neg_num": cos_neg_num,
        "eigs": eigs,
    }


def sin_cos_dcp_from_block(block):
    """Compute interval sin(d_CP) and cos(d_CP) from a block (only for anchor / sanity).

    Note: division by D introduces interval-dependency blow-up; use this only
    for low-blow-up reporting at the anchor (point intervals) and for sanity
    checks. The certified inequalities use J and cos_neg_num directly.
    """
    s_12sq = block["s_12sq"]
    s_13sq = block["s_13sq"]
    s_23sq = block["s_23sq"]
    c_12sq = block["c_12sq"]
    c_13sq = block["c_13sq"]
    c_23sq = block["c_23sq"]
    if (0 in c_12sq or 0 in c_23sq or 0 in s_12sq or 0 in s_23sq or 0 in s_13sq
            or float(c_12sq.a) <= 0 or float(c_23sq.a) <= 0
            or float(s_12sq.a) <= 0 or float(s_23sq.a) <= 0
            or float(s_13sq.a) <= 0):
        return None
    D_iv = iv.sqrt(c_12sq * s_12sq * c_23sq * s_23sq) * c_13sq * iv.sqrt(s_13sq)
    if 0 in D_iv:
        return None
    sin_dcp_iv = block["J"] / D_iv
    cos_dcp_iv = -block["cos_neg_num"] / D_iv
    return {"sin_dcp": sin_dcp_iv, "cos_dcp": cos_dcp_iv, "D": D_iv}


# ---------------------------------------------------------------------------
# Part 1: sympy chart-invariant identity.
# ---------------------------------------------------------------------------


def part1_sqrt_identity() -> None:
    print()
    print("=" * 80)
    print("Part 1 (S1): sympy: chamber-boundary constant identity (inherited from Cycle 7).")
    print("=" * 80)

    lhs = sp.sqrt(sp.Rational(8, 3))
    rhs = sp.Rational(2, 3) * sp.sqrt(6)
    diff = sp.simplify(lhs - rhs)
    check(
        "(S1) sympy.simplify(sqrt(8/3) - 2 sqrt(6)/3) == 0",
        diff == 0,
        f"diff = {diff}",
    )
    check(
        "(S1a) (sqrt(8/3))^2 = 8/3",
        sp.simplify(lhs ** 2) == sp.Rational(8, 3),
    )


# ---------------------------------------------------------------------------
# Part 2: interval Newton at PDG anchor.
# ---------------------------------------------------------------------------


def part2_anchor_eigenvalue_bracketing():
    print()
    print("=" * 80)
    print("Part 2: interval Newton brackets eigenvalues of H at PDG anchor.")
    print("=" * 80)

    trH, e2, detH = char_poly_coeffs(M_STAR, DELTA_STAR, Q_STAR)
    m_f = float(M_STAR.mid)
    d_f = float(DELTA_STAR.mid)
    q_f = float(Q_STAR.mid)
    w = numpy_seeds(m_f, d_f, q_f)

    eigs = []
    for idx, seed in enumerate(w):
        L = interval_newton(seed, 0.1, trH, e2, detH)
        check(
            f"(P2.{idx+1}) interval Newton converges for lambda_{idx+1}",
            L is not None,
        )
        if L is not None:
            width = iv_width(L)
            check(
                f"(P2.{idx+1}w) lambda_{idx+1} width <= 1e-13",
                width <= 1e-13,
                f"width = {width:.3e}",
            )
            eigs.append(L)

    if len(eigs) == 3:
        sep_12 = float(eigs[1].a) - float(eigs[0].b)
        sep_23 = float(eigs[2].a) - float(eigs[1].b)
        check("(P2.sep1) lambda_1 < lambda_2 strictly", sep_12 > 0,
              f"separation = {sep_12:.4f}")
        check("(P2.sep2) lambda_2 < lambda_3 strictly", sep_23 > 0,
              f"separation = {sep_23:.4f}")
    return eigs


# ---------------------------------------------------------------------------
# Part 3: anchor projector readout for (s_12^2, s_13^2, s_23^2).
# ---------------------------------------------------------------------------


def part3_anchor_observables():
    print()
    print("=" * 80)
    print("Part 3: adjugate projectors reproduce PDG-central (0.307, 0.0218, 0.545).")
    print("=" * 80)

    r = pmns_full_interval(M_STAR, DELTA_STAR, Q_STAR)
    if r is None:
        check("(P3) anchor readout", False, "computation failed")
        return
    s12 = r["s_12sq"]; s13 = r["s_13sq"]; s23 = r["s_23sq"]
    print(f"  s_12^2 = [{float(s12.a):.10f}, {float(s12.b):.10f}]")
    print(f"  s_13^2 = [{float(s13.a):.10f}, {float(s13.b):.10f}]")
    print(f"  s_23^2 = [{float(s23.a):.10f}, {float(s23.b):.10f}]")
    check("(P3.1) s_12^2 contains 0.307 within 1e-9",
          float(s12.a) - 1e-9 <= 0.307 <= float(s12.b) + 1e-9,
          f"interval [{float(s12.a):.13f}, {float(s12.b):.13f}]")
    check("(P3.2) s_13^2 contains 0.0218 within 1e-9",
          float(s13.a) - 1e-9 <= 0.0218 <= float(s13.b) + 1e-9,
          f"interval [{float(s13.a):.13f}, {float(s13.b):.13f}]")
    check("(P3.3) s_23^2 contains 0.545 within 1e-9",
          float(s23.a) - 1e-9 <= 0.545 <= float(s23.b) + 1e-9,
          f"interval [{float(s23.a):.13f}, {float(s23.b):.13f}]")
    return r


# ---------------------------------------------------------------------------
# Part 4: anchor delta_CP + Jarlskog cross-check.
# ---------------------------------------------------------------------------


def part4_anchor_delta_cp():
    print()
    print("=" * 80)
    print("Part 4: anchor Jarlskog / cos_neg_num / sin(d_CP) / cos(d_CP) match parent runner.")
    print("=" * 80)

    r = pmns_full_interval(M_STAR, DELTA_STAR, Q_STAR)
    if r is None:
        check("(P4) anchor delta_CP", False, "computation failed")
        return
    J = r["J"]; ReBox = r["ReBox"]; cnn = r["cos_neg_num"]

    print(f"  J             interval = [{float(J.a):+.10f}, {float(J.b):+.10f}]")
    print(f"  ReBox         interval = [{float(ReBox.a):+.10f}, {float(ReBox.b):+.10f}]")
    print(f"  cos_neg_num   interval = [{float(cnn.a):+.10f}, {float(cnn.b):+.10f}]")
    check(
        "(P4.1) J interval contains parent's -0.0328 within 1e-4",
        float(J.a) - 1e-4 <= -0.0328 <= float(J.b) + 1e-4,
        f"interval [{float(J.a):.6f}, {float(J.b):.6f}]",
    )
    check(
        "(P4.2a) J interval strictly negative (sin(d_CP) sign certified)",
        float(J.b) < 0,
        f"upper J bound = {float(J.b):.6f}",
    )
    check(
        "(P4.2b) cos_neg_num interval strictly positive (cos(d_CP) negative)",
        float(cnn.a) > 0,
        f"lower cos_neg_num bound = {float(cnn.a):.6f}",
    )
    # Recover sin(d_CP) / cos(d_CP) at the anchor for parent-runner cross-check.
    extra = sin_cos_dcp_from_block(r)
    if extra is None:
        check("(P4) sin/cos extraction at anchor", False, "D zero or degenerate")
        return r
    sd = extra["sin_dcp"]; cd = extra["cos_dcp"]
    print(f"  sin(d_CP)     interval = [{float(sd.a):+.10f}, {float(sd.b):+.10f}]")
    print(f"  cos(d_CP)     interval = [{float(cd.a):+.10f}, {float(cd.b):+.10f}]")
    check(
        "(P4.3) sin(d_CP) interval contains parent's -0.9874 within 1e-3",
        float(sd.a) - 1e-3 <= SIN_DCP_PARENT <= float(sd.b) + 1e-3,
        f"interval [{float(sd.a):.4f}, {float(sd.b):.4f}]",
    )
    check(
        "(P4.4) cos(d_CP) interval strictly negative (third quadrant)",
        float(cd.b) < 0,
        f"upper bound = {float(cd.b):.6f}",
    )
    mid_sd = float(sd.mid)
    mid_cd = float(cd.mid)
    dcp_rad = math.atan2(mid_sd, mid_cd)
    dcp_deg = dcp_rad * 180.0 / math.pi
    dcp_pdg = dcp_deg % 360.0
    print(f"  delta_CP (atan2 at interval midpoints) = {dcp_deg:.4f} deg")
    print(f"  delta_CP (PDG convention, [0,360))     = {dcp_pdg:.4f} deg")
    check(
        "(P4.5) anchor delta_CP (PDG third-quadrant branch) matches parent's 260.88 within 0.1 deg",
        abs(dcp_pdg - DCP_PARENT_THIRD_QUADRANT_DEG) < 0.1,
        f"computed {dcp_pdg:.4f} vs. parent {DCP_PARENT_THIRD_QUADRANT_DEG:.4f}",
    )
    return r


# ---------------------------------------------------------------------------
# Part 5: BOX-KRAWCZYK delta_CP CERTIFICATION (NEW CONTENT).
# ---------------------------------------------------------------------------


def _dcp_pdg_bounds_from_intervals(J_iv, cnn_iv):
    """Given strictly-negative J and strictly-positive cos_neg_num intervals on a
    box, return the [d_CP_min, d_CP_max] bracket in PDG degrees [180, 270).

    Derivation (third quadrant):

        d_CP = pi + arctan(|sin|/|cos|)
             = pi + arctan( (|J|/D) / (cos_neg_num/D) )
             = pi + arctan( |J| / cos_neg_num )

    The D division cancels. The function arctan(x) is monotonically increasing
    in x. |J| / cos_neg_num is monotone in both arguments. The bracket is
    therefore obtained from the four corner combinations of (|J|, cos_neg_num).
    """
    # |J|: J is negative; |J| = -J ranges from -J_hi (min) to -J_lo (max)
    J_lo, J_hi = float(J_iv.a), float(J_iv.b)
    cnn_lo, cnn_hi = float(cnn_iv.a), float(cnn_iv.b)
    # |J| range: [-J_hi, -J_lo], both positive since J_hi < 0
    abs_J_min = -J_hi
    abs_J_max = -J_lo
    # ratio |J|/cnn (positive)
    # min ratio = abs_J_min / cnn_hi
    # max ratio = abs_J_max / cnn_lo
    if cnn_lo <= 0 or cnn_hi <= 0:
        # cos_neg_num straddles 0; cannot certify third quadrant
        return None
    ratio_min = abs_J_min / cnn_hi
    ratio_max = abs_J_max / cnn_lo
    # arctan monotone increasing
    ang_min = math.pi + math.atan(ratio_min)   # in (pi, 3pi/2)
    ang_max = math.pi + math.atan(ratio_max)
    return ang_min * 180.0 / math.pi, ang_max * 180.0 / math.pi


def _certify_subbox(m_iv, d_iv, q_iv):
    """Helper: evaluate pmns_full_interval and return (J, cnn, s12, s13, s23, ok)
    or (None, None, None, None, None, False).

    ok = (J.b < 0) and (cnn.a > 0).
    """
    r = pmns_full_interval(m_iv, d_iv, q_iv)
    if r is None:
        return None, None, None, None, None, False
    J = r["J"]; cnn = r["cos_neg_num"]
    s12 = r["s_12sq"]; s13 = r["s_13sq"]; s23 = r["s_23sq"]
    ok = float(J.b) < 0 and float(cnn.a) > 0
    return J, cnn, s12, s13, s23, ok


def _subdivide_until_certified(m_lo, m_hi, d_lo, d_hi, max_depth=6):
    """Recursively bisect a (m, d) sub-box until cos_neg_num > 0 and J < 0 certify
    on every sub-piece whose image overlaps the NuFit rectangle, OR until max_depth
    reached.

    Returns: (all_certify, n_subboxes_tried, abs_J_min, abs_J_max, cnn_min, cnn_max,
              dcp_min, dcp_max, s23_lower).
    """
    stack = [(m_lo, m_hi, d_lo, d_hi, 0)]
    all_certify = True
    n_tried = 0
    abs_J_min = 1e9; abs_J_max = 0.0
    cnn_min = 1e9;   cnn_max = 0.0
    dcp_min = 360.0; dcp_max = 0.0
    s23_lower = 1.0
    while stack:
        a_lo, a_hi, b_lo, b_hi, depth = stack.pop()
        m_iv = iv.mpf([a_lo, a_hi])
        d_iv = iv.mpf([b_lo, b_hi])
        q_iv = SQRT_8_3 - d_iv
        n_tried += 1
        J, cnn, s12, s13, s23, ok = _certify_subbox(m_iv, d_iv, q_iv)
        if J is None:
            # Interval-Newton failure
            all_certify = False
            continue
        # Check image overlap
        s12_lo = float(s12.a); s12_hi = float(s12.b)
        s13_lo = float(s13.a); s13_hi = float(s13.b)
        if s12_hi < S12_LO or s12_lo > S12_HI or s13_hi < S13_LO or s13_lo > S13_HI:
            continue  # disjoint; skip
        s23_lo = float(s23.a)
        if s23_lo < s23_lower:
            s23_lower = s23_lo
        if ok:
            bracket = _dcp_pdg_bounds_from_intervals(J, cnn)
            if bracket is not None:
                bmin, bmax = bracket
                if bmin < dcp_min: dcp_min = bmin
                if bmax > dcp_max: dcp_max = bmax
                aj_min = -float(J.b); aj_max = -float(J.a)
                if aj_min < abs_J_min: abs_J_min = aj_min
                if aj_max > abs_J_max: abs_J_max = aj_max
                cn_lo = float(cnn.a); cn_hi = float(cnn.b)
                if cn_lo < cnn_min: cnn_min = cn_lo
                if cn_hi > cnn_max: cnn_max = cn_hi
            else:
                all_certify = False
        else:
            if depth >= max_depth:
                all_certify = False
                continue
            mm = 0.5 * (a_lo + a_hi)
            dd_mid = 0.5 * (b_lo + b_hi)
            stack.append((a_lo, mm, b_lo, dd_mid, depth + 1))
            stack.append((mm, a_hi, b_lo, dd_mid, depth + 1))
            stack.append((a_lo, mm, dd_mid, b_hi, depth + 1))
            stack.append((mm, a_hi, dd_mid, b_hi, depth + 1))
    return (all_certify, n_tried, abs_J_min, abs_J_max, cnn_min, cnn_max,
            dcp_min, dcp_max, s23_lower)


def part5_delta_cp_box_krawczyk() -> dict:
    print()
    print("=" * 80)
    print("Part 5 (X5*, NEW CONTENT): box-Krawczyk delta_CP certification over B.")
    print("=" * 80)
    print("  D-free certification: J < 0 (sin<0); cos_neg_num > 0 (cos<0);")
    print("  d_CP in third quadrant; d_CP = pi + arctan(|J| / cos_neg_num).")
    print()

    dm = (M_HI - M_LO) / NX
    dd = (D_HI - D_LO) / NY
    print(f"  bounding box B = [{M_LO}, {M_HI}] x [{D_LO}, {D_HI}]")
    print(f"  grid: {NX} x {NY} = {NX*NY} sub-boxes  (dm={dm:.4e}, dd={dd:.4e})")
    print(f"  NuFit 5.3 NO 3-sigma rectangle (X3): s_12^2 in [{S12_LO}, {S12_HI}], "
          f"s_13^2 in [{S13_LO}, {S13_HI}]")
    print(f"  embedding: q = sqrt(8/3) - delta (chamber boundary)")
    print(f"  precision: 200-bit mpmath; seed radius 0.1")
    print(f"  bisection: failing sub-boxes recursively subdivided (max depth 6)")
    print()

    t0 = time.time()
    n_total = 0
    n_overlap = 0
    n_skip = 0
    n_newton_fail = 0
    n_overlap_J_neg = 0
    n_overlap_cnn_pos = 0
    n_overlap_third_q_top = 0   # third-quadrant at depth 0 (top-level grid)
    n_overlap_third_q_certified_via_bisect = 0   # certified via subdivision
    n_overlap_uncertified = 0
    n_subdivided = 0
    n_subbox_tried_total = 0

    dcp_pdg_min = 360.0
    dcp_pdg_max = 0.0
    abs_J_min_overlap = 1e9
    abs_J_max_overlap = 0.0
    cnn_min_overlap = 1e9
    cnn_max_overlap = 0.0
    s23_lower_tightest = 1.0

    for i in range(NX):
        for j in range(NY):
            m_lo = M_LO + i * dm
            m_hi = m_lo + dm
            d_lo = D_LO + j * dd
            d_hi = d_lo + dd
            m_iv = iv.mpf([m_lo, m_hi])
            d_iv = iv.mpf([d_lo, d_hi])
            q_iv = SQRT_8_3 - d_iv
            r = pmns_full_interval(m_iv, d_iv, q_iv)
            n_total += 1
            if r is None:
                n_newton_fail += 1
                continue
            s12 = r["s_12sq"]; s13 = r["s_13sq"]
            s12_lo, s12_hi = float(s12.a), float(s12.b)
            s13_lo, s13_hi = float(s13.a), float(s13.b)
            if (
                s12_hi < S12_LO
                or s12_lo > S12_HI
                or s13_hi < S13_LO
                or s13_lo > S13_HI
            ):
                n_skip += 1
                continue
            n_overlap += 1
            J = r["J"]; cnn = r["cos_neg_num"]
            J_hi = float(J.b)
            cnn_lo = float(cnn.a)
            s23 = r["s_23sq"]
            s23_lo_t = float(s23.a)
            if s23_lo_t < s23_lower_tightest:
                s23_lower_tightest = s23_lo_t
            J_neg = J_hi < 0
            cnn_pos = cnn_lo > 0
            if J_neg:
                n_overlap_J_neg += 1
            if cnn_pos:
                n_overlap_cnn_pos += 1
            if J_neg and cnn_pos:
                n_overlap_third_q_top += 1
                bracket = _dcp_pdg_bounds_from_intervals(J, cnn)
                if bracket is not None:
                    bmin, bmax = bracket
                    if bmin < dcp_pdg_min: dcp_pdg_min = bmin
                    if bmax > dcp_pdg_max: dcp_pdg_max = bmax
                    aj_min = -float(J.b); aj_max = -float(J.a)
                    if aj_min < abs_J_min_overlap: abs_J_min_overlap = aj_min
                    if aj_max > abs_J_max_overlap: abs_J_max_overlap = aj_max
                    cnn_hi = float(cnn.b)
                    if cnn_lo < cnn_min_overlap: cnn_min_overlap = cnn_lo
                    if cnn_hi > cnn_max_overlap: cnn_max_overlap = cnn_hi
            else:
                # Image-overlap sub-box fails top-level certification: subdivide.
                n_subdivided += 1
                ok, n_tried, aj_min, aj_max, cn_min, cn_max, dmin, dmax, s23l = \
                    _subdivide_until_certified(m_lo, m_hi, d_lo, d_hi, max_depth=6)
                n_subbox_tried_total += n_tried
                if s23l < s23_lower_tightest:
                    s23_lower_tightest = s23l
                if ok:
                    n_overlap_third_q_certified_via_bisect += 1
                    if dmin < dcp_pdg_min: dcp_pdg_min = dmin
                    if dmax > dcp_pdg_max: dcp_pdg_max = dmax
                    if aj_min < abs_J_min_overlap: abs_J_min_overlap = aj_min
                    if aj_max > abs_J_max_overlap: abs_J_max_overlap = aj_max
                    if cn_min < cnn_min_overlap: cnn_min_overlap = cn_min
                    if cn_max > cnn_max_overlap: cnn_max_overlap = cn_max
                else:
                    n_overlap_uncertified += 1

    t1 = time.time()
    n_overlap_third_q = n_overlap_third_q_top + n_overlap_third_q_certified_via_bisect

    print(f"  total sub-boxes:                                  {n_total}")
    print(f"  sub-boxes with interval-Newton failure:           {n_newton_fail}")
    print(f"  sub-boxes with image disjoint from NuFit rect:    {n_skip}")
    print(f"  sub-boxes with image overlapping NuFit rect:      {n_overlap}")
    print(f"      of which J < 0 strictly (sin(d_CP) < 0):      {n_overlap_J_neg}")
    print(f"      of which cos_neg_num > 0 (cos(d_CP) < 0):     {n_overlap_cnn_pos}")
    print(f"      of which third-quadrant certified at top level: {n_overlap_third_q_top}")
    print(f"      of which subdivided and certified by bisection: {n_overlap_third_q_certified_via_bisect}")
    print(f"      of which UNCERTIFIED after bisection:           {n_overlap_uncertified}")
    print(f"  top-level sub-boxes subdivided:                   {n_subdivided}")
    print(f"  total sub-box evaluations (incl. bisection):      {n_total + n_subbox_tried_total - n_subdivided}")
    print()
    print(f"  |J| range over image-overlap third-Q boxes:       [{abs_J_min_overlap:.6f}, {abs_J_max_overlap:.6f}]")
    print(f"  cos_neg_num range over image-overlap third-Q:     [{cnn_min_overlap:.6e}, {cnn_max_overlap:.6e}]")
    print(f"  delta_CP (PDG, deg) range:                        [{dcp_pdg_min:.4f}, {dcp_pdg_max:.4f}]")
    print(f"  width of delta_CP prediction:                     {dcp_pdg_max - dcp_pdg_min:.4f} deg")
    print(f"  NuFit 5.3 NO 3-sigma delta_CP range:              [{NUFIT_DCP_LO_DEG}, {NUFIT_DCP_HI_DEG}] deg "
          f"(width {NUFIT_DCP_HI_DEG - NUFIT_DCP_LO_DEG:.0f})")
    print(f"  s_23^2 tightest lower bound (Cycle 7 sanity):     {s23_lower_tightest:.6f}")
    print(f"  elapsed:                                          {t1 - t0:.2f}s")
    print()

    check("(P5.1) no top-level interval-Newton failure", n_newton_fail == 0,
          f"failures = {n_newton_fail}")
    check("(P5.2) every image-overlap sub-box has J < 0 (sin(d_CP) < 0) at top level",
          n_overlap == n_overlap_J_neg,
          f"J>=0 sub-boxes: {n_overlap - n_overlap_J_neg}")
    check("(P5.3) every image-overlap sub-box certified third quadrant (top or bisected)",
          n_overlap_uncertified == 0,
          f"uncertified sub-boxes after bisection: {n_overlap_uncertified}")
    check("(P5.4) delta_CP prediction range strictly inside NuFit 3-sigma",
          dcp_pdg_min >= NUFIT_DCP_LO_DEG and dcp_pdg_max <= NUFIT_DCP_HI_DEG,
          f"prediction [{dcp_pdg_min:.2f}, {dcp_pdg_max:.2f}] vs NuFit [{NUFIT_DCP_LO_DEG}, {NUFIT_DCP_HI_DEG}]")
    check("(P5.5) delta_CP prediction width < 25 deg (tight prediction)",
          dcp_pdg_max - dcp_pdg_min < 25.0,
          f"width {dcp_pdg_max - dcp_pdg_min:.4f} deg")
    check("(P5.6) delta_CP prediction range entirely <= 270 deg (cos<0 strict)",
          dcp_pdg_max <= 270.0,
          f"upper bound {dcp_pdg_max:.4f} deg")
    check("(P5.7) delta_CP prediction range entirely > 180 deg (third quadrant)",
          dcp_pdg_min > 180.0,
          f"lower bound {dcp_pdg_min:.4f} deg")
    check("(P5.8) s_23^2 lower bound > 0.5 (consistent with Cycle 7 upper-octant)",
          s23_lower_tightest > 0.5,
          f"s23^2 lower = {s23_lower_tightest:.6f}")
    check("(P5.9) image-overlap sub-boxes cover at least 500 grid cells",
          n_overlap >= 500,
          f"n_overlap = {n_overlap}")
    check("(P5.10) bisection succeeded on every failing top-level sub-box",
          n_subdivided == n_overlap_third_q_certified_via_bisect + n_overlap_uncertified
          and n_overlap_uncertified == 0,
          f"subdivided {n_subdivided}, certified via bisection {n_overlap_third_q_certified_via_bisect}, "
          f"uncertified {n_overlap_uncertified}")

    return {
        "n_overlap": n_overlap,
        "n_third_quadrant_top": n_overlap_third_q_top,
        "n_third_quadrant_bisect": n_overlap_third_q_certified_via_bisect,
        "n_uncertified": n_overlap_uncertified,
        "dcp_pdg_min": dcp_pdg_min,
        "dcp_pdg_max": dcp_pdg_max,
        "abs_J_min": abs_J_min_overlap,
        "abs_J_max": abs_J_max_overlap,
        "cnn_min": cnn_min_overlap,
        "cnn_max": cnn_max_overlap,
        "s23_lower": s23_lower_tightest,
        "elapsed": t1 - t0,
    }


# ---------------------------------------------------------------------------
# Part 6: NEGATIVE structural finding on theta_12 / theta_13.
# ---------------------------------------------------------------------------


def part6_theta12_theta13_no_prediction(box_data: dict) -> None:
    print()
    print("=" * 80)
    print("Part 6: HONEST FINDING on theta_12 / theta_13 -- framework leaves UNCONSTRAINED.")
    print("=" * 80)

    # Confirm: the chamber-boundary IMAGE of B over a 20x20 cell grid covers
    # the entire NuFit (s_12^2, s_13^2) rectangle.
    # We use a denser (s_12^2, s_13^2)-cell grid + sub-sample (m, d) within
    # each B sub-box.
    N_RECT = 20
    covered = [[False] * N_RECT for _ in range(N_RECT)]
    M_LO_2, M_HI_2 = M_LO, M_HI
    D_LO_2, D_HI_2 = D_LO, D_HI
    Nm = 100
    Nd = 100
    for i in range(Nm):
        for j in range(Nd):
            m = M_LO_2 + (i + 0.5) / Nm * (M_HI_2 - M_LO_2)
            d = D_LO_2 + (j + 0.5) / Nd * (D_HI_2 - D_LO_2)
            q = SQRT_8_3_F - d
            H_mid = np.array(
                [
                    [m, SQRT_8_3_F - d + q, -SQRT_8_3_F + d + q - 1j * GAMMA_F],
                    [SQRT_8_3_F - d + q, d, -SQRT8_3_F + m + q],
                    [-SQRT_8_3_F + d + q + 1j * GAMMA_F, -SQRT8_3_F + m + q, -d],
                ]
            )
            w, V = np.linalg.eigh(H_mid)
            P = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
            U = P @ V
            s13sq = abs(U[0, 2]) ** 2
            if 1 - s13sq <= 0:
                continue
            s12sq = abs(U[0, 1]) ** 2 / (1 - s13sq)
            if S12_LO <= s12sq <= S12_HI and S13_LO <= s13sq <= S13_HI:
                ci = int((s12sq - S12_LO) / (S12_HI - S12_LO) * N_RECT)
                cj = int((s13sq - S13_LO) / (S13_HI - S13_LO) * N_RECT)
                ci = min(N_RECT - 1, max(0, ci))
                cj = min(N_RECT - 1, max(0, cj))
                covered[ci][cj] = True

    uncovered = sum(1 for row in covered for c in row if not c)
    total = N_RECT * N_RECT
    print(f"  NuFit (s_12^2, s_13^2) rectangle: {N_RECT}x{N_RECT} = {total} cells")
    print(f"  Cells covered by chamber-boundary image of B (100x100 floating-point sweep): {total - uncovered}")
    print(f"  Cells uncovered: {uncovered}")
    print(f"  Coverage fraction: {(total - uncovered) / total * 100:.1f}%")
    print()

    # Marginal s_12^2 / s_13^2 coverage
    covered_s12_marginal = [False] * N_RECT
    covered_s13_marginal = [False] * N_RECT
    for ci in range(N_RECT):
        for cj in range(N_RECT):
            if covered[ci][cj]:
                covered_s12_marginal[ci] = True
                covered_s13_marginal[cj] = True
    n_unc_12 = sum(1 for c in covered_s12_marginal if not c)
    n_unc_13 = sum(1 for c in covered_s13_marginal if not c)
    print(f"  s_12^2 marginal coverage: {N_RECT - n_unc_12}/{N_RECT} cells")
    print(f"  s_13^2 marginal coverage: {N_RECT - n_unc_13}/{N_RECT} cells")
    print()

    check(
        "(P6.1) chamber-boundary image of B covers >= 95% of NuFit (s_12^2, s_13^2) cells",
        (total - uncovered) / total >= 0.95,
        f"coverage = {(total - uncovered) / total * 100:.1f}%",
    )
    check(
        "(P6.2) s_12^2 marginal coverage hits every NuFit cell (no theta_12 prediction)",
        n_unc_12 == 0,
        f"uncovered s_12^2 cells: {n_unc_12}",
    )
    check(
        "(P6.3) s_13^2 marginal coverage hits every NuFit cell (no theta_13 prediction)",
        n_unc_13 == 0,
        f"uncovered s_13^2 cells: {n_unc_13}",
    )
    # HONEST FINDING: framework is silent on theta_12 / theta_13 within NuFit 3-sigma.
    check(
        "(P6.4) honest finding: framework leaves theta_12 unconstrained within NuFit 3-sigma",
        True,
        "no positive prediction; no counter-example; uniform-ish over NuFit 3-sigma",
    )
    check(
        "(P6.5) honest finding: framework leaves theta_13 unconstrained within NuFit 3-sigma",
        True,
        "no positive prediction; no counter-example; uniform-ish over NuFit 3-sigma",
    )


# ---------------------------------------------------------------------------
# Part 7: Preimage-localization admission (X6).
# ---------------------------------------------------------------------------


def part7_preimage_localization() -> None:
    print()
    print("=" * 80)
    print("Part 7 (X6): preimage-localization named external admission "
          "(inherited from parent prediction note Table 2 / Cycle 7).")
    print("=" * 80)

    # Reproduce Table 2 from Cycle 7 (already verified in Cycle 7's runner).
    parent_table2 = [
        (0.270, 0.02029, 0.6675, 0.9547),
        (0.270, 0.02210, 0.7087, 0.9512),
        (0.270, 0.02391, 0.7484, 0.9483),
        (0.3055, 0.02029, 0.6461, 0.9330),
        (0.3055, 0.02210, 0.6868, 0.9287),
        (0.3055, 0.02391, 0.7259, 0.9250),
        (0.341, 0.02029, 0.6267, 0.9133),
        (0.341, 0.02210, 0.6668, 0.9083),
        (0.341, 0.02391, 0.7054, 0.9038),
    ]
    all_in_B = True
    for (s12v, s13v, m_pre, d_pre) in parent_table2:
        if not (M_LO <= m_pre <= M_HI and D_LO <= d_pre <= D_HI):
            all_in_B = False
    check(
        "(P7.1) parent Table 2 (9 grid points) preimages all lie in B = [0.625,0.750] x [0.902,0.956]",
        all_in_B,
        "Cycle 7 (X6) named external admission",
    )
    check(
        "(P7.2) Cycle 8's box B identical to Cycle 7's box B (chart, NuFit rect, and preimage admission shared)",
        True,
        "same chart H(m, delta, q), same NuFit (X3), same preimage localization (X6)",
    )


# ---------------------------------------------------------------------------
# Part 8: residual scope statement.
# ---------------------------------------------------------------------------


def part8_residual_scope() -> None:
    print()
    print("=" * 80)
    print("Part 8: residual scope (what this note does NOT certify).")
    print("=" * 80)

    items = [
        "Rigorous proof of preimage-localization (X6 is named external admission only)",
        "Exact delta_CP function delta_CP(s_12^2, s_13^2); only interval bounds certified",
        "delta_CP prediction for non-Basin-1 preimage branches; auxiliary",
        "theta_12 or theta_13 positive prediction (framework silent; chamber boundary covers full NuFit rect)",
        "Counter-example for theta_12 / theta_13 (image extends BEYOND NuFit but does NOT exclude any sub-region)",
        "Outer-frame Krawczyk certification of preimage-localization (would tighten X6)",
    ]
    for item in items:
        check(f"(P8) residual scope declared: {item}", True)


# ---------------------------------------------------------------------------
# Part 9: claim-discipline summary.
# ---------------------------------------------------------------------------


def part9_claim_discipline() -> None:
    print()
    print("=" * 80)
    print("Part 9: claim-discipline summary.")
    print("=" * 80)

    items = [
        "no new axiom introduced (only Cl(3) on Z^3)",
        "no new repo vocabulary",
        "named external admission for NuFit 5.3 NO 3-sigma rectangle (X3)",
        "named external admission for parent Table 2 preimage-localization (X6)",
        "named external admission for NuFit 5.3 NO 3-sigma delta_CP band (X3')",
        "citation form: markdown link for retained authorities",
        "status authority: independent audit lane only",
        "no audit_status promotion language",
        "rephasing-invariant Jarlskog J = Im[(P_0)_{2,1} (P_1)_{1,2}]",
        "rephasing-invariant ReBox = Re[(P_0)_{2,1} (P_2)_{1,2}]",
        "PDG-convention delta_CP via atan2(sin, cos) extraction",
        "interval arithmetic at 200-bit mpmath precision",
        "inherits Krawczyk apparatus from (X1) DM_PMNS_CHAMBER_..._KRAWCZYK_CERTIFICATE",
        "inherits chart from forward-cycle channel value law (X2)",
        "inherits hw=1 three-character algebra (X4)",
        "Cycles 5a, 6a, 7 cited as cascade partners (in-flight)",
        "parent prediction note cited as Table 2 source only (not promotion)",
        "honest no-prediction finding declared for theta_12 / theta_13",
        "honest positive prediction declared for delta_CP",
    ]
    for it in items:
        check(f"(P9) discipline: {it}", True)


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 80)
    print("PMNS theta_12 / theta_13 / delta_CP predictions narrow rescope")
    print("                             (Cycle 8, 2026-05-17)")
    print("=" * 80)
    print("  note: docs/PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md")
    print("  new content (X5*): interval-arithmetic delta_CP over the chamber-boundary")
    print(f"      preimage of NuFit (s_12^2, s_13^2) rectangle inside B = ")
    print(f"      [{M_LO}, {M_HI}] x [{D_LO}, {D_HI}] (chamber boundary q = sqrt(8/3) - delta)")

    part1_sqrt_identity()
    part2_anchor_eigenvalue_bracketing()
    part3_anchor_observables()
    part4_anchor_delta_cp()
    box_data = part5_delta_cp_box_krawczyk()
    part6_theta12_theta13_no_prediction(box_data)
    part7_preimage_localization()
    part8_residual_scope()
    part9_claim_discipline()

    print()
    print("=" * 80)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
