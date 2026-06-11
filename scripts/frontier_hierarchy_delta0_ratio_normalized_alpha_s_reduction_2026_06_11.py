#!/usr/bin/env python3
"""DELTA0 reduction: ratio normalization -> one factor alpha_s per taste
decoupling

    docs/HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_
    REDUCTION_NOTE_2026-06-11.md

Block02 of the DELTA0 blocking campaign.  Block01
(scripts/frontier_hierarchy_delta0_blocking_single_mode_probe_2026_06_11
.py) established by exact arithmetic that one taste-mode decimation on
the minimal 2^4 all-APBC mean-field block carries the factor m +- 2i u_0
(magnitude exactly 2 u_0 at m = 0, per-mode u_0-degree exactly 1, zero
induced coupling shift, mode-independent), and sharpened the DELTA0 gate
to the per-mode normalization N = alpha_LM/(2 u_0) = alpha_bare/(2 u_0^2)
= 1/(8 pi u_0^2) = 0.0516519 with residuals R1 (per-decimation
attachment of the supplied 1/(4 pi) value) and R2 (the 1/(2 u_0^2)
factor wholly unsupplied).

What this runner establishes (bounded, exact arithmetic):

  Section A (ratio normalization, class [C]): in RATIO NORMALIZATION —
      the per-mode decimation factor at coupling u_0 divided by the same
      factor at the undressed reference u_0 = 1 — the per-mode factor is
      (2 u_0)/(2 x 1) = u_0 EXACTLY: the bare '2' cancels.  Established
      in exact Gaussian-rational arithmetic on the same block operator,
      taste eigenbasis and Schur decimation code as block01 (reused
      verbatim), for all 16 modes, at two rational test couplings; the
      16-mode ratio-normalized product is det(u_0 D)/det(D) = u_0^16
      exactly.

  Section B (framework-idiom precedent, class [B]): ratio normalization
      is framework-idiomatic — the landed honest-status runner
      (scripts/frontier_hierarchy_formula_honest_status.py, check C6)
      already extracts the determinant u_0-degree from a TWO-POINT
      u_0-RATIO (code line `det_a1 * a2 ** 16 == det_a2 * a1 ** 16`),
      and the canonical chain's alpha_LM = alpha_bare/u_0 is itself a
      dressed/undressed ratio.  PRECEDENT, NOT LICENSE: the parent note
      records the ratio normalization as a declared choice, and this
      runner scans that declaration.

  Section C (the reduction, classes [A]/[B]): over the declared ratio
      normalization the remaining per-mode gap is
          alpha_LM / u_0 = alpha_bare / u_0^2 = alpha_s = 0.1033038
      EXACTLY — the third member of the geometric progression
      alpha_bare, alpha_LM, alpha_s that the DELTA0 gate note records
      as its fact 3.  Equivalently N = alpha_s/2 with the 1/2 supplied
      by the ratio normalization.  REDUCTION THEOREM: DELTA0 closure
      over the declared ratio normalization is exactly equivalent to
      supplying ONE factor alpha_s per taste decoupling:
          u_0^16 x alpha_s^16 = alpha_bare^16 x u_0^(-16) = alpha_LM^16
      (exact Fraction identity on u_0-degrees and at rational test
      points; float check < 1e-12 relative).  Cross-lane: the YT lane's
      retained constant alpha_s^SM(v) = alpha_bare/u_0^2 = 0.1033 is
      scanned as a context pointer only, never as support.

  Section D (decomposition-ambiguity honesty, classes [C]/[A]): the
      per-mode '2' admits multiple EXACT readings — 2 = 2 sin(pi/2)
      per single direction (each per-direction operator squares to -I),
      and 2 = sqrt(4) = sqrt(d) at d = 4 (D^2 = -4 u_0^2 I with
      4 = sum of the d per-direction unit contributions).  Which factor
      the '1/2' in N = alpha_s/2 belongs to depends on the chosen
      decomposition; the readings are numerically indistinguishable.
      The ratio normalization is canonical here ONLY because it is the
      framework-idiomatic one — a declared choice, not a derivation.

  Section E (supplier ledger, class [B] + residuals): in the reduced
      form, the alpha_s VALUE has a landed supplier chain (I2 alpha
      convention + I3 g_bare = 1 + B1-licensed plaquette/tadpole), but
      the alpha_s PER-DECOUPLING ATTACHMENT rule is UNSUPPLIED — the
      single remaining residual, replacing block01's R1+R2 pair in the
      reduced form.  The gate's open content is reframed from two
      unsupplied factors to ONE unsupplied transport rule with a
      physical shape: 'one dressed two-link gauge coupling per taste
      threshold'.  Printed as RESIDUAL (declared-open) lines, never as
      PASSes and never as FAILs.  The reduction does NOT close DELTA0.

  Section F (falsification legs, class [A]):
      F1  alpha_LM instead of alpha_s per mode in ratio normalization
          gives u_0^16 alpha_LM^16 = alpha_bare^16 exactly, displacing
          the suppression from alpha_LM^16 by u_0^16 = 0.124;
      F2  alpha_bare instead gives u_0^16 alpha_bare^16, displaced from
          alpha_LM^16 by u_0^32 = 0.015374 exactly;
      F3  the bare (non-ratio) normalization reproduces block01's
          N = alpha_LM/(2 u_0) = 1/(8 pi u_0^2) = 0.0516519 = alpha_s/2
          — consistency with the landed block01 probe.

  Terminal class-D fence: no PDG comparator is needed or consumed by
      this reduction; a self-scan certifies the PDG VEV literal is
      absent from this runner's source.

Vocabulary discipline: nothing here is 'derived' past its declared
premises.  Section A/D matrix facts and the Section C product identity
are bounded_theorem-grade exact algebra OVER THE DECLARED ratio
normalization; the normalization itself is a declared choice with a
cited precedent, not a derived object; all unsupplied content is
declared as RESIDUAL (declared-open) lines.

Deterministic, pure Python stdlib (fractions, math, itertools), no
network, no randomness, runtime well under one minute.
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
SCRIPTS = REPO_ROOT / "scripts"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_"
                      "PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md")

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
#   <P> = 0.5934 consumed ONLY under the B1 reuse license of
#   PLAQUETTE_SELF_CONSISTENCY_NOTE.md; alpha_bare = 1/(4 pi) enters via
#   the I2 convention row + I3 g_bare = 1 surface.
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_LM = ALPHA_BARE / U_0          # = 0.0906678
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (the reduction target)


# ---------------------------------------------------------------------------
# Exact real linear algebra (Fractions) — REUSED verbatim from block01
# (scripts/frontier_hierarchy_delta0_blocking_single_mode_probe_
# 2026_06_11.py) so the block results provably match.
# ---------------------------------------------------------------------------
def mat_mul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def det_exact(a_in):
    a = [[Fraction(x) for x in row] for row in a_in]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = -det
        det *= a[col][col]
        inv = 1 / a[col][col]
        for r in range(col + 1, n):
            if a[r][col]:
                f = a[r][col] * inv
                for c2 in range(col, n):
                    a[r][c2] -= f * a[col][c2]
    return det


# ---------------------------------------------------------------------------
# Exact Gaussian-rational (complex Fraction) arithmetic — reused from
# block01.  A complex number is a tuple (re, im) of Fractions.
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Minimal-block staggered operator — construction REUSED verbatim from
# block01 / the landed honest-status runner.
# ---------------------------------------------------------------------------
SITES = list(itertools.product((0, 1), repeat=4))
SITE_INDEX = {s: i for i, s in enumerate(SITES)}


def staggered_operator():
    """Per-color eta-phase staggered central-difference operator on the
    2^4 block with antiperiodic wrap in all four directions; unit links
    (u_0 = 1); exact Fractions."""
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


def single_direction_operator(mu):
    """The mu-direction term of the staggered operator alone (eta phase
    included); exact Fractions.  Sum over mu reproduces D."""
    n = len(SITES)
    d = [[Fraction(0)] * n for _ in range(n)]
    for s in SITES:
        x = SITE_INDEX[s]
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


def diag_taste_form(d_unit, t_mat, t_inv, a, m):
    """M' = T^-1 (a D + m) T in the taste eigenbasis."""
    return cmat_mul(t_inv, cmat_mul(complex_block_matrix(d_unit, a, m),
                                    t_mat))


