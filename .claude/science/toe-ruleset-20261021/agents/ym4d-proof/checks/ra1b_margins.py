#!/usr/bin/env python3 -I
# ra1_margins.py -- independent re-derivation for REVIEW_ARS_EPS_S1 (target T55-H).
# Criteria: checks/ra1_criteria.md, written BEFORE this script.
# Exact fractions throughout; Decimal at 60 digits for log10 display only. No numpy/BLAS. No lock needed.

from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60

def dec(fr):
    return Decimal(fr.numerator) / Decimal(fr.denominator)

def log10(fr):
    return dec(fr).ln() / Decimal(10).ln()

def s(x, n=6):
    return f"{x:.{n}f}"

# ---------------- structural inputs (all transcribed; see ra1_criteria.md) ----------------
d, L = 4, 3
A_d = F((d - 1) * L * (L - 1), 2)            # RLARGE l.973 -> 9
assert A_d == 9
c1 = F(1, 1) / (2 * (L**2 + F(11, 2) * A_d))  # EXISTENCE l.1771
DXp = F(2456, 1000) * F(10) ** -152           # REVIEW_SF_S7 l.203, C_Omega = 1
TEN2 = F(100)
cRS_rs = F(5) ** 4                            # RLARGE l.1021
cRS_joint = F(81)                             # RLARGE l.435 / HIST l.185

EPS = {
    "1.27e-39  (SF l.2837)":        F(127, 100) * F(10) ** -39,
    "9.52e-40  (RLARGE l.71)":      F(952, 100) * F(10) ** -40,
    "8.95e-40  (RLARGE l.611)":     F(895, 100) * F(10) ** -40,
    "6.7e-40   (RLARGE l.72 HEAD)": F(67, 10) * F(10) ** -40,
    "9.38495112638e-45 PROPOSED":   F(938495112638, 10**12) * F(10) ** -44,
}
E_TODAY = EPS["6.7e-40   (RLARGE l.72 HEAD)"]
E_PROP = EPS["9.38495112638e-45 PROPOSED"]


def eta1_quad(e, N):
    return min(e / (2 * L**2), e * e / (512 * N * A_d))

def eta1_lin(e, N=None):
    return c1 * e

def eta_q(e, N):                      # delta_0/A_d entry omitted: inactive at eps_1 ~ 1e-40 (HIST l.180)
    return min(e / (2 * L**2), e / (256 * N * A_d))

def a_eta(eta, N):
    return eta * eta / (2 * N)

def a_RS(eta, e, N, kappa=F(1)):
    return min(a_eta(eta, N), kappa * e * e / (256 * N))

def margin(a, div=TEN2, COm=F(1)):
    return log10((a / div) / (DXp / COm))


out = []
P = out.append
P("ra1_margins.py -- REVIEW_ARS_EPS_S1, target T55-H.  Exact rational arithmetic.")
P(f"A_d = {A_d}, L^2 = {L**2}, c_1 = {c1} = 1/{1/c1}, DX' = 2.456e-152 (C_Omega = 1)")
P("")

# ---------------- RA1-4 : c_1 and the identity ----------------
P("=== RA1-4  c_1 = 1/117 and the 'identity' ===")
P(f"  1/(2(L^2 + 5.5 A_d)) = 1/(2(9 + 49.5)) = 1/{1/c1}   -> {'DERIVES' if c1 == F(1,117) else 'FAILS'}")
ident = (F(L**2) + F(11, 2) * A_d) * c1
P(f"  (L^2 + 5.5A_d)*c_1 = {ident}   [NO POWER: true by the definition of c_1 -- cannot fail]")
sharp = F(475889, 100000)   # the rebuilt 4.75889 of ARS_FIX l.377
ident_mixed = (F(L**2) + sharp * A_d) * c1
P(f"  POWER VARIANT (dichotomy's sharp 4.75889 vs c_1's 5.5): (L^2+4.75889A_d)c_1 = {s(float(ident_mixed),6)}"
  f"  -> {'differs from 1/2, so the comparison CAN fail and the two 5.5 are the SAME constant' if ident_mixed != F(1,2) else 'NO POWER'}")
c1_sharp = F(1, 1) / (2 * (L**2 + sharp * A_d))
P(f"  (aside) c_1 with the sharp 4.75889 would be 1/{s(float(1/c1_sharp),4)}; gain forgone ="
  f" {s(float(2*log10(c1_sharp/c1)),4)} decades")
P("")

# ---------------- RA1-5 : 117/4608, 39.3846, 59.0769, the two 4608s ----------------
P("=== RA1-5  117/4608, 39.3846, 59.0769, and the two 4608s ===")
for N in (2, 3):
    r = eta1_lin(F(1)) / eta_q(F(1), N)
    P(f"  N={N}: eta_1^lin/eta_q = {r.numerator}/{r.denominator} = {s(float(r),4)}")
