#!/usr/bin/env python3
# es1_eps.py -- (EPS-STAR) session 24.  Pre-registered in checks/es1_criteria.md (14:14 UTC);
# this script was written AFTER that file.  Plain python, exact Fractions + fixed-precision Decimal.
# No numpy, no BLAS, single thread, no numeric lock (exact / decimal arithmetic only).
#
# Every INPUT constant is inherited and listed in es1_criteria.md section 0.  The FORMULAS are
# EPSSTAR.md sections 2-4 (derived by hand, before this script); this script does arithmetic,
# precision control and monotonicity only.
#
# Blocks A-F exactly as pre-registered.  One post-hoc block at the end, labelled [POST-HOC].

from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext
import sys

PREC = int(sys.argv[1]) if len(sys.argv) > 1 else 40
getcontext().prec = PREC + 10

out = []
def say(s=""):
    out.append(s)

def dsqrt(x):
    return x.sqrt()

def dpow(x, y):
    # x>0 Decimal, y Decimal/Fraction-ish -> Decimal, via exp/ln at working precision
    return (D(y) * x.ln()).exp()

def fmt(x, sig=6):
    return f"{D(x):.{sig}E}"

# ---------------------------------------------------------------- inherited inputs
c_s   = D("411.9229708842423061")          # STAR_CONST section 7 (exact)
c_g   = D("5699.632830341894211")          # STAR_CONST section 7 (exact)
N3    = 7**4 * 6                           # 14406   CONST_T section 2.3
N1    = 3**4 * 6                           # 486     CONST_T section 2.3
NS    = 3                                  # STAR_CONST Lemma A2 (source plaquette neighbourhood)
LREV  = 3                                  # STAR_CONST Lemma A2 (source link reverse count)
F_sch = D("175.8")                         # CONST_T section 3.2
SQRT6 = D(6).sqrt()
CEIL  = D("1e13")                          # REVIEW_SQ_S4 S4-16
TARG  = D("3.4e3")                         # STAR_CONST section 8.3
TARG12= D("3.35e3")                        # STAR_CONST section 8.3 at q = 12
EPSFLOOR_S416 = D("5.6e-38")               # REVIEW_SQ_S4 S4-16
THETA_EPS_DEN = D(84)                      # REVIEW_SQ_S4 S4-16: theta_eps = eps_*/84
C_ERR_COEF = D("1.655e7")                  # REVIEW_SQ_S4 S4-16: C_err = 1.655e7 * C_D^2
C_D_PER_CT = D("0.9e3")                    # REVIEW_SQ_S4 S4-16: C_D ~ (0.5-0.9)e3 * C_T (worst end)
EPS1  = D("6.7e-40")                       # RLARGE / REVIEW_SQ_S4 S4-16
R0    = D(64)                              # SQ.md l.1466 (written R_0); 128 as sensitivity
CK_LO, CK_HI = D("3.9"), D("1.92e4")       # STAR_CONST section 4.4/8.1: C_K' SUPPLIED range
cN_LO, cN_HI = D(1), D(2)                  # REVIEW_SQ_S4 S4-16
CK_COEF = D("17.51")                       # STAR_CONST section 8.1: c_K = 17.51*C_K'*c_N
cRB_REF = D("3.0e6")                       # STAR_CONST section 8.1 at (c_N,C_B)=(1,3.6)

QGRID = [10, 11, 12, 16, 24, 32, 50, 100]

say("=" * 100)
say(f"es1_eps.py  --  (EPS-STAR) session 24.  Decimal precision = {PREC} significant digits")
say("Criteria: checks/es1_criteria.md (pre-registered).  Formulas: EPSSTAR.md sections 2-4.")
say("=" * 100)

