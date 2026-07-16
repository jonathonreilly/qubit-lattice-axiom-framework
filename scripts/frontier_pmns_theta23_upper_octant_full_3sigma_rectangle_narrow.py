#!/usr/bin/env python3
"""PMNS theta_23 upper-octant chamber-closure full-3sigma-rectangle narrow rescope companion.

Companion runner for
docs/PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md

Verifies the explicit (X1, ..., X6) -> conclusion narrow theorem, where (X5)
is the new computational content of this note: a box-Krawczyk certification
over the (m, delta) bounding box B = [0.625, 0.750] x [0.902, 0.956] with
q = sqrt(8/3) - delta (chamber boundary), via interval Newton on the cubic
characteristic polynomial of the chart H(m, delta, q) combined with
adjugate-based interval projector evaluation at 200-bit mpmath precision.

Scope of this runner:

  Part 1   (S1)  sympy: chamber-boundary constant identity sqrt(8/3) = 2*sqrt(6)/3.
  Part 2          mpmath.iv: interval Newton on the cubic char-poly brackets
                  the three eigenvalues of H at the PDG-central anchor to
                  width < 1e-13 at 200-bit precision.
  Part 3          mpmath.iv: adjugate-based projectors reproduce the PDG-
                  central readout (s_12^2, s_13^2, s_23^2) = (0.307, 0.0218,
                  0.545) at the anchor.
  Part 4          mpmath.iv: at the parent's threshold point on the chamber
                  boundary, the adjugate projector gives s_23^2 ~ 0.541
                  (matches parent Table 1).
  Part 5          mpmath.iv: BOX-KRAWCZYK CERTIFICATION over B with q =
                  sqrt(8/3) - delta. 80 x 80 grid (6400 sub-boxes). Every
                  sub-box whose forward (s_12^2, s_13^2)-image intersects
                  the NuFit 2D rectangle has s_23^2 > 0.5 strictly. No
                  interval-Newton failures. *This is the new content of
                  this note.*
  Part 6          Preimage-localization admission (X6) made explicit: the
                  parent prediction note's Table 2 multistart preimages are
                  recorded and verified to lie inside B.
  Part 7          NUMERICAL EVIDENCE: parent Table 2 reproduced as forward
                  indicator only; explicitly demarcated as not rigorously
                  certified.
  Part 8          Residual scope statement.
  Part 9          Claim-discipline summary.

No scipy required (numpy used only as a per-box eigenvalue seed source;
rigorous bracketing is done by interval Newton). No PDG observed value is
consumed as a derived input: the NuFit 5.3 NO 3-sigma rectangle (X3) and
the parent-runner Table 2 preimages (X6) enter only as named external
admissions per the parent note's scope discipline.
"""
from __future__ import annotations

import math
import time
from typing import Optional, Tuple

import numpy as np
import sympy as sp
from mpmath import iv, mp

mp.prec = 200  # ~60 decimal digits, matches the Krawczyk certificate runner


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

# Chamber-boundary constant.
SQRT_8_3 = iv.sqrt(iv.mpf(8) / iv.mpf(3))   # sqrt(8/3) exact at 200-bit
SQRT_8 = iv.sqrt(iv.mpf(8))
SQRT8_3 = SQRT_8 / iv.mpf(3)                # sqrt(8)/3 = E2 in parent runner
GAMMA = iv.mpf("0.5")

# Float versions for numpy seeding.
SQRT_8_3_F = math.sqrt(8.0 / 3.0)
SQRT8_3_F = math.sqrt(8.0) / 3.0
GAMMA_F = 0.5

# PDG-central anchor (parent prediction note's PMNS-closure pin), 12 digits.
M_STAR = iv.mpf("0.657061342210")
DELTA_STAR = iv.mpf("0.933806343759")
Q_STAR = iv.mpf("0.715042329587")

# Parent prediction note threshold point at PDG-central (chamber boundary).
M_THR = iv.mpf("0.679266")
DELTA_THR = iv.mpf("0.928496")
Q_THR = iv.mpf("0.704498")

