#!/usr/bin/env python3
"""Common-scale four-loop check of the down-type five-sixths bridge (correction runner).

Corrigendum runner, 2026-09-30, for the down-type bridge

    |V_cb| = (m_s/m_b)^(5/6)      (5/6 = C_F - T_F),   R_pred = [alpha_s(v)/sqrt(6)]^(6/5).

Companion to the Corrigendum (2026-09-30) sections of
  docs/CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md   (full table)
  docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md
  docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md
  docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md
  docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md
and of the downstream notes that restated the mixed-scale figure:
  docs/UP_TYPE_MASS_RATIO_CKM_INVERSION_NOTE.md, docs/MASS_SPECTRUM_DERIVED_NOTE.md,
  docs/COMPLETE_PREDICTION_CHAIN_2026_04_15.md,
  docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md,
  docs/lanes/open_science/03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md.

What it checks (all COMPARATOR content; it derives no mass, no exponent and no scale):

  A. exact bookkeeping: C_F - T_F = 5/6, and the literature values of the QCD
     coefficients it relies on;
  B. the running engine itself, against closed forms and against a second,
     independent integration path (coupling-space quadrature);
  C. the ratio R = m_s/m_b is scale-independent at fixed flavour number, so the
     ONLY consistent comparison surface for a bridge stated on R is one common
     scale;
  D. at one common scale, with four-loop QCD running, two-loop matching and PDG 2024 inputs, the
     bridge misses by about about +18.7% (not +0.2%), and the exponent that fits is
     about 0.7973, not 5/6;
  E. the same holds across standard input sets, and with no running at all
     (lattice mass ratios);
  F. the +0.2% figure is the mixed-scale value m_s(2 GeV)/m_b(m_b); it requires
     the strange mass to be quoted at 1.99 GeV, and moves 1% per 3.6% in that scale;
  G. two downstream figures that rode on the mixed comparator: m_d/m_b (+3.5% becomes
     +22.5%) and the up-type partition f_23 (0.9983 becomes 0.867);
  H. the sampled supplied truncated one-loop Standard-Model flow does not move the needed exponent to 5/6 (it stays 0.790-0.798).

Inputs are observational comparators, not derivation inputs:
  PDG 2024 (Phys. Rev. D 110, 030001): m_s(2 GeV) = 93.5(8) MeV, m_b(m_b) = 4.183(7) GeV,
    alpha_s(M_Z) = 0.1180(9); PDG 2024 lattice-only average m_s(2 GeV) = 92.74(54) MeV.
  FLAG 2024 (arXiv:2411.04268): Nf=2+1+1 m_s = 93.46(58) MeV, m_b(m_b) = 4.200(14) GeV,
    m_c/m_s = 11.766(30), m_b/m_c (FNAL/MILC/TUMQCD 18) = 4.578(5)(6)(0)(1);
    Nf=2+1 m_s = 92.4(1.0) MeV, m_b(m_b) = 4.171(20) GeV.
  Repository atlas value alpha_s(v) = 0.103303816122 (ALPHA_S_DERIVED_NOTE.md).
QCD ingredients (literature): four-loop beta function (van Ritbergen, Vermaseren, Larin
1997), four-loop quark-mass anomalous dimension (Vermaseren, Larin, van Ritbergen 1997;
Chetyrkin 1997), two-loop decoupling at mu = m_h(m_h) (Chetyrkin, Kniehl, Steinhauser
1997).  Pure Python for Parts A-G; numpy for Part H.  No randomness.
"""

from __future__ import annotations

# Explicit bounded execution cap; scientific content is unchanged by this metadata.
AUDIT_TIMEOUT_SEC = 120

import math
from fractions import Fraction

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


# ---------------------------------------------------------------------------
# QCD coefficients, a = alpha_s/pi:  da/dt = -sum beta_i a^(i+2),
#                                     d ln m/dt = -sum gamma_i a^(i+1),  t = ln mu^2.
# ---------------------------------------------------------------------------
Z3 = 1.2020569031595942
Z4 = math.pi**4 / 90.0
Z5 = 1.0369277551433699


def beta_coeffs(nf: int, loops: int = 4) -> list[float]:
    b0 = (11.0 - 2.0 * nf / 3.0) / 4.0
    b1 = (102.0 - 38.0 * nf / 3.0) / 16.0
    b2 = (2857.0 / 2.0 - 5033.0 * nf / 18.0 + 325.0 * nf**2 / 54.0) / 64.0
    b3 = (
        149753.0 / 6.0 + 3564.0 * Z3
        - (1078361.0 / 162.0 + 6508.0 * Z3 / 27.0) * nf
        + (50065.0 / 162.0 + 6472.0 * Z3 / 81.0) * nf**2
        + 1093.0 * nf**3 / 729.0
    ) / 256.0
    return [b0, b1, b2, b3][:loops]


