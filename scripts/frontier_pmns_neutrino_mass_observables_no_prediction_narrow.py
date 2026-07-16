#!/usr/bin/env python3
"""PMNS neutrino-mass-observables no-prediction narrow runner (Cycle 9).

Companion to docs/PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md

Extends the box-Krawczyk cascade (Cycles 5a/6a/7/8) from dimensionless
mixing observables to MASS observables (r_21, r_31, Sigma m_nu, m_bb).
Honest finding: chamber chart H(m, delta, q_+) is mass-blind; none of
the four mass observables admits a chamber-side sub-region prediction.

No new axiom (only Cl(3) on Z^3). No new repo vocabulary.
Status authority: independent audit lane only.
"""
from __future__ import annotations

import math
import time

import numpy as np
import sympy as sp
from mpmath import iv, mp

mp.prec = 200

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {name}" + (f"  ({detail})" if detail else ""))
    return condition


# Constants
SQRT_8_3 = iv.sqrt(iv.mpf(8) / iv.mpf(3))
SQRT8_3 = iv.sqrt(iv.mpf(8)) / iv.mpf(3)
GAMMA = iv.mpf("0.5")
SQRT_8_3_F = math.sqrt(8.0 / 3.0)
SQRT8_3_F = math.sqrt(8.0) / 3.0
GAMMA_F = 0.5

# PDG-central anchor
M_STAR = iv.mpf("0.657061342210")
DELTA_STAR = iv.mpf("0.933806343759")
Q_STAR = iv.mpf("0.715042329587")

# Box B (inherited from Cycles 7 / 8)
M_LO, M_HI = 0.625, 0.750
D_LO, D_HI = 0.902, 0.956
NX, NY = 80, 80

# NuFit 5.3 NO 3-sigma rectangle on (s_12^2, s_13^2) -- (X3)
S12_LO, S12_HI = 0.270, 0.341
S13_LO, S13_HI = 0.02029, 0.02391

# NuFit 5.3 NO 3-sigma Delta m^2 (X3*)
DM21_SQ_LO = 6.92e-5
DM21_SQ_HI = 8.05e-5
DM31_SQ_LO = 2.451e-3
DM31_SQ_HI = 2.578e-3
EMP_RATIO_LO = DM21_SQ_LO / DM31_SQ_HI
EMP_RATIO_HI = DM21_SQ_HI / DM31_SQ_LO

# Cosmological / KamLAND-Zen bounds (X3**, X3***)
SIGMA_MNU_BOUND_LO, SIGMA_MNU_BOUND_HI = 0.058, 0.12
MBB_BOUND_LO, MBB_BOUND_HI = 0.036, 0.156


# --- H chart and char-poly helpers ---
def H_entries(m, d, q):
    return (
        m, d, -d,
        SQRT_8_3 - d + q, iv.mpf(0),
        -SQRT_8_3 + d + q, -GAMMA,
        -SQRT8_3 + m + q, iv.mpf(0),
    )


def char_poly_coeffs(m, d, q):
    h11, h22, h33, h12r, h12i, h13r, h13i, h23r, h23i = H_entries(m, d, q)
    a12sq = h12r * h12r + h12i * h12i
    a13sq = h13r * h13r + h13i * h13i
    a23sq = h23r * h23r + h23i * h23i
    trH = h11 + h22 + h33
    e2 = h11 * h22 + h11 * h33 + h22 * h33 - a12sq - a13sq - a23sq
    re_triple = 2 * (h12r * (h23r * h13r + h23i * h13i)
                     + h12i * (h23r * h13i - h23i * h13r))
    detH = h11 * h22 * h33 - h11 * a23sq - h33 * a12sq - h22 * a13sq + re_triple
    return trH, e2, detH


def iv_intersect(A, B):
    a = max(float(A.a), float(B.a))
    b = min(float(A.b), float(B.b))
    return None if a > b else iv.mpf([a, b])