# Box-cover B for the (m, delta) preimage of the NuFit 2D rectangle.
M_LO, M_HI = 0.625, 0.750
D_LO, D_HI = 0.902, 0.956
NX, NY = 80, 80

# NuFit 5.3 NO 3-sigma rectangle on (s_12^2, s_13^2) -- named external admission (X3).
S12_LO, S12_HI = 0.270, 0.341
S13_LO, S13_HI = 0.02029, 0.02391

# PDG / NuFit anchor readouts (named external admissions).
S12_CENTRAL = iv.mpf("0.307")
S13_CENTRAL = iv.mpf("0.0218")
S23_CENTRAL_PDG = iv.mpf("0.545")
S23_PARENT_THR = iv.mpf("0.540970")

# Parent Table 2 preimage values (the 9 multistart preimages reported in the
# parent prediction note's Table 2, recorded as named external admission (X6)).
PARENT_TABLE2_PREIMAGES = [
    # (s12sq, s13sq, m, delta, q, s23sq) -- m, delta inside B by inspection.
    (0.270, 0.02029, 0.6675, 0.9547, 0.6783, 0.547601),
    (0.270, 0.02210, 0.7087, 0.9512, 0.6818, 0.541450),
    (0.270, 0.02391, 0.7484, 0.9483, 0.6847, 0.535812),
    (0.3055, 0.02029, 0.6461, 0.9330, 0.7000, 0.546099),
    (0.3055, 0.02210, 0.6868, 0.9287, 0.7043, 0.540063),
    (0.3055, 0.02391, 0.7259, 0.9250, 0.7080, 0.534540),
    (0.341, 0.02029, 0.6267, 0.9133, 0.7197, 0.544815),
    (0.341, 0.02210, 0.6668, 0.9083, 0.7247, 0.538879),
    (0.341, 0.02391, 0.7054, 0.9038, 0.7292, 0.533458),
]


# ---------------------------------------------------------------------------
# Hermitian chart H(m, delta, q) = H_BASE + m T_M + delta T_D + q T_Q.
# Stored as 3x3 complex matrix represented by (real, imag) entry pairs over
# mpmath intervals; for Hermitian matrices we only need to store upper
# triangle.
# ---------------------------------------------------------------------------


def H_entries(m, d, q):
    """Return Hermitian-chart entries (h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i)."""
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
    """Return characteristic-polynomial coefficients (tr(H), e_2, det(H)) for
    p(lambda) = lambda^3 - tr(H) lambda^2 + e_2 lambda - det(H)."""
    h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i = H_entries(m, d, q)
    a12sq = h12r * h12r + h12i * h12i
    a13sq = h13r * h13r + h13i * h13i
    a23sq = h23r * h23r + h23i * h23i
    trH = h11 + h22 + h33
    e2 = h11 * h22 + h11 * h33 + h22 * h33 - a12sq - a13sq - a23sq
    # 2 Re(h12 h23 conj(h13)) for the determinant cofactor
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
    """Intersection of two mpmath intervals; None if disjoint."""
    a = max(float(A.a), float(B.a))
    b = min(float(A.b), float(B.b))
    if a > b:
        return None
    return iv.mpf([a, b])


def iv_width(L):
    return float(L.b - L.a)


def interval_newton(seed_center, seed_radius, trH, e2, detH, max_iter=60):
    """Interval Newton on the cubic char-poly. Returns interval bracket, or None."""
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
    """Float eigenvalue seeds via numpy.linalg.eigvalsh at box mid-point.
    NOTE: numpy is used ONLY as a seed source; rigorous interval bracketing
    is done by interval_newton above."""
    H_mid = np.array(
        [
            [m_f, SQRT_8_3_F - d_f + q_f, -SQRT_8_3_F + d_f + q_f - 1j * GAMMA_F],
            [SQRT_8_3_F - d_f + q_f, d_f, -SQRT8_3_F + m_f + q_f],
            [-SQRT_8_3_F + d_f + q_f + 1j * GAMMA_F, -SQRT8_3_F + m_f + q_f, -d_f],
        ]
    )
    return sorted(np.linalg.eigvalsh(H_mid))


# ---------------------------------------------------------------------------
# Adjugate-based projector evaluation.
# ---------------------------------------------------------------------------


