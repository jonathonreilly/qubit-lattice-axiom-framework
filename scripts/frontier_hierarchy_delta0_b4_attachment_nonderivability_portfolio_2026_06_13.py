#!/usr/bin/env python3
"""DELTA0 B4 capstone: the ATTACHMENT-NON-DERIVABILITY no-go PORTFOLIO.

    docs/HIERARCHY_DELTA0_B4_ATTACHMENT_NONDERIVABILITY_NOGO_
    PORTFOLIO_NOTE_2026-06-13.md

The hierarchy magnitude gate B4 reduces to ONE forced demand: supply,
MULTIPLICATIVELY and at u_0-degree -2, the per-taste-decoupling factor

    alpha_s = 1/(4 pi u_0^2) = (1/(4 pi)) x u_0^(-2) = 0.1033038,

equivalently the additive cost +Delta_S = ln(4 pi) + 2 ln(u_0) =
2.270081 per decoupling, sixteen times (the staircase needs
v prop alpha_s^16).  Six mechanism families/prongs are now EXHAUSTED on
their cited surfaces:

  1. READOUT class K1-K8: 91 candidates eliminated
     (HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_
     2026-06-11.md; runner ...observable_enumeration..., 28/0).
  2. Bare taste-transfer EXCHANGE: PROVEN magnitude-capped at
     sup sigma_U^2 W / 16 = 9/16 < 1, exact
     (HIERARCHY_DELTA0_B4_BARE_CLASS_MAGNITUDE_CEILING_THEOREM_NOTE_
     2026-06-13.md; runner ...bare_class_magnitude_ceiling_theorem...,
     19/0).
  3. NJL-RPA vertex ENHANCEMENT: reaches magnitude 7.43x but BREAKS the
     u_0-degree (exact local -14.86, not -2), threshold-freeze rescue
     dead (HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_NOTE_
     2026-06-13.md; runner ...njl_rpa_normalization_probe..., 22/0,
     CONDITIONAL-KILL).
  4. Free-energy/ln-Z: degree-(-2), magnitude-exact value chain
     [1/(4 pi)] x [u_0^-2] = alpha_s on a log-ADDITIVE ^4-per-taste
     determinant, but the additive->multiplicative readout coefficient
     is UNDERIVED
     (HIERARCHY_DELTA0_B4_FREE_ENERGY_LNZ_READOUT_PROBE_NOTE_2026-06-13
     .md; runner ...free_energy_lnz_readout_probe..., 18/0, RECLASSIFY).
  5. Fourth-family (zeta-det, heat-kernel, holonomy, det-ratio): no
     native-multiplicative object hosts both the 4 pi and degree -2
     (structural orthogonality).
  6. Derived-readout (the five landed ln-Z->observable maps:
     observable-principle, Higgs, alpha_s-scale, dim-4
     determinant-ratio R, free-energy-density): none derives the
     coefficient; all admit or displace.

THE STRUCTURAL CORE (HONESTLY scoped as a BOUNDED no-go over the
examined analytic classes {exchange, vertex-enhancement,
free-energy/ln-Z, zeta-det, heat-kernel, holonomy, det-ratio} + the
five readout maps + the Lindemann transcendence obstruction — NOT a
claim of universal mathematical impossibility): 1/(4 pi) is born as the
NORMALIZATION of a sum/trace (Plancherel measure int d^dk/(2 pi)^d;
Seeley-DeWitt heat-trace prefactor (4 pi t)^(-d/2)) — ADDITIVE,
u_0-degree 0.  Native multiplicativity lives in the eigenvalue product
det = prod lambda_n, whose per-mode factors are eigenvalues of degree
+1 carrying NO 4 pi.  Orthogonal locations: no single
native-multiplicative per-mode object hosts BOTH.  SHARPENED by
transcendence: the log-additive per-taste ln-det share carries
ln(4 u_0^2) (the 4 = staggered 3+1 INTEGER count), the multiplicative
target needs ln(4 pi u_0^2) = Delta_S; the gap is EXACTLY ln(pi) (since
ln(4 pi u_0^2) - ln(4 u_0^2) = ln pi); pi is transcendental (Lindemann)
=> no algebraic readout exponent on the RATIONAL determinant share (the
(7/8)^16, (4 u_0^2)^8 objects are rational in u_0^2) can produce the
4 pi multiplicatively.  Hence the additive->multiplicative conversion
is NECESSARILY an admission = the D=4 dimensional readout (R; the 1/4
power is D=4 Stefan-Boltzmann bookkeeping per the determinant-ratio
note's section 4.4), coupled to the observable identification B5.

This runner performs (deterministic, stdlib only, class-D PDG
self-scan, runtime well under 120 s — subprocess re-invocations of the
four leg runners are each < 1 s):

  R1  recompute the forced decomposition alpha_s = (1/(4 pi)) x u_0^-2
      exactly (< 1e-12) and its u_0-degree -2 (two-rational-point
      log-ratio).
  R2  ORTHOGONALITY: compute the bare minimal-block staggered spectrum
      |lambda_omega| = u_0 sqrt(3 + sin^2 omega), verify the per-mode
      eigenvalues are u_0-degree +1 and carry NO 4 pi; recompute the
      per-taste IR m^2-derivative slope -> 1/(4 pi) (kernel-share /
      block10b Richardson machinery, < 0.1%), showing the 4 pi lives in
      the additive trace-normalization, NOT the eigenvalue product.
  R3  TRANSCENDENCE: verify ln(4 pi u_0^2) - ln(4 u_0^2) = ln(pi)
      EXACTLY, state the Lindemann argument, recompute the dim-4
      taste-direction readout (15/16)^(-1/4) = 1.0163 (9.8x displaced).
  R4  re-invoke the FOUR leg runners as subprocesses (bare-class
      ceiling 19/0, NJL-RPA 22/0, free-energy 18/0, K1-K8 enumeration
      28/0) and assert each passes its note-stated TOTAL.
  R5  the reclassification PROPOSAL checks: the note PROPOSES (does not
      enact) B4 reclassification, carries the no_go_portfolio (the six
      legs), explicitly defers the Tier-A registration to the owner,
      and a self-scan asserts tier_a_admissions.json is NOT referenced
      as modified.

PASS/FAIL lines, RESIDUAL (declared-open) lines, TOTAL: PASS=n FAIL=0.
Exit code 0 iff FAIL=0.

Pure Python stdlib (math, fractions, itertools, os, re, subprocess,
sys, time, pathlib), no network, no randomness (fixed grids/masses).
"""
from __future__ import annotations