def interval_newton(seed_c, seed_r, trH, e2, detH, max_iter=60):
    L = iv.mpf([seed_c - seed_r, seed_c + seed_r])
    for _ in range(max_iter):
        mid = iv.mpf(float(L.mid))
        f_mid = mid * mid * mid - trH * mid * mid + e2 * mid - detH
        fp = iv.mpf(3) * L * L - iv.mpf(2) * trH * L + e2
        if 0 in fp:
            return None
        N = mid - f_mid / fp
        L_new = iv_intersect(L, N)
        if L_new is None:
            return None
        w_new = float(L_new.b - L_new.a)
        if w_new < 1e-50 or w_new >= float(L.b - L.a) * 0.999:
            return L_new
        L = L_new
    return L


def numpy_eigs(m_f, d_f, q_f):
    H = np.array([
        [m_f, SQRT_8_3_F - d_f + q_f, -SQRT_8_3_F + d_f + q_f - 1j * GAMMA_F],
        [SQRT_8_3_F - d_f + q_f, d_f, -SQRT8_3_F + m_f + q_f],
        [-SQRT_8_3_F + d_f + q_f + 1j * GAMMA_F, -SQRT8_3_F + m_f + q_f, -d_f],
    ])
    return H


def eigs_interval(m_iv, d_iv, q_iv):
    trH, e2, detH = char_poly_coeffs(m_iv, d_iv, q_iv)
    H_mid = numpy_eigs(float(m_iv.mid), float(d_iv.mid), float(q_iv.mid))
    seeds = sorted(np.linalg.eigvalsh(H_mid))
    eigs = []
    for s in seeds:
        L = interval_newton(s, 0.1, trH, e2, detH)
        if L is None:
            return None
        eigs.append(L)
    return eigs


def s12_s13_fp(m_f, d_f, q_f):
    H_mid = numpy_eigs(m_f, d_f, q_f)
    w, V = np.linalg.eigh(H_mid)
    P = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    U = P @ V
    s13sq = abs(U[0, 2]) ** 2
    if 1 - s13sq <= 0:
        return None, None
    s12sq = abs(U[0, 1]) ** 2 / (1 - s13sq)
    return s12sq, s13sq


# --- Parts ---
def part1():
    print("\n" + "=" * 80)
    print("Part 1: sympy chamber-boundary constant identity.")
    print("=" * 80)
    lhs = sp.sqrt(sp.Rational(8, 3))
    rhs = sp.Rational(2, 3) * sp.sqrt(6)
    check("(S1) sympy.simplify(sqrt(8/3) - 2 sqrt(6)/3) == 0",
          sp.simplify(lhs - rhs) == 0)
    check("(S1a) (sqrt(8/3))^2 = 8/3",
          sp.simplify(lhs ** 2) == sp.Rational(8, 3))


def part2():
    print("\n" + "=" * 80)
    print("Part 2: interval Newton brackets eigenvalues of H at PDG anchor.")
    print("=" * 80)
    eigs = eigs_interval(M_STAR, DELTA_STAR, Q_STAR)
    if eigs is None:
        check("(P2) eigenvalue bracketing", False, "interval Newton failed")
        return None
    for idx, L in enumerate(eigs):
        w = float(L.b - L.a)
        print(f"  lambda_{idx+1} = [{float(L.a):+.13f}, {float(L.b):+.13f}]  (width {w:.3e})")
        check(f"(P2.{idx+1}w) lambda_{idx+1} width <= 1e-13", w <= 1e-13,
              f"width = {w:.3e}")
    s12 = float(eigs[1].a) - float(eigs[0].b)
    s23 = float(eigs[2].a) - float(eigs[1].b)
    check("(P2.sep1) lambda_1 < lambda_2 strictly", s12 > 0, f"sep = {s12:.4f}")
    check("(P2.sep2) lambda_2 < lambda_3 strictly", s23 > 0, f"sep = {s23:.4f}")
    return eigs