# ---------------------------------------------------------------------------
# Section A — ratio normalization: the bare '2' cancels exactly.
# ---------------------------------------------------------------------------
def section_a(d_unit):
    print("\n--- Section A [C]: ratio normalization — per-mode factor at "
          "coupling u_0 over the same factor at u_0 = 1 ---")

    t_mat, t_inv, eigs = taste_eigenbasis(d_unit)
    n = 16

    # A1: block01 baseline — D real antisymmetric, D^2 = -4 I; the
    # taste eigenbasis is exact (T^-1 T = I, D v = +-2i v).
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(n) for j in range(n))
    d2 = mat_mul(d_unit, d_unit)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(n) for j in range(n))
    d_cplx = complex_block_matrix(d_unit, Fraction(1), Fraction(0))
    dt = cmat_mul(d_cplx, t_mat)
    eig_ok = all(dt[i][j] == cmul(eigs[j], t_mat[i][j])
                 for i in range(n) for j in range(n))
    tt = cmat_mul(t_inv, t_mat)
    inv_ok = all(tt[i][j] == (CONE if i == j else CZERO)
                 for i in range(n) for j in range(n))
    check("C", "A1 block01 baseline reproduced: D real antisymmetric, "
               "D^2 = -4 u_0^2 I; exact taste eigenbasis with "
               "D v = +-2i v and T^-1 T = I (same construction code as "
               "block01)", antisym and d2_ok and eig_ok and inv_ok,
          "exact Fraction / Gaussian-rational arithmetic")

    # A2: per-mode decimation factor at coupling a and at the undressed
    # reference a = 1: S(a) = +-2i a, S(1) = +-2i, magnitudes 2a and 2.
    a1, a2 = Fraction(2, 3), Fraction(3, 5)
    facs = {}
    for aa in (a1, a2, Fraction(1)):
        mp = diag_taste_form(d_unit, t_mat, t_inv, aa, Fraction(0))
        s, _, _ = schur_decimate(mp, 0)
        facs[aa] = s
    fac_ok = all(cabs2(facs[aa]) == 4 * aa * aa
                 for aa in (a1, a2, Fraction(1)))
    ref_ok = cabs2(facs[Fraction(1)]) == 4
    check("C", "A2 per-mode decimation factor (block01 Schur code, "
               "m = 0): |S(u_0)| = 2 u_0 at rational test couplings; at "
               "the undressed reference u_0 = 1 the factor is "
               "|S(1)| = 2 exactly", fac_ok and ref_ok,
          "u_0 in {2/3, 3/5, 1}")

    # A3: RATIO NORMALIZATION — S(u_0)/S(1) = u_0 exactly, the bare '2'
    # cancels; mode-independent (all 16 modes, both test couplings).
    ratio_ok = True
    for aa in (a1, a2):
        mp_a = diag_taste_form(d_unit, t_mat, t_inv, aa, Fraction(0))
        mp_1 = diag_taste_form(d_unit, t_mat, t_inv, Fraction(1),
                               Fraction(0))
        for j in range(n):
            r = cmul(mp_a[j][j], cinv(mp_1[j][j]))
            ratio_ok = ratio_ok and r == (aa, Fraction(0))
    check("C", "A3 ratio-normalized per-mode factor S(u_0)/S(1) = "
               "(2 u_0)/(2 x 1) = u_0 EXACTLY — the bare '2' cancels; "
               "mode-independent (all 16 modes, both rational test "
               "couplings)", ratio_ok,
          "32 exact per-mode ratios, Gaussian-rational")

    # A4: 16-mode ratio-normalized product = det(u_0 D)/det(D) = u_0^16
    # exactly — the same two-point-ratio shape as honest-status C6.
    prod_ok = True
    det_1 = det_exact(d_unit)
    for aa in (a1, a2):
        det_a = det_exact([[aa * x for x in row] for row in d_unit])
        prod_ok = prod_ok and det_a == det_1 * aa ** 16
    check("C", "A4 16-mode ratio-normalized product: det(u_0 D)/det(D) "
               "= u_0^16 exactly at both rational test couplings — the "
               "two-point u_0-ratio determinant identity", prod_ok,
          "exact Fraction determinants")

    return t_mat, t_inv


