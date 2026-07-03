#!/usr/bin/env python3
"""DELTA0 B4 theory probe: the taste-pairing transfer-ladder PROPOSAL,
graded by computation.  (Block12 of the DELTA0 blocking campaign.)

    docs/HIERARCHY_DELTA0_B4_TASTE_TRANSFER_LADDER_THEORY_PROBE_
    NOTE_2026-06-11.md

Setting.  Block11 (the B4 attachment-observable enumeration) executed
block10b's kill criterion over the declared readout class K1-K8 and
found the attachment observable, if it exists, is NOT among them; any
closing identification must exhibit block10b's four consequences
(log-additivity, threshold-scale evaluation, two-link vertex dressing,
d = 3 substrate) AND lie outside the enumerated class.  This block
states the campaign's first PROPOSED mechanism satisfying all of those
constraints — the taste-pairing transfer ladder — and grades its
computable core honestly.

PROPOSED mechanism (proposal, NOT established; the parent note carries
the full statement and fences): the IR condensate channel is built from
the 16-taste UV condensate through 16 taste-sector reductions; at each
threshold the decoupling taste's pairing amplitude must transfer to the
surviving tastes.  At frozen links this transfer is EXACTLY ZERO
(block01's zero cross-taste coupling — the load-bearing fact that makes
the mechanism non-trivial); the leading transfer is mediated by ONE
link-fluctuation exchange whose strength factorizes as
[vertex leg: connected link variance across two dressed hops,
sigma_U^2/u_0^2-shaped] x [kernel leg: the readout-normalized gluon
kernel 1/(4 pi), landed in block10b, declared NOT recomputed here].
One exchange per threshold => one alpha_s per decoupling => alpha_s^16.

COMPUTABLE CORE graded by this runner (the falsifiable content):

  P1 (Section B/C): connected link variance under the one-link measure
      exp(h Re Tr U) d_Haar(U) — DECLARED object: the gauge-invariant
      trace-channel connected variance
          sigma_U^2(h) := <|(1/N) Tr U|^2>_h - (<(1/N) Re Tr U>_h)^2,
      which equals the full connected <(1/N)Tr U (1/N)Tr U*>_c because
      <Im Tr U>_h = 0 (theta -> -theta symmetry of the weight).  Chosen
      because the exchange couples through the gauge-invariant scalar
      channel of the link; the component-wise <U_ij U*_kl>_c is NOT
      needed for the declared scalar vertex and is left undeclared.
      Exact closed forms:
        U(1):  <U U*> = 1 identically (|e^{i th}| = 1), <U>_h = I1/I0,
               so sigma_U^2 = 1 - (I1(h)/I0(h))^2 EXACTLY;
        SU(2): (1/2)Tr U = cos th (real), Weyl measure (2/pi) sin^2 th,
               weight exp(2h cos th); with Z(x) = int sin^2 e^{x cos}
               = pi I1(x)/x at x = 2h:  <cos th> = I2/I1 and
               <cos^2 th> = Z''/Z = (I1 + 3 I3)/(4 I1)
               => sigma_U^2 = 1/4 + (3/4) I3/I1 - (I2/I1)^2 EXACTLY
               (both identities verified against deterministic Weyl
               quadrature to < 1e-12);
        SU(3): deterministic maximal-torus Weyl quadrature (block04's
               E3 machinery, extended with q = |Tr U|^2), Haar moments
               certified.
      Baths (declared variants): (A) threshold bath h_A solving
      F(h) = u_0 = 0.8776814 per group (one bisection each — the bath
      whose one-link expectation IS the licensed dressing); (B) the
      beta = 6 mean-field bath h_B = 6 beta u*^3/N at the pure-gauge
      self-consistent saddle u* (block04's M1, kappa = 0, dressed
      branch).  The SU(3) pure-gauge mean-field self-consistency has NO
      nontrivial root at beta = 6 (block04's recorded F1 diagnostic,
      reproduced deterministically here), so bath B is DECLARED ABSENT
      for SU(3) and the threshold bath A carries the SU(3) variant.
      All baths are DECLARED MODELS, never licensed-surface claims.

  P2 (Section D): the cross-taste transfer matrix, EXACT.  On the
      block01 2^4 block in the exact taste eigenbasis, the single-bond
      hop operator h_b (the one-link term of the kinetic operator; the
      64 of them sum to D exactly) is NOT taste-diagonal: the full
      16 x 16 table |<t| h_b |t'>|^2 is computed in exact
      Gaussian-rational arithmetic for the declared bond
      b0 = (site 0000, mu = 0).  Structure (all exact): entries take
      ONLY the values {0, 1/64, 1/16} with counts {230, 24, 2}; the
      same-corner opposite-sign element is EXACTLY ZERO; the two
      anchored rows carry off-diagonal sum 3/32, the six neighbor rows
      1/32, the eight far rows 0; sum over all 64 bonds restores
      block01's taste-diagonality (Sigma_b H'_b = diag(+-2i) exactly);
      the all-bond aggregate Sigma_b Sigma_{t' != t} |<t|h_b|t'>|^2
      = 3/2 exactly for EVERY taste (mode independence).

      DECLARED second-order perturbation-theory form (the pairing /
      Bogoliubov transfer shape; all 16 modes degenerate at |E| = 2 u_0
      so every pair denominator is E_t + E_t' = 4 u_0):
          A_{t t'} = sigma_U^2 |<t| h_b |t'>|^2 / (E_t + E_t')^2
      — the squared first-order mixing amplitude, dimensionless; the
      dressed kinetic normalization is carried by the dressed
      denominators.  Ratio-normalized vertex (two declared
      aggregations, both reported):
          V_bond = sigma_U^2 x (3/32)  / (16 u_0^2)   (one bond,
                   anchored decoupling-taste row, 15 kept channels),
          V_all  = sigma_U^2 x (3/2)   / (16 u_0^2)   (all 64 bonds).
      EXACT u_0-degree of V: -2 (two-point Fraction ratio at
      u in {2/3, 3/5} on the dressed-operator eigenvalues) — the
      mechanism-required power.  The degree CHECK passes; the
      MAGNITUDE is then graded in P3.

  P3 (Section E): the graded identity.  Mechanism predicts
      per-threshold factor = V x [kernel leg 1/(4 pi)] = alpha_s
      = 0.1033038?  Computed per variant with the EXACT displacement
      identity  factor/alpha_s = sigma_U^2 x S / 16  (u_0-free,
      S = 3/32 or 3/2).  STRINGENT declared window logic (block11
      pattern): [0.99, 1.01] = CANDIDATE MECHANISM; [0.5, 2.0] =
      numerology-risk observation; beyond = DISPLACED.  Result
      (spoiler in the verdict, not the checks): displaced in EVERY
      variant — and STRUCTURALLY so: sigma_U^2 < 1 for every bath, so
      factor <= (3/32) alpha_s = 0.094 alpha_s under the declared
      form — the candidate window is UNREACHABLE for any bath
      variance.  The displacement and the required change are recorded.

  P4 (Section F): the vacuum-overlap / Anderson-orthogonality reading,
      DECLARED form: |<vac_16|vac_15>|^2 = 1 - V_bond at second order
      in sigma_U (the decoupling taste's admixture deficit through one
      fluctuating bond).  Near 1 and displaced from alpha_s, as
      expected — completeness leg of the theory wave.

  P5 (RESIDUAL lines): the channel-factorization OPEN THEOREM — what
      would promote the proposal if its vertex landed — stated with
      kill criteria; the B4 identification and the DELTA0 gate stay
      open.

Inputs consumed: <P> = 0.5934 (hence u_0, hence alpha_s) ONLY under the
B1 reuse license of PLAQUETTE_SELF_CONSISTENCY_NOTE.md;
alpha_bare = 1/(4 pi) via the I2 convention row on the I3 g_bare = 1
surface (cited through block02, not asserted); the kernel leg 1/(4 pi)
per taste is block10b's landed object, DECLARED not recomputed here.

Vocabulary discipline: Sections A/D facts are bounded_theorem-grade
exact algebra; Sections B/C/E/F are exact arithmetic ON DECLARED MODELS
(one-link measure, second-order PT form, bath variants — all fenced);
the mechanism itself is a PROPOSAL graded by these numbers, never a
claim; all open content is printed as RESIDUAL (declared-open) lines,
never as PASSes and never as FAILs.

Deterministic, pure Python stdlib (fractions, math, itertools), no
network, no randomness (fixed quadrature grids), runtime well under
90 s (typically a few seconds).  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_B4_TASTE_TRANSFER_LADDER_THEORY_"
                      "PROBE_NOTE_2026-06-11.md")

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
    print(f"  OBSERVATION (bounded, numerology-risk flagged): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381 (licensed value)
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (block02 reduction target)

BETA = 6.0                           # declared M1 coupling (licensed surface)
DIM = 4                              # Z^4
STAPLES_PER_LINK = 2 * (DIM - 1)     # = 6, declared counting (block04 M1)

# Exact rational row sums of the single-bond transfer table (verified in
# Section D before they are consumed by Sections E/F).
S_BOND = Fraction(3, 32)             # anchored row, one bond, 15 kept
S_ALL = Fraction(3, 2)               # all 64 bonds, any taste row


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


# ---------------------------------------------------------------------------
# Single-bond hop operators (this block's exact object).
# ---------------------------------------------------------------------------
def bond_list():
    """The 64 oriented links of the 2^4 block: (x, y, val) with
    h_b[x][y] = +val, h_b[y][x] = -val, val = eta_mu(s) * sigma_wrap / 2;
    sigma_wrap = -1 iff the link wraps (s[mu] = 1).  Summing the 64
    bond operators reproduces the block01 operator D exactly."""
    bonds = []
    for s in SITES:
        x = SITE_INDEX[s]
        for mu in range(4):
            eta = (-1) ** sum(s[:mu])
            wrap = s[mu] == 1
            sigma = -1 if wrap else 1
            t = list(s)
            t[mu] = (t[mu] + 1) % 2
            y = SITE_INDEX[tuple(t)]
            bonds.append((x, y, Fraction(eta * sigma, 2)))
    return bonds


def bond_taste_matrix(t_mat, t_inv, x, y, val):
    """H'_b = T^-1 h_b T for the sparse single-bond operator
    (h_b[x][y] = val, h_b[y][x] = -val, real), exact Gaussian-rational.
    Exploits sparsity: (h_b T) has only rows x and y nonzero."""
    n = 16
    vplus = (val, Fraction(0))
    vminus = (-val, Fraction(0))
    row_x = [cmul(vplus, t_mat[y][j]) for j in range(n)]
    row_y = [cmul(vminus, t_mat[x][j]) for j in range(n)]
    return [[cadd(cmul(t_inv[i][x], row_x[j]), cmul(t_inv[i][y], row_y[j]))
             for j in range(n)] for i in range(n)]


# ---------------------------------------------------------------------------
# One-link integrals (block04 E3 machinery, reused; extended with the
# |Tr U|^2 column needed for the connected variance).
# ---------------------------------------------------------------------------
def bessel_ratio(n: int, x: float) -> float:
    """I_{n+1}(x)/I_n(x) by the Gautschi backward recurrence
    (deterministic, overflow-safe for any x > 0)."""
    if x == 0.0:
        return 0.0
    k_top = int(x + 4.0 * math.sqrt(x) + 60.0)
    r = 0.0
    for k in range(k_top, n, -1):
        r = 1.0 / (2.0 * k / x + r)
    return r


def f_u1(h: float) -> float:
    if h == 0.0:
        return 0.0
    return bessel_ratio(0, h)


def sigma2_u1(h: float) -> float:
    """U(1) EXACT: <U U*>_h = 1 identically, <U>_h = I1/I0 (real), so
    sigma_U^2 = 1 - (I1(h)/I0(h))^2."""
    r = f_u1(h)
    return 1.0 - r * r


def f_su2(h: float) -> float:
    if h == 0.0:
        return 0.0
    return bessel_ratio(1, 2.0 * h)


def sigma2_su2(h: float) -> float:
    """SU(2) EXACT Bessel identity (derived in the docstring):
    <cos^2 th>_h = 1/4 + (3/4) I3(2h)/I1(2h), so
    sigma_U^2 = 1/4 + (3/4) I3/I1 - (I2/I1)^2."""
    if h == 0.0:
        return 0.25
    x = 2.0 * h
    r21 = bessel_ratio(1, x)            # I2/I1
    r32 = bessel_ratio(2, x)            # I3/I2
    r31 = r21 * r32                     # I3/I1
    return 0.25 + 0.75 * r31 - r21 * r21


def su3_grid_tq(ngrid: int):
    """Fixed midpoint grid over the SU(3) maximal torus: returns
    (t_list, q_list, w_list) with t = Re Tr U, q = |Tr U|^2 and Weyl
    weight w = prod_{i<j} 4 sin^2((th_i - th_j)/2).  Deterministic."""
    ts, qs, ws = [], [], []
    step = 2.0 * math.pi / ngrid
    for i in range(ngrid):
        th1 = (i + 0.5) * step
        for j in range(ngrid):
            th2 = (j + 0.5) * step
            th3 = -(th1 + th2)
            cr = math.cos(th1) + math.cos(th2) + math.cos(th3)
            ci = math.sin(th1) + math.sin(th2) + math.sin(th3)
            w = (64.0
                 * math.sin((th1 - th2) / 2.0) ** 2
                 * math.sin((th1 - th3) / 2.0) ** 2
                 * math.sin((th2 - th3) / 2.0) ** 2)
            ts.append(cr)
            qs.append(cr * cr + ci * ci)
            ws.append(w)
    return ts, qs, ws


SU3_T64, SU3_Q64, SU3_W64 = su3_grid_tq(64)     # production grid
SU3_T96, SU3_Q96, SU3_W96 = su3_grid_tq(96)     # convergence-check grid


def su3_f_sigma2(h: float, ts=SU3_T64, qs=SU3_Q64, ws=SU3_W64):
    """SU(3): (F, sigma_U^2) by deterministic Weyl-measure midpoint
    quadrature (exp shifted by max t = 3, no overflow)."""
    num_t = 0.0
    num_q = 0.0
    den = 0.0
    for t, q, w in zip(ts, qs, ws):
        e = w * math.exp(h * (t - 3.0))
        den += e
        num_t += e * t
        num_q += e * q
    f = num_t / (3.0 * den)
    qbar = num_q / (9.0 * den)
    return f, qbar - f * f


def f_su3(h: float) -> float:
    if h == 0.0:
        return 0.0
    return su3_f_sigma2(h)[0]


def sigma2_su3(h: float) -> float:
    return su3_f_sigma2(h)[1]


# ---------------------------------------------------------------------------
# Deterministic solvers (block04 patterns).
# ---------------------------------------------------------------------------
def solve_h_threshold(f_func, target: float):
    """One bisection: h with F(h) = target on (0, 400] (F monotone
    increasing toward 1).  Returns (h, |F(h) - target|)."""
    lo, hi = 1e-9, 400.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f_func(mid) < target:
            lo = mid
        else:
            hi = mid
    h = 0.5 * (lo + hi)
    return h, abs(f_func(h) - target)


def solve_u_meanfield(f_func, n_group: int):
    """Pure-gauge mean-field saddle u = F(6 beta u^3 / N) at beta = 6
    (block04 M1 with kappa = 0), dressed (largest) branch: deterministic
    160-point scan for a sign change from above, then bisection."""
    def g(u: float) -> float:
        return u - f_func(STAPLES_PER_LINK * BETA * u ** 3 / n_group)

    lo, hi, nscan = 1e-3, 0.999999, 160
    us = [lo + (hi - lo) * k / nscan for k in range(nscan + 1)]
    gs = [g(u) for u in us]
    bracket = None
    for k in range(nscan, 0, -1):
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
# Section A — block01 reuse: the frozen-link zero (the load-bearing fact).
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]: block01 reuse — exact block, taste basis, "
          "and the frozen-link ZERO cross-taste coupling ---")
    d_unit = staggered_operator()
    n = 16

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
               "D^2 = -4 u^2 I, exact Gaussian-rational taste eigenbasis "
               "with T^-1 T = I (same construction code as block01)",
          antisym and d2_ok and inv_ok)

    d_cplx = [[(d_unit[i][j], Fraction(0)) for j in range(n)]
              for i in range(n)]
    d_prime = cmat_mul(t_inv, cmat_mul(d_cplx, t_mat))
    diag_ok = all(d_prime[i][j] == CZERO
                  for i in range(n) for j in range(n) if i != j)
    ent_ok = all(d_prime[j][j] == eigs[j] for j in range(n))
    check("C", "A2 frozen-link taste-diagonality EXACT (block01's "
               "load-bearing zero): the FULL kinetic operator has ZERO "
               "cross-taste coupling in the taste eigenbasis — the "
               "proposed transfer is non-trivially zero at frozen links",
          diag_ok and ent_ok, "D' = diag(+-2i), all 240 off-diag exact 0")
    return d_unit, t_mat, t_inv, eigs


# ---------------------------------------------------------------------------
# Section B — P1 derivations: connected link variance machinery.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [C]: P1 machinery — connected link variance "
          "sigma_U^2(h) per group (exact identities + quadrature) ---")
    npts = 512

    # B1: U(1).
    ok_u1 = True
    for h in (0.5, 2.0, 4.0, 10.0):
        num = 0.0
        den = 0.0
        for i in range(npts):
            th = (i + 0.5) * 2.0 * math.pi / npts
            e = math.exp(h * (math.cos(th) - 1.0))
            den += e
            num += e * math.cos(th)
        fq = num / den
        ok_u1 = ok_u1 and abs(fq - f_u1(h)) < 1e-12
        ok_u1 = ok_u1 and abs((1.0 - fq * fq) - sigma2_u1(h)) < 1e-12
    haar_u1 = abs(sigma2_u1(1e-9) - 1.0) < 1e-6
    check("C", "B1 U(1) EXACT: <U U*>_h = 1 identically (|e^{i th}| = 1) "
               "so sigma_U^2 = 1 - (I1(h)/I0(h))^2; Gautschi ratio vs "
               "512-pt quadrature < 1e-12 at 4 test h; Haar limit "
               "sigma_U^2(0) = 1", ok_u1 and haar_u1)

    # B2: SU(2).
    ok_su2 = True
    for h in (0.5, 2.0, 6.0, 12.0):
        num1 = 0.0
        num2 = 0.0
        den = 0.0
        for i in range(npts):
            th = (i + 0.5) * math.pi / npts
            e = math.sin(th) ** 2 * math.exp(2.0 * h * (math.cos(th) - 1.0))
            den += e
            num1 += e * math.cos(th)
            num2 += e * math.cos(th) ** 2
        f_q = num1 / den
        s2_q = num2 / den - f_q * f_q
        ok_su2 = ok_su2 and abs(f_q - f_su2(h)) < 1e-12
        ok_su2 = ok_su2 and abs(s2_q - sigma2_su2(h)) < 1e-12
    haar_su2 = abs(sigma2_su2(0.0) - 0.25) < 1e-15
    check("C", "B2 SU(2) EXACT Bessel identity: <cos^2 th>_h = "
               "1/4 + (3/4) I3(2h)/I1(2h) (Z = pi I1(x)/x route), so "
               "sigma_U^2 = 1/4 + (3/4) I3/I1 - (I2/I1)^2; verified vs "
               "512-pt Weyl quadrature < 1e-12 at 4 test h; Haar limit "
               "sigma_U^2(0) = <(Tr U/2)^2>_Haar = 1/4",
          ok_su2 and haar_su2)

    # B3: SU(3) Haar moments + grid convergence of sigma_U^2.
    sw = sum(SU3_W64)
    m0 = sw / len(SU3_W64) / 6.0
    m1 = sum(w * t for w, t in zip(SU3_W64, SU3_T64)) / sw
    m2 = sum(w * t * t for w, t in zip(SU3_W64, SU3_T64)) / sw
    mq = sum(w * q for w, q in zip(SU3_W64, SU3_Q64)) / sw
    moments_ok = (abs(m0 - 1.0) < 1e-12 and abs(m1) < 1e-12
                  and abs(m2 - 0.5) < 1e-12 and abs(mq - 1.0) < 1e-12)
    conv_ok = all(
        abs(su3_f_sigma2(h)[1]
            - su3_f_sigma2(h, SU3_T96, SU3_Q96, SU3_W96)[1]) < 1e-12
        for h in (0.5, 2.0, 6.0, 12.0))
    haar_su3 = abs(sigma2_su3(0.0) - 1.0 / 9.0) < 1e-12
    check("C", "B3 SU(3) Weyl torus quadrature certified: Haar moments "
               "<1> = 1, <Re Tr U> = 0, <(Re Tr U)^2> = 1/2, "
               "<|Tr U|^2> = 1 (fundamental-character orthonormality) "
               "all < 1e-12; 64- vs 96-grid sigma_U^2 agreement < 1e-12 "
               "at 4 test h; Haar limit sigma_U^2(0) = 1/9",
          moments_ok and conv_ok and haar_su3,
          f"<|Tr U|^2>_Haar = {mq:.14f}")


# ---------------------------------------------------------------------------
# Section C — P1 solves: the two declared baths per group.
# ---------------------------------------------------------------------------
VARIANTS = (("U(1)", f_u1, sigma2_u1, 1),
            ("SU(2)", f_su2, sigma2_su2, 2),
            ("SU(3)", f_su3, sigma2_su3, 3))


def section_c():
    print("\n--- Section C [A]: P1 solves — threshold bath F(h) = u_0 and "
          "the beta = 6 mean-field bath; sigma_U^2 tabulated ---")
    baths = {}

    # C1: threshold bath (variant A): one bisection per group.
    res_ok = True
    for name, f_func, s2_func, _ in VARIANTS:
        h_a, res = solve_h_threshold(f_func, U_0)
        s2_a = s2_func(h_a)
        baths[(name, "A")] = (h_a, s2_a)
        res_ok = res_ok and res < 1e-12
        print(f"    {name} threshold bath:  h_A = {h_a:.7f}, "
              f"F(h_A) = u_0 = {U_0:.7f}, sigma_U^2 = {s2_a:.10f}")
    check("A", "C1 threshold bath per group: h_A solving F(h) = u_0 = "
               "0.8776814 (one bisection each, residual < 1e-12); "
               "sigma_U^2(h_A) tabulated",
          res_ok)

    # C2: beta = 6 mean-field bath (variant B).  The SU(3) pure-gauge
    # mean-field self-consistency has NO nontrivial root at beta = 6
    # (block04's recorded F1 diagnostic: 'NO nontrivial pure-gauge root
    # (disordered mean-field branch)') — the deterministic expected
    # outcome; bath B is DECLARED ABSENT for SU(3).
    mf_ok = True
    su3_absent = False
    for name, f_func, s2_func, n_group in VARIANTS:
        sol = solve_u_meanfield(f_func, n_group)
        if sol is None:
            su3_absent = su3_absent or name == "SU(3)"
            mf_ok = mf_ok and name == "SU(3)"
            print(f"    {name} mean-field bath:  NO nontrivial pure-gauge "
                  f"root at beta = 6 (disordered mean-field branch; "
                  f"block04 F1 diagnostic reproduced) — bath B DECLARED "
                  f"ABSENT, threshold bath A carries this group")
            continue
        u_star, res = sol
        h_b = STAPLES_PER_LINK * BETA * u_star ** 3 / n_group
        s2_b = s2_func(h_b)
        baths[(name, "B")] = (h_b, s2_b)
        mf_ok = mf_ok and res < 1e-12
        print(f"    {name} mean-field bath:  u* = {u_star:.7f}, "
              f"h_B = {h_b:.7f}, sigma_U^2 = {s2_b:.10f}")
    check("A", "C2 beta = 6 mean-field bath (block04 M1, kappa = 0, "
               "dressed branch): U(1) and SU(2) saddles solved with "
               "residual < 1e-12 and sigma_U^2(h_B) tabulated; SU(3) "
               "has NO nontrivial pure-gauge root at beta = 6 "
               "(block04's recorded disordered-branch diagnostic "
               "reproduced) — bath B declared absent for SU(3)",
          mf_ok and su3_absent
          and ("U(1)", "B") in baths and ("SU(2)", "B") in baths)

    # C3: exact cross-checks: U(1) sigma^2_A = 1 - u_0^2 by construction;
    # every sigma_U^2 strictly inside (0, 1).
    u1_exact = abs(baths[("U(1)", "A")][1] - (1.0 - U_0 ** 2)) < 1e-10
    all_in = all(0.0 < v[1] < 1.0 for v in baths.values())
    check("A", "C3 cross-checks: U(1) threshold-bath variance equals "
               "1 - u_0^2 = 1 - <P>^(1/2) = 0.2296757 exactly (since "
               "F(h_A) = u_0 by construction); every sigma_U^2 strictly "
               "inside (0, 1) — the structural bound input for E3",
          u1_exact and all_in,
          f"1 - u_0^2 = {1.0 - U_0 ** 2:.7f}")
    return baths


# ---------------------------------------------------------------------------
# Section D — P2: the exact cross-taste transfer matrix.
# ---------------------------------------------------------------------------
def section_d(d_unit, t_mat, t_inv, eigs):
    print("\n--- Section D [C]: P2 — single-bond hop operator in the taste "
          "basis, exact 16 x 16 transfer table ---")
    n = 16
    bonds = bond_list()

    # D1: 64 bonds; each real antisymmetric with Frobenius^2 = 1/2;
    # they sum to D exactly.
    sum_ok = True
    acc = [[Fraction(0)] * n for _ in range(n)]
    frob_ok = True
    for x, y, val in bonds:
        acc[x][y] += val
        acc[y][x] -= val
        frob_ok = frob_ok and 2 * val * val == Fraction(1, 2)
    sum_ok = acc == d_unit
    check("C", "D1 the 64 single-link hop operators h_b (one per "
               "oriented link, eta and antiperiodic wrap signs included) "
               "are each real antisymmetric with Frobenius norm^2 = 1/2 "
               "and sum EXACTLY to the block01 operator D",
          sum_ok and frob_ok and len(bonds) == 64)

    # Chosen bond b0 = (site 0000, mu = 0): x0 even endpoint, y0 odd.
    x0 = SITE_INDEX[(0, 0, 0, 0)]
    y0 = SITE_INDEX[(1, 0, 0, 0)]
    b0 = next((x, y, v) for (x, y, v) in bonds if x == x0 and y == y0)
    h0 = bond_taste_matrix(t_mat, t_inv, *b0)
    tab = [[cabs2(h0[i][j]) for j in range(n)] for i in range(n)]

    # D2: value classes and counts; anti-Hermitian magnitude symmetry;
    # Frobenius invariance.
    vals = {}
    for i in range(n):
        for j in range(n):
            vals[tab[i][j]] = vals.get(tab[i][j], 0) + 1
    classes_ok = (set(vals) == {Fraction(0), Fraction(1, 64),
                                Fraction(1, 16)}
                  and vals[Fraction(0)] == 230
                  and vals[Fraction(1, 64)] == 24
                  and vals[Fraction(1, 16)] == 2)
    herm_ok = all(tab[i][j] == tab[j][i] for i in range(n) for j in range(n))
    frob_inv = sum(tab[i][j] for i in range(n) for j in range(n)) \
        == Fraction(1, 2)
    print("    |<t|h_b0|t'>|^2 table in units of 1/64 "
          "(rows/cols = taste modes; bond b0 = (0000, mu=0)):")
    for i in range(n):
        print("      " + " ".join(f"{int(tab[i][j] * 64):2d}"
                                  for j in range(n)))
    check("C", "D2 exact taste-basis table for the declared bond b0: "
               "entries take ONLY the values {0, 1/64, 1/16} with counts "
               "{230, 24, 2}; |<t|h|t'>| = |<t'|h|t>| (anti-Hermitian "
               "magnitude symmetry); Frobenius sum = 1/2 preserved "
               "(unitary-invariance cross-check)",
          classes_ok and herm_ok and frob_inv)

    # D3: structure: the single-bond operator is NOT taste-diagonal;
    # rows split anchored/neighbor/far with exact rational sums.
    even = [SITE_INDEX[s] for s in SITES if sum(s) % 2 == 0]
    anchor = {j: even[j % 8] for j in range(n)}
    nbrs_y0 = {SITE_INDEX[(0, 0, 0, 0)], SITE_INDEX[(1, 1, 0, 0)],
               SITE_INDEX[(1, 0, 1, 0)], SITE_INDEX[(1, 0, 0, 1)]}
    anchored = [j for j in range(n) if anchor[j] == x0]
    neighbor = [j for j in range(n)
                if anchor[j] in nbrs_y0 and anchor[j] != x0]
    far = [j for j in range(n) if anchor[j] not in nbrs_y0]
    offdiag = [sum(tab[i][j] for j in range(n) if j != i) for i in range(n)]
    anch_ok = (len(anchored) == 2
               and all(offdiag[i] == S_BOND for i in anchored)
               and tab[anchored[0]][anchored[1]] == Fraction(0))
    nbr_ok = (len(neighbor) == 6
              and all(offdiag[i] == Fraction(1, 32) for i in neighbor))
    far_ok = (len(far) == 8
              and all(offdiag[i] == Fraction(0) for i in far))
    not_diag = any(tab[i][j] != Fraction(0)
                   for i in range(n) for j in range(n) if i != j)
    check("C", "D3 structure: h_b0 is NOT taste-diagonal (the single "
               "bond DOES couple taste sectors); same-corner "
               "opposite-sign element EXACTLY ZERO; off-diagonal row "
               "sums: 2 anchored rows = 3/32 each, 6 neighbor rows = "
               "1/32, 8 far rows = 0 (exact rationals)",
          not_diag and anch_ok and nbr_ok and far_ok,
          "S_bond = 3/32 = sum over the 15 kept channels, anchored row")

    # D4: summing the 64 bond operators in the taste basis restores
    # block01's taste-diagonality exactly.
    acc_taste = [[CZERO] * n for _ in range(n)]
    all_bond_offdiag = [Fraction(0)] * n
    for x, y, val in bonds:
        hb = bond_taste_matrix(t_mat, t_inv, x, y, val)
        for i in range(n):
            for j in range(n):
                acc_taste[i][j] = cadd(acc_taste[i][j], hb[i][j])
                if i != j:
                    all_bond_offdiag[i] += cabs2(hb[i][j])
    diag_restored = all(
        acc_taste[i][j] == (eigs[i] if i == j else CZERO)
        for i in range(n) for j in range(n))
    check("C", "D4 consistency with block01: Sigma_b H'_b = diag(+-2i) "
               "EXACTLY — the 64 single-bond cross-taste couplings "
               "cancel identically in the bond sum, restoring the "
               "frozen-link taste-diagonality of A2",
          diag_restored)

    # D5: all-bond aggregate per taste: 3/2 exactly, every taste.
    agg_ok = all(v == S_ALL for v in all_bond_offdiag)
    check("C", "D5 all-bond aggregate Sigma_b Sigma_{t' != t} "
               "|<t|h_b|t'>|^2 = 3/2 EXACTLY for every one of the 16 "
               "tastes (mode independence of the transfer weight)",
          agg_ok, "S_all = 3/2")

    # D6: exact u_0-degree of the declared vertex V: -2.
    u1, u2 = Fraction(2, 3), Fraction(3, 5)
    deg_ok = True
    for s_sum in (S_BOND, S_ALL):
        v1 = s_sum / ((2 * u1 + 2 * u1) ** 2)     # E_t + E_t' = 4u exact
        v2 = s_sum / ((2 * u2 + 2 * u2) ** 2)
        deg_ok = deg_ok and v1 * u1 ** 2 == v2 * u2 ** 2 == s_sum / 16
    # the dressed gaps really are 2u: eigenvalues of u D are u x (+-2i).
    gap_ok = True
    for uu in (u1, u2):
        d_dr = [[(uu * d_unit[i][j], Fraction(0)) for j in range(n)]
                for i in range(n)]
        dp = cmat_mul(t_inv, cmat_mul(d_dr, t_mat))
        gap_ok = gap_ok and all(
            dp[j][j] == cmul((uu, Fraction(0)), eigs[j]) for j in range(n))
    check("C", "D6 EXACT u_0-degree of the declared vertex "
               "V = sigma_U^2 S/(E_t + E_t')^2 with the dressed gaps "
               "E = 2 u_0 (verified: eigenvalues of u D are +-2iu "
               "exactly): two-point Fraction ratio at u in {2/3, 3/5} "
               "gives degree EXACTLY -2 — the mechanism-required power "
               "(V u_0^2 = S/16, u_0-independent)",
          deg_ok and gap_ok,
          "u_0-degree(V) = -2: the two-dressed-hop shape holds")
    return tab


# ---------------------------------------------------------------------------
# Section E — P3: the graded identity.
# ---------------------------------------------------------------------------
def section_e(baths):
    print("\n--- Section E [A]: P3 — graded identity: V x [kernel leg "
          "1/(4 pi)] vs alpha_s = 0.1033038 ---")
    s_bond = float(S_BOND)
    s_all = float(S_ALL)
    rows = []
    ok_fin = True
    id_ok = True
    for name, _, _, _ in VARIANTS:
        for bath in ("A", "B"):
            if (name, bath) not in baths:
                continue          # SU(3) bath B declared absent (C2)
            h, s2 = baths[(name, bath)]
            for tag, s_sum in (("bond", s_bond), ("all", s_all)):
                v = s2 * s_sum / (16.0 * U_0 ** 2)
                factor = v * (1.0 / (4.0 * math.pi))
                disp = factor / ALPHA_S
                # exact displacement identity: disp = sigma^2 S / 16
                id_ok = id_ok and abs(disp - s2 * s_sum / 16.0) < 1e-14
                ok_fin = ok_fin and math.isfinite(v) and v > 0.0
                rows.append((name, bath, tag, s2, v, factor, disp))
                print(f"    {name} bath {bath} [{tag:4s}]: "
                      f"sigma_U^2 = {s2:.7f}, V = {v:.7e}, "
                      f"V/(4 pi) = {factor:.7e}, "
                      f"factor/alpha_s = {disp:.6f}  "
                      f"({1.0 / disp:.1f}x short)")
    check("A", "E1 per-threshold factor computed per variant (10 rows: "
               "3 groups x declared baths x 2 aggregations; SU(3) bath "
               "B absent per C2): V = sigma_U^2 S/(16 u_0^2) and "
               "factor = V/(4 pi); all finite and positive; the EXACT "
               "u_0-free displacement identity factor/alpha_s = "
               "sigma_U^2 x S/16 holds to < 1e-14 in every row",
          ok_fin and id_ok and len(rows) == 10)

    # E2: window logic.
    cand = [r for r in rows if 0.99 <= r[6] <= 1.01]
    obs = [r for r in rows if 0.5 <= r[6] <= 2.0]
    max_disp = max(r[6] for r in rows)
    min_short = 1.0 / max_disp
    check("A", "E2 STRINGENT window logic (declared up front): the "
               "CANDIDATE-MECHANISM window [0.99, 1.01] fires in NO "
               "variant; the factor-2 observation window [0.5, 2.0] "
               "fires in NO variant — the proposal's vertex leg is "
               "DISPLACED in every declared variant",
          not cand and not obs,
          f"closest approach = {max_disp:.6f}x alpha_s "
          f"({min_short:.0f}x short), "
          f"farthest = {min(r[6] for r in rows):.2e}x")

    # E3: the structural bound — the window is unreachable.
    bound = float(Fraction(3, 32))
    s2_max = max(r[3] for r in rows)
    bound_ok = (s2_max < 1.0
                and all(r[6] <= bound + 1e-15 for r in rows)
                and Fraction(3, 2) / 16 == Fraction(3, 32))
    check("A", "E3 structural displacement bound: sigma_U^2 < 1 for "
               "every bath (one-link variance of a bounded trace), so "
               "factor/alpha_s = sigma_U^2 S/16 <= S_all/16 = 3/32 = "
               "0.09375 under the declared second-order form — the "
               "candidate window (and even the factor-2 window) is "
               "UNREACHABLE for ANY bath variance: the displacement is "
               "structural, not a tuning failure",
          bound_ok,
          f"max sigma_U^2 = {s2_max:.6f}, bound = 3/32 = {bound:.5f}")

    observation("the REQUIRED vertex V_req = 4 pi x alpha_s = u_0^(-2) "
                "= 1.2981704 is the supplier-chain identity alpha_s = "
                "(1/(4 pi)) x u_0^(-2) restated as a vertex requirement "
                "— DEFINITIONAL, zero mechanism content (the block11 "
                "K2-cell lesson); it is recorded so the shortfall "
                "V_req/V is read as a displacement, never as a target "
                "'discovered' by this probe.")
    return rows


# ---------------------------------------------------------------------------
# Section F — P4: the vacuum-overlap reading.
# ---------------------------------------------------------------------------
def section_f(baths):
    print("\n--- Section F [A]: P4 — vacuum overlap |<vac_16|vac_15>|^2 "
          "(Anderson-orthogonality reading, declared form) ---")
    s_bond = float(S_BOND)
    ok = True
    details = []
    for name, _, _, _ in VARIANTS:
        h, s2 = baths[(name, "A")]
        v_bond = s2 * s_bond / (16.0 * U_0 ** 2)
        overlap = 1.0 - v_bond
        disp = overlap / ALPHA_S
        details.append(f"{name}: {overlap:.7f} ({disp:.2f}x alpha_s)")
        ok = ok and 0.99 < overlap < 1.0 and not (0.5 <= disp <= 2.0)
    check("A", "F1 declared second-order overlap |<vac_16|vac_15>|^2 = "
               "1 - sigma_U^2 Sigma_{t' kept} |<t|h_b|t'>|^2/(4 u_0)^2 "
               "= 1 - V_bond (one fluctuating bond, threshold bath): "
               "near 1 in every group and O(10x) DISPLACED from "
               "alpha_s — the secondary candidate is displaced as "
               "expected (completeness leg, no claim)",
          ok, "; ".join(details))


# ---------------------------------------------------------------------------
# Section G — supplier/constraint scans on disk.
# ---------------------------------------------------------------------------
def section_g():
    print("\n--- Section G [B]: constraint set, supplier chain, and "
          "honesty fences on disk ---")

    b11 = (DOCS / "HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_"
                  "ENUMERATION_NOTE_2026-06-11.md")
    b10b = (DOCS / "HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_"
                   "PROBE_NOTE_2026-06-11.md")
    b11_text = " ".join((b11.read_text() if b11.exists() else "").split())
    b10b_text = " ".join((b10b.read_text() if b10b.exists() else "").split())
    check("B", "G1 block11 constraint set on disk: the attachment "
               "observable is 'not among the K1-K8 declared readouts'; "
               "block10b's four consequences named (log-additivity, "
               "threshold-scale evaluation, two-link vertex dressing, "
               "d = 3 substrate) — the constraints this proposal is "
               "built to satisfy",
          "not among the K1-K8 declared readouts" in b11_text
          and "log-additivity" in b11_text
          and "threshold-scale evaluation" in b11_text
          and "log-additivity:" in b10b_text
          and "threshold-scale evaluation:" in b10b_text
          and "two-link vertex dressing" in b10b_text)

    b01 = (DOCS / "HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_"
                  "PROBE_NOTE_2026-06-11.md")
    b02 = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                  "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    plaq = DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
    b01_text = " ".join((b01.read_text() if b01.exists() else "").split())
    b02_text = b02.read_text() if b02.exists() else ""
    plaq_text = plaq.read_text() if plaq.exists() else ""
    check("B", "G2 supplier chain on disk: block01's zero cross-taste "
               "coupling ('EXACTLY ZERO induced coupling shift' — the "
               "load-bearing fact); block02's target 'alpha_s = "
               "0.1033038' 'per taste decoupling'; block10b's per-taste "
               "IR kernel slope (the kernel leg, LANDED — declared not "
               "recomputed here); the B1 plaquette reuse license",
          "EXACTLY ZERO induced coupling shift" in b01_text
          and "alpha_s = 0.1033038" in b02_text
          and "per taste decoupling" in b02_text
          and "per-taste IR kernel slope" in b10b_text
          and "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text)

    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "proposed mechanism",
        "taste-pairing transfer ladder",
        "does not close the delta0 gate",
        "declared model",
        "displaced",
        "open theorem",
        "kill criteria",
    ]
    forbidden = [
        "closes the delta0 gate",
        "derives the attachment",
        "mechanism is established",
        "candidate mechanism confirmed",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "G3 parent-note honesty fences on disk: the note labels "
               "the mechanism a 'proposed mechanism' (the taste-pairing "
               "transfer ladder), records the computed grade "
               "'displaced', carries the channel-factorization 'open "
               "theorem' with 'kill criteria', fences 'declared model' "
               "content, and states it 'does not close the DELTA0 "
               "gate'; forbidden closure tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")

    # Declared-open residuals (P5 + the gate).
    print()
    residual("P5, the channel-factorization OPEN THEOREM (what would "
             "promote the proposal had P3 landed; stated for the "
             "record): (i) the EW condensate channel factorizes through "
             "exactly ONE link-fluctuation exchange per taste threshold "
             "at leading order in the fluctuation expansion; (ii) the "
             "kernel leg attaches with readout normalization "
             "4 pi G -> 1 at the threshold scale; (iii) corrections are "
             "O(alpha_s^2) per rung, preserving the integer 16.  KILL "
             "CRITERIA: factorization fails (multiple exchanges at the "
             "same order), vertex u_0-degree != -2, or k-dependence in "
             "the per-threshold factor.  THIS BLOCK'S COMPUTATION: the "
             "u_0-degree IS -2 (D6 passes), but the vertex MAGNITUDE is "
             "structurally displaced (E3) — the theorem remains open "
             "AND its declared-form vertex is displaced.")
    residual("the B4 attachment-observable identification (block10b R2, "
             "constrained 'not K1-K8' by block11) remains UNSUPPLIED: "
             "this block contributes the FIRST proposal satisfying all "
             "block11 constraints (outside K1-K8, log-additive by "
             "construction, threshold-scale bath, two-dressed-hop "
             "u_0^(-2), d = 3 kernel leg), and grades it DISPLACED "
             "under the declared second-order one-exchange form: "
             "factor/alpha_s = sigma_U^2 S/16 <= 3/32 for any bath.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: this probe grades a proposal "
             "and sharpens the constraint surface (a mechanism-shaped "
             "vertex with the right u_0-degree exists but is >= 10.7x "
             "too small at saturation); it does not close the gate.")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; the "
          "transfer table,")
    print("   the baths, and the displacement are internal structure "
          "only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "H1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_b4_taste_transfer_ladder_theory_probe_"
          "2026_06_11.py")
    print(" Block12 of the DELTA0 campaign: the taste-pairing transfer "
          "ladder —")
    print(" the first PROPOSED attachment mechanism satisfying all block11 "
          "constraints")
    print(" (outside K1-K8; log-additive; threshold-scale; two-link "
          "dressing; d = 3) —")
    print(" graded by computation: vertex leg = sigma_U^2 x |<t|h_b|t'>|^2 "
          "/ (4 u_0)^2,")
    print(" kernel leg = 1/(4 pi) (landed, block10b).  Does V x (1/(4 pi)) "
          "= alpha_s?")
    print(" Parent note: docs/HIERARCHY_DELTA0_B4_TASTE_TRANSFER_LADDER_"
          "THEORY_PROBE_")
    print("              NOTE_2026-06-11.md")
    print("=" * 78)

    d_unit, t_mat, t_inv, eigs = section_a()
    section_b()
    baths = section_c()
    section_d(d_unit, t_mat, t_inv, eigs)
    rows = section_e(baths)
    section_f(baths)
    section_g()
    section_fence()
    disp_lo = min(r[6] for r in rows)
    disp_hi = max(r[6] for r in rows)

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT} OBSERVATION={OBSERVATION_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: proposal graded DISPLACED (vertex leg).  Established "
          "(bounded,")
    print("   exact): the single-bond hop operator is NOT taste-diagonal "
          "(table exact;")
    print("   anchored row 3/32, all-bond 3/2, bond sum restores "
          "diagonality), and the")
    print("   declared one-exchange vertex has u_0-degree EXACTLY -2 — "
          "the mechanism's")
    print("   required shape.  Graded (declared models): its MAGNITUDE is "
          "structurally")
    print("   short — factor/alpha_s = sigma_U^2 S/16 <= 3/32 = 0.094 for "
          "ANY bath, so")
    print("   the candidate window is unreachable in the declared "
          "second-order form;")
    print(f"   computed displacements {disp_lo:.1e}x to {disp_hi:.1e}x "
          "of alpha_s.  The vacuum-overlap")
    print("   reading is near 1 and displaced (P4).  NOT claimed: closure, "
          "the channel-")
    print("   factorization theorem (open, with kill criteria), or any "
          "licensed-surface")
    print("   reproduction.  DELTA0 stays open; the proposal stands as the "
          "first")
    print("   constraint-compliant candidate, graded honestly by its "
          "arithmetic.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