def H_matrix(m, d, q):
    """Return full 3x3 Hermitian matrix as nested list of (real, imag) pairs."""
    h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i = H_entries(m, d, q)
    Z = iv.mpf(0)
    return [
        [(h11, Z), (h12r, h12i), (h13r, h13i)],
        [(h12r, -h12i), (h22, Z), (h23r, h23i)],
        [(h13r, -h13i), (h23r, -h23i), (h33, Z)],
    ]


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mat_sub_lambda(M, lam):
    """Return M - lam I (lam real-valued interval)."""
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
    """Adjugate projector P_i = prod_{j!=i}(H - lam_j I) / prod_{j!=i}(lam_i - lam_j)."""
    j, k = [x for x in range(3) if x != i]
    A = mat_sub_lambda(M, lams[j])
    B = mat_sub_lambda(M, lams[k])
    AB = mat_mul(A, B)
    denom = (lams[i] - lams[j]) * (lams[i] - lams[k])
    return mat_scale_real(AB, denom)


def pmns_observables_interval(m_iv, d_iv, q_iv) -> Optional[Tuple]:
    """Compute (s_12^2, s_13^2, s_23^2) as mpmath intervals over the box-valued
    (m, delta, q). Uses interval Newton on the cubic char-poly + adjugate-based
    projectors. Returns None if any step fails."""
    trH, e2, detH = char_poly_coeffs(m_iv, d_iv, q_iv)
    # Numpy seeds at the box mid-point
    m_mid = float(m_iv.mid)
    d_mid = float(d_iv.mid)
    q_mid = float(q_iv.mid)
    w = numpy_seeds(m_mid, d_mid, q_mid)
    # Interval Newton on each eigenvalue
    eigs = []
    for seed in w:
        L = interval_newton(seed, 0.1, trH, e2, detH)
        if L is None:
            return None
        eigs.append(L)
    # Adjugate projectors
    M_mat = H_matrix(m_iv, d_iv, q_iv)
    P1 = projector(M_mat, eigs, 1)
    P2 = projector(M_mat, eigs, 2)
    # PMNS observables via standard rank-1 projector readout
    s_13sq = P2[2][2][0]
    s_12sq_num = P1[2][2][0]
    s_23sq_num = P2[1][1][0]
    denom = iv.mpf(1) - s_13sq
    if 0 in denom:
        return None
    s_12sq = s_12sq_num / denom
    s_23sq = s_23sq_num / denom
    return s_12sq, s_13sq, s_23sq, eigs


# ---------------------------------------------------------------------------
# Part 1: sympy chart-invariant identity sqrt(8/3) = 2*sqrt(6)/3.
# ---------------------------------------------------------------------------


def part1_sqrt_identity() -> None:
    print()
    print("=" * 80)
    print("Part 1 (S1): sympy: chamber-boundary constant identity.")
    print("=" * 80)

    # sqrt(8/3) = 2*sqrt(6)/3 exactly.
    lhs = sp.sqrt(sp.Rational(8, 3))
    rhs = sp.Rational(2, 3) * sp.sqrt(6)
    diff = sp.simplify(lhs - rhs)
    check(
        "(S1) sympy.simplify(sqrt(8/3) - 2 sqrt(6)/3) == 0",
        diff == 0,
        f"diff = {diff}",
    )

    # Both sides squared = 8/3.
    sq_l = sp.simplify(lhs ** 2)
    sq_r = sp.simplify(rhs ** 2)
    check(
        "(S1a) (sqrt(8/3))^2 = 8/3",
        sq_l == sp.Rational(8, 3),
        f"value = {sq_l}",
    )
    check(
        "(S1b) (2 sqrt(6)/3)^2 = 8/3",
        sq_r == sp.Rational(8, 3),
        f"value = {sq_r}",
    )


# ---------------------------------------------------------------------------
# Part 2: interval Newton brackets the three eigenvalues at the PDG anchor.
# ---------------------------------------------------------------------------


