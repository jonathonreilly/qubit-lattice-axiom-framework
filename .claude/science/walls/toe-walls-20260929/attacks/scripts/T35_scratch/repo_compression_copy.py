#!/usr/bin/env python3
"""How much does the uncontrolled P1/Δ_R matching error at M_Pl actually move m_t?

Memory-safe: a single 1-D SM RGE integration (4 couplings), no quadratures.

Chain (the framework's own): set y_t(M_Pl) = g3(M_Pl)/sqrt(6) * (1 + Δ_R), run
the SM down 17 decades to m_t via the top-Yukawa RGE (IR quasi-fixed point), read
m_t = y_t(m_t) * v / sqrt(2). Vary Δ_R over the corrected uncontrolled range and
report the compression: how a high-scale matching error propagates to m_t.

1-loop SM RGEs (GUT-normalised g1 = sqrt(5/3) g_Y), y_b,y_tau neglected:
  dg_i/dt = b_i g_i^3 / (16π²),   b = (41/10, -19/6, -7)
  dy_t/dt = y_t/(16π²) [ 9/2 y_t² - 17/20 g1² - 9/4 g2² - 8 g3² ],   t = ln μ
This is enough for the SENSITIVITY (compression) even if the absolute m_t needs
2-loop + thresholds + pole conversion.
"""
from __future__ import annotations
import math
from scipy.integrate import solve_ivp

PI = math.pi
K = 1.0 / (16.0 * PI * PI)
MZ = 91.1876
MPL = 1.221e19
V = 246.22
POLE_FACTOR = 1.019
SQRT6 = math.sqrt(6.0)
B = (41.0/10.0, -19.0/6.0, -7.0)

# gauge couplings at M_Z (GUT-normalised g1)
ALPHA_EM = 1.0/127.95
SIN2W = 0.23122
ALPHA3 = 0.1181
g3_MZ = math.sqrt(4*PI*ALPHA3)
alpha2 = ALPHA_EM/SIN2W
g2_MZ = math.sqrt(4*PI*alpha2)
alpha1 = (5.0/3.0)*ALPHA_EM/(1.0-SIN2W)
g1_MZ = math.sqrt(4*PI*alpha1)


def gauge_rhs(t, y):
    g1, g2, g3 = y
    return [B[0]*g1**3*K, B[1]*g2**3*K, B[2]*g3**3*K]


def full_rhs(t, y):
    g1, g2, g3, yt = y
    dg = [B[0]*g1**3*K, B[1]*g2**3*K, B[2]*g3**3*K]
    dyt = yt*K*(4.5*yt*yt - 0.85*g1*g1 - 2.25*g2*g2 - 8.0*g3*g3)
    return dg + [dyt]


def run_gauge_up():
    t0, t1 = math.log(MZ), math.log(MPL)
    sol = solve_ivp(gauge_rhs, [t0, t1], [g1_MZ, g2_MZ, g3_MZ],
                    rtol=1e-9, atol=1e-12, dense_output=True)
    return sol.y[:, -1]  # g1,g2,g3 at M_Pl


def mt_from_delta(gMPl, delta, mt_scale=173.0):
    g1P, g2P, g3P = gMPl
    yt_MPl = (g3P/SQRT6)*(1.0+delta)
    t0, t1 = math.log(MPL), math.log(mt_scale)
    sol = solve_ivp(full_rhs, [t0, t1], [g1P, g2P, g3P, yt_MPl],
                    rtol=1e-9, atol=1e-12, dense_output=True)
    yt_mt = sol.y[3, -1]
    return yt_mt * V / math.sqrt(2.0), yt_MPl, yt_mt


def mt_from_yt_MPl(gMPl, yt_MPl, mt_scale=173.0):
    g1P, g2P, g3P = gMPl
    t0, t1 = math.log(MPL), math.log(mt_scale)
    sol = solve_ivp(full_rhs, [t0, t1], [g1P, g2P, g3P, yt_MPl],
                    rtol=1e-9, atol=1e-12, dense_output=True)
    return sol.y[3, -1] * V / math.sqrt(2.0)


