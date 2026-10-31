#!/usr/bin/env python3
# qf1b_q.py -- RE-RUN of qf1_q.py under a new id.  Criteria UNTOUCHED (checks/qf1_criteria.md).
#
# WHY A RE-RUN.  qf1_q.py contained a transcription error OF MY OWN in ONE expression:
#     CD_desc = sqrt( 1 / (2*C_err_coef * (DIV*eps_1)**2) )        <-- WRONG, t_pr_need squared
#   should be
#     CD_desc = sqrt( 1 / (2*C_err_coef * (DIV*eps_1)) )           <-- t_pr_need enters linearly
#   because t_pr = 1/(2*C_err) = 1/(2*1.655e7*C_D^2) >= t_pr_need  <=>  C_D^2 <= 1/(2*1.655e7*t_pr_need).
# It affected ONLY: Block H's "C_T vs DESC ceil" column, Block H's closing C_D line, Block I's
# "self-consistent C_D" line and knock-on, and the P-ct "clears?" column.  It did NOT touch
# QF1-1..QF1-6 or QF1-9, nor the objective curve of Block F2, nor QF1-8's primary comparison
# (t_pr_need = 9.522489e-35 vs EPSSTAR l.525's 3.01e-35), all of which are unchanged below.
# qf1_q.py and qf1_out.txt are kept byte-unaltered.
#
# Additions in this re-run, all REPORTED not pre-registered, and labelled [ADDED] in the output:
#   - the plateau term-split of Chat;
#   - theta_eps(q) and the q at which theta_G would finally bind;
#   - the spread of the objective over q >= 11 and over q >= 8 separately.
#
# Plain python, Fractions + Decimal, no numpy/BLAS, single thread, no numeric lock.

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

# ------------------------------------------------------------------ inherited inputs (unchanged)
c_s    = D("411.9229708842423061")
c_g    = D("5699.632830341894211")
NS     = 3
F_sch  = D("175.8")
R0     = D(64)
SQRT6  = D(6).sqrt()
M_TARG = 19615
M_ONE  = 7

TWO47N = D("4.94")
C0_SQ  = D("3.34")
B0_SQ  = D("46.8")
CERR_C = D("1.655e7")
ETAB_D = D("5.05e9")
EPS1_0 = D("6.7e-40")
CD_CEIL= D("6.7e15")
DXP    = D("2.456e-152")
ARS0   = D("5.93136e-166")
C_RS   = D(625)
THG8   = D("1.46e-13")
EPSSTAR_FLOOR = D("1.12e-37")      # EPSSTAR l.482: eps_* >= 84*theta_0^SUP
C3     = D(1)
COMEGA = D(1)

ARS_ROWS = [(D("1.27e-39"),  D("7.65720e-165"), D("-14.506"), D("-17.302")),
            (D("9.52e-40"),  D("2.41770e-165"), D("-15.007"), D("-17.803")),
            (D("8.95e-40"),  D("1.88863e-165"), D("-15.114"), D("-17.910")),
            (D("6.7e-40"),   D("5.93136e-166"), D("-15.617"), D("-18.413")),
            (D("9.38495112638e-45"), D("2.28341e-185"), D("-35.032"), D("-37.828"))]

QGRID = [8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 32, 50, 100, 200, 1000, 10**4, 10**6]

say("=" * 104)
say(f"qf1b_q.py -- T55-N (QFIX.md) RE-RUN.  Decimal precision = {PREC} significant digits")
say("Criteria: checks/qf1_criteria.md (pre-registered 21:48 UTC, UNTOUCHED).")
say("Re-run of qf1_q.py; the corrected expression and its scope are in this file's header.")
say("=" * 104)

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

def C_T_parts(q, m, pmax=True, Nsrc=NS, r0=R0):
    ct, a, th = c_theta(q)
    Asgs = D(36) * c_s * D(Nsrc)
    Btel = B8 if pmax else B(4 * a)
    ac = Acgc(q, m)
    t1 = dpow(Asgs, a) / 2
    t2 = ac * ac / 2
    t3 = Qterm(q, m, r0, Nsrc)
    Chat = t1 + t2 + t3
    return SQRT6 * F_sch * Btel * Chat, (t1, t2, t3, Chat)

def C_T(q, m, pmax=True):
    return C_T_parts(q, m, pmax)[0]

def Lam(q):
    return D(4) * dpow(D(2), D(2) + D(4) / D(q)) * (TWO47N + C0_SQ * dpow(D(32), D(1) / D(q)))
L8, L12, Linf = Lam(8), Lam(12), Lam(10**9)

P_ARS = 4           # QF1-9 verdict in qf1_out.txt: unique integer p, worst deviation 0.0002%
def a_RS(e1):
    return ARS0 * dpow(e1 / EPS1_0, D(P_ARS))
def margin(e1, crs=False):
    return lg(a_RS(e1) / D(100) / (C_RS if crs else D(1))) - lg(DXP / COMEGA)

DIV = D(2) * (ETAB_D * C3).sqrt()