# ---------------------------------------------------------------- Block A: the beta telescope
say()
say("BLOCK A -- the beta telescope B(m) = prod_i (p_i-1)^(m/p_i), p_i = 2^(i+1)")
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
say(f"  B(4) = {B4:.6f}     CONST_T section 3.1 says 43.95   rel.dev = {abs(B4-D('43.95'))/D('43.95'):.2E}")
say(f"  B(8) = {B8:.4f}   CONST_T section 3.1 says 1931.5   rel.dev = {abs(B8-D('1931.5'))/D('1931.5'):.2E}")
ES1_1 = (abs(B4 - D("43.95")) / D("43.95") < D("0.005")) and (abs(B8 - D("1931.5")) / D("1931.5") < D("0.005"))
say(f"  ES1-1: {'PASS' if ES1_1 else 'FAIL'}")

# ---------------------------------------------------------------- Block B: Stage 1 constant
say()
say("BLOCK B -- the Stage-1 constant C_S1(q,m), and exact scale-invariance")
say("  C_S1(q,m)^2 = [1 - 1/4 - 1/(4m)]^{-1} * [ c_theta*(27*c_s)^a + 4096*c_g ],")
say("     a = q/(q-4),  theta = 4/q,  c_theta = (1-theta)*(4*theta)^{theta/(1-theta)}")

# exact scale-invariance identity: (-2 + 8/q) * q/(q-4) == -2
si_ok = True
for q in QGRID:
    lhs = (Fr(-2) + Fr(8, q)) * Fr(q, q - 4)
    if lhs != Fr(-2):
        si_ok = False
    say(f"    q = {q:4d}:  (-2 + 8/q)*q/(q-4) = {lhs}   {'OK' if lhs == Fr(-2) else 'MISMATCH'}")

def c_theta(q):
    th = D(4) / D(q)
    a = D(1) / (1 - th)
    return (1 - th) * dpow(4 * th, th / (1 - th)), a, th

def C_S1(q, m):
    ct, a, th = c_theta(q)
    inner = ct * dpow(27 * c_s, a) + D(4096) * c_g
    frac = D(1) - D(1) / D(4) - D(1) / (D(4) * D(m))
    return (inner / frac).sqrt(), inner, frac

cs1_12_1, inner12, _ = C_S1(12, 1)
say(f"  at q = 12: c_theta = {c_theta(12)[0]:.8f}, a = 3/2, bracket = {inner12:.8E}")
say(f"  C_S1(12, m=1)   = {cs1_12_1:.6f}      (m = 1 is Stage 1's absorption exactly as written)")
for m in [1, 8, 100, 20000]:
    v, _, _ = C_S1(12, m)
    say(f"  C_S1(12, m={m:<6d}) = {v:.6f}")
ES1_2 = si_ok and (cs1_12_1 < D("1e5"))
say(f"  ES1-2: {'PASS' if ES1_2 else 'FAIL'}  (exact scale-invariance {si_ok}, C_S1(12,1) < 1e5)")

# ---------------------------------------------------------------- Block C: the uniform bound
say()
say("BLOCK C -- the uniform bound  A_c*gamma_c <= (1+sqrt6)*C_S1(q,m)/m")
say("  It contains NO c_K, c_RB, C_B, C_K' or c_N: that is the uniformity claim.")
ONE_P_S6 = 1 + SQRT6
def Acgc_bound(q, m):
    v, _, _ = C_S1(q, m)
    return ONE_P_S6 * v / D(m)

for m in [1, 2, 4, 6, 7, 8, 10, 100, 1000, 10000, 20000, 25000]:
    say(f"    m = {m:>6d}:  A_c*gamma_c <= {Acgc_bound(12, m):.6E}")

m_targ = None
for m in range(1, 1001):
    if Acgc_bound(12, m) <= TARG12:
        m_targ = m
        break
m_one = None
for m in range(1, 1000001):
    if Acgc_bound(12, m) <= D(1):
        m_one = m
        break
say(f"  smallest integer m with bound <= 3.35e3 (q=12): m = {m_targ}, bound = {Acgc_bound(12, m_targ):.6E}")
say(f"  smallest integer m with bound <= 1:             m = {m_one}, bound = {Acgc_bound(12, m_one):.6E}")
ES1_3 = (m_targ is not None and m_targ <= 1000)
ES1_3b = (m_one is not None and m_one <= 10**6)
say(f"  ES1-3:  {'PASS' if ES1_3 else 'FAIL'}")
say(f"  ES1-3b: {'PASS' if ES1_3b else 'FAIL'}")

