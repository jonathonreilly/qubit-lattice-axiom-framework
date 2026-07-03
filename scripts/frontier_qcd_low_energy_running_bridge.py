#!/usr/bin/env python3
"""QCD v -> M_Z running transfer-map kernel theorem (K1-K5).

Status: bounded kernel theorem about the transfer map T defined by the
        declared imports (continuum 2-loop SM MSbar RGE coefficients,
        Machacek-Vaughn 1984 / Arason et al 1992; scale convention
        v = 246.282818290129 GeV; PDG scales m_t, M_Z; fixed auxiliary
        EW tuple).  The theorem is quantified over the whole admissible
        domain D = [0.085, 0.130]; NO specific boundary value alpha_s(v)
        appears anywhere in the load-bearing claim.  This responds to the
        2026-05-25 numerical-match classification, whose load-bearing
        step depended on one imported boundary value.

Verifies the claims of QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md:

  K1. Well-definedness: 1 - L*a > 0 on D with derived Landau margin
      1/(L*a_max) = 6.55; T_1 and T_2 are finite and positive on D.
  K2. Exact 1-loop closed form 1/T_1(a) = 1/a - L with
      L = (7/2pi) ln(v/m_t) + ((23/3)/2pi) ln(m_t/M_Z) = 1.1746670551,
      verified against an independent numerical integration.
  K3. T_1 obeys the exact Jacobian identity dT_1/da = (T_1/a)^2 > 1 on D;
      T_2 is grid-certified as strictly increasing and expansive
      (J_2 = 1.328 at the domain center), with a center inverse round-trip.
  K4. Auxiliary-tuple insensitivity: 5% variations of (g1, g2, yt, lambda)
      shift T_2 by < 3.1e-6 (anti-tuning).
  K5. Truncation envelope: T_2 - T_1 = +5.7e-4 at the domain center.

Group factors C_A = 3 and T_F = 1/2 are COMPUTED from the Gell-Mann
generators (structure constants + trace normalization), so the 1-loop
coefficient b0(n_f) = (11/3) C_A - (4/3) T_F n_f is derived inside this
packet rather than asserted.

Every check is tagged [A] (algebraic identity on declared inputs),
[B] (note/runner manifest sync), or [D] (external PDG comparator,
appendix only, not load-bearing).  Two-integrator independence
(RK45 vs DOP853) and two falsification legs (sign-flipped kernel
contracts; threshold removal shifts T_2 by ~1e-3, four orders above the
integrator residual) guard against vacuous passes.

Deterministic; runs in about a second.  Self-contained except numpy/scipy.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "D": 0}

PI = np.pi
NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md"
)

# ---------------------------------------------------------------------------
# Declared imports (the boundary of the bounded theorem; see note section
# "Declared imports").  These define the transfer map; the theorem is about
# the map, not about any particular boundary value fed into it.
# ---------------------------------------------------------------------------
V_SCALE = 246.282818290129   # GeV — framework scale convention v
M_T = 172.69                 # GeV — PDG top pole mass (declared import)
M_Z = 91.1876                # GeV — PDG Z mass (declared import)

# Auxiliary EW boundary tuple (fixed declared import; K4 shows it is
# non-tuning at the < 3.1e-6 level under 5% variations).
G1_AUX = 0.46228
G2_AUX = 0.65184
YT_AUX = 0.93737
LAM_AUX = 0.13

# Kernel domain D (the whole quantified domain of the theorem).
A_MIN = 0.085
A_MAX = 0.130
A_CENTER = 0.5 * (A_MIN + A_MAX)          # 0.1075
GRID = np.linspace(A_MIN, A_MAX, 10)       # uniform 10-point grid on D

# Note-declared closed-form constant (B-class manifest sync target).
L_DECLARED = 1.1746670551

# -- PDG comparator (class D, appendix only; NOT load-bearing) --------------
ALPHA_S_MZ_PDG = 0.1180
ALPHA_S_MZ_PDG_SIGMA = 0.0009
# Historical plaquette-lane boundary value: appears ONLY in the labeled
# comparator appendix, never in any load-bearing check.
ALPHA_S_V_COMPARATOR = 0.103304
PULLBACK_WINDOW_DECLARED = (0.10257, 0.10394)


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    CLASS_COUNTS[kind] = CLASS_COUNTS.get(kind, 0) + 1
    msg = f"  [{status}] [{kind}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
#  Part 1: SU(3) group factors computed from the Gell-Mann generators
# ---------------------------------------------------------------------------

def gell_mann_generators() -> list[np.ndarray]:
    """The eight SU(3) generators T^a = lambda^a / 2 (fundamental rep)."""
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0)
    return [m / 2.0 for m in (l1, l2, l3, l4, l5, l6, l7, l8)]


def derive_group_factors():
    """Compute T_F, f^{abc}, C_A, C_F from the generators (no assertion)."""
    T = gell_mann_generators()
    n = len(T)
    # Trace normalization Tr(T^a T^b) = T_F delta_ab
    tr = np.array([[np.trace(T[a] @ T[b]) for b in range(n)] for a in range(n)])
    t_f = float(np.real(tr[0, 0]))
    tr_offdiag_max = float(np.max(np.abs(tr - t_f * np.eye(n))))
    # Structure constants from [T^a, T^b] = i f^{abc} T^c with the derived
    # normalization: f^{abc} = -2i/(2 T_F) * Tr([T^a, T^b] T^c).
    f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            comm = T[a] @ T[b] - T[b] @ T[a]
            for c in range(n):
                f[a, b, c] = float(np.real(-1j / t_f * np.trace(comm @ T[c])))
    # Adjoint Casimir from f^{acd} f^{bcd} = C_A delta^{ab}
    ff = np.einsum("acd,bcd->ab", f, f)
    c_a = float(ff[0, 0])
    ff_offdiag_max = float(np.max(np.abs(ff - c_a * np.eye(n))))
    # Fundamental Casimir sum_a T^a T^a = C_F * I
    casimir = sum(t @ t for t in T)
    c_f = float(np.real(casimir[0, 0]))
    cf_dev = float(np.max(np.abs(casimir - c_f * np.eye(3))))
    return T, t_f, tr_offdiag_max, f, c_a, ff_offdiag_max, c_f, cf_dev


def b0(n_f: int, c_a: float = 3.0, t_f: float = 0.5) -> float:
    """Positive 1-loop coefficient: d(1/alpha)/d ln mu = b0/(2 pi)."""
    return (11.0 / 3.0) * c_a - (4.0 / 3.0) * t_f * n_f


def part_1_group_factors():
    print("\n=== Part 1: SU(3) group factors derived from Gell-Mann generators ===\n")
    (_T, t_f, tr_dev, f, c_a, ff_dev, c_f, cf_dev) = derive_group_factors()
    check("trace normalization Tr(T^a T^b) = T_F delta_ab with T_F = 1/2",
          abs(t_f - 0.5) < 1e-14 and tr_dev < 1e-14,
          f"T_F = {t_f:.15f}, max off-diagonal deviation = {tr_dev:.2e}")
    anti_ab = float(np.max(np.abs(f + np.transpose(f, (1, 0, 2)))))
    anti_bc = float(np.max(np.abs(f + np.transpose(f, (0, 2, 1)))))
    check("structure constants f^{abc} totally antisymmetric (computed, not asserted)",
          anti_ab < 1e-13 and anti_bc < 1e-13,
          f"max |f^abc + f^bac| = {anti_ab:.2e}, max |f^abc + f^acb| = {anti_bc:.2e}")
    check("adjoint Casimir f^{acd} f^{bcd} = C_A delta^ab with C_A = 3",
          abs(c_a - 3.0) < 1e-12 and ff_dev < 1e-12,
          f"C_A = {c_a:.15f}, max off-diagonal deviation = {ff_dev:.2e}")
    check("fundamental Casimir sum_a T^a T^a = C_F * I with C_F = 4/3",
          abs(c_f - 4.0 / 3.0) < 1e-14 and cf_dev < 1e-14,
          f"C_F = {c_f:.15f}, deviation from C_F*I = {cf_dev:.2e}")
    b0_6 = b0(6, c_a, t_f)
    b0_5 = b0(5, c_a, t_f)
    check("b0(n_f) = (11/3)C_A - (4/3)T_F n_f gives b0(6) = 7, b0(5) = 23/3 "
          "(= 11 - 2 n_f/3, derived not asserted)",
          abs(b0_6 - 7.0) < 1e-12 and abs(b0_5 - 23.0 / 3.0) < 1e-12
          and b0_5 > b0_6 > 0.0,
          f"b0(6) = {b0_6:.12f}, b0(5) = {b0_5:.12f}; b0(5) > b0(6) > 0")
    return c_a, t_f


# ---------------------------------------------------------------------------
#  Transfer maps
# ---------------------------------------------------------------------------

def closed_form_L(c_a: float = 3.0, t_f: float = 0.5) -> float:
    """L = (b0(6)/2pi) ln(v/m_t) + (b0(5)/2pi) ln(m_t/M_Z)."""
    return (b0(6, c_a, t_f) / (2.0 * PI)) * np.log(V_SCALE / M_T) \
        + (b0(5, c_a, t_f) / (2.0 * PI)) * np.log(M_T / M_Z)


def t1_closed(a: float, L: float) -> float:
    """Exact 1-loop transfer map: 1/T_1(a) = 1/a - L."""
    return a / (1.0 - L * a)


def t1_jacobian_analytic(a: float, L: float) -> float:
    """dT_1/da = 1/(1 - L a)^2 (exact)."""
    return 1.0 / (1.0 - L * a) ** 2


def beta_g3_1loop(t, y, n_f: int):
    g3, = y
    return [-(b0(n_f) / (16.0 * PI ** 2)) * g3 ** 3]


def t1_numeric(a: float, method: str = "RK45") -> float:
    """Independent numerical 1-loop transfer (same map, integrated)."""
    g3 = np.sqrt(4.0 * PI * a)
    for (t_s, t_e, n_f) in [(np.log(V_SCALE), np.log(M_T), 6),
                            (np.log(M_T), np.log(M_Z), 5)]:
        sol = solve_ivp(lambda t, y: beta_g3_1loop(t, y, n_f),
                        [t_s, t_e], [g3], method=method,
                        rtol=1e-13, atol=1e-15)
        if not sol.success:
            raise RuntimeError(f"1-loop segment failed: {sol.message}")
        g3 = float(sol.y[0, -1])
    return g3 ** 2 / (4.0 * PI)


def beta_2loop_full(t, y, n_f: int):
    """Standard MSbar 2-loop SM RGE (Machacek-Vaughn 1984; Arason 1992).

    Declared continuum import; the SU(3) group factors entering the gauge
    coefficient are recomputed in Part 1.
    """
    g1, g2, g3, yt, lam = y
    fac = 1.0 / (16.0 * PI ** 2)
    fac2 = fac ** 2
    g1sq, g2sq, g3sq, ytsq = g1 ** 2, g2 ** 2, g3 ** 2, yt ** 2

    beta_g1_1 = (41.0 / 10.0) * g1 ** 3
    beta_g2_1 = -(19.0 / 6.0) * g2 ** 3
    beta_g3_1 = -b0(n_f) * g3 ** 3
    beta_yt_1 = yt * (9.0 / 2.0 * ytsq - 17.0 / 20.0 * g1sq
                      - 9.0 / 4.0 * g2sq - 8.0 * g3sq)
    beta_lam_1 = (24.0 * lam ** 2 + 12.0 * lam * ytsq - 6.0 * ytsq ** 2
                  - 3.0 * lam * (3.0 * g2sq + g1sq)
                  + 3.0 / 8.0 * (2.0 * g2sq ** 2 + (g2sq + g1sq) ** 2))

    beta_g1_2 = g1 ** 3 * (199.0 / 50.0 * g1sq + 27.0 / 10.0 * g2sq
                           + 44.0 / 5.0 * g3sq - 17.0 / 10.0 * ytsq)
    beta_g2_2 = g2 ** 3 * (9.0 / 10.0 * g1sq + 35.0 / 6.0 * g2sq
                           + 12.0 * g3sq - 3.0 / 2.0 * ytsq)
    beta_g3_2 = g3 ** 3 * (11.0 / 10.0 * g1sq + 9.0 / 2.0 * g2sq
                           - 26.0 * g3sq - 2.0 * ytsq)
    beta_yt_2 = yt * (
        -12.0 * ytsq ** 2
        + ytsq * (36.0 * g3sq + 225.0 / 16.0 * g2sq + 131.0 / 80.0 * g1sq)
        + 1187.0 / 216.0 * g1sq ** 2 - 23.0 / 4.0 * g2sq ** 2
        - 108.0 * g3sq ** 2
        + 19.0 / 15.0 * g1sq * g3sq + 9.0 / 4.0 * g2sq * g3sq
        + 6.0 * lam ** 2 - 6.0 * lam * ytsq
    )

    return [fac * beta_g1_1 + fac2 * beta_g1_2,
            fac * beta_g2_1 + fac2 * beta_g2_2,
            fac * beta_g3_1 + fac2 * beta_g3_2,
            fac * beta_yt_1 + fac2 * beta_yt_2,
            fac * beta_lam_1]


SEGMENTS_MATCHED = [(np.log(V_SCALE), np.log(M_T), 6),
                    (np.log(M_T), np.log(M_Z), 5)]
SEGMENTS_NF6_ONLY = [(np.log(V_SCALE), np.log(M_Z), 6)]
SEGMENTS_NF5_ONLY = [(np.log(V_SCALE), np.log(M_Z), 5)]


def t2(a: float, method: str = "RK45", segments=None,
       aux=(G1_AUX, G2_AUX, YT_AUX, LAM_AUX)) -> float:
    """2-loop matched transfer map T_2: alpha_s(v) -> alpha_s(M_Z).

    Defined for any a in the kernel domain; the auxiliary tuple is a fixed
    declared import (K4 quantifies its (in)sensitivity).
    """
    if segments is None:
        segments = SEGMENTS_MATCHED
    g3 = np.sqrt(4.0 * PI * a)
    y = [aux[0], aux[1], g3, aux[2], aux[3]]
    for (t_s, t_e, n_f) in segments:
        sol = solve_ivp(lambda t, yy: beta_2loop_full(t, yy, n_f),
                        [t_s, t_e], y, method=method,
                        rtol=1e-12, atol=1e-14)
        if not sol.success:
            raise RuntimeError(f"2-loop segment failed: {sol.message}")
        y = list(sol.y[:, -1])
    return y[2] ** 2 / (4.0 * PI)


# ---------------------------------------------------------------------------
#  Parts 2-6: kernel theorem K1-K5 (all class A, quantified over D)
# ---------------------------------------------------------------------------

def part_2_k1_landau_margin(L: float):
    print("\n=== Part 2 (K1): well-definedness on D = [0.085, 0.130] ===\n")
    check("closed-form constant L matches the note-declared value 1.1746670551",
          abs(L - L_DECLARED) < 1e-9,
          f"L = {L:.13f}, |L - declared| = {abs(L - L_DECLARED):.2e}")
    landau_pole = 1.0 / L
    margin = landau_pole / A_MAX
    check("Landau margin: pole 1/L lies a factor 6.55 above the domain edge "
          "(1 - L a > 0 on all of D)",
          margin > 6.5 and (1.0 - L * A_MAX) > 0.0,
          f"1/L = {landau_pole:.6f}, margin (1/L)/a_max = {margin:.4f}")
    t1_vals = [t1_closed(a, L) for a in GRID]
    check("T_1 finite and positive at every point of the 10-point grid on D",
          all(np.isfinite(v) and 0.0 < v < 1.0 for v in t1_vals),
          f"T_1 range on D: [{t1_vals[0]:.6f}, {t1_vals[-1]:.6f}]")


def part_3_k2_closed_form(L: float):
    print("\n=== Part 3 (K2): exact 1-loop closed form vs independent integration ===\n")
    res_center = abs(t1_closed(A_CENTER, L) - t1_numeric(A_CENTER))
    check("closed form 1/T_1 = 1/a - L matches RK45 integration at the domain "
          "center a = 0.1075",
          res_center < 1e-12,
          f"residual = {res_center:.2e}")
    res_grid = max(abs(t1_closed(a, L) - t1_numeric(a)) for a in GRID)
    check("closed form matches RK45 at every grid point of D",
          res_grid < 1e-12,
          f"max residual over grid = {res_grid:.2e}")
    two_int = abs(t2(A_CENTER, method="RK45") - t2(A_CENTER, method="DOP853"))
    check("two-integrator independence: T_2 via RK45 vs DOP853 agree",
          two_int < 1e-12,
          f"|RK45 - DOP853| = {two_int:.2e}")
    return two_int


def part_4_k3_expansive_bijection(L: float):
    print("\n=== Part 4 (K3): exact T_1 plus T_2 grid monotonicity/expansivity ===\n")
    jac_dev = max(abs(t1_jacobian_analytic(a, L) - (t1_closed(a, L) / a) ** 2)
                  for a in GRID)
    h = 1e-6
    fd = (t1_closed(A_CENTER + h, L) - t1_closed(A_CENTER - h, L)) / (2.0 * h)
    fd_dev = abs(fd - t1_jacobian_analytic(A_CENTER, L)) / fd
    check("exact Jacobian identity dT_1/da = (T_1/a)^2 holds on the grid "
          "(and matches a finite difference at the center)",
          jac_dev < 1e-12 and fd_dev < 1e-8,
          f"max |1/(1-La)^2 - (T_1/a)^2| = {jac_dev:.2e}, FD rel dev = {fd_dev:.2e}")
    t1_vals = [t1_closed(a, L) for a in GRID]
    j1_min = t1_jacobian_analytic(A_MIN, L)
    check("T_1 strictly increasing and expansive on D (dT_1/da > 1 everywhere)",
          all(t1_vals[i + 1] > t1_vals[i] for i in range(len(GRID) - 1))
          and j1_min > 1.0,
          f"min dT_1/da on D = {j1_min:.6f} > 1")
    t2_vals = [t2(a) for a in GRID]
    check("T_2 strictly increasing on the 10-point grid",
          all(t2_vals[i + 1] > t2_vals[i] for i in range(len(GRID) - 1)),
          f"T_2 image on grid: [{t2_vals[0]:.6f}, {t2_vals[-1]:.6f}]")
    slopes = [(t2_vals[i + 1] - t2_vals[i]) / (GRID[i + 1] - GRID[i])
              for i in range(len(GRID) - 1)]
    j2_center = (t2(A_CENTER + 1e-5) - t2(A_CENTER - 1e-5)) / 2e-5
    check("T_2 grid expansivity: every grid slope > 1; central Jacobian J_2 = 1.328",
          min(slopes) > 1.0 and abs(j2_center - 1.328) < 5e-3,
          f"min slope = {min(slopes):.4f}, J_2(0.1075) = {j2_center:.4f}")
    target = t2(A_CENTER)
    a_back = brentq(lambda a: t2(a) - target, A_MIN, A_MAX, xtol=1e-12)
    check("inverse round-trip: T_2^{-1}(T_2(0.1075)) recovers 0.1075",
          abs(a_back - A_CENTER) < 1e-9,
          f"|round-trip - 0.1075| = {abs(a_back - A_CENTER):.2e}")
    return t2_vals


def part_5_k4_auxiliary_insensitivity():
    print("\n=== Part 5 (K4): auxiliary-tuple insensitivity (anti-tuning) ===\n")
    t2_center = t2(A_CENTER)
    base = [G1_AUX, G2_AUX, YT_AUX, LAM_AUX]
    names = ["g1", "g2", "yt", "lambda"]
    worst = 0.0
    worst_name = ""
    for i, name in enumerate(names):
        for fac in (1.05, 0.95):
            varied = list(base)
            varied[i] *= fac
            d = abs(t2(A_CENTER, aux=tuple(varied)) - t2_center)
            print(f"    {name} x {fac:.2f}: |delta T_2| = {d:.3e}")
            if d > worst:
                worst, worst_name = d, name
    check("max single-parameter 5% variation of the auxiliary tuple shifts "
          "T_2 by < 3.1e-6",
          worst < 3.1e-6,
          f"worst = {worst:.3e} ({worst_name}); the tuple is not a tuning knob")
    joint_up = abs(t2(A_CENTER, aux=tuple(x * 1.05 for x in base)) - t2_center)
    joint_dn = abs(t2(A_CENTER, aux=tuple(x * 0.95 for x in base)) - t2_center)
    check("joint 5% variation of all four auxiliary parameters shifts T_2 by "
          "< 3.1e-6",
          max(joint_up, joint_dn) < 3.1e-6,
          f"joint up/down = {joint_up:.3e} / {joint_dn:.3e}")


def part_6_k5_envelope_and_falsification(L: float, two_int_residual: float):
    print("\n=== Part 6 (K5 + falsification legs): envelope, threshold bracket, "
          "sign flip ===\n")
    t2_c = t2(A_CENTER)
    t1_c = t1_closed(A_CENTER, L)
    envelope = t2_c - t1_c
    check("truncation envelope T_2 - T_1 = +5.7e-4 at the domain center "
          "(positive, bounded)",
          0.0 < envelope < 1e-3 and abs(envelope - 5.7e-4) < 5e-5,
          f"T_2 - T_1 = {envelope:+.3e}")
    t2_nf6 = t2(A_CENTER, segments=SEGMENTS_NF6_ONLY)
    t2_nf5 = t2(A_CENTER, segments=SEGMENTS_NF5_ONLY)
    check("derived strict threshold bracket T_2[nf=6 only] < T_2[matched] < "
          "T_2[nf=5 only] (from b0(5) > b0(6) > 0)",
          t2_nf6 < t2_c < t2_nf5,
          f"{t2_nf6:.6f} < {t2_c:.6f} < {t2_nf5:.6f}")
    shift = abs(t2_c - t2_nf6)
    check("falsification: removing the top threshold shifts T_2 by ~1.03e-3, "
          "more than 1e4 x the two-integrator residual (check is not vacuous)",
          shift > 1e4 * max(two_int_residual, 1e-15)
          and abs(shift - 1.03e-3) < 5e-5,
          f"shift = {shift:.3e}, 1e4 x residual = {1e4 * max(two_int_residual, 1e-15):.3e}")
    t_flip = A_CENTER / (1.0 + L * A_CENTER)
    j_flip = (t_flip / A_CENTER) ** 2
    check("falsification: sign-flipped kernel 1/T = 1/a + L contracts "
          "(T < a, Jacobian < 1) — expansivity is a real property, not a tautology",
          t_flip < A_CENTER and j_flip < 1.0,
          f"T_flip(0.1075) = {t_flip:.6f} < 0.1075, J_flip = {j_flip:.4f} < 1")


# ---------------------------------------------------------------------------
#  Part 7: note/runner manifest sync (class B)
# ---------------------------------------------------------------------------

def _section(text: str, heading: str) -> str:
    """Return the body of a markdown section starting at `heading`."""
    idx = text.find(heading)
    if idx < 0:
        return ""
    rest = text[idx + len(heading):]
    nxt = rest.find("\n## ")
    return rest if nxt < 0 else rest[:nxt]


def part_7_manifest_sync(L: float):
    print("\n=== Part 7: note/runner manifest sync (bookkeeping, class B) ===\n")
    note = NOTE_PATH.read_text(encoding="utf-8")
    check("note declares the same closed-form constant L = 1.1746670551 and "
          "the same kernel domain [0.085, 0.130]",
          "1.1746670551" in note and "[0.085, 0.130]" in note
          and abs(L - L_DECLARED) < 1e-9,
          "note text carries the runner's L and domain", kind="B")
    check("note declares the same import scales v, m_t, M_Z and auxiliary tuple",
          "246.282818290129" in note and "172.69" in note and "91.1876" in note
          and "0.46228" in note and "0.65184" in note and "0.93737" in note,
          f"v = {V_SCALE}, m_t = {M_T}, M_Z = {M_Z}", kind="B")
    theorem_sec = _section(note, "## Kernel theorem")
    appendix_sec = _section(note, "## Comparator appendix")
    check("the boundary value 0.103304 is absent from the kernel-theorem claim "
          "surface and confined to the labeled class-D comparator appendix",
          bool(theorem_sec) and bool(appendix_sec)
          and "0.103304" not in theorem_sec
          and "0.103304" in appendix_sec
          and "class D" in appendix_sec and "not load-bearing" in appendix_sec,
          "claim surface is boundary-value-free", kind="B")


# ---------------------------------------------------------------------------
#  Part 8: comparator appendix (class D; NOT load-bearing)
# ---------------------------------------------------------------------------

def part_8_comparator_appendix():
    print("\n=== Part 8: comparator appendix (class D; NOT load-bearing) ===\n")
    print("  These two checks are external PDG comparisons recorded for")
    print("  downstream context only. The kernel theorem K1-K5 above does not")
    print("  depend on them; the T2 theorem surface is grid/center certified over D.\n")
    a_mz = t2(ALPHA_S_V_COMPARATOR)
    check("worked example: T_2(0.103304) = 0.118067, inside the PDG band "
          "0.1180 +/- 0.0009",
          abs(a_mz - 0.118067) < 5e-6
          and abs(a_mz - ALPHA_S_MZ_PDG) <= ALPHA_S_MZ_PDG_SIGMA,
          f"T_2(0.103304) = {a_mz:.6f}", kind="D")
    band_lo = ALPHA_S_MZ_PDG - ALPHA_S_MZ_PDG_SIGMA
    band_hi = ALPHA_S_MZ_PDG + ALPHA_S_MZ_PDG_SIGMA
    w_lo = brentq(lambda a: t2(a) - band_lo, A_MIN, A_MAX, xtol=1e-12)
    w_hi = brentq(lambda a: t2(a) - band_hi, A_MIN, A_MAX, xtol=1e-12)
    check("PDG-band pullback window T_2^{-1}([0.1171, 0.1189]) = "
          "[0.10257, 0.10394] (interior to D)",
          abs(w_lo - PULLBACK_WINDOW_DECLARED[0]) < 5e-5
          and abs(w_hi - PULLBACK_WINDOW_DECLARED[1]) < 5e-5
          and A_MIN < w_lo < w_hi < A_MAX,
          f"window = [{w_lo:.5f}, {w_hi:.5f}]", kind="D")


def main() -> None:
    print("=" * 78)
    print("QCD v -> M_Z running transfer-map kernel theorem (K1-K5)")
    print("=" * 78)
    print()
    print("Theorem surface: exact T_1 on D plus a bounded T_2 grid certificate")
    print(f"over D = [{A_MIN}, {A_MAX}] under the declared imports.")
    print("No specific boundary value alpha_s(v) appears in any load-bearing check;")
    print("PDG comparisons are confined to the labeled class-D appendix (Part 8).")

    c_a, t_f = part_1_group_factors()
    L = closed_form_L(c_a, t_f)
    part_2_k1_landau_margin(L)
    two_int_residual = part_3_k2_closed_form(L)
    part_4_k3_expansive_bijection(L)
    part_5_k4_auxiliary_insensitivity()
    part_6_k5_envelope_and_falsification(L, two_int_residual)
    part_7_manifest_sync(L)
    part_8_comparator_appendix()

    print()
    print("=" * 78)
    print(f"CHECK CLASSES: A={CLASS_COUNTS['A']}  B={CLASS_COUNTS['B']}  "
          f"D={CLASS_COUNTS['D']}  (D-comparators are a labeled minority; "
          "no C-class first-principles claims made)")
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 78)

    sys.exit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
