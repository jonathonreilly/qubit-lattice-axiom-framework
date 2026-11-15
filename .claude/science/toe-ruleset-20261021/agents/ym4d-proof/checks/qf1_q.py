#!/usr/bin/env python3
# qf1_q.py -- T55-N (QFIX.md), session 25.  Pre-registered in checks/qf1_criteria.md (21:48 UTC);
# this script was written AFTER that file.
#
# Plain python.  fractions.Fraction + fixed-precision Decimal.  No numpy, no BLAS, single thread,
# no numeric lock (exact / decimal arithmetic only, per the brief's rule 6).
#
# Every INPUT constant is inherited and listed with its file:line in checks/qf1_criteria.md section 0.
# The FORMULAS are the inherited ones (CONST_T section 6.1 / EPSSTAR section 7.1 / SQ l.1513, l.1624,
# l.1633-1634 / REVIEW_SQ_S4 S4-16 / ARS_FIX section 2.2).  This script does arithmetic, precision
# control, monotonicity and the pre-registered verdicts only.
#
# Blocks A-H exactly as pre-registered.  QF1-8 is labelled [POST-HOC-HAND] here and in QFIX.md.

from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext
import sys

PREC = int(sys.argv[1]) if len(sys.argv) > 1 else 40
getcontext().prec = PREC + 15

out = []
def say(s=""):
    out.append(s)

def dpow(x, y):
    return (D(y) * D(x).ln()).exp()

def lg(x):
    return D(x).log10()

# ------------------------------------------------------------------ inherited inputs
c_s    = D("411.9229708842423061")     # STAR_CONST section 7
c_g    = D("5699.632830341894211")     # STAR_CONST section 7
NS     = 3                             # STAR_CONST Lemma A2  (M-sharp)
N1     = 3**4 * 6                      # 486    CONST_T section 2.3 (M-ct, sensitivity only)
F_sch  = D("175.8")                    # CONST_T section 3.2
R0     = D(64)                         # SQ.md l.1466
SQRT6  = D(6).sqrt()
M_TARG = 19615                         # EPSSTAR l.545 (A_c*gamma_c <= 1)
M_ONE  = 7                             # EPSSTAR l.545 (A_c*gamma_c <= 2.87e3)

TWO47N = D("4.94")                     # 2.47*N*sqrt(kappa_+), N=2, kappa_+=1   REVIEW_SQ_S4 l.371
C0_SQ  = D("3.34")                     # REVIEW_SQ_S4 l.371
B0_SQ  = D("46.8")                     # REVIEW_SQ_S4 l.371  (NB: its "q" is SQ l.1524's decay ratio)
CERR_C = D("1.655e7")                  # REVIEW_SQ_S4 S4-16
ETAB_D = D("5.05e9")                   # EPSSTAR l.521:  eta_flat = t_pr^2 / 5.05e9
EPS1_0 = D("6.7e-40")                  # RLARGE l.72
CD_CEIL= D("6.7e15")                   # REVIEW_SQ_S4 S4-16 / EPSSTAR l.602
DXP    = D("2.456e-152")               # REVIEW_SF_S7 l.203, C_Omega = 1
ARS0   = D("5.93136e-166")             # ARS_FIX section 2.2, at eps_1 = 6.7e-40
C_RS   = D(625)                        # RLARGE l.1021
THG8   = D("1.46e-13")                 # REVIEW_SQ_S4 S4-14, theta_G at q = 8
C3     = D(1)
COMEGA = D(1)

# ARS_FIX section 2.2 rows: (eps_1, a_RS, margin_bare, margin_cRS)
ARS_ROWS = [(D("1.27e-39"),  D("7.65720e-165"), D("-14.506"), D("-17.302")),
            (D("9.52e-40"),  D("2.41770e-165"), D("-15.007"), D("-17.803")),
            (D("8.95e-40"),  D("1.88863e-165"), D("-15.114"), D("-17.910")),
            (D("6.7e-40"),   D("5.93136e-166"), D("-15.617"), D("-18.413")),
            (D("9.38495112638e-45"), D("2.28341e-185"), D("-35.032"), D("-37.828"))]

# EPSSTAR l.547-553 published q-row (m = 19615, m = 7), P-max, M-sharp
EPSSTAR_ROW = {10: (D("2.463e13"), D("2.857e13")),
               11: (D("9.774e12"), D("1.333e13")),
               12: (D("5.288e12"), D("8.717e12")),
               16: (D("2.031e12"), D("5.358e12")),
               24: (D("1.528e12"), D("4.836e12")),
               32: (D("1.454e12"), D("4.760e12")),
               100:(D("1.396e12"), D("4.699e12"))}

