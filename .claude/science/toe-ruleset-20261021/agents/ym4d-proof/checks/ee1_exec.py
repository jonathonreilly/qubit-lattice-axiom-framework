#!/usr/bin/env python3 -I
"""ee1_exec.py -- EPS1_EXEC (target T55-B) numeric checks.

Criteria pre-registered in checks/ee1_criteria.md BEFORE this file existed.
Exact Fraction arithmetic; Decimal only to display. No numpy, no BLAS, no lock.
Every transcribed constant carries its file:line in the comment beside it.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 50


def D(x):
    """Exact Fraction -> Decimal, for display only."""
    return Decimal(x.numerator) / Decimal(x.denominator)


def log10(x):
    """log10 of a positive Fraction, via Decimal at the ambient precision."""
    return D(x).log10()


def dec(a, b):
    """decades from a down to b (positive when b < a)."""
    return log10(a) - log10(b)


# ---------------------------------------------------------------- transcriptions
# every one of these is quoted in ee1_criteria.md with its file:line
E_OLD_PRE = F(12687, 10) * F(10) ** -39      # 1.2687e-39  REVIEW_SF_S7 l.196 / SF l.2837 / NORMS l.746
E_RERUN_PRE = F(952, 100) * F(10) ** -40     # 9.52e-40    RLARGE l.71 / REVIEW_SF_S7 l.53,247
E_OLD_TB = F(895, 100) * F(10) ** -40        # 8.95e-40    REVIEW_SF_S7 l.47,200,297 / RLARGE l.611
E_RERUN_TB = F(67, 10) * F(10) ** -40        # 6.7e-40     RLARGE l.72,612  <- claimed in force

TB1 = F(7056, 10000)                         # 0.7056      REVIEW_SF_S7 l.199-200
CLASS = F(75, 100)                           # x0.75       REVIEW_SF_S7 l.251

E_PROP = F(938495112638, 10 ** 11) * F(10) ** -45   # 9.38495112638e-45  EPS1_SWEEP 4.5
E_TAUFLAT = F(938496, 10 ** 5) * F(10) ** -45       # 9.38496e-45        TAUFLAT l.408
ETA_FLAT = F(352310, 10 ** 5) * F(10) ** -88        # 3.52310e-88        TAUFLAT l.196,213
C3 = F(1)                                           # reference          TAUFLAT l.211

PREF_CERR = F(331, 100) * F(10) ** 7         # 3.31e7      TAUFLAT l.372,567
CB_OVER_CP4 = F(53) ** 4 * F(640)            # 5.04991e9   TAUFLAT l.204 (= C'^4/c_b)
STRENGTH = F(142125)                         # 2*sqrt(C'^4/c_b)  TAUFLAT l.205
CD_BAND_HI = F(9, 10) * F(10) ** 3           # 0.9e3       S4-16 via TAUFLAT l.182

CT_ROW = {  # EPSSTAR l.547-553
    10: F(2463, 1000) * F(10) ** 13,
    11: F(9774, 1000) * F(10) ** 12,
    12: F(5288, 1000) * F(10) ** 12,
    16: F(2031, 1000) * F(10) ** 12,
    24: F(1528, 1000) * F(10) ** 12,
    32: F(1454, 1000) * F(10) ** 12,
    100: F(1396, 1000) * F(10) ** 12,
}
CT_NO_H2 = F(805, 100) * F(10) ** 15         # 8.05e15     EPSSTAR l.590
CT_Q8 = F(127, 100) * F(10) ** 14            # 1.27e14     HANDOFF critical path item 4

N, L, A_D = 2, 3, 9                          # RLARGE l.1009 fixes 512*N*A_d = 4608N at d=4,L=3
C1_KN = F(1, 117)                            # c_1 = 1/(2(L^2+5.5A_d)) = 1/117   EXISTENCE l.1771
G_DX = F(157, 100) * F(10) ** -76            # 1.57e-76/sqrt(C_Omega), at C_Omega=1  REVIEW_SF_S7 l.204

out = []


def say(s=""):
    out.append(s)


# ---------------------------------------------------------------- ee1-1  (C6)
say("=" * 78)
say("ee1-1  (C6): do the four live eps_1 values factorise on two named axes?")
say("=" * 78)


def factorise(tb1_factor, label):
    """Predict the 2x2 table from the single base E_OLD_PRE and two transcribed factors."""
    cells = {
        ("old", "pre"): (E_OLD_PRE, F(1)),
        ("old", "TB1"): (E_OLD_TB, tb1_factor),
        ("rerun", "pre"): (E_RERUN_PRE, CLASS),
        ("rerun", "TB1"): (E_RERUN_TB, CLASS * tb1_factor),
    }
    worst = F(1)
    rows = []
    for (cls, corr), (recorded, fac) in cells.items():
        pred = E_OLD_PRE * fac
        ratio = pred / recorded
        rows.append((cls, corr, recorded, pred, ratio))
        dev = ratio if ratio >= 1 else 1 / ratio
        worst = max(worst, dev)
    verdict = "FACTORISES" if worst <= F(101, 100) else "DOES-NOT-FACTORISE"
    say("")
    say(f"-- {label}: TB-1 factor = {D(tb1_factor)}")
    say(f"{'class':8s} {'corr':5s} {'recorded':>16s} {'predicted':>16s} {'ratio':>12s}")
    for cls, corr, rec, pred, ratio in rows:
        say(f"{cls:8s} {corr:5s} {D(rec):16.6E} {D(pred):16.6E} {D(ratio):12.6f}")
    say(f"worst deviation = x{D(worst):.6f}   ->  {verdict}")
    return verdict


v_main = factorise(TB1, "MAIN")
v_ctrl = factorise(F(1, 2), "DESIGNED-FAIL CONTROL (TB-1 replaced by 1/2)")
say("")
say(f"ee1-1 MAIN    : {v_main}")
say(f"ee1-1 CONTROL : {v_ctrl}  (criteria require DOES-NOT-FACTORISE)")
say("ee1-1 POWER   : " + ("HAS-POWER" if v_ctrl == "DOES-NOT-FACTORISE" else "NO POWER"))
say("")
say("Cross-check, independent of the above: the TB-1 factor 0.7056 decomposes as")
say("  1/sqrt(2) (from a_c = a_p/2, REVIEW_SF_S7 l.199) times a small n_K correction.")
inv_sqrt2 = F(1)
# exact: compare 0.7056 with 1/sqrt(2) using squares, no floating sqrt
say(f"  0.7056^2 = {D(TB1 ** 2):.8f}   vs   1/2 = 0.50000000")
say(f"  ratio (0.7056^2)/(1/2) = {D(TB1 ** 2 * 2):.8f}  -> the n_K term costs this much in a_p units")

# ---------------------------------------------------------------- ee1-2  (C4)
say("")
say("=" * 78)
say("ee1-2  (C4): rounding direction, and what the value is a function of")
say("=" * 78)


def clause_holds(e1):
    """DESC-eps (iii) size clause: 4*C_3*eps_1^2 <= eta_flat."""
    return 4 * C3 * e1 * e1 <= ETA_FLAT


say("")
say("(a) rounding direction, clause 4*C_3*eps_1^2 <= eta_flat, C_3 = 1")
for nm, v in (("proposed  9.38495112638e-45", E_PROP),
              ("TAUFLAT   9.38496e-45      ", E_TAUFLAT),
              ("CONTROL   9.3850e-45       ", F(93850, 10 ** 4) * F(10) ** -45)):
    lhs = 4 * C3 * v * v
    say(f"  {nm}: 4C_3 eps^2 = {D(lhs):.10E}  {'<=' if clause_holds(v) else ' >'} "
        f"eta_b = {D(ETA_FLAT):.10E}   {'HOLDS' if clause_holds(v) else 'FAILS'}")

if clause_holds(E_PROP) and not clause_holds(E_TAUFLAT):
    v2a = "SAFE-SIDE"
elif not clause_holds(E_PROP):
    v2a = "UNSAFE-SIDE"
else:
    v2a = "NO-DISCRIMINATION"
ctrl2a = "UNSAFE-SIDE" if not clause_holds(F(93850, 10 ** 4) * F(10) ** -45) else "NOT-UNSAFE"
say(f"ee1-2(a) MAIN    : {v2a}")
say(f"ee1-2(a) CONTROL : {ctrl2a}  (criteria require UNSAFE-SIDE)")
say("ee1-2(a) POWER   : " + ("HAS-POWER" if ctrl2a == "UNSAFE-SIDE" else "NO POWER"))

say("")
say("(b) the value as a function of C_T (hence of q), via C_D = 0.9e3*C_T,")
say("    t_pr = 1/(3.31e7*C_D^2), eps_1^cut = t_pr/142125.")


def cut_from_CT(ct):
    cd = CD_BAND_HI * ct
    t_pr = 1 / (PREF_CERR * cd * cd)
    return t_pr / STRENGTH


say("")
say(f"{'q':>6s} {'C_T':>14s} {'C_D':>14s} {'eps_1^cut':>18s} {'decades vs q=12':>18s}")
base = cut_from_CT(CT_ROW[12])
spread_lo, spread_hi = None, None
for q in sorted(CT_ROW):
    c = cut_from_CT(CT_ROW[q])
    d = dec(c, base)
    say(f"{q:6d} {D(CT_ROW[q]):14.4E} {D(CD_BAND_HI * CT_ROW[q]):14.4E} {D(c):18.6E} {d:+18.4f}")
    spread_lo = d if spread_lo is None else min(spread_lo, d)
    spread_hi = d if spread_hi is None else max(spread_hi, d)
for nm, ct in (("q=8 (HANDOFF)", CT_Q8), ("no (H2)", CT_NO_H2)):
    c = cut_from_CT(ct)
    say(f"{nm:>6s} {D(ct):14.4E} {D(CD_BAND_HI * ct):14.4E} {D(c):18.6E} {dec(c, base):+18.4f}")

say("")
say(f"  reproduction check: cut at q=12 = {D(base):.6E}  vs EPS1_SWEEP's {D(E_PROP):.6E}"
    f"  ratio {D(base / E_PROP):.6f}")
say(f"  spread over EPSSTAR's own q-row (q=10..100): {spread_hi - spread_lo:.4f} decades")
say(f"  spread over the admissible range q>=11      : "
    f"{dec(cut_from_CT(CT_ROW[100]), cut_from_CT(CT_ROW[11])):.4f} decades")
v2b = "VALUE-PARAMETRIC" if (spread_hi - spread_lo) >= Decimal("0.30") else "VALUE-PINNED"

flat = [cut_from_CT(CT_ROW[12]) for _ in CT_ROW]
ctrl_spread = max(dec(x, base) for x in flat) - min(dec(x, base) for x in flat)
ctrl2b = "VALUE-PINNED" if ctrl_spread < Decimal("0.30") else "VALUE-PARAMETRIC"
say(f"ee1-2(b) MAIN    : {v2b}   (spread {spread_hi - spread_lo:.4f} decades)")
say(f"ee1-2(b) CONTROL : {ctrl2b}  (constant C_T row; criteria require VALUE-PINNED)")
say("ee1-2(b) POWER   : " + ("HAS-POWER" if ctrl2b == "VALUE-PINNED" else "NO POWER"))

# ---------------------------------------------------------------- ee1-3  (C5)
say("")
say("=" * 78)
say("ee1-3  (C5): do the steeper prices equal (exponent) x (the move)?")
say("=" * 78)

DELTA = dec(E_RERUN_TB, E_PROP)
say("")
say(f"  the move Delta = log10(6.7e-40 / 9.38495112638e-45) = {DELTA:.6f} decades")


def eta1_quad(e1):
    return e1 * e1 / (512 * N * A_D)          # RLARGE l.64, quadratic branch


def eta1_lin(e1):
    return C1_KN * e1                          # EXISTENCE l.1771


def a_eta(eta1):
    return eta1 * eta1 / (2 * N)               # RLARGE l.1026


say("")
say(f"{'quantity':38s} {'at 6.7e-40':>16s} {'at proposed':>16s} {'decades':>10s} {'k*Delta':>10s}")
rows3 = []
for nm, f_e1, k in (("a_RS, RLARGE quadratic eta_1 (eps^4)", lambda e: a_eta(eta1_quad(e)), 4),
                    ("a_RS, KN-step linear eta_1   (eps^2)", lambda e: a_eta(eta1_lin(e)), 2)):
    hi, lo = f_e1(E_RERUN_TB), f_e1(E_PROP)
    d = dec(hi, lo)
    rows3.append((nm, d, k * DELTA))
    say(f"{nm:38s} {D(hi):16.5E} {D(lo):16.5E} {d:10.4f} {k * DELTA:10.4f}")
# Cauchy C^3 on D_{alpha_E}, alpha_E ~ eps_1, constant ∝ eps_1^-3  [ARGUED: HIST l.862 omits the constant]
hi, lo = 1 / E_RERUN_TB ** 3, 1 / E_PROP ** 3
rows3.append(("Cauchy C^3 on D_alpha_E (eps^-3)", dec(lo, hi), 3 * DELTA))
say(f"{'Cauchy C^3 on D_alpha_E (eps^-3)':38s} {D(hi):16.5E} {D(lo):16.5E} "
    f"{dec(lo, hi):10.4f} {3 * DELTA:10.4f}")

worst3 = max(abs(d - k) for _, d, k in rows3)
say("")
say(f"  worst |formula - k*Delta| = {worst3:.3E} decades")
say(f"  a_RS at eps^4 reproduces EPS1_SWEEP's 19.415 ? "
    f"{abs(rows3[0][1] - Decimal('19.415')) <= Decimal('0.01')}  (got {rows3[0][1]:.4f})")
say(f"  a_RS at eps^2 reproduces EPS1_SWEEP's  9.707 ? "
    f"{abs(rows3[1][1] - Decimal('9.707')) <= Decimal('0.01')}  (got {rows3[1][1]:.4f})")
say(f"  Cauchy reproduces EPS1_SWEEP's        14.561 ? "
    f"{abs(rows3[2][1] - Decimal('14.561')) <= Decimal('0.01')}  (got {rows3[2][1]:.4f})")
v3 = ("PRICES-AGREE" if (worst3 <= Decimal("1e-3")
                         and abs(rows3[0][1] - Decimal('19.415')) <= Decimal('0.01')
                         and abs(rows3[1][1] - Decimal('9.707')) <= Decimal('0.01')
                         and abs(rows3[2][1] - Decimal('14.561')) <= Decimal('0.01'))
      else "PRICES-DISAGREE")

# designed-FAIL: assert exponent 2 against the QUADRATIC branch
d_quad = dec(a_eta(eta1_quad(E_RERUN_TB)), a_eta(eta1_quad(E_PROP)))
miss = abs(d_quad - 2 * DELTA)
ctrl3 = "PRICES-DISAGREE" if miss > Decimal("1e-3") else "PRICES-AGREE"
say(f"ee1-3 MAIN    : {v3}")
say(f"ee1-3 CONTROL : {ctrl3}  (exponent 2 asserted against the quadratic branch, "
    f"misses by {miss:.4f} decades; criteria require PRICES-DISAGREE)")
say("ee1-3 POWER   : " + ("HAS-POWER" if ctrl3 == "PRICES-DISAGREE" else "NO POWER"))

# also reproduce the absolute a_RS values, as an independent transcription gate
say("")
say("  absolute a_RS, against ARS_FIX 2.2's table (a different file, a different author):")
for nm, e1, want in (("6.7e-40 ", E_RERUN_TB, "5.93136e-166"),
                     ("proposed", E_PROP, "2.28341e-185")):
    say(f"    a_RS({nm}) = {D(a_eta(eta1_quad(e1))):.6E}   ARS_FIX 2.2 records {want}")

# ---------------------------------------------------------------- ee1-4  (C3)
say("")
say("=" * 78)
say("ee1-4  (C3): which way does PLD l.995's 2 m_* g / eps_1 move?")
say("=" * 78)


def ratio_verdict(e1_hi, e1_lo, g_hi, g_lo, tol=Decimal("1e-12")):
    """g/eps_1 at the two eps_1; m_* cancels."""
    r_hi, r_lo = g_hi / e1_hi, g_lo / e1_lo
    d = log10(r_lo) - log10(r_hi)
    if abs(d) < tol:
        return "INVARIANT", d
    return ("RATIO-RISES" if d > 0 else "RATIO-FALLS"), d


say("")
say("  MAIN: fixed g at the DX' ceiling (g is eps_1-INDEPENDENT; SF l.2587)")
v4, d4 = ratio_verdict(E_RERUN_TB, E_PROP, G_DX, G_DX)
say(f"    g/eps_1 : {D(G_DX / E_RERUN_TB):.6E}  ->  {D(G_DX / E_PROP):.6E}   "
    f"change {d4:+.4f} decades  -> {v4}")
say(f"    EPS1_SWEEP 2.2/2.3 state this 'shrinks as eps_1 falls' / 'falls 4.854 decades'.")
say("")
say("  window margin log10(eps_1/g), against EPS1_SWEEP 2.2's 36.63 -> 31.78:")
m_hi, m_lo = log10(E_RERUN_TB / G_DX), log10(E_PROP / G_DX)
say(f"    {m_hi:.4f}  ->  {m_lo:.4f}   (loses {m_hi - m_lo:.4f} decades)")
say(f"    reproduces 36.63 ? {abs(m_hi - Decimal('36.63')) <= Decimal('0.01')}   "
    f"reproduces 31.78 ? {abs(m_lo - Decimal('31.78')) <= Decimal('0.01')}")

say("")
say("  CONTROL 1 (known-invariant): g proportional to eps_1 (the eps-driven ceiling,")
say("            EPS1_SWEEP 2.4's structural fact). Must return INVARIANT.")
scale = E_PROP / E_RERUN_TB
c1v, c1d = ratio_verdict(E_RERUN_TB, E_PROP, G_DX, G_DX * scale)
say(f"    -> {c1v}  (change {c1d:+.3E} decades)")

say("")
say("  CONTROL 2 (reversed input): eps_1 RAISED x10 at fixed g. Must return RATIO-FALLS.")
c2v, c2d = ratio_verdict(E_RERUN_TB, E_RERUN_TB * 10, G_DX, G_DX)
say(f"    -> {c2v}  (change {c2d:+.4f} decades)")

pw4 = "HAS-POWER" if (c1v == "INVARIANT" and c2v == "RATIO-FALLS") else "NO POWER"
say("")
say(f"ee1-4 MAIN     : {v4}")
say(f"ee1-4 CONTROL1 : {c1v}  (criteria require INVARIANT)")
say(f"ee1-4 CONTROL2 : {c2v}  (criteria require RATIO-FALLS)")
say(f"ee1-4 POWER    : {pw4}")

# ---------------------------------------------------------------- precision
say("")
say("=" * 78)
say("precision control")
say("=" * 78)
snapshot = (v_main, v_ctrl, v2a, v2b, v3, v4, c1v, c2v)
getcontext().prec = 100
re_delta = dec(E_RERUN_TB, E_PROP)
re_m_hi = log10(E_RERUN_TB / G_DX)
re_v4, _ = ratio_verdict(E_RERUN_TB, E_PROP, G_DX, G_DX)
stable = (str(re_delta)[:20] == str(DELTA)[:20] and re_v4 == v4
          and str(re_m_hi)[:12] == str(m_hi)[:12])
say(f"  Delta at 50 digits : {DELTA}")
say(f"  Delta at 100 digits: {re_delta}")
say(f"  verdicts identical : {re_v4 == v4}")
say(f"  PRECISION-{'STABLE' if stable else 'UNSTABLE'}")

say("")
say("=" * 78)
say("SUMMARY (pre-registered verdicts only)")
say("=" * 78)
for k, v in (("ee1-1 (C6) factorisation", v_main), ("ee1-1 control", v_ctrl),
             ("ee1-2a (C4) rounding", v2a), ("ee1-2a control", ctrl2a),
             ("ee1-2b (C4) q-sensitivity", v2b), ("ee1-2b control", ctrl2b),
             ("ee1-3 (C5) prices", v3), ("ee1-3 control", ctrl3),
             ("ee1-4 (C3) sign", v4), ("ee1-4 control1", c1v), ("ee1-4 control2", c2v)):
    say(f"  {k:32s} : {v}")

print("\n".join(out))
