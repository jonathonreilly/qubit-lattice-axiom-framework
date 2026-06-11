#!/usr/bin/env python3
"""DELTA0 S1 probe: exact one-link strong-coupling content vs the
alpha_s-per-decoupling target.  (Block09 of the DELTA0 blocking
campaign; executes the route inventory's S1 kill criterion.)

    docs/HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_COUPLING_PROBE_
    NOTE_2026-06-11.md

Setting.  The route-inventory synthesis (docs/HIERARCHY_DELTA0_
ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_NOTE_2026-06-11.md) reduces B4
closure to ONE unsupplied transport rule (block02): one factor
alpha_s = alpha_bare/u_0^2 = 0.1033038 per taste decoupling.  Surviving
route S1 (strong-coupling one-link Haar / Kawamoto-Smit lineage) must
supply that factor from EXACT one-link Haar integration over the
decimated-mode fermion bilinear source.  Its kill criterion: "an exact
one-link computation whose per-decoupling factor is O(1)-displaced from
alpha_s under every declared variant (the E3 pattern) eliminates S1."

THREE CHEAP ARMS (no symbolic Grassmann engine, no high-dimensional
symbolic quadrature; every section runs in seconds):

  ARM 1 (beta = 6, numeric, declared bath).  The E3/block04 runner's
      one-link expectation functions F(h) (U(1) Bessel ratio, SU(2)
      Gautschi continued fraction, SU(3) Weyl-measure quadrature) are
      REUSED VERBATIM by module import.  F(h) IS the exact one-link
      Haar integral <(1/N) Re Tr U> under exp(h Re Tr U): the only
      model content in E3 was the BATH (the mean-field staple source),
      never the link integral.  Arm 1 recomputes the E3 saddles u*(16),
      u*(15) per variant, then evaluates the exact one-link expectation
      ONCE (no iteration) at the fixed saddle bath,
          u_exact(n) = F( (6 beta u*(n)^3 + kappa(n)/u*(n)) / N ),
      kappa(n) = n_c n / 64 (E3's M2 uniform share), and reads off
          R_arm1 = (u_exact(15)/u_exact(16))^(-2),
      plus a frozen-bath sub-variant (bath pinned at u*(16) for both n,
      isolating the pure exact-one-link response with zero bath
      relaxation) and the E3 stress brackets kappa -> 2 kappa, kappa/2.

  ARM 2 (beta = 0, exact rationals).  Known closed-form Haar moments
      consumed as exact Fractions (Creutz's book / Weingarten calculus
      as parallel references; the framework consumes its own verified
      constants):
        U(1):  int U^a U*^b      = delta_ab                (verified),
        SU(2): int U_ij U*_kl    = (1/2) delta_ik delta_jl (verified),
               int U_ij U_kl     = (1/2) eps_ik eps_jl     (verified),
        SU(3): int U_ij U*_kl    = (1/3) delta_ik delta_jl (cited;
               cross-checked through exact class-function grid moments
               <|t|^2> = 1 and the exact-Fraction unitarity sum rule),
               int U_i1j1 U_i2j2 U_i3j3 = (1/6) eps_i eps_j (cited;
               cross-checked through <t^3> = 1 on the same grid).
      Verification is deterministic numeric quadrature of POLYNOMIAL
      moments only (U(1): exact uniform circle grid; SU(2): Euler/S^3
      midpoint grid, declared tolerance 1e-3 — a VERIFICATION of an
      exact rational, not a derivation; SU(3): the E3 Weyl-measure
      torus grid, which reaches only class functions, hence the honest
      cited-constant + cross-check declaration).  Fermionic consequence
      WITHOUT any symbolic engine (one-component staggered fermions,
      one Grassmann pair per site per color; nilpotency truncates the
      link expansion at order N_c): the per-dimer and per-baryon-link
      weights are PRODUCTS of these rational moments with rational
      combinatorial factors, derived by hand in the parent note and
      consumed here as exact Fractions:
        meson dimer (M_x M_y coefficient): 1/N_c  (1, 1/2, 1/3),
        baryon-link Haar moment factor:    1/N_c! (SU(2): 1/2;
                                                   SU(3): 1/6).
      Partition-function scope (kept deliberately tiny):
        (a) 2-site single-link Z(m): exact binomial collapse
            Z = sum_k c_k [k! C(N,k)]^2 m^(2(N-k)) = (m^2 + 1)^N over
            the U(N)-moment (mesonic) sector, c_k = (N-k)!/(N! k!)
            with c_0, c_1 derived from verified moments and c_2, c_3
            cited (Rossi-Wolff closed form, parallel reference); the
            SU(3) baryonic eps-sector addition needs the sixth moment
            and is DECLARED out of scope (fence);
        (b) the 2^3 framework-native Z^3 block (8 sites, 3 directions,
            APBC wrap): the doubled links per cube edge (direct + wrap;
            hop signs enter the dimer weight squared, so the APBC sign
            drops) collapse to multiplicity-2 edges of single-dimer
            weight 2/N_c; the DECLARED model is the single-occupancy
            monomer-dimer (matching) sector, enumerated EXACTLY by
            memoized recursion over the 8-vertex cube graph AND
            independently by brute force over all 2^12 edge subsets;
            Z(m) extracted as an exact Fraction polynomial; factor
            structure probed by an exact rational-root scan plus
            numeric (flagged) Durand-Kerner roots.
      Per-object weight table with displacements vs alpha_s, including
      the 1/N_c^2 = 0.1111 entry (1.076x alpha_s — inside the
      inventory's factor-2 observation window; printed as a clearly
      labeled OBSERVATION with a numerology-risk flag, never a
      residual and never a closure).

  ARM 3 (the rationality obstruction; the sharpest deliverable).
      Every coefficient produced by exact beta = 0 Haar integration of
      polynomial fermion-bilinear sources is RATIONAL (all Arm-2
      constants are exact Fractions; the general statement is
      Weingarten calculus, cited as a parallel reference and consumed
      at the strength of the computed instances).  The required
      alpha_s = 1/(4 pi u_0^2) carries pi: if 4 pi u_0^2 were rational
      then pi = (rational)/(4 u_0^2) would be algebraic (u_0^2 =
      sqrt(5934/10000) is algebraic), contradicting the Lindemann
      transcendence of pi (parallel reference).  Hence EXACT supply of
      alpha_s per decoupling by beta = 0 link integration alone is
      IMPOSSIBLE, and the 4 pi's only landed supplier remains the
      Green-kernel/Plancherel readout chain (docs/ALPHA_BARE_FOUR_PI_
      FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md).
      Conclusion: S1 STANDALONE is eliminated at beta = 0 (exact) and
      at one-link-exact beta = 6 (Arm 1, numeric, declared bath); S1
      REFINES to the composite route S1' = finite-beta link integration
      COMPOSITED with the readout kernel chain (group-theory rationals
      from the links; the 4 pi from the kernel).  The inventory is NOT
      modified (its section 5 non-modification rule); this runner's
      parent note records the refinement downstream.

Vocabulary discipline: exact-Fraction facts and verified moments are
bounded_theorem-grade; the Arm-1 bath and the Arm-2 matching sector
are DECLARED models (fenced); all remaining open content is printed as
RESIDUAL (declared-open) lines; the 1/N_c^2 proximity is printed as a
single clearly-labeled OBSERVATION line (not a residual, not a pass).

Deterministic, pure Python stdlib (fractions, math, cmath, itertools,
functools), no network, no randomness (fixed grids, fixed iteration
counts), TOTAL RUNTIME well under 60 s (typically ~2 s).  Exit code 0
iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import cmath
import importlib.util
import itertools
import math
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
SCRIPTS = REPO_ROOT / "scripts"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_"
                      "COUPLING_PROBE_NOTE_2026-06-11.md")

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
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381 (licensed value)
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (block02 reduction target)

# E3 runner reused verbatim by module import (its module body only
# defines functions and builds the fixed SU(3) torus grids).
E3_PATH = (SCRIPTS / "frontier_hierarchy_delta0_attachment_mean_field_"
                     "feedback_probe_2026_06_11.py")
_spec = importlib.util.spec_from_file_location("e3_probe", E3_PATH)
E3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E3)

VARIANTS = (("U(1)", E3.f_u1, 1), ("SU(2)", E3.f_su2, 2),
            ("SU(3)", E3.f_su3, 3))


# ---------------------------------------------------------------------------
# Section A [C] — E3 reuse certification.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]: E3 one-link machinery reused verbatim "
          "(module import) and re-certified ---")

    # A1: U(1)/SU(2) exact Bessel-ratio integrals vs independent
    # deterministic quadrature at fresh test points.
    npts = 512
    ok = True
    for h in (1.0, 7.0, 21.0):
        num = den = 0.0
        for i in range(npts):
            th = (i + 0.5) * 2.0 * math.pi / npts
            e = math.exp(h * (math.cos(th) - 1.0))
            den += e
            num += e * math.cos(th)
        ok = ok and abs(num / den - E3.f_u1(h)) < 1e-12
    for h in (1.0, 7.0, 14.0):
        num = den = 0.0
        for i in range(npts):
            th = (i + 0.5) * math.pi / npts
            e = math.sin(th) ** 2 * math.exp(2.0 * h * (math.cos(th) - 1.0))
            den += e
            num += e * math.cos(th)
        ok = ok and abs(num / den - E3.f_su2(h)) < 1e-12
    check("C", "A1 E3's U(1) and SU(2) one-link expectations F(h) "
               "(Gautschi continued-fraction Bessel ratios) re-certified "
               "against independent 512-point deterministic quadrature at "
               "3 fresh test h each, < 1e-12 — F(h) IS the exact one-link "
               "Haar integral",
          ok)

    # A2: SU(3) Weyl grid Haar moments + boundary-input consistency.
    sw = sum(E3.SU3_W64)
    m0 = sw / len(E3.SU3_W64) / 6.0
    m2 = sum(w * t * t for w, t in zip(E3.SU3_W64, E3.SU3_T64)) / sw
    consist = (abs(E3.ALPHA_S - ALPHA_S) < 1e-15
               and abs(E3.U_0 - U_0) < 1e-15
               and E3.BETA == 6.0 and E3.N_COLORS == 3
               and E3.LINKS_PER_BLOCK == 64 and E3.STAPLES_PER_LINK == 6)
    check("C", "A2 E3's SU(3) Weyl-measure torus grid re-certified "
               "(norm = 1, <(Re Tr U)^2> = 1/2 to < 1e-12) and this "
               "runner's declared boundary inputs (alpha_s, u_0, beta, "
               "n_c, link counting) IDENTICAL to E3's",
          abs(m0 - 1.0) < 1e-12 and abs(m2 - 0.5) < 1e-12 and consist,
          f"alpha_s = {ALPHA_S:.7f}")


# ---------------------------------------------------------------------------
# Section B [A] — ARM 1: exact one-link evaluation at the E3 saddle bath.
# ---------------------------------------------------------------------------
def h_total(u: float, kappa: float, n_group: int) -> float:
    """E3's M1+M2 total one-link source at link dressing u."""
    return (E3.STAPLES_PER_LINK * E3.BETA * u ** 3
            + (kappa / u if kappa else 0.0)) / n_group