# monotone in m?
mono_m = all(Acgc_bound(12, m) >= Acgc_bound(12, m + 1) for m in range(1, 200))
say(f"  bound non-increasing in m on m = 1..200: {mono_m}")

# ---------------------------------------------------------------- Block D: C_T
say()
say("BLOCK D -- C_T = sqrt6 * F * B_tel * [ (1/2)(A_s*gamma_s)^a + (1/2)(A_c*gamma_c)^2 + 288*C_1*Q ]")
say("  A_s*gamma_s = 36*c_s*|N| with |N| = 3 (M-sharp, STAR_CONST Lemma A2) or 486 (M-ct, CONST_T section 2.3)")
say("  288*C_1*Q   = 288*[ c_g + 18*( |N_S|*c_s*||V_s||_inf + 1/(36m) ) ],  ||V_s||_inf <= R_0^(-2+8/q)")

def Qterm(q, m, r0=R0, Nsrc=NS):
    Vs = dpow(r0, D(-2) + D(8) / D(q))
    return D(288) * (c_g + D(18) * (D(Nsrc) * c_s * Vs + D(1) / (D(36) * D(m))))

def C_T(q, m, pmax=True, Nsrc=NS, acgc=None, r0=R0):
    ct, a, th = c_theta(q)
    Asgs = D(36) * c_s * D(Nsrc)
    if acgc is None:
        acgc = Acgc_bound(q, m)
    Btel = B8 if pmax else B(4 * float(a)) if False else (B8 if pmax else None)
    if not pmax:
        Btel = B(4 * (D(q) / D(q - 4)))
    Chat = dpow(Asgs, a) / 2 + acgc * acgc / 2 + Qterm(q, m, r0, Nsrc)
    return SQRT6 * F_sch * Btel * Chat, Chat, acgc, Asgs

say()
say("  M-sharp (|N| = 3), P-max (B(8)), at the two margins:")
say(f"  {'q':>5} {'a':>8} {'A_c*g_c':>12} {'Chat':>14} {'C_T (m=m_targ)':>18} {'C_T (m=m_one)':>18}")
rows = []
for q in QGRID:
    ct1, Ch1, ac1, _ = C_T(q, m_targ)
    ct2, Ch2, ac2, _ = C_T(q, m_one)
    a = D(q) / D(q - 4)
    say(f"  {q:>5} {a:>8.4f} {ac1:>12.4E} {Ch1:>14.6E} {ct1:>18.6E} {ct2:>18.6E}")
    rows.append((q, ct1, ct2))

ct12_one = C_T(12, m_one)[0]
ct12_targ = C_T(12, m_targ)[0]
ES1_4 = ct12_one <= CEIL
ES1_4b = ct12_targ <= CEIL
say(f"  ES1-4  (q=12, m={m_one}):     C_T = {ct12_one:.6E}  vs ceiling 1e13  -> {'PASS' if ES1_4 else 'FAIL'}")
say(f"  ES1-4b (q=12, m={m_targ}):        C_T = {ct12_targ:.6E}  vs ceiling 1e13  -> {'PASS' if ES1_4b else 'FAIL'}")

say()
say("  sensitivity: the SAME numbers must come out for every C_K' and C_B in their SUPPLIED ranges,")
say("  because none of them appears in Block C or Block D.  Explicit re-evaluation:")
for ckp in [CK_LO, CK_HI]:
    for cn in [cN_LO, cN_HI]:
        cK = CK_COEF * ckp * cn
        # C_T does not take cK as an argument at all; demonstrate by recomputation
        v = C_T(12, m_one)[0]
        say(f"    C_K' = {ckp:>9}, c_N = {cn}:  c_K = {cK:.4E}   C_T(q=12) = {v:.6E}  (identical)")