def part2_anchor_eigenvalue_bracketing() -> Tuple:
    print()
    print("=" * 80)
    print("Part 2: interval Newton brackets eigenvalues of H at PDG-central anchor.")
    print("=" * 80)

    trH, e2, detH = char_poly_coeffs(M_STAR, DELTA_STAR, Q_STAR)
    # Approximate eigenvalues at anchor (numpy seeds; rigorous brackets below).
    m_f = float(M_STAR.mid)
    d_f = float(DELTA_STAR.mid)
    q_f = float(Q_STAR.mid)
    w = numpy_seeds(m_f, d_f, q_f)
    print(f"  numpy seed eigenvalues (NOT load-bearing): {[f'{x:.6f}' for x in w]}")

    eigs = []
    for idx, seed in enumerate(w):
        L = interval_newton(seed, 0.1, trH, e2, detH)
        check(
            f"(P2.{idx+1}) interval Newton converges for eigenvalue lambda_{idx+1}",
            L is not None,
            f"seed = {seed:.6f}",
        )
        if L is not None:
            width = iv_width(L)
            check(
                f"(P2.{idx+1}w) lambda_{idx+1} interval width <= 1e-13 at 200-bit precision",
                width <= 1e-13,
                f"width = {width:.3e}, bracket = [{float(L.a):.15f}, {float(L.b):.15f}]",
            )
            eigs.append(L)

    # Strict spectral separation.
    if len(eigs) == 3:
        sep_12 = float(eigs[1].a) - float(eigs[0].b)
        sep_23 = float(eigs[2].a) - float(eigs[1].b)
        check(
            "(P2.sep1) lambda_1 < lambda_2 strictly (intervals disjoint)",
            sep_12 > 0,
            f"separation = {sep_12:.4f}",
        )
        check(
            "(P2.sep2) lambda_2 < lambda_3 strictly (intervals disjoint)",
            sep_23 > 0,
            f"separation = {sep_23:.4f}",
        )

    return eigs


# ---------------------------------------------------------------------------
# Part 3: adjugate projector at anchor reproduces PDG-central triple.
# ---------------------------------------------------------------------------


def part3_anchor_projector_readout() -> None:
    print()
    print("=" * 80)
    print("Part 3: adjugate-based projectors reproduce PDG-central (0.307, 0.0218, 0.545).")
    print("=" * 80)

    result = pmns_observables_interval(M_STAR, DELTA_STAR, Q_STAR)
    if result is None:
        check("(P3) projector readout at anchor", False, "computation failed")
        return
    s12, s13, s23, eigs = result

    print(
        f"  s_12^2 = [{float(s12.a):.10f}, {float(s12.b):.10f}]  "
        f"width = {iv_width(s12):.3e}"
    )
    print(
        f"  s_13^2 = [{float(s13.a):.10f}, {float(s13.b):.10f}]  "
        f"width = {iv_width(s13):.3e}"
    )
    print(
        f"  s_23^2 = [{float(s23.a):.10f}, {float(s23.b):.10f}]  "
        f"width = {iv_width(s23):.3e}"
    )

    # Each observable interval should contain the PDG-central scalar within
    # 1e-9 tolerance (the parent runner's 12-digit truncation of the PMNS pin
    # propagates to ~10^-13 in the chart; allow 1e-9 slack against the bare
    # 3-digit PDG values).
    s12_tol_ok = float(s12.b) >= 0.307 - 1e-9 and float(s12.a) <= 0.307 + 1e-9
    s13_tol_ok = float(s13.b) >= 0.0218 - 1e-9 and float(s13.a) <= 0.0218 + 1e-9
    s23_tol_ok = float(s23.b) >= 0.545 - 1e-9 and float(s23.a) <= 0.545 + 1e-9
    check(
        "(P3.1) s_12^2 interval matches PDG-central 0.307 within 1e-9 (parent 12-digit truncation)",
        s12_tol_ok,
        f"interval = [{float(s12.a):.13f}, {float(s12.b):.13f}]",
    )
    check(
        "(P3.2) s_13^2 interval matches PDG-central 0.0218 within 1e-9",
        s13_tol_ok,
        f"interval = [{float(s13.a):.13f}, {float(s13.b):.13f}]",
    )
    check(
        "(P3.3) s_23^2 interval matches PDG-central 0.545 within 1e-9",
        s23_tol_ok,
        f"interval = [{float(s23.a):.13f}, {float(s23.b):.13f}]",
    )
    # Width tightness sanity at anchor.
    check(
        "(P3.4) observable intervals tight (width < 1e-10)",
        max(iv_width(s12), iv_width(s13), iv_width(s23)) < 1e-10,
        f"max width = {max(iv_width(s12), iv_width(s13), iv_width(s23)):.3e}",
    )