def section_b():
    print("\n--- Section B [A]: ARM 1 — exact one-link expectation at "
          "the fixed E3 saddle bath, beta = 6 ---")
    saddles = {}
    res_ok = True
    for name, f_func, n_group in VARIANTS:
        row = {}
        for n_modes in (16, 15):
            kappa = E3.N_COLORS * n_modes / E3.LINKS_PER_BLOCK
            sol = E3.solve_u(f_func, n_group, kappa)
            res_ok = res_ok and sol is not None and sol[1] < 1e-12
            row[n_modes] = sol[0]
        saddles[name] = row
        print(f"    {name}: u*(16) = {row[16]:.10f}, "
              f"u*(15) = {row[15]:.10f}")
    check("A", "B1 E3 saddles u*(16), u*(15) recomputed per variant with "
               "E3's own solver (dressed branch, uniform share "
               "kappa = 3n/64); every root residual < 1e-12",
          res_ok)

    # B2: ONE-SHOT exact one-link evaluation at the fixed saddle bath.
    fp_ok = True
    u_exact = {}
    for name, f_func, n_group in VARIANTS:
        row = {}
        for n_modes in (16, 15):
            kappa = E3.N_COLORS * n_modes / E3.LINKS_PER_BLOCK
            ue = f_func(h_total(saddles[name][n_modes], kappa, n_group))
            row[n_modes] = ue
            fp_ok = fp_ok and abs(ue - saddles[name][n_modes]) < 1e-9
        u_exact[name] = row
    check("A", "B2 exact one-link expectation evaluated ONCE (no "
               "iteration) at the fixed E3 saddle bath: u_exact(n) = "
               "F(h_total(n)) reproduces u*(n) to < 1e-9 in every "
               "variant for n = 16 and 15 — the link integral in E3 was "
               "already EXACT; the saddle approximation lives in the "
               "bath, not in the link integration",
          fp_ok)

    # B3: the Arm-1 readout, plus the frozen-bath sub-variant.
    table = {}
    ok_disp = True
    for name, f_func, n_group in VARIANTS:
        r_arm1 = (u_exact[name][15] / u_exact[name][16]) ** -2
        # frozen bath: gauge staple source pinned at u*(16) for BOTH n;
        # only the fermion source kappa(n)/u*(16) changes.
        u16 = saddles[name][16]
        uf15 = f_func((E3.STAPLES_PER_LINK * E3.BETA * u16 ** 3
                       + (E3.N_COLORS * 15 / E3.LINKS_PER_BLOCK) / u16)
                      / n_group)
        r_frozen = (uf15 / u_exact[name][16]) ** -2
        table[name] = (r_arm1, r_arm1 / ALPHA_S, r_frozen,
                       r_frozen / ALPHA_S)
        ok_disp = (ok_disp
                   and abs(r_arm1 - 1.0) < 0.5
                   and not (0.5 <= r_arm1 / ALPHA_S <= 2.0)
                   and abs(r_frozen - 1.0) < 0.5
                   and not (0.5 <= r_frozen / ALPHA_S <= 2.0))
        print(f"    {name}: R_arm1 = {r_arm1:.10f} "
              f"(R/alpha_s = {r_arm1 / ALPHA_S:.4f});  frozen bath "
              f"R = {r_frozen:.10f} (R/alpha_s = {r_frozen / ALPHA_S:.4f})")
    check("A", "B3 per-decimation factor R_arm1 = "
               "(u_exact(15)/u_exact(16))^(-2) is O(1) (|R - 1| < 0.5) "
               "and outside a factor 2 of the required alpha_s = "
               "0.1033038 in EVERY variant, in BOTH the relaxed-bath and "
               "frozen-bath conventions — the inventory's S1 kill "
               "criterion fires at one-link-exact beta = 6 under the "
               "declared bath",
          ok_disp,
          ", ".join(f"{v}: {table[v][1]:.3f}x" for v, _, _ in VARIANTS))

    # B4: stress brackets (E3's deliberate mis-sharing robustness axis).
    stress_ok = True
    details = []
    for name, f_func, n_group in VARIANTS:
        for mult, tag in ((2.0, "x2"), (0.5, "x1/2")):
            us = {}
            for n_modes in (16, 15):
                kappa = mult * E3.N_COLORS * n_modes / E3.LINKS_PER_BLOCK
                sol = E3.solve_u(f_func, n_group, kappa)
                ok = sol is not None and sol[1] < 1e-12
                if ok:
                    us[n_modes] = f_func(h_total(sol[0], kappa, n_group))
                stress_ok = stress_ok and ok
            if 16 in us and 15 in us:
                r = (us[15] / us[16]) ** -2
                stress_ok = (stress_ok and abs(r - 1.0) < 0.5
                             and not (0.5 <= r / ALPHA_S <= 2.0))
                details.append(f"{name} {tag}: {r / ALPHA_S:.3f}x")
    # E3's declared SU(3) small-u branch (D4 robustness axis), with the
    # same one-shot exact evaluation.
    small = {}
    for n_modes in (16, 15):
        kappa = E3.N_COLORS * n_modes / E3.LINKS_PER_BLOCK
        sol = E3.solve_u(E3.f_su3, 3, kappa, "smallest")
        stress_ok = stress_ok and sol is not None and sol[1] < 1e-12
        if sol is not None:
            small[n_modes] = E3.f_su3(h_total(sol[0], kappa, 3))
    if 16 in small and 15 in small:
        r_small = (small[15] / small[16]) ** -2
        stress_ok = (stress_ok and abs(r_small - 1.0) < 0.5
                     and not (0.5 <= r_small / ALPHA_S <= 2.0))
        details.append(f"SU(3) small branch: {r_small / ALPHA_S:.3f}x")
    check("A", "B4 stress brackets kappa -> 2 kappa and kappa/2 "
               "(deliberate mis-sharing by a factor 4 overall) AND the "
               "SU(3) small-u branch (E3's D4 axis): the one-shot exact "
               "one-link factor stays O(1) and outside a factor 2 of "
               "alpha_s in every leg — no sharing convention or branch "
               "selection rescues the standalone route at beta = 6",
          stress_ok, "; ".join(details))
    return table


