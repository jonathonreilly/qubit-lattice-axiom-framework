#!/usr/bin/env python3
"""DELTA0 route-inventory synthesis: the single citeable object for
'what stands between the hierarchy formula and a closed B4'

    docs/HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_
    NOTE_2026-06-11.md

Block07 of the DELTA0 blocking campaign.  Patterned on the YT master
obstruction theorem (YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_
2026-04-17.md): this runner ENUMERATES, it fixes the route
decomposition, and downstream rows refine routes without modifying the
inventory.  It closes nothing and changes no gate status.

What this runner establishes (bounded; everything cited is recomputed
or verified against the cited note's stated values as declared inputs):

  Section A (the reduced target, classes [A]/[B]): over the declared
      ratio normalization of campaign block02, B4 closure is EXACTLY
      equivalent to one landed transport rule supplying one factor
          alpha_s = alpha_bare/u_0^2 = 0.1033038
      per taste decoupling; equivalently the staircase rung ratio
      mu_{k+1}/mu_k = alpha_LM with per-rung observable share alpha_s
      (alpha_LM = u_0 x alpha_s exactly: the determinant supplies the
      u_0, the missing transport rule supplies the alpha_s).  The
      equivalence chain u_0^16 x alpha_s^16 = alpha_LM^16 is recomputed
      as exact Fraction bookkeeping (degrees 16 - 32 = -16), as an
      exact rational identity, and as a float identity < 1e-12
      relative; ln(alpha_LM) = -2.4006 (the YT-P2 retained per-rung
      log interval) and N = 1/(8 pi u_0^2) = alpha_s/2 = 0.0516519 are
      recomputed.

  Section B (eliminated routes E1-E5, classes [A]/[B]/[C]; each key
      number recomputed here, each eliminating runner re-invoked in
      Section C):
      E1  quadratic block algebra at frozen links — block01: one
          taste-mode decimation carries m +- 2i u_0 with EXACTLY ZERO
          induced coupling shift; recomputed from scratch here in
          exact Gaussian-rational arithmetic (block construction
          reused verbatim from block01/honest-status).
      E2  bare relabeling u_0^16 -> alpha_LM^16 — honest-status
          identity (S): alpha_LM^16 = alpha_bare^16 u_0^(-16)
          (residual < 1e-12 recomputed); the relabeling is
          bookkeeping, not transport; the determinant's own u_0^16 is
          displaced from alpha_LM^16 by x 5.94e15.
      E3  mean-field link feedback — block04: feedback factor R in
          [1.0000412422, 1.087382] across every declared variant,
          branch and sharing convention, minimum displacement
          R/alpha_s = 9.681 (recomputed from the note's recorded
          saddle values, consumed as declared inputs).  REFUTED under
          all declared variants.
      E4  per-step 1-loop perturbative beta — YT-P2 no-go: b_3(16) =
          1/3 exactly (AF-marginal; b_3(17) = -1/3 < 0) and the
          cumulative 1-loop correction 2.594 exceeds the lattice UV
          anchor 1/g^2 = u_0 = 0.878 (Landau-pole crossing), both
          recomputed.
      E5  coupling-independent-c dimensional-transmutation rewrite —
          dim-trans note: c_eff = 16 alpha_LM ln(1/alpha_LM) = 3.4824
          (note prose quotes 3.4832 from its 4-d.p. alpha_LM = 0.0907;
          reproduced here from the quoted input), identity
          alpha_LM^16 = exp(-c_eff/alpha_LM) < 1e-12 relative, and
          c_eff is coupling-DEPENDENT (dc_eff/dalpha != 0) — not a
          canonical dim-trans constant.

  Section C (eliminating runners re-verified, class [B]): the five
      cited runners are invoked as subprocesses; exit code 0 and the
      note-stated totals are required (block01 21/0, block02 19/0,
      block04 mean-field 20/0, YT-P2 12/0, dim-trans 5/0).

  Section D (surviving routes S1-S3, class [A]/[B] + residuals): the
      three routes left open by the eliminated set, each printed as a
      RESIDUAL (declared-open) line with its named gate input, what
      already constrains it, and its kill criterion:
      S1  strong-coupling one-link Haar / Kawamoto-Smit lineage —
          already constrained at LEADING order by the landed NJL row:
          G_eff = 1/(2 N_c) = 1/6 = 0.16667 < G_critical = u_0^2/4 =
          0.192581 (both recomputed; ratio 0.8654, sigma_min^2 =
          16 G_eff - 4 u_0^2 = -0.4146 < 0, symmetric phase, no
          broken-phase saddle), so S1 survives ONLY at beyond-leading
          order or with electroweak-sector structure added.
      S2  readout-side dressing of the Green-kernel/static-source
          chain (vacuum polarization on the 1/(4 pi) supplier rather
          than on the saddle) — unprobed.
      S3  a direct non-link transport rule (threshold mass
          generation: rung ratio from a gap-equation spectrum) — the
          NJL symmetric-phase result also constrains its
          lattice-gauge-only version (no gap-equation spectrum exists
          there at leading order); an EW-sector-driven version is
          open.

  Section E (claim-shape ceiling, class [B]): on-disk scans of the
      regulator-dependence no-go (routes O1-O3 enumerated; exponent
      substrate-imposed, never regulator-independent) and of the
      scale-reference primitive's anti-promotion policy ('should not
      become retained_bounded merely for using a ruler'): the lane's
      honest ceiling is retained_bounded over {axioms + approved
      primitives + declared conventions}.

  Section F (non-modification + fence, classes [B]/[D]): the DELTA0
      gate note is still an open gate on disk; the parent synthesis
      note carries the required disclaimers and modifies nothing; the
      PDG VEV literal is certified absent from this runner's source.

  Flagged recomputation deviations (findings, recorded as PASS-line
      details, since recomputation governs and the qualitative
      conclusions are unchanged):
      (i)  the NJL note's prose sigma_min^2(formal) ~= -0.4561
           deviates from the recomputed 16 G_eff - 4 u_0^2 = -0.4141
           (at the note's own u_0 = 0.8776); the sign — hence the
           symmetric-phase verdict — is unchanged;
      (ii) the dim-trans note's prose c_eff ~= 3.4832 is the rounded-
           input value (alpha_LM = 0.0907); its own runner and this
           one compute 3.4824 at full B1 precision.

Vocabulary discipline: nothing here is 'derived' past its declared
premises.  The recomputed algebra is bounded_theorem-grade; the route
inventory itself is a META decomposition (declared, citeable,
refinable downstream) — not a claim that the surviving routes succeed
and not a closure of anything.  All open content is printed as
RESIDUAL (declared-open) lines, never as PASSes and never as FAILs.

Deterministic, pure Python stdlib (fractions, math, itertools,
subprocess on sibling repo scripts only), no network, no randomness.
Subprocess timeouts are generous (120 s each); total runtime is well
under three minutes (typically a few seconds).
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import math
import os
import re
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
SCRIPTS = REPO_ROOT / "scripts"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_"
                      "SYNTHESIS_NOTE_2026-06-11.md")

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


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


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
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038


# ---------------------------------------------------------------------------
# Exact Gaussian-rational (complex Fraction) arithmetic and the minimal
# 2^4 block construction — REUSED verbatim from block01
# (scripts/frontier_hierarchy_delta0_blocking_single_mode_probe_2026_06_11.py),
# which reuses the landed honest-status construction, so the recomputed
# E1 facts provably live on the same surface.
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
    """Exact taste-mode basis from even-site symplectic pairs (block01
    construction): v_x^+- = e_x -+ i f_x with f_x = D e_x / 2; columns
    pairwise orthogonal with Hermitian norm^2 = 2, T^-1 = T_dagger/2."""
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


# ---------------------------------------------------------------------------
# Section A — the reduced target (block02's reduction, recomputed).
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [A]/[B]: the REDUCED TARGET — B4 closure == one "
          "factor alpha_s per taste decoupling (block02, recomputed) ---")

    # A1: the supplied values along the geometric progression.
    alpha_s_route2 = ALPHA_LM / U_0
    n_const = 1.0 / (8.0 * math.pi * U_0 ** 2)
    a1 = (
        abs(ALPHA_S - alpha_s_route2) < 1e-14
        and abs(ALPHA_S - 0.1033038) < 5e-8
        and abs(n_const - ALPHA_S / 2.0) < 1e-15
        and abs(n_const - 0.0516519) < 5e-8
        and abs(ALPHA_LM - U_0 * ALPHA_S) < 1e-15
    )
    check("A", "A1 supplied constants recomputed: alpha_s = alpha_bare/u_0^2 "
               "= alpha_LM/u_0 = 0.1033038 (two routes agree < 1e-14); "
               "block01's bare conversion target N = 1/(8 pi u_0^2) = "
               "0.0516519 = alpha_s/2; alpha_LM = u_0 x alpha_s exactly "
               "(determinant supplies the u_0, transport must supply the "
               "alpha_s)", a1,
          f"alpha_s = {ALPHA_S:.10f}, N = {n_const:.10f}")

    # A2: the equivalence chain u_0^16 x alpha_s^16 = alpha_LM^16.
    deg_ok = (16 - 32) == -16
    sym_ok = True
    for u in (Fraction(2, 3), Fraction(3, 5)):
        for a in (Fraction(1, 13), Fraction(2, 7)):
            sym_ok &= u ** 16 * (a / u ** 2) ** 16 == (a / u) ** 16
    lhs = U_0 ** 16 * ALPHA_S ** 16
    rhs = ALPHA_LM ** 16
    rel = abs(lhs - rhs) / rhs
    check("A", "A2 equivalence chain recomputed: u_0^16 x alpha_s^16 = "
               "alpha_bare^16 x u_0^(-16) = alpha_LM^16 — exact u_0-degree "
               "bookkeeping (16 - 32 = -16), exact Fraction identity at 4 "
               "rational test points, float identity < 1e-12 relative on "
               "the B1-licensed values",
          deg_ok and sym_ok and rel < 1e-12,
          f"u_0^16 alpha_s^16 = {lhs:.6e}, alpha_LM^16 = {rhs:.6e}, "
          f"rel = {rel:.2e}")

    # A3: staircase reading (YT-P2 retained per-rung log interval).
    ln_alm = math.log(ALPHA_LM)
    a3 = (
        abs(ln_alm - (-2.4006)) < 5e-5
        and abs(16 * ln_alm - (-38.41)) < 5e-3
    )
    check("A", "A3 staircase reading recomputed: rung ratio mu_{k+1}/mu_k = "
               "alpha_LM, per-rung log interval ln(alpha_LM) = -2.4006 "
               "(the YT-P2 retained constant), 16 rungs -> total log-span "
               "-38.41; per-rung observable share alpha_s", a3,
          f"ln(alpha_LM) = {ln_alm:.6f}, 16 ln = {16 * ln_alm:.4f}")

    # A4: the reduction is on disk as the single remaining transport rule.
    txt = read_doc("HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                   "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    a4 = (
        "ONE unsupplied transport rule" in txt
        and "one dressed two-link gauge coupling" in txt
        and "alpha_s = alpha_bare/u_0^2 = 0.1033038" in txt
        and "not closed" in txt
    )
    check("B", "A4 reduced target on disk: block02 records B4's open "
               "content as exactly ONE unsupplied transport rule ('one "
               "dressed two-link gauge coupling per taste threshold') over "
               "its declared ratio normalization — reduced, not closed",
          a4)


# ---------------------------------------------------------------------------
# Section B — eliminated routes E1-E5, key numbers recomputed.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [A]/[B]/[C]: ELIMINATED ROUTES E1-E5 — each key "
          "number recomputed ---")

    # ---- E1: quadratic block algebra at frozen links (block01). ----
    d_unit = staggered_operator()
    n = len(SITES)
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(n) for j in range(n))
    d2 = [[sum(d_unit[i][k] * d_unit[k][j] for k in range(n))
           for j in range(n)] for i in range(n)]
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(n) for j in range(n))
    det_ok = True
    for u in (Fraction(2, 3), Fraction(3, 5)):
        for m in (Fraction(0), Fraction(1, 3)):
            mat = [[u * d_unit[i][j] + (m if i == j else 0)
                    for j in range(n)] for i in range(n)]
            det_ok &= det_exact(mat) == (m * m + 4 * u * u) ** 8
    check("C", "E1.a block algebra recomputed from scratch (block01 "
               "construction reused verbatim): D real antisymmetric, "
               "D^2 = -4 I, det(u_0 D + m) = (m^2 + 4 u_0^2)^8 per color "
               "at rational test couplings", antisym and d2_ok and det_ok,
          "exact Fraction arithmetic, u_0 in {2/3, 3/5}, m in {0, 1/3}")

    t_mat, t_inv, eigs = taste_eigenbasis(d_unit)
    u_test, m_test = Fraction(2, 3), Fraction(1, 3)
    m_mat = complex_block_matrix(d_unit, u_test, m_test)
    q = cmat_mul(t_inv, cmat_mul(m_mat, t_mat))
    diag_ok = True
    factor_ok = True
    for i in range(n):
        lam = cadd((m_test, Fraction(0)),
                   cmul((u_test, Fraction(0)), eigs[i]))
        factor_ok &= q[i][i] == lam            # entries m +- 2i u_0
        for j in range(n):
            if i != j and q[i][j] != CZERO:
                diag_ok = False
    # zero induced shift: with Q exactly diagonal, the cross blocks
    # B = Q[kept][dec] and C = Q[dec][kept] vanish identically, so the
    # Schur correction B S^-1 C on the kept 15 modes is exactly zero.
    shift_zero = True
    for d_idx in (0, 5, 11):
        s_inv = cinv(q[d_idx][d_idx])
        for i in range(n):
            if i == d_idx:
                continue
            for j in range(n):
                if j == d_idx:
                    continue
                term = cmul(cmul(q[i][d_idx], s_inv), q[d_idx][j])
                if term != CZERO:
                    shift_zero = False
    check("C", "E1.b zero induced shift recomputed: in the exact taste "
               "eigenbasis Q = T^-1 (u_0 D + m) T is EXACTLY diagonal with "
               "entries m +- 2i u_0, so one taste-mode decimation is purely "
               "multiplicative (factor m +- 2i u_0, magnitude 2 u_0 at "
               "m = 0) and the induced coupling shift B S^-1 C on the kept "
               "15 modes is EXACTLY ZERO", diag_ok and factor_ok and shift_zero,
          "Gaussian-rational arithmetic; decimated modes {0, 5, 11}")

    check("A", "E1.c VERDICT recomputed: the frozen-link quadratic block "
               "algebra supplies u_0-degree +1 per mode and ZERO alpha_bare "
               "— it cannot supply the conversion target N = alpha_LM/"
               "(2 u_0) = 1/(8 pi u_0^2) = 0.0516519; route E1 ELIMINATED "
               "as a closure route (block01)",
          abs(1.0 / (8.0 * math.pi * U_0 ** 2) - 0.0516519) < 5e-8
          and abs(ALPHA_LM / (2 * U_0)
                  - 1.0 / (8.0 * math.pi * U_0 ** 2)) < 1e-15,
          f"N = {1.0 / (8.0 * math.pi * U_0 ** 2):.10f}")

    # ---- E2: bare relabeling u_0^16 -> alpha_LM^16 (honest status). ----
    rel_s = abs(ALPHA_LM ** 16 - ALPHA_BARE ** 16 * U_0 ** -16) \
        / ALPHA_LM ** 16
    displacement = U_0 ** 16 / ALPHA_LM ** 16
    txt_hs = read_doc("HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md")
    check("A", "E2 bare relabeling recomputed: identity (S) alpha_LM^16 = "
               "alpha_bare^16 x u_0^(-16) holds to < 1e-12 relative — the "
               "substitution u_0^16 -> alpha_LM^16 is BOOKKEEPING, not "
               "transport (honest-status B4: 'identity (S) is bookkeeping, "
               "not transport' on disk); the determinant's own u_0^16 is "
               "displaced from alpha_LM^16 by x 5.94e15 (no hierarchy); "
               "route E2 ELIMINATED",
          rel_s < 1e-12
          and abs(displacement / 5.94e15 - 1.0) < 1e-2
          and "identity (S) is bookkeeping, not transport" in txt_hs,
          f"identity (S) rel = {rel_s:.2e}, displacement = "
          f"{displacement:.3e}")

    # ---- E3: mean-field link feedback (block04). ----
    txt_mf = read_doc("HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_"
                      "PROBE_NOTE_2026-06-11.md")
    recorded = ["0.9857076265", "0.9856873008", "0.9534944113",
                "0.9534118085", "0.7892969743", "0.7867845593",
                "0.247288", "0.237144", "1.0000412422", "1.087382",
                "9.681", "10.526"]
    check("B", "E3.a block04's recorded saddle values on disk (consumed "
               "below as DECLARED inputs of its declared models M1/M2): "
               "u*(16)/u*(15) for U(1), SU(2), SU(3) dressed and SU(3) "
               "small-u branch, window endpoints and displacements all "
               "present in the note",
          all(tok in txt_mf for tok in recorded))

    saddles = {
        "U(1)": (0.9857076265, 0.9856873008),
        "SU(2)": (0.9534944113, 0.9534118085),
        "SU(3)": (0.7892969743, 0.7867845593),
        "SU(3) small-u": (0.247288, 0.237144),
    }
    r_values = {}
    for name, (u16, u15) in saddles.items():
        r_values[name] = (u15 / u16) ** -2
    r_min = min(r_values.values())
    r_max = max(r_values.values())
    disp_min = r_min / ALPHA_S
    e3 = (
        abs(r_min - 1.0000412422) < 1e-9
        and abs(r_max - 1.087382) < 5e-6
        and abs(disp_min - 9.681) < 5e-4
        and abs(r_values["SU(3) small-u"] / ALPHA_S - 10.526) < 5e-3
        and not (0.99 <= disp_min <= 1.01)        # 'supplied' trigger
        and not (0.5 <= disp_min <= 2.0)          # 'bounded obs' trigger
        and not (r_min <= ALPHA_S <= r_max)
    )
    check("A", "E3.b mean-field feedback recomputed from the declared "
               "inputs: R = (u*(15)/u*(16))^(-2) spans [1.0000412422, "
               "1.087382] over every variant/branch — the window does NOT "
               "contain alpha_s, minimum displacement R/alpha_s = 9.681 "
               "(max 10.526), and neither declared verdict trigger fires; "
               "route E3 REFUTED under all declared variants (block04)", e3,
          f"R in [{r_min:.10f}, {r_max:.6f}], min R/alpha_s = "
          f"{disp_min:.3f}")

    # ---- E4: per-step 1-loop perturbative beta (YT-P2 no-go). ----
    b3 = lambda n_t: Fraction(33 - 2 * n_t, 3)
    cum = abs(math.log(ALPHA_LM)) \
        * float(sum(b3(16 - k) for k in range(16))) / (8 * math.pi ** 2)
    inv_g2 = U_0                       # g_s^lat(M_Pl) = 1/sqrt(u_0)
    e4 = (
        b3(16) == Fraction(1, 3)
        and b3(17) == Fraction(-1, 3)
        and abs(cum - 2.594) < 5e-3
        and abs(inv_g2 - 0.878) < 5e-4
        and cum > inv_g2
    )
    check("A", "E4.a per-step 1-loop beta recomputed: b_3(16) = "
               "(33 - 32)/3 = 1/3 exactly (AF-marginal at the UV rung); "
               "b_3(17) = -1/3 < 0 (AF lost one step beyond the canonical "
               "staircase)", b3(16) == Fraction(1, 3)
          and b3(17) == Fraction(-1, 3),
          "exact Fraction arithmetic")
    check("A", "E4.b Landau crossing recomputed: cumulative 1-loop "
               "correction |ln alpha_LM| x sum b_3 / (8 pi^2) = 2.594 "
               "EXCEEDS the lattice UV anchor 1/g_s^2(M_Pl) = u_0 = 0.878 "
               "— the 1/g^2 trajectory crosses zero, the integration is "
               "ill-defined; route E4 ELIMINATED (YT-P2 no-go; blocking-RG "
               "/ strong-coupling routes explicitly NOT foreclosed by it)",
          e4, f"cumulative = {cum:.4f} > 1/g^2 = {inv_g2:.4f}")

    # ---- E5: coupling-independent-c dim-trans rewrite. ----
    c_eff = 16 * ALPHA_LM * math.log(1.0 / ALPHA_LM)
    rel_id = abs(ALPHA_LM ** 16 - math.exp(-c_eff / ALPHA_LM)) \
        / ALPHA_LM ** 16
    c_eff_quoted_input = 16 * 0.0907 * math.log(1.0 / 0.0907)
    check("A", "E5.a dim-trans rewrite recomputed: c_eff = 16 alpha_LM "
               "ln(1/alpha_LM) = 3.4824 at full B1 precision (the note's "
               "prose 3.4832 is reproduced exactly from its quoted 4-d.p. "
               "alpha_LM = 0.0907 — FLAGGED as a rounded-input prose "
               "artifact; its runner computes 3.482446... as here); "
               "identity alpha_LM^16 = exp(-c_eff/alpha_LM) < 1e-12 "
               "relative",
          abs(c_eff - 3.482446557878) < 1e-9
          and abs(c_eff_quoted_input - 3.4832) < 2e-4
          and rel_id < 1e-12,
          f"c_eff = {c_eff:.10f}, quoted-input c_eff = "
          f"{c_eff_quoted_input:.6f}, identity rel = {rel_id:.2e}")
    dc_dalpha = 16 * (math.log(1.0 / ALPHA_LM) - 1.0)
    c_at_perturbed = 16 * (1.1 * ALPHA_LM) * math.log(1.0 / (1.1 * ALPHA_LM))
    check("A", "E5.b coupling dependence recomputed: dc_eff/dalpha = "
               "16 (ln(1/alpha) - 1) = 22.41 != 0 and c_eff shifts under "
               "alpha -> 1.1 alpha — c_eff is a FUNCTION of the coupling "
               "whose hierarchy is being explained, unlike the canonical "
               "coupling-independent dim-trans constants (instanton "
               "8 pi^2 = 78.96, gaugino 8 pi^2/3 = 26.32); route E5 "
               "ELIMINATED as a closure route (notation rewrite only)",
          abs(dc_dalpha - 22.41) < 5e-2
          and abs(c_at_perturbed - c_eff) > 1e-2
          and abs(8 * math.pi ** 2 - 78.96) < 5e-3,
          f"dc/dalpha = {dc_dalpha:.4f}, c_eff(1.1 alpha) = "
          f"{c_at_perturbed:.4f}")


# ---------------------------------------------------------------------------
# Section C — the five eliminating runners re-verified as subprocesses.
# ---------------------------------------------------------------------------
RUNNERS = [
    ("C1", "frontier_hierarchy_delta0_blocking_single_mode_probe_"
           "2026_06_11.py",
     r"TOTAL:\s*PASS=21\s+FAIL=0", "block01 (E1): 21/0"),
    ("C2", "frontier_hierarchy_delta0_ratio_normalized_alpha_s_reduction_"
           "2026_06_11.py",
     r"TOTAL:\s*PASS=19\s+FAIL=0", "block02 (reduced target + E2 legs): "
                                   "19/0"),
    ("C3", "frontier_hierarchy_delta0_attachment_mean_field_feedback_probe_"
           "2026_06_11.py",
     r"TOTAL:\s*PASS=20\s+FAIL=0", "block04 (E3): 20/0"),
    ("C4", "frontier_yt_p2_taste_staircase_beta.py",
     r"RESULT:\s*12 PASS, 0 FAIL", "YT-P2 no-go (E4): 12/0"),
    ("C5", "frontier_hierarchy_alpha_lm_dim_trans_reframing_bounded_"
           "notation_equivalence.py",
     r"TOTAL:\s*PASS=5\s+FAIL=0", "dim-trans (E5): 5/0"),
]


def section_c():
    print("\n--- Section C [B]: eliminating runners re-verified "
          "(subprocess, exit code + note-stated totals) ---")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SCRIPTS)
    for tag, script, pattern, label in RUNNERS:
        path = SCRIPTS / script
        ok = False
        detail = "script missing"
        if path.exists():
            t0 = time.time()
            try:
                proc = subprocess.run(
                    [sys.executable, str(path)],
                    capture_output=True, text=True, timeout=120,
                    cwd=str(REPO_ROOT), env=env,
                )
                elapsed = time.time() - t0
                total_ok = re.search(pattern, proc.stdout) is not None
                ok = proc.returncode == 0 and total_ok
                detail = (f"exit = {proc.returncode}, total line "
                          f"{'matched' if total_ok else 'NOT matched'} "
                          f"[{pattern}], {elapsed:.1f}s")
            except subprocess.TimeoutExpired:
                detail = "TIMEOUT (120 s)"
        check("B", f"{tag} {label} — {script} still passes with its "
                   f"note-stated total", ok, detail)


# ---------------------------------------------------------------------------
# Section D — surviving routes S1-S3 (constraints recomputed; residuals).
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- Section D [A]/[B]: SURVIVING ROUTES S1-S3 — known "
          "constraints recomputed; routes printed as residuals ---")

    # D1: NJL leading-order constraint on S1 (and on S3's gauge-only form).
    g_eff = 1.0 / 6.0                       # Kawamoto-Smit LO, 1/(2 N_c)
    g_crit = U_0 ** 2 / 4.0                 # = sqrt(<P>)/4
    sigma_min_sq = 16.0 * g_eff - 4.0 * U_0 ** 2
    g_crit_note = 0.8776 ** 2 / 4.0         # at the NJL note's 4-d.p. u_0
    sigma_note_input = 16.0 * g_eff - 4.0 * 0.8776 ** 2
    d1 = (
        abs(g_eff - 1.0 / 6.0) < 1e-15
        and abs(g_crit - 0.192581) < 5e-7
        and g_eff < g_crit
        and abs(g_eff / g_crit - 0.866) < 1e-3
        and sigma_min_sq < 0.0
        and sigma_note_input < 0.0
        and abs(g_crit_note - 0.19255) < 5e-6
    )
    check("A", "D1 NJL leading-order constraint recomputed: G_eff = "
               "1/(2 N_c) = 1/6 = 0.16667 < G_critical = u_0^2/4 = "
               "0.192581 (0.19255 at the note's 4-d.p. u_0 = 0.8776), "
               "ratio 0.8654 -> SYMMETRIC phase at leading order; "
               "sigma_min^2 = 16 G_eff - 4 u_0^2 = -0.4146 < 0 (no "
               "broken-phase saddle).  FLAGGED deviation: the NJL note's "
               "prose quotes sigma_min^2 ~= -0.4561, ~10% from the "
               "recomputed -0.4141 at its own u_0 — the SIGN, hence the "
               "symmetric-phase verdict, is unchanged; recomputation "
               "governs here", d1,
          f"G_eff = {g_eff:.6f}, G_crit = {g_crit:.6f}, ratio = "
          f"{g_eff / g_crit:.4f}, sigma_min^2 = {sigma_min_sq:.4f} "
          f"(note-input {sigma_note_input:.4f})")

    txt_njl = read_doc("V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_"
                       "2026-05-10.md")
    check("B", "D2 NJL scope on disk: the symmetric-phase verdict is "
               "LEADING-order with a named O(1) sub-leading admission and "
               "an EW-sector escape — so S1 survives ONLY at beyond-leading "
               "order (sub-leading G_eff corrections flipping "
               "G_eff > G_critical) or with electroweak-sector structure "
               "added; S3's lattice-gauge-only version inherits the same "
               "constraint (no gap-equation spectrum exists at leading "
               "order)",
          "Kawamoto" in txt_njl
          and "symmetric phase" in txt_njl.lower()
          and "sub-leading" in txt_njl
          and "SU(2)_L" in txt_njl)

    txt_mf = read_doc("HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_"
                      "PROBE_NOTE_2026-06-11.md")
    check("B", "D3 route enumeration matches block04's remaining-routes "
               "list on disk: S1 = its route 5.1 (Kawamoto-Smit lineage "
               "one-link Haar at strong coupling), S2 = its route 5.2 "
               "(vacuum-polarization dressing of the Green-kernel "
               "readout), S3 = its route 5.3 (non-link transport rule) — "
               "the inventory adds NO new route and drops none",
          "Kawamoto-Smit lineage" in txt_mf
          and "Vacuum-polarization dressing" in txt_mf
          and "non-link-feedback transport rule" in txt_mf)

    residual(
        "S1 strong-coupling one-link Haar / Kawamoto-Smit lineage: a "
        "closing source must integrate links EXACTLY (not at a saddle) "
        "over the decimated-mode fermion bilinear source and land one "
        "factor alpha_s = 0.1033038 per taste threshold.  Already "
        "constrained: the landed NJL row puts the leading strong-coupling "
        "order in the SYMMETRIC phase (G_eff = 1/6 < G_critical = "
        "u_0^2/4 = 0.192581), so S1 survives only at beyond-leading order "
        "or with EW-sector structure added.  KILL criterion: an exact "
        "one-link computation whose per-decoupling factor is O(1)-"
        "displaced from alpha_s under every declared variant (the E3 "
        "pattern) eliminates it."
    )
    residual(
        "S2 readout-side dressing of the Green-kernel/static-source chain: "
        "a closing source must supply a per-taste-threshold vacuum-"
        "polarization dressing of the 1/(4 pi) SUPPLIER (the Plancherel-"
        "bridge kernel G(r) -> 1/(4 pi |r|) under V(r) = -C g^2 G(r)), "
        "NOT of the saddle u — delivering one factor alpha_s per "
        "threshold on the readout side.  Already constrained: the chain "
        "supplies the static VALUE only; no per-threshold rule exists.  "
        "KILL criterion: a computed kernel dressing that is per-threshold "
        "O(1) (or threshold-count-independent) eliminates it."
    )
    residual(
        "S3 direct non-link transport rule (threshold mass generation): a "
        "closing source must produce the rung ratio mu_{k+1}/mu_k = "
        "alpha_LM from a gap-equation mass spectrum at successive taste "
        "decouplings.  Already constrained: the NJL symmetric-phase "
        "result forecloses the lattice-gauge-only version at leading "
        "order (sigma_min^2 = 16 G_eff - 4 u_0^2 < 0: no spectrum to "
        "transport); an EW-sector-driven version is open.  KILL "
        "criterion: a gap-equation spectrum computed on the declared "
        "surface whose successive-threshold ratios are O(1)-displaced "
        "from alpha_LM eliminates it."
    )


# ---------------------------------------------------------------------------
# Section E — claim-shape ceiling.
# ---------------------------------------------------------------------------
def section_e():
    print("\n--- Section E [B]: CLAIM-SHAPE CEILING — what even a closed "
          "B4 could claim ---")
    txt_ng = read_doc("HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_"
                      "REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md")
    check("B", "E.1 regulator-dependence no-go on disk: the exponent-16 "
               "identification is regulator-DEPENDENT with the closure "
               "routes O1-O3 enumerated exhaustively — any B4 closure "
               "inherits a SUBSTRATE-IMPOSED exponent, never a "
               "regulator-independent one",
          "(O1)" in txt_ng and "(O2)" in txt_ng and "(O3)" in txt_ng
          and "regulator-dependent" in txt_ng
          and "substrate-imposed" in txt_ng)
    txt_sr = read_doc("SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    check("B", "E.2 scale-reference anti-promotion policy on disk: the "
               "single dimensionful reference a^{-1} = M_Pl carries zero "
               "dimensionless content and a row 'should not become "
               "retained_bounded merely for using a ruler' — so the lane's "
               "honest ceiling, even after a B4 closure, is "
               "retained_bounded over {axioms + approved primitives + "
               "declared conventions}",
          "merely for using a ruler" in txt_sr
          and "retained_bounded" in txt_sr
          and "exactly one dimensionful reference" in txt_sr)


# ---------------------------------------------------------------------------
# Section F — non-modification + terminal fence.
# ---------------------------------------------------------------------------
def section_f():
    print("\n--- Section F [B]/[D]: non-modification + terminal class-D "
          "fence ---")
    txt_gate = read_doc("HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_"
                        "NOTE_2026-05-30.md")
    check("B", "F1 the DELTA0 gate is UNCHANGED on disk: claim type "
               "open_gate, the 2026-06-11 sharpening record present, gate "
               "recorded 'still open' — this synthesis closes nothing and "
               "changes no gate status",
          "open_gate" in txt_gate
          and "Sharpening record" in txt_gate
          and "still open" in txt_gate)
    ok_parent = False
    detail = "parent note missing"
    if PARENT_NOTE.exists():
        txt_p = PARENT_NOTE.read_text(encoding="utf-8")
        required = [
            "Status authority", "independent audit lane",
            "source-note proposal", "bounded_theorem",
            "does NOT claim", "changes no gate status",
            "refine routes without modifying the inventory",
        ]
        missing = [t for t in required if t not in txt_p]
        ok_parent = not missing
        detail = f"missing = {missing}"
    check("B", "F2 parent synthesis note carries the required "
               "disclaimers: independent-audit status authority, "
               "source-note proposal, bounded_theorem scope fence, "
               "what-this-note-does-NOT-claim, non-modification + "
               "downstream-refinement rule", ok_parent, detail)
    pdg_vev = "246" + "." + "22"
    src = Path(__file__).read_text(encoding="utf-8")
    check("D", "F3 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          pdg_vev not in src)


# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_route_inventory_synthesis_"
          "2026_06_11.py")
    print(" Block07 of the DELTA0 blocking campaign: the route-inventory")
    print(" synthesis — reduced target, five eliminated routes (E1-E5,")
    print(" key numbers recomputed, eliminating runners re-invoked), three")
    print(" surviving routes (S1-S3, declared-open with kill criteria),")
    print(" claim-shape ceiling.  Enumeration, not closure: DELTA0 stays")
    print(" open and no gate status changes.")
    print(" Parent note: docs/HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_")
    print("              SYNTHESIS_NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    section_b()
    section_c()
    section_d()
    section_e()
    section_f()

    print("\n" + "=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded): over the declared ratio")
    print("   normalization B4 closure is exactly one landed transport rule")
    print("   away — one factor alpha_s = alpha_bare/u_0^2 = 0.1033038 per")
    print("   taste decoupling (u_0^16 alpha_s^16 = alpha_LM^16 exactly) —")
    print("   and five routes to that rule are ELIMINATED on their cited")
    print("   surfaces (E1 frozen-link block algebra, E2 bare relabeling,")
    print("   E3 mean-field link feedback, E4 per-step 1-loop beta, E5")
    print("   coupling-independent-c dim-trans rewrite), with all five")
    print("   eliminating runners re-verified.  NOT established: any")
    print("   surviving route (S1 strong-coupling one-link Haar — leading")
    print("   order already symmetric-phase-constrained by the NJL row; S2")
    print("   Green-kernel readout dressing; S3 direct non-link transport)")
    print("   — all three are declared-open residuals with kill criteria.")
    print("   Ceiling: any closure is retained_bounded over {axioms +")
    print("   approved primitives + declared conventions} with a substrate-")
    print("   imposed exponent (O1-O3), never regulator-independent.")
    print("   DELTA0 stays open; this synthesis fixes the decomposition and")
    print("   closes nothing.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