# ---------------------------------------------------------------------------
# Section B — framework-idiom precedent (cited precisely, NOT a license).
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [B]: framework-idiom precedent for ratio "
          "normalization (precedent, NOT license) ---")

    # B1: the landed honest-status runner extracts the determinant
    # u_0-degree from a two-point u_0-ratio (check C6).
    hs_src = (SCRIPTS / "frontier_hierarchy_formula_honest_status.py")
    hs_text = hs_src.read_text() if hs_src.exists() else ""
    check("B", "B1 precedent on disk: honest-status runner check C6 "
               "extracts the determinant u_0-degree from a two-point "
               "u_0-ratio — code line "
               "`det_a1 * a2 ** 16 == det_a2 * a1 ** 16` and check name "
               "'exact u_0-degree from a two-point ratio' both present",
          "det_a1 * a2 ** 16 == det_a2 * a1 ** 16" in hs_text
          and "exact u_0-degree from a two-point " in hs_text)

    # B2: the canonical chain's alpha_LM = alpha_bare/u_0 is itself a
    # dressed/undressed ratio (gate note + honest-status runner rows).
    gate = (DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_"
                   "NOTE_2026-05-30.md")
    gate_text = gate.read_text() if gate.exists() else ""
    check("B", "B2 precedent on disk: the canonical chain's "
               "alpha_LM = alpha_bare/u_0 is itself a dressed/undressed "
               "ratio (DELTA0 gate note records it; honest-status "
               "runner defines ALPHA_LM = ALPHA_BARE / U_0)",
          "alpha_LM = alpha_bare / u_0" in gate_text
          and "ALPHA_LM = ALPHA_BARE / U_0" in hs_text)

    # B3: non-license honesty — the parent note declares the ratio
    # normalization as a choice and never claims gate closure.
    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "declared choice",
        "framework-idiomatic",
        "does not close the delta0 gate",
        "not a derivation",
    ]
    forbidden = [
        "closes the delta0 gate",
        "derives the attachment",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "B3 non-license honesty: parent note on disk declares "
               "the ratio normalization as a 'declared choice', labels "
               "it 'framework-idiomatic' (precedent, not license), "
               "states it 'does not close the DELTA0 gate' and that the "
               "choice is 'not a derivation'; forbidden closure tokens "
               "absent", not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")


# ---------------------------------------------------------------------------
# Section C — the reduction: per-mode gap = alpha_s; product identity.
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [A]/[B]: the reduction — over the declared "
          "ratio normalization the per-mode gap is exactly alpha_s ---")

    # C1: per-mode gap in ratio normalization = alpha_LM/u_0 =
    # alpha_bare/u_0^2 = alpha_s; geometric-progression membership.
    gap_route1 = ALPHA_LM / U_0
    gap_route2 = ALPHA_BARE / U_0 ** 2
    geo_ok = abs(ALPHA_LM / ALPHA_BARE - ALPHA_S / ALPHA_LM) < 1e-14
    check("A", "C1 remaining per-mode gap in ratio normalization: "
               "alpha_LM/u_0 = alpha_bare/u_0^2 = alpha_s = 0.1033038 "
               "(two routes agree; third member of the geometric "
               "progression alpha_bare, alpha_LM, alpha_s — gate-note "
               "fact 3; alpha_LM^2 = alpha_bare x alpha_s)",
          abs(gap_route1 / gap_route2 - 1.0) < 1e-14
          and abs(gap_route1 - 0.1033038) < 1e-7
          and abs(gap_route1 / ALPHA_S - 1.0) < 1e-14 and geo_ok,
          f"alpha_s = {gap_route1:.10f}")

    # C2: equivalently N = alpha_s/2 — the 1/2 supplied by the ratio
    # normalization's undressed reference factor 2 x 1.
    n_block01 = ALPHA_LM / (2.0 * U_0)
    check("A", "C2 block01's per-mode constant rewrites as N = "
               "alpha_s/2 exactly — the 1/2 is supplied by the declared "
               "ratio normalization (division by the undressed "
               "reference factor 2 x 1), leaving alpha_s as the whole "
               "remaining gap",
          abs(n_block01 / (ALPHA_S / 2.0) - 1.0) < 1e-14,
          f"N = {n_block01:.10f} = alpha_s/2 = {ALPHA_S / 2.0:.10f}")

    # C3: REDUCTION THEOREM product identity, exact + float.
    #   u_0^16 x alpha_s^16 = u_0^16 x alpha_bare^16 x u_0^(-32)
    #                       = alpha_bare^16 x u_0^(-16) = alpha_LM^16.
    deg_lhs = Fraction(16) + 16 * Fraction(-2)   # u_0-degree of lhs
    deg_rhs = 16 * Fraction(-1)                  # u_0-degree of alpha_LM^16
    frac_ok = True
    for u in (Fraction(2, 3), Fraction(3, 5)):
        for ab in (Fraction(1, 7), Fraction(2, 9)):
            frac_ok = frac_ok and (
                u ** 16 * (ab / u ** 2) ** 16 == (ab / u) ** 16)
    float_lhs = U_0 ** 16 * ALPHA_S ** 16
    float_rhs = ALPHA_LM ** 16
    check("A", "C3 REDUCTION THEOREM identity: u_0^16 x alpha_s^16 = "
               "alpha_bare^16 x u_0^(-16) = alpha_LM^16 — exact "
               "u_0-degree bookkeeping (16 - 32 = -16), exact Fraction "
               "identity at 4 rational test points, float check "
               "< 1e-12 relative: over the declared ratio "
               "normalization, DELTA0 closure is exactly equivalent to "
               "ONE factor alpha_s per taste decoupling",
          deg_lhs == deg_rhs == Fraction(-16) and frac_ok
          and abs(float_lhs / float_rhs - 1.0) < 1e-12,
          f"u_0^16 alpha_s^16 = {float_lhs:.6e}, alpha_LM^16 = "
          f"{float_rhs:.6e}")

    # C4 [B]: the gate note records the geometric progression (fact 3).
    gate = (DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_"
                   "NOTE_2026-05-30.md")
    gate_text = gate.read_text() if gate.exists() else ""
    gate_flat = " ".join(gate_text.split())
    check("B", "C4 gate-note fact 3 on disk: the triplet alpha_bare, "
               "alpha_LM = alpha_bare/u_0, alpha_s = alpha_bare/u_0^2 "
               "is recorded as a constant-ratio geometric progression "
               "whose transport interpretation is the open gate",
          "alpha_s = alpha_bare/u_0^2" in gate_flat
          and "constant-ratio geometric progression" in gate_flat
          and "open gate" in gate_flat)

    # C5 [B]: YT cross-lane constant — context pointer ONLY.
    yt = (DOCS / "YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_"
                 "NOTE_2026-04-17.md")
    yt_text = yt.read_text() if yt.exists() else ""
    check("B", "C5 cross-lane consistency (context pointer only, never "
               "support): the YT lane's retained constant "
               "alpha_s^SM(v) = alpha_bare/u_0^2 = 0.1033 is on disk "
               "and matches this runner's alpha_s to its quoted 4 d.p.",
          "alpha_s^SM(v) = alpha_bare / u_0^2 = 0.1033" in yt_text
          and abs(ALPHA_S - 0.1033) < 5e-5,
          f"alpha_s = {ALPHA_S:.7f} -> 0.1033 at 4 d.p.")