# ---------------------------------------------------------------------------
# Section C [C] — ARM 2: Haar moment verification (polynomial moments only).
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [C]: ARM 2 — closed-form Haar moments as exact "
          "rationals, verified by deterministic polynomial quadrature ---")

    # C1: U(1) — uniform circle grid (exact for trig polynomials).
    n = 16
    ok_u1 = True
    for a in range(3):
        for b in range(3):
            s = 0j
            for i in range(n):
                th = (i + 0.5) * 2.0 * math.pi / n
                s += cmath.exp(1j * (a - b) * th)
            s /= n
            exact = 1.0 if a == b else 0.0
            ok_u1 = ok_u1 and abs(s - exact) < 1e-12
    check("C", "C1 U(1) moments int U^a U*^b dU = delta_ab verified for "
               "a, b in {0, 1, 2} on a uniform 16-point circle grid "
               "(exact for trig polynomials; < 1e-12) — the U(1) meson "
               "dimer weight 1/N_c = 1 and the absence of an eps sector "
               "(int U^k = 0, k != 0) read off directly",
          ok_u1)

    # C2/C3: SU(2) entrywise moments via the Euler/S^3 midpoint grid
    # (DECLARED tolerance 1e-3: a verification of exact rationals, not a
    # derivation; phases are integrated exactly by the uniform periodic
    # grids, the polar direction by 192 midpoints).
    n_th, n_phi, n_psi = 192, 8, 8
    norm = 0.0
    m_star = [[0j] * 4 for _ in range(4)]
    m_plain = [[0j] * 4 for _ in range(4)]
    for it in range(n_th):
        th = (it + 0.5) * (math.pi / 2) / n_th
        w_th = math.sin(th) * math.cos(th)
        ct, st = math.cos(th), math.sin(th)
        for ip in range(n_phi):
            ph = (ip + 0.5) * 2.0 * math.pi / n_phi
            a = ct * cmath.exp(1j * ph)
            for iq in range(n_psi):
                ps = (iq + 0.5) * 2.0 * math.pi / n_psi
                b = st * cmath.exp(1j * ps)
                u_ent = (a, b, -b.conjugate(), a.conjugate())
                norm += w_th
                for e1 in range(4):
                    u1 = u_ent[e1]
                    row_s, row_p = m_star[e1], m_plain[e1]
                    for e2 in range(4):
                        row_s[e2] += w_th * u1 * u_ent[e2].conjugate()
                        row_p[e2] += w_th * u1 * u_ent[e2]
    eps2 = ((0, 1), (-1, 0))
    err_s = err_p = 0.0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    ex_s = 0.5 * (i == k) * (j == l)
                    ex_p = 0.5 * eps2[i][k] * eps2[j][l]
                    err_s = max(err_s,
                                abs(m_star[2 * i + j][2 * k + l] / norm
                                    - ex_s))
                    err_p = max(err_p,
                                abs(m_plain[2 * i + j][2 * k + l] / norm
                                    - ex_p))
    check("C", "C2 SU(2) quadratic moment int U_ij U*_kl dU = "
               "(1/2) delta_ik delta_jl verified ENTRYWISE (all 16 index "
               "combinations) on the deterministic Euler/S^3 midpoint "
               "grid (192 x 8 x 8), declared tolerance 1e-3",
          err_s < 1e-3, f"max entry deviation = {err_s:.2e}")
    check("C", "C3 SU(2) eps-sector moment int U_ij U_kl dU = "
               "(1/2) eps_ik eps_jl verified ENTRYWISE on the same grid, "
               "declared tolerance 1e-3 — the SU(2) baryon-link Haar "
               "factor 1/N_c! = 1/2 is this verified moment",
          err_p < 1e-3, f"max entry deviation = {err_p:.2e}")

    # C4: SU(3) — cited exact rationals + class-function cross-checks on
    # the Weyl torus grid (the grid reaches class functions ONLY; the
    # entrywise formulas are CITED constants, declared honestly) + the
    # exact-Fraction unitarity sum rule.
    ng = 64
    step = 2.0 * math.pi / ng
    s0 = sa2 = sa4 = srt3 = 0.0
    st3 = 0j
    st2 = 0j
    for i in range(ng):
        th1 = (i + 0.5) * step
        for j in range(ng):
            th2 = (j + 0.5) * step
            th3 = -(th1 + th2)
            w = (64.0
                 * math.sin((th1 - th2) / 2.0) ** 2
                 * math.sin((th1 - th3) / 2.0) ** 2
                 * math.sin((th2 - th3) / 2.0) ** 2)
            t = (cmath.exp(1j * th1) + cmath.exp(1j * th2)
                 + cmath.exp(1j * th3))
            a2 = (t * t.conjugate()).real
            s0 += w
            st3 += w * t ** 3
            st2 += w * t * t
            sa2 += w * a2
            sa4 += w * a2 * a2
            srt3 += w * t.real ** 3
    norm3 = s0 / (6.0 * ng * ng)
    grid_ok = (abs(norm3 - 1.0) < 1e-10
               and abs(st3 / s0 - 1.0) < 1e-10
               and abs(st2 / s0) < 1e-10
               and abs(sa2 / s0 - 1.0) < 1e-10
               and abs(sa4 / s0 - 2.0) < 1e-10
               and abs(srt3 / s0 - 0.25) < 1e-10)
    # Exact-Fraction side: the cited formulas' contractions.
    q = Fraction(1, 3)   # cited quadratic constant 1/N_c
    c = Fraction(1, 6)   # cited cubic constant 1/N_c!
    # unitarity sum rule: sum_j int U_ij U*_kj = delta_ik
    unit_ok = all(sum(q * (1 if i == k else 0) * 1 for _j in range(3))
                  == (1 if i == k else 0)
                  for i in range(3) for k in range(3))
    # trace contraction of the quadratic formula: <|Tr U|^2> = 1
    tr2 = sum(q * (1 if i == j else 0) * (1 if i == j else 0)
              for i in range(3) for j in range(3))
    # eps-eps contraction of the cubic formula: <(Tr U)^3> = 1
    eps3 = {}
    for p in itertools.permutations((0, 1, 2)):
        sign = 1
        pl = list(p)
        for x in range(3):
            for y in range(x + 1, 3):
                if pl[x] > pl[y]:
                    sign = -sign
        eps3[p] = sign
    tr3 = sum(c * eps3[p] * eps3[p] for p in eps3)
    check("C", "C4 SU(3): cited exact moments int U U* = "
               "(1/3) delta delta and int UUU = (1/6) eps eps "
               "(Creutz / Weingarten, parallel references) "
               "cross-checked: exact-Fraction unitarity sum rule "
               "sum_j (1/3) delta_ik delta_jj = delta_ik; trace "
               "contraction <|Tr U|^2> = 1 and eps contraction "
               "<(Tr U)^3> = 1 both REPRODUCED by the deterministic "
               "Weyl torus grid (also <Tr U^.. t^2> = 0, <|t|^4> = 2, "
               "<(Re t)^3> = 1/4; all < 1e-10) — class-function "
               "verification only, entrywise formulas consumed as cited "
               "constants (declared honestly)",
          grid_ok and unit_ok and tr2 == 1 and tr3 == 1,
          f"<t^3> = {abs(st3 / s0):.12f}, <|t|^2> = {sa2 / s0:.12f}, "
          f"<|t|^4> = {sa4 / s0:.12f}")