QGRID = [8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 32, 50, 100, 200, 1000, 10**4, 10**6]

say("=" * 104)
say(f"qf1_q.py -- T55-N (QFIX.md).  Decimal precision = {PREC} significant digits")
say("Criteria: checks/qf1_criteria.md (pre-registered, 21:48 UTC).  Inputs: that file's section 0.")
say("=" * 104)

# ------------------------------------------------------------------ Block A: beta telescope
say()
say("BLOCK A -- beta telescope  B(m) = prod_{i>=0} (p_i - 1)^(m/p_i),  p_i = 2^(i+1)")
def B(m, nmax=400):
    tot = D(0)
    for i in range(nmax):
        p = D(2) ** (i + 1)
        b = p - 1
        if b <= 1:
            continue
        tot += D(m) / p * b.ln()
    return tot.exp()
B4, B8 = B(4), B(8)
say(f"  B(4) = {B4:.6f}   CONST_T section 3.1 says 43.95   rel.dev = {abs(B4-D('43.95'))/D('43.95'):.2E}")
say(f"  B(8) = {B8:.6f}   CONST_T section 3.1 says 1931.5  rel.dev = {abs(B8-D('1931.5'))/D('1931.5'):.2E}")
A_OK = (abs(B4 - D("43.95")) / D("43.95") < D("0.005")) and (abs(B8 - D("1931.5")) / D("1931.5") < D("0.005"))

# ------------------------------------------------------------------ C_T machinery
def c_theta(q):
    th = D(4) / D(q)
    a = D(1) / (D(1) - th)
    ct = (D(1) - th) * dpow(D(4) * th, th / (D(1) - th))
    return ct, a, th

def C_S1(q, m):
    ct, a, th = c_theta(q)
    inner = ct * dpow(D(27) * c_s, a) + D(4096) * c_g
    frac = D(1) - D(1) / D(4) - D(1) / (D(4) * D(m))
    return (inner / frac).sqrt()

def Acgc(q, m):
    return (D(1) + SQRT6) * C_S1(q, m) / D(m)

def Qterm(q, m, r0=R0, Nsrc=NS):
    Vs = dpow(r0, D(-2) + D(8) / D(q))
    return D(288) * (c_g + D(18) * (D(Nsrc) * c_s * Vs + D(1) / (D(36) * D(m))))

def C_T(q, m, pmax=True, Nsrc=NS, r0=R0):
    ct, a, th = c_theta(q)
    Asgs = D(36) * c_s * D(Nsrc)
    Btel = B8 if pmax else B(4 * a)
    ac = Acgc(q, m)
    Chat = dpow(Asgs, a) / 2 + ac * ac / 2 + Qterm(q, m, r0, Nsrc)
    return SQRT6 * F_sch * Btel * Chat, Chat, ac

# ------------------------------------------------------------------ Block B: QF1-1 reproduction
say()
say("BLOCK B -- QF1-1  reproduction of EPSSTAR l.547-553 (P-max, M-sharp)")
say(f"  {'q':>7} {'mine m=19615':>16} {'EPSSTAR':>12} {'rel':>10} | {'mine m=7':>16} {'EPSSTAR':>12} {'rel':>10}")
worst = D(0)
for q in sorted(EPSSTAR_ROW):
    a1 = C_T(q, M_TARG)[0]
    a2 = C_T(q, M_ONE)[0]
    e1, e2 = EPSSTAR_ROW[q]
    r1 = abs(a1 - e1) / e1
    r2 = abs(a2 - e2) / e2
    worst = max(worst, r1)
    say(f"  {q:>7} {a1:>16.4E} {e1:>12.3E} {r1:>10.2%} | {a2:>16.4E} {e2:>12.3E} {r2:>10.2%}")
QF1_1 = A_OK and (worst < D("0.01"))
say(f"  worst m=19615 relative deviation = {worst:.3%}")
say(f"  QF1-1: {'PASS' if QF1_1 else 'FAIL'}   (B(4),B(8) within 0.5%: {A_OK}; q-row within 1%)")

# ------------------------------------------------------------------ Block C: QF1-2 monotone + plateau
say()
say("BLOCK C -- QF1-2  monotonicity and plateau of C_T(q), P-max, m = 19615")
vals = [(q, C_T(q, M_TARG)[0]) for q in QGRID]
mono = all(vals[i][1] > vals[i + 1][1] for i in range(len(vals) - 1))
say(f"  {'q':>8} {'C_T (P-max)':>16} {'C_T (P-ct)':>16} {'B(4a)':>10} {'a':>10}")
for q in QGRID:
    ct_max = C_T(q, M_TARG)[0]
    ct_ct = C_T(q, M_TARG, pmax=False)[0]
    _, a, _ = c_theta(q)
    say(f"  {q:>8} {ct_max:>16.5E} {ct_ct:>16.5E} {B(4*a):>10.3f} {a:>10.6f}")