def gamma_coeffs(nf: int, loops: int = 4) -> list[float]:
    g0 = 1.0
    g1 = (202.0 / 3.0 - 20.0 * nf / 9.0) / 16.0
    g2 = (1249.0 + (-2216.0 / 27.0 - 160.0 * Z3 / 3.0) * nf - 140.0 * nf**2 / 81.0) / 64.0
    g3 = (
        4603055.0 / 162.0 + 135680.0 * Z3 / 27.0 - 8800.0 * Z5
        + (-91723.0 / 27.0 - 34192.0 * Z3 / 9.0 + 880.0 * Z4 + 18400.0 * Z5 / 9.0) * nf
        + (5242.0 / 243.0 + 800.0 * Z3 / 9.0 - 160.0 * Z4 / 3.0) * nf**2
        + (-332.0 / 243.0 + 64.0 * Z3 / 27.0) * nf**3
    ) / 256.0
    return [g0, g1, g2, g3][:loops]


def _da(a: float, nf: int, loops: int) -> float:
    return -sum(b * a ** (i + 2) for i, b in enumerate(beta_coeffs(nf, loops)))


def _dlnm(a: float, nf: int, loops: int) -> float:
    return -sum(g * a ** (i + 1) for i, g in enumerate(gamma_coeffs(nf, loops)))


def run_rk4(a0: float, lnm0: float, mu0: float, mu1: float, nf: int, loops: int, steps: int = 400):
    """Path 1: RK4 in t = ln mu^2 on the pair (a, ln m)."""
    if mu0 == mu1:
        return a0, lnm0
    t0, t1 = math.log(mu0**2), math.log(mu1**2)
    h = (t1 - t0) / steps
    a, lm = a0, lnm0
    for _ in range(steps):
        k1a, k1m = _da(a, nf, loops), _dlnm(a, nf, loops)
        a2 = a + 0.5 * h * k1a
        k2a, k2m = _da(a2, nf, loops), _dlnm(a2, nf, loops)
        a3 = a + 0.5 * h * k2a
        k3a, k3m = _da(a3, nf, loops), _dlnm(a3, nf, loops)
        a4 = a + h * k3a
        k4a, k4m = _da(a4, nf, loops), _dlnm(a4, nf, loops)
        a += h * (k1a + 2 * k2a + 2 * k3a + k4a) / 6.0
        lm += h * (k1m + 2 * k2m + 2 * k3m + k4m) / 6.0
    return a, lm


def _simpson(f, x0: float, x1: float, n: int) -> float:
    if n % 2:
        n += 1
    h = (x1 - x0) / n
    s = f(x0) + f(x1)
    for i in range(1, n):
        s += f(x0 + i * h) * (4 if i % 2 else 2)
    return s * h / 3.0


def run_quadrature(a0: float, lnm0: float, mu0: float, mu1: float, nf: int, loops: int, n: int = 2000):
    """Path 2 (independent): eliminate t.  t(a) = int da/beta(a); ln m = int (gamma/beta) da.

    The coupling at mu1 is found by bisection on t(a) - (t1 - t0); the mass follows from a
    single quadrature in the coupling.  No ODE stepping is shared with path 1.
    """
    if mu0 == mu1:
        return a0, lnm0
    dt = math.log(mu1**2) - math.log(mu0**2)

    def t_of(a: float) -> float:
        return _simpson(lambda x: 1.0 / _da(x, nf, loops), a0, a, n)

    # beta = da/dt < 0, so t(a) = int_{a0}^{a} dx/beta(x) is strictly decreasing in a
    # (positive for a < a0, negative for a > a0).  Bisect t(a) = dt.
    lo, hi = 0.2 * a0, 3.0 * a0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if t_of(mid) > dt:
            lo = mid
        else:
            hi = mid
    a1 = 0.5 * (lo + hi)
    lnm1 = lnm0 + _simpson(lambda x: _dlnm(x, nf, loops) / _da(x, nf, loops), a0, a1, n)
    return a1, lnm1


# Two-loop decoupling at mu = m_h(m_h), with the (nf)-flavour coupling a = alpha_s^(nf)/pi:
#   alpha^(nf-1) = alpha^(nf) (1 + 11/72 a^2),  m^(nf-1) = m^(nf) (1 + 89/432 a^2).
C2_ALPHA = 11.0 / 72.0
C2_MASS = 89.0 / 432.0
MZ = 91.1876


class Chain:
    """alpha_s^(5)(M_Z) -> nf=5 to mu_b=m_b -> decouple -> nf=4 (charm threshold is below 2 GeV)."""

    def __init__(self, as_mz: float, mb: float, loops: int = 4, integrator=run_rk4):
        self.loops, self.integ, self.mb = loops, integrator, mb
        a5, _ = integrator(as_mz / math.pi, 0.0, MZ, mb, 5, loops)
        self.a5_mb = a5
        self.a4_mb = a5 * (1.0 + C2_ALPHA * a5**2) if loops >= 3 else a5

    def alpha4(self, mu: float) -> float:
        a, _ = self.integ(self.a4_mb, 0.0, self.mb, mu, 4, self.loops)
        return a * math.pi