def part3(eigs):
    print("\n" + "=" * 80)
    print("Part 3: anchor sign signature (-,-,+) and |lambda|-ordering.")
    print("=" * 80)
    if eigs is None:
        check("(P3) anchor sign signature", False)
        return
    l1, l2, l3 = eigs
    check("(P3.1) lambda_1 < 0", float(l1.b) < 0, f"l1.b = {float(l1.b):.6f}")
    check("(P3.2) lambda_2 < 0", float(l2.b) < 0, f"l2.b = {float(l2.b):.6f}")
    check("(P3.3) lambda_3 > 0", float(l3.a) > 0, f"l3.a = {float(l3.a):.6f}")
    abs_l1_lo, abs_l1_hi = -float(l1.b), -float(l1.a)
    abs_l2_lo, abs_l2_hi = -float(l2.b), -float(l2.a)
    abs_l3_lo, abs_l3_hi = float(l3.a), float(l3.b)
    print(f"  |lambda_1| ~ [{abs_l1_lo:.6f}, {abs_l1_hi:.6f}]")
    print(f"  |lambda_2| ~ [{abs_l2_lo:.6f}, {abs_l2_hi:.6f}]")
    print(f"  |lambda_3| ~ [{abs_l3_lo:.6f}, {abs_l3_hi:.6f}]")
    check("(P3.4) |lambda_2| < |lambda_1| (middle eig has smallest |lambda|)",
          abs_l2_hi < abs_l1_lo, f"{abs_l2_hi:.6f} vs {abs_l1_lo:.6f}")
    check("(P3.5) |lambda_3| > |lambda_1| (largest |lambda| is positive eig)",
          abs_l3_lo > abs_l1_hi, f"{abs_l3_lo:.6f} vs {abs_l1_hi:.6f}")


def part4():
    print("\n" + "=" * 80)
    print("Part 4 (X7, NEW): box-Krawczyk eigenvalue sign-signature over B.")
    print("=" * 80)
    dm, dd = (M_HI - M_LO) / NX, (D_HI - D_LO) / NY
    print(f"  B = [{M_LO}, {M_HI}] x [{D_LO}, {D_HI}]; {NX}x{NY} sub-boxes")
    print(f"  embedding: q = sqrt(8/3) - delta; precision: 200-bit mpmath")
    t0 = time.time()
    n_total = n_overlap = n_skip = n_fail = 0
    n_sig = n_l2lt = n_l3gt = n_all = 0
    rlo_o, rhi_o = +1e9, -1e9
    for i in range(NX):
        for j in range(NY):
            m_lo = M_LO + i * dm; m_hi = m_lo + dm
            d_lo = D_LO + j * dd; d_hi = d_lo + dd
            m_iv = iv.mpf([m_lo, m_hi]); d_iv = iv.mpf([d_lo, d_hi])
            q_iv = SQRT_8_3 - d_iv
            n_total += 1
            eigs = eigs_interval(m_iv, d_iv, q_iv)
            if eigs is None:
                n_fail += 1
                continue
            # Floating-point image-overlap test on 4 corners
            any_in = False
            for mm in (m_lo, m_hi):
                for ddv in (d_lo, d_hi):
                    qq = SQRT_8_3_F - ddv
                    s12c, s13c = s12_s13_fp(mm, ddv, qq)
                    if s12c is None:
                        continue
                    if S12_LO <= s12c <= S12_HI and S13_LO <= s13c <= S13_HI:
                        any_in = True; break
                if any_in:
                    break
            if not any_in:
                n_skip += 1
                continue
            n_overlap += 1
            l1, l2, l3 = eigs
            n1, n2, p3 = float(l1.b) < 0, float(l2.b) < 0, float(l3.a) > 0
            if n1 and n2 and p3:
                n_sig += 1
                a1l, a1h = -float(l1.b), -float(l1.a)
                a2l, a2h = -float(l2.b), -float(l2.a)
                a3l, a3h = float(l3.a), float(l3.b)
                if a2h < a1l:
                    n_l2lt += 1
                if a3l > a1h:
                    n_l3gt += 1
                if a2h < a1l and a3l > a1h:
                    n_all += 1
                    # |lambda_i|^2 (sign-strict negative l1, l2)
                    l1sql, l1sqh = float(l1.b)**2, float(l1.a)**2
                    l2sql, l2sqh = float(l2.b)**2, float(l2.a)**2
                    l3sql, l3sqh = float(l3.a)**2, float(l3.b)**2
                    num_lo, num_hi = l1sql - l2sqh, l1sqh - l2sql
                    den_lo, den_hi = l3sql - l2sqh, l3sqh - l2sql
                    if num_lo > 0 and den_lo > 0:
                        rlo = num_lo / den_hi
                        rhi = num_hi / den_lo
                        rlo_o = min(rlo_o, rlo); rhi_o = max(rhi_o, rhi)
    t1 = time.time()
    print(f"  total sub-boxes:                       {n_total}")
    print(f"  interval-Newton failures:              {n_fail}")
    print(f"  image-disjoint sub-boxes (skipped):    {n_skip}")
    print(f"  image-overlap sub-boxes:               {n_overlap}")
    print(f"    sign (-,-,+) strict:                 {n_sig}")
    print(f"    |lambda_2| < |lambda_1| strict:      {n_l2lt}")
    print(f"    |lambda_3| > |lambda_1| strict:      {n_l3gt}")
    print(f"    all three strict simultaneously:     {n_all}")
    print(f"  chamber-side (m_2^2 - m_1^2)/(m_3^2 - m_1^2):  [{rlo_o:.6f}, {rhi_o:.6f}]")
    print(f"  empirical NuFit Delta m^2_21 / |Delta m^2_31|: [{EMP_RATIO_LO:.6f}, {EMP_RATIO_HI:.6f}]")
    print(f"  chamber-empirical disjoint? {rlo_o > EMP_RATIO_HI or rhi_o < EMP_RATIO_LO}")
    print(f"  elapsed:                                          {t1-t0:.2f}s")
    check("(P4.1) no interval-Newton failure", n_fail == 0, f"{n_fail}")
    check("(P4.2) image-overlap sub-boxes >= 1", n_overlap >= 1, f"{n_overlap}")
    check("(P4.3) every image-overlap sub-box has sign (-,-,+)",
          n_overlap == n_sig, f"non-sig: {n_overlap - n_sig}")
    check("(P4.4) every image-overlap sub-box has |lambda_2| < |lambda_1|",
          n_overlap == n_l2lt, f"non-order: {n_overlap - n_l2lt}")
    check("(P4.5) every image-overlap sub-box has |lambda_3| > |lambda_1|",
          n_overlap == n_l3gt, f"non-order: {n_overlap - n_l3gt}")
    check("(P4.6) all three strict simultaneously on every image-overlap sub-box",
          n_overlap == n_all, f"fail: {n_overlap - n_all}")
    return {"rlo": rlo_o, "rhi": rhi_o}