plateau = C_T(10**6, M_TARG)[0]
QF1_2 = mono and plateau > 0
say(f"  strictly decreasing on the grid: {mono};  C_T(q=1e6) = {plateau:.5E} (finite, positive)")
say(f"  QF1-2: {'PASS' if QF1_2 else 'FAIL'}")

# ------------------------------------------------------------------ Block D: QF1-3 / QF1-3b exact
say()
say("BLOCK D -- QF1-3 / QF1-3b  the structural clauses, as EXACT Fractions")
say(f"  {'q':>6} {'sigma=q/2>2':>12} {'theta=4/q':>12} {'a=q/(q-4)':>12} {'(-2+8/q)a=-2':>14} {'theta<=1/2':>11}")
ok3 = True
ok3b_low = True   # expect FALSE for q in (4,8)
ok3b_hi = True    # expect TRUE  for q >= 8
for q in [5, 6, 7, 8, 10, 11, 12, 16, 32, 100]:
    Q = Fr(q)
    sig = Q / 2
    th = Fr(4, 1) / Q
    a = Q / (Q - 4)
    ident = (Fr(-2) + Fr(8, 1) / Q) * a == Fr(-2)
    cl = (sig > 2) and (a > 1) and ident
    ok3 = ok3 and cl
    half = th <= Fr(1, 2)
    if q < 8:
        ok3b_low = ok3b_low and (not half)
    else:
        ok3b_hi = ok3b_hi and half
    say(f"  {q:>6} {str(sig > 2):>12} {str(th):>12} {str(a):>12} {str(ident):>14} {str(half):>11}")
QF1_3 = ok3
QF1_3b = ok3b_low and ok3b_hi
say(f"  QF1-3:  {'PASS' if QF1_3 else 'FAIL'}   (nothing in the step's own mathematics excludes q < 11)")
say(f"  QF1-3b: {'PASS' if QF1_3b else 'FAIL'}   (theta <= 1/2 FAILS on (4,8), holds for q >= 8)")

# ------------------------------------------------------------------ Block E: QF1-4 the frozen prefactor
say()
say("BLOCK E -- QF1-4  the C_D prefactor Lambda(q) = 4*2^(2+4/q)*(4.94 + 3.34*32^(1/q))")
def Lam(q):
    return D(4) * dpow(D(2), D(2) + D(4) / D(q)) * (TWO47N + C0_SQ * dpow(D(32), D(1) / D(q)))
L8, L12, Linf = Lam(8), Lam(12), Lam(10**9)
say(f"  Lambda(8)    = {L8:.5f}     (REVIEW_SQ_S4 l.371: C_T' = 22.63C_T, bracket 10.09 -> 228)")
say(f"  Lambda(12)   = {L12:.5f}")
say(f"  Lambda(inf)  = {Linf:.5f}    (CONST_T section 4.2: 16*8.28 = 132)")
say(f"  Lambda(12)/Lambda(8)   = {L12/L8:.6f}   ({(D(1)-L12/L8)*100:.2f} % below)")
say(f"  Lambda(8)/Lambda(inf)  = {L8/Linf:.6f}   (CONST_T section 4.2 says 'a further ~1.7x on C_D')")
QF1_4 = (abs(L12 / L8 - 1) > D("0.05")) and (L8 / Linf > D("1.5"))
say(f"  QF1-4: {'PASS' if QF1_4 else 'FAIL'}")
say("  => REVIEW_SQ_S4 S4-16's (0.5-0.9)e3 is Lambda(8)*2.022*c_N with c_N in [1,2]:")
for cn in [D(1), D(2)]:
    say(f"       c_N = {cn}:  2.022*Lambda(8)*c_N = {D('2.022')*L8*cn:.2f}")
say("     and es1_eps.py l.48 hard-codes C_D_PER_CT = 0.9e3 for EVERY q.")

# ------------------------------------------------------------------ Block F: QF1-9 then the objective
say()
say("BLOCK F -- QF1-9  the power of eps_1 in a_RS, from ARS_FIX section 2.2's own rows")
best = None
for p in range(1, 7):
    err = max(abs(ARS0 * dpow(e / EPS1_0, D(p)) - v) / v for (e, v, _, _) in ARS_ROWS)
    say(f"  p = {p}: worst relative deviation over the five rows = {err:.4%}")
    if err < D("0.002"):
        best = p if best is None else best