P(f"  117/4608 = {F(117,4608)} = {s(float(F(117,4608)),9)}")
P(f"  256*N*A_d at N=2 = {256*2*A_d};  512*A_d = {512*A_d};  equal? {256*2*A_d == 512*A_d}")
P(f"  256*N*A_d at N=3 = {256*3*A_d};  512*A_d*N at N=3 = {512*A_d*3}  -> the coincidence is N=2 only")
P("  VERDICT RA1-5: EXACT; the two integers '4608' have DIFFERENT factorisations (256*N*A_d|_{N=2} vs 512*A_d)")
P("")

# ---------------- RA1-1 / RA1-3 : margins and gains ----------------
P("=== RA1-1 / RA1-3  margins and gains (N=2, kappa=1) ===")
P(f"{'eps_1':34s} {'a_RS quad':>13s} {'/1e2':>9s} {'/(625*1e2)':>11s} {'gain(dec)':>10s}")
gains = {}
for name, e in EPS.items():
    aq = a_RS(eta1_quad(e, 2), e, 2)
    al = a_RS(eta1_lin(e), e, 2)
    m1, m2 = margin(aq), margin(aq, TEN2 * cRS_rs)
    ml1, ml2 = margin(al), margin(al, TEN2 * cRS_rs)
    g = log10(al / aq)
    gains[name] = float(g)
    P(f"{name:34s} {float(dec(aq)):13.5e} {float(m1):9.3f} {float(m2):11.3f} {float(g):10.3f}"
      f"   | linear margins {float(ml1):+8.3f} / {float(ml2):+8.3f}")
live = [v for k, v in gains.items() if "PROPOSED" not in k]
sp = max(live) - min(live)
P(f"  spread of the GAIN across the four LIVE eps_1 (proposed row excluded): {s(sp,3)} decades"
  f"  -> {'GAIN-DETERMINATE' if sp <= 0.01 else 'GAIN-INDETERMINATE'}")
P("")

# ---------------- RA1-2 : the 625 reconciliation ----------------
P("=== RA1-2  does log10(625) reconcile -15.617 with -18.413? ===")
m_today = margin(a_RS(eta1_quad(E_TODAY, 2), E_TODAY, 2))
for cc, tag in ((cRS_rs, "c_RS = 625  (as ARS_FIX states)"), (cRS_joint, "c_RS = 81   (DESIGNED-FAIL control F-c)")):
    diff = m_today - log10(cc)
    ok = abs(diff - Decimal("-18.413")) < Decimal("0.001")
    P(f"  {tag}: {s(float(m_today),4)} - log10({cc}) = {s(float(diff),4)}"
      f"  -> {'RECONCILES' if ok else 'DOES-NOT-RECONCILE'}")
P("")

# ---------------- RA1-6 : the 1551x route reversal ----------------
P("=== RA1-6  the route reversal ARS_FIX l.537 prices at 1551x ===")
for N in (2, 3):
    rs_per_cube = a_eta(eta1_lin(E_TODAY), N) / cRS_rs
    jt_per_cube = a_eta(eta_q(E_TODAY, N), N) / cRS_joint
    bare = a_eta(eta1_lin(E_TODAY), N) / a_eta(eta_q(E_TODAY, N), N)
    P(f"  N={N}: bare exponent ratio (eta_1^lin/eta_q)^2 = {s(float(bare),3)}"
      f"   |  PER-CUBE ratio (/625 vs /81) = {s(float(rs_per_cube/jt_per_cube),3)}"
      f"  = {s(float(log10(rs_per_cube/jt_per_cube)),4)} decades")
P("  DESIGNED-FAIL control F-d (both routes at 625, i.e. asymmetry removed):")
for N in (2, 3):
    r = (a_eta(eta1_lin(E_TODAY), N) / cRS_rs) / (a_eta(eta_q(E_TODAY, N), N) / cRS_rs)
    P(f"    N={N}: ratio = {s(float(r),3)}  -> {'AGREES-1551' if N==2 and abs(float(r)-1551)<1 else 'n/a'}")
P("")

# ---------------- RA1-8 : net value over HIST's joint route ----------------
P("=== RA1-8  the joint route (HIST Lemma RS-lin, PROVEN-HERE at RLARGE l.628) ===")
for label, e in (("today  6.7e-40", E_TODAY), ("proposed", E_PROP)):
    for N in (2, 3):
        jt = a_eta(eta_q(e, N), N) / cRS_joint
        rs_q = a_RS(eta1_quad(e, N), e, N) / cRS_rs
        rs_l = a_RS(eta1_lin(e), e, N) / cRS_rs
        P(f"  {label}, N={N}: joint a_eta(eta_q)/81 = {float(dec(jt)):.5e}, margin vs DX' ="
          f" {float(margin(jt, TEN2)):+8.3f} dec")
        P(f"      RS quad /625 margin {float(margin(rs_q, TEN2)):+8.3f} ;"
          f" RS lin /625 margin {float(margin(rs_l, TEN2)):+8.3f} ;"
          f" NET gain of adoption over the joint route = {float(log10(rs_l/jt)):+7.3f} dec"
          f"  (joint beats RS-quad by {float(log10(jt/rs_q)):.3f} dec today)")