def common_scale_ratio(ms2: float, mb: float, as_mz: float, loops: int = 4, integrator=run_rk4) -> float:
    """R_common = m_s^(5)(mb)/m_b^(5)(mb), after nf=4 running and light-mass threshold matching."""
    ch = Chain(as_mz, mb, loops, integrator)
    a2, lm = integrator(ch.a4_mb, 0.0, mb, 2.0, 4, loops)  # a(2 GeV) and mass factor m(2)/m(mb)
    # Match the light strange mass UP to the same nf=5 theory as mb(mb).
    # RunDec Eq. (28): m_s^(4) = zeta_m m_s^(5), zeta_m = 1+89/432*a5^2.
    # Four-loop running with TWO-loop matching is a truncated diagnostic,
    # not a fully consistent four-loop + three-loop decoupling prediction.
    zeta_m = 1.0 + C2_MASS * ch.a5_mb**2 if loops >= 3 else 1.0
    transport = math.exp(lm) * zeta_m  # m_s^(4)(2 GeV)/m_s^(5)(mb)
    return ms2 / transport / mb, transport, a2 * math.pi, ch.a4_mb * math.pi


ALPHA_S_V = 0.103303816122
V_ATLAS = ALPHA_S_V / math.sqrt(6.0)
R_PRED = V_ATLAS ** 1.2


def miss(R: float) -> float:
    return R_PRED / R - 1.0


def exponent(R: float, V: float = V_ATLAS) -> float:
    return math.log(V) / math.log(R)


def bridge_needed_R(p: float) -> float:
    return V_ATLAS ** (1.0 / p)


# ---------------------------------------------------------------------------
# Part A - exact bookkeeping
# ---------------------------------------------------------------------------
def part_a() -> None:
    section("A. Exact bookkeeping (Fraction)")
    cf, tf = Fraction(4, 3), Fraction(1, 2)
    check("C_F - T_F = 5/6 and 1/(C_F - T_F) = 6/5", cf - tf == Fraction(5, 6) and 1 / (cf - tf) == Fraction(6, 5))
    # literature values quoted in RunDec-style tables for nf = 5 (a = alpha_s/pi normalisation)
    b0 = (Fraction(11) - Fraction(2, 3) * 5) / 4
    b1 = (Fraction(102) - Fraction(38, 3) * 5) / 16
    b2 = (Fraction(2857, 2) - Fraction(5033, 18) * 5 + Fraction(325, 54) * 25) / 64
    g1 = (Fraction(202, 3) - Fraction(20, 9) * 5) / 16
    check("beta_0(nf=5) = 23/12", b0 == Fraction(23, 12))
    check("beta_1(nf=5) = 29/12", b1 == Fraction(29, 12))
    check("beta_2(nf=5) = 9769/3456", b2 == Fraction(9769, 3456))
    check("gamma_1(nf=5) = 253/72 and gamma_1(nf=4) = 263/72",
          g1 == Fraction(253, 72) and (Fraction(202, 3) - Fraction(20, 9) * 4) / 16 == Fraction(263, 72))
    check("float coefficient tables agree with the Fractions (nf=5)",
          abs(beta_coeffs(5)[0] - 23 / 12) < 1e-12 and abs(beta_coeffs(5)[1] - 29 / 12) < 1e-12
          and abs(beta_coeffs(5)[2] - 9769 / 3456) < 1e-12 and abs(gamma_coeffs(5)[1] - 253 / 72) < 1e-12)
    print(f"  R_pred = [alpha_s(v)/sqrt6]^(6/5) = {R_PRED:.10f}   (alpha_s(v)={ALPHA_S_V}, V_atlas={V_ATLAS:.8f})")
    check("R_pred reproduces the repository comparator 0.0223897316",
          abs(R_PRED - 0.0223897316159) < 5e-12, f"{R_PRED:.13f}")