def report_boundary(gMPl, label, gs_MPl):
    """Compression for boundary y_t(M_Pl) = gs_MPl/sqrt(6)*(1+Δ_R)."""
    yt0 = gs_MPl / SQRT6
    base = mt_from_yt_MPl(gMPl, yt0)
    print(f"\n  [{label}]  g_s(M_Pl)={gs_MPl:.3f} -> y_t(M_Pl)={yt0:.4f} -> "
          f"base m_t={base:.1f} GeV")
    print(f"    Δ_R    y_t(M_Pl)   m_t [GeV]   Δm_t/m_t")
    points = {}
    for d in [-0.50, -0.30, 0.0, 0.30, 0.50]:
        mt = mt_from_yt_MPl(gMPl, yt0*(1+d))
        points[d] = mt
        print(f"   {d:+5.2f}    {yt0*(1+d):.4f}    {mt:7.1f}    {(mt-base)/base*100:+6.1f}%")
    mtp = mt_from_yt_MPl(gMPl, yt0*1.05)
    mtm = mt_from_yt_MPl(gMPl, yt0*0.95)
    sens = ((mtp-mtm)/base)/0.10
    mt50 = mt_from_yt_MPl(gMPl, yt0*1.50)
    print(f"    sensitivity d ln m_t / d Δ_R ~ {sens:.2f}  =>  "
          f"+50% matching -> {(mt50-base)/base*100:+.0f}% in m_t")
    print(f"    pole-converted Δ_R ±50% range (+1.9%): "
          f"{points[-0.50]*POLE_FACTOR:.1f}..{points[0.50]*POLE_FACTOR:.1f} GeV")
    return {
        "sens": sens,
        "base_msbar": base,
        "low_pole": points[-0.50] * POLE_FACTOR,
        "high_pole": points[0.50] * POLE_FACTOR,
    }


def require(name, condition, detail):
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    print(f"  [PASS] {name}: {detail}")


def main():
    print("="*68)
    print("m_t compression of the P1/Δ_R matching error (memory-safe SM RGE)")
    print("="*68)
    gMPl = run_gauge_up()
    print(f"  couplings at M_Pl: g1={gMPl[0]:.4f} g2={gMPl[1]:.4f} g3={gMPl[2]:.4f}")
    g_LM = math.sqrt(4*PI*0.09067)
    print(f"  continuum g3(M_Pl)={gMPl[2]:.3f}; canonical g_LM=√(4π·α_LM)={g_LM:.3f}")
    s1 = report_boundary(gMPl, "scenario A: g_s = continuum g3(M_Pl)", gMPl[2])
    s2 = report_boundary(gMPl, "scenario B: g_s = canonical g_LM (reproduces m_t)", g_LM)
    print("\n" + "="*68)
    print(f"  COMPRESSION is WEAK in both: sensitivity ~{min(s1['sens'],s2['sens']):.2f}-{max(s1['sens'],s2['sens']):.2f}")
    print("  (framework high-scale y_t sits BELOW the fixed-point trap y_t*~0.65,")
    print("   so the IR quasi-fixed point does NOT strongly compress).")
    print("  => uncontrolled O(50%) matching maps to ~tens-of-% in m_t; NOT ~few%.")
    require(
        "canonical compression is weak",
        0.30 < s2["sens"] < 0.60,
        f"d ln m_t / d Δ_R = {s2['sens']:.3f}",
    )
    require(
        "canonical pole range remains broad",
        s2["low_pole"] < 120.0 and s2["high_pole"] > 190.0,
        f"Δ_R ±50% -> pole range {s2['low_pole']:.1f}..{s2['high_pole']:.1f} GeV",
    )
    require(
        "baseline reproduces the top scale at one-loop sensitivity level",
        165.0 < s2["base_msbar"] < 172.0,
        f"MSbar baseline = {s2['base_msbar']:.1f} GeV",
    )
    print("="*68)


if __name__ == "__main__":
    main()