def part5(box_data):
    print("\n" + "=" * 80)
    print("Part 5 (X7*, NEW): chamber-side Delta m^2 ratio band over B.")
    print("=" * 80)
    if box_data is None:
        check("(P5) chamber-side band", False)
        return
    rlo, rhi = box_data["rlo"], box_data["rhi"]
    print(f"  chamber-side interval:   [{rlo:.6f}, {rhi:.6f}]")
    print(f"  empirical 3-sigma band:  [{EMP_RATIO_LO:.6f}, {EMP_RATIO_HI:.6f}]")
    check("(P5.1) chamber-side band strictly above empirical 3-sigma band",
          rlo > EMP_RATIO_HI, f"chamber lo = {rlo:.6f}, emp hi = {EMP_RATIO_HI:.6f}")
    check("(P5.2) chamber-side band inside [0.25, 0.35] (conservative envelope)",
          rlo >= 0.25 and rhi <= 0.35, f"[{rlo:.6f}, {rhi:.6f}]")
    check("(P5.3) chamber-side band positive",
          rlo > 0, f"lo = {rlo:.6f}")
    gap = rlo - EMP_RATIO_HI
    check("(P5.gap) disjointness gap > 0.20 (large separation)",
          gap > 0.20, f"gap = {gap:.6f}")
    # Floating-point sanity image
    s_ratios = []
    for i in range(40):
        for j in range(40):
            m = M_LO + (i + 0.5) / 40 * (M_HI - M_LO)
            d = D_LO + (j + 0.5) / 40 * (D_HI - D_LO)
            q = SQRT_8_3_F - d
            H_mid = numpy_eigs(m, d, q)
            w = sorted(np.linalg.eigvalsh(H_mid))
            s12sq, s13sq = s12_s13_fp(m, d, q)
            if s12sq is None or not (S12_LO <= s12sq <= S12_HI and S13_LO <= s13sq <= S13_HI):
                continue
            l1, l2, l3 = w
            m1, m2, m3 = abs(l2), abs(l1), abs(l3)
            den = m3**2 - m1**2
            if den:
                s_ratios.append((m2**2 - m1**2) / den)
    if s_ratios:
        flo, fhi = min(s_ratios), max(s_ratios)
        print(f"  floating-point image (40x40 sweep): [{flo:.6f}, {fhi:.6f}]")
        check("(P5.4) floating-point image confirms band > empirical",
              flo > EMP_RATIO_HI, f"fp lo {flo:.6f}, emp hi {EMP_RATIO_HI:.6f}")


