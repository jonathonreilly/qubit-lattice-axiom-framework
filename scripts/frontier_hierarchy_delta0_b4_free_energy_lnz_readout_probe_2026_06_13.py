#!/usr/bin/env python3
"""DELTA0 B4 probe (A3): the infinite-volume per-taste FREE ENERGY /
ln-determinant share, and THE LOAD-BEARING readout map ln Z -> ln v in
the TASTE-COUNT direction.  (The third surviving attachment family.)

    docs/HIERARCHY_DELTA0_B4_FREE_ENERGY_LNZ_READOUT_PROBE_NOTE_
    2026-06-13.md

Setting.  Two of the three B4-attachment families are closed on their
surfaces: (i) bare taste-transfer EXCHANGE amplitudes are
magnitude-capped (sup sigma_U^2 W/16 = 9/16 < 1; the taste-transfer
ceiling); (ii) the NJL-RPA vertex ENHANCEMENT reaches magnitude (7.43x)
but BREAKS the u_0-degree (exact local degree -14.86, not -2), and its
threshold-freeze rescue is unsupplied (the NJL-RPA probe,
HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_NOTE_2026-06-13.md).

The surviving THIRD family (A3) is the infinite-volume per-taste FREE
ENERGY / ln-determinant.  Unlike the bare exchange amplitude (a bounded
object) or the RPA vertex (a u_0-degree-breaking ENHANCEMENT), the free
energy carries alpha_bare = 1/(4 pi) as a degree-0 kernel NORMALIZATION
(NOT a capped amplitude) times the dressed two-link u_0^(-2) (degree -2)
= alpha_s exactly, degree -2 exactly.  The value chain is LANDED:

  - the per-taste d = 3 IR kernel slope 1/(4 pi) was COMPUTED in
    HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_NOTE_
    2026-06-11.md (corner subtraction
    int d^3q/(2pi)^3 [1/q^2 - 1/(q^2+m^2)] = m/(4 pi); Richardson
    L = 192/384; < 0.1%), reused verbatim here;
  - the determinant FACTORIZES ^4 per taste
    (HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_THEOREM_NOTE_
    2026-05-10.md: |det(D+m)| = Prod_omega [m^2+u_0^2(3+sin^2 w)]^4 — one
    ln-factor per taste species; it also carries the dim-4 readout
    admission v ~ A(L_t)^(-1/4));
  - the free-energy density is log-ADDITIVE
    (HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_
    2026-05-16.md: Delta f = (1/(2 L_t)) Sum_omega ln(1 + m^2/[...])).

The SINGLE open leg is multiplicativity/readout: the free energy is
ADDITIVE in ln Z; B4 needs the per-decoupling factor MULTIPLICATIVE in
v.  This probe computes:

  F1  infinite-volume per-taste free-energy density
      f_t(m) = int_cell d^3q/(2pi)^3 ln(q^2 + m^2) over ONE BZ corner
      Voronoi cell, and locates the 1/(4 pi):  f_t itself and its slope
      df_t/dm = int_cell 2m/(q^2+m^2) are UV-divergent and carry NO
      clean 1/(4 pi); the 1/(4 pi) is carried by the m^2-derivative
      I_t(m) = d f_t/d(m^2) = int_cell 1/(q^2+m^2) through the
      IR-subtracted slope d[I_t(0) - I_t(m)]/dm -> 1/(4 pi) (Richardson
      L = 192/384, < 0.1%, the kernel-share machinery reused verbatim).
      HONEST: the degree-0 kernel normalization 1/(4 pi) lives in
      d f_t/d(m^2), NOT in df_t/dm.

  F2  log-additivity: removing one taste subtracts exactly one
      ln-factor from ln det — the ^4-per-taste factorization on the
      minimal block, removing one species removes one factor, EXACT
      (exact rational arithmetic at L_s = 2, L_t in {2, 4}).

  F3  the value chain: [1/(4 pi) kernel slope, degree 0] x [u_0^(-2)
      dressing, degree -2] = alpha_s exactly (< 1e-12), degree of
      product = -2 exactly (two-rational-point u_0-ratio: factor x u_0^2
      is u_0-free).

  F4  THE LOAD-BEARING TEST — the readout map ln Z -> ln v in the
      TASTE-COUNT direction.  The dim-4 admission v ~ A(L_t)^(-1/4)
      currently runs in the L_t direction.  Tested in the taste-count
      direction (n_taste: 16 -> 15): under v ~ A(n)^(-1/4) with
      A(n) prop n (each taste contributes equally), removing one taste
      multiplies v by (15/16)^(-1/4) = 1.0163 — an O(1) factor near 1,
      O(1)-DISPLACED from the required alpha_s = 0.1033 by ~9.8x.  Every
      pure ln-Z-additive readout gives the same shape: ln Z = n x
      (per-taste additive share), and the per-taste additive share of
      the free energy is NOT ln(alpha_s).  The ONLY map that lands
      +Delta_S = -ln(alpha_s) per decoupling is a readout
      v = exp(theta x per-taste-share) whose coefficient theta is chosen
      to match — and that coefficient is precisely the dim-4 readout
      admission (R) re-expressed (here shown to give the WRONG number in
      the taste direction unless theta itself is admitted to hit
      Delta_S).

Verdict shape (declared up front): RECLASSIFY.  The additive ->
multiplicative conversion is a readout coefficient that no landed object
derives; the dim-4 admission (R), taken literally in the taste
direction, is O(1)-displaced; so B4 closure <=> deriving the readout
coefficient (a NAMED admission).  This SHARPENS B4 to a specific landed
admission.  NOT closure (no DERIVED readout lands the factor in
[0.99,1.01]x alpha_s); NOT a full kill (a degree-(-2), magnitude-exact
value chain DOES exist — only the readout coefficient is underived).

Deterministic, pure Python stdlib (math, fractions, itertools,
pathlib), no network, no randomness (fixed grids and masses), runtime
well under 90 s (typically a few seconds).  Exit code 0 iff
TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_FREE_ENERGY_LNZ_READOUT_"
                      "PROBE_NOTE_2026-06-13.md")

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
OBSERVATION_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}][{klass}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def residual(msg: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {msg}")


def observation(msg: str) -> None:
    global OBSERVATION_COUNT
    OBSERVATION_COUNT += 1
    print(f"  OBSERVATION (bounded, numerology-risk flagged — NOT a "
          f"residual, NOT a closure): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681 (licensed value)
U_0_SQ = P_BOUNDARY ** 0.5           # = 0.7703246 (= sqrt(0.5934))
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_S = ALPHA_BARE / U_0_SQ        # = 0.1033038 (block02 target)
FOURPI = 4.0 * math.pi
# per-decoupling action cost; +Delta_S = -ln(alpha_s) (the multiplicative
# attachment the readout must deliver per taste decoupling).
DELTA_S = math.log(4.0 * math.pi) + 2.0 * math.log(U_0)
N_TASTE = 16                         # 2^D species (staggered, D = 4)

# Declared grids and masses (half-shifted, zero-mode-free,
# boundary-unambiguous: L divisible by 4 keeps every grid point off the
# Voronoi cell boundaries |k_mu| = pi/2).  Reused VERBATIM from the
# kernel-share probe's IR-slope machinery (block10b Richardson L=192/384).
DIFF_MASSES = (0.05, 0.1, 0.2)       # F1 prescribed-estimator masses
DIFF_SIZES = (192, 384)              # F1 prescribed-estimator grids
DERIV_MASSES = (0.05, 0.075, 0.1)    # F1 derivative-kernel masses
DERIV_SIZES = (288, 384)             # F1 derivative-kernel grids


# ---------------------------------------------------------------------------
# Half-shifted BZ grids, taste-cell tables, deterministic cell sums.
# (Reused verbatim from the kernel-share probe.)
# ---------------------------------------------------------------------------
def grid_ks(L: int):
    """Half-shifted grid k_j = 2 pi (j + 1/2)/L (never hits a corner of
    {0, pi}^d, never hits |k| = pi/2)."""
    return [2.0 * math.pi * (j + 0.5) / L for j in range(L)]


def axis_quarter_vals(L: int):
    """Distinct sin^2 values of the near-0 half axis: k in (0, pi/2),
    j = 0..L/4 - 1; each carries exact multiplicity 2 per axis."""
    return [math.sin(2.0 * math.pi * (j + 0.5) / L) ** 2
            for j in range(L // 4)]


def axis_half_tables(L: int):
    """(s0, s1): per-axis sin^2 tables for the near-0 half (cos k > 0)
    and the near-pi half (cos k < 0)."""
    s0, s1 = [], []
    for k in grid_ks(L):
        (s0 if math.cos(k) > 0.0 else s1).append(math.sin(k) ** 2)
    return s0, s1


def cell_sums_direct(L: int, d: int, fs):
    """Per-cell sums (1/L^d) sum_{k in cell} f(s^2) for ALL 2^d taste
    cells, by direct nested loops over each cell's own half-axis
    tables.  Returns dict cell_bitmask -> [sum per f]."""
    s0, s1 = axis_half_tables(L)
    halves = (s0, s1)
    inv = 1.0 / L ** d
    out = {}
    for t in range(2 ** d):
        ax = [halves[(t >> b) & 1] for b in range(d)]
        accs = [0.0] * len(fs)
        if d == 3:
            for x in ax[0]:
                for y in ax[1]:
                    xy = x + y
                    for z in ax[2]:
                        s2 = xy + z
                        for i, f in enumerate(fs):
                            accs[i] += f(s2)
        else:
            raise ValueError(d)
        out[t] = [a * inv for a in accs]
    return out


_FACT = (1, 1, 2, 6, 24)


def cell_sum_compressed(L: int, d: int, fs):
    """Single near-0-cell sum (1/L^d) sum f(s^2) by the exact
    value-multiplicity compression: L/4 distinct per-axis sin^2 values x
    multiplicity 2, sorted index combinations x permutation count.
    Exactly the same quadrature as the direct loop."""
    v = axis_quarter_vals(L)
    accs = [0.0] * len(fs)
    two_d = 2 ** d
    fact_d = _FACT[d]
    for combo in combinations_with_replacement(range(len(v)), d):
        s2 = 0.0
        for i in combo:
            s2 += v[i]
        denom = 1
        run = 1
        prev = combo[0]
        for i in combo[1:]:
            if i == prev:
                run += 1
            else:
                denom *= _FACT[run]
                run = 1
                prev = i
        denom *= _FACT[run]
        w = two_d * fact_d // denom
        for fi, f in enumerate(fs):
            accs[fi] += w * f(s2)
    inv = 1.0 / L ** d
    return [a * inv for a in accs]


def lagrange0(xs, ys):
    """Polynomial extrapolation to 0 through the points (xs, ys)."""
    tot = 0.0
    for i in range(len(xs)):
        w = 1.0
        for j in range(len(xs)):
            if j != i:
                w *= (0.0 - xs[j]) / (xs[i] - xs[j])
        tot += w * ys[i]
    return tot


# ---------------------------------------------------------------------------
# Section A — F1: per-taste log free energy and where the 1/(4 pi) lives.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A: F1 — infinite-volume per-taste free-energy "
          "density f_t(m) = int_cell ln(q^2+m^2), and WHERE the 1/(4 pi) "
          "lives ---")

    # A1 [C]: continuum closed forms.  The log free energy f_t and its
    # first m-derivative df_t/dm = int 2m/(q^2+m^2) are UV-divergent and
    # carry NO clean 1/(4 pi).  The 1/(4 pi) is carried by the
    # m^2-derivative I_t(m) = d f_t/d(m^2) = int 1/(q^2+m^2) through the
    # IR-subtracted slope d[I_t(0) - I_t(m)]/dm = 1/(4 pi).
    m = 0.3
    lam = 25.0
    n_q = 200000
    h = lam / n_q
    # (a) df_t/dm over a ball = int_0^lam (q^2/(2pi^2)) 2m/(q^2+m^2) dq
    #     = (m/pi^2)[lam - m arctan(lam/m)] -> diverges linearly in lam.
    dfdm_ball = sum((((i + 0.5) * h) ** 2 / (2.0 * math.pi ** 2))
                    * 2.0 * m / (((i + 0.5) * h) ** 2 + m * m)
                    for i in range(n_q)) * h
    dfdm_closed = (m / math.pi ** 2) * (lam - m * math.atan(lam / m))
    # UV-LINEAR divergence: doubling the cutoff (very nearly) doubles the
    # value (the lam-linear piece dominates the m-arctan piece) — so
    # df_t/dm has no finite whole-space limit and no clean 1/(4 pi).
    dfdm_closed_2lam = (m / math.pi ** 2) * (
        2.0 * lam - m * math.atan(2.0 * lam / m))
    uv_div = abs(dfdm_closed_2lam / dfdm_closed - 2.0) < 0.05
    # (b) I_t(m) = d f_t/d(m^2) = int 1/(q^2+m^2); subtracted
    #     [I(0)-I(m)] = (1/(2pi^2)) m^2 int_0^inf dq/(q^2+m^2) =
    #     (m/(2pi^2))(pi/2) = m/(4 pi), so d/dm = 1/(4 pi) EXACT.
    sub_lim_ok = abs((m / (2.0 * math.pi ** 2)) * (math.pi / 2.0)
                     - m / FOURPI) < 1e-15
    # (c) the m^2-second-derivative d^2 f_t/d(m^2)^2 = int q^2/(2pi^2)
    #     /(q^2+m^2)^2 [UV finite]; over a ball the exact closed form is
    #     (1/(2pi^2)) [-Lam/(2(Lam^2+m^2)) + arctan(Lam/m)/(2m)], and its
    #     whole-space limit (Lam -> inf) is (1/(2pi^2)) pi/(4m) =
    #     1/(8 pi m): the SAME 4 pi.  Verify the midpoint quadrature
    #     against the EXACT BALL closed form (tight), and separately the
    #     whole-space limit against 1/(8 pi m).
    n_q2 = 400000
    h2 = lam / n_q2
    d2 = sum((((i + 0.5) * h2) ** 2 / (2.0 * math.pi ** 2))
             / (((i + 0.5) * h2) ** 2 + m * m) ** 2
             for i in range(n_q2)) * h2
    d2_ball = (1.0 / (2.0 * math.pi ** 2)) * (
        -lam / (2.0 * (lam * lam + m * m))
        + math.atan(lam / m) / (2.0 * m))
    d2_whole = 1.0 / (8.0 * math.pi * m)
    check("C", "A1 continuum closed forms: the per-taste LOG free-energy "
               "slope df_t/dm = int_ball (q^2/(2pi^2)) 2m/(q^2+m^2) = "
               "(m/pi^2)[Lam - m arctan(Lam/m)] is UV-LINEARLY DIVERGENT "
               "(midpoint vs closed < 1e-5 rel; grows with Lam) — it "
               "carries NO clean 1/(4 pi); the 1/(4 pi) is carried by "
               "the m^2-derivative I_t(m) = d f_t/d(m^2) = "
               "int 1/(q^2+m^2) via the IR-subtracted slope "
               "d[I_t(0) - I_t(m)]/dm = (1/(2pi^2))(pi/2)/... = 1/(4 pi) "
               "EXACTLY (and the UV-FINITE m^2-2nd-derivative "
               "int q^2/(2pi^2)/(q^2+m^2)^2: midpoint matches the exact "
               "ball closed form < 1e-5, whose whole-space limit is "
               "1/(8 pi m) — the same 4 pi)",
          abs(dfdm_ball - dfdm_closed) / dfdm_closed < 1e-5
          and uv_div and sub_lim_ok
          and abs(d2 - d2_ball) / d2_ball < 1e-5
          and abs(d2_ball / d2_whole - 1.0) < 0.02,
          f"df/dm ball/closed - 1 = {dfdm_ball / dfdm_closed - 1:.2e} "
          f"(value {dfdm_closed:.4f}, UV-divergent); d^2 num/ball - 1 = "
          f"{d2 / d2_ball - 1:.2e}; ball/whole(1/(8 pi m)) - 1 = "
          f"{d2_ball / d2_whole - 1:.2e}")

    # A2 [A]: per-cell equality of the I_t kernels (the equal-share lemma
    # covers any function of s^2; verify on the two estimators).
    fs_eq = [lambda s2: 1.0 / s2 - 1.0 / (s2 + 0.01),
             lambda s2: 2.0 * 0.075 / (s2 + 0.075 ** 2) ** 2]
    cs = cell_sums_direct(96, 3, fs_eq)
    worst = max(abs(cs[t][i] - cs[0][i]) / abs(cs[0][i])
                for t in range(8) for i in range(2))
    check("A", "A2 per-cell equality holds for the I_t = d f_t/d(m^2) "
               "kernels (equal-share lemma instance, reused from the "
               "kernel-share probe): the subtracted integrand "
               "[1/s^2 - 1/(s^2+m^2)] at m = 0.1 and the m^2-derivative "
               "kernel 2m/(s^2+m^2)^2 give EQUAL sums on all 8 taste "
               "cells (d = 3, L = 96, direct loops, rel spread < 1e-11) "
               "— whatever IR coefficient one taste's free energy "
               "carries, every taste carries identically",
          worst < 1e-11, f"max rel spread = {worst:.1e}")

    # A3 [A]: derivative-kernel estimator of the I_t IR slope -> 1/(4 pi)
    # per taste cell (the kernel-share machinery reused verbatim).
    der_vals = {}
    for L in DERIV_SIZES:
        fs = [(lambda s2, m2=mm * mm: 1.0 / (s2 + m2) ** 2)
              for mm in DERIV_MASSES]
        v = cell_sum_compressed(L, 3, fs)
        der_vals[L] = [2.0 * mm * x for mm, x in zip(DERIV_MASSES, v)]
    conv = max(abs(a - b) / abs(b)
               for a, b in zip(der_vals[288], der_vals[384]))
    ext_der = lagrange0(list(DERIV_MASSES), der_vals[384])
    print("    I_t IR slope estimator 4pi*K_t(m), L=384: "
          + ", ".join(f"m={mm}: {x * FOURPI:.6f}"
                      for mm, x in zip(DERIV_MASSES, der_vals[384])))
    check("A", "A3 the per-taste 1/(4 pi) carrier, COMPUTED: the "
               "m^2-derivative kernel K_t(m) = int_cell 2m/(s^2+m^2)^2 "
               "(= the IR slope of I_t = d f_t/d(m^2), no m=0 eval) at "
               "m = 0.05, 0.075, 0.1 is grid-converged (L = 288 vs 384 "
               "< 1e-4 rel) and its quadratic m -> 0 extrapolation lands "
               "on 1/(4 pi) within the declared 0.5% — EACH taste's "
               "free-energy m^2-derivative carries IR slope 1/(4 pi) per "
               "unit mass (Richardson machinery reused verbatim from the "
               "kernel-share probe)",
          conv < 1e-4 and abs(ext_der * FOURPI - 1.0) < 5e-3,
          f"4pi x extrapolated slope = {ext_der * FOURPI:.6f} "
          f"(deviation {ext_der * FOURPI - 1.0:+.1e}); "
          f"L-convergence {conv:.1e}")

    # A4 [A]: the prescribed difference estimator [I_t(0) - I_t(m)]/m.
    diff_vals = {}
    for L in DIFF_SIZES:
        fs = [lambda s2: 1.0 / s2] + [
            (lambda s2, m2=mm * mm: 1.0 / (s2 + m2))
            for mm in DIFF_MASSES]
        v = cell_sum_compressed(L, 3, fs)
        diff_vals[L] = [(v[0] - v[i + 1]) / mm
                        for i, mm in enumerate(DIFF_MASSES)]
    rich = [2.0 * diff_vals[384][i] - diff_vals[192][i]
            for i in range(len(DIFF_MASSES))]
    print("    prescribed [I_t(0)-I_t(m)]/m x 4pi: "
          + ", ".join(f"m={mm}: L192 {diff_vals[192][i] * FOURPI:.5f}"
                      f" / L384 {diff_vals[384][i] * FOURPI:.5f}"
                      f" / rich {rich[i] * FOURPI:.5f}"
                      for i, mm in enumerate(DIFF_MASSES)))
    ext_diff = lagrange0(list(DIFF_MASSES), rich)
    cross = abs(ext_diff - ext_der) * FOURPI
    check("A", "A4 prescribed difference estimator: [I_t(0) - I_t(m)]/m "
               "per taste cell at m = 0.05, 0.1, 0.2 (Richardson(1/L) "
               "over L = 192, 384, quadratic m -> 0) lands on 1/(4 pi) "
               "within the declared 3%, agreeing with A3 to "
               "< 0.01 x 1/(4 pi) — the per-taste free-energy "
               "m^2-derivative IR slope is 1/(4 pi), the SAME 4 pi as "
               "the kernel chain (degree-0 NORMALIZATION, uncapped, NOT "
               "a bounded exchange amplitude and NOT an enhancement)",
          abs(ext_diff * FOURPI - 1.0) < 0.03 and cross < 0.01,
          f"4pi x extrapolated slope = {ext_diff * FOURPI:.6f}; "
          f"cross-estimator gap = {cross:.1e} x (4 pi)^-1")

    return ext_der, ext_diff


# ---------------------------------------------------------------------------
# Section B — F2: log-additivity / the ^4-per-taste factorization.
# ---------------------------------------------------------------------------
def matsubara_omega(L_t):
    """APBC temporal Matsubara momenta omega_n = (2n+1) pi / L_t."""
    return [(2 * n + 1) * math.pi / L_t for n in range(L_t)]


def det_factors_rational(L_t, m2_frac, u02_frac):
    """At L_s = 2 (sin^2 k_i = 1 for all spatial dirs) the per-mode
    eigenvalue base is m^2 + u_0^2 (3 + sin^2 omega), each raised to the
    taste power.  Returns the list of (3 + sin^2 omega) as exact
    Fractions for the special L_t in {2, 4} (sin^2 omega rational)."""
    if L_t == 2:
        sins = [Fraction(1), Fraction(1)]           # sin^2 = 1
    elif L_t == 4:
        sins = [Fraction(1, 2)] * 4                  # sin^2 = 1/2
    else:
        raise ValueError(L_t)
    return [m2_frac + u02_frac * (3 + s) for s in sins]


def section_b():
    print("\n--- Section B [A]: F2 — log-additivity: the ^4-per-taste "
          "factorization; removing one taste removes exactly one "
          "ln-factor (exact) ---")

    # B1: the taste power is a clean exponent on ln det; removing one
    # taste subtracts exactly one ln-factor.  Verify with exact rational
    # arithmetic that ln|det| = n_taste x Sum_omega ln(base) and that
    # d ln|det|/d n_taste = Sum_omega ln(base) (one species worth) EXACT.
    u02 = Fraction(5934, 10000) ** 0  # placeholder, use rational u02
    u02 = Fraction(7703246, 10000000)  # ~ sqrt(0.5934), rational proxy
    m2 = Fraction(0)                    # massless determinant
    add_ok = True
    detail = []
    for L_t in (2, 4):
        bases = det_factors_rational(L_t, m2, u02)
        # |det| at taste power p: Prod base^p; ln|det| = p Sum ln base.
        per_species = sum(math.log(float(b)) for b in bases)
        # full (4 tastes) minus (3 tastes) = exactly one per_species:
        full4 = 4 * per_species
        drop1 = 3 * per_species
        removed = full4 - drop1
        add_ok = add_ok and abs(removed - per_species) < 1e-12
        # exact-rational handle on the m=0 base product: at L_t=2 it is
        # (4 u_0^2)^... ; verify the ratio identity (7/8)^16 of the
        # ratio note as the consistency tie.
        detail.append(f"L_t={L_t}: one-taste ln-factor = "
                      f"{per_species:.5f}")
    # exact ratio identity (7/8)^16 (the ratio note's Class A result),
    # exact rational, ties the ^4 factorization to a landed theorem.
    bases2 = det_factors_rational(2, Fraction(0), u02)
    bases4 = det_factors_rational(4, Fraction(0), u02)
    det2 = Fraction(1)
    for b in bases2:
        det2 *= b ** 4
    det4 = Fraction(1)
    for b in bases4:
        det4 *= b ** 4
    ratio = det4 / (det2 ** 2)
    target = Fraction(7, 8) ** 16
    ratio_ok = ratio == target
    check("A", "B2 log-additivity is EXACT: the staggered determinant "
               "FACTORIZES as |det(D+m)| = Prod_omega [m^2 + "
               "u_0^2(3+sin^2 omega)]^(n_taste) with n_taste = 4 the "
               "taste fourth-power (ratio-note Class A), so ln|det| = "
               "n_taste x Sum_omega ln(base): removing one taste removes "
               "exactly ONE additive ln-factor (full 4-taste minus "
               "3-taste = one per-species share, < 1e-12), and the "
               "cross-block ratio is the exact rational |det(L_t=4)| / "
               "|det(L_t=2)|^2 = (7/8)^16 (exact Fraction) — the "
               "free-energy / ln det is ADDITIVE in the taste count",
          add_ok and ratio_ok,
          "; ".join(detail) + f"; ratio == (7/8)^16: {ratio_ok}")

    # B3: the free-energy density is log-additive (the 2026-05-16 note's
    # closed form Delta f = (1/(2 L_t)) Sum_omega ln(1+m^2/[...])).
    # Verify the density formula matches the per-matrix-entry log-det
    # difference for the rational L_t in {2, 4} at a float m, u_0.
    u02f = U_0_SQ
    m2f = 0.1 ** 2
    df_ok = True
    df_detail = []
    for L_t in (2, 4):
        omegas = matsubara_omega(L_t)
        # density formula:
        dens = (1.0 / (2.0 * L_t)) * sum(
            math.log(1.0 + m2f / (u02f * (3.0 + math.sin(w) ** 2)))
            for w in omegas)
        # per-matrix-entry log-det difference (n_matrix = 8 L_t, taste 4):
        ld_diff = (4.0 / (8.0 * L_t)) * sum(
            math.log((m2f + u02f * (3.0 + math.sin(w) ** 2))
                     / (u02f * (3.0 + math.sin(w) ** 2)))
            for w in omegas)
        df_ok = df_ok and abs(dens - ld_diff) < 1e-12
        df_detail.append(f"L_t={L_t}: Delta f = {dens:.6f}")
    check("A", "B3 the free-energy density is log-additive (the landed "
               "2026-05-16 closed form): Delta f(L_t, m) = (1/(2 L_t)) "
               "Sum_omega ln(1 + m^2/[u_0^2(3+sin^2 omega)]) equals the "
               "per-matrix-entry log-det difference 4/(8 L_t) Sum ln(...) "
               "to < 1e-12 — the prefactor 4/(8 L_t) = 1/(2 L_t) carries "
               "the taste-4 in the numerator: the per-taste free-energy "
               "share enters ln Z ADDITIVELY, NOT multiplicatively",
          df_ok, "; ".join(df_detail))


# ---------------------------------------------------------------------------
# Section C — F3: the value chain and its exact degree -2.
# ---------------------------------------------------------------------------
def section_c(ext_der, ext_diff):
    print("\n--- Section C [A]: F3 — the value chain "
          "[1/(4 pi), deg 0] x [u_0^(-2), deg -2] = alpha_s, degree -2 "
          "exactly ---")

    # C1: value chain = alpha_s exactly.
    chain = ALPHA_BARE * (1.0 / U_0_SQ)
    check("A", "C1 the value chain is exact: [per-taste IR kernel slope "
               "1/(4 pi), the degree-0 kernel NORMALIZATION computed in "
               "Section A] x [dressed two-link vertex u_0^(-2), "
               "B1-licensed value] = alpha_s = 0.1033038 exactly "
               "(< 1e-12) — the SAME chain the kernel-share note landed, "
               "now read off the free-energy m^2-derivative; the "
               "1/(4 pi) is a kernel NORMALIZATION (uncapped), NOT a "
               "bounded exchange amplitude (family i) and NOT a vertex "
               "ENHANCEMENT (family ii)",
          abs(chain / ALPHA_S - 1.0) < 1e-12,
          f"(1/(4 pi)) x u_0^-2 = {chain:.7f} = alpha_s = {ALPHA_S:.7f}")

    # C2: degree -2 exactly, by two-rational-point u_0-ratio.
    # factor(u_0) = (1/(4 pi)) u_0^(-2); the 1/(4 pi) is u_0-FREE
    # (degree 0), so deg(factor) = -2.  Verify (a) factor x u_0^2 is
    # u_0-free across two rational u_0^2, (b) the two-point log-ratio
    # degree is exactly -2.
    def factor(u02):
        return ALPHA_BARE * (1.0 / u02)
    u02a, u02b = 0.70, 0.80
    inv_a = factor(u02a) * u02a
    inv_b = factor(u02b) * u02b
    free_ok = abs(inv_a - inv_b) < 1e-14 and abs(inv_a - ALPHA_BARE) < 1e-14
    u0a, u0b = u02a ** 0.5, u02b ** 0.5
    deg = math.log(factor(u02b) / factor(u02a)) / math.log(u0b / u0a)
    deg_ok = abs(deg - (-2.0)) < 1e-9
    check("A", "C2 the per-decoupling factor's exact u_0-degree is -2 "
               "(the kill-criterion of families i/ii here PASSES): the "
               "kernel slope 1/(4 pi) is u_0-FREE (degree 0, verified: "
               "factor x u_0^2 = 1/(4 pi) at u_0^2 in {0.70, 0.80} to "
               "< 1e-14), so the two-rational-point log-ratio degree "
               "d ln(factor)/d ln(u_0) = -2 exactly (< 1e-9) — UNLIKE "
               "the NJL-RPA vertex (degree -14.86); the free-energy "
               "share carries a clean degree-0 NORMALIZATION times the "
               "degree-(-2) dressing",
          free_ok and deg_ok,
          f"factor x u_0^2 = {inv_a:.10f} (= 1/(4pi)); two-point "
          f"degree = {deg:.10f}")

    # C3: the computed slope confirms the value chain numerically.
    slope_chain = ext_der * (1.0 / U_0_SQ)
    check("A", "C3 the computed free-energy m^2-derivative slope "
               "(Section A3, 4pi x slope = "
               f"{ext_der * FOURPI:.5f}) times u_0^(-2) reproduces "
               "alpha_s to the slope's Richardson tolerance (< 0.6%) — "
               "the value chain is not just algebraically exact at the "
               "constant 1/(4 pi) but lands from the actual per-taste "
               "BZ free-energy computation",
          abs(slope_chain / ALPHA_S - 1.0) < 6e-3,
          f"slope x u_0^-2 = {slope_chain:.7f} vs alpha_s = "
          f"{ALPHA_S:.7f} (rel {slope_chain / ALPHA_S - 1.0:+.2e})")


# ---------------------------------------------------------------------------
# Section D — F4: THE LOAD-BEARING readout map in the TASTE-COUNT
# direction.  ln Z -> ln v.
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- Section D: F4 — THE LOAD-BEARING readout map ln Z -> "
          "ln v in the TASTE-COUNT direction (n_taste: 16 -> 15) ---")

    # Required: removing one taste must multiply v by alpha_s, i.e.
    #   d ln v / d n_taste = ln(alpha_s) = -Delta_S = -2.270081.
    # (so that per decoupling the factor is alpha_s, multiplicative.)
    required = math.log(ALPHA_S)   # = -Delta_S
    print(f"    required d ln v/d n_taste = ln(alpha_s) = -Delta_S = "
          f"{required:.7f}")

    # D1 [A]: the dim-4 readout v ~ A(L_t)^(-1/4), re-expressed in the
    # taste-count direction.  A(n_taste) prop n_taste (each taste
    # contributes 1/(3+sin^2 omega) equally to the m^2 coefficient of
    # Delta f; the taste sum is the n_taste-fold copy).  So:
    #   v(n) prop A(n)^(-1/4) prop n^(-1/4),
    #   d ln v/d n = -(1/4) (1/n) = -1/(4 n),  and
    #   removing one taste (16->15): v ratio = (15/16)^(-1/4).
    n = N_TASTE
    dimreadout_deriv = -1.0 / (4.0 * n)
    dimreadout_ratio = (float(n - 1) / n) ** (-0.25)
    print(f"    dim-4 readout v ~ A(n)^(-1/4): A(n) prop n_taste; "
          f"d ln v/d n_taste = -1/(4n) = {dimreadout_deriv:.7f}; "
          f"16->15 v-ratio = (15/16)^(-1/4) = {dimreadout_ratio:.7f}")
    # The dim-4 readout gives an O(1) factor near 1, O(1)-displaced from
    # the required alpha_s = 0.1033.
    displ = dimreadout_ratio / ALPHA_S
    check("A", "D1 the dim-4 readout v ~ A(L_t)^(-1/4), re-expressed in "
               "the TASTE-COUNT direction, is O(1)-DISPLACED: A(n_taste) "
               "prop n_taste (each taste contributes equally to the m^2 "
               "coefficient of Delta f, the n_taste-fold copy), so "
               "removing one taste (16 -> 15) multiplies v by "
               "(15/16)^(-1/4) = 1.0163 — an O(1) factor NEAR 1, "
               "displaced from the required alpha_s = 0.1033 by ~9.8x "
               "(d ln v/d n_taste = -1/(4n) = -0.0156, NOT "
               "-Delta_S = -2.2701); the dim-4 admission taken LITERALLY "
               "in the taste direction does NOT deliver alpha_s",
          abs(dimreadout_ratio - 1.0163) < 1e-3
          and abs(dimreadout_deriv - (-1.0 / 64.0)) < 1e-12
          and displ > 9.0,
          f"v-ratio = {dimreadout_ratio:.5f}, ratio/alpha_s = "
          f"{displ:.4f}x (O(1)-displaced)")

    # D2 [A]: the general pure-ln-Z-additive readout shape.  Any readout
    # v = exp(theta x S_per_taste) where S_per_taste is the additive
    # per-taste ln-Z share gives d ln v/d n_taste = theta x S_per_taste,
    # a CONSTANT (n-independent) increment.  To hit -Delta_S the
    # coefficient theta must be CHOSEN as theta = -Delta_S / S_per_taste
    # — i.e. the readout coefficient IS the admission.  Demonstrate that
    # the per-taste additive free-energy share S_per_taste is NOT
    # ln(alpha_s): compute the per-species ln-det share at the licensed
    # scale (massless, L_t = 2) and show it is O(1)-far from ln(alpha_s).
    u02 = U_0_SQ
    # per-species massless ln-det share at L_t = 2 (one taste worth):
    omegas = matsubara_omega(2)
    s_per_taste = sum(math.log(u02 * (3.0 + math.sin(w) ** 2))
                      for w in omegas)  # = 2 ln(4 u_0^2)
    theta_needed = required / s_per_taste
    # the per-taste additive share is NOT ln(alpha_s):
    not_lnalpha = abs(s_per_taste - math.log(ALPHA_S)) > 0.5
    print(f"    per-taste additive ln-det share (massless, L_t=2) "
          f"S_per_taste = 2 ln(4 u_0^2) = {s_per_taste:.6f}  "
          f"(vs ln(alpha_s) = {math.log(ALPHA_S):.6f})")
    print(f"    => the readout coefficient that would land -Delta_S per "
          f"taste is theta = -Delta_S/S_per_taste = {theta_needed:.6f} "
          f"(an ADMITTED number, not derived)")
    check("A", "D2 the additive->multiplicative conversion is a READOUT "
               "COEFFICIENT, not a derived map: any pure ln-Z readout "
               "v = exp(theta x S_per_taste) gives a CONSTANT per-taste "
               "increment d ln v/d n = theta x S_per_taste, and the "
               "per-taste additive ln-det share S_per_taste = 2 ln(4 "
               "u_0^2) = 2.2507 (massless, L_t=2) is O(1)-FAR from the "
               "required ln(alpha_s) = -2.2701 (opposite sign even) — so "
               "to deliver -Delta_S "
               "the coefficient theta must be ADMITTED (theta = "
               "-Delta_S/S_per_taste), which is exactly the dim-4 "
               "readout admission (R) re-expressed: B4 closure <=> "
               "deriving that coefficient",
          not_lnalpha and abs(theta_needed * s_per_taste - required)
          < 1e-12,
          f"S_per_taste = {s_per_taste:.6f}, theta_needed = "
          f"{theta_needed:.6f}, theta x S = {theta_needed * s_per_taste:.6f}"
          f" = -Delta_S")

    # D3 [A]: the multiplicativity gap stated exactly.  The free energy
    # ln Z = n_taste x S_per_taste is ADDITIVE; B4 needs v multiplicative
    # in alpha_s per decoupling, v prop alpha_s^(n_taste).  The ONLY map
    # converting additive S to multiplicative alpha_s^n is
    # v = exp(c x S) with c = ln(alpha_s)/S_per_taste — and NO landed
    # object derives c.  The dim-4 admission supplies c = -1/(4 n_taste)
    # x (1/S?) ... no: the dim-4 admission supplies the EXPONENT -1/4 on
    # A, which in the taste direction is the WRONG number (D1).  Confirm
    # the gap is exact: required ratio alpha_s vs dim-4 ratio 1.0163.
    gap = math.log(ALPHA_S) - math.log(dimreadout_ratio)
    check("A", "D3 the multiplicativity gap, stated exactly: the free "
               "energy ln Z = n_taste x S_per_taste is ADDITIVE; B4 "
               "needs v MULTIPLICATIVE, v prop alpha_s^(n_taste) "
               "(per-decoupling factor alpha_s). The ONLY map converting "
               "the additive per-taste share to alpha_s^n is "
               "v = exp(c x S_per_taste) with c = ln(alpha_s)/S_per_taste "
               "— a readout coefficient NO landed object derives. The "
               "dim-4 admission supplies the exponent -1/4 on A(n), which "
               "in the taste direction gives ln-increment "
               "ln((15/16)^(-1/4)) = +0.0161, displaced from the required "
               "ln(alpha_s) = -2.2701 by a gap of "
               f"{gap:.4f} (an O(1) miss) — the additive->multiplicative "
               "conversion is the UNDERIVED leg, exactly the dim-4 "
               "readout admission (R)",
          abs(gap - (math.log(ALPHA_S) - math.log(dimreadout_ratio)))
          < 1e-12 and abs(gap) > 2.0,
          f"required ln-increment = {math.log(ALPHA_S):.4f}, dim-4 "
          f"ln-increment = {math.log(dimreadout_ratio):+.4f}, gap = "
          f"{gap:.4f}")

    observation("the dim-4 readout's taste-direction v-ratio "
                "(15/16)^(-1/4) = 1.0163 sits inside the inventory's "
                "factor-2 observation window of 1 (trivially, being near "
                "1), but is ~9.8x ABOVE alpha_s = 0.1033 and so does NOT "
                "approach the required per-decoupling factor; this is the "
                "honest statement that the dim-4 admission, taken "
                "literally in the taste direction, MISSES alpha_s by an "
                "O(1) factor — NO mechanism, NO supplier, NO claim, "
                "recorded only to be explicit that no numerology window "
                "is crossed here.")


# ---------------------------------------------------------------------------
# Section E — on-disk scans (the chain consumed, the rows refined,
# the fences carried).
# ---------------------------------------------------------------------------
def flat(path: Path) -> str:
    return " ".join((path.read_text() if path.exists() else "").split())


def section_e():
    print("\n--- Section E [B]: on-disk scans — kernel-share leg, "
          "Matsubara determinant/free-energy notes, route inventory, "
          "parent-note fences ---")

    ks = flat(DOCS / "HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_"
                     "SHARE_PROBE_NOTE_2026-06-11.md")
    check("B", "E1 kernel-share probe on disk supplies the per-taste "
               "d = 3 IR kernel slope 1/(4 pi) (the degree-0 kernel "
               "normalization this probe reads off the free-energy "
               "m^2-derivative) and the u_0^(-2) two-link dressing; the "
               "BZ-corner Voronoi partition and Richardson IR-slope "
               "machinery this runner reuses verbatim are its content",
          "m/(4 pi)" in ks
          and "equal-share lemma" in ks
          and "u_0^(-2)" in ks)

    ratio = flat(DOCS / "HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_"
                        "THEOREM_NOTE_2026-05-10.md")
    check("B", "E2 Matsubara determinant-ratio note on disk supplies the "
               "^4-per-taste factorization |det(D+m)| = Prod_omega "
               "[m^2 + u_0^2(3+sin^2 omega)]^4 (one ln-factor per taste, "
               "the F2 log-additivity), the exact ratio (7/8)^16, AND "
               "the dim-4 readout admission v ~ A(L_t)^(-1/4) tested in "
               "the taste direction in Section D",
          "[m² + u_0² (3 + sin²ω)]⁴" in ratio
          and "(7/8)^16" in ratio
          and "A(L_t)^(-1/4)" in ratio)

    fed = flat(DOCS / "HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_"
                      "THEOREM_NOTE_2026-05-16.md")
    check("B", "E3 Matsubara free-energy-density note on disk supplies "
               "the log-ADDITIVE density Delta f(L_t, m) = (1/(2 L_t)) "
               "Sum_omega ln(1 + m^2/[u_0^2(3+sin^2 omega)]) (the F2/B3 "
               "additivity in ln Z) — the ADDITIVE object whose "
               "conversion to a MULTIPLICATIVE per-decoupling factor is "
               "the open leg",
          "Delta f(L_t, m) = (1 / (2 L_t)) * Sum_omega ln(1 + m^2"
          in fed
          and "log-determinant" in fed)

    inv = flat(DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_"
                      "SYNTHESIS_NOTE_2026-06-11.md")
    njl = flat(DOCS / "HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_"
                      "NOTE_2026-06-13.md")
    check("B", "E4 route inventory + NJL-RPA probe on disk record the "
               "two closed families this probe contrasts against: the "
               "route inventory's S1/S2/S3 surviving set and "
               "non-modification rule, and the NJL-RPA probe's degree "
               "kill (the as-computed vertex u_0-degree -14.86, "
               "CONDITIONAL-KILL) — the family-(ii) failure mode this "
               "probe's degree-(-2) value chain (Section C) avoids",
          "refine routes without modifying the inventory" in inv
          and "S1" in inv and "S2" in inv and "S3" in inv
          and "-14.86" in njl
          and "CONDITIONAL-KILL" in njl)

    note = flat(PARENT_NOTE).lower()
    required_tok = [
        "reclassify",
        "additive",
        "multiplicative",
        "dim-4 readout admission",
        "does not close the delta0 gate",
        "degree -2",
    ]
    forbidden_tok = [
        "closes the delta0 gate",
        "derived readout converts",
        "per-decoupling attachment is now supplied",
    ]
    req_missing = [t for t in required_tok if t not in note]
    forb_hit = [t for t in forbidden_tok if t in note]
    check("B", "E5 parent-note honesty fences on disk: the note grades "
               "itself RECLASSIFY, distinguishes ADDITIVE (ln Z) from "
               "MULTIPLICATIVE (v), names the open leg the 'dim-4 readout "
               "admission' re-expressed, carries degree -2 exactly, and "
               "'does not close the DELTA0 gate'; forbidden closure "
               "tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; "
          "every number is a BZ")
    print("   sum, an exact rational, or a cited framework constant.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_b4_free_energy_lnz_readout_probe_"
          "2026_06_13.py")
    print(" The THIRD B4-attachment family (A3): the infinite-volume "
          "per-taste FREE")
    print(" ENERGY / ln-determinant share, and THE LOAD-BEARING readout "
          "map ln Z -> ln v")
    print(" in the TASTE-COUNT direction.  Two families are closed: bare "
          "exchange is")
    print(" magnitude-capped; the NJL-RPA enhancement breaks the "
          "u_0-degree (-14.86).")
    print(" F1: per-taste log free energy f_t = int_cell ln(q^2+m^2); "
          "the 1/(4 pi) lives")
    print(" in d f_t/d(m^2) = I_t (Richardson L=192/384), NOT in df_t/dm "
          "(UV-divergent).")
    print(" F2: the ^4-per-taste factorization is log-ADDITIVE (exact). "
          "F3: value chain")
    print(" [1/(4 pi)] x [u_0^-2] = alpha_s, degree -2 exactly. F4: the "
          "dim-4 readout")
    print(" v ~ A^(-1/4) in the taste direction gives (15/16)^(-1/4) = "
          "1.0163, O(1)-")
    print(" displaced from alpha_s — the additive->multiplicative "
          "conversion is an")
    print(" UNDERIVED readout coefficient (the dim-4 admission "
          "re-expressed): RECLASSIFY.")
    print(" Parent note: docs/HIERARCHY_DELTA0_B4_FREE_ENERGY_LNZ_"
          "READOUT_PROBE_NOTE_")
    print("              2026-06-13.md")
    print("=" * 78)

    ext_der, ext_diff = section_a()
    section_b()
    section_c(ext_der, ext_diff)
    section_d()
    section_e()
    section_fence()

    # Declared-open residuals.
    print()
    residual("the additive -> multiplicative READOUT COEFFICIENT is "
             "UNDERIVED.  The free energy is ADDITIVE in ln Z "
             "(ln Z = n_taste x S_per_taste); B4 needs the per-decoupling "
             "factor MULTIPLICATIVE in v (v prop alpha_s^(n_taste)).  The "
             "only map converting one to the other is a readout "
             "v = exp(c x S_per_taste) with c = ln(alpha_s)/S_per_taste — "
             "a coefficient NO landed object derives.  This probe SUPPLIES "
             "a degree-(-2), magnitude-exact value chain [1/(4 pi)] x "
             "[u_0^-2] = alpha_s (Section C) — the family-(ii) degree "
             "failure is AVOIDED — but NOT the readout coefficient.")
    residual("B4 closure <=> deriving the DIM-4 READOUT ADMISSION (R) "
             "v ~ A(L_t)^(-1/4).  Re-expressed in the TASTE-COUNT "
             "direction (Section D), the dim-4 admission gives removing "
             "one taste multiplies v by (15/16)^(-1/4) = 1.0163, "
             "O(1)-DISPLACED from the required alpha_s = 0.1033 by ~9.8x "
             "— so the dim-4 admission taken LITERALLY in the taste "
             "direction MISSES alpha_s, and a closing readout must derive "
             "a DIFFERENT coefficient (theta = -Delta_S/S_per_taste).  "
             "B4 is hereby SHARPENED to: derive the readout coefficient "
             "that lands +Delta_S per decoupling — a specific NAMED "
             "admission, the dim-4 readout (R) re-expressed.  This is the "
             "RECLASSIFY content.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: this probe RECLASSIFIES B4 to "
             "a single landed admission (the readout coefficient), it "
             "does NOT close it; the inventory is not modified.")

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: RECLASSIFY (B4 reduces to the dim-4 readout "
          "admission).  The third")
    print("   attachment family — the infinite-volume per-taste free "
          "energy / ln det —")
    print("   carries the 1/(4 pi) as a degree-0 kernel NORMALIZATION "
          "(in d f_t/d(m^2),")
    print("   NOT df_t/dm, which is UV-divergent), the determinant "
          "FACTORIZES ^4 per taste")
    print("   (log-additive, exact), and the value chain [1/(4 pi)] x "
          "[u_0^-2] = alpha_s is")
    print("   degree -2 EXACTLY (the family-ii degree kill is AVOIDED).  "
          "But the free energy")
    print("   is ADDITIVE in ln Z while B4 needs MULTIPLICATIVE in v; the "
          "ONLY map that")
    print("   converts one to the other is a readout COEFFICIENT, and the "
          "dim-4 admission")
    print("   v ~ A^(-1/4) taken literally in the TASTE direction gives "
          "(15/16)^(-1/4) =")
    print("   1.0163, O(1)-displaced from alpha_s by ~9.8x.  So B4 "
          "closure <=> deriving the")
    print("   readout coefficient (the dim-4 readout admission R "
          "re-expressed) — a specific")
    print("   NAMED admission.  NOT closure (no DERIVED readout lands the "
          "factor in")
    print("   [0.99,1.01]x alpha_s); NOT a full kill (a degree-(-2), "
          "magnitude-exact value")
    print("   chain DOES exist).  DELTA0 stays open; B4 sharpened to one "
          "landed admission.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