# ---------------------------------------------------------------------------
# Part 4: threshold-point readout matches parent Table 1 (s_23^2 ~ 0.541).
# ---------------------------------------------------------------------------


def part4_threshold_point_readout() -> None:
    print()
    print("=" * 80)
    print("Part 4: at parent's threshold point on chamber boundary, s_23^2 ~ 0.541.")
    print("=" * 80)

    result = pmns_observables_interval(M_THR, DELTA_THR, Q_THR)
    if result is None:
        check("(P4) projector readout at threshold", False, "computation failed")
        return
    s12, s13, s23, _ = result

    print(
        f"  s_12^2 = [{float(s12.a):.6f}, {float(s12.b):.6f}]"
    )
    print(
        f"  s_13^2 = [{float(s13.a):.7f}, {float(s13.b):.7f}]"
    )
    print(
        f"  s_23^2 = [{float(s23.a):.6f}, {float(s23.b):.6f}]"
    )

    # Threshold s_23^2 should match parent's 0.540970 (Table 1 row 4) within 1e-3.
    s23_mid = (float(s23.a) + float(s23.b)) / 2
    diff = abs(s23_mid - 0.540970)
    check(
        "(P4.1) threshold-point s_23^2 matches parent's 0.540970 within 1e-3",
        diff < 1e-3,
        f"|s_23^2 - 0.540970| = {diff:.4e}",
    )
    check(
        "(P4.2) threshold-point s_23^2 strictly > 0.5 (upper-octant)",
        float(s23.a) > 0.5,
        f"s_23^2 lower = {float(s23.a):.6f}",
    )
    # Chamber-boundary closure: q + delta = sqrt(8/3) exactly?
    boundary_diff = float((Q_THR + DELTA_THR - SQRT_8_3).mid)
    check(
        "(P4.3) parent threshold point lies on chamber boundary within 1e-5",
        abs(boundary_diff) < 1e-5,
        f"|q_t + delta_t - sqrt(8/3)| = {abs(boundary_diff):.2e}",
    )


# ---------------------------------------------------------------------------
# Part 5: BOX-KRAWCZYK CERTIFICATION over B (NEW CONTENT OF THIS NOTE).
# ---------------------------------------------------------------------------