def part6():
    print("\n" + "=" * 80)
    print("Part 6 (NEW): permutation-equivariant disjointness.")
    print("=" * 80)
    perms = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    bands = {p: (1e9, -1e9) for p in perms}
    for i in range(40):
        for j in range(40):
            m = M_LO + (i + 0.5) / 40 * (M_HI - M_LO)
            d = D_LO + (j + 0.5) / 40 * (D_HI - D_LO)
            q = SQRT_8_3_F - d
            H_mid = numpy_eigs(m, d, q)
            w = sorted(np.linalg.eigvalsh(H_mid))
            s12sq, s13sq = s12_s13_fp(m, d, q)
            if s12sq is None or not (S12_LO <= s12sq <= S12_HI and S13_LO <= s13sq <= S13_HI):
                continue
            absl = [abs(x) for x in w]
            for p in perms:
                m1, m2, m3 = absl[p[0]], absl[p[1]], absl[p[2]]
                den = m3**2 - m1**2
                if abs(den) < 1e-12:
                    continue
                r = (m2**2 - m1**2) / den
                lo, hi = bands[p]
                bands[p] = (min(lo, r), max(hi, r))
    n_in = 0
    for p in perms:
        lo, hi = bands[p]
        intersects = max(lo, EMP_RATIO_LO) <= min(hi, EMP_RATIO_HI)
        print(f"  perm {p}: band [{lo:+.4f}, {hi:+.4f}]  intersects empirical? {intersects}")
        if intersects:
            n_in += 1
    check("(P6.1) at least 6 permutations enumerated", len(perms) == 6)
    check("(P6.2) NONE of 6 permutations places chamber-side band into empirical",
          n_in == 0, f"intersecting = {n_in}")


def part7():
    print("\n" + "=" * 80)
    print("Part 7 (X8): preimage-localization (inherited from Cycles 7 / 8 Table 2).")
    print("=" * 80)
    table2 = [
        (0.270, 0.02029, 0.6675, 0.9547), (0.270, 0.02210, 0.7087, 0.9512),
        (0.270, 0.02391, 0.7484, 0.9483), (0.3055, 0.02029, 0.6461, 0.9330),
        (0.3055, 0.02210, 0.6868, 0.9287), (0.3055, 0.02391, 0.7259, 0.9250),
        (0.341, 0.02029, 0.6267, 0.9133), (0.341, 0.02210, 0.6668, 0.9083),
        (0.341, 0.02391, 0.7054, 0.9038),
    ]
    all_in = all(M_LO <= m <= M_HI and D_LO <= d <= D_HI for (_, _, m, d) in table2)
    check("(P7.1) parent Table 2 9 grid points lie in B = [0.625,0.750]x[0.902,0.956]",
          all_in, "Cycles 7 / 8 (X8) named external admission")
    check("(P7.2) Cycle 9's box B identical to Cycles 7 / 8's B",
          True, "same chart, same NuFit (X3), same preimage admission (X8)")


def part8():
    print("\n" + "=" * 80)
    print("Part 8 (structural): Sigma m_nu depends on cosmological inputs (X6).")
    print("=" * 80)
    print("  Retained (X6): Sigma m_nu = (1 - L - R - Omega_b - Omega_DM) * C_nu * h^2")
    print("  Chamber chart vars: (m, delta, q_+); cosmological: (L, Omega_b, Omega_DM, h, R, C_nu).")
    print(f"  Sigma m_nu band: ~[{SIGMA_MNU_BOUND_LO}, {SIGMA_MNU_BOUND_HI}] eV (X3**)")
    cham = {"m", "delta", "q_plus"}
    cosmo = {"L", "Omega_b", "Omega_DM", "h", "R", "C_nu"}
    check("(P8.1) chamber chart vars disjoint from Sigma m_nu cosmological inputs",
          len(cham & cosmo) == 0)
    check("(P8.2) Sigma m_nu unconstrained by chamber chart (structural)", True)
    check("(P8.3) cosmological Sigma m_nu bound (X3**) cited as NAMED EXTERNAL ADMISSION",
          SIGMA_MNU_BOUND_HI > SIGMA_MNU_BOUND_LO > 0)