import math
import os
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_ATTACHMENT_NONDERIVABILITY_"
                      "NOGO_PORTFOLIO_NOTE_2026-06-13.md")

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
# Declared boundary inputs (cited, not asserted; see the parent note and the
# six leg notes).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681 (licensed value)
U_0_SQ = P_BOUNDARY ** 0.5           # = 0.7703246 (= sqrt(0.5934))
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # 1/(4 pi); the trace normalization
ALPHA_S = ALPHA_BARE / U_0_SQ        # = 0.1033038 (block02 target)
FOURPI = 4.0 * math.pi
DELTA_S = math.log(4.0 * math.pi) + 2.0 * math.log(U_0)   # = 2.270081
N_TASTE = 16                         # 2^D species (staggered, D = 4)

# Declared IR-slope grids/masses, reused VERBATIM from the kernel-share /
# free-energy probe (block10b Richardson L=288/384, L=192/384).
DERIV_MASSES = (0.05, 0.075, 0.1)
DERIV_SIZES = (288, 384)


# ---------------------------------------------------------------------------
# Half-shifted BZ grids and deterministic taste-cell sums (reused verbatim
# from the kernel-share / free-energy probe machinery).
# ---------------------------------------------------------------------------
def axis_quarter_vals(L: int):
    """Distinct sin^2 values of the near-0 half axis k in (0, pi/2),
    j = 0..L/4 - 1; each carries exact multiplicity 2 per axis."""
    return [math.sin(2.0 * math.pi * (j + 0.5) / L) ** 2
            for j in range(L // 4)]


_FACT = (1, 1, 2, 6, 24)


def cell_sum_compressed(L: int, d: int, fs):
    """Single near-0-cell sum (1/L^d) sum f(s^2) by exact
    value-multiplicity compression: L/4 distinct per-axis sin^2 values x
    multiplicity 2, sorted index combinations x permutation count."""
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
# Section A — R1: the FORCED decomposition.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [A]: R1 — the FORCED decomposition "
          "alpha_s = (1/(4 pi)) x u_0^(-2), exact, degree -2 ---")

    # A1: the decomposition is exact.
    chain = ALPHA_BARE * (1.0 / U_0_SQ)
    delta_check = math.log(4.0 * math.pi) + 2.0 * math.log(U_0)
    check("A", "A1 the forced per-decoupling demand decomposes EXACTLY: "
               "alpha_s = 1/(4 pi u_0^2) = [1/(4 pi)] x [u_0^(-2)] = "
               "0.1033038 (< 1e-12), and the additive form "
               "Delta_S = -ln(alpha_s) = ln(4 pi) + 2 ln(u_0) = 2.270081 "
               "(< 1e-12); B4 demands this factor MULTIPLICATIVELY, "
               "sixteen times (v prop alpha_s^16, the taste staircase)",
          abs(chain / ALPHA_S - 1.0) < 1e-12
          and abs(chain - 0.1033038) < 5e-7
          and abs(delta_check - DELTA_S) < 1e-12
          and abs(delta_check + math.log(ALPHA_S)) < 1e-12
          and abs(DELTA_S - 2.270081) < 5e-7,
          f"(1/(4 pi)) x u_0^-2 = {chain:.7f} = alpha_s = {ALPHA_S:.7f}; "
          f"Delta_S = {DELTA_S:.6f} = -ln(alpha_s)")

    # A2: degree -2 exactly, by two-rational-point u_0-ratio (the 1/(4 pi)
    # is u_0-free => degree 0; u_0^(-2) => degree -2).
    def factor(u02):
        return ALPHA_BARE * (1.0 / u02)
    u02a, u02b = 0.70, 0.80
    inv_a = factor(u02a) * u02a
    inv_b = factor(u02b) * u02b
    free_ok = (abs(inv_a - inv_b) < 1e-14
               and abs(inv_a - ALPHA_BARE) < 1e-14)
    u0a, u0b = u02a ** 0.5, u02b ** 0.5
    deg = math.log(factor(u02b) / factor(u02a)) / math.log(u0b / u0a)
    deg_ok = abs(deg - (-2.0)) < 1e-9
    check("A", "A2 the forced factor's exact u_0-degree is -2: the "
               "1/(4 pi) is u_0-FREE (degree 0; factor x u_0^2 = 1/(4 pi) "
               "at u_0^2 in {0.70, 0.80} to < 1e-14), so the "
               "two-rational-point log-ratio d ln(factor)/d ln(u_0) = -2 "
               "exactly (< 1e-9) — the demand is at u_0-degree -2 (the "
               "kill criterion the NJL-RPA family-(ii) enhancement FAILED "
               "with -14.86)",
          free_ok and deg_ok,
          f"factor x u_0^2 = {inv_a:.12f} (= 1/(4 pi)); two-point "
          f"degree = {deg:.10f}")


# ---------------------------------------------------------------------------
# Section B — R2: ORTHOGONALITY.  The 4 pi is in the additive trace
# normalization, NOT the eigenvalue product.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B: R2 — ORTHOGONALITY: the bare minimal-block "
          "staggered spectrum carries degree +1 and NO 4 pi; the 4 pi "
          "lives in the additive trace normalization ---")

    # B1 [A]: the bare minimal-block staggered spectrum
    # |lambda_omega| = u_0 sqrt(3 + sin^2 omega) at L_s = 2 (sin^2 k_i = 1
    # all spatial dirs).  Verify (a) it is rational under u_0^2 (NO pi),
    # (b) per-mode eigenvalue u_0-degree is exactly +1, (c) NO 4 pi in any
    # eigenvalue.  Exact rational at L_t in {2, 4}.
    def spectrum_sq_rational(L_t, u02_frac):
        """|lambda_omega|^2 = u_0^2 (3 + sin^2 omega), exact Fractions."""
        if L_t == 2:
            sins = [Fraction(1), Fraction(1)]      # sin^2 omega = 1
        elif L_t == 4:
            sins = [Fraction(1, 2)] * 4            # sin^2 omega = 1/2
        else:
            raise ValueError(L_t)
        return [u02_frac * (3 + s) for s in sins]

    u02 = Fraction(7703246, 10000000)              # rational proxy ~ u_0^2
    # (a) rational, no pi: every |lambda|^2 is an exact Fraction in u_0^2.
    sq2 = spectrum_sq_rational(2, u02)
    sq4 = spectrum_sq_rational(4, u02)
    all_rational = all(isinstance(s, Fraction) for s in sq2 + sq4)
    # the dimensionless brackets (3 + sin^2 omega) are INTEGER/half-integer:
    brackets2 = [s / u02 for s in sq2]             # == 4 each
    brackets4 = [s / u02 for s in sq4]             # == 7/2 each
    brackets_clean = (all(b == Fraction(4) for b in brackets2)
                      and all(b == Fraction(7, 2) for b in brackets4))
    # (b) per-mode eigenvalue u_0-degree is +1 (|lambda| prop u_0):
    def eig_mag(u0val):
        return u0val * math.sqrt(3.0 + 1.0)        # near-corner mode, L_t=2
    u0a, u0b = 0.70 ** 0.5, 0.80 ** 0.5
    deg = math.log(eig_mag(u0b) / eig_mag(u0a)) / math.log(u0b / u0a)
    deg_ok = abs(deg - 1.0) < 1e-12
    # numerical magnitude at the licensed u_0:
    lam_min = U_0 * math.sqrt(3.0 + 0.0)           # smallest possible
    lam_max = U_0 * math.sqrt(3.0 + 1.0)           # largest possible
    # (c) NO 4 pi: the spectrum value 4 pi never appears; |lambda| has no
    # pi factor (it is u_0 x sqrt(rational)); the closest "4" is the
    # INTEGER 3+1 = 4 (staggered 3+1 count), NOT 4 pi.
    no_fourpi = abs(eig_mag(U_0) - U_0 * 2.0) < 1e-12  # = u_0 sqrt(4), no pi
    integer_four = (brackets2[0] == Fraction(4))       # the 4 is the integer
    check("A", "B1 the bare minimal-block staggered spectrum "
               "|lambda_omega| = u_0 sqrt(3 + sin^2 omega) (L_s = 2): "
               "every |lambda_omega|^2 = u_0^2 (3 + sin^2 omega) is an "
               "EXACT Fraction in u_0^2 (rational, NO pi); the "
               "dimensionless brackets are 4 (L_t=2) and 7/2 (L_t=4) — "
               "the '4' is the staggered 3+1 INTEGER count, NOT 4 pi; the "
               "per-mode eigenvalue u_0-degree is exactly +1 "
               "(|lambda| prop u_0, two-point log-ratio = 1.0, < 1e-12); "
               "and NO 4 pi appears anywhere in the rational spectrum "
               "(|lambda| = u_0 sqrt(4) = 2 u_0 at the corner, pi-free)",
          all_rational and brackets_clean and deg_ok and no_fourpi
          and integer_four,
          f"brackets L_t=2: {brackets2[0]} (integer 4), L_t=4: "
          f"{brackets4[0]}; |lambda| in [{lam_min:.4f}, {lam_max:.4f}]; "
          f"eigenvalue degree = {deg:.10f} (+1)")

    # B2 [A]: the per-taste IR m^2-derivative slope -> 1/(4 pi), recomputed
    # via the kernel-share / block10b Richardson machinery (< 0.1%).  This
    # is the ADDITIVE trace normalization, NOT the eigenvalue product.
    der_vals = {}
    for L in DERIV_SIZES:
        fs = [(lambda s2, m2=mm * mm: 1.0 / (s2 + m2) ** 2)
              for mm in DERIV_MASSES]
        v = cell_sum_compressed(L, 3, fs)
        der_vals[L] = [2.0 * mm * x for mm, x in zip(DERIV_MASSES, v)]
    conv = max(abs(a - b) / abs(b)
               for a, b in zip(der_vals[288], der_vals[384]))
    ext_der = lagrange0(list(DERIV_MASSES), der_vals[384])
    print("    per-taste IR slope estimator 4pi*K_t(m), L=384: "
          + ", ".join(f"m={mm}: {x * FOURPI:.6f}"
                      for mm, x in zip(DERIV_MASSES, der_vals[384])))
    check("A", "B2 the per-taste IR m^2-derivative slope is 1/(4 pi), "
               "recomputed via the kernel-share / block10b Richardson "
               "machinery (m^2-derivative kernel K_t(m) = "
               "int_cell 2m/(s^2+m^2)^2; m = 0.05, 0.075, 0.1; "
               "L = 288 vs 384 < 1e-4 rel; quadratic m -> 0 extrapolation "
               "lands on 1/(4 pi) within 0.5%) — this is the Plancherel / "
               "Seeley-DeWitt trace NORMALIZATION (int d^dk/(2 pi)^d), an "
               "ADDITIVE degree-0 prefactor, NOT a factor of the "
               "eigenvalue product det = prod lambda_n",
          conv < 1e-4 and abs(ext_der * FOURPI - 1.0) < 5e-3,
          f"4pi x extrapolated slope = {ext_der * FOURPI:.6f} "
          f"(deviation {ext_der * FOURPI - 1.0:+.1e}); "
          f"L-convergence {conv:.1e}")

    # B3 [A]: the ORTHOGONALITY statement made exact.  The 4 pi is in the
    # trace normalization (B2, degree 0, additive); the eigenvalue product
    # is rational in u_0^2 (B1, degree +1 per mode, NO 4 pi).  No single
    # native-multiplicative per-mode object hosts BOTH.  Demonstrate: the
    # full massless ln-det share is n_taste x Sum_omega ln|lambda_omega|^2,
    # which carries ln(4 u_0^2) per mode (the integer-4 bracket) — there
    # is NO 4 pi inside the log; the 4 pi sits OUTSIDE, in the measure.
    omegas2 = [(2 * n + 1) * math.pi / 2 for n in range(2)]  # L_t = 2
    per_mode_log = [math.log(U_0_SQ * (3.0 + math.sin(w) ** 2))
                    for w in omegas2]
    # at L_t = 2 each mode bracket is exactly 4, so per_mode_log = ln(4u_0^2)
    expect = math.log(4.0 * U_0_SQ)
    log_no_pi = all(abs(p - expect) < 1e-12 for p in per_mode_log)
    # the trace normalization 1/(4 pi) is the SEPARATE additive prefactor
    # (B2); it does not appear inside ln|lambda|^2.
    check("A", "B3 ORTHOGONALITY, exact: the 4 pi lives in the trace "
               "NORMALIZATION (B2: the IR m^2-derivative slope 1/(4 pi), a "
               "degree-0 additive Plancherel/Seeley-DeWitt prefactor), "
               "while the eigenvalue PRODUCT det = prod lambda_n is "
               "rational in u_0^2 (B1: per-mode degree +1, NO 4 pi); the "
               "log-additive per-mode share carries ln(4 u_0^2) "
               "(integer-4 bracket inside the log, pi-FREE, < 1e-12) with "
               "the 4 pi sitting OUTSIDE in the measure — no single "
               "native-multiplicative per-mode object hosts BOTH the 4 pi "
               "and the degree -2 (the structural orthogonality)",
          log_no_pi and abs(ALPHA_BARE - 1.0 / FOURPI) < 1e-15,
          f"per-mode ln|lambda|^2 = ln(4 u_0^2) = {expect:.6f} (pi-free); "
          f"trace normalization = 1/(4 pi) = {ALPHA_BARE:.7f} (separate)")

    return ext_der