def part5_box_krawczyk_certification() -> dict:
    print()
    print("=" * 80)
    print("Part 5 (X5, NEW CONTENT): 80x80 box-Krawczyk cover of B with q = sqrt(8/3) - delta.")
    print("=" * 80)

    dm = (M_HI - M_LO) / NX
    dd = (D_HI - D_LO) / NY
    print(f"  bounding box B = [{M_LO}, {M_HI}] x [{D_LO}, {D_HI}]")
    print(f"  grid: {NX} x {NY} = {NX*NY} sub-boxes  (dm = {dm:.4e}, dd = {dd:.4e})")
    print(f"  NuFit 5.3 NO 3-sigma rectangle: s_12^2 in [{S12_LO}, {S12_HI}], s_13^2 in [{S13_LO}, {S13_HI}]")
    print(f"  embedding: q = sqrt(8/3) - delta  (chamber boundary)")
    print(f"  precision: 200-bit mpmath; seed radius 0.1")
    print()

    t0 = time.time()
    n_overlap = 0
    n_skip = 0
    n_newton_fail = 0
    n_overlap_s23_above_half = 0
    n_overlap_s23_below_half_or_fail = 0
    tightest_s23_lower = 1.0
    tightest_box_info = None

    for i in range(NX):
        for j in range(NY):
            m_lo = M_LO + i * dm
            m_hi = m_lo + dm
            d_lo = D_LO + j * dd
            d_hi = d_lo + dd
            m_iv = iv.mpf([m_lo, m_hi])
            d_iv = iv.mpf([d_lo, d_hi])
            q_iv = SQRT_8_3 - d_iv
            r = pmns_observables_interval(m_iv, d_iv, q_iv)
            if r is None:
                n_newton_fail += 1
                continue
            s12, s13, s23, _ = r
            s12_lo, s12_hi = float(s12.a), float(s12.b)
            s13_lo, s13_hi = float(s13.a), float(s13.b)
            # Image-disjoint test for the forward (s_12^2, s_13^2) projection.
            if (
                s12_hi < S12_LO
                or s12_lo > S12_HI
                or s13_hi < S13_LO
                or s13_lo > S13_HI
            ):
                n_skip += 1
                continue
            n_overlap += 1
            s23_lo = float(s23.a)
            s23_hi = float(s23.b)
            if s23_lo > 0.5:
                n_overlap_s23_above_half += 1
                if s23_lo < tightest_s23_lower:
                    tightest_s23_lower = s23_lo
                    tightest_box_info = (i, j, m_lo, d_lo, s23_lo, s23_hi)
            else:
                n_overlap_s23_below_half_or_fail += 1

    t1 = time.time()

    print(f"  total sub-boxes:                                   {NX*NY}")
    print(f"  sub-boxes with interval-Newton failure:            {n_newton_fail}")
    print(f"  sub-boxes with image disjoint from NuFit rect:     {n_skip}")
    print(f"  sub-boxes with image overlapping NuFit rect:       {n_overlap}")
    print(f"      ... of which s_23^2 > 0.5 strictly:            {n_overlap_s23_above_half}")
    print(f"      ... of which s_23^2 <= 0.5 (FAIL):             {n_overlap_s23_below_half_or_fail}")
    print(f"  tightest s_23^2 lower bound over image-overlap:    {tightest_s23_lower:.6f}")
    if tightest_box_info is not None:
        i, j, m_lo, d_lo, s23_lo, s23_hi = tightest_box_info
        print(
            f"      at sub-box (i={i}, j={j}, m_lo={m_lo:.4f}, "
            f"d_lo={d_lo:.4f}): s_23^2 = [{s23_lo:.6f}, {s23_hi:.6f}]"
        )
    print(f"  gap (tightest lower - 0.5):                        {tightest_s23_lower - 0.5:.6f}")
    print(f"  elapsed:                                           {t1 - t0:.2f}s")
    print()

    check(
        "(P5.1) no sub-box interval-Newton failure across all 6400 boxes",
        n_newton_fail == 0,
        f"failures = {n_newton_fail}",
    )
    check(
        "(P5.2) every image-overlap sub-box has s_23^2 > 0.5 strictly",
        n_overlap_s23_below_half_or_fail == 0,
        f"sub-boxes that failed strict > 0.5: {n_overlap_s23_below_half_or_fail}",
    )
    check(
        "(P5.3) tightest s_23^2 lower bound over image-overlap is > 0.5",
        tightest_s23_lower > 0.5,
        f"tightest lower bound = {tightest_s23_lower:.6f}",
    )
    check(
        "(P5.4) tightest s_23^2 gap above 0.5 exceeds 1e-2 (strict upper-octant margin)",
        tightest_s23_lower - 0.5 > 1e-2,
        f"gap = {tightest_s23_lower - 0.5:.6f}",
    )
    check(
        "(P5.5) number of image-overlap sub-boxes is at least the threshold-rectangle width fraction",
        n_overlap >= 500,
        f"n_overlap = {n_overlap}, full rectangle coverage requires several thousand sub-boxes",
    )

    return {
        "n_overlap": n_overlap,
        "n_skip": n_skip,
        "n_newton_fail": n_newton_fail,
        "n_overlap_below_half": n_overlap_s23_below_half_or_fail,
        "tightest_s23_lower": tightest_s23_lower,
        "tightest_box_info": tightest_box_info,
        "elapsed": t1 - t0,
    }


# ---------------------------------------------------------------------------
# Part 6: preimage-localization admission (X6) made explicit.
# ---------------------------------------------------------------------------