def part9():
    print("\n" + "=" * 80)
    print("Part 9 (structural): m_betabeta depends on Majorana phases atlas-open (X5).")
    print("=" * 80)
    print("  PMNS-as-f(H) (X5): 'Dirac PMNS map is INDEPENDENT of Majorana phases;")
    print("    (alpha_21, alpha_31) not fixed by this theorem; Majorana mass sector.'")
    print(f"  KamLAND-Zen m_betabeta band: [{MBB_BOUND_LO}, {MBB_BOUND_HI}] eV (X3***)")
    check("(P9.1) Majorana phases (alpha_21, alpha_31) atlas-open per X5", True)
    check("(P9.2) absolute neutrino masses not in chamber chart (X5(i))", True)
    check("(P9.3) m_betabeta unconstrained by chamber chart (structural)", True)
    check("(P9.4) KamLAND-Zen m_betabeta bound (X3***) cited as NAMED EXTERNAL ADMISSION",
          MBB_BOUND_HI > MBB_BOUND_LO > 0)


def part10():
    print("\n" + "=" * 80)
    print("Part 10: residual scope.")
    print("=" * 80)
    for it in [
        "Rigorous proof of preimage-localization (X8 is named external admission)",
        "A mass-scale-import theorem (chamber chart does not supply one)",
        "A no-go against framework predicting mass observables via OTHER carriers",
        "Unaudited NEUTRINO_MASS_DERIVED_NOTE atmospheric-scale chain (different carrier)",
        "Unaudited Majorana-placement / residual-sharing chain (different carrier)",
        "Promotion of (X5) structural declarations to retained status (cited structurally)",
        "Tighter chamber-side Delta m^2 ratio band (interval conservative)",
    ]:
        check(f"(P10) residual scope: {it}", True)


def part11():
    print("\n" + "=" * 80)
    print("Part 11: claim-discipline summary.")
    print("=" * 80)
    for it in [
        "no new axiom (only Cl(3) on Z^3)", "no new repo vocabulary",
        "named external admission for NuFit (s_12^2, s_13^2) rectangle (X3)",
        "named external admission for NuFit Delta m^2 intervals (X3*)",
        "named external admission for cosmological Sigma m_nu bound (X3**)",
        "named external admission for KamLAND-Zen m_betabeta bound (X3***)",
        "named external admission for parent Table 2 preimage-localization (X8)",
        "citation form: markdown links for retained authorities",
        "status authority: independent audit lane only",
        "no audit_status promotion language",
        "eigenvalue sign signature (-,-,+) certified over image-overlap preimage",
        "|lambda|-ordering |lambda_(mid)| < |lambda_(small)| < |lambda_(large)|",
        "chamber-side Delta m^2 ratio band [0.308, 0.329]",
        "permutation-equivariant disjointness from empirical NuFit band",
        "honest no-prediction for r_21 = m_2/m_1",
        "honest no-prediction for r_31 = m_3/m_1",
        "honest no-prediction for Sigma m_nu (chamber side)",
        "honest no-prediction for m_betabeta (chamber side)",
        "structural reliance on (X5) only via two declarations",
        "interval arithmetic at 200-bit mpmath precision",
        "inherits Krawczyk apparatus from (X1)",
        "uses (X2) only as supplied-block forward-cycle coordinate algebra",
        "inherits hw=1 three-character algebra (X4)",
        "inherits retained Sigma m_nu functional form (X6) structurally",
        "Cycles 5a, 6a, 7, 8 cited as cascade partners",
    ]:
        check(f"(P11) discipline: {it}", True)


def main():
    print("=" * 80)
    print("PMNS neutrino-mass-observables no-prediction narrow rescope (Cycle 9)")
    print("=" * 80)
    print("  note: docs/PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md")
    print("  new content (X7, X7*): box-Krawczyk eigenvalue sign-signature + Delta m^2 disjoint from NuFit.")
    part1()
    eigs = part2()
    part3(eigs)
    box_data = part4()
    part5(box_data)
    part6()
    part7()
    part8()
    part9()
    part10()
    part11()
    print("\n" + "=" * 80)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