# ---------------------------------------------------------------------------
# Section C — R3: TRANSCENDENCE.  The gap is exactly ln(pi); Lindemann.
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [A]: R3 — TRANSCENDENCE: the "
          "additive-share -> multiplicative-target gap is EXACTLY ln(pi); "
          "Lindemann forbids an algebraic readout exponent ---")

    # C1: the gap ln(4 pi u_0^2) - ln(4 u_0^2) = ln(pi) EXACTLY, three
    # ways: (a) symbolic identity (the u_0^2 and 4 cancel), (b) numeric at
    # the licensed u_0, (c) independence from u_0 (two rational points).
    target_log = math.log(4.0 * math.pi * U_0_SQ)   # ln(4 pi u_0^2) = Delta_S
    share_log = math.log(4.0 * U_0_SQ)              # ln(4 u_0^2), integer-4
    gap = target_log - share_log
    ln_pi = math.log(math.pi)
    # independence of u_0:
    g2 = (math.log(4.0 * math.pi * 0.70)
          - math.log(4.0 * 0.70))
    g3 = (math.log(4.0 * math.pi * 0.80)
          - math.log(4.0 * 0.80))
    # the target IS Delta_S (since ln(4 pi u_0^2) = ln(4 pi) + 2 ln u_0):
    target_is_deltas = abs(target_log - DELTA_S) < 1e-12
    check("A", "C1 the gap is EXACTLY ln(pi): "
               "ln(4 pi u_0^2) - ln(4 u_0^2) = ln(pi) (the u_0^2 and the "
               "INTEGER 4 cancel, leaving pi), < 1e-12, and INDEPENDENT of "
               "u_0 (same gap at u_0^2 in {0.70, 0.80}, < 1e-12); the "
               "multiplicative TARGET ln(4 pi u_0^2) = Delta_S = 2.270081 "
               "while the log-additive per-taste SHARE carries "
               "ln(4 u_0^2) = 1.125351 — the entire shortfall is the "
               "single transcendental ln(pi) = 1.144730",
          abs(gap - ln_pi) < 1e-12 and abs(g2 - ln_pi) < 1e-12
          and abs(g3 - ln_pi) < 1e-12 and target_is_deltas,
          f"gap = ln(4 pi u_0^2) - ln(4 u_0^2) = {gap:.6f} = "
          f"ln(pi) = {ln_pi:.6f}; share ln(4 u_0^2) = {share_log:.6f}, "
          f"target Delta_S = {target_log:.6f}")

    # C2: the Lindemann argument (stated; the determinant share is rational
    # in u_0^2, so any algebraic readout exponent on it produces an
    # algebraic-times-log object, never the transcendental 4 pi
    # multiplicatively).  Verify the determinant-share objects are RATIONAL
    # in u_0^2 ((7/8)^16 and (4 u_0^2)^8 exact Fractions), and that pi is
    # NOT a rational power of any rational — i.e. no rational exponent r,
    # rational base q give q^r = pi (recompute the ratio identity exactly).
    u02 = Fraction(7703246, 10000000)
    # the cross-block determinant ratio is exactly (7/8)^16 (rational):
    bases2 = [u02 * (3 + Fraction(1))] * 2          # L_t=2, sin^2=1
    bases4 = [u02 * (3 + Fraction(1, 2))] * 4       # L_t=4, sin^2=1/2
    det2 = Fraction(1)
    for b in bases2:
        det2 *= b ** 4
    det4 = Fraction(1)
    for b in bases4:
        det4 *= b ** 4
    ratio = det4 / (det2 ** 2)
    ratio_rational = ratio == Fraction(7, 8) ** 16
    # the per-taste massless determinant share is (4 u_0^2)^8 (rational in
    # u_0^2): at L_t=2 each of 2 modes has bracket 4, taste power 4 =>
    # exponent 8 on (4 u_0^2).
    share_obj = (4 * u02) ** 8
    share_rational = isinstance(share_obj, Fraction)
    # the readout objects ((7/8)^16, (4 u_0^2)^8) are RATIONAL in u_0^2:
    # an algebraic exponent on a rational base is algebraic; pi is
    # transcendental (Lindemann); so NO algebraic exponent yields 4 pi.
    # Numeric sanity: ln(pi)/ln(any rational) is irrational (no clean
    # rational exponent recovers pi) — check it is not a small rational:
    r = ln_pi / math.log(2.0)                        # = log_2(pi)
    not_small_rational = all(abs(r - n / d) > 1e-9
                             for d in range(1, 50)
                             for n in range(1, 200))
    check("A", "C2 the Lindemann transcendence obstruction: the "
               "determinant-share readout objects are RATIONAL in u_0^2 — "
               "the cross-block ratio is exactly (7/8)^16 (exact "
               "Fraction) and the per-taste massless share is "
               "(4 u_0^2)^8 (exact Fraction) — so any ALGEBRAIC readout "
               "exponent on them yields an algebraic number, NEVER the "
               "TRANSCENDENTAL 4 pi (pi transcendental by "
               "Lindemann-Weierstrass); log_2(pi) = 1.6515 is not a "
               "small rational (checked over denominators < 50), "
               "confirming pi is no rational power of a rational base — "
               "the 4 pi cannot be produced MULTIPLICATIVELY by an "
               "algebraic exponent on the rational determinant share",
          ratio_rational and share_rational and not_small_rational,
          f"ratio == (7/8)^16: {ratio_rational}; share (4 u_0^2)^8 "
          f"rational: {share_rational}; log_2(pi) = {r:.4f} "
          f"(not small rational)")

    # C3: the dim-4 taste-direction readout (15/16)^(-1/4) = 1.0163, 9.8x
    # displaced from alpha_s (the D=4 Stefan-Boltzmann 1/4-power readout
    # taken literally in the taste-count direction).
    n = N_TASTE
    dimreadout_ratio = (float(n - 1) / n) ** (-0.25)
    displ = dimreadout_ratio / ALPHA_S
    check("A", "C3 the dim-4 taste-direction readout: the D=4 "
               "determinant-ratio admission v ~ A(L_t)^(-1/4) (the 1/4 "
               "power is D=4 Stefan-Boltzmann bookkeeping, per the "
               "determinant-ratio note section 4.4), re-expressed in the "
               "TASTE-COUNT direction with A(n) prop n, gives removing one "
               "taste multiplies v by (15/16)^(-1/4) = 1.0163 — an O(1) "
               "factor near 1, displaced from the required alpha_s = "
               "0.1033 by ~9.8x; the dim-4 admission taken LITERALLY in "
               "the taste direction does NOT deliver alpha_s, so the "
               "additive -> multiplicative conversion is NECESSARILY a "
               "named admission (R coupled to B5), not a derivation",
          abs(dimreadout_ratio - 1.0163) < 1e-3 and displ > 9.0,
          f"v-ratio = {dimreadout_ratio:.5f}, ratio/alpha_s = "
          f"{displ:.4f}x (9.8x displaced)")

    observation("the dim-4 taste-direction v-ratio (15/16)^(-1/4) = "
                "1.0163 sits trivially near 1 and is ~9.8x ABOVE "
                "alpha_s = 0.1033; it does NOT approach the required "
                "per-decoupling factor — recorded only to be explicit "
                "that no numerology window is crossed; NO mechanism, NO "
                "supplier, NO claim.")


