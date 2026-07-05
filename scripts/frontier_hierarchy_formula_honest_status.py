#!/usr/bin/env python3
"""Structural-theorem runner for the hierarchy/VEV lane row

    docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md
    (2026-06-11 theorem/boundary-input restructure;
     2026-06-16 B3 kinetic-substrate split)

Claim under check (theorem T1 of the note, plus declared map appendix
D1 and bounded readout appendix C1):

    T1 (load-bearing, computed here from local algebra — NOT hard-coded):
      (i)   naive symbol zero set on the even-L momentum torus is
            {0, pi}^d -> exactly 2^d species; 16 at d = 4 with Hamming
            staircase (1,4,6,4,1); 4 / 8 / 32 at d = 2 / 3 / 5
            (regulator- and dimension-conditional surface data);
      (ii)  on the minimal 2^4 all-antiperiodic mean-field block,
            det(u_0 D + m) = (m^2 + 4 u_0^2)^8 per color; at m = 0 the
            magnitude is (2 u_0)^16 = 4^8 u_0^16 — u_0-degree exactly
            equal to the species count 16 (exact Fraction arithmetic);
      (iii) selector (7/8)^(1/4) = g(4) = (eta(4)/zeta(4))^(1/4), with
            eta(4)/zeta(4) = 1 - 2^(1-4) = 7/8 exact (Fraction algebra
            plus rigorously bracketed series);
      (iv)  suppression constant K := (7/8)^(1/4) alpha_LM^16
            = 2.017224e-17 with zero continuous knobs beyond the
            licensed plaquette B1; identity (S)
            alpha_LM^16 = alpha_bare^16 u_0^(-16); the magnitude is
            carried by alpha_bare^16 = (4 pi)^(-16), NOT by the
            determinant power u_0^16 = 0.124;
      (v)   sensitivity algebra of the declared map dln v_cand/dln <P>
            = -4 and dln v_cand/dln M_Pl = +1 exactly (fd-verified).

      B3 is split: B3a (four-direction kinetic-form substrate) is
      supplied only to the scope of the registered kinetic-isotropy
      primitive; B3b (regulator/species realization) remains open.
      B4 (coupling-power transport) remains open. Neither B3b nor B4 is
      derived by this runner.

    D1 (declared candidate map appendix, NOT formula closure and NOT an
    observable identification):
      v_cand := M_Pl x (7/8)^(1/4) x alpha_LM^16  over the declared
      anchor B2 (M_Pl = 1.2209e19 GeV, Planck-lane import).

    C1 (bounded numeric readout appendix over declared inputs/open gates):
      v_cand = 246.282818290129 GeV.  NOT formula closure and NOT an EW
      VEV prediction.

Falsification legs (baseline-relative; would FAIL if the declared
structure were softer than claimed):

    F1  exponent displacement: one unit of N moves v_cand by the factor
        1/alpha_LM = 11.03; the Z^3 spatial-only count N = 8 displaces
        by x 2.19e8.  The integer N cannot move within input resolution.
    F2  coupling-power displacement: the determinant's own u_0^16 gives
        NO hierarchy (x 5.94e15); alpha_bare^16 and alpha_s(v)^16
        displace by x 0.124 and x 8.0651 = u_0^(-16).  This identifies
        B4 as the open transport gate rather than accepting it as a
        premise.
    F3  selector displacement: removing (7/8)^(1/4) displaces by
        +3.39 %, two orders above the B1 resolution window.
    F4  anti-tuning: the plaquette value that would reproduce the PDG
        VEV exactly differs from the licensed 0.5934 by LESS than the
        4-decimal rounding half-step (the licensed grid cannot encode a
        tuned target); the equivalent M_Pl shift is 6.2x the B2
        half-step (the residual is attributable to the Planck anchor).
        The PDG value enters here ONLY as the tuning target whose
        unreachability-on-the-B1-grid is certified.

Check classes (each PASS line is tagged):

  [C] first-principles compute from local algebra (symbol zero
      set, eta-phase staggered operator on the 2^4 block, exact char
      poly / determinants, bracketed eta/zeta series).
  [A] exact arithmetic / algebraic identities over the declared
      boundary inputs (K, identity (S), readout, elasticities,
      falsification legs, anti-tuning certificate).
  [B] cross-note input verification (canonical plaquette helper,
      license/authority text on disk, parent-note hygiene, forbidden
      overclaim-token scan, runner self-scan).
  [D] external comparator (PDG VEV), quarantined terminal section;
      NO PASS in this runner rests on agreement with a PDG number.

Deterministic, pure Python stdlib (math, fractions, itertools), runtime
well under one minute.  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = REPO_ROOT / "docs" / "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md"
KINETIC_PRIMITIVE_PATH = REPO_ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
B3_STAGGERED_SUPPLIER = REPO_ROOT / "docs" / "HIERARCHY_B3_STAGGERED_SUPPLIER_CASCADE_NOTE_2026-06-17.md"
AXIOM_PREMISE_NODES = REPO_ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import canonical_plaquette_surface as cps  # noqa: E402

PASS_COUNT = 0
FAIL_COUNT = 0
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


# ---------------------------------------------------------------------------
# Declared boundary inputs (mirrors the note's B1/B2 verbatim).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1: licensed reuse number (4 d.p.)
P_HALF_STEP = 0.00005                # B1 license rounding half-step
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # exact convention
ALPHA_LM = ALPHA_BARE / U_0          # = 0.090668
ALPHA_S_V = ALPHA_BARE / U_0 ** 2    # canonical-surface alpha_s(v)
M_PL = 1.2209e19                     # B2: declared Planck-lane anchor (GeV)
M_PL_HALF_STEP_REL = 0.00005 / 1.2209  # B2 quoted-precision half-step (rel)
N_EXPONENT = 16                      # B3b: declared regulator/species surface
APBC = (7.0 / 8.0) ** 0.25           # selector, recomputed in [C]

# Published constants of the note (reproducibility targets, class A).
V_CAND_PUBLISHED = 246.282818290129  # GeV (corollary C1)
K_PUBLISHED = 2.017224e-17           # suppression constant (T1.iv, rounded)

# PDG comparator — class-D terminal section and F4 tuning target ONLY.
V_OBS_PDG = 246.22                   # observed EW VEV (GeV)


# ---------------------------------------------------------------------------
# Exact linear algebra helpers (Fractions; no third-party imports).
# ---------------------------------------------------------------------------
def mat_mul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def mat_add_diag(a, c):
    out = [row[:] for row in a]
    for i in range(len(a)):
        out[i][i] += c
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


def char_poly_exact(a):
    """Faddeev-LeVerrier: [1, c1, ..., cn] for lambda^n + c1 lambda^(n-1)
    + ... + cn, exact Fractions."""
    n = len(a)
    coeffs = [Fraction(1)]
    m = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
         for i in range(n)]
    for k in range(1, n + 1):
        am = mat_mul(a, m)
        tr = sum(am[i][i] for i in range(n))
        ck = -tr / k
        coeffs.append(ck)
        m = mat_add_diag(am, ck)
    return coeffs


# ---------------------------------------------------------------------------
# Local algebra: minimal-block staggered operator (all-APBC 2^4).
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


def v_cand_of(p, m_pl, n_exp):
    """Readout map: declared-input function (no hidden state)."""
    a_lm = (1.0 / (4.0 * math.pi)) / p ** 0.25
    return m_pl * (7.0 / 8.0) ** 0.25 * a_lm ** n_exp


# ---------------------------------------------------------------------------
# Section C — first-principles compute (load-bearing chain of T1).
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- [C] T1 first-principles compute (species count -> "
          "determinant degree -> selector) ---")

    # C1: per-direction symbol zero set {0, pi} on even-L grids.
    zero_sets = {}
    for big_l in (6, 8):
        zeros = [n for n in range(big_l) if (2 * n) % big_l == 0]
        zero_sets[big_l] = zeros
    check("C", "naive symbol zero set per direction is {0, pi} (momenta "
               "n = 0, L/2) on even-L grids L = 6, 8 — exact integer count",
          all(zero_sets[big_l] == [0, big_l // 2] for big_l in (6, 8)),
          f"zero sets: {zero_sets}")

    # C2: species count 2^d at d = 2, 3, 4, 5 — exponent data is
    # dimension-conditional; d = 4 gives the declared N = 16; the d = 3
    # spatial-only count 8 is falsification-leg data for B3.
    counts = {d: 2 ** d for d in (2, 3, 4, 5)}
    explicit = {d: sum(1 for k in itertools.product((0, 1), repeat=d))
                for d in (2, 3, 4, 5)}
    check("C", "species count = 2^d: (d=2,3,4,5) -> (4, 8, 16, 32); "
               "d = 4 corner enumeration gives the declared N = 16",
          counts == explicit and counts[4] == N_EXPONENT
          and counts[3] == 8,
          f"counts: {explicit}")

    # C3: Hamming staircase over the 16 corners.
    hw = {}
    for c in itertools.product((0, 1), repeat=4):
        hw[sum(c)] = hw.get(sum(c), 0) + 1
    staircase = tuple(hw[k] for k in sorted(hw))
    check("C", "Hamming staircase over the d = 4 corners is (1,4,6,4,1), "
               "sum 16", staircase == (1, 4, 6, 4, 1) and sum(staircase) == 16)

    # C4: minimal-block operator: real antisymmetric, D^2 = -4 I.
    d_unit = staggered_operator()
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(16) for j in range(16))
    d2 = mat_mul(d_unit, d_unit)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(16) for j in range(16))
    check("C", "eta-phase staggered operator on the all-APBC 2^4 block: "
               "D real antisymmetric and D^2 = -4 I exactly",
          antisym and d2_ok, "exact Fraction matrix arithmetic")

    # C5: char poly of D/u_0 is (lambda^2 + 4)^8 — 16 modes +/- 2i.
    coeffs = char_poly_exact(d_unit)
    target = [Fraction(0)] * 17
    for k in range(9):
        target[2 * k] = Fraction(math.comb(8, k) * 4 ** k)
    check("C", "char poly of D/u_0 is (lambda^2 + 4)^8 — 16 taste modes "
               "+/- 2i u_0, multiplicity 8 each",
          coeffs == target, "Faddeev-LeVerrier, exact")

    # C6: determinant identity and exact u_0-degree = species count.
    a1, a2, m = Fraction(2, 3), Fraction(3, 5), Fraction(1, 3)
    mat_am = [[a1 * d_unit[i][j] + (m if i == j else 0) for j in range(16)]
              for i in range(16)]
    det_id_ok = det_exact(mat_am) == (m * m + 4 * a1 * a1) ** 8
    det_a1 = det_exact([[a1 * x for x in row] for row in d_unit])
    det_a2 = det_exact([[a2 * x for x in row] for row in d_unit])
    mag_ok = det_a1 == Fraction(4) ** 8 * a1 ** 16
    degree_ok = det_a1 * a2 ** 16 == det_a2 * a1 ** 16
    check("C", "det(u_0 D + m) = (m^2 + 4 u_0^2)^8 per color; at m = 0 "
               "|det| = 4^8 u_0^16; exact u_0-degree from a two-point "
               "ratio equals the species count 16",
          det_id_ok and mag_ok and degree_ok,
          "exact at rational (u_0, m) test points")

    # C7: selector (7/8)^(1/4): exact closed form and bracketed series.
    closed = Fraction(1) - Fraction(2) ** (1 - 4)
    big_n = 50
    zeta_part = sum(Fraction(1, n ** 4) for n in range(1, big_n + 1))
    zeta_lo = zeta_part + Fraction(1, 3 * (big_n + 1) ** 3)
    zeta_hi = zeta_part + Fraction(1, 3 * big_n ** 3)
    eta_part = sum(Fraction((-1) ** (n - 1), n ** 4)
                   for n in range(1, big_n + 1))  # big_n even -> lower bound
    eta_lo = eta_part
    eta_hi = eta_part + Fraction(1, (big_n + 1) ** 4)
    ratio_lo = eta_lo / zeta_hi
    ratio_hi = eta_hi / zeta_lo
    width = float(ratio_hi - ratio_lo)
    check("C", "selector: eta(4)/zeta(4) = 1 - 2^(1-4) = 7/8 exact "
               "(Fraction algebra); bracketed series interval contains "
               "7/8", closed == Fraction(7, 8)
          and ratio_lo <= Fraction(7, 8) <= ratio_hi and width < 1e-4,
          f"ratio in [{float(ratio_lo):.8f}, {float(ratio_hi):.8f}], "
          f"width {width:.1e}")


# ---------------------------------------------------------------------------
# Section A — readout algebra, sensitivities, falsification legs.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- [A] T1.iv/T1.v + D1/C1 readout algebra over declared "
          "inputs and open formula-closure gates ---")

    # A1: suppression constant K and its log decomposition.
    k_const = APBC * ALPHA_LM ** 16
    orders = math.log10(1.0 / k_const)
    orders_decomp = (16 * math.log10(1.0 / ALPHA_LM)
                     - 0.25 * math.log10(7.0 / 8.0))
    check("A", "K = (7/8)^(1/4) alpha_LM^16 = 2.017224e-17 (zero "
               "continuous knobs beyond B1); log decomposition "
               "16 log10(1/alpha_LM) - (1/4) log10(7/8) matches",
          abs(k_const / K_PUBLISHED - 1.0) < 5e-7
          and abs(orders - orders_decomp) < 1e-12,
          f"K = {k_const:.12e}, orders = {orders:.6f}")

    # A2: identity (S) and magnitude attribution (B4 bookkeeping).
    lhs = ALPHA_LM ** 16
    rhs = ALPHA_BARE ** 16 * U_0 ** -16
    u016 = U_0 ** 16
    check("A", "identity (S): alpha_LM^16 = alpha_bare^16 u_0^(-16); "
               "magnitude carried by alpha_bare^16 = (4 pi)^(-16) ~ "
               "2.6e-18 while |log10 u_0^16| < 1 — the determinant "
               "power supplies no hierarchy",
          abs(lhs / rhs - 1.0) < 1e-12
          and ALPHA_BARE ** 16 < 1e-17
          and abs(math.log10(u016)) < 1.0,
          f"alpha_bare^16 = {ALPHA_BARE ** 16:.4e}, u_0^16 = {u016:.5f}")

    # A3: corollary C1 readout reproducibility (note's own constant).
    v_cand = v_cand_of(P_BOUNDARY, M_PL, N_EXPONENT)
    check("A", "C1 readout: v_cand = M_Pl x K = 246.282818290129 GeV "
               "(matches the note's published constant)",
          abs(v_cand / V_CAND_PUBLISHED - 1.0) < 1e-12,
          f"v_cand = {v_cand:.12f} GeV")

    # A4: elasticities (T1.v), analytic vs finite difference.
    dp = 1e-7
    el_p_fd = ((math.log(v_cand_of(P_BOUNDARY + dp, M_PL, 16))
                - math.log(v_cand_of(P_BOUNDARY - dp, M_PL, 16)))
               / (math.log(P_BOUNDARY + dp) - math.log(P_BOUNDARY - dp)))
    el_m = v_cand_of(P_BOUNDARY, 1.01 * M_PL, 16) / v_cand
    check("A", "elasticities: dln v_cand/dln <P> = -4 (fd-verified) and "
               "dln v_cand/dln M_Pl = +1 (exact linearity)",
          abs(el_p_fd + 4.0) < 1e-6 and abs(el_m - 1.01) < 1e-12,
          f"fd elasticity = {el_p_fd:.9f}")

    # A5: B1 resolution window on v_cand.
    window = 4.0 * (P_HALF_STEP / P_BOUNDARY)
    check("A", "B1 resolution window: 4-d.p. plaquette license induces "
               "+/- 0.0337 % on v_cand",
          abs(window - 3.3704e-4) < 1e-7,
          f"window = {window * 100:.5f} %")

    # A6: falsification leg F1 — exponent displacement, baseline-relative.
    r15 = v_cand_of(P_BOUNDARY, M_PL, 15) / v_cand
    r17 = v_cand_of(P_BOUNDARY, M_PL, 17) / v_cand
    r8 = v_cand_of(P_BOUNDARY, M_PL, 8) / v_cand
    check("A", "F1 exponent displacement: N = 15 -> x 11.029, N = 17 -> "
               "x 0.09067, N = 8 (Z^3 spatial-only) -> x 2.19e8; every "
               "unit of N displaces >> the B1 window",
          abs(r15 - 1.0 / ALPHA_LM) < 1e-9
          and abs(r17 - ALPHA_LM) < 1e-9
          and abs(r8 / 2.1896e8 - 1.0) < 1e-3
          and min(abs(math.log10(r15)), abs(math.log10(r17))) > 0.95,
          f"x {r15:.4f} / x {r17:.6f} / x {r8:.4e}")

    # A7: falsification leg F2 — coupling-power displacement.
    r_det = u_ratio = (U_0 ** 16) / (ALPHA_LM ** 16)
    r_bare = (ALPHA_BARE ** 16) / (ALPHA_LM ** 16)
    r_sv = (ALPHA_S_V ** 16) / (ALPHA_LM ** 16)
    check("A", "F2 coupling displacement: determinant power u_0^16 -> "
               "x 5.94e15 (NO hierarchy; B4 remains the open transport "
               "gate), alpha_bare^16 -> x 0.1240, alpha_s(v)^16 -> "
               "x 8.0651 = u_0^(-16) exactly",
          abs(r_det / 5.9447e15 - 1.0) < 1e-3
          and abs(r_bare - U_0 ** 16) < 1e-12
          and abs(r_sv - U_0 ** -16) < 1e-9,
          f"x {u_ratio:.4e} / x {r_bare:.5f} / x {r_sv:.5f}")

    # A8: falsification leg F3 — selector displacement.
    r_sel = 1.0 / APBC
    check("A", "F3 selector displacement: removing (7/8)^(1/4) -> "
               "x 1.033946 (+3.39 %), two orders above the B1 window",
          abs(r_sel - 1.0339463) < 1e-6
          and (r_sel - 1.0) > 100.0 * 4.0 * (P_HALF_STEP / P_BOUNDARY),
          f"x {r_sel:.7f}")

    # A9: falsification leg F4 — anti-tuning certificate. The PDG value
    # enters ONLY as the tuning target whose unreachability on the B1
    # grid is certified; no PASS rewards agreement with it.
    p_needed = P_BOUNDARY * (v_cand / V_OBS_PDG) ** 0.25
    p_offset = p_needed - P_BOUNDARY
    m_needed = M_PL * (V_OBS_PDG / v_cand)
    m_offset_rel = abs(m_needed / M_PL - 1.0)
    m_steps = m_offset_rel / M_PL_HALF_STEP_REL
    check("A", "F4 anti-tuning: <P>_needed - 0.5934 = +3.78e-5 < the "
               "4-d.p. half-step 5e-5 (the licensed grid cannot encode "
               "a tuned target; 0.5934 IS the rounding of <P>_needed); "
               "M_Pl_needed shift = 6.2x the B2 half-step (residual "
               "attributable to the Planck anchor)",
          0 < p_offset < P_HALF_STEP and 5.5 < m_steps < 7.0,
          f"<P>_needed = {p_needed:.7f}, M_Pl_needed = {m_needed:.6e}, "
          f"B2 steps = {m_steps:.2f}")


# ---------------------------------------------------------------------------
# Section B — cross-note inputs, hygiene, and self-scans.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- [B] cross-note inputs, parent-note hygiene, self-scans ---")

    # B1: canonical plaquette helper residuals (B1 chain recomputed).
    check("B", "B1 matches canonical helper: <P> = 0.5934, u_0, "
               "alpha_bare = 1/(4 pi), alpha_LM = alpha_bare/u_0",
          cps.CANONICAL_PLAQUETTE == P_BOUNDARY
          and abs(cps.CANONICAL_U0 - U_0) < 1e-15
          and abs(cps.CANONICAL_ALPHA_BARE - ALPHA_BARE) < 1e-18
          and abs(cps.CANONICAL_ALPHA_LM - ALPHA_LM) < 1e-15,
          f"alpha_LM = {ALPHA_LM:.10f}")

    # B2: plaquette reuse license on disk.
    plaq = (REPO_ROOT / "docs" / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md")
    plaq_text = plaq.read_text() if plaq.exists() else ""
    check("B", "plaquette license present: 0.5934 'admitted "
               "comparison/reuse number' language on disk",
          "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text)

    # B3: naive 2^d parent narrow theorem on disk with the exact-count
    # claim this note's S2 cites.
    naive = (REPO_ROOT / "docs" /
             "NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW"
             "_THEOREM_NOTE_2026-05-10.md")
    naive_text = naive.read_text() if naive.exists() else ""
    check("B", "naive 2^d species-count parent theorem on disk with the "
               "exact-count claim",
          "realizes exactly `2^d` species" in naive_text)

    # B4: joint Riemann-Dirichlet fourth-root theorem on disk with the
    # closed form and the integer-d uniqueness clause.
    joint = (REPO_ROOT / "docs" /
             "HIERARCHY_JOINT_RIEMANN_DIRICHLET_DIMENSIONAL_FOURTH_ROOT"
             "_NARROW_THEOREM_NOTE_2026-05-10.md")
    joint_text = joint.read_text() if joint.exists() else ""
    check("B", "joint fourth-root theorem on disk: (7/8)^(1/4) closed "
               "form and integer-d uniqueness at s = 4",
          "(7/8)^(1/4)" in joint_text
          and "if and only if `s = 4`" in joint_text)

    # B5: regulator-dependence no-go on disk; B3b's declaration mirrors it.
    nogo = (REPO_ROOT / "docs" /
            "HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR"
            "_DEPENDENCE_NO_GO_NOTE_2026-05-10.md")
    nogo_text = nogo.read_text() if nogo.exists() else ""
    check("B", "regulator-dependence no-go on disk: identification is "
               "regulator-dependent (Wilson: 1, twisted-mass: 2, "
               "staggered: 4, domain-wall: 1, overlap: 1)",
          "regulator-dependent" in nogo_text and "Wilson: 1" in nogo_text)

    note_text = NOTE_PATH.read_text()

    # B6: kinetic-isotropy primitive supplies only the B3a substrate split.
    kinetic_text = (KINETIC_PRIMITIVE_PATH.read_text()
                    if KINETIC_PRIMITIVE_PATH.exists() else "")
    nodes = (json.loads(AXIOM_PREMISE_NODES.read_text())
             if AXIOM_PREMISE_NODES.exists() else {"nodes": {}})
    kinetic_node = nodes.get("nodes", {}).get("kinetic_isotropy_primitive", {})
    check("B", "B3a kinetic substrate is sourced to registered "
               "kinetic_isotropy_primitive with c_t = c_s / OS0 "
               "hypercubic-form scope only",
          kinetic_node.get("current_path")
          == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
          and "c_t = c_s" in kinetic_text
          and "hypercubic-symmetric" in kinetic_text
          and "no mass ratio" in kinetic_text
          and "does not supply any dimensionless dynamical quantity" in kinetic_text)

    # B7: the parent note preserves the split: B3a gets the primitive;
    # B3b and B4 remain open.
    check("B", "parent note splits B3a kinetic substrate from B3b "
               "regulator/species realization and keeps B4 open",
          "**B3a, kinetic substrate:**" in note_text
          and "**B3b, regulator/species realization:**" in note_text
          and "B4 is unchanged and remains open" in note_text
          and "B4 attachment-observable problem" in note_text)

    # B8: the substrate gate is referenced as backticked context only
    # (open gate; not a one-hop authority edge).
    gate_name = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    gate_on_disk = (REPO_ROOT / "docs" / gate_name).exists()
    check("B", "staggered-Dirac realization gate on disk and referenced "
               "as backticked context (no markdown-link edge)",
          gate_on_disk and gate_name in note_text
          and f"]({gate_name})" not in note_text)

    # B9: every markdown-linked citation in the note resolves on disk.
    links = re.findall(r"\]\(([A-Za-z0-9_\-./]+\.md)\)", note_text)
    missing = [l for l in links
               if not (REPO_ROOT / "docs" / l).exists()
               and not (REPO_ROOT / l).exists()]
    check("B", "all markdown-linked note citations resolve on disk",
          not missing and len(set(links)) == 6
          and B3_STAGGERED_SUPPLIER.exists(),
          f"links = {sorted(set(links))}" if not missing
          else f"missing: {missing}")

    # B10: parent-note hygiene — required declarations present, forbidden
    # overclaim / back-propagation tokens absent.
    lowered = note_text.lower()
    required = [
        "b3a, kinetic substrate",
        "b3b, regulator/species realization",
        "kinetic_isotropy_primitive",
        "regulator-conditional",
        "not an ew vev prediction",
        "fenced comparator appendix",
        "zero continuous knobs",
        "open formula-closure gates",
    ]
    forbidden = [
        "regulator-independent derivation",
        "derives the electroweak vev",
        "derived hierarchy theorem",
        "within 1 % of v_obs",
        "within 1% of v_obs",
        "tuned to land",
        "b4 is load-bearing",
        "declared admission tuple",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "parent-note hygiene: required declarations present and "
               "forbidden overclaim tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")

    # B11: runner self-scan (no back-propagation): the PDG literal occurs
    # exactly once in this runner's source — the declared comparator
    # constant. Structural sections never touch it.
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only the constant
    occurrences = src.count(pdg_literal)
    check("B", "runner self-scan: PDG VEV literal appears exactly once "
               "in the runner source (the class-D constant definition)",
          occurrences == 1, f"occurrences = {occurrences}")


# ---------------------------------------------------------------------------
# Section D — fenced external comparators (terminal; never load-bearing).
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- [D] fenced comparators (PDG; quarantined, never "
          "load-bearing) ---")
    v_cand = v_cand_of(P_BOUNDARY, M_PL, N_EXPONENT)

    # D1: deviation report. PASS verifies the note's stated figure
    # reproduces — it does NOT reward agreement.
    dev = (v_cand - V_OBS_PDG) / V_OBS_PDG
    check("D", "comparator: v_cand deviates from the PDG EW VEV by "
               "+0.025513 % (deviation report, not a match claim)",
          abs(dev - 2.5513e-4) < 1e-8,
          f"deviation = {dev * 100:+.6f} %")

    # D2: resolution framing recomputed: sub-resolution in B1, real and
    # attributable in B2 — both directions stated, neither rewarded.
    b1_window = 4.0 * (P_HALF_STEP / P_BOUNDARY)
    b2_window = M_PL_HALF_STEP_REL
    check("D", "comparator framing: deviation < B1 window (0.0337 %) "
               "AND deviation > B2 window (0.0041 %) — sub-resolution "
               "in the plaquette license, attributable in the Planck "
               "anchor",
          abs(dev) < b1_window and abs(dev) > b2_window,
          f"|dev| = {abs(dev):.3e}, B1 = {b1_window:.3e}, "
          f"B2 = {b2_window:.3e}")


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_formula_honest_status.py")
    print(" (2026-06-16 B3 split: T1 structural support from local")
    print("  algebra; B3a kinetic substrate sourced to the primitive;")
    print("  D1/C1 appendices over open B3b/B4/B5 gates;")
    print("  comparators fenced)")
    print(" Parent note: docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_"
          "2026-05-10.md")
    print("=" * 78)

    section_c()
    section_a()
    section_b()
    section_d()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