# ---------------------------------------------------------------------------
# Part B - the running engine
# ---------------------------------------------------------------------------
def part_b() -> None:
    section("B. Running engine: closed forms and an independent second path")
    # one loop closed forms: a(mu) = a0/(1 + b0 a0 ln(mu^2/mu0^2)), m ratio = (a/a0)^(g0/b0)
    a0, mu0, mu1, nf = 0.09, 4.183, 2.0, 4
    a1, lm1 = run_rk4(a0, 0.0, mu0, mu1, nf, 1)
    b0 = beta_coeffs(nf, 1)[0]
    a_exact = a0 / (1.0 + b0 * a0 * math.log(mu1**2 / mu0**2))
    lm_exact = (1.0 / b0) * math.log(a_exact / a0)
    check("one-loop coupling matches the closed form", abs(a1 - a_exact) < 1e-13, f"{a1:.12f} vs {a_exact:.12f}")
    check("one-loop mass factor matches (a/a0)^(gamma0/beta0)", abs(lm1 - lm_exact) < 1e-13,
          f"{math.exp(lm1):.10f}")
    # second path agreement, four loops
    ra, rm = run_rk4(0.0715, 0.0, 4.183, 2.0, 4, 4)
    qa, qm = run_quadrature(0.0715, 0.0, 4.183, 2.0, 4, 4)
    check("4-loop coupling: RK4 in ln mu^2 equals quadrature-in-coupling path", abs(ra - qa) < 1e-9,
          f"{ra:.11f} vs {qa:.11f}")
    check("4-loop mass factor: RK4 equals quadrature path", abs(rm - qm) < 1e-9,
          f"{math.exp(rm):.10f} vs {math.exp(qm):.10f}")
    # reversibility
    ua, um = run_rk4(ra, rm, 2.0, 4.183, 4, 4)
    check("running down and back up returns the start", abs(ua - 0.0715) < 1e-10 and abs(um) < 1e-10)
    # loop-order hierarchy of the coupling at 2 GeV from M_Z: monotone convergence
    vals = [Chain(0.1180, 4.183, L).alpha4(2.0) for L in (1, 2, 3, 4)]
    check("alpha_s^(4)(2 GeV) converges with loop order (|d3| < |d2|)",
          abs(vals[3] - vals[2]) < abs(vals[2] - vals[1]), "L1..L4 = " + ", ".join(f"{v:.4f}" for v in vals))
    ch = Chain(0.1180, 4.183)
    print(f"  alpha_s(M_Z)=0.1180 -> alpha_s^(5)(m_b)={ch.a5_mb*math.pi:.5f}, alpha_s^(4)(m_b)={ch.a4_mb*math.pi:.5f}, "
          f"alpha_s^(4)(2 GeV)={ch.alpha4(2.0):.5f}")
    check("alpha_s^(4)(2 GeV) lies in the standard 0.29-0.31 window",
          0.29 < ch.alpha4(2.0) < 0.31, f"{ch.alpha4(2.0):.5f}")


# ---------------------------------------------------------------------------
# Part C - R = m_s/m_b is scale-blind at fixed flavour number
# ---------------------------------------------------------------------------
def part_c() -> None:
    section("C. R = m_s/m_b does not run: a bridge on R needs one common scale")
    a0 = 0.30140 / math.pi
    ratios = []
    for mu in (4.183, 5.0, 10.0, 30.0, 91.1876, 1000.0):
        # both masses in the nf=5 theory above m_b, universal anomalous dimension
        _, l_s = run_rk4(a0, math.log(0.0785), 4.183, mu, 5, 4)
        _, l_b = run_rk4(a0, math.log(4.183), 4.183, mu, 5, 4)
        ratios.append(math.exp(l_s - l_b))
    spread = (max(ratios) - min(ratios)) / ratios[0]
    check("ln(m_s/m_b) is exactly constant under nf=5 running (universal gamma_m)", spread < 1e-12,
          f"spread={spread:.2e}")
    # the mixed ratio m_s(mu_s)/m_b(m_b) is not constant: logarithmic slope at 2 GeV
    ch = Chain(0.1180, 4.183)
    def mixed(mu_s: float) -> float:
        _, lm = run_rk4(ch.a4_mb, 0.0, 4.183, mu_s, 4, 4)     # m_s(mu_s)/m_s(m_b)
        return 0.0785 * math.exp(lm) / 4.183
    slope = (math.log(mixed(2.02)) - math.log(mixed(1.98))) / (math.log(2.02) - math.log(1.98))
    check("mixed ratio m_s(mu_s)/m_b(m_b) has slope d ln R/d ln mu_s ~ -0.28 at 2 GeV",
          -0.30 < slope < -0.26, f"slope={slope:.4f}")
    print(f"  => 1% in the mixed ratio corresponds to {1.0/abs(slope):.1f}% in the strange-mass scale.")


# ---------------------------------------------------------------------------
# Part D - the common-scale miss and the needed exponent (PDG 2024)
# ---------------------------------------------------------------------------
PDG24 = dict(ms2=0.0935, mb=4.183, as_mz=0.1180)
PDG24_ERR = dict(ms2=0.0008, mb=0.007, as_mz=0.0009)