# ---------------------------------------------------------------------------
# Section D [C] — ARM 2: per-dimer weights and the 2-site exact Z(m).
# ---------------------------------------------------------------------------
def c_meson(n_c: int, k: int) -> Fraction:
    """Rossi-Wolff one-link mesonic coefficient c_k = (N-k)!/(N! k!)
    (c_0 trivial, c_1 = 1/N derived from the verified quadratic moment
    in the parent note; k >= 2 cited closed form, parallel reference)."""
    return Fraction(math.factorial(n_c - k),
                    math.factorial(n_c) * math.factorial(k))


def section_d():
    print("\n--- Section D [C]: ARM 2 — exact per-object weights and the "
          "2-site single-link Z(m) (exact Fractions) ---")

    # D1: meson dimer weight 1/N_c per group, tied to the verified
    # moments: coefficient of M_x M_y = (moment constant 1/N) x
    # (Grassmann reorder sign chain (-1) x (-1) = +1), by-hand
    # derivation in the parent note.
    weights = {1: Fraction(1, 1), 2: Fraction(1, 2), 3: Fraction(1, 3)}
    ok_d1 = all(c_meson(n, 1) == w for n, w in weights.items())
    check("C", "D1 meson-dimer weight (M_x M_y coefficient) = 1/N_c "
               "exactly: 1 (U(1)), 1/2 (SU(2)), 1/3 (SU(3)) — the "
               "quadratic Haar constant times the by-hand Grassmann "
               "reorder sign (+1); equals Rossi-Wolff c_1 = "
               "(N-1)!/(N! 1!) in exact Fractions; hop sign eta and the "
               "APBC wrap sign enter SQUARED and drop",
          ok_d1, "c_1: " + ", ".join(f"N={n}: {c_meson(n, 1)}"
                                     for n in (1, 2, 3)))

    # D2: baryon-link Haar factor 1/N_c! and the canonical-normalization
    # bookkeeping chain (1/3!) x (1/3!) x (3!)^2 = 1 (note section 2.3).
    chain_su3 = (Fraction(1, math.factorial(3)) * Fraction(1, 6)
                 * math.factorial(3) ** 2)
    chain_su2 = (Fraction(1, math.factorial(2)) * Fraction(1, 2)
                 * math.factorial(2) ** 2)
    check("C", "D2 baryon-link Haar moment factor = 1/N_c! exactly: 1/6 "
               "(SU(3), the cited cubic eps moment) and 1/2 (SU(2), the "
               "VERIFIED C3 eps moment); with the canonical baryon "
               "normalization B = chi^1...chi^N the full monomial "
               "coefficient chain (1/N!) x (1/N!) x (N!)^2 = 1 in exact "
               "Fractions (normalization-dependent bookkeeping, "
               "declared); U(1) has NO eps sector (C1: int U^k = 0); "
               "distinct from c_3 = (1/N_c!)^2 = 1/36 (the top mesonic "
               "coefficient)",
          chain_su3 == 1 and chain_su2 == 1
          and Fraction(1, math.factorial(3)) == Fraction(1, 6)
          and Fraction(1, math.factorial(2)) == Fraction(1, 2)
          and c_meson(3, 3) == Fraction(1, 36),
          "1/N_c! = 1/6 (SU(3)), 1/2 (SU(2)); c_3 = 1/36")

    # D3: 2-site single-link Z(m), mesonic (U(N)-moment) sector, exact:
    # Z = sum_k c_k [k! C(N,k)]^2 m^(2(N-k)) = (m^2+1)^N as a binomial
    # identity in Fractions, verified term-by-term AND by direct
    # evaluation at rational test points.
    ok_d3 = True
    details = []
    for n_c in (1, 2, 3):
        coeffs = []
        for k in range(n_c + 1):
            site = (math.factorial(k) * math.comb(n_c, k))
            coeffs.append(c_meson(n_c, k) * site * site)
        binom_ok = all(coeffs[k] == math.comb(n_c, k)
                       for k in range(n_c + 1))
        for m in (Fraction(2, 3), Fraction(3, 5)):
            z = sum(coeffs[k] * m ** (2 * (n_c - k))
                    for k in range(n_c + 1))
            binom_ok = binom_ok and z == (m * m + 1) ** n_c
        ok_d3 = ok_d3 and binom_ok
        details.append(f"N={n_c}: Z = (m^2+1)^{n_c}")
    check("C", "D3 2-site single-link Z(m), mesonic sector, exact "
               "Fractions: term-k coefficient c_k [k! C(N,k)]^2 "
               "collapses to C(N,k) exactly, so Z(m) = (m^2 + 1)^N_c — "
               "factor structure: N_c identical factors (m^2 + 1), "
               "roots m = +-i; verified term-by-term and by direct "
               "expansion at m = 2/3, 3/5 for N_c = 1, 2, 3 (c_2, c_3 "
               "cited Rossi-Wolff closed form; SU(3) baryonic eps-sector "
               "addition DECLARED out of scope — needs the unverified "
               "sixth moment)",
          ok_d3, "; ".join(details))