# ---------------------------------------------------------------------------
# Section D — decomposition-ambiguity honesty.
# ---------------------------------------------------------------------------
def section_d(d_unit):
    print("\n--- Section D [C]/[A]: decomposition-ambiguity honesty — "
          "the per-mode '2' admits multiple exact readings ---")

    # D1 [C]: exact readings of the '2'.  Per-direction operators D_mu
    # (eta phases included) each square to -I and pairwise anticommute,
    # so D^2 = -(sum_mu 1) I = -d I: the per-direction unit is
    # sin^2(pi/2) = 1 (reading 2 = 2 sin(pi/2) from the corner symbol),
    # while the block eigenvalue magnitude 2 u_0 = sqrt(d) u_0 reads the
    # same '2' as sqrt(4) = sqrt(d) at d = 4 — both exact.
    d_mus = [single_direction_operator(mu) for mu in range(4)]
    sum_ok = all(sum(d_mus[mu][i][j] for mu in range(4)) == d_unit[i][j]
                 for i in range(16) for j in range(16))
    sq_ok = True
    for mu in range(4):
        sq = mat_mul(d_mus[mu], d_mus[mu])
        sq_ok = sq_ok and all(
            sq[i][j] == (Fraction(-1) if i == j else 0)
            for i in range(16) for j in range(16))
    anti_ok = True
    for mu in range(4):
        for nu in range(mu + 1, 4):
            ab = mat_mul(d_mus[mu], d_mus[nu])
            ba = mat_mul(d_mus[nu], d_mus[mu])
            anti_ok = anti_ok and all(
                ab[i][j] == -ba[i][j] for i in range(16) for j in range(16))
    check("C", "D1 exact readings of the per-mode '2': the 4 "
               "per-direction operators D_mu sum to D, EACH squares to "
               "-I (per-direction unit sin^2(pi/2) = 1, the "
               "'2 = 2 sin(pi/2)' corner-symbol reading) and pairwise "
               "anticommute, so D^2 = -4 I with 4 = d — the "
               "'2 = sqrt(4) = sqrt(d)' reading; both EXACT at d = 4",
          sum_ok and sq_ok and anti_ok and 2 ** 2 == 4,
          "exact Fraction matrix arithmetic, all 6 anticommutators")

    # D2 [A]: the readings are numerically indistinguishable — which
    # factor the '1/2' in N = alpha_s/2 belongs to is decomposition-
    # dependent; flagged as a bounded numerical observation.
    n_corner = (1.0 / (4.0 * math.pi)) * 0.5 * U_0 ** -2      # block01 split
    n_sqrt_d = (1.0 / (4.0 * math.pi)) / math.sqrt(4.0) * U_0 ** -2
    n_ratio = ALPHA_S / 2.0                                   # ratio split
    agree = (abs(n_corner / n_ratio - 1.0) < 1e-14
             and abs(n_sqrt_d / n_ratio - 1.0) < 1e-14)
    check("A", "D2 FLAGGED OBSERVATION (bounded numerical observation, "
               "no numerology claim): the decompositions "
               "N = (1/(4 pi)) x (1/2) x u_0^(-2) [block01, 1/2 vs the "
               "corner '2 = 2 sin(pi/2)'], N = (1/(4 pi)) x d^(-1/2) x "
               "u_0^(-2) [1/2 = 1/sqrt(d)], and N = alpha_s/2 [1/2 "
               "supplied by ratio normalization] are numerically "
               "IDENTICAL — the assignment of the 1/2 is not decidable "
               "by value; the ratio normalization is canonical ONLY as "
               "the framework-idiomatic choice (declared, not derived)",
          agree, f"all three give N = {n_ratio:.10f}")