say()
say("  comparison readings (not the verdict):")
for Nsrc, lab in [(3, "M-sharp |N|=3"), (486, "M-ct |N|=486")]:
    for pmax, plab in [(True, "P-max B(8)"), (False, "P-ct B(4a)")]:
        v = C_T(12, m_one, pmax=pmax, Nsrc=Nsrc)[0]
        say(f"    q=12  {lab:<16} {plab:<12} C_T = {v:.4E}")
say(f"    q=12  M-sharp, P-max, R_0 = 128 instead of 64: C_T = {C_T(12, m_one, r0=D(128))[0]:.4E}")

# q-monotonicity under P-max
mono_q = all(rows[i][2] >= rows[i + 1][2] for i in range(len(rows) - 1))
say(f"  C_T(q) non-increasing in q on the grid (P-max, m=m_one): {mono_q}")

# ---------------------------------------------------------------- Block E: eps_* and the floors
say()
say("BLOCK E -- the value of eps_*, and the audit floors")
say("  Stage-1 absorption at margin m:  9*|N_3|*c_K*eps + 9*sqrt(|N_3|)*|N_1|*c_RB*eps^2 <= 1/(4m)")
say("  -> eps_*(m, c_K, c_RB) = the positive root")

def eps_star(m, cK, cRB):
    A = D(9) * D(N3).sqrt() * D(N1) * cRB     # quadratic coefficient
    Bq = D(9) * D(N3) * cK                    # linear coefficient
    C = -D(1) / (D(4) * D(m))
    disc = Bq * Bq - 4 * A * C
    return (-Bq + disc.sqrt()) / (2 * A)

# the no-change floor: eps_* >= 84 * theta_0^SUP, theta_0^SUP = 1/(2*C_err), C_err = 1.655e7*C_D^2
C_D = C_D_PER_CT * ct12_one
theta0_sup = D(1) / (D(2) * C_ERR_COEF * C_D * C_D)
nochange_floor = THETA_EPS_DEN * theta0_sup
say(f"  C_T(q=12) = {ct12_one:.4E} -> C_D = {C_D:.4E} (worst end)  <= 6.7e15 ? {C_D <= D('6.7e15')}")
say(f"  theta_0^SUP = 1/(2*C_err) = {theta0_sup:.4E};  t_pr = theta_0^SUP;  eps_1 = {EPS1}")
say(f"  eps_1 < t_pr ? {EPS1 < theta0_sup}  (margin x{theta0_sup/EPS1:.3f})")
say(f"  NO-CHANGE FLOOR on eps_*: 84*theta_0^SUP = {nochange_floor:.4E}")
say(f"  REVIEW_SQ_S4 S4-16 floor (t_pr > eps_1 through theta_eps): {EPSFLOOR_S416}")
say()
say(f"  {'C_K prime':>10} {'c_N':>4} {'c_K':>12} {'eps_*(m_targ)':>16} {'eps_*(m_one)':>16} {'decades over no-change floor':>30}")
es1_5 = True
es1_5b = True
for ckp in [CK_LO, CK_HI]:
    for cn in [cN_LO, cN_HI]:
        cK = CK_COEF * ckp * cn
        e1 = eps_star(m_targ, cK, cRB_REF)
        e2 = eps_star(m_one, cK, cRB_REF)
        dec = (e2 / nochange_floor).log10()
        say(f"  {ckp:>10} {cn:>4} {cK:>12.4E} {e1:>16.4E} {e2:>16.4E} {dec:>30.2f}")
        if not (e2 > EPSFLOOR_S416 and e1 > EPSFLOOR_S416):
            es1_5 = False
        if not (e2 > nochange_floor and e1 > nochange_floor):
            es1_5b = False
say(f"  ES1-5:  {'PASS' if es1_5 else 'FAIL'}   (both margins, both ends of C_K' x c_N, above 5.6e-38)")
say(f"  ES1-5b: {'PASS' if es1_5b else 'FAIL'}  (same, above the no-change floor 84*theta_0^SUP)")