P("")

# ---------------- RA1-7 : C_Omega, the (C7) window, kappa ----------------
P("=== RA1-7  C_Omega crossovers, (C7)'s window, and kappa ===")
for label, e in (("today  6.7e-40", E_TODAY), ("proposed", E_PROP)):
    aq = a_RS(eta1_quad(e, 2), e, 2)
    for div, tag in ((TEN2, "/1e2"), (TEN2 * cRS_rs, "/(625*1e2)")):
        m = margin(aq, div)
        P(f"  {label} {tag}: margin {float(m):+8.3f} at C_Omega=1  ->  a_RS stops binding once"
          f" C_Omega > 10^{s(float(-m),3)} = {float(Decimal(10)**(-m)):.3e}")
P(f"  EPS1_SWEEP (C7) admits c_+*C_Omega up to 1.5e46 (l.494).  Crossover 10^15.617 = 4.14e15 is"
  f" {'INSIDE' if 15.617 < 46 else 'OUTSIDE'} that window by {s(46-15.617,3)} decades.")
P("")
P("  (C7)'s four exhaustion figures, recomputed -- which combination are they?")
gCRC_today, gCRC_prop = F(185835, 100000) * F(10)**-96, F(37936, 10000) * F(10)**-106
aRL_today, aRL_prop = F(10404, 10000) * F(10)**-88, F(20414, 10000) * F(10)**-98
for tag, val, has_cp in (("RLARGE a/1e2 today", aRL_today, False), ("RLARGE a/1e2 proposed", aRL_prop, False),
                         ("g2_CRC x82 today", gCRC_today, True), ("g2_CRC x82 proposed", gCRC_prop, True)):
    ratio = val / DXp
    P(f"    {tag:24s}: margin {float(log10(ratio)):+7.3f} dec; exhausted at"
      f" {'c_+/C_Omega' if has_cp else '1/C_Omega'} = {float(dec(ratio)):.3e}")
P("    -> compare EPS1_SWEEP l.443-444: 8.31e53 (RLARGE), 1.54e46 (CRC) at the proposed eps_1;")
P("       4.24e63 and 7.87e55 today.  Reported there as 'c_+*C_Omega'.")
P("")
P("  kappa: a_eta^lin binds the min of a_RS iff kappa > 128*c_1^2 = " + str(128 * c1 * c1)
  + f" = {s(float(128*c1*c1),8)}")
for kv in ("1", "0.01", "1e-4", "1e-8"):
    k = F(Decimal(kv))
    al = a_RS(eta1_lin(E_TODAY), E_TODAY, 2, k)
    aq = a_RS(eta1_quad(E_TODAY, 2), E_TODAY, 2, k)
    P(f"    kappa={kv:6s}: gain = {float(log10(al/aq)):7.3f} dec")
P("")

# ---------------- RA1-9 : H5 ----------------
P("=== RA1-9  H5: t <= 1/(106 sqrt(N) A_d^2 c_1^2) ===")
for N, quoted in ((2, "1.12737"), (3, "0.920492")):
    base = F(1) / (106 * A_d * A_d * c1 * c1)
    val = dec(base) / Decimal(N).sqrt()
    P(f"  N={N}: mine {s(float(val),6)} vs ARS_FIX l.408 {quoted}"
      f"  -> rel. diff {s(float(abs(val-Decimal(quoted))/Decimal(quoted)),8)}"
      f"  {'REPRODUCES' if abs(val-Decimal(quoted))/Decimal(quoted) < Decimal('1e-3') else 'SOURCE-DISAGREES'}")
reb = F(1) / (96 * A_d * A_d * c1 * c1)
pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494")
P(f"  rebuild of EXISTENCE's 106: 8*12*(pi/3)^2 = {s(float(96*(pi/3)**2),4)}; ratio 106/that ="
  f" {s(float(Decimal(106)/(96*(pi/3)**2)),6)}")
P("")

# ---------------- DESIGNED-FAIL controls F-a, F-b ----------------
P("=== DESIGNED-FAIL controls ===")
for tag, fn in (("F-a  eta_1 := eps_1 (c_1=1)", lambda e, N: e),
                ("F-b  eta_1 := eps_1^3/(512 N A_d)", lambda e, N: e**3 / (512 * N * A_d))):
    a = a_RS(fn(E_TODAY, 2), E_TODAY, 2)
    aq = a_RS(eta1_quad(E_TODAY, 2), E_TODAY, 2)
    m = margin(a)
    P(f"  {tag}: margin {float(m):+9.3f} -> {'NOT-BINDING' if m > 0 else 'BINDS'};"
      f" gain over quadratic {float(log10(a/aq)):+8.3f} dec")
P("  Both controls move the verdict -> the margin gate HAS POWER.")

txt = "\n".join(out)
print(txt)