def chain(q, m=M_TARG, cn=D(2), pmax=True, frozen=False):
    ct = D("5.288e12") if frozen else C_T(q, m, pmax=pmax)
    lam = L8 if frozen else Lam(q)
    A0 = cn * lam * ct
    CD = D(2) * (D("1.011") * A0 + B0_SQ)
    tpr = D(1) / (D(2) * CERR_C * CD * CD)
    cut = tpr / DIV
    eff = min(EPS1_0, cut)
    return ct, CD, tpr, cut, eff

# ------------------------------------------------------------------ the objective, unchanged
say()
say("BLOCK F2 (unchanged) -- the objective over q.  P-max, m = 19615, c_N = 2, C_3 = C_Omega = 1")
say(f"  {'q':>8} {'C_T':>12} {'C_D':>12} {'t_pr':>12} {'eps_1^cut':>12} {'d(cut) vs 12':>13}"
    f" {'OBJECTIVE':>11} {'vs q=12':>9} {'CLSmin hd':>10} {'a_bad hd':>9}")
base = chain(12)
rows = []
for q in QGRID:
    ct, CD, tpr, cut, eff = chain(q)
    obj = margin(eff)
    rows.append((q, ct, CD, tpr, cut, obj))
    say(f"  {q:>8} {ct:>12.4E} {CD:>12.4E} {tpr:>12.4E} {cut:>12.4E}"
        f" {lg(cut)-lg(base[3]):>13.4f} {obj:>11.3f} {obj-margin(base[4]):>9.3f}"
        f" {lg(CD_CEIL/CD):>10.3f} {lg(tpr/eff):>9.3f}")
objs = {q: o for (q, _a, _b, _c, _d, o) in rows}
sup = max(objs.values())
say(f"  supremum over the grid = {sup:.4f} (at q -> infinity; C_T saturates)")
say(f"  spread over q >= 8   (the structural floor, QF1-3b): {sup - objs[8]:.4f} decades")
say(f"  spread over q >= 11  (EPSSTAR's q_min):              {sup - objs[11]:.4f} decades")
say(f"  cost of q = 12 against the supremum:                 {sup - objs[12]:.4f} decades")
say(f"  cost of q = 32:  {sup-objs[32]:.4f}   q = 100: {sup-objs[100]:.4f}   q = 200: {sup-objs[200]:.4f}"
    f"   q = 1000: {sup-objs[1000]:.4f}")

# ------------------------------------------------------------------ Block H, CORRECTED
say()
say("BLOCK H (CORRECTED) -- the other ceilings, and the one consumer that moves AGAINST q")
tpr_need = EPS1_0 * DIV
CD_desc = (D(1) / (D(2) * CERR_C * tpr_need)).sqrt()
say(f"  DESC-eps needs t_pr >= 2*eps_1*sqrt(5.05e9*C_3) = {tpr_need:.6E} (at eps_1 = 6.7e-40, C_3 = 1)")
say(f"  hence  C_D <= sqrt(1/(2*1.655e7*t_pr_need)) = {CD_desc:.6E} / C_3^(1/4)")
say()
say(f"  {'q':>8} {'eta_flat':>12} {'DESC short(dec)':>16} {'C_T ceil (DESC)':>16} {'theta_G':>11}"
    f" {'theta_eps':>11} {'thG/thEps':>11}")
need_eta = D(4) * C3 * EPS1_0 * EPS1_0
for q in QGRID:
    ct, CD, tpr, cut, eff = chain(q)
    eta = tpr * tpr / ETAB_D
    thG = THG8 * D(8) / D(q)
    thE = EPSSTAR_FLOOR / (D(16) * C0_SQ * dpow(D(32), D(1) / D(q)))
    ctc = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(2) * Lam(q))
    say(f"  {q:>8} {eta:>12.4E} {lg(need_eta/eta):>16.3f} {ctc:>16.4E} {thG:>11.4E}"
        f" {thE:>11.4E} {thG/thE:>11.3E}")
q_cross = THG8 * D(8) / (EPSSTAR_FLOOR / (D(16) * C0_SQ))
say(f"  [ADDED] theta_G binds (falls below theta_eps) only for q > {q_cross:.4E}"
    f"  -- theta_eps at eps_* = 1.12e-37 is {EPSSTAR_FLOOR/(D(16)*C0_SQ):.4E} at q -> inf")

say()
say("  P-ct sensitivity (B(4a), STAR_CONST section 6.4 says P-max is the correct convention):")
say(f"  {'q':>8} {'C_T (P-ct)':>14} {'C_D (P-ct)':>14} {'C_T ceil (DESC)':>17} {'clears DESC?':>13}"
    f" {'OBJECTIVE':>11}")
for q in [12, 32, 100, 1000, 10**6]:
    ct, CD, tpr, cut, eff = chain(q, pmax=False)
    ctc = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(2) * Lam(q))
    say(f"  {q:>8} {ct:>14.4E} {CD:>14.4E} {ctc:>17.4E} {str(ct <= ctc):>13} {margin(eff):>11.3f}")