QF1_9a = best is not None
say(f"  unique integer p with all rows within 0.2% : {best}")

def a_RS(e1):
    return ARS0 * dpow(e1 / EPS1_0, D(best if best else 4))
def margin(e1, crs=False):
    ceil = a_RS(e1) / D(100) / (C_RS if crs else D(1))
    return lg(ceil) - lg(DXP / COMEGA)
mrep = all(abs(margin(e, False) - mb) < D("0.01") and abs(margin(e, True) - mc) < D("0.01")
           for (e, v, mb, mc) in ARS_ROWS)
say(f"  margins reproduce ARS_FIX's five rows to <= 0.01 decades: {mrep}")
for (e, v, mb, mc) in ARS_ROWS:
    say(f"    eps_1 = {e:.6E}: margin(bare) = {margin(e,False):.3f} (ARS_FIX {mb}),"
        f"  margin(c_RS) = {margin(e,True):.3f} (ARS_FIX {mc})")
QF1_9 = QF1_9a and mrep
say(f"  QF1-9: {'PASS' if QF1_9 else 'FAIL'}")

# ------------------------------------------------------------------ the chain, as a function of q
DIV = D(2) * (ETAB_D * C3).sqrt()      # eps_1^cut = t_pr / (2 sqrt(5.05e9 C_3))
say()
say(f"  eps_1^cut = t_pr / (2*sqrt(5.05e9*C_3)) ; divisor = {DIV:.6f}  (EPS1_EXEC quotes 142125)")

def chain(q, m=M_TARG, cn=D(2), pmax=True, frozen=False):
    ct = D("5.288e12") if frozen else C_T(q, m, pmax=pmax)[0]
    lam = L8 if frozen else Lam(q)
    A0 = cn * lam * ct
    CD = D(2) * (D("1.011") * A0 + B0_SQ)
    tpr = D(1) / (D(2) * CERR_C * CD * CD)
    cut = tpr / DIV
    eff = min(EPS1_0, cut)
    return ct, CD, tpr, cut, eff

say()
say("BLOCK F2 -- the objective over q.  P-max, m = 19615, c_N = 2 (the conservative end), C_3 = C_Omega = 1")
say("  OBJECTIVE = log10(a_RS(eps_1^eff)/1e2) - log10(DX')   [bare convention; c_RS column is -2.796 shifted]")
say()
hdr = (f"  {'q':>8} {'C_T':>12} {'C_D':>12} {'t_pr':>12} {'eps_1^cut':>12} {'d(cut) vs q=12':>15}"
       f" {'OBJECTIVE':>11} {'vs q=12':>9} {'CLSmin hd':>10} {'a_bad hd':>9}")
say(hdr)
base = chain(12)
rows = []
for q in QGRID:
    ct, CD, tpr, cut, eff = chain(q)
    obj = margin(eff)
    rows.append((q, ct, CD, tpr, cut, obj))
    say(f"  {q:>8} {ct:>12.4E} {CD:>12.4E} {tpr:>12.4E} {cut:>12.4E}"
        f" {lg(cut)-lg(base[3]):>15.4f} {obj:>11.3f} {obj-margin(base[4]):>9.3f}"
        f" {lg(CD_CEIL/CD):>10.3f} {lg(tpr/eff):>9.3f}")
objs = [r[5] for r in rows]
sup = max(objs)
rec = min(q for (q, *_rest, o) in rows if sup - o <= D("0.05"))
QF1_5 = all(objs[i] <= objs[i + 1] + D("1e-12") for i in range(len(objs) - 1)) and (sup - objs[QGRID.index(12)] <= 20)
say(f"  supremum over grid = {sup:.3f};  recommended q (first within 0.05 dec of sup) = {rec}")
say(f"  QF1-5: {'PASS' if QF1_5 else 'FAIL'}  (monotone non-decreasing, total rise finite and <= 20 dec)")

# ------------------------------------------------------------------ Block G: QF1-6 designed-FAIL control
say()
say("BLOCK G -- QF1-6  designed-FAIL control: C_T and Lambda replaced by q-independent constants")
ctrl = [margin(chain(q, frozen=True)[4]) for q in QGRID]
spread_ctrl = max(ctrl) - min(ctrl)
spread_live = sup - min(objs)
say(f"  control objective spread over the grid = {spread_ctrl} decades  -> "
    f"{'NO-LEVER' if spread_ctrl == 0 else 'CONTROL MOVED (bad)'}")
say(f"  live    objective spread over the grid = {spread_live:.4f} decades -> "
    f"{'HAS-LEVER' if spread_live > D('0.30') else 'NO-LEVER'}")