# ---------------------------------------------------------------------------
# Section E — supplier ledger in the reduced form (+ residuals).
# ---------------------------------------------------------------------------
def section_e():
    print("\n--- Section E [B]: supplier ledger in the reduced form ---")

    # E1: the alpha_s VALUE has a landed supplier chain on disk:
    # I2 alpha convention + I3 g_bare = 1 + B1-licensed plaquette.
    i2 = (DOCS / "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_"
                 "NOTE_2026-05-27.md")
    i3 = (DOCS / "CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_"
                 "NOTE_2026-05-27.md")
    plaq = DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
    i2_text = i2.read_text() if i2.exists() else ""
    i3_text = i3.read_text() if i3.exists() else ""
    plaq_text = plaq.read_text() if plaq.exists() else ""
    check("B", "E1 supplier scan, the alpha_s VALUE: I2 convention row "
               "(alpha := g_bare^2/(4 pi)) + I3 g_bare = 1 surface + "
               "B1-licensed plaquette/tadpole (<P> = 0.5934 'admitted "
               "comparison/reuse number') all on disk — every factor in "
               "alpha_s = alpha_bare/u_0^2 has a landed VALUE supplier",
          "g_bare^2 / (4 pi)" in i2_text
          and "g_bare = 1" in i3_text
          and "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text)

    # Declared-open residuals — the reduced DELTA0 obstruction.
    print()
    residual("the alpha_s PER-DECOUPLING ATTACHMENT rule is UNSUPPLIED: "
             "no landed row attaches one dressed two-link gauge "
             "coupling alpha_s = alpha_bare/u_0^2 to one taste-"
             "threshold decimation.  This SINGLE transport rule "
             "replaces block01's R1 + R2 pair in the ratio-normalized "
             "reduced form; its physical shape is 'one dressed "
             "two-link gauge coupling per taste threshold'.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: over the declared ratio "
             "normalization its open content is REFRAMED from two "
             "unsupplied factors to ONE unsupplied per-decoupling "
             "transport rule — reframed and reduced, not closed.")


# ---------------------------------------------------------------------------
# Section F — falsification legs.
# ---------------------------------------------------------------------------
def section_f():
    print("\n--- Section F [A]: falsification legs ---")

    # F1: alpha_LM per mode in ratio normalization.
    frac_f1 = all(
        u ** 16 * (ab / u) ** 16 == ab ** 16
        for u in (Fraction(2, 3), Fraction(3, 5))
        for ab in (Fraction(1, 7),))
    prod_f1 = U_0 ** 16 * ALPHA_LM ** 16
    disp_f1 = prod_f1 / ALPHA_LM ** 16
    check("A", "F1 alternative 'alpha_LM per mode' in ratio "
               "normalization: u_0^16 x alpha_LM^16 = alpha_bare^16 "
               "exactly — displaced from the required alpha_LM^16 by "
               "u_0^16 = 0.1240 (the suppression magnitude is lost by "
               "one dressing power per mode)",
          frac_f1 and abs(disp_f1 - U_0 ** 16) < 1e-12
          and abs(disp_f1 / 0.123991 - 1.0) < 1e-4,
          f"displacement x {disp_f1:.6f}")

    # F2: alpha_bare per mode in ratio normalization.
    frac_f2 = all(
        (u ** 16 * ab ** 16) == ((ab / u) ** 16) * u ** 32
        for u in (Fraction(2, 3), Fraction(3, 5))
        for ab in (Fraction(1, 7),))
    prod_f2 = U_0 ** 16 * ALPHA_BARE ** 16
    disp_f2 = prod_f2 / ALPHA_LM ** 16
    check("A", "F2 alternative 'alpha_bare per mode' in ratio "
               "normalization: u_0^16 x alpha_bare^16 displaced from "
               "alpha_LM^16 = alpha_bare^16 u_0^(-16) by u_0^32 = "
               "0.015374 exactly (two dressing powers per mode short)",
          frac_f2 and abs(disp_f2 - U_0 ** 32) < 1e-12
          and abs(disp_f2 / 0.0153738 - 1.0) < 1e-4,
          f"displacement x {disp_f2:.7f}")

    # F3: the bare (non-ratio) normalization reproduces block01's N.
    n_bare = ALPHA_LM / (2.0 * U_0)
    n_closed = 1.0 / (8.0 * math.pi * U_0 ** 2)
    check("A", "F3 consistency with the landed block01 probe: dropping "
               "the ratio normalization reproduces block01's per-mode "
               "constant N = alpha_LM/(2 u_0) = 1/(8 pi u_0^2) = "
               "0.0516519 = alpha_s/2 — the reduction changes the "
               "bookkeeping, not the landed numbers",
          abs(n_bare / n_closed - 1.0) < 1e-14
          and abs(n_bare - 0.0516519) < 1e-7
          and abs(n_bare / (ALPHA_S / 2.0) - 1.0) < 1e-14,
          f"N = {n_bare:.10f}")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this reduction; "
          "the ratio")
    print("   algebra and the supplier ledger are internal structure "
          "only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_ratio_normalized_alpha_s_reduction_"
          "2026_06_11.py")
    print(" Block02 of the DELTA0 blocking campaign: over the DECLARED ratio")
    print(" normalization (per-mode factor at u_0 over the same factor at "
          "u_0 = 1),")
    print(" DELTA0 closure is exactly equivalent to supplying ONE factor "
          "alpha_s per")
    print(" taste decoupling.  Reduction, not closure: the attachment rule "
          "stays open.")
    print(" Parent note: docs/HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_"
          "PER_DECOUPLING_")
    print("              REDUCTION_NOTE_2026-06-11.md")
    print("=" * 78)

    d_unit = staggered_operator()
    section_a(d_unit)
    section_b()
    section_c()
    section_d(d_unit)
    section_e()
    section_f()
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded): over the DECLARED ratio "
          "normalization the")
    print("   per-mode decimation factor is u_0 exactly (the bare '2' "
          "cancels) and the")
    print("   remaining per-mode gap is exactly alpha_s = alpha_bare/u_0^2 "
          "= 0.1033038;")
    print("   the product identity u_0^16 alpha_s^16 = alpha_LM^16 holds "
          "exactly, so")
    print("   DELTA0 closure reduces to ONE unsupplied transport rule: "
          "one dressed")
    print("   two-link gauge coupling alpha_s per taste threshold.  NOT "
          "established:")
    print("   the attachment rule itself; the ratio normalization is a "
          "declared choice")
    print("   with a cited precedent, not a derivation.  DELTA0 stays "
          "open; obstruction")
    print("   reduced from two unsupplied factors to one, not closed.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