# ---------------------------------------------------------------------------
# Section E [A] — ARM 2: the 2^3 block Z(m) and the weight table.
# ---------------------------------------------------------------------------
CUBE_EDGES = tuple(sorted((i, i ^ (1 << mu))
                          for i in range(8) for mu in range(3)
                          if i < (i ^ (1 << mu))))
CUBE_ADJ = {v: tuple(u for e in CUBE_EDGES for x, u in (e, e[::-1])
                     if x == v) for v in range(8)}


@lru_cache(maxsize=None)
def cube_matchings(mask: int) -> tuple:
    """Counts of k-dimer matchings on the cube graph restricted to
    vertices not in mask; memoized bitmask recursion."""
    if mask == 255:
        return (1, 0, 0, 0, 0)
    v = next(i for i in range(8) if not mask & (1 << i))
    out = list(cube_matchings(mask | (1 << v)))      # monomer at v
    for u in CUBE_ADJ[v]:
        if not mask & (1 << u):
            sub = cube_matchings(mask | (1 << v) | (1 << u))
            for k in range(4):
                out[k + 1] += sub[k]
    return tuple(out)


def section_e(arm1_table):
    print("\n--- Section E [A]: ARM 2 — exact Z(m) of the 2^3 block "
          "(declared matching sector) and the per-object weight "
          "table ---")

    # E1: matching counts, two independent methods.
    counts = cube_matchings(0)
    brute = [0] * 5
    for r in range(5):
        for sub in itertools.combinations(CUBE_EDGES, r):
            vs = [v for e in sub for v in e]
            if len(set(vs)) == len(vs):
                brute[r] += 1
    sanity = (counts[0] == 1 and counts[1] == len(CUBE_EDGES) == 12)
    check("A", "E1 cube-graph (2^3 block) k-dimer matching counts by "
               "memoized bitmask recursion = (1, 12, 42, 44, 9), "
               "CONFIRMED independently by brute force over all 2^12 "
               "edge subsets; k=1 count equals the edge count 12 and "
               "the 9 perfect matchings of Q3 are reproduced",
          tuple(brute) == counts and sanity,
          f"counts = {counts}")

    # E2: Z(m) as an exact Fraction polynomial with the derived
    # doubled-edge weight w = 2/N_c.
    w_link = Fraction(1, 3)        # verified per-link dimer weight 1/N_c
    w_edge = 2 * w_link            # two parallel links (direct + APBC
    #                                wrap), signs squared -> additive
    zc = [counts[k] * w_edge ** k for k in range(5)]
    # coefficient of m^(8-2k); in t = m^2: t^(4-k)
    z_expected = [Fraction(1), Fraction(8), Fraction(56, 3),
                  Fraction(352, 27), Fraction(16, 9)]
    check("A", "E2 exact Z(m) of the declared monomer-dimer (matching) "
               "sector of the 2^3 APBC block: doubled links per cube "
               "edge collapse to multiplicity-2 edges of weight "
               "2/N_c = 2/3 (derived: per-link weight 1/N_c verified, "
               "hop and APBC signs squared, single-occupancy DECLARED); "
               "Z(m) = m^8 + 8 m^6 + (56/3) m^4 + (352/27) m^2 + 16/9 "
               "in exact Fractions",
          zc == z_expected and w_edge == Fraction(2, 3),
          "Z = " + " + ".join(f"({zc[k]}) m^{8 - 2 * k}"
                              for k in range(5)))

    # E3: factor structure.  Exact rational-root scan (rational root
    # theorem on 27 t^4 + 216 t^3 + 504 t^2 + 352 t + 48) + numeric
    # Durand-Kerner roots (FLAGGED numeric).
    pi_coeffs = [c * 27 for c in zc]          # integer coefficients in t
    assert all(c.denominator == 1 for c in pi_coeffs)
    pi_int = [int(c) for c in pi_coeffs]

    def divisors(x):
        x = abs(x)
        return [d for d in range(1, x + 1) if x % d == 0]

    cands = sorted({Fraction(p, q) for p in divisors(pi_int[-1])
                    for q in divisors(pi_int[0])})

    def eval_frac(coefs, x):
        s = Fraction(0)
        for cc in coefs:
            s = s * x + cc
        return s

    rational_roots = [s * r for r in cands for s in (1, -1)
                      if eval_frac([Fraction(c) for c in pi_int],
                                   s * r) == 0]

    mon = [float(zc[k] / zc[0]) for k in range(5)]

    def pv(z):
        s = 0j
        for cc in mon:
            s = s * z + cc
        return s

    zs = [(0.4 + 0.9j) ** k for k in range(1, 5)]
    for _ in range(200):
        zs = [z - pv(z) / math.prod([(z - o) for o in zs if o is not z],
                                    start=1 + 0j) for z in zs]
    recon = max(abs(pv(z)) for z in zs)
    roots_str = ", ".join(f"{z.real:+.6f}{z.imag:+.6f}i" for z in zs)
    no_pos_real = all(z.real < 0 or abs(z.imag) > 1e-8 for z in zs)
    check("A", "E3 factor structure of Z in t = m^2: NO rational roots "
               "(exact rational-root-theorem scan over all +-p/q, "
               "p | 48, q | 27) — no linear factor over Q; numeric "
               "roots (FLAGGED numeric, Durand-Kerner, residual "
               "< 1e-10) are all in the left half-plane (Z(m) > 0 for "
               "real m, as positivity of all coefficients requires); "
               "unlike the 2-site case Z does NOT collapse to "
               "(m^2 + 1)-power form",
          not rational_roots and recon < 1e-10 and no_pos_real,
          f"t-roots: {roots_str}")

    # E4: the per-object weight table and displacements vs alpha_s.
    table = [
        ("1/N_c    (meson dimer, per link; VERIFIED)", Fraction(1, 3)),
        ("1/(2N_c) (NJL G_eff, inventory S1 row)", Fraction(1, 6)),
        ("1/N_c!   (baryon-link Haar factor; cited+x-checked)",
         Fraction(1, 6)),
        ("1/N_c^2  (two-dimer product across two links; Weingarten "
         "fourth-moment layer ~ Wg constants 1/8, -1/24 cited "
         "parallel-reference only)", Fraction(1, 9)),
        ("2/N_c    (doubled-edge dimer weight, 2^3 block)",
         Fraction(2, 3)),
        ("c_2 = 1/12 (double dimer on one link; cited closed form)",
         Fraction(1, 12)),
    ]
    supplied_hits = []
    window_hits = []
    for label, frac in table:
        disp = float(frac) / ALPHA_S
        print(f"    weight {str(frac):>5} = {float(frac):.4f}  "
              f"displacement = {disp:.4f}x alpha_s   [{label}]")
        if 0.99 <= disp <= 1.01:
            supplied_hits.append(label)
        if 0.5 <= disp <= 2.0:
            window_hits.append((label, disp))
    check("A", "E4 per-object weight table vs alpha_s = 0.1033038: NO "
               "computed or cited beta = 0 weight lands in the "
               "'supplied' window [0.99, 1.01] x alpha_s; FOUR "
               "tabulated rationals (1/(2N_c) and 1/N_c! at 1.6134x, "
               "1/N_c^2 at 1.0756x — the closest — and c_2 = 1/12 at "
               "0.8067x) fall inside the inventory's factor-2 "
               "observation window and are flagged below as an "
               "OBSERVATION, never a closure; every weight attaches "
               "PER OBJECT (per link, dimer, or loop), NONE attaches "
               "per decimated taste mode",
          not supplied_hits and len(window_hits) == 4,
          "factor-2 window: "
          + ", ".join(f"{d:.4f}x" for _, d in window_hits))
    return table