QF1_6 = (spread_ctrl == 0) and (spread_live > D("0.30"))
say(f"  QF1-6: {'PASS' if QF1_6 else 'FAIL'}")

# ------------------------------------------------------------------ Block H: the other ceilings and theta_G
say()
say("BLOCK H -- the other ceilings, and the one consumer that moves AGAINST q")
say(f"  {'q':>8} {'eta_flat':>12} {'DESCeps short(dec)':>19} {'C_T vs DESC ceil':>17} {'theta_G':>11} {'thG headroom(dec)':>18}")
need_eta = D(4) * C3 * EPS1_0 * EPS1_0
for q in QGRID:
    ct, CD, tpr, cut, eff = chain(q)
    eta = tpr * tpr / ETAB_D
    thG = THG8 * D(8) / D(q)
    # C_T ceiling for DESC-eps at this q: C_D <= CDceil_desc, then C_T <= that / (2*1.011*cn*Lam(q))
    CD_desc = (D(1) / (D(2) * CERR_C * (DIV * EPS1_0) ** 2)).sqrt()
    ct_ceil = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(2) * Lam(q))
    say(f"  {q:>8} {eta:>12.4E} {lg(need_eta/eta):>19.3f} {ct_ceil:>17.4E} {thG:>11.4E} {lg(thG/eff):>18.3f}")
say(f"  the DESC-eps C_D ceiling, self-consistently derived: C_D <= {CD_desc:.5E} / C_3^(1/4)")

say()
say("  P-ct sensitivity (B(4a) instead of B(8)) -- STAR_CONST section 6.4 calls P-max the correct one:")
say(f"  {'q':>8} {'C_T (P-ct)':>14} {'C_D (P-ct)':>14} {'DESC ceil on C_T':>18} {'clears?':>9}")
for q in [12, 32, 100, 1000, 10**6]:
    ct, CD, tpr, cut, eff = chain(q, pmax=False)
    ct_ceil = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(2) * Lam(q))
    say(f"  {q:>8} {ct:>14.4E} {CD:>14.4E} {ct_ceil:>18.4E} {str(ct <= ct_ceil):>9}")

# ------------------------------------------------------------------ Block I: QF1-8 [POST-HOC-HAND]
say()
say("BLOCK I -- QF1-8 [POST-HOC-HAND]  EPSSTAR l.525's internal consistency")
tpr_need = EPS1_0 * DIV
say(f"  eta_flat = t_pr^2/5.05e9 >= 4*C_3*eps_1^2 at eps_1 = 6.7e-40, C_3 = 1")
say(f"    => t_pr >= 2*eps_1*sqrt(5.05e9*C_3) = {tpr_need:.6E}")
say(f"    EPSSTAR l.525 states t_pr >= 3.01e-35 ; ratio mine/theirs = {tpr_need/D('3.01e-35'):.6f}")
CD_theirs = (D(1) / (D(2) * CERR_C * D("3.01e-35"))).sqrt()
say(f"    their t_pr gives C_D <= {CD_theirs:.5E}  (EPSSTAR l.525 states 3.17e13)")
say(f"    self-consistent  C_D <= {CD_desc:.5E}  -- ratio {CD_theirs/CD_desc:.6f}")
QF1_8 = abs(tpr_need - D("3.01e-35")) / D("3.01e-35") < D("0.01")
say(f"  QF1-8: {'PASS' if QF1_8 else 'FAIL'}  (PASS would mean EPSSTAR l.525 is self-consistent)")
ct_ceil12 = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(2) * Lam(12))
ct_ceil12_cn1 = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(1) * Lam(12))
say(f"    knock-on: EPSSTAR l.525's 'C_T <~ 3.5e10 - 6.3e10' becomes "
    f"{ct_ceil12:.4E} (c_N=2) - {ct_ceil12_cn1:.4E} (c_N=1) at q = 12")

# ------------------------------------------------------------------ summary
say()
say("=" * 104)
say("PRE-REGISTERED VERDICTS")
for k, v in [("QF1-1", QF1_1), ("QF1-2", QF1_2), ("QF1-3", QF1_3), ("QF1-3b", QF1_3b),
             ("QF1-4", QF1_4), ("QF1-5", QF1_5), ("QF1-6", QF1_6), ("QF1-8", QF1_8), ("QF1-9", QF1_9)]:
    say(f"  {k:<8} {'PASS' if v else 'FAIL'}")
say("  QF1-7  -- compare qf1_out.txt (prec 40) with qf1_out_prec60.txt (prec 60) outside the script.")
say("=" * 104)

print("\n".join(out))
