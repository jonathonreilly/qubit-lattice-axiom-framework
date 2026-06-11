#!/usr/bin/env python3
"""DELTA0 blocking-RG probe: single taste-mode decimation on the minimal block

    docs/HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_PROBE_NOTE_2026-06-11.md

Campaign hypothesis under probe (NOT assumed true): one taste-mode
decimation (Schur complement / partial Grassmann integration of one
corner mode out of the 16 on the minimal 2^4 all-antiperiodic mean-field
block) costs exactly one factor alpha_bare/u_0 = alpha_LM, with the
4 pi in alpha_bare = 1/(4 pi) (at g_bare = 1) entering through the
framework's static-source/Green-kernel normalization chain
(V(r) = -C g^2 G(r), G(r) -> 1/(4 pi |r|); the Plancherel bridge note).

What this runner establishes (bounded, exact arithmetic):

  Section A (baseline reproduction, class [C]): the minimal-block
      eta-phase staggered operator is rebuilt exactly as in the landed
      honest-status runner (scripts/frontier_hierarchy_formula_honest_
      status.py); D real antisymmetric, D^2 = -4 u_0^2 I, char poly
      (lambda^2 + 4)^8 for D/u_0, det(u_0 D + m) = (m^2 + 4 u_0^2)^8
      per color, |det| = 4^8 u_0^16 at m = 0, u_0-degree 16 from a
      two-point ratio (T1.ii facts of the honest-status note).

  Section B (single-mode decimation, class [C]): an exact rational
      taste eigenbasis is constructed (even-site symplectic pairs
      e_x, f_x = D e_x / 2; taste modes v_x^{+-} = e_x -+ i f_x with
      D v = +-2i u_0 v; Gaussian-rational arithmetic throughout).  The
      quadratic form Q = chibar (u_0 D + m) chi is split into a kept
      15-mode block and one decimated mode; the Grassmann pair is
      integrated out exactly via the Schur complement.  Established:
      (i)  the decimation contributes the multiplicative factor
           S = m +- 2i u_0 to the partition function — magnitude
           sqrt(m^2 + 4 u_0^2), i.e. exactly 2 u_0 at m = 0;
      (ii) the induced effective-action shift on the kept 15 modes is
           EXACTLY ZERO in the taste eigenbasis (B S^-1 C = 0);
      (iii) the per-mode u_0-degree is exactly 1; sixteen sequential
           decimations multiply to det(u_0 D + m) exactly.
      CONFIRMS the expectation from the landed algebra: one decimation
      step carries 2 u_0 per mode in |det| — NOT alpha_LM.

  Section C (normalization attach — the actual probe, classes [A]/[B]):
      the per-mode factor in the bare-determinant normalization is
      2 u_0 (C1).  For the 16-mode product to equal alpha_LM^16, each
      mode would need the extra normalization
          N = alpha_LM / (2 u_0) = alpha_bare / (2 u_0^2)
            = 1 / (8 pi u_0^2)   at g_bare = 1   (C2),
      with the exact decomposition N = (1/(4 pi)) x (1/(2 u_0^2)) (C3).
      Supplier scan (C4-C6): the VALUE 1/(4 pi) has a landed supplier
      chain (Plancherel bridge B1-B5 + I2 convention + I3 g_bare = 1
      surface); the VALUE u_0 is licensed (plaquette B1 reuse license);
      but NO landed row supplies a per-mode attachment rule for the
      1/(4 pi), and NO landed row supplies the per-mode factor
      1/(2 u_0^2) at all.  These are printed as RESIDUAL
      (declared-open) lines — the sharpened DELTA0 obstruction.  The
      probe does NOT close the DELTA0 gate.

  Section D (falsification legs, classes [C]/[A]):
      F1  mode independence: all 16 modes give the same factor
          magnitude (exact, both rational test couplings);
      F2  N != 1: the bare block algebra alone does NOT supply
          alpha_LM — consistency check against the DELTA0 gate's
          recorded obstruction (u_0-only block observables);
      F3  alternative hypothesis 'per-mode factor = alpha_bare alone'
          (no 1/u_0) displaces the 16-mode product from alpha_LM^16 by
          u_0^(-16) = 8.065 — computed;
      F4  basis honesty: decimating one POSITION-basis Grassmann pair
          gives factor m (not sqrt(m^2 + 4 u_0^2)); the single-step
          factor is basis-dependent, only the 16-step product (the
          determinant) is basis-independent.

  Terminal class-D fence: no PDG comparator is needed or consumed by
      this probe; a self-scan certifies the PDG VEV literal is absent
      from this runner's source.

Vocabulary discipline: nothing here is 'derived' past its declared
premises.  Section A/B facts are bounded_theorem-grade exact algebra;
Section C consumes the B1 plaquette reuse license and the I2/I3
convention rows by citation; all unsupplied factors are declared as
RESIDUAL (declared-open) lines, never as PASSes and never as FAILs.

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
#   the I2 convention row + I3 g_bare = 1 surface (Plancherel bridge).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_LM = ALPHA_BARE / U_0          # = 0.090668


# ---------------------------------------------------------------------------
# Exact real linear algebra (Fractions) — same style as the landed
# honest-status runner.
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


def char_poly_exact(a):
    """Faddeev-LeVerrier: [1, c1, ..., cn], exact Fractions."""
    n = len(a)
    coeffs = [Fraction(1)]
    m = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
         for i in range(n)]
    for k in range(1, n + 1):
        am = mat_mul(a, m)
        tr = sum(am[i][i] for i in range(n))
        ck = -tr / k
        coeffs.append(ck)
        m = [row[:] for row in am]
        for i in range(n):
            m[i][i] += ck
    return coeffs


# ---------------------------------------------------------------------------
# Exact Gaussian-rational (complex Fraction) arithmetic.
# A complex number is a tuple (re, im) of Fractions.
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


def cdet(a_in):
    a = [row[:] for row in a_in]
    n = len(a)
    det = CONE
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != CZERO), None)
        if piv is None:
            return CZERO
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = (-det[0], -det[1])
        det = cmul(det, a[col][col])
        inv = cinv(a[col][col])
        for r in range(col + 1, n):
            if a[r][col] != CZERO:
                f = cmul(a[r][col], inv)
                for c2 in range(col, n):
                    a[r][c2] = csub(a[r][c2], cmul(f, a[col][c2]))
    return det


# ---------------------------------------------------------------------------
# Minimal-block staggered operator — construction REUSED verbatim from
# scripts/frontier_hierarchy_formula_honest_status.py so the block
# operator provably matches the landed T1.ii surface.
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


def taste_eigenbasis(d_unit):
    """Exact taste-mode basis from even-site symplectic pairs.

    For each of the 8 even-parity sites x: e_x = position basis vector,
    f_x = D e_x / 2 (supported on odd sites; |f_x| = 1 since D^2 = -4).
    Taste modes: v_x^+ = e_x - i f_x (eigenvalue +2i),
                 v_x^- = e_x + i f_x (eigenvalue -2i).
    Columns are pairwise orthogonal with Hermitian norm^2 = 2, so
    T^-1 = T_dagger / 2 exactly.  All entries Gaussian-rational."""
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
    """Integrate out the single Grassmann pair (chibar_d, chi_d).

    Returns (factor S = M'[d][d], kept-block Schur complement
    K - B S^-1 C, induced shift B S^-1 C on the kept 15 modes)."""
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
# Section A — baseline reproduction of the landed T1.ii facts.
# ---------------------------------------------------------------------------
def section_a(d_unit):
    print("\n--- Section A [C]: baseline reproduction (honest-status T1.ii "
          "facts, exact arithmetic) ---")

    # A1: D real antisymmetric, D^2 = -4 I at u_0 = 1.
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(16) for j in range(16))
    d2 = mat_mul(d_unit, d_unit)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(16) for j in range(16))
    check("C", "A1 minimal 2^4 all-APBC eta-phase block: D real "
               "antisymmetric and D^2 = -4 u_0^2 I (u_0 = 1 surface)",
          antisym and d2_ok, "exact Fraction matrix arithmetic")

    # A2: char poly of D/u_0 is (lambda^2 + 4)^8.
    coeffs = char_poly_exact(d_unit)
    target = [Fraction(0)] * 17
    for k in range(9):
        target[2 * k] = Fraction(math.comb(8, k) * 4 ** k)
    check("C", "A2 char poly of D/u_0 is (lambda^2 + 4)^8 — 16 taste "
               "modes +-2i u_0, multiplicity 8 each",
          coeffs == target, "Faddeev-LeVerrier, exact")

    # A3: det(u_0 D + m) = (m^2 + 4 u_0^2)^8 at rational test points.
    pts = [(Fraction(2, 3), Fraction(0)), (Fraction(2, 3), Fraction(1, 3)),
           (Fraction(3, 5), Fraction(2, 7))]
    det_id_ok = True
    for a, m in pts:
        mat_am = [[a * d_unit[i][j] + (m if i == j else 0)
                   for j in range(16)] for i in range(16)]
        det_id_ok = det_id_ok and det_exact(mat_am) == (m * m + 4 * a * a) ** 8
    check("C", "A3 det(u_0 D + m) = (m^2 + 4 u_0^2)^8 per color at 3 "
               "rational (u_0, m) test points", det_id_ok,
          "u_0 in {2/3, 3/5}, m in {0, 1/3, 2/7}")

    # A4: m = 0 magnitude (2 u_0)^16 = 4^8 u_0^16; exact u_0-degree 16.
    a1, a2 = Fraction(2, 3), Fraction(3, 5)
    det_a1 = det_exact([[a1 * x for x in row] for row in d_unit])
    det_a2 = det_exact([[a2 * x for x in row] for row in d_unit])
    mag_ok = det_a1 == Fraction(4) ** 8 * a1 ** 16
    degree_ok = det_a1 * a2 ** 16 == det_a2 * a1 ** 16
    check("C", "A4 |det(u_0 D)| = (2 u_0)^16 = 4^8 u_0^16 at m = 0; "
               "exact u_0-degree from a two-point ratio = 16 = species "
               "count", mag_ok and degree_ok,
          "matches honest-status T1.ii exactly")


# ---------------------------------------------------------------------------
# Section B — single taste-mode decimation (Schur complement).
# ---------------------------------------------------------------------------
def section_b(d_unit):
    print("\n--- Section B [C]: single-mode Schur decimation in the exact "
          "taste eigenbasis ---")

    t_mat, t_inv, eigs = taste_eigenbasis(d_unit)
    n = 16

    # B1: T columns are exact eigenvectors of D; T^-1 T = I exactly.
    d_cplx = complex_block_matrix(d_unit, Fraction(1), Fraction(0))
    dt = cmat_mul(d_cplx, t_mat)
    eig_ok = all(dt[i][j] == cmul(eigs[j], t_mat[i][j])
                 for i in range(n) for j in range(n))
    tt = cmat_mul(t_inv, t_mat)
    inv_ok = all(tt[i][j] == (CONE if i == j else CZERO)
                 for i in range(n) for j in range(n))
    check("C", "B1 exact taste eigenbasis: 16 Gaussian-rational columns "
               "with D v = +-2i v (8 each, from even-site symplectic "
               "pairs e_x, f_x = D e_x/2); T^-1 = T_dag/2 and "
               "T^-1 T = I exactly", eig_ok and inv_ok)

    # B2: M' = T^-1 (u_0 D + m) T exactly diagonal, entries m +- 2i u_0.
    a, m = Fraction(2, 3), Fraction(1, 3)
    m_cplx = complex_block_matrix(d_unit, a, m)
    m_prime = cmat_mul(t_inv, cmat_mul(m_cplx, t_mat))
    diag_ok = all(m_prime[i][j] == CZERO
                  for i in range(n) for j in range(n) if i != j)
    entries_ok = all(m_prime[j][j] == cadd((m, Fraction(0)),
                                           cmul((a, Fraction(0)), eigs[j]))
                     for j in range(n))
    plus = sum(1 for j in range(n) if m_prime[j][j][1] > 0)
    check("C", "B2 quadratic form Q = chibar (u_0 D + m) chi is exactly "
               "diagonal over the 16 taste modes: entries m +- 2i u_0, "
               "multiplicity 8 each",
          diag_ok and entries_ok and plus == 8,
          "u_0 = 2/3, m = 1/3, Gaussian-rational")

    # B3: single-mode decimation — multiplicative factor and exact
    # determinant bookkeeping det M = S x det(Schur complement).
    s_fac, schur, _shift = schur_decimate(m_prime, 0)
    det_full = det_exact([[a * d_unit[i][j] + (m if i == j else 0)
                           for j in range(16)] for i in range(16)])
    det_schur = cdet(schur)
    det_product = cmul(s_fac, det_schur)
    factor_ok = s_fac == (m, 2 * a)
    det_ok = det_product == (det_full, Fraction(0))
    check("C", "B3 integrating ONE Grassmann pair out: multiplicative "
               "factor S = m + 2i u_0 exactly; det(u_0 D + m) = "
               "S x det(kept 15-mode Schur complement) exactly",
          factor_ok and det_ok,
          f"S = {s_fac[0]} + {s_fac[1]} i at (u_0, m) = (2/3, 1/3)")

    # B4: induced effective action on the kept 15 modes.
    _s2, _schur2, shift2 = schur_decimate(m_prime, 3)
    shift_zero = all(x == CZERO for row in shift2 for x in row)
    check("C", "B4 induced effective-action / coupling shift on the kept "
               "15 modes is EXACTLY ZERO in the taste eigenbasis "
               "(B S^-1 C = 0): the decimation is purely multiplicative",
          shift_zero)

    # B5: per-mode factor magnitude and exact per-mode u_0-degree 1.
    a2 = Fraction(3, 5)
    mag_checks = []
    for aa in (a, a2):
        mp = cmat_mul(t_inv, cmat_mul(
            complex_block_matrix(d_unit, aa, m), t_mat))
        s, _, _ = schur_decimate(mp, 0)
        mag_checks.append(cabs2(s) == m * m + 4 * aa * aa)
    # m = 0 limit via the known factor structure: |S|^2 = 4 u_0^2.
    s0_a1 = schur_decimate(cmat_mul(t_inv, cmat_mul(
        complex_block_matrix(d_unit, a, Fraction(0)), t_mat)), 0)[0]
    s0_a2 = schur_decimate(cmat_mul(t_inv, cmat_mul(
        complex_block_matrix(d_unit, a2, Fraction(0)), t_mat)), 0)[0]
    m0_ok = cabs2(s0_a1) == 4 * a * a and cabs2(s0_a2) == 4 * a2 * a2
    degree1_ok = cabs2(s0_a1) * a2 * a2 == cabs2(s0_a2) * a * a
    check("C", "B5 per-mode factor magnitude |S| = sqrt(m^2 + 4 u_0^2); "
               "at m = 0 exactly 2 u_0 per mode; per-mode u_0-degree "
               "exactly 1 (two-point ratio)",
          all(mag_checks) and m0_ok and degree1_ok,
          "ONE decimation step carries 2 u_0, NOT alpha_LM")

    # B6: sixteen sequential decimations reproduce the determinant.
    prod = CONE
    work = m_prime
    for _ in range(16):
        s, work, _ = schur_decimate(work, 0) if len(work) > 1 else (
            work[0][0], [], None)
        prod = cmul(prod, s)
    det_m0 = det_exact([[a * x for x in row] for row in d_unit])
    # product at (a, m): equals (m^2 + 4 a^2)^8.
    seq_ok = prod == ((m * m + 4 * a * a) ** 8, Fraction(0))
    mp0 = cmat_mul(t_inv, cmat_mul(
        complex_block_matrix(d_unit, a, Fraction(0)), t_mat))
    prod0 = CONE
    work = mp0
    for _ in range(16):
        s, work, _ = schur_decimate(work, 0) if len(work) > 1 else (
            work[0][0], [], None)
        prod0 = cmul(prod0, s)
    seq0_ok = prod0 == (det_m0, Fraction(0)) and cabs2(prod0) == (
        (2 * a) ** 16) ** 2
    check("C", "B6 sixteen sequential single-mode decimations multiply "
               "exactly to det(u_0 D + m) = (m^2 + 4 u_0^2)^8; at m = 0 "
               "the product magnitude is (2 u_0)^16",
          seq_ok and seq0_ok, "exact sequential Schur chain")

    return t_mat, t_inv, eigs


# ---------------------------------------------------------------------------
# Section C — normalization attach (the actual probe).
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- Section C [A]/[B]: normalization attach — can the "
          "static-source chain convert 2 u_0 -> alpha_LM per mode? ---")

    # C1: per-mode factor in the bare-determinant normalization.
    per_mode_bare = 2.0 * U_0
    check("A", "C1 per-mode decimation factor in the bare-determinant "
               "normalization = 2 u_0 = 1.7553628 (B1-licensed value; "
               "established exactly in Section B)",
          abs(per_mode_bare - 1.7553628) < 1e-7,
          f"2 u_0 = {per_mode_bare:.7f}")

    # C2: required per-mode normalization N = alpha_LM / (2 u_0).
    n_req = ALPHA_LM / (2.0 * U_0)
    n_closed = 1.0 / (8.0 * math.pi * U_0 ** 2)
    check("A", "C2 required per-mode normalization N = alpha_LM/(2 u_0) "
               "= alpha_bare/(2 u_0^2) = 1/(8 pi u_0^2) at g_bare = 1 "
               "= 0.0516519 (two routes agree)",
          abs(n_req / n_closed - 1.0) < 1e-14
          and abs(n_req - 0.0516519) < 1e-7,
          f"N = {n_req:.10f}")

    # C3: decomposition of N into candidate framework-supplied objects,
    # and the 16-mode product identity.
    n_decomp = (1.0 / (4.0 * math.pi)) * (1.0 / (2.0 * U_0 ** 2))
    prod16 = (2.0 * U_0 * n_req) ** 16
    check("A", "C3 exact decomposition N = (1/(4 pi)) x (1/(2 u_0^2)); "
               "16-mode product check (2 u_0 x N)^16 = alpha_LM^16",
          abs(n_req / n_decomp - 1.0) < 1e-14
          and abs(prod16 / ALPHA_LM ** 16 - 1.0) < 1e-12,
          f"(2 u_0 N)^16 = {prod16:.6e}, alpha_LM^16 = "
          f"{ALPHA_LM ** 16:.6e}")

    # C4 [B]: supplier scan for the 1/(4 pi) factor — landed chain on disk.
    bridge = (DOCS / "ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_"
                     "BOUNDED_NOTE_2026-05-26.md")
    i2 = (DOCS / "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_"
                 "NOTE_2026-05-27.md")
    i3 = (DOCS / "CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_"
                 "NOTE_2026-05-27.md")
    bridge_text = bridge.read_text() if bridge.exists() else ""
    i2_text = i2.read_text() if i2.exists() else ""
    i3_text = i3.read_text() if i3.exists() else ""
    check("B", "C4 supplier scan, factor 1/(4 pi): Plancherel bridge "
               "chain on disk (Green kernel G(r) -> 1/(4 pi |r|); I2 "
               "convention alpha_bare := g_bare^2/(4 pi); I3 g_bare = 1 "
               "surface) — the VALUE 1/(4 pi) has a landed supplier",
          "G(r) -> 1/(4 pi |r|)" in bridge_text
          and "alpha_bare := g_bare^2 / (4 pi)" in bridge_text
          and "g_bare^2 / (4 pi)" in i2_text
          and "g_bare = 1" in i3_text)

    # C5 [B]: supplier scan for the u_0 value and the recorded
    # obstruction — plaquette B1 license + DELTA0 gate note on disk.
    plaq_text = (DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md").read_text()
    gate = (DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_"
                   "NOTE_2026-05-30.md")
    gate_text = gate.read_text() if gate.exists() else ""
    gate_flat = " ".join(gate_text.split())
    check("B", "C5 supplier scan, factor u_0: VALUE licensed by the "
               "plaquette B1 reuse license; DELTA0 gate note on disk "
               "records the obstruction (block observables u_0-only; "
               "transport source open)",
          "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text
          and "open_gate" in gate_text
          and "u_0-only" in gate_flat
          and ("transport source for that coupling-power magnitude on "
               "the current baseline: open" in gate_flat))

    # C6 [B]: the blocking mechanism naming — the YT-P2 no-go forecloses
    # per-step 1-loop perturbative beta integration but names the
    # non-perturbative blocking mechanism and leaves blocking-RG open.
    nogo = (DOCS / "YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_"
                   "NOTE_2026-04-17.md")
    nogo_text = nogo.read_text() if nogo.exists() else ""
    nogo_flat = " ".join(nogo_text.split())
    check("B", "C6 mechanism scoping: YT-P2 no-go on disk names "
               "'non-perturbative blocking renormalization' and "
               "explicitly leaves blocking-RG / strong-coupling routes "
               "open — this probe lives inside the permitted route",
          "non-perturbative blocking renormalization" in nogo_flat
          and "blocking RG, strong coupling expansion" in nogo_flat)

    # Declared-open residuals — the sharpened DELTA0 obstruction.
    print()
    residual("the per-mode ATTACHMENT of the supplied value alpha_bare "
             "= 1/(4 pi) to a single decimation step has no landed "
             "transport rule — the Plancherel bridge supplies the "
             "static-source VALUE, not a per-decimation rule.")
    residual("the per-mode factor 1/(2 u_0^2) inside N = alpha_LM/(2 u_0) "
             "has NO landed supplier at all: the block algebra supplies "
             "u_0-degree +1 per mode (not -2), and the bare 1/2 that "
             "would cancel the determinant's per-mode 2 = 2 sin(pi/2) "
             "is unsupplied.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: this probe sharpens the "
             "obstruction to the per-mode normalization "
             "N = alpha_bare/(2 u_0^2) = 1/(8 pi u_0^2) = 0.0516519, "
             "it does not close the gate.")


# ---------------------------------------------------------------------------
# Section D — falsification legs.
# ---------------------------------------------------------------------------
def section_d(d_unit, t_mat, t_inv):
    print("\n--- Section D [C]/[A]: falsification legs ---")

    # F1: mode independence of the decimation factor — all 16 modes.
    a, a2, m = Fraction(2, 3), Fraction(3, 5), Fraction(1, 3)
    f1_ok = True
    for aa in (a, a2):
        mp = cmat_mul(t_inv, cmat_mul(
            complex_block_matrix(d_unit, aa, m), t_mat))
        for d_idx in range(16):
            s = mp[d_idx][d_idx]
            col_ok = all(mp[i][d_idx] == CZERO
                         for i in range(16) if i != d_idx)
            row_ok = all(mp[d_idx][j] == CZERO
                         for j in range(16) if j != d_idx)
            f1_ok = f1_ok and col_ok and row_ok and (
                cabs2(s) == m * m + 4 * aa * aa)
    check("C", "F1 mode independence: every one of the 16 taste modes "
               "decimates with the SAME factor magnitude "
               "sqrt(m^2 + 4 u_0^2), purely multiplicatively, at both "
               "rational test couplings", f1_ok,
          "32 single-mode decimations, exact")

    # F2: N != 1 — the bare block algebra alone does NOT supply alpha_LM.
    n_req = ALPHA_LM / (2.0 * U_0)
    check("A", "F2 the required per-mode normalization N = 0.0517 is NOT "
               "1: the bare block determinant supplies 2 u_0 per mode, "
               "not alpha_LM — consistent with (and reproducing) the "
               "DELTA0 gate's recorded u_0-only obstruction; a "
               "consistency check, not a failure",
          abs(n_req - 1.0) > 0.9 and 2.0 * U_0 != ALPHA_LM,
          f"N = {n_req:.7f}, |log10 N| = {abs(math.log10(n_req)):.4f}")

    # F3: alternative hypothesis 'per-mode factor = alpha_bare alone'.
    displacement = ALPHA_LM ** 16 / ALPHA_BARE ** 16
    check("A", "F3 alternative hypothesis 'per-mode factor = alpha_bare "
               "alone' (no 1/u_0) displaces the 16-mode product from "
               "alpha_LM^16 by u_0^(-16) = 8.065",
          abs(displacement - U_0 ** -16) < 1e-9
          and abs(displacement / 8.0652 - 1.0) < 1e-3,
          f"alpha_LM^16/alpha_bare^16 = {displacement:.4f}")

    # F4: basis honesty — position-basis single-pair decimation.
    aa, mm = Fraction(2, 3), Fraction(1, 3)
    m_pos = [[aa * d_unit[i][j] + (mm if i == j else 0)
              for j in range(16)] for i in range(16)]
    s_pos = m_pos[0][0]
    kept = list(range(1, 16))
    schur_pos = [[m_pos[i][j] - m_pos[i][0] * m_pos[0][j] / s_pos
                  for j in kept] for i in kept]
    det_id = s_pos * det_exact(schur_pos) == det_exact(m_pos)
    check("C", "F4 basis honesty: decimating one POSITION-basis pair "
               "gives factor m (= 1/3 here), NOT sqrt(m^2 + 4 u_0^2); "
               "det M = m x det(position Schur complement) still holds "
               "exactly — the single-step factor is basis-dependent, "
               "only the full 16-step product is basis-independent",
          s_pos == mm and s_pos * s_pos != mm * mm + 4 * aa * aa
          and det_id,
          "the '2 u_0 per mode' reading is specific to the taste basis")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; the "
          "per-mode")
    print("   algebra and the normalization residual are internal "
          "structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "D1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_blocking_single_mode_probe_2026_06_11.py")
    print(" DELTA0 blocking-RG probe: does ONE taste-mode decimation cost")
    print(" alpha_bare/u_0 = alpha_LM?  (Campaign hypothesis under exact test;")
    print(" baseline = honest-status T1.ii minimal 2^4 block, reused verbatim.)")
    print(" Parent note: docs/HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_"
          "DECIMATION_PROBE_NOTE_2026-06-11.md")
    print("=" * 78)

    d_unit = staggered_operator()
    section_a(d_unit)
    t_mat, t_inv, _eigs = section_b(d_unit)
    section_c()
    section_d(d_unit, t_mat, t_inv)
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded): one taste-mode decimation "
          "carries exactly")
    print("   one factor 2 u_0 (per-mode u_0-degree 1, zero induced "
          "coupling shift in")
    print("   the taste basis); NOT established: the campaign hypothesis "
          "factor alpha_LM")
    print("   per mode — it would require the per-mode normalization "
          "N = alpha_bare/(2 u_0^2)")
    print("   = 1/(8 pi u_0^2), whose 1/(4 pi) VALUE has a landed "
          "supplier but whose")
    print("   per-mode attachment and 1/(2 u_0^2) factor do not. "
          "DELTA0 stays open;")
    print("   obstruction sharpened, not closed.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