def part_d() -> dict:
    section("D. Common nf=5 scale: four-loop QCD running, two-loop matching, PDG 2024 inputs")
    R, T, a2, ab = common_scale_ratio(**PDG24)
    Rq, Tq, _, _ = common_scale_ratio(**PDG24, integrator=run_quadrature)
    print(f"  alpha_s^(4)(2 GeV)={a2:.5f}, alpha_s^(4)(m_b)={ab:.5f}, transport m_s(2 GeV)/m_s(m_b)={T:.5f}")
    print(f"  m_s(m_b) = {1000*PDG24['ms2']/T:.2f} MeV;  R_common = m_s(m_b)/m_b(m_b) = {R:.6f}  (1/R = {1/R:.2f})")
    check("second integration path reproduces R_common", abs(R - Rq) / R < 1e-8, f"{R:.8f} vs {Rq:.8f}")
    m = miss(R)
    print(f"  R_pred/R_common - 1 = {100*m:+.2f}%")
    check("common-scale miss with two-loop matching is about +18.7% (18.4% to 18.8%)", 0.184 < m < 0.188, f"{100*m:+.3f}%")
    check("the miss exceeds the repository one-loop value +15.5%", m > 0.155)
    mixed = R_PRED / (PDG24["ms2"] / PDG24["mb"]) - 1.0
    mixed_notes = R_PRED / (93.4e-3 / 4.180) - 1.0
    check("the notes' comparator 93.4 MeV / 4.180 GeV reproduces their +0.20% (+0.2024%)",
          abs(mixed_notes - 0.002024) < 2e-5, f"{100*mixed_notes:+.4f}%")
    check("with PDG 2024 central values the mixed-scale ratio m_s(2 GeV)/m_b(m_b) also gives |miss| < 0.5%",
          abs(mixed) < 0.005, f"{100*mixed:+.3f}%")
    print(f"  mixed-scale comparator {PDG24['ms2']/PDG24['mb']:.6f}; bridge misses it by {100*mixed:+.2f}%")
    p = exponent(R)
    print(f"  exponent needed: p = ln V / ln R_common = {p:.4f}   (5/6 = {5/6:.4f})")
    check("needed exponent on the common surface is about 0.7973 within 0.001", abs(p - 0.7975) < 0.001, f"{p:.5f}")
    check("needed exponent differs from 5/6 by more than 0.03", abs(p - 5 / 6) > 0.03)
    c = V_ATLAS / R ** (5 / 6)
    print(f"  prefactor needed at exponent 5/6: c = V/R^(5/6) = {c:.4f}")
    check("prefactor needed at exponent 5/6 is 1.15 (1.14 to 1.17)", 1.14 < c < 1.17, f"{c:.4f}")
    # linear error propagation
    var_miss = 0.0
    for key in ("ms2", "mb", "as_mz"):
        up = dict(PDG24); dn = dict(PDG24)
        up[key] += PDG24_ERR[key]; dn[key] -= PDG24_ERR[key]
        d = 0.5 * (miss(common_scale_ratio(**up)[0]) - miss(common_scale_ratio(**dn)[0]))
        var_miss += d * d
    sigma = math.sqrt(var_miss)
    z = m / sigma
    print(f"  linear error propagation (ms 0.8 MeV, mb 7 MeV, alpha_s(MZ) 0.0009): miss = {100*m:+.2f}% +- {100*sigma:.2f}%  -> {z:.1f} combined quoted-error units (not significance)")
    check("miss exceeds 15 combined quoted-error halfwidth units (mass errors are 90% CL, alpha error 68%; atlas V_cb exact)", z > 15.0, f"{z:.1f} combined quoted-error units (not significance)")
    # loop-order table
    seq = []
    for L in (1, 2, 3, 4):
        RL = common_scale_ratio(**PDG24, loops=L)[0]
        seq.append(miss(RL))
    print("  miss by loop order (1..4): " + ", ".join(f"{100*x:+.1f}%" for x in seq))
    check("loop order does not rescue the bridge: every order gives at least +11%", min(seq) > 0.11)
    check("miss grows monotonically with loop order (1..4)", all(seq[i] < seq[i + 1] for i in range(3)))
    # repository one-loop-style transport: m_s(m_b) = 81.0 MeV
    print(f"  repository comparator m_s(m_b)=81.0 MeV -> transport {93.4/81.0:.5f}; four-loop running of 93.4 MeV gives {common_scale_ratio(0.0934, 4.180, 0.1180)[1]:.5f}")
    check("repository m_s(m_b)=81.0 MeV is not reproduced by four-loop running of m_s(2 GeV)=93.4 MeV",
          not (80.0 < 93.4 / common_scale_ratio(0.0934, 4.180, 0.1180)[1] < 82.0),
          f"{93.4/common_scale_ratio(0.0934, 4.180, 0.1180)[1]:.2f} MeV")
    return dict(R=R, p=p)


# ---------------------------------------------------------------------------
# Part E - other standard inputs, and no running at all
# ---------------------------------------------------------------------------
INPUT_SETS = [
    ("PDG24 listing (93.5, 4.183)", 0.0935, 4.183, 0.1180),
    ("PDG24 lattice-only m_s (92.74, 4.183)", 0.09274, 4.183, 0.1180),
    ("FLAG24 Nf=2+1+1 (93.46, 4.200)", 0.09346, 4.200, 0.1180),
    ("FLAG24 Nf=2+1 (92.4, 4.171)", 0.0924, 4.171, 0.1180),
    ("FLAG24 2+1+1, alpha_s(MZ)=0.1184", 0.09346, 4.200, 0.1184),
    ("high-side corner (94.3, 4.176, 0.1171)", 0.0943, 4.176, 0.1171),
    ("low-side corner (92.7, 4.190, 0.1189)", 0.0927, 4.190, 0.1189),
]