for q in [100, 10**6]:
    ct, CD, tpr, cut, eff = chain(q, cn=D(1), pmax=False)
    ctc = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * D(1) * Lam(q))
    say(f"  c_N=1 {q:>2} {ct:>14.4E} {CD:>14.4E} {ctc:>17.4E} {str(ct <= ctc):>13} {margin(eff):>11.3f}")

# ------------------------------------------------------------------ Block I, CORRECTED
say()
say("BLOCK I (CORRECTED) -- QF1-8 [POST-HOC-HAND]  EPSSTAR l.525's internal consistency")
say(f"  self-consistent t_pr floor = {tpr_need:.6E};  EPSSTAR l.525 states 3.01e-35")
say(f"  ratio = {tpr_need/D('3.01e-35'):.6f};  sqrt(10) = {D(10).sqrt():.6f};"
    f"  ratio/sqrt(10) = {tpr_need/D('3.01e-35')/D(10).sqrt():.6f}")
say(f"  t_pr_need / sqrt(10) = {tpr_need/D(10).sqrt():.6E}  -> rounds to 3.01e-35 exactly")
CD_theirs = (D(1) / (D(2) * CERR_C * D("3.01e-35"))).sqrt()
say(f"  their t_pr -> C_D <= {CD_theirs:.6E} (EPSSTAR l.525 states 3.17e13: reproduced)")
say(f"  self-consistent        C_D <= {CD_desc:.6E};  theirs is {CD_theirs/CD_desc:.4f}x too lenient")
for cn, lab in [(D(2), "c_N=2"), (D(1), "c_N=1")]:
    ctc = (CD_desc - D(2) * B0_SQ) / (D(2) * D("1.011") * cn * Lam(12))
    ctc_theirs = (CD_theirs - D(2) * B0_SQ) / (D(2) * D("1.011") * cn * Lam(12))
    say(f"    at q = 12, {lab}: C_T ceiling = {ctc:.4E}  (EPSSTAR l.525's band says 3.5e10-6.3e10:"
        f" theirs would be {ctc_theirs:.4E})")
QF1_8 = abs(tpr_need - D("3.01e-35")) / D("3.01e-35") < D("0.01")
say(f"  QF1-8: {'PASS' if QF1_8 else 'FAIL'}   (FAIL = EPSSTAR l.525 is NOT self-consistent)")

# ------------------------------------------------------------------ [ADDED] plateau split
say()
say("[ADDED] Where C_T sits at the plateau (P-max, m = 19615) -- what to attack once q is parked")
for q in [8, 12, 100, 10**6]:
    ct, (t1, t2, t3, Chat) = C_T_parts(q, M_TARG)
    say(f"  q = {q:>8}: Chat = {Chat:.6E};  (1/2)(A_s g_s)^a = {t1:.4E} ({t1/Chat:.2%}),"
        f"  (1/2)(A_c g_c)^2 = {t2:.4E} ({t2/Chat:.2%}),  288 C_1 Q = {t3:.4E} ({t3/Chat:.2%})")
say(f"  and 288*C_1*Q at q -> inf is 288*(c_g + 18*(3*c_s*R_0^-2 + 1/(36m))) with c_g = {c_g}")
say(f"     the c_g part alone = {D(288)*c_g:.6E}, i.e. {D(288)*c_g/C_T_parts(10**6,M_TARG)[1][3]:.2%}"
    f" of Chat at the plateau")
say(f"  C_T(plateau, P-max) = {C_T(10**6, M_TARG):.6E};  C_T(plateau, P-ct) = {C_T(10**6, M_TARG, pmax=False):.6E}"
    f";  ratio = {C_T(10**6,M_TARG)/C_T(10**6,M_TARG,pmax=False):.3f} (= B(8)/B(4))")

# ------------------------------------------------------------------ [ADDED] the parametric statement
say()
say("[ADDED] The parametric forms, to be carried beside every number")
say("  a(q)        = q/(q-4)")
say("  C_T(q,m)    = sqrt6 * F * B_tel * [ (1/2)(36 c_s |N_S|)^a + (1/2)(A_c g_c(q,m))^2")
say("                 + 288( c_g + 18( |N_S| c_s R_0^{-2+8/q} + 1/(36m) ) ) ]")
say("  Lambda(q)   = 4 * 2^{2+4/q} * ( 2.47 N sqrt(kappa_+) + 32^{1/q} C_0 )")
say("  C_D(q)      = 2( 1.011 c_N Lambda(q) C_T(q) + B_0 )")
say("  t_pr(q)     = 1 / ( 3.31e7 C_D(q)^2 )")
say("  eps_1^cut(q)= t_pr(q) / ( 2 sqrt(5.05e9 C_3) )")
say("  margin(q)   = log10( a_RS(eps_1^eff(q)) / 1e2 ) - log10( DX' ),  a_RS ∝ eps_1^4")
say()
for q in [12, 32, 100, 200]:
    ct, CD, tpr, cut, eff = chain(q)
    say(f"  q = {q:>4}:  C_T = {ct:.5E}   C_D = {CD:.5E}   t_pr = {tpr:.5E}"
        f"   eps_1^cut = {cut:.5E}   margin = {margin(eff):.3f}")

say()
say("=" * 104)
print("\n".join(out))