say()
say("  C_B sensitivity of eps_* only (C_T is unaffected):  c_RB = 17.51*290*(576*c_N^2 + C_B^2*c_N^4)")
for CB in [D("3.6"), D("1e2"), D("1e4")]:
    for cn in [cN_HI]:
        cRB = D("17.51") * D(290) * (D(576) * cn * cn + CB * CB * cn**4)
        cK = CK_COEF * CK_HI * cn
        e2 = eps_star(m_one, cK, cRB)
        say(f"    C_B = {CB:>8}, c_N = {cn}: c_RB = {cRB:.4E}  eps_*(m_one) = {e2:.4E}  above floor? {e2 > nochange_floor}")

# A_c*gamma_c increasing in eps_* at fixed c_K (monotonicity leg of ES1-6)
def acgc_direct(q, m, cK, cRB, eps):
    v, _, _ = C_S1(q, m)
    pref = D(36) * dpow(D(N3), D(3) / D(4)) * ONE_P_S6 * v
    return pref * (cK * dpow(D(N3), D(1) / D(4)) * eps + cRB * dpow(D(N1), D(1) / D(4)) * eps * eps)

cK_t = CK_COEF * CK_HI * cN_HI
e_ref = eps_star(m_one, cK_t, cRB_REF)
mono_eps = True
prev = None
say()
say("  direct A_c*gamma_c(eps_*) at c_K = 17.51*1.92e4*2, c_RB = 3.0e6, m = m_one:")
for k in range(6):
    e = e_ref / (D(10) ** k)
    v = acgc_direct(12, m_one, cK_t, cRB_REF, e)
    say(f"    eps_* = {e:.4E}  ->  A_c*gamma_c = {v:.6E}")
    if prev is not None and not (v <= prev):
        mono_eps = False
    prev = v
say(f"  at eps_* = eps_*(m_one) the direct value is {acgc_direct(12,m_one,cK_t,cRB_REF,e_ref):.6E},")
say(f"  and the uniform bound is {Acgc_bound(12,m_one):.6E}  -> direct <= uniform ? "
    f"{acgc_direct(12,m_one,cK_t,cRB_REF,e_ref) <= Acgc_bound(12,m_one)}")

ES1_6 = mono_m and mono_q and mono_eps
say(f"  ES1-6: {'PASS' if ES1_6 else 'FAIL'}  (monotone in m: {mono_m}; in q: {mono_q}; in eps_*: {mono_eps})")

# ---------------------------------------------------------------- summary
say()
say("=" * 100)
say("VERDICT SUMMARY (pre-registered ids)")
for k, v in [("ES1-1", ES1_1), ("ES1-2", ES1_2), ("ES1-3", ES1_3), ("ES1-3b", ES1_3b),
             ("ES1-4", ES1_4), ("ES1-4b", ES1_4b), ("ES1-5", es1_5), ("ES1-5b", es1_5b),
             ("ES1-6", ES1_6)]:
    say(f"  {k:<8} {'PASS' if v else 'FAIL'}")
say(f"  ES1-7   requires diff against the {PREC}-vs-60-digit run; see es1_out*.txt")
say("=" * 100)

# ---------------------------------------------------------------- [POST-HOC]
say()
say("[POST-HOC, ES1-P1] -- written after reading the Block C/D output.  Not pre-registered.")
say("  How much of the 1e13 ceiling does each term of Chat use, at q = 12, m = m_one?")
ct, a, th = c_theta(12)
Asgs = D(36) * c_s * D(NS)
t1 = dpow(Asgs, a) / 2
t2 = Acgc_bound(12, m_one) ** 2 / 2
t3 = Qterm(12, m_one)
tot = t1 + t2 + t3
for lab, t in [("(1/2)(A_s g_s)^a", t1), ("(1/2)(A_c g_c)^2", t2), ("288 C_1 Q", t3)]:
    say(f"    {lab:<20} = {t:>14.6E}   {100*t/tot:>6.2f} %  of Chat")
say(f"    Chat = {tot:.6E};  C_T = {SQRT6*F_sch*B8*tot:.6E}")
say("  So the V_c branch is no longer a contributor at all: the ceiling is set by the SOURCE term.")

print("\n".join(out))