# ---------------------------------------------------------------------------
# Section F [A] — ARM 3: the rationality obstruction and the S1' refinement.
# ---------------------------------------------------------------------------
def section_f(arm1_table, weight_table):
    print("\n--- Section F [A]: ARM 3 — rationality obstruction; S1 "
          "standalone eliminated; refinement to composite S1' ---")

    # F1: every consumed beta = 0 constant is an exact rational.
    consts = ([frac for _, frac in weight_table]
              + [c_meson(n, k) for n in (1, 2, 3) for k in range(n + 1)]
              + [Fraction(1, 2), Fraction(1, 6), Fraction(2, 3)]
              + [counts * Fraction(2, 3) ** k
                 for k, counts in enumerate(cube_matchings(0))])
    check("A", "F1 rationality (computed instances): every beta = 0 "
               "constant this probe produced or consumed — moments, "
               "dimer/baryon weights, c_k chain, both Z(m) coefficient "
               "lists — is an exact Fraction (general statement: "
               "Weingarten calculus yields rational polynomial Haar "
               "moments; cited parallel reference, consumed at the "
               "strength of these computed instances)",
          all(isinstance(x, Fraction) for x in consts)
          and len(consts) >= 20,
          f"{len(consts)} exact rationals checked")

    # F2: alpha_s carries pi; the 1/N_c^2 proximity computed exactly.
    ratio = 4.0 * math.pi * U_0 ** 2 / 9.0
    would_be = math.pi * U_0 ** 2          # 'pi u_0^2 = 9/4' would-be
    off = would_be / 2.25 - 1.0
    gaps = sorted(abs(float(f) - ALPHA_S) / ALPHA_S
                  for _, f in weight_table)
    check("A", "F2 alpha_s = 1/(4 pi u_0^2) is pi-carrying: if it were "
               "rational, pi = 1/(4 u_0^2 alpha_s) would be algebraic "
               "(u_0^2 = sqrt(5934/10000) is algebraic), contradicting "
               "Lindemann (parallel reference) — so NO finite product/"
               "sum of beta = 0 rational link-integration constants "
               "equals alpha_s EXACTLY; numerically the nearest "
               "tabulated rational (1/N_c^2) sits 7.56% away "
               "(4 pi u_0^2/9 = 1.0756), i.e. the would-be identity "
               "'pi u_0^2 = 9/4' fails at 7.56%",
          min(gaps) > 0.07 and abs(ratio - 1.0756) < 5e-4
          and abs(off - 0.0756) < 5e-3,
          f"4 pi u_0^2/9 = {ratio:.6f}; pi u_0^2 = {would_be:.6f} vs "
          f"9/4 = 2.25 ({100 * off:.2f}% off); min rational gap = "
          f"{100 * min(gaps):.2f}%")

    # F3: the elimination logic and the S1 -> S1' refinement.
    beta6_ok = all(not (0.5 <= arm1_table[v][1] <= 2.0)
                   and not (0.5 <= arm1_table[v][3] <= 2.0)
                   for v, _, _ in VARIANTS)
    beta0_ok = all(not (0.99 <= float(f) / ALPHA_S <= 1.01)
                   for _, f in weight_table)
    check("A", "F3 elimination logic: at beta = 0 EXACT supply of "
               "alpha_s per decoupling by link integration alone is "
               "impossible (F2 rationality obstruction) and no computed "
               "per-object weight is alpha_s (E4); at one-link-exact "
               "beta = 6 the per-decimation factor is 9.68x-10.6x "
               "displaced in every declared variant, bath convention, "
               "and stress bracket (B3/B4) — the inventory's S1 kill "
               "criterion fires; S1 STANDALONE is eliminated, and the "
               "4 pi's only landed supplier remains the Green-kernel/"
               "Plancherel readout chain, so S1 REFINES to the "
               "composite S1' (finite-beta link integration COMPOSITED "
               "with the readout kernel chain: group-theory rationals "
               "from links, the 4 pi from the kernel)",
          beta6_ok and beta0_ok,
          "min beta=6 displacement = "
          + f"{min(arm1_table[v][1] for v, _, _ in VARIANTS):.3f}x")