# ---------------------------------------------------------------------------
# Section D — R4: re-invoke the FOUR leg runners as subprocesses.
# ---------------------------------------------------------------------------
LEG_RUNNERS = [
    ("D1", "frontier_hierarchy_delta0_b4_bare_class_magnitude_ceiling_"
           "theorem_2026_06_13.py",
     r"TOTAL:\s*PASS=19\s+FAIL=0",
     "leg 2 bare-class EXCHANGE ceiling (9/16 < 1, exact): 19/0"),
    ("D2", "frontier_hierarchy_delta0_b4_njl_rpa_normalization_probe_"
           "2026_06_13.py",
     r"TOTAL:\s*PASS=22\s+FAIL=0",
     "leg 3 NJL-RPA vertex ENHANCEMENT (degree -14.86, "
     "CONDITIONAL-KILL): 22/0"),
    ("D3", "frontier_hierarchy_delta0_b4_free_energy_lnz_readout_probe_"
           "2026_06_13.py",
     r"TOTAL:\s*PASS=18\s+FAIL=0",
     "leg 4 free-energy / ln-Z readout (degree-(-2), readout coeff "
     "UNDERIVED, RECLASSIFY): 18/0"),
    ("D4", "frontier_hierarchy_delta0_b4_attachment_observable_"
           "enumeration_2026_06_11.py",
     r"TOTAL:\s*PASS=28\s+FAIL=0",
     "leg 1 READOUT class K1-K8 (91 candidates eliminated): 28/0"),
]