def part_e() -> None:
    section("E. Supplied input sensitivities; FLAG flavour conventions not rematched; no-running lattice chain")
    misses = []
    for name, ms2, mb, a in INPUT_SETS:
        R = common_scale_ratio(ms2, mb, a)[0]
        m = miss(R)
        misses.append(m)
        print(f"  {name:44s} R={R:.6f}  miss={100*m:+.2f}%  p={exponent(R):.4f}")
    check("every supplied diagnostic tuple misses by 16% to 21% (FLAG nf conventions not fully rematched)", all(0.16 < m < 0.21 for m in misses),
          f"range {100*min(misses):+.1f}% .. {100*max(misses):+.1f}%")
    check("no standard input set gets the exponent within 0.03 of 5/6",
          all(abs(exponent(common_scale_ratio(ms2, mb, a)[0]) - 5 / 6) > 0.03 for _, ms2, mb, a in INPUT_SETS))
    # lattice chain: R = 1/[(m_b/m_c)(m_c/m_s)], both ratios at one scale, so no running enters
    bc, cs = 4.578, 11.766
    R_flag = 1.0 / (bc * cs)
    m_flag = miss(R_flag)
    print(f"  FLAG 2024 chain: m_b/m_s = {bc*cs:.2f}, R = {R_flag:.6f}, miss = {100*m_flag:+.2f}%, p = {exponent(R_flag):.4f}")
    check("lattice mass-ratio chain (no running, no 2 GeV convention) misses by +20.6% (20.4% to 20.8%)",
          0.204 < m_flag < 0.208, f"{100*m_flag:+.3f}%")
    # the atlas |V_cb| = 0.04217 sits at the inclusive end of the measured range; test the measured values too
    R = common_scale_ratio(**PDG24)[0]
    rows = [(V, V**1.2 / R - 1.0, exponent(R, V)) for V in (0.0392, 0.0410, 0.0422)]
    for V, m, p in rows:
        print(f"  measured-style |V_cb|={V:.4f}: V^(6/5)/R_common - 1 = {100*m:+.1f}%, exponent p = {p:.4f}")
    check("against |V_cb| = 0.0392 / 0.0410 / 0.0422 the common-scale miss is +8.6% / +14.6% / +18.7% (each within 0.3%)",
          all(abs(m - t) < 0.003 for (_, m, _), t in zip(rows, (0.086, 0.146, 0.187))))
    check("the exponent stays above 0.79 and below 0.82 for every measured |V_cb| (never 5/6)",
          all(0.79 < p < 0.82 for _, _, p in rows))
    V_need = R ** (5 / 6)
    print(f"  |V_cb| needed for an exact 5/6 on the common surface: {V_need:.4f}")
    check("exact 5/6 on the common surface needs |V_cb| = 0.0366, below every measured value 0.039-0.042",
          abs(V_need - 0.0366) < 0.0002 and V_need < 0.039, f"{V_need:.5f}")


# ---------------------------------------------------------------------------
# Part F - what the +0.2% needs
# ---------------------------------------------------------------------------
def part_f() -> None:
    section("F. The +0.2% needs a strange-mass scale of 1.99 GeV")
    ch = Chain(0.1180, 4.183)
    ms2, mb = PDG24["ms2"], PDG24["mb"]

    def mixed(mu_s: float) -> float:
        # strange mass at mu_s from 2 GeV in the nf=4 theory (mu_s >= 1.3 GeV: charm threshold below)
        a2 = ch.alpha4(2.0) / math.pi
        _, lm = run_rk4(a2, 0.0, 2.0, mu_s, 4, 4)
        return ms2 * math.exp(lm) / mb

    def root(target: float) -> float:
        lo, hi = 1.3, 8.0
        if not mixed(lo) >= target >= mixed(hi):
            raise ValueError("no root in nf=4 domain [1.3,8] GeV; charm matching below it is not implemented")
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if mixed(mid) > target:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    for p_txt, p in (("4/5", 0.8), ("5/6", 5 / 6), ("6/7", 6 / 7), ("8/9", 8 / 9)):
        try:
            mu = root(bridge_needed_R(p))
        except ValueError as exc:
            print(f"  exponent {p_txt}: UNTESTED outside bracket: {exc}")
            continue
        print(f"  exponent {p_txt}: m_s(mu_s)/m_b(m_b) = V^(1/p) at mu_s = {mu:.3f} GeV")
    mu56 = root(R_PRED)
    check("exponent 5/6 fits the mixed ratio only at mu_s = 1.99 GeV (1.95 to 2.03)", 1.95 < mu56 < 2.03,
          f"{mu56:.3f} GeV")
    check("exponent 4/5 would fit at mu_s ~ 3.9 GeV, so the '2 GeV' surface is not singled out by the data alone",
          3.5 < root(bridge_needed_R(0.8)) < 4.3, f"{root(bridge_needed_R(0.8)):.3f} GeV")