# ---------------------------------------------------------------------------
# Section G [B] — document scans.
# ---------------------------------------------------------------------------
def section_g():
    print("\n--- Section G [B]: upstream notes, licenses, and parent-note "
          "fences on disk ---")

    inv = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_"
                  "SYNTHESIS_NOTE_2026-06-11.md")
    inv_flat = " ".join(inv.read_text().split()) if inv.exists() else ""
    check("B", "G1 route-inventory synthesis on disk: names S1 "
               "('strong-coupling one-link Haar / Kawamoto-Smit "
               "lineage'), states the kill criterion this probe "
               "executes ('an exact one-link computation whose "
               "per-decoupling factor is O(1)-displaced...'), the NJL "
               "leading-order constraint (G_eff = 1/(2 N_c) = 1/6), and "
               "the non-modification rule this note obeys",
          "strong-coupling one-link Haar / Kawamoto-Smit lineage"
          in inv_flat
          and ("an exact one-link computation whose per-decoupling "
               "factor is O(1)-displaced") in inv_flat
          and "G_eff = 1/(2 N_c) = 1/6" in inv_flat
          and "refine routes without modifying the inventory" in inv_flat)

    b02 = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                  "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    b02_flat = " ".join(b02.read_text().split()) if b02.exists() else ""
    plaq_text = (DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md").read_text()
    fourpi = (DOCS / "ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_"
                     "BOUNDED_NOTE_2026-05-26.md")
    fourpi_flat = " ".join(fourpi.read_text().split()) \
        if fourpi.exists() else ""
    check("B", "G2 supplier chain on disk: block02 records the target "
               "'alpha_s = 0.1033038' 'per taste decoupling'; the B1 "
               "plaquette license ('admitted comparison/reuse number', "
               "0.5934) covers this probe's u_0; the landed 4 pi "
               "supplier is the Z3 Plancherel/Green-kernel bridge "
               "('alpha_bare = 1 / (4 pi)', 'G(r) -> 1/(4 pi |r|)') — "
               "the kernel chain S1' composites with",
          "alpha_s = 0.1033038" in b02_flat
          and "per taste decoupling" in b02_flat
          and "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text
          and "alpha_bare = 1 / (4 pi)" in fourpi_flat
          and "G(r) -> 1/(4 pi |r|)" in fourpi_flat
          and "Plancherel" in fourpi_flat)

    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "declared model",
        "does not close the delta0 gate",
        "numerology-risk",
        "composite route s1'",
        "not removed",
        "what this note does not claim",
    ]
    forbidden = [
        "closes the delta0 gate",
        "derives the attachment",
        "supplies the attachment rule",
        "pi u_0^2 = 9/4 holds",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "G3 parent-note honesty fences on disk: labels the bath "
               "and matching sector 'declared model' content, records "
               "the S1 -> S1' refinement ('composite route S1''), "
               "marks the 1/N_c^2 proximity 'numerology-risk', states "
               "the S1 row is refined and 'NOT removed', and 'does not "
               "close the DELTA0 gate'; forbidden closure tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")