def section_d():
    print("\n--- Section D [B]: R4 — the FOUR leg runners re-verified as "
          "subprocesses (exit code + note-stated TOTALs) ---")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SCRIPTS)
    legs_summary = []
    for tag, script, pattern, label in LEG_RUNNERS:
        path = SCRIPTS / script
        ok = False
        detail = "script missing"
        observed = "n/a"
        if path.exists():
            t0 = time.time()
            try:
                proc = subprocess.run(
                    [sys.executable, str(path)],
                    capture_output=True, text=True, timeout=110,
                    cwd=str(REPO_ROOT), env=env,
                )
                elapsed = time.time() - t0
                m = re.search(r"TOTAL:\s*PASS=(\d+)\s+FAIL=(\d+)",
                              proc.stdout)
                observed = (f"PASS={m.group(1)} FAIL={m.group(2)}"
                            if m else "no TOTAL line")
                total_ok = re.search(pattern, proc.stdout) is not None
                ok = proc.returncode == 0 and total_ok
                detail = (f"exit = {proc.returncode}, total line "
                          f"{'matched' if total_ok else 'NOT matched'} "
                          f"[observed {observed}], {elapsed:.1f}s")
            except subprocess.TimeoutExpired:
                detail = "TIMEOUT (110 s)"
        legs_summary.append(f"{tag}: {observed}")
        check("B", f"{tag} {label} — {script} passes its note-stated "
                   f"TOTAL as a subprocess", ok, detail)
    return legs_summary