# ---------------------------------------------------------------------------
# Part G - downstream ratios that used the mixed-scale comparator
# ---------------------------------------------------------------------------
def part_g() -> None:
    section("G. Downstream quantities built on the mixed-scale comparator")
    # The repository's own comparator values: m_d = 4.67 MeV, m_s = 93.4 MeV (both at 2 GeV), m_b(m_b) = 4.180 GeV.
    Rc = common_scale_ratio(0.0934, 4.180, 0.1180)[0]
    r12_obs = 4.67 / 93.4                       # both masses at 2 GeV: scale-blind
    r12_pred = ALPHA_S_V / 2.0
    check("m_d/m_s (both at 2 GeV) keeps its +3.3%: it needs no scale convention",
          abs(r12_pred / r12_obs - 1.0 - 0.0330) < 5e-4, f"{100*(r12_pred/r12_obs-1):+.2f}%")
    chain_pred = r12_pred * R_PRED
    mixed = chain_pred / (4.67 / 4180.0) - 1.0
    common = chain_pred / (r12_obs * Rc) - 1.0
    print(f"  m_d/m_b: prediction {chain_pred:.6f}; mixed-scale comparator 4.67/4180 -> {100*mixed:+.2f}%; "
          f"common-scale comparator (m_d/m_s)_obs R_common = {r12_obs*Rc:.6f} -> {100*common:+.2f}%")
    check("m_d/m_b: the mixed-scale +3.5% becomes +22.5% at one common scale", abs(mixed - 0.0351) < 5e-4
          and abs(common - 0.2255) < 2e-3, f"mixed {100*mixed:+.2f}%, common {100*common:+.2f}%")
    # up-type partition f_23 = sqrt((m_s/m_b)^(5/3)_obs)/|V_cb| used the mixed comparator
    f_mixed = math.sqrt((93.4 / 4180.0) ** (5.0 / 3.0)) / V_ATLAS
    f_common = math.sqrt(Rc ** (5.0 / 3.0)) / V_ATLAS
    print(f"  up-type partition f_23: mixed comparator {f_mixed:.4f}, common-scale comparator {f_common:.4f}")
    check("f_23 = 0.9983 is reproduced on the mixed comparator (the '2-3 down-dominant at 0.2%' figure)",
          abs(f_mixed - 0.9983) < 5e-4, f"{f_mixed:.5f}")
    check("on one common scale f_23 = 0.867: the '0.2% saturation of |V_cb|^2' is an artefact of the mixed comparator",
          abs(f_common - 0.867) < 0.003, f"{f_common:.4f}")