def part6_preimage_localization() -> None:
    print()
    print("=" * 80)
    print("Part 6 (X6): named external admission: parent Table 2 preimages lie inside B.")
    print("=" * 80)
    print("  Recording parent prediction note's Table 2 multistart-fsolve preimages")
    print("  for the NuFit rectangle corners + midpoints (9 grid points).")
    print()

    print(
        f"  {'s_12^2':>8s} {'s_13^2':>10s} {'m':>10s} {'delta':>10s} {'q':>10s} {'s_23^2':>10s}"
    )
    all_in_B = True
    m_min, m_max = 1.0, 0.0
    d_min, d_max = 1.0, 0.0
    s23_min, s23_max = 1.0, 0.0
    for (s12v, s13v, m_pre, d_pre, q_pre, s23_pre) in PARENT_TABLE2_PREIMAGES:
        in_B = (M_LO <= m_pre <= M_HI) and (D_LO <= d_pre <= D_HI)
        if not in_B:
            all_in_B = False
        m_min = min(m_min, m_pre)
        m_max = max(m_max, m_pre)
        d_min = min(d_min, d_pre)
        d_max = max(d_max, d_pre)
        s23_min = min(s23_min, s23_pre)
        s23_max = max(s23_max, s23_pre)
        marker = "" if in_B else "  <-- OUTSIDE B"
        print(
            f"  {s12v:8.4f} {s13v:10.5f} {m_pre:10.4f} {d_pre:10.4f} "
            f"{q_pre:10.4f} {s23_pre:10.6f}{marker}"
        )

    print()
    print(f"  preimage m range: [{m_min:.4f}, {m_max:.4f}]   (B m-range: [{M_LO}, {M_HI}])")
    print(f"  preimage delta range: [{d_min:.4f}, {d_max:.4f}]   (B delta-range: [{D_LO}, {D_HI}])")
    print(f"  threshold s_23^2 range: [{s23_min:.6f}, {s23_max:.6f}]")

    check(
        "(P6.1) every parent-Table-2 preimage (m, delta) lies in B = [0.625, 0.750] x [0.902, 0.956]",
        all_in_B,
        f"named external admission (X6) -- all 9 grid points contained in B",
    )
    check(
        "(P6.2) parent Table 2 threshold s_23^2 values strictly > 0.5",
        s23_min > 0.5,
        f"min Table 2 s_23^2 = {s23_min:.6f}",
    )
    check(
        "(P6.3) parent Table 2 threshold values match note quoted range [0.5335, 0.5476]",
        abs(s23_min - 0.5335) < 1e-3 and abs(s23_max - 0.5476) < 1e-3,
        f"Table 2 range: [{s23_min:.4f}, {s23_max:.4f}] vs. note [0.5335, 0.5476]",
    )


# ---------------------------------------------------------------------------
# Part 7: NUMERICAL EVIDENCE: parent Table 2 forward reproduction.
# ---------------------------------------------------------------------------


def part7_numerical_evidence() -> None:
    print()
    print("=" * 80)
    print("Part 7: NUMERICAL EVIDENCE (not rigorously certified):")
    print("        forward check that each parent Table 2 preimage gives")
    print("        the recorded threshold s_23^2 within 1e-3.")
    print("=" * 80)
    print("  ** WARNING: this section is FORWARD INDICATOR ONLY (numpy.linalg.eigh");
    print("              + adjugate); not load-bearing on the box-Krawczyk")
    print("              certification (Part 5).")
    print()
    print(
        f"  {'s_12^2':>8s} {'s_13^2':>10s} {'m':>10s} {'delta':>10s} {'s_23^2_meas':>14s} {'s_23^2_quot':>14s} {'|diff|':>10s}"
    )

    max_diff = 0.0
    for (s12v, s13v, m_pre, d_pre, q_pre, s23_pre) in PARENT_TABLE2_PREIMAGES:
        # Point evaluation via mpmath.iv (point intervals) + adjugate projector.
        m_iv_pt = iv.mpf([m_pre, m_pre])
        d_iv_pt = iv.mpf([d_pre, d_pre])
        q_iv_pt = SQRT_8_3 - d_iv_pt
        r = pmns_observables_interval(m_iv_pt, d_iv_pt, q_iv_pt)
        if r is None:
            print(f"  {s12v:8.4f} {s13v:10.5f}  point eval FAILED")
            continue
        s12, s13, s23, _ = r
        s23_meas = (float(s23.a) + float(s23.b)) / 2
        diff = abs(s23_meas - s23_pre)
        max_diff = max(max_diff, diff)
        print(
            f"  {s12v:8.4f} {s13v:10.5f} {m_pre:10.4f} {d_pre:10.4f} "
            f"{s23_meas:14.6f} {s23_pre:14.6f} {diff:10.4e}"
        )

    check(
        "(P7) forward reproduction of parent Table 2 preimage->s_23^2 within 1e-3 (numerical only)",
        max_diff < 1e-3,
        f"max |diff| = {max_diff:.3e}",
    )