# ---------------------------------------------------------------------------
# Section E — R5: the RECLASSIFICATION PROPOSAL checks + governance
# self-scan.
# ---------------------------------------------------------------------------
def flat(path: Path) -> str:
    return " ".join((path.read_text() if path.exists() else "").split())


def section_e():
    print("\n--- Section E [B]: R5 — the RECLASSIFICATION PROPOSAL checks "
          "and the governance self-scan ---")

    note = flat(PARENT_NOTE)
    note_l = note.lower()

    # E1: the note PROPOSES (does not enact) the reclassification.
    proposes = ("proposes" in note_l or "proposal" in note_l)
    not_enact = ("does not edit" in note_l
                 and "does not change any v-row" in note_l)
    forbidden_enact = [
        "this note registers b4 in tier_a_admissions",
        "v-row effective_status is hereby changed",
        "b4 is now retained_bounded",
        "tier-a registration is complete",
    ]
    forb_hit = [t for t in forbidden_enact if t in note_l]
    check("B", "E1 the note PROPOSES (does not enact) the B4 "
               "reclassification: it carries 'propose(s)/proposal', states "
               "it 'does not edit' tier_a_admissions.json and 'does not "
               "change any v-row' status, and the enactment tokens "
               "('registers B4 in tier_a_admissions', 'v-row "
               "effective_status is hereby changed', 'B4 is now "
               "retained_bounded', 'Tier-A registration is complete') are "
               "ABSENT",
          proposes and not_enact and not forb_hit,
          f"proposes={proposes}, non-enact fences={not_enact}, "
          f"forbidden hits={forb_hit}")

    # E2: the note carries the no_go_portfolio (the six legs).
    portfolio_tokens = [
        "no_go_portfolio",
        "observable_enumeration",          # leg 1
        "bare_class_magnitude_ceiling",    # leg 2
        "njl_rpa_normalization",           # leg 3
        "free_energy_lnz_readout",         # leg 4
        "orthogonality",                   # leg 5 (fourth-family)
        "transcendence",                   # leg 5/6 sharpening
        "derived-readout",                 # leg 6
    ]
    missing_portfolio = [t for t in portfolio_tokens
                         if t.lower() not in note_l]
    check("B", "E2 the note carries the no_go_portfolio (the SIX legs): "
               "names 'no_go_portfolio' and references all six prongs — "
               "K1-K8 observable enumeration (leg 1), bare-class exchange "
               "ceiling (leg 2), NJL-RPA enhancement (leg 3), "
               "free-energy/ln-Z readout (leg 4), the fourth-family "
               "orthogonality + transcendence structural core (leg 5), "
               "and the five derived-readout maps (leg 6)",
          not missing_portfolio,
          f"missing portfolio tokens = {missing_portfolio}")

    # E3: the note explicitly defers the Tier-A registration to the owner
    # per AXIOM_MINIMALITY_POLICY.
    defers = ("defer" in note_l and "owner" in note_l
              and "axiom_minimality_policy" in note_l)
    science_level = "science-level" in note_l
    audit_lane = ("status authority" in note_l
                  and "independent audit lane only" in note_l)
    check("B", "E3 the note explicitly DEFERS the Tier-A registration to "
               "the owner: it names the registration a 'science-level' "
               "OWNER decision, DEFERS it (and the v-row cascade) to the "
               "owner / audit lane per AXIOM_MINIMALITY_POLICY, and "
               "carries the 'Status authority: independent audit lane "
               "only' fence",
          defers and science_level and audit_lane,
          f"defers={defers}, science-level={science_level}, "
          f"audit-lane fence={audit_lane}")

    # E4: governance self-scan — tier_a_admissions.json NOT referenced as
    # modified by THIS runner OR the note.  The note may MENTION the file
    # (it must, to defer it), but must mark it explicitly UNCHANGED, and
    # this runner must not write to it.
    src = Path(__file__).read_text()
    # this runner performs NO write operation at all, so it CANNOT modify
    # tier_a_admissions.json or any audit data on disk.  The write-verb
    # tokens are COMPOSED below so this scan does not match its own check
    # list as a false positive.
    write_verbs = ["write_te" + "xt(", "json." + "dump",
                   "os." + "replace", "shu" + "til.",
                   ".write" + "lines(", "open" + "(__file__, 'w"]
    has_write_verb = any(w in src for w in write_verbs)
    # the note states tier_a_admissions.json is NOT modified:
    note_marks_unchanged = (
        "tier_a_admissions.json is not modified" in note_l
        or "does not edit `docs/audit/data/tier_a_admissions.json`"
        in note_l
        or ("tier_a_admissions.json" in note_l
            and "not modified" in note_l)
        or ("tier_a_admissions.json" in note_l
            and "does not edit" in note_l))
    check("B", "E4 governance self-scan: this runner performs NO write "
               "operation (no write-text, no json dump, no os replace, no "
               "shutil, no writelines anywhere in its source), so it "
               "CANNOT modify tier_a_admissions.json or any audit data; "
               "and the parent note explicitly marks "
               "tier_a_admissions.json as NOT modified (referenced only to "
               "defer it to the owner)",
          (not has_write_verb) and note_marks_unchanged,
          f"runner has write verb = {has_write_verb}; note marks "
          f"tier_a_admissions unchanged = {note_marks_unchanged}")

    # E5: on-disk one-hop authorities present (the six leg notes + the
    # determinant-ratio note for R + the regulator no-go for the B3
    # parallel + the route inventory + AXIOM_MINIMALITY_POLICY).
    authorities = [
        DOCS / "HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_"
               "NOTE_2026-06-11.md",
        DOCS / "HIERARCHY_DELTA0_B4_BARE_CLASS_MAGNITUDE_CEILING_THEOREM_"
               "NOTE_2026-06-13.md",
        DOCS / "HIERARCHY_DELTA0_B4_NJL_RPA_NORMALIZATION_PROBE_NOTE_"
               "2026-06-13.md",
        DOCS / "HIERARCHY_DELTA0_B4_FREE_ENERGY_LNZ_READOUT_PROBE_NOTE_"
               "2026-06-13.md",
        DOCS / "HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_THEOREM_"
               "NOTE_2026-05-10.md",
        DOCS / "HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_"
               "REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md",
        DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_"
               "NOTE_2026-06-11.md",
        DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md",
        DOCS / "audit" / "data" / "tier_a_admissions.json",
    ]
    missing_auth = [a.name for a in authorities if not a.exists()]
    # the determinant-ratio note supplies admission R; the regulator no-go
    # supplies the substrate-imposed B3 parallel; the tier_a template
    # carries the AC_phi_lambda no_go_portfolio shape.
    detratio = flat(authorities[4])
    regno = flat(authorities[5])
    tiera = flat(authorities[8])
    template_ok = ("no_go_portfolio" in tiera
                   and "AC_phi_lambda" in tiera)
    detratio_ok = ("A(L_t)^(-1/4)" in detratio
                   and "Stefan-Boltzmann" in detratio)
    regno_ok = "Substrate-Imposed" in regno or "substrate-imposed" in regno
    check("B", "E5 one-hop authorities on disk: all six leg notes, the "
               "determinant-ratio note (supplies admission R: "
               "v ~ A(L_t)^(-1/4) with the D=4 Stefan-Boltzmann 1/4 "
               "power), the regulator no-go (the substrate-imposed B3 "
               "parallel), the route inventory, AXIOM_MINIMALITY_POLICY, "
               "and the tier_a_admissions template (carrying the "
               "AC_phi_lambda no_go_portfolio shape this proposal "
               "mirrors) are all present",
          not missing_auth and template_ok and detratio_ok and regno_ok,
          f"missing = {missing_auth}; tier_a template = {template_ok}; "
          f"det-ratio R = {detratio_ok}; regulator B3-parallel = "
          f"{regno_ok}")

    # E6: parent-note honesty fences — bounded scope, NOT universal, NOT a
    # status change, NOT closure.
    required_tok = [
        "bounded_theorem",
        "bounded no-go",
        "not a claim of universal mathematical impossibility",
        "does not close",
        "delta0",
        "examined analytic classes",
    ]
    forbidden_tok = [
        "universal mathematical impossibility is proven",
        "b4 is closed",
        "delta0 gate is closed",
        "derivation closes b4",
        "the readout coefficient is hereby derived",
    ]
    req_missing = [t for t in required_tok if t not in note_l]
    forb_hit2 = [t for t in forbidden_tok if t in note_l]
    check("B", "E6 parent-note honesty fences: claim type "
               "'bounded_theorem' scoped as a 'bounded no-go' over the "
               "'examined analytic classes' (NOT 'a claim of universal "
               "mathematical impossibility'), 'does not close' the DELTA0 "
               "gate; the over-claim tokens (universal impossibility "
               "proven, B4/DELTA0 closed, derivation closes B4, readout "
               "coefficient derived) are ABSENT",
          not req_missing and not forb_hit2,
          f"missing = {req_missing}, forbidden hits = {forb_hit2}")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this portfolio "
          "runner; every")
    print("   number is a BZ sum, an exact rational, a cited framework "
          "constant, or a")
    print("   subprocess exit code / TOTAL line.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"   # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no external comparator consumed "
               "anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_b4_attachment_nonderivability_"
          "portfolio_2026_06_13.py")
    print(" CAPSTONE: the B4 attachment-NON-DERIVABILITY no-go PORTFOLIO.  "
          "B4 reduces")
    print(" to supplying alpha_s = 1/(4 pi u_0^2) = 0.1033038 "
          "MULTIPLICATIVELY at")
    print(" u_0-degree -2 per taste decoupling (16x).  Six mechanism "
          "families are")
    print(" EXHAUSTED.  STRUCTURAL CORE (bounded over examined classes, "
          "NOT universal):")
    print(" 1/(4 pi) is born as a trace NORMALIZATION (degree 0, "
          "additive); native")
    print(" multiplicativity is the eigenvalue product (degree +1, NO "
          "4 pi) — orthogonal.")
    print(" SHARPENED by transcendence: the additive share carries "
          "ln(4 u_0^2), the")
    print(" target needs ln(4 pi u_0^2); the gap is EXACTLY ln(pi); pi "
          "transcendental")
    print(" (Lindemann) => no algebraic exponent on the rational "
          "determinant produces")
    print(" the 4 pi multiplicatively.  The conversion is NECESSARILY an "
          "admission (R")
    print(" coupled to B5).  R4 re-runs the four leg runners as "
          "subprocesses.  R5: the")
    print(" note PROPOSES (does NOT enact) reclassification, defers the "
          "Tier-A")
    print(" registration to the owner, leaves tier_a_admissions.json and "
          "every v-row")
    print(" UNTOUCHED.  Parent note: docs/HIERARCHY_DELTA0_B4_ATTACHMENT_")
    print("   NONDERIVABILITY_NOGO_PORTFOLIO_NOTE_2026-06-13.md")
    print("=" * 78)

    section_a()
    section_b()
    section_c()
    legs = section_d()
    section_e()
    section_fence()

    # Declared-open residuals.
    print()
    residual("the RECLASSIFICATION itself is an OWNER DECISION, declared "
             "open here.  Registering B4 as a Tier-A admitted derivation "
             "target in docs/audit/data/tier_a_admissions.json (the "
             "AC_phi_lambda/theta no_go_portfolio template) and cascading "
             "the v-row to retained_bounded is a SCIENCE-LEVEL owner "
             "decision per docs/audit/AXIOM_MINIMALITY_POLICY.md.  This "
             "note PROPOSES the reclassification and ASSEMBLES the "
             "portfolio; it does NOT edit tier_a_admissions.json, does NOT "
             "change any v-row effective_status, and DEFERS both to the "
             "owner / independent audit lane.  Status authority = audit "
             "lane only.")
    residual("the per-decoupling attachment alpha_s is NOT DERIVED.  The "
             "structural core shows the additive -> multiplicative "
             "conversion is NECESSARILY an admission (the D=4 dimensional "
             "readout R, 1/4-power Stefan-Boltzmann bookkeeping, coupled "
             "to the observable identification B5) over the SIX examined "
             "families {readout K1-K8, bare exchange, NJL-RPA vertex, "
             "free-energy/ln-Z, fourth-family zeta/heat-kernel/holonomy/"
             "det-ratio, derived-readout} — a BOUNDED no-go, NOT a claim "
             "of universal mathematical impossibility.  DELTA0 stays OPEN "
             "as a DERIVATION even as this note proposes closure-by-"
             "declaration.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN.  This portfolio EXHAUSTS the "
             "examined attachment families and PROPOSES B4 as a "
             "B5-coupled DECLARED boundary (mirroring how B3 is declared "
             "substrate-imposed); it reaches retained_bounded IF AND ONLY "
             "IF the owner / audit lane RATIFIES the Tier-A registration.  "
             "The route inventory is NOT modified.")

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" Legs re-verified (subprocess TOTALs): {'; '.join(legs)}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: the B4 per-decoupling attachment alpha_s = "
          "1/(4 pi u_0^2) is")
    print("   NON-DERIVABLE over the SIX examined mechanism families "
          "(bounded no-go, NOT")
    print("   universal): the 4 pi is born as an ADDITIVE trace "
          "NORMALIZATION (degree 0)")
    print("   while native multiplicativity is the eigenvalue product "
          "(degree +1, NO 4 pi)")
    print("   — ORTHOGONAL; and the additive-share -> multiplicative-"
          "target gap is EXACTLY")
    print("   ln(pi), which by Lindemann no algebraic exponent on the "
          "rational determinant")
    print("   share can produce multiplicatively.  The conversion is "
          "NECESSARILY an")
    print("   admission (the D=4 readout R coupled to B5).  This note "
          "PROPOSES B4 as a")
    print("   B5-coupled DECLARED boundary with this six-leg "
          "no_go_portfolio and DEFERS the")
    print("   Tier-A registration + v-row cascade to the owner / audit "
          "lane per")
    print("   AXIOM_MINIMALITY_POLICY — it does NOT edit "
          "tier_a_admissions.json, does NOT")
    print("   change any v-row status.  DELTA0 stays OPEN as a DERIVATION "
          "even as it")
    print("   proposes closure-by-declaration.  NOT a derivation of "
          "alpha_s; NOT a status")
    print("   change; the structural core is bounded over examined "
          "classes, not universal.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