# ---------------------------------------------------------------------------
# Part H - one-loop SM Yukawa running up to the Planck scale
# ---------------------------------------------------------------------------
def part_h(R0: float) -> None:
    section("H. One-loop Standard-Model running of the Yukawa matrices to M_Pl")
    import numpy as np

    MPL = 1.220890e19
    MT = 163.0
    KPI = 1.0 / (16.0 * math.pi**2)

    def ckm_matrix(s12, s23, s13, d):
        c12, c23, c13 = (math.sqrt(1 - x * x) for x in (s12, s23, s13))
        e = np.exp(1j * d)
        return np.array([
            [c12 * c13, s12 * c13, s13 / e],
            [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13],
        ])

    def pack(Hu, Hd, g):
        return np.concatenate([Hu.real.ravel(), Hu.imag.ravel(), Hd.real.ravel(), Hd.imag.ravel(), g])

    def unpack(y):
        return ((y[0:9] + 1j * y[9:18]).reshape(3, 3), (y[18:27] + 1j * y[27:36]).reshape(3, 3), y[36:39])

    b1 = np.array([41 / 10, -19 / 6, -7.0])

    def rhs(t, y, ytau2):
        Hu, Hd, g = unpack(y)
        g1, g2, g3 = g
        T = (3 * np.trace(Hu) + 3 * np.trace(Hd)).real + ytau2
        Gu = 17 / 20 * g1**2 + 9 / 4 * g2**2 + 8 * g3**2
        Gd = 1 / 4 * g1**2 + 9 / 4 * g2**2 + 8 * g3**2
        dHu = KPI * (3 * Hu @ Hu - 1.5 * (Hd @ Hu + Hu @ Hd) + 2 * (T - Gu) * Hu)
        dHd = KPI * (3 * Hd @ Hd - 1.5 * (Hu @ Hd + Hd @ Hu) + 2 * (T - Gd) * Hd)
        dg = KPI * b1 * g**3
        return pack(dHu, dHd, dg)

    def rk4(y, t0, t1, steps, ytau2):
        h = (t1 - t0) / steps
        t = t0
        out = [(t, y.copy())]
        for _ in range(steps):
            k1 = rhs(t, y, ytau2)
            k2 = rhs(t + h / 2, y + h / 2 * k1, ytau2)
            k3 = rhs(t + h / 2, y + h / 2 * k2, ytau2)
            k4 = rhs(t + h, y + h * k3, ytau2)
            y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += h
            out.append((t, y.copy()))
        return out

    def observables(Hu, Hd):
        wu, Uu = np.linalg.eigh(Hu)
        wd, Ud = np.linalg.eigh(Hd)
        V = np.abs(Uu.conj().T @ Ud)
        return wu, wd, V

    def build(V_cb, R_msmb, yt=0.9369):
        # SM inputs at mu = m_t = 163 GeV (MS-bar): y_t = 0.9369, g' = 0.3583 (g1 = sqrt(5/3) g'),
        # g2 = 0.6478, g3 = 1.1666 (Buttazzo et al., JHEP 12 (2013) 089).  Comparators; the result
        # is insensitive to them (see the y_t variants below).
        vev = 246.22
        yb = math.sqrt(2) * 2.73 / vev
        ys = R_msmb * yb
        yc = math.sqrt(2) * 0.62 / vev
        yu, yd = 6.0e-6, 1.3e-5
        Hu = np.diag([yu**2, yc**2, yt**2]).astype(complex)
        Vk = ckm_matrix(0.22501, V_cb, 0.00369, 1.144)
        Hd = Vk @ np.diag([yd**2, ys**2, yb**2]).astype(complex) @ Vk.conj().T
        g = np.array([0.4626, 0.6478, 1.1666])
        return Hu, Hd, g

    ytau2 = (math.sqrt(2) * 1.7 / 246.22) ** 2
    Hu, Hd, g = build(V_ATLAS, R0)
    wu, wd, V = observables(Hu, Hd)
    check("initial condition reproduces V_cb and m_s/m_b", abs(V[1, 2] - V_ATLAS) < 1e-6
          and abs(math.sqrt(wd[1] / wd[2]) - R0) / R0 < 1e-6, f"V_cb={V[1,2]:.6f}, R={math.sqrt(wd[1]/wd[2]):.6f}")
    y0 = pack(Hu, Hd, g)
    path = rk4(y0, 0.0, math.log(MPL / MT), 3000, ytau2)
    ps, rows = [], []
    for t, y in path[::300] + [path[-1]]:
        Hu_t, Hd_t, g_t = unpack(y)
        wu_t, wd_t, V_t = observables(Hu_t, Hd_t)
        Vcb, R = V_t[1, 2], math.sqrt(wd_t[1] / wd_t[2])
        ps.append(math.log(Vcb) / math.log(R))
        rows.append((MT * math.exp(t), math.sqrt(wu_t[2]), Vcb, R, ps[-1]))
    for mu, yt, Vcb, R, p in rows:
        print(f"  mu={mu:10.3e} GeV  y_t={yt:.4f}  V_cb={Vcb:.5f}  m_s/m_b={R:.6f}  p={p:.4f}")
    Vend, Rend = rows[-1][2], rows[-1][3]
    check("running V_cb and m_s/m_b rise by the same factor (equal to 0.1%), as the top-Yukawa flow predicts",
          abs((Vend / V_ATLAS) / (Rend / R0) - 1.0) < 1e-3, f"{Vend/V_ATLAS:.4f} vs {Rend/R0:.4f}")
    check("needed exponent stays within 0.788-0.798 at the sampled scales of the supplied truncated one-loop SM flow", all(0.788 < p < 0.798 for p in ps),
          f"p from {ps[0]:.4f} to {ps[-1]:.4f}")
    check("sampled exponents stay at least 0.035 from 5/6; no continuous all-scale bound is tested", all(abs(p - 5 / 6) > 0.035 for p in ps))
    check("it moves toward smaller p as mu rises (the wrong direction for 5/6)", ps[-1] < ps[0])

    def p_at_planck(V_cb, R_msmb, yt):
        H1, H2, g0 = build(V_cb, R_msmb, yt)
        end = rk4(pack(H1, H2, g0), 0.0, math.log(MPL / MT), 1500, ytau2)[-1][1]
        a, b, _ = unpack(end)
        _, wd_e, V_e = observables(a, b)
        return math.log(V_e[1, 2]) / math.log(math.sqrt(wd_e[1] / wd_e[2]))

    variants = [("y_t(m_t) = 0.9269", V_ATLAS, R0, 0.9269), ("y_t(m_t) = 0.9469", V_ATLAS, R0, 0.9469),
                ("|V_cb| = 0.0392 (exclusive-like)", 0.0392, R0, 0.9369)]
    pv = []
    for name, Vv, Rv, ytv in variants:
        pv.append(p_at_planck(Vv, Rv, ytv))
        print(f"  variant {name:34s} p(M_Pl) = {pv[-1]:.4f}")
    check("y_t(m_t) = 0.9269 and 0.9469 leave p(M_Pl) within 0.788-0.794", all(0.788 < x < 0.794 for x in pv[:2]),
          f"{pv[0]:.4f}, {pv[1]:.4f}")
    check("with |V_cb| = 0.0392 the exponent at M_Pl is still 0.80-0.82, not 5/6", 0.80 < pv[2] < 0.82,
          f"{pv[2]:.4f}")


def main() -> int:
    print("COMMON-SCALE FOUR-LOOP CHECK OF THE DOWN-TYPE FIVE-SIXTHS BRIDGE (comparator correction)")
    part_a()
    part_b()
    part_c()
    res = part_d()
    part_e()
    part_f()
    part_g()
    part_h(res["R"])
    print()
    print("=" * 64)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("Comparator content only: the runner derives no mass, exponent or scale.")
    print("=" * 64)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