# ---------------------------------------------------------------------------
# Residuals, observation, terminal class-D fence.
# ---------------------------------------------------------------------------
def section_residuals():
    print()
    residual("the alpha_s PER-DECOUPLING ATTACHMENT rule (block02 R1) "
             "remains UNSUPPLIED.  This probe ELIMINATES route S1 "
             "STANDALONE: at beta = 0 exact Haar link integration "
             "yields only rationals and cannot exactly supply the "
             "pi-carrying alpha_s = 1/(4 pi u_0^2) (Arm 3); at "
             "one-link-exact beta = 6 the per-decimation factor is "
             "9.68x-10.6x displaced under every declared variant, bath "
             "convention, and stress bracket (Arm 1, declared bath).")
    residual("the surviving content of S1 REFINES to the composite "
             "route S1' (declared-open, NOT probed here): finite-beta "
             "link integration COMPOSITED with the Green-kernel/"
             "Plancherel readout chain — group-theory rationals from "
             "the links, the 4 pi from the kernel.  Neither a closing "
             "nor an eliminating computation for S1' has been "
             "performed; the inventory is NOT modified.")
    residual("the DELTA0 magnitude gate (HIERARCHY_ALPHA_LM_MAGNITUDE_"
             "DELTA0_OPEN_GATE_NOTE_2026-05-30.md) remains OPEN: the "
             "obstruction is sharpened (S1 standalone eliminated, "
             "composite S1' identified), not closed.")
    print()
    observation("1/N_c^2 = 0.1111 sits 1.0756x from the required "
                "alpha_s = 0.1033038 — INSIDE the inventory's factor-2 "
                "observation window.  Where it arises in the computed "
                "structures: two-dimer products across two links "
                "((1/N_c)^2), c_3 = 1/36 = (1/N_c!)^2, and the "
                "fourth-moment Weingarten layer (U(3) constants "
                "Wg ~ 1/(N^2-1) = 1/8 and -1/(N(N^2-1)) = -1/24, cited "
                "parallel-reference only, NOT verified here).  NO "
                "per-threshold attachment of one 1/N_c^2 per decimated "
                "mode is derivable from anything computed here: every "
                "weight attaches per OBJECT, and the would-be identity "
                "'pi u_0^2 = 9/4' fails at 7.56%.  Three MORE tabulated "
                "rationals also fall in the factor-2 window (1/(2N_c) "
                "and 1/N_c! at 1.6134x, c_2 = 1/12 at 0.8067x) — small "
                "rationals populate a factor-2 window generically, "
                "which is itself the strongest reason to distrust the "
                "proximity.  NUMEROLOGY RISK: no supplier, no "
                "mechanism, no claim.")


def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; all "
          "factors and weights")
    print("   are internal structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "H1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_s1_exact_one_link_strong_coupling_"
          "probe_2026_06_11.py")
    print(" Block09 of the DELTA0 blocking campaign: executing the "
          "inventory's S1 kill")
    print(" criterion.  ARM 1: exact one-link expectation at the fixed "
          "E3 saddle bath,")
    print(" beta = 6 (E3 machinery reused verbatim).  ARM 2: exact "
          "beta = 0 Haar")
    print(" moments as Fractions; per-dimer/baryon weights; 2-site and "
          "2^3 exact Z(m).")
    print(" ARM 3: the rationality obstruction — beta = 0 link "
          "integration yields only")
    print(" rationals; alpha_s = 1/(4 pi u_0^2) carries pi; S1 "
          "standalone eliminated,")
    print(" refines to composite S1' (links x readout kernel chain).")
    print(" Parent note: docs/HIERARCHY_DELTA0_S1_EXACT_ONE_LINK_STRONG_"
          "COUPLING_PROBE_")
    print("              NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    arm1_table = section_b()
    section_c()
    section_d()
    weight_table = section_e(arm1_table)
    section_f(arm1_table, weight_table)
    section_g()
    section_residuals()
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded): the exact one-link "
          "expectation at the fixed")
    print("   E3 saddle bath gives a per-decimation factor "
          "9.68x-10.6x displaced from")
    print("   alpha_s in every declared variant at beta = 6 (the link "
          "integral was")
    print("   always exact; the bath is the declared model); at "
          "beta = 0 every link-")
    print("   integration constant is an exact rational, so the "
          "pi-carrying alpha_s")
    print("   cannot be supplied exactly by beta = 0 link integration "
          "at all.  S1")
    print("   STANDALONE is eliminated at its kill criterion; the "
          "surviving content")
    print("   REFINES to the composite route S1' = finite-beta link "
          "integration x the")
    print("   Green-kernel/Plancherel readout chain (the 4 pi's only "
          "landed supplier).")
    print("   NOT claimed: closure, any licensed-surface reproduction, "
          "any model-")
    print("   independent statement, or any content for the 1/N_c^2 "
          "proximity beyond")
    print("   a numerology-risk-flagged observation.  DELTA0 stays "
          "open; the inventory")
    print("   is not modified.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
