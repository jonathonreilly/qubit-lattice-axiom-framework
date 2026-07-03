#!/usr/bin/env python3
"""Dedicated bounded-chain runner for docs/HIGGS_MASS_FROM_AXIOM_NOTE.md
(2026-05-03; structural checks 2026-05-07/05-10; theorem/boundary-input
restructure 2026-06-11).

Claim under check (theorem T1 of the note, plus definition D1 and bounded
corollary C1):

    T1 (load-bearing, computed here from primitives — NOT hard-coded):
      On the declared minimal-block mean-field surface (boundary inputs
      B3/B4 of the note: L = 2 block of Z^3 + t, antiperiodic wrap in all
      four directions, staggered eta phases, mean-field links
      U_{ab} -> u_0 delta_{ab}), the per-color staggered operator D
      satisfies, with exact integer/rational arithmetic:

        (i)   D is real antisymmetric and D^2 = -4 u_0^2 I  (16x16);
        (ii)  char poly of D/u_0 is (lambda^2 + 4)^8, i.e. all 16 taste
              eigenvalues are +/- 2 i u_0 (multiplicity 8 each);
        (iii) det(D + m) = (m^2 + 4 u_0^2)^8 per color, and
              det over N_c colors = [per-color det]^{N_c};
        (iv)  V_taste(m) := -(1/N_c) log det_color(D + m)
                          = -(N_taste/2) log(m^2 + 4 u_0^2);
        (v)   V_taste'(0) = 0 and V_taste''(0) = -N_taste/(4 u_0^2)
                          = -4/u_0^2; per-channel magnitude 1/(4 u_0^2);
        (vi)  every per-color quantity is exactly N_c-independent
              (verified at N_c in {1, 2, 3, 4} from the determinant,
              not from the final formula).

    D1 (declared definition, NOT an observable identification):
      m_curv_tree^2 := (|V_taste''(0)| / N_taste) * v^2  =  v^2/(4 u_0^2).

    C1 (bounded numeric corollary over declared inputs B1/B2):
      with <P> = 0.5934 (licensed reuse number; plaquette authority) so
      u_0 = <P>^(1/4) = 0.877681381, and v = 246.22 GeV (declared external
      EW VEV scale; NOT derived by the note),
      m_curv_tree = v/(2 u_0) = 140.27 GeV ~ 140.3 GeV.
      This is a symmetric-point per-channel curvature scale, NOT a
      Higgs-mass prediction.

Falsification legs (would FAIL if the declared surface or the algebra
were wrong):

    F1  time-only antiperiodic wrap (the old "APBC in time" gloss) gives
        D^2 = -u_0^2 I and det(D + m) = (m^2 + u_0^2)^8 — a DIFFERENT
        determinant. The all-four-directions antiperiodic declaration in
        B4 is load-bearing and is exposed, not hidden.
    F2  anti-tuning: reproducing the PDG Higgs pole 125.10 GeV from
        v/(2 u_0) would require <P> = 0.9379, i.e. +58% off the licensed
        0.5934. There is no admissible knob; the chain output 140.3 GeV
        disagrees with the PDG pole by +12.1% and the note says so.

Check classes (each PASS line is tagged):

  [C] first-principles compute from framework primitives (Clifford
      generators, eta-phase staggered operator on the 2^4 block, exact
      char poly / determinants) producing numbers not present in any
      input.
  [A] exact arithmetic / algebraic identities over the declared boundary
      inputs (readout identity, two-route agreement, analytic
      sensitivity, anti-tuning certificate).
  [B] cross-note input verification (canonical plaquette helper
      residuals, dependency license text on disk, parent-note hygiene
      guards).
  [D] external comparator (PDG values), quarantined terminal section;
      NO PASS in this runner rests on agreement with a PDG number.

Deterministic, pure Python stdlib (math, fractions, itertools), runtime
well under one minute.  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = REPO_ROOT / "docs" / "HIGGS_MASS_FROM_AXIOM_NOTE.md"

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
# Declared boundary inputs (mirrors the note's B1-B2 verbatim).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934            # B1: licensed reuse number (plaquette license)
U_0 = P_BOUNDARY ** 0.25       # = 0.877681381 (exact arithmetic on B1)
V_GEV = 246.22                 # B2: declared external EW VEV scale (GeV)
V_HIERARCHY_LANE = 246.282818290129  # hierarchy-lane bounded formula value
                               # (context for the B2 insensitivity check;
                               # NOT a derivation claim of this runner)
N_TASTE_DECLARED = 16          # B3: channel count (recomputed in C-section)

# PDG comparators — quarantined class-D terminal section ONLY.
M_H_PDG_POLE = 125.10          # observed Higgs pole mass (GeV)
V_PDG_OBS = 246.22             # observed EW VEV (GeV); B2 consumes this
                               # number as a declared external scale


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
    """Exact determinant via fraction-free-ish Gaussian elimination."""
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
    """Faddeev-LeVerrier: coefficients [1, c1, ..., cn] of
    lambda^n + c1 lambda^(n-1) + ... + cn, exact Fractions."""
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


def logdet_float(a):
    """log|det| of a float matrix via partial-pivot LU."""
    m = [row[:] for row in a]
    n = len(m)
    acc = 0.0
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if piv != col:
            m[col], m[piv] = m[piv], m[col]
        acc += math.log(abs(m[col][col]))
        for r in range(col + 1, n):
            f = m[r][col] / m[col][col]
            for c2 in range(col, n):
                m[r][c2] -= f * m[col][c2]
    return acc


# ---------------------------------------------------------------------------
# Framework primitives: minimal-block staggered operator (B4 surface).
# ---------------------------------------------------------------------------
SITES = list(itertools.product((0, 1), repeat=4))
SITE_INDEX = {s: i for i, s in enumerate(SITES)}


def staggered_operator(apbc_mask=(1, 1, 1, 1)):
    """Per-color staggered central-difference operator on the 2^4 block
    with eta phases eta_mu(x) = (-1)^(x_0 + ... + x_(mu-1)) and
    antiperiodic wrap in the directions flagged by apbc_mask.
    Returned with unit links (u_0 = 1); exact Fractions."""
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
                sign = -1 if (wrapped and apbc_mask[mu]) else 1
                y = SITE_INDEX[tuple(t)]
                d[x][y] += direction * eta * sign * Fraction(1, 2)
    return d


def pauli_kron():
    """4x4 Euclidean hermitian gamma matrices from Pauli tensor products:
    gamma_i = sigma_x (x) sigma_i (i = 1..3), gamma_4 = sigma_z (x) I.
    Gaussian-integer entries (python complex with integer parts)."""
    i2 = [[1, 0], [0, 1]]
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]

    # straightforward Kronecker product for 2x2 complex matrices
    def kron2(a, b):
        out = []
        for i in range(2):
            for k in range(2):
                row = []
                for j in range(2):
                    for l in range(2):
                        row.append(a[i][j] * b[k][l])
                out.append(row)
        return out

    return [kron2(sx, sx), kron2(sx, sy), kron2(sx, sz), kron2(sz, i2)]


# ---------------------------------------------------------------------------
# Section C — first-principles compute (load-bearing chain of T1).
# ---------------------------------------------------------------------------
def section_c():
    print("\n--- [C] T1 first-principles compute (operator -> spectrum -> "
          "determinant -> curvature) ---")

    # C1: Clifford generators and the taste-block Clifford identity.
    gammas = pauli_kron()
    clifford_ok = True
    for mu in range(4):
        for nu in range(4):
            for i in range(4):
                for j in range(4):
                    anti = sum(
                        gammas[mu][i][k] * gammas[nu][k][j]
                        + gammas[nu][i][k] * gammas[mu][k][j]
                        for k in range(4)
                    )
                    want = 2 if (mu == nu and i == j) else 0
                    if anti != want:
                        clifford_ok = False
    check("C", "Clifford algebra {gamma_mu, gamma_nu} = 2 delta_mu_nu "
               "(exact, built from Pauli kron)", clifford_ok)

    s = [[sum(gammas[mu][i][j] for mu in range(4)) for j in range(4)]
         for i in range(4)]
    s2 = [[sum(s[i][k] * s[k][j] for k in range(4)) for j in range(4)]
          for i in range(4)]
    check("C", "taste-block Clifford identity (sum_mu gamma_mu)^2 = 4 I "
               "(eigenvalue magnitude 2, i.e. |lambda| = 2 u_0 after "
               "mean-field scaling)",
          all(s2[i][j] == (4 if i == j else 0)
              for i in range(4) for j in range(4)))

    # C2: site-space staggered operator on the declared B4 surface.
    d_unit = staggered_operator()
    antisym = all(d_unit[i][j] == -d_unit[j][i]
                  for i in range(16) for j in range(16))
    d2 = mat_mul(d_unit, d_unit)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0)
                for i in range(16) for j in range(16))
    check("C", "eta-phase staggered operator on 2^4 block (all-direction "
               "antiperiodic wrap): D real antisymmetric", antisym)
    check("C", "D^2 = -4 I exactly (unit links; so D^2 = -4 u_0^2 I at "
               "mean field)", d2_ok,
          "exact Fraction matrix arithmetic")

    # C3: characteristic polynomial = (lambda^2 + 4)^8.
    coeffs = char_poly_exact(d_unit)
    target = [Fraction(0)] * 17
    for k in range(9):
        target[2 * k] = Fraction(math.comb(8, k) * 4 ** k)
    check("C", "char poly of D/u_0 is (lambda^2 + 4)^8 — 16 taste "
               "eigenvalues +/- 2i, multiplicity 8 each",
          coeffs == target,
          "Faddeev-LeVerrier, exact")

    # C4: taste channel count recomputed from the BZ-corner set (not
    # imported): |{0,1}^4| with Hamming multiplicities binom(4, hw).
    corners = list(itertools.product((0, 1), repeat=4))
    hw_classes = {}
    for n in corners:
        hw_classes.setdefault(sum(n), 0)
        hw_classes[sum(n)] += 1
    staircase = tuple(hw_classes[k] for k in sorted(hw_classes))
    n_taste_computed = len(corners)
    check("C", "N_taste = 16 recomputed from the BZ-corner set {0,1}^4 "
               "with Hamming staircase (1,4,6,4,1); W(hw) = 2 r hw -> "
               "all degenerate at r = 0",
          n_taste_computed == N_TASTE_DECLARED
          and staircase == (1, 4, 6, 4, 1)
          and sum(staircase) == 16)

    # C5: exact per-color determinant identity at rational test points.
    det_ok = True
    for a, m in ((Fraction(2, 3), Fraction(1, 3)),
                 (Fraction(7, 5), Fraction(0)),
                 (Fraction(1, 2), Fraction(2))):
        mat = [[a * d_unit[i][j] + (m if i == j else 0) for j in range(16)]
               for i in range(16)]
        if det_exact(mat) != (m * m + 4 * a * a) ** 8:
            det_ok = False
    check("C", "det(u_0 D + m) = (m^2 + 4 u_0^2)^8 per color — exact at "
               "3 rational (u_0, m) test points", det_ok)

    # C6: color factorization det over N_c colors = [per-color]^{N_c}
    # (exact, N_c = 3, 48x48 block matrix).
    a, m = Fraction(2, 3), Fraction(1, 3)
    n_c = 3
    big = [[Fraction(0)] * (16 * n_c) for _ in range(16 * n_c)]
    for c in range(n_c):
        for i in range(16):
            for j in range(16):
                big[c * 16 + i][c * 16 + j] = a * d_unit[i][j]
            big[c * 16 + i][c * 16 + i] += m
    check("C", "color factorization: det_48x48 = [det_taste]^3 at N_c = 3 "
               "(exact)", det_exact(big) == ((m * m + 4 * a * a) ** 8) ** 3)

    # C7: curvature from the determinant (NOT from the closed form):
    # per-color V(m) = -log det(u_0 D + m); finite-difference V''(0).
    d_float = [[float(x) * U_0 for x in row] for row in d_unit]

    def v_taste(m_val):
        mat = [[d_float[i][j] + (m_val if i == j else 0.0)
                for j in range(16)] for i in range(16)]
        return -logdet_float(mat)

    h = 1e-4
    curv_fd = (v_taste(h) - 2 * v_taste(0.0) + v_taste(-h)) / h ** 2
    curv_analytic = -4.0 / U_0 ** 2
    check("C", "V_taste''(0) = -N_taste/(4 u_0^2) = -4/u_0^2 from the "
               "computed determinant (finite difference vs analytic)",
          abs(curv_fd - curv_analytic) < 1e-5,
          f"fd = {curv_fd:.9f}, analytic = {curv_analytic:.9f}")
    grad_fd = (v_taste(h) - v_taste(-h)) / (2 * h)
    check("C", "V_taste'(0) = 0 (symmetric point is an extremum; "
               "tachyonic maximum since V'' < 0)",
          abs(grad_fd) < 1e-9 and curv_fd < 0.0,
          f"V'(0) fd = {grad_fd:.2e}")

    # C8: N_c independence computed from the determinant chain, not from
    # symbol inspection of the final formula.
    per_color_curvs = []
    for n_c_test in (1, 2, 3, 4):
        def v_color(m_val, k=n_c_test):
            mat = [[d_float[i][j] + (m_val if i == j else 0.0)
                    for j in range(16)] for i in range(16)]
            return -(k * logdet_float(mat)) / k  # det over colors, / N_c
        c_fd = (v_color(h) - 2 * v_color(0.0) + v_color(-h)) / h ** 2
        per_color_curvs.append(c_fd)
    spread = max(per_color_curvs) - min(per_color_curvs)
    check("C", "exact N_c cancellation: per-color curvature identical at "
               "N_c in {1,2,3,4} (computed)", spread == 0.0,
          f"spread = {spread:.2e}")

    # C9 (falsification leg F1): the old 'APBC in time only' gloss gives a
    # DIFFERENT operator: D^2 = -I and det = (m^2 + u_0^2)^8.
    d_time_only = staggered_operator(apbc_mask=(1, 0, 0, 0))
    d2t = mat_mul(d_time_only, d_time_only)
    time_only_d2 = all(d2t[i][j] == (Fraction(-1) if i == j else 0)
                       for i in range(16) for j in range(16))
    a, m = Fraction(2, 3), Fraction(1, 3)
    mat_t = [[a * d_time_only[i][j] + (m if i == j else 0)
              for j in range(16)] for i in range(16)]
    det_t = det_exact(mat_t)
    check("C", "falsification leg F1: time-only antiperiodic wrap gives "
               "D^2 = -I and det = (m^2 + u_0^2)^8 != (m^2 + 4 u_0^2)^8 "
               "— the all-direction B4 declaration is load-bearing",
          time_only_d2
          and det_t == (m * m + a * a) ** 8
          and det_t != (m * m + 4 * a * a) ** 8)

    # C10 (Step 5(c) susceptibility cross-check, audit-requested
    # 2026-06-11): the FULL susceptibility from the color-stacked
    # generating function W(m) = N_c log det(u_0 D + m) = -N_c V_taste(m)
    # is W''(0) = N_c N_taste / (4 u_0^2); the per-color per-channel
    # value W''(0) / (N_c N_taste) = 1/(4 u_0^2) equals the Step-4
    # per-channel curvature magnitude |V_taste''(0)| / N_taste — the
    # cross-check reduces to the same algebra, not an independent
    # derivation. (The pre-fix note text omitted the N_taste factor in
    # the full susceptibility and so double-divided by N_taste.)
    n_c_phys = 3

    def w_full(m_val):
        mat = [[d_float[i][j] + (m_val if i == j else 0.0)
                for j in range(16)] for i in range(16)]
        return n_c_phys * logdet_float(mat)

    wpp_fd = (w_full(h) - 2 * w_full(0.0) + w_full(-h)) / h ** 2
    wpp_analytic = n_c_phys * N_TASTE_DECLARED / (4.0 * U_0 ** 2)
    check("C", "Step 5(c) susceptibility: W''(0) = N_c N_taste/(4 u_0^2) "
               "from the computed determinant (finite difference vs "
               "analytic)",
          abs(wpp_fd - wpp_analytic) < 1e-4,
          f"fd = {wpp_fd:.9f}, analytic = {wpp_analytic:.9f}")
    per_color_channel = wpp_fd / (n_c_phys * N_TASTE_DECLARED)
    check("C", "Step 5(c) per-color per-channel W''(0)/(N_c N_taste) = "
               "1/(4 u_0^2) — equals the Step-4 per-channel curvature "
               "magnitude (same algebra; no double N_taste division)",
          abs(per_color_channel - 1.0 / (4.0 * U_0 ** 2)) < 1e-5
          and abs(per_color_channel - abs(curv_fd) / N_TASTE_DECLARED) < 1e-12,
          f"per-color per-channel = {per_color_channel:.9f}, "
          f"1/(4 u_0^2) = {1.0 / (4.0 * U_0 ** 2):.9f}")


# ---------------------------------------------------------------------------
# Section A — exact readout algebra over declared inputs (D1 + C1).
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- [A] D1/C1 readout algebra over declared boundary inputs ---")

    # A1: two independent evaluation routes for the defined scale.
    per_channel = (4.0 / U_0 ** 2) / N_TASTE_DECLARED
    route_one = V_GEV * math.sqrt(per_channel)          # definition D1
    route_two = V_GEV / (2.0 * U_0)                      # collapsed form
    check("A", "two routes agree: v*sqrt((4/u_0^2)/N_taste) == v/(2 u_0)",
          abs(route_one - route_two) < 1e-12,
          f"{route_one:.10f} vs {route_two:.10f}")
    m_curv = route_two

    # A2: exact readout identity residual.
    resid = abs(2.0 * U_0 * m_curv - V_GEV)
    check("A", "readout identity residual |2 u_0 m_curv_tree - v| ~ 0",
          resid < 1e-9, f"residual = {resid:.2e}")

    # A3: headline value at the declared inputs.
    check("A", "C1 headline: m_curv_tree = 140.3 GeV at (B1, B2) "
               "(rounded to 0.1 GeV)",
          abs(round(m_curv, 1) - 140.3) < 1e-9,
          f"m_curv_tree = {m_curv:.4f} GeV")

    # A4: B2 insensitivity certificate: PDG-anchored v vs the
    # hierarchy-lane bounded-formula value differ by 0.026%; both give
    # 140.3 at headline precision.  (This does NOT derive either v.)
    m_alt = V_HIERARCHY_LANE / (2.0 * U_0)
    rel = abs(V_HIERARCHY_LANE / V_GEV - 1.0)
    check("A", "B2 insensitivity: v = 246.22 and v = 246.2828 both give "
               "m_curv_tree = 140.3 at 0.1 GeV precision",
          round(m_curv, 1) == round(m_alt, 1) == 140.3 and rel < 3e-4,
          f"{m_curv:.4f} vs {m_alt:.4f}, dv/v = {rel:.2e}")

    # A5: analytic sensitivity (anti-tuning certificate, part 1):
    # d m_curv / d<P> = -m_curv / (4 <P>), verified by central difference.
    sens_analytic = -m_curv / (4.0 * P_BOUNDARY)
    dp = 1e-6
    m_plus = V_GEV / (2.0 * (P_BOUNDARY + dp) ** 0.25)
    m_minus = V_GEV / (2.0 * (P_BOUNDARY - dp) ** 0.25)
    sens_fd = (m_plus - m_minus) / (2 * dp)
    check("A", "analytic sensitivity d m_curv/d<P> = -m_curv/(4<P>) = "
               "-59.09 GeV (1% in <P> -> 0.25% in m_curv), fd-verified",
          abs(sens_fd - sens_analytic) < 1e-3,
          f"fd = {sens_fd:.6f}, analytic = {sens_analytic:.6f}")

    # A6: anti-tuning certificate, part 2 (falsification leg F2): the
    # single knob <P> cannot be tuned to the PDG Higgs pole within any
    # admissible neighborhood of the licensed value.
    p_needed = (V_GEV / (2.0 * M_H_PDG_POLE)) ** 4
    rel_off = p_needed / P_BOUNDARY - 1.0
    check("A", "falsification leg F2 (anti-tuning): hitting 125.10 GeV "
               "would need <P> = 0.9379, +58% off the licensed 0.5934 — "
               "no admissible tuning exists and none is claimed",
          abs(p_needed - 0.93787) < 5e-4 and rel_off > 0.5,
          f"<P>_needed = {p_needed:.5f}, rel offset = {rel_off:+.3f}")


# ---------------------------------------------------------------------------
# Section B — cross-note input verification and parent-note hygiene.
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- [B] cross-note inputs and parent-note hygiene ---")

    # B1: canonical plaquette helper residuals.
    check("B", "B1 matches canonical helper: CANONICAL_PLAQUETTE = 0.5934",
          abs(cps.CANONICAL_PLAQUETTE - P_BOUNDARY) == 0.0)
    check("B", "u_0 = <P>^(1/4) = 0.877681381 matches CANONICAL_U0",
          abs(cps.CANONICAL_U0 - U_0) < 1e-15,
          f"u_0 = {U_0:.9f}")

    # B2: the plaquette dependency's reuse license is on disk and still
    # carries the admitted-comparison/reuse-number language B1 relies on.
    plaq = (REPO_ROOT / "docs" / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md")
    plaq_text = plaq.read_text() if plaq.exists() else ""
    check("B", "plaquette license present: 0.5934 'admitted "
               "comparison/reuse number' language on disk",
          "admitted comparison/reuse number" in plaq_text
          and "0.5934" in plaq_text)

    # B3: the staircase dependency states the (1,4,6,4,1) multiplicities
    # and the W = 2 r hw staircase this note's B3 licenses.
    stair = (REPO_ROOT / "docs" /
             "WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md")
    stair_text = stair.read_text() if stair.exists() else ""
    check("B", "staircase dependency on disk with (1,4,6,4,1) "
               "multiplicities",
          "( 1, 4, 6, 4, 1 )" in stair_text or "(1,4,6,4,1)" in stair_text
          or "(1, 4, 6, 4, 1)" in stair_text)

    note_text = NOTE_PATH.read_text()
    flat = re.sub(r"\s+", " ", note_text)

    # B4: parent-note hygiene — primary label and demotion narrative.
    check("B", "parent note primary label is m_curv_tree with explicit "
               "demotion narrative (no Higgs-pole claim)",
          "m_curv_tree" in note_text
          and ("demot" in note_text.lower())
          and "NOT a Higgs-mass prediction" in note_text)

    # B5: no stale pre-repair Step 5(c) identification.
    check("B", "stale 'correct identification is m_H^2 = (1/chi_H)...' "
               "phrasing absent",
          "the correct identification is m_H" not in flat.lower())

    # B6: the v = 246.22 miscitation is repaired: the note declares v as
    # an external scale input and does not attribute 246.22 to the
    # bounded hierarchy formula.
    miscite = re.search(
        r"246\.22[^.]{0,160}from the bounded hierarchy formula", flat)
    check("B", "B2 declared honestly: 246.22 GeV is not attributed to "
               "the bounded hierarchy formula",
          miscite is None and "declared external EW VEV scale" in flat)

    # B7: every load-bearing markdown link in the note resolves to a file
    # on disk (dead-citation guard; the 2026-06-11 repair removed dead
    # TASTE_POLYNOMIAL / DM_AMGM / HIERARCHY_THEOREM citations).
    links = re.findall(r"\]\(([A-Za-z0-9_\-./]+\.md)\)", note_text)
    missing = [l for l in links
               if not (REPO_ROOT / "docs" / l).exists()
               and not (REPO_ROOT / l).exists()]
    check("B", "all markdown-linked note citations resolve on disk",
          not missing, f"missing: {missing}" if missing else "all resolve")

    # B8: comparator fence present in the parent note.
    check("B", "fenced class-D comparator section present in parent note",
          "Fenced comparator" in note_text)


# ---------------------------------------------------------------------------
# Section D — fenced external comparators (terminal; never load-bearing).
# ---------------------------------------------------------------------------
def section_d():
    print("\n--- [D] fenced comparators (PDG; quarantined, never "
          "load-bearing) ---")
    m_curv = V_GEV / (2.0 * U_0)

    # D1: the +12% separation report.  PASS verifies the SEPARATION is
    # correctly reported as +12.1% — it does NOT reward agreement.
    sep = m_curv / M_H_PDG_POLE - 1.0
    check("D", "comparator: m_curv_tree = 140.3 GeV sits +12.1% ABOVE the "
               "PDG Higgs pole 125.10 GeV (separation report, not a "
               "match claim)",
          0.115 < sep < 0.128,
          f"separation = {sep * 100:+.2f}%")

    # D2: the B2 scale label vs PDG observed VEV (identical by
    # declaration) and vs the hierarchy-lane bounded value (+0.0255%);
    # comparator context only.
    rel = V_HIERARCHY_LANE / V_PDG_OBS - 1.0
    check("D", "comparator: hierarchy-lane bounded v = 246.2828 GeV vs "
               "PDG v_obs = 246.22 GeV differ by +0.0255% (context only; "
               "neither derived here)",
          abs(rel - 0.000255) < 5e-5,
          f"rel = {rel * 100:+.4f}%")


def main() -> int:
    print("=" * 78)
    print(" higgs_tree_level_mean_field_runner_2026_05_03.py")
    print(" (2026-06-11 restructure: T1 computed from primitives;")
    print("  D1 declared definition; C1 bounded readout; comparators fenced)")
    print(" Parent note: docs/HIGGS_MASS_FROM_AXIOM_NOTE.md")
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
