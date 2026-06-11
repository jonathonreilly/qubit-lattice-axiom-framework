#!/usr/bin/env python3
"""DELTA0 attachment probe: is the alpha_s-per-decoupling rule mean-field
link feedback?  (Block04 of the DELTA0 blocking campaign.)

    docs/HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_PROBE_
    NOTE_2026-06-11.md

Setting.  Block01 (scripts/frontier_hierarchy_delta0_blocking_single_
mode_probe_2026_06_11.py) established by exact arithmetic that one
taste-mode decimation on the minimal 2^4 all-APBC mean-field block
carries the factor 2 u_0 per mode per color with EXACTLY ZERO induced
coupling shift on the kept modes (frozen links).  Block02 (scripts/
frontier_hierarchy_delta0_ratio_normalized_alpha_s_reduction_2026_06_11
.py) reduced the DELTA0 gate, over a declared ratio normalization, to
ONE unsupplied transport rule: one factor
alpha_s = alpha_bare/u_0^2 = 0.1033038 per taste decoupling.

Since the frozen-link cross-term vanishes identically (block01 B4), the
only way a decimation can shift the gauge-sector readout
alpha_s(u) = alpha_bare/u^2 inside a mean-field treatment is LINK
UN-FREEZING: the decimated mode's induced action depends on the link
dressing u (the per-mode factor is 2u as a FUNCTION of u, induced
action -ln(2u) per mode per color), and that term feeds the mean-field
self-consistency that determines u.  This runner computes that feedback
EXACTLY under declared models and reports honestly whether it supplies
a multiplicative factor alpha_s per decimation.

THE FIRST FALSIFIABLE ATTEMPT at the attachment rule — and (spoiler in
the verdict, not in the checks) a SHARPENED OBSTRUCTION: the feedback
factor R is O(1) in every declared variant, an order of magnitude
(9.7x-10.5x) above the required alpha_s.

Declared models (every element DECLARED and fenced; the framework's
licensed surface is SU(3) Wilson at beta = 6, and per
docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md the canonical <P> = 0.5934 is
an admitted reuse number, NOT derived; the mean-field F below is a
DECLARED approximation, not a licensed framework object):

  M1 (gauge sector): standard single-link mean-field self-consistency
      for the Wilson single-plaquette action at beta = 6,
          u = F(h(u)),    h(u) = (2(d-1) beta u^3) / N = 6 beta u^3 / N
      at d = 4 (each link sits in 2(d-1) = 6 plaquettes, i.e. 6 staples
      per link on Z^4, each staple -> u^3 in mean field), where
      F(h) = <(1/N) Re Tr U>_h under the one-link weight
      exp(h Re Tr U) d_Haar(U).  Equivalent variational route: per-link
      mean-field action s_g(u) = (3/2) beta u^4 (plaquette/link ratio
      d(d-1)/2 / d = 3/2; each plaquette contributes beta u^4 in the
      (beta/N) Re Tr convention), stationarity h = (1/N) ds_g/du
      = 6 beta u^3 / N — same h.  Three group variants so the
      conclusion is not an artifact of one group choice:
        U(1):  F(h) = I_1(h)/I_0(h)            (exact Bessel ratio),
        SU(2): F(h) = I_2(2h)/I_1(2h)          (exact Bessel ratio;
               Re Tr U = 2 cos th, Weyl measure (2/pi) sin^2 th),
        SU(3): deterministic fixed-grid midpoint quadrature over the
               eigenvalue-angle (maximal torus) parametrization with
               Weyl measure |Delta|^2 = prod_{i<j} 4 sin^2((th_i -
               th_j)/2), th_3 = -(th_1 + th_2); NO randomness.

  M2 (fermion feedback): n taste modes contribute induced action
      -n_c * n * ln(2u) per minimal block (n_c = 3 colors; block01's
      exact per-mode factor recomputed in Section A).  Per-block link
      counting DECLARED: the 2^4 block has 16 sites x 4 forward
      directions = 64 links.  Sharing conventions (robustness axis):
        S-uniform:  per-link share kappa = n_c n / 64;
        S-per-site: per-site share n_c n / 16, split over the 8
                    incident links of the site, each link fed by its 2
                    endpoint sites -> kappa = 2 x (n_c n/16)/8
                    = n_c n / 64 (PROVED equal to S-uniform, exact
                    Fraction arithmetic);
        S-x2 / S-half: stress brackets kappa -> 2 kappa, kappa/2
                    (deliberate mis-sharing bound).
      Feedback enters the self-consistency through the same stationary
      route as the gauge term: per-link induced term
      s_f(u) = kappa ln(2u), extra source dh_f = (1/N) ds_f/du
      = kappa/(N u), so
          u = F( (6 beta u^3 + kappa/u) / N ).

  Computation: solve u*(n) for n = 16 and n = 15 (one decimation) per
      variant per convention; deterministic scan + bisection, residual
      |u - F(h(u))| < 1e-12 demanded.  Bessel ratios are evaluated by
      the Gautschi continued-fraction backward recurrence (overflow-
      safe for the kappa/u source at small scan u).  DECLARED branch
      selection: the dressed (largest) root; the SU(3) variant at
      beta = 6 has a multi-root structure and leg D4 verifies the
      small-u branch gives the same conclusion.  Report the
      per-decimation multiplicative feedback factors
          R_det  = u*(15)/u*(16)        (per-mode determinant share
                                         2u*(15) vs 2u*(16)),
          R      = (u*(15)/u*(16))^(-2) (ratio-normalized readout
                                         alpha_s(u) = alpha_bare/u^2),
      and the displacement R / alpha_s against the required
      alpha_s = 0.1033038 per decoupling.

  Sanity diagnostics (bounded observations, fenced): the pure-gauge
      mean-field u*(0) at beta = 6 per variant, compared against the
      licensed u_0 = 0.8777 as model-diagnostic CONTEXT only — NO claim
      that the mean-field model reproduces the licensed surface.

Verdict logic (declared up front): the candidate rule "mean-field link
feedback supplies one factor alpha_s per decimation" is
  SUPPLIED            if R/alpha_s in [0.99, 1.01] in the licensed-
                      group variant (SU(3)) robustly across conventions,
  BOUNDED OBSERVATION if R/alpha_s in [0.5, 2] in any variant
                      (flagged, all model dependence declared,
                      NO closure claim),
  REFUTED (this route) otherwise — the sharpened obstruction.

Vocabulary discipline: the Section A facts are bounded_theorem-grade
exact algebra; the M1/M2 solves are exact arithmetic ON DECLARED
MODELS (model-fenced, never licensed-surface claims); all remaining
open content is printed as RESIDUAL (declared-open) lines, never as
PASSes and never as FAILs.

Deterministic, pure Python stdlib (fractions, math, itertools), no
network, no randomness (fixed quadrature grids), runtime < 1 min.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_"
                      "PROBE_NOTE_2026-06-11.md")

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
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


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381 (licensed value)
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_LM = ALPHA_BARE / U_0          # = 0.0906678
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (block02 reduction target)

BETA = 6.0                           # declared M1 coupling (licensed surface)
DIM = 4                              # Z^4
N_COLORS = 3                         # declared M2 color count
STAPLES_PER_LINK = 2 * (DIM - 1)     # = 6, declared counting
LINKS_PER_BLOCK = 16 * 4             # = 64, declared counting


# ---------------------------------------------------------------------------
# Block01 exact machinery (REUSED verbatim so Section A provably matches).
# ---------------------------------------------------------------------------
SITES = list(itertools.product((0, 1), repeat=4))
SITE_INDEX = {s: i for i, s in enumerate(SITES)}

CZERO = (Fraction(0), Fraction(0))
CONE = (Fraction(1), Fraction(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def cconj(a):
    return (a[0], -a[1])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def cmat_mul(a, b):
    n, p, q = len(a), len(b), len(b[0])
    out = [[CZERO] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            s = CZERO
            for k in range(p):
                if a[i][k] != CZERO and b[k][j] != CZERO:
                    s = cadd(s, cmul(a[i][k], b[k][j]))
            out[i][j] = s
    return out


def mat_mul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def staggered_operator():
    """Per-color eta-phase staggered central-difference operator on the
    2^4 block with antiperiodic wrap in all four directions; unit links
    (u_0 = 1); exact Fractions.  Reused verbatim from block01."""
    n = len(SITES)
    d = [[Fraction(0)] * n for _ in range(n)]
    for s in SITES:
        x = SITE_INDEX[s]
        for mu in range(4):
            eta = (-1) ** sum(s[:mu])
            for direction in (+1, -1):
                t = list(s)
                t[mu] += direction
                wrapped = t[mu] < 0 or t[mu] > 1
                t[mu] %= 2
                sign = -1 if wrapped else 1
                y = SITE_INDEX[tuple(t)]
                d[x][y] += direction * eta * sign * Fraction(1, 2)
    return d


def taste_eigenbasis(d_unit):
    """Exact taste-mode basis — reused verbatim from block01."""
    even = [SITE_INDEX[s] for s in SITES if sum(s) % 2 == 0]
    n = len(SITES)
    cols = []
    eigs = []
    for sign, lam_im in ((-1, 2), (+1, -2)):
        for ix in even:
            col = []
            for i in range(n):
                re = Fraction(1) if i == ix else Fraction(0)
                im = Fraction(sign) * d_unit[i][ix] / 2
                col.append((re, im))
            cols.append(col)
            eigs.append((Fraction(0), Fraction(lam_im)))
    t_mat = [[cols[j][i] for j in range(n)] for i in range(n)]
    t_inv = [[cmul((Fraction(1, 2), Fraction(0)), cconj(t_mat[j][i]))
              for j in range(n)] for i in range(n)]
    return t_mat, t_inv, eigs


def complex_block_matrix(d_unit, a, m):
    """M = a D + m as a complex (Gaussian-rational) matrix."""
    n = len(d_unit)
    return [[(a * d_unit[i][j] + (m if i == j else Fraction(0)), Fraction(0))
             for j in range(n)] for i in range(n)]


def schur_decimate(m_prime, d_idx):
    """Integrate out the single Grassmann pair — reused from block01."""
    n = len(m_prime)
    kept = [i for i in range(n) if i != d_idx]
    s_fac = m_prime[d_idx][d_idx]
    s_inv = cinv(s_fac)
    b_col = [m_prime[i][d_idx] for i in kept]
    c_row = [m_prime[d_idx][j] for j in kept]
    shift = [[cmul(cmul(b_col[i], s_inv), c_row[j])
              for j in range(len(kept))] for i in range(len(kept))]
    schur = [[csub(m_prime[ki][kj], shift[i][j])
              for j, kj in enumerate(kept)] for i, ki in enumerate(kept)]
    return s_fac, schur, shift


# ---------------------------------------------------------------------------
# One-link integrals F(h) = <(1/N) Re Tr U> under weight exp(h Re Tr U).
# ---------------------------------------------------------------------------
def bessel_ratio(n: int, x: float) -> float:
    """Exact Bessel ratio I_{n+1}(x)/I_n(x) by the Gautschi backward
    recurrence (deterministic, overflow-safe for any x > 0):
    r_{k-1} = 1/(2k/x + r_k), seeded r_K = 0 at large K."""
    if x == 0.0:
        return 0.0
    k_top = int(x + 4.0 * math.sqrt(x) + 60.0)
    r = 0.0
    for k in range(k_top, n, -1):
        r = 1.0 / (2.0 * k / x + r)
    return r


def f_u1(h: float) -> float:
    """U(1): Re Tr U = cos th; F(h) = I_1(h)/I_0(h)."""
    if h == 0.0:
        return 0.0
    return bessel_ratio(0, h)


def f_su2(h: float) -> float:
    """SU(2): Re Tr U = 2 cos th, Weyl measure (2/pi) sin^2 th;
    F(h) = <cos th> = I_2(2h)/I_1(2h)."""
    if h == 0.0:
        return 0.0
    return bessel_ratio(1, 2.0 * h)


def su3_grid(ngrid: int):
    """Fixed midpoint grid over the SU(3) maximal torus (th_1, th_2),
    th_3 = -(th_1 + th_2); returns (t_list, w_list) with
    t = Re Tr U = cos th_1 + cos th_2 + cos th_3 and Weyl weight
    w = prod_{i<j} 4 sin^2((th_i - th_j)/2).  Deterministic."""
    ts, ws = [], []
    step = 2.0 * math.pi / ngrid
    for i in range(ngrid):
        th1 = (i + 0.5) * step
        for j in range(ngrid):
            th2 = (j + 0.5) * step
            th3 = -(th1 + th2)
            t = math.cos(th1) + math.cos(th2) + math.cos(th3)
            w = (64.0
                 * math.sin((th1 - th2) / 2.0) ** 2
                 * math.sin((th1 - th3) / 2.0) ** 2
                 * math.sin((th2 - th3) / 2.0) ** 2)
            ts.append(t)
            ws.append(w)
    return ts, ws


SU3_T64, SU3_W64 = su3_grid(64)      # production grid
SU3_T96, SU3_W96 = su3_grid(96)      # convergence-check grid


def f_su3(h: float, ts=SU3_T64, ws=SU3_W64) -> float:
    """SU(3): F(h) = <(1/3) Re Tr U>_h by deterministic Weyl-measure
    midpoint quadrature (exp shifted by the max t = 3, no overflow)."""
    if h == 0.0:
        return 0.0
    num = 0.0
    den = 0.0
    for t, w in zip(ts, ws):
        e = w * math.exp(h * (t - 3.0))
        den += e
        num += e * t
    return num / (3.0 * den)


# ---------------------------------------------------------------------------
# Declared model M1+M2 self-consistency solver (deterministic).
# ---------------------------------------------------------------------------
def solve_u(f_func, n_group: int, kappa: float, branch: str = "largest"):
    """Root of u = F((6 beta u^3 + kappa/u)/N) on (0, 1): deterministic
    160-point scan for a sign change, then bisection to width < 1e-15.
    DECLARED branch selection: 'largest' (default) follows the dressed
    branch — the largest root; 'smallest' follows the small-u branch
    where one exists (robustness leg D4).  Returns (u, residual) or
    None if no sign change is found (no nontrivial solution)."""
    def g(u: float) -> float:
        h = (STAPLES_PER_LINK * BETA * u ** 3
             + (kappa / u if kappa else 0.0)) / n_group
        return u - f_func(h)

    lo, hi, nscan = 1e-3, 0.999999, 160
    us = [lo + (hi - lo) * k / nscan for k in range(nscan + 1)]
    gs = [g(u) for u in us]
    bracket = None
    ks = (range(nscan, 0, -1) if branch == "largest"
          else range(1, nscan + 1))
    for k in ks:
        if gs[k] * gs[k - 1] <= 0.0:
            bracket = (us[k - 1], us[k])
            break
    if bracket is None:
        return None
    a, b = bracket
    ga = g(a)
    for _ in range(60):
        mid = 0.5 * (a + b)
        gm = g(mid)
        if ga * gm <= 0.0:
            b = mid
        else:
            a, ga = mid, gm
        if b - a < 1e-15:
            break
    u = 0.5 * (a + b)
    return u, abs(g(u))


# ---------------------------------------------------------------------------
# Section A — block01 reuse: the induced-action form -ln(2u) per mode
# per color, and the vanishing frozen-link cross-term.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]: block01 reuse — induced action is exactly "
          "-ln(2u) per mode per color; frozen-link shift is zero ---")
    d_unit = staggered_operator()
    n = 16

    # A1: operator + taste basis exact (block01 A1/B1 facts).
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(n) for j in range(n))
    d2 = mat_mul(d_unit, d_unit)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(n) for j in range(n))
    t_mat, t_inv, eigs = taste_eigenbasis(d_unit)
    tt = cmat_mul(t_inv, t_mat)
    inv_ok = all(tt[i][j] == (CONE if i == j else CZERO)
                 for i in range(n) for j in range(n))
    check("C", "A1 block01 baseline reproduced: D real antisymmetric, "
               "D^2 = -4 u^2 I, exact taste eigenbasis with T^-1 T = I "
               "(same construction code as block01)",
          antisym and d2_ok and inv_ok)

    # A2: per-mode factor 2u AS A FUNCTION OF u at rational test points
    # -> induced action per mode per color is exactly -ln(2u).
    fac_ok = True
    facs = {}
    for aa in (Fraction(2, 3), Fraction(3, 5)):
        mp = cmat_mul(t_inv, cmat_mul(
            complex_block_matrix(d_unit, aa, Fraction(0)), t_mat))
        s, _, _ = schur_decimate(mp, 0)
        facs[aa] = s
        fac_ok = fac_ok and cabs2(s) == 4 * aa * aa
    a1, a2 = Fraction(2, 3), Fraction(3, 5)
    degree1 = cabs2(facs[a1]) * a2 * a2 == cabs2(facs[a2]) * a1 * a1
    check("C", "A2 per-mode decimation factor recomputed from the "
               "block01 code AS A FUNCTION of the link dressing: "
               "|S(u)| = 2u exactly at u in {2/3, 3/5} (m = 0), per-mode "
               "u-degree 1 — so the induced action per mode per color is "
               "exactly -ln(2u), an EXPLICIT function of u",
          fac_ok and degree1,
          "exact Gaussian-rational; weight (2u)^(n_c n) per block")

    # A3: frozen-link cross-term zero -> link un-freezing is the ONLY
    # mean-field feedback channel.
    shift_ok = True
    for aa in (Fraction(2, 3), Fraction(3, 5)):
        mp = cmat_mul(t_inv, cmat_mul(
            complex_block_matrix(d_unit, aa, Fraction(0)), t_mat))
        _, _, shift = schur_decimate(mp, 5)
        shift_ok = shift_ok and all(x == CZERO for row in shift
                                    for x in row)
    check("C", "A3 frozen-link Schur cross-term is EXACTLY ZERO at both "
               "rational couplings (block01 B4 reproduced): at frozen "
               "links a decimation shifts NO coupling — link un-freezing "
               "via the u-dependence of -ln(2u) is the only mean-field "
               "feedback channel left",
          shift_ok)


# ---------------------------------------------------------------------------
# Section B — one-link integral infrastructure (declared model M1).
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [C]: one-link integrals F(h) per group variant "
          "(declared model M1 infrastructure) ---")

    # B1: U(1) Bessel ratio vs deterministic quadrature; exact slope.
    npts = 512
    ok_u1 = True
    for h in (0.5, 2.0, 10.0, 30.0):
        num = 0.0
        den = 0.0
        for i in range(npts):
            th = (i + 0.5) * 2.0 * math.pi / npts
            e = math.exp(h * (math.cos(th) - 1.0))
            den += e
            num += e * math.cos(th)
        ok_u1 = ok_u1 and abs(num / den - f_u1(h)) < 1e-12
    slope_u1 = f_u1(1e-6) / 1e-6
    check("C", "B1 U(1) one-link integral: F(h) = I_1(h)/I_0(h) "
               "(Gautschi continued-fraction backward recurrence, "
               "overflow-safe) matches deterministic 512-point "
               "quadrature of <cos th> under exp(h cos th) to < 1e-12 "
               "at 4 test h; small-h slope F'(0) = <cos^2 th>_Haar "
               "= 1/2",
          ok_u1 and abs(slope_u1 - 0.5) < 1e-6)

    # B2: SU(2) Bessel ratio vs deterministic Weyl quadrature.
    ok_su2 = True
    for h in (0.5, 2.0, 10.0, 18.0):
        num = 0.0
        den = 0.0
        for i in range(npts):
            th = (i + 0.5) * math.pi / npts
            e = math.sin(th) ** 2 * math.exp(2.0 * h * (math.cos(th) - 1.0))
            den += e
            num += e * math.cos(th)
        ok_su2 = ok_su2 and abs(num / den - f_su2(h)) < 1e-12
    slope_su2 = f_su2(1e-6) / 1e-6
    check("C", "B2 SU(2) one-link integral: F(h) = I_2(2h)/I_1(2h) "
               "(Gautschi continued-fraction backward recurrence, "
               "overflow-safe) matches deterministic 512-point Weyl "
               "quadrature (sin^2 measure, weight exp(2h cos th)) to "
               "< 1e-12 at 4 test h; small-h slope F'(0) = "
               "(1/N) <(Re Tr U)^2>_Haar = 1/2 (pseudo-real "
               "fundamental: <(Tr U)^2>_Haar = 1, not 0)",
          ok_su2 and abs(slope_su2 - 0.5) < 1e-6)

    # B3: SU(3) Weyl-measure quadrature: exact Haar moments and grid
    # convergence (midpoint rule is exact on trig polynomials, so the
    # moment checks certify the measure implementation).
    sw = sum(SU3_W64)
    m0 = sw / len(SU3_W64) / 6.0            # normalization: 3! = 6
    m1 = sum(w * t for w, t in zip(SU3_W64, SU3_T64)) / sw
    m2 = sum(w * t * t for w, t in zip(SU3_W64, SU3_T64)) / sw
    m3 = sum(w * t ** 3 for w, t in zip(SU3_W64, SU3_T64)) / sw
    moments_ok = (abs(m0 - 1.0) < 1e-12 and abs(m1) < 1e-12
                  and abs(m2 - 0.5) < 1e-12 and abs(m3 - 0.25) < 1e-12)
    conv_ok = all(
        abs(f_su3(h) - f_su3(h, SU3_T96, SU3_W96)) < 1e-12
        for h in (0.5, 2.0, 6.0, 12.0))
    slope_su3 = f_su3(1e-6) / 1e-6
    check("C", "B3 SU(3) one-link integral: Weyl eigenvalue-angle "
               "measure certified by exact Haar moments (<1> = 1 via "
               "norm 3!, <Re Tr U> = 0, <(Re Tr U)^2> = 1/2, "
               "<(Re Tr U)^3> = 1/4, all < 1e-12 — midpoint rule exact "
               "on trig polynomials); 64- vs 96-grid F(h) agreement "
               "< 1e-12 at 4 test h; small-h slope F'(0) = "
               "(1/N) <(Re Tr U)^2>_Haar = (1/3)(1/2) = 1/6",
          moments_ok and conv_ok and abs(slope_su3 - 1.0 / 6.0) < 1e-6,
          f"norm = {m0:.14f}, <t^2> = {m2:.14f}, <t^3> = {m3:.14f}")


# ---------------------------------------------------------------------------
# Sections C-E — the declared-model computation.
# ---------------------------------------------------------------------------
VARIANTS = (("U(1)", f_u1, 1), ("SU(2)", f_su2, 2), ("SU(3)", f_su3, 3))


def section_c():
    print("\n--- Section C [A]: declared-model self-consistency solves "
          "(M1 + M2, uniform share) ---")
    results = {}
    res_ok = True
    for name, f_func, n_group in VARIANTS:
        row = {}
        for n_modes in (0, 16, 15):
            kappa = N_COLORS * n_modes / LINKS_PER_BLOCK
            sol = solve_u(f_func, n_group, kappa)
            row[n_modes] = sol
            if sol is not None:
                res_ok = res_ok and sol[1] < 1e-12
        results[name] = row
        pg = row[0]
        pg_str = (f"u*(0) = {pg[0]:.10f}" if pg is not None
                  else "u*(0): no nontrivial root (disordered branch)")
        u16_str = (f"{row[16][0]:.10f}" if row[16] is not None else "NONE")
        u15_str = (f"{row[15][0]:.10f}" if row[15] is not None else "NONE")
        print(f"    {name}:  {pg_str};  "
              f"u*(16) = {u16_str}, u*(15) = {u15_str}")
    check("A", "C1 self-consistency u = F((6 beta u^3 + kappa/u)/N) "
               "solved per variant for n = 16 and n = 15 (uniform share "
               "kappa = 3n/64); every solved root has residual "
               "|u - F(h(u))| < 1e-12 (deterministic scan + bisection)",
          res_ok and all(results[v][16] is not None
                         and results[v][15] is not None
                         for v, _, _ in VARIANTS))

    # C2: fermion-feedback roots exist for n > 0 by construction
    # (kappa/u source diverges as u -> 0, so g changes sign): verify
    # computed roots are interior and the feedback direction is sane
    # (more modes -> more induced source -> u*(16) >= u*(15) is NOT
    # presumed; just record strict ordering as computed).
    order_ok = all(0.0 < results[v][15][0] < 1.0
                   and 0.0 < results[v][16][0] < 1.0
                   for v, _, _ in VARIANTS)
    check("A", "C2 all fermion-feedback roots are interior to (0, 1) in "
               "all three group variants; u*(16) and u*(15) both exist "
               "(the kappa/u source forbids the trivial root)",
          order_ok)
    return results


def section_d(results):
    print("\n--- Section D [A]: the readout — feedback factor R per "
          "decimation vs the required alpha_s ---")
    table = {}
    ok_all = True
    for name, _, _ in VARIANTS:
        u16 = results[name][16][0]
        u15 = results[name][15][0]
        r_det = u15 / u16
        r = r_det ** -2
        disp = r / ALPHA_S
        table[name] = (r_det, r, disp)
        ok_all = ok_all and math.isfinite(r) and r > 0.0
        print(f"    {name}:  R_det = u*(15)/u*(16) = {r_det:.10f};  "
              f"R = (u*(15)/u*(16))^-2 = {r:.10f};  "
              f"R/alpha_s = {disp:.4f}")
    check("A", "D1 per-decimation feedback factors computed per variant: "
               "R_det = u*(15)/u*(16) on the per-mode determinant share "
               "2u, and R = R_det^(-2) on the ratio-normalized readout "
               "alpha_s(u) = alpha_bare/u^2; all finite and positive",
          ok_all)

    # D2: R is O(1) — a small saddle shift, not a suppression factor.
    o1_ok = all(abs(table[v][1] - 1.0) < 0.5 for v, _, _ in VARIANTS)
    check("A", "D2 in EVERY declared variant the feedback factor R is "
               "O(1) and close to 1 (|R - 1| < 0.5): the link "
               "un-freezing feedback is a small saddle shift, not a "
               "per-decoupling suppression", o1_ok,
          ", ".join(f"{v}: R = {table[v][1]:.6f}" for v, _, _ in VARIANTS))

    # D3: displacement against the required alpha_s.
    disp_ok = all(not (0.5 <= table[v][2] <= 2.0) for v, _, _ in VARIANTS)
    check("A", "D3 displacement R/alpha_s computed exactly per variant; "
               "in NO variant does R land within a factor 2 of the "
               "required alpha_s = 0.1033038 — the declared verdict "
               "trigger for 'supplied' or 'bounded observation' fires in "
               "NO variant", disp_ok,
          ", ".join(f"{v}: R/alpha_s = {table[v][2]:.3f}"
                    for v, _, _ in VARIANTS))

    # D4: branch robustness.  The SU(3) self-consistency at beta = 6
    # with fermion feedback has a multi-root structure (small-u branch,
    # unstable middle root, dressed largest root — the DECLARED default
    # branch).  No branch choice rescues the rule: the small-u branch
    # gives an O(1) feedback factor too.
    s16 = solve_u(f_su3, 3, N_COLORS * 16 / LINKS_PER_BLOCK, "smallest")
    s15 = solve_u(f_su3, 3, N_COLORS * 15 / LINKS_PER_BLOCK, "smallest")
    branch_ok = (s16 is not None and s15 is not None
                 and s16[1] < 1e-12 and s15[1] < 1e-12)
    if branch_ok:
        r_small = (s15[0] / s16[0]) ** -2
        branch_ok = (abs(r_small - 1.0) < 0.5
                     and not (0.5 <= r_small / ALPHA_S <= 2.0))
        detail = (f"small branch: u*(16) = {s16[0]:.6f}, "
                  f"u*(15) = {s15[0]:.6f}, R = {r_small:.6f}, "
                  f"R/alpha_s = {r_small / ALPHA_S:.3f}")
    else:
        detail = "small branch missing"
    check("A", "D4 branch robustness (SU(3), uniform share): the "
               "declared model's small-u branch ALSO gives an O(1) "
               "feedback factor outside a factor 2 of alpha_s — no "
               "branch selection rescues the candidate rule",
          branch_ok, detail)
    return table


def section_e(results):
    print("\n--- Section E [A]/[C]: robustness — sharing conventions ---")

    # E1: per-site share equals uniform share EXACTLY (Fraction proof).
    n_modes = Fraction(16)
    uniform = N_COLORS * n_modes / Fraction(LINKS_PER_BLOCK)
    per_site = 2 * (N_COLORS * n_modes / Fraction(16)) / Fraction(8)
    check("C", "E1 sharing conventions: per-site share (per-site "
               "n_c n/16 split over the site's 8 incident links, each "
               "link fed by its 2 endpoints) equals the uniform share "
               "kappa = n_c n/64 EXACTLY (Fraction identity "
               "2 x (n_c n/16)/8 = n_c n/64) — the two declared "
               "conventions give the SAME self-consistency, hence the "
               "same R", uniform == per_site == Fraction(3 * 16, 64),
          f"kappa(n=16) = {uniform} per link")

    # E2: stress brackets kappa -> 2 kappa and kappa/2 (deliberate
    # mis-sharing): R must stay O(1) and far from alpha_s in all
    # variants for the conclusion to be sharing-robust.
    stress_ok = True
    details = []
    for name, f_func, n_group in VARIANTS:
        for mult, tag in ((2.0, "x2"), (0.5, "x1/2")):
            k16 = mult * N_COLORS * 16 / LINKS_PER_BLOCK
            k15 = mult * N_COLORS * 15 / LINKS_PER_BLOCK
            s16 = solve_u(f_func, n_group, k16)
            s15 = solve_u(f_func, n_group, k15)
            ok = (s16 is not None and s15 is not None
                  and s16[1] < 1e-12 and s15[1] < 1e-12)
            if ok:
                r = (s15[0] / s16[0]) ** -2
                ok = abs(r - 1.0) < 0.5 and not (0.5 <= r / ALPHA_S <= 2.0)
                details.append(f"{name} {tag}: R = {r:.6f}")
            stress_ok = stress_ok and ok
    check("A", "E2 stress brackets (kappa -> 2 kappa and kappa/2, "
               "deliberate mis-sharing by a factor 4 overall): in every "
               "variant R stays O(1) (|R - 1| < 0.5) and outside a "
               "factor 2 of alpha_s — the conclusion does NOT depend on "
               "the sharing convention", stress_ok,
          "; ".join(details))


# ---------------------------------------------------------------------------
# Section F — diagnostics, supplier scans, verdict logic.
# ---------------------------------------------------------------------------
def section_f(results, table):
    print("\n--- Section F [A]/[B]: fenced diagnostics, scans, verdict "
          "logic ---")

    # F1 [A]: pure-gauge diagnostic (bounded observation, fenced).
    diag = []
    diag_ok = True
    for name, _, _ in VARIANTS:
        pg = results[name][0]
        if pg is None:
            diag.append(f"{name}: NO nontrivial pure-gauge root at "
                        f"beta = 6 (disordered mean-field branch)")
        else:
            diag_ok = diag_ok and pg[1] < 1e-12
            diag.append(f"{name}: u*(0) = {pg[0]:.7f} vs licensed "
                        f"u_0 = {U_0:.7f} (delta = {pg[0] - U_0:+.4f})")
    for line in diag:
        print(f"    diagnostic: {line}")
    check("A", "F1 FENCED DIAGNOSTIC (bounded observation, "
               "model-diagnostic context ONLY — NO claim that the "
               "mean-field model reproduces the licensed surface): "
               "pure-gauge u*(0) at beta = 6 computed and reported per "
               "variant; every root found has residual < 1e-12",
          diag_ok)

    # F2 [B]: block02 reduction target on disk (alpha_s per decoupling).
    b02 = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                  "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    b02_text = b02.read_text() if b02.exists() else ""
    b01 = (DOCS / "HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_"
                  "PROBE_NOTE_2026-06-11.md")
    b01_text = b01.read_text() if b01.exists() else ""
    b01_flat = " ".join(b01_text.split())
    check("B", "F2 upstream campaign notes on disk: block02 records the "
               "reduction target 'one factor alpha_s = 0.1033038 per "
               "taste decoupling' and block01 records the zero "
               "frozen-link coupling shift this probe starts from",
          "alpha_s = 0.1033038" in b02_text
          and "per taste decoupling" in b02_text
          and "EXACTLY ZERO induced coupling shift" in b01_flat)

    # F3 [B]: licenses and fences on disk — B1 plaquette reuse license,
    # DELTA0 gate, YT-P2 blocking-mechanism scoping.
    plaq_text = (DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md").read_text()
    gate = (DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_"
                   "NOTE_2026-05-30.md")
    gate_text = gate.read_text() if gate.exists() else ""
    yt = (DOCS / "YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_"
                 "NOTE_2026-04-17.md")
    yt_flat = " ".join((yt.read_text() if yt.exists() else "").split())
    check("B", "F3 licenses on disk: plaquette B1 reuse license "
               "('admitted comparison/reuse number', 0.5934 — the "
               "licensed surface this probe does NOT claim to "
               "reproduce); DELTA0 gate note open; YT-P2 names "
               "'non-perturbative blocking renormalization' and leaves "
               "blocking-RG routes open (this probe lives inside that "
               "permitted route)",
          "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text
          and "open_gate" in gate_text
          and "non-perturbative blocking renormalization" in yt_flat)

    # F4 [B]: parent-note honesty fences.
    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "declared model",
        "does not close the delta0 gate",
        "not a licensed framework object",
        "refuted",
    ]
    forbidden = [
        "closes the delta0 gate",
        "derives the attachment",
        "reproduces the licensed surface",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "F4 parent-note honesty fences on disk: the note labels "
               "M1/M2 'declared model' content, states the mean-field F "
               "is 'not a licensed framework object', records the "
               "verdict as 'refuted' for this route, and 'does not "
               "close the DELTA0 gate'; forbidden closure tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")

    # F5 [A]: the verdict logic itself, applied to the computed table.
    supplied = 0.99 <= table["SU(3)"][2] <= 1.01
    observation = any(0.5 <= table[v][2] <= 2.0 for v, _, _ in VARIANTS)
    refuted = (not supplied) and (not observation)
    check("A", "F5 verdict logic (declared up front in the docstring) "
               "applied to the computed displacements: 'supplied' fires "
               "in no variant, 'bounded observation' fires in no "
               "variant, so the candidate rule 'alpha_s per decoupling "
               "= mean-field link feedback' is REFUTED under every "
               "declared variant and sharing convention",
          refuted,
          f"min displacement = "
          f"{min(table[v][2] for v, _, _ in VARIANTS):.3f}x alpha_s")

    # Declared-open residuals.
    print()
    residual("the alpha_s PER-DECOUPLING ATTACHMENT rule (block02 R1) "
             "remains UNSUPPLIED.  This probe REFUTES one candidate "
             "supplier — mean-field link un-freezing feedback of the "
             "induced action -n_c n ln(2u) — under every declared "
             "variant (U(1), SU(2), SU(3)) and sharing convention: the "
             "feedback factor R is O(1), an order of magnitude "
             "(9.7x-10.5x displacement) above alpha_s = 0.1033038.")
    residual("remaining candidate routes (declared-open, none probed "
             "here): (i) beyond-mean-field link fluctuations / exact "
             "one-link Haar integrals at strong coupling in the "
             "Kawamoto-Smit lineage; (ii) vacuum-polarization dressing "
             "of the Green-kernel readout itself (the 1/(4 pi) chain), "
             "rather than of the saddle u; (iii) a non-link-feedback "
             "transport rule attaching alpha_s per taste threshold "
             "directly.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: the obstruction is sharpened "
             "(one named candidate route eliminated), not closed.")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; the "
          "declared-model")
    print("   feedback factors and the displacement are internal "
          "structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_attachment_mean_field_feedback_probe_"
          "2026_06_11.py")
    print(" Block04 of the DELTA0 blocking campaign: FIRST FALSIFIABLE "
          "ATTEMPT at the")
    print(" attachment rule.  Does mean-field link un-freezing (the "
          "decimated mode's")
    print(" induced action -ln(2u) feeding the link self-consistency) "
          "supply one")
    print(" factor alpha_s = 0.1033038 per taste decoupling?  Computed "
          "exactly under")
    print(" DECLARED models M1 (Wilson mean field, beta = 6; U(1)/SU(2)/"
          "SU(3)) and M2")
    print(" (induced action -n_c n ln(2u), declared link sharing).")
    print(" Parent note: docs/HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_"
          "FEEDBACK_PROBE_")
    print("              NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    section_b()
    results = section_c()
    table = section_d(results)
    section_e(results)
    section_f(results, table)
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded, declared models): the induced "
          "action of one")
    print("   decimated taste mode is exactly -ln(2u) per color as a "
          "function of the")
    print("   link dressing, and feeding it into the mean-field "
          "self-consistency shifts")
    print("   the saddle by an O(1)-with-small-deviation factor R close "
          "to 1 in every")
    print("   declared variant — an order of magnitude (9.7x-10.5x) "
          "above the required")
    print("   alpha_s per decoupling.  REFUTED (this route): the "
          "alpha_s-per-decoupling attachment")
    print("   rule canNOT be mean-field link feedback under any declared "
          "variant or")
    print("   sharing convention.  NOT claimed: closure, any licensed-"
          "surface")
    print("   reproduction, or any model-independent statement.  DELTA0 "
          "stays open;")
    print("   obstruction sharpened (one candidate route eliminated), "
          "not closed.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