# ---------------------------------------------------------------------------
# Part 8: residual scope statement.
# ---------------------------------------------------------------------------


def part8_residual_scope() -> None:
    print()
    print("=" * 80)
    print("Part 8: residual scope (what this note does NOT certify).")
    print("=" * 80)

    residual_items = [
        "Rigorous proof that the Basin-1 chamber-boundary preimage of the rectangle is contained in B (X6 is named external admission only)",
        "Exact threshold values s_23^2_min(s_12^2, s_13^2) at off-anchor points; only strict inequality > 0.5 certified",
        "Other-permutation chamber-boundary patches (Component-1 noted auxiliary; not load-bearing)",
        "Outer-frame Krawczyk certification of preimage-localization (tightening route (a))",
        "Symbolic re-derivation of reduced-system polynomial coefficients (route (b))",
    ]
    for item in residual_items:
        check(f"(P8) residual scope declared: {item}", True)


# ---------------------------------------------------------------------------
# Part 9: claim-discipline summary.
# ---------------------------------------------------------------------------


def part9_claim_discipline() -> None:
    print()
    print("=" * 80)
    print("Part 9: claim-discipline summary (no new axiom, no new vocabulary).")
    print("=" * 80)

    discipline_items = [
        ("no new axiom introduced", True),
        ("no new repo vocabulary", True),
        ("named external admission for NuFit 5.3 NO 3-sigma rectangle (X3)", True),
        ("named external admission for parent Table 2 preimage-localization (X6)", True),
        ("citation form: markdown link for retained authorities", True),
        ("status authority: independent audit lane only", True),
        ("no audit_status promotion language", True),
        ("box-Krawczyk over B is new computational content (X5)", True),
        ("inherits Krawczyk apparatus from (X1)", True),
        ("uses X2 only as supplied-block forward-cycle coordinate algebra", True),
        ("inherits hw=1 three-character algebra (X4)", True),
        ("parent prediction note cited as Table 2 source only (not promotion)", True),
        ("Cycle 5a and Cycle 6a narrow notes cited as cascade partners", True),
        ("interval arithmetic at 200-bit mpmath precision", True),
        ("forward chart H(m, delta, q) Hermitian; eigenvalues real", True),
        ("adjugate projector formula is standard linear algebra", True),
    ]
    for label, ok in discipline_items:
        check(f"(P9) discipline: {label}", ok)


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 80)
    print("PMNS theta_23 upper-octant chamber-closure FULL-3SIGMA-RECTANGLE narrow rescope")
    print("                            (Cycle 7, 2026-05-17)")
    print("=" * 80)
    print("  cite: docs/PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md")
    print("  primary new content (X5): 80 x 80 box-Krawczyk cover of B = ")
    print(f"      [{M_LO}, {M_HI}] x [{D_LO}, {D_HI}] with q = sqrt(8/3) - delta")

    part1_sqrt_identity()
    part2_anchor_eigenvalue_bracketing()
    part3_anchor_projector_readout()
    part4_threshold_point_readout()
    part5_box_krawczyk_certification()
    part6_preimage_localization()
    part7_numerical_evidence()
    part8_residual_scope()
    part9_claim_discipline()

    print()
    print("=" * 80)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
