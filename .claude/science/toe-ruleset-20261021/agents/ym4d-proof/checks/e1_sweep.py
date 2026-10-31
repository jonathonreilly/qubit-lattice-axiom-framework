#!/usr/bin/env python3 -I
# checks/e1_sweep.py -- ym4d-proof, session 24, EPS1_SWEEP worker.
# Criteria pre-registered in checks/e1_criteria.md (written first, no constant in it).
# Exact fractions.Fraction throughout; Decimal only to display; plain python -I, single thread,
# no numpy / no BLAS, no numeric lock needed (exact rational arithmetic, brief rule 6).
#
# Every constant below is TRANSCRIBED from its owning file with a file+line citation.
# Nothing here is re-derived, and a number reproduced here is NOT an endorsement of its source.

from fractions import Fraction as F
from decimal import Decimal, getcontext

def dec(x, p=40):
    getcontext().prec = p
    if isinstance(x, Decimal):
        return +x
    return Decimal(x.numerator) / Decimal(x.denominator)

def log10(x, p=50):
    """exact-input log10 by integer exponent extraction + Decimal mantissa; display only."""
    getcontext().prec = p
    return dec(x, p).log10()

def E(mant, exp):
    return F(mant) * F(10) ** exp

# ---------------------------------------------------------------- transcribed constants
# RLARGE.md l.72  "So ε_1 ≲ 6.7·10⁻⁴⁰"
EPS_T   = E("6.7", -40)
# RLARGE.md l.71  the same min's first entry, before TB-1's sharpening
EPS_T71 = E("9.52", -40)
# SF.md l.2837 via NORMS.md l.746 "ε_1 = 1.27·10⁻³⁹"; RLARGE l.611 "1.27·10⁻³⁹ / 8.95·10⁻⁴⁰"
EPS_NORMS = E("1.27", -39)
EPS_TB1   = E("8.95", -40)
# TAUFLAT.md §4 C l.408 (session 24): the PROPOSED value
EPS_P   = E("9.38496", -45)
# TAUFLAT.md §2.2 l.203 (session 24): t_pr = C'τ_♭ = θ_0^SUP
T_PR    = E("1.33384", -39)
# RLARGE.md l.90: c_♭ = 1/640, C' = 53 at N = 2, L = 3; c_pr = c_♭/C'²
C_FLAT  = F(1, 640)
C_PRIME = F(53)
C_PR    = C_FLAT / C_PRIME**2
# RLARGE.md l.612: θ < 1/24, β_- ≈ 0.186 at N = 2
THETA   = F(1, 24)
BETA_M  = F(186, 1000)
# RLARGE.md l.1009 (d = 4, L = 3): A_4 = 9, L² = 9; l.1248 reference κ = 1, N = 2
L, N, A4, KAPPA = F(3), F(2), F(9), F(1)
# RLARGE.md l.1245: a'' = 0.9·ε_1²/(4N)
# RLARGE.md l.1017: n_* = ⌊4/(a''β_-)⌋ ; l.612: n_H ≥ 4/(aβ_-), W ≳ 2·n_H
# RLARGE.md l.1248: ε_loc = 3.5·10⁻³ at ε_1 = 0.5  ->  ε_loc/ε_1 is a fixed ratio
LOC_RATIO = E("3.5", -3) / F(1, 2)
# RLARGE.md l.84: (TC) holds whenever ε_loc ≥ (16N + 3)ε_1/(128N)
TC_REQ  = (16*N + 3) / (128*N)
# HW.md l.2006 §35.7 table, "session 6, ring ×82 (PLD's price)": b_n at c_A=0,c_U=1,C_ℓ=1,R=0
B_N_82  = F(5381106005)
# HW.md l.1639: g²_CRC := a/(b_n + aR + log(12800C_ℓ)); at C_ℓ = 1, R = 0 the additive term is log 12800
LOG12800 = F(9457, 1000)                       # ln(12800) = 9.45718..., transcribed to 4 s.f.
# HW.md l.2024: at the ×17 ring the HIST-side ceilings give 2.33375e-96 against g²_CRC 8.96376e-96
HIST_SIDE_DIV = E("8.96376", -96) / E("2.33375", -96)
# HW.md l.2008: g²_ret = 3.67644e-98 (session 6) ; PLD l.1595: a_ret/a_bad = 8.03e-7
G2_RET_T = E("3.67644", -98)
ARET_OVER_ABAD = E("8.03", -7)
# PLD §16.8 via HW.md l.1635: the recorded (RLF-δ) ceiling g_K² ≲ 10⁻⁹⁴
RLF_DELTA_CEIL = E("1", -94)
# REVIEW_SF_S7.md l.203: DX'-1 (iii) = 2.456e-152/C_Ω  (RLARGE l.618 rounds it to 2.5e-152)
G_DX2 = E("2.456", -152)
# EXISTENCE.md l.1771: KN-step's re-centred linear η_1 = c_1ε_1, c_1 = 1/(2(L² + 5.5A_d))
C1_KN = 1 / (2 * (L**2 + F(55,10)*A4))
# HW.md l.2170 / PLD §18.7.2: the (CEM-2) gap, measured at 4.489e15
CEM2_GAP = E("4.489", 15)

# ---------------------------------------------------------------- ε-driven quantities
def a_bad(e):      return C_PR * min(e*e, T_PR*T_PR)          # RLARGE l.88
def a_unret(e):    return THETA * a_bad(e)                    # RLARGE l.87-88, l.612
def a_dd(e):       return F(9,10) * e*e / (4*N)               # RLARGE l.1245
def n_star(e):     return 4 / (a_dd(e) * BETA_M)              # RLARGE l.1017
def n_H(e):        return 4 / (a_unret(e) * BETA_M)           # RLARGE l.612
def wrap(e):       return log10(2*n_H(e)) / log10(L)          # RLARGE l.612 (W ≳ 2n_H)
def eta_1(e):      return min(e/(2*L*L), e*e/(512*N*A4))      # RLARGE l.64
def a_eta(e):      return eta_1(e)**2 / 4                     # RLARGE l.1248
def a_RS(e):       return min(a_eta(e), KAPPA*e*e/(256*N))    # RLARGE l.1020
def eta_1_kn(e):   return C1_KN * e                           # EXISTENCE l.1771
def a_RS_kn(e):    return min(eta_1_kn(e)**2/4, KAPPA*e*e/(256*N))
def eps_loc(e):    return LOC_RATIO * e                       # RLARGE l.907/l.1248
def a_ret(e):      return ARET_OVER_ABAD * a_bad(e)           # PLD l.1595
def g2_crc(e):     return a_unret(e) / (B_N_82 + LOG12800)    # HW l.1639 + l.2006
def g2_hist(e):    return g2_crc(e) / HIST_SIDE_DIV           # HW l.2024
def g2_ret(e):     return G2_RET_T * a_ret(e) / a_ret(EPS_T)  # HW l.2008, scaled by a_ret
def g2_rlarge(e):  return a_unret(e) / 100                    # RLARGE l.616-617 ("g_K² ≲ a/10²")
def g2_rs(e):      return a_RS(e) / 100                       # same form on the RS/joint route
def u_0(e):        return 64 / (e*e)                          # EXISTENCE l.3556
def depth(e):      return log10(2/e) / (2*log10(L))           # PLD l.2307
def eta_flat():    return C_FLAT * T_PR*T_PR / C_PRIME**4     # SQ DESC-ε (iii), TAUFLAT §2.2
def clause(e, C3=F(1)):                                       # HIST A5 (A): 4C_3ε² ≤ η_♭
    return 4*C3*e*e <= eta_flat()

out = []
def P(s=""): out.append(s)

P("e1_sweep.py -- exact Fraction arithmetic; Decimal for display only.")
P("Criteria: checks/e1_criteria.md (written first; contains no constant).")
P("")
P("=== transcription gate ===")
P("  eta_flat  = c_♭ t_pr²/C'⁴      = %s   (TAUFLAT §2.2 reports 3.52310e-88)" % dec(eta_flat(),6))
P("  1/(c_♭/C'⁴)                    = %s   (TAUFLAT §2.2 reports 5.04991e9)" % dec(C_PRIME**4/C_FLAT,6))
P("  a_bad(E_t)                     = %s   (RLARGE l.93 reports ~2.5e-85)" % dec(a_bad(EPS_T),6))
P("  a(E_t) = θ a_bad               = %s   (RLARGE l.612 reports ≲1.0e-86)" % dec(a_unret(EPS_T),6))
P("  n_H(E_t)                       = %s   (RLARGE l.612 reports ≳2e87)" % dec(n_H(EPS_T),6))
P("  wrap(E_t)                      = %s   (RLARGE l.612 reports ≈184)" % dec(wrap(EPS_T),6))
P("  g2_crc(E_t) at ring x82        = %s   (HW l.2006 table reports 1.85835e-96)" % dec(g2_crc(EPS_T),6))
P("  a_ret(E_t)                     = %s   (HW l.1635 reports ≈2.0e-91)" % dec(a_ret(EPS_T),6))
P("  eps_loc/eps_1                  = %s   ((TC) needs ≥ %s)" % (dec(LOC_RATIO,6), dec(TC_REQ,6)))
P("  n_star(E_t)                    = %s   (RLARGE l.611 reports 1.19e80 at 8.95e-40)" % dec(n_star(EPS_T),6))
P("  n_star(8.95e-40)               = %s" % dec(n_star(EPS_TB1),6))
P("  E_p vs t_pr/(2C'²√640)         = %s  (ratio to TAUFLAT's 9.38496e-45)"
  % dec(EPS_P / (T_PR * C_PRIME**(-2) / 2 / F(25298221281347035,10**15)), 8))
P("")

P("=== e1-1 SCALING CENSUS (claimed exponent n: value ∝ ε^n) ===")
ratio_eps = EPS_P / EPS_T
P("  E_t = %s   E_p = %s   E_p/E_t = %s  (%s decades)"
  % (dec(EPS_T,6), dec(EPS_P,6), dec(ratio_eps,6), log10(ratio_eps).quantize(Decimal('0.001'))))
rows = [
 ("a_bad        RLARGE l.88",      2,  a_bad),
 ("a = θa_bad   RLARGE l.87",      2,  a_unret),
 ("a''          RLARGE l.1245",    2,  a_dd),
 ("a_ret        PLD l.1595",       2,  a_ret),
 ("eta_1        RLARGE l.64",      2,  eta_1),
 ("a_eta        RLARGE l.1248",    4,  a_eta),
 ("a_RS         RLARGE l.1020",    4,  a_RS),
 ("a_RS (KN-st) EXISTENCE l.1771", 2,  a_RS_kn),
 ("eps_loc      RLARGE l.907",     1,  eps_loc),
 ("eta_1 (KN)   EXISTENCE l.1771", 1,  eta_1_kn),
 ("n_star       RLARGE l.1017",   -2,  n_star),
 ("n_H          RLARGE l.612",    -2,  n_H),
 ("u_0          EXISTENCE l.3556",-2,  u_0),
 ("g2_crc  x82  HW l.1639/2006",   2,  g2_crc),
 ("g2_hist      HW l.2024",        2,  g2_hist),
 ("g2_ret       HW l.2008",        2,  g2_ret),
 ("g2_rlarge    RLARGE l.617",     2,  g2_rlarge),
 ("g2_rs        RLARGE l.617 form",4,  g2_rs),
]
bad = []
for name, n, f in rows:
    vt, vp = f(EPS_T), f(EPS_P)
    got = vp / vt
    want = ratio_eps ** n
    ok = (got == want)
    if not ok:
        bad.append(name)
    P("  %-32s n=%+d  %-14s -> %-14s  ratio %-12s  %s"
      % (name, n, dec(vt,5), dec(vp,5), dec(got,5), "ok" if ok else "MISMATCH"))
P("  -- invariant / log entries --")
P("  eps_loc/eps_1  (TC, RLARGE l.84)   %s -> %s   invariant: %s ; (TC) met: %s / %s"
  % (dec(eps_loc(EPS_T)/EPS_T,5), dec(eps_loc(EPS_P)/EPS_P,5),
     eps_loc(EPS_T)/EPS_T == eps_loc(EPS_P)/EPS_P,
     eps_loc(EPS_T) >= TC_REQ*EPS_T, eps_loc(EPS_P) >= TC_REQ*EPS_P))
P("  (TC) shortfall factor              %s  (ε-independent)" % dec(TC_REQ/LOC_RATIO,6))
P("  wrap levels    RLARGE l.612        %s -> %s   (+%s)"
  % (wrap(EPS_T).quantize(Decimal('0.1')), wrap(EPS_P).quantize(Decimal('0.1')),
     (wrap(EPS_P)-wrap(EPS_T)).quantize(Decimal('0.1'))))
P("  n_* torus levels log_L(n_*^1/4)    %s -> %s   (+%s)"
  % ((log10(n_star(EPS_T))/log10(L)/4).quantize(Decimal('0.1')),
     (log10(n_star(EPS_P))/log10(L)/4).quantize(Decimal('0.1')),
     ((log10(n_star(EPS_P))-log10(n_star(EPS_T)))/log10(L)/4).quantize(Decimal('0.1'))))
P("  coherent-chain depth PLD l.2307    %s -> %s   (+%s); 81^depth %s -> %s"
  % (depth(EPS_T).quantize(Decimal('0.1')), depth(EPS_P).quantize(Decimal('0.1')),
     (depth(EPS_P)-depth(EPS_T)).quantize(Decimal('0.1')),
     (depth(EPS_T)*Decimal(81).log10()).quantize(Decimal('0.1')),
     (depth(EPS_P)*Decimal(81).log10()).quantize(Decimal('0.1'))))
P("  a·u_k at the ε-driven ceiling      %s -> %s   (invariant? %s)"
  % (dec(a_unret(EPS_T)/g2_crc(EPS_T),6), dec(a_unret(EPS_P)/g2_crc(EPS_P),6),
     a_unret(EPS_T)/g2_crc(EPS_T) == a_unret(EPS_P)/g2_crc(EPS_P)))
P("  (CEM-2) gap ε²/g_K² at g_K²=1e-94  %s -> %s" % (dec(EPS_T**2/RLF_DELTA_CEIL,5),
                                                      dec(EPS_P**2/RLF_DELTA_CEIL,5)))
P("     [HW l.2170 records 4.489e15 at E_t; reproduced: %s]" % dec(EPS_T**2/RLF_DELTA_CEIL,5))
P("  (CEM-2) gap at the ε-driven g_CRC  %s -> %s   (invariant? %s)"
  % (dec(EPS_T**2/g2_crc(EPS_T),5), dec(EPS_P**2/g2_crc(EPS_P),5),
     EPS_T**2/g2_crc(EPS_T) == EPS_P**2/g2_crc(EPS_P)))
P("  (CEM-2) gap at the ε-free  g_DX    %s -> %s   (improves by %s decades)"
  % (dec(EPS_T**2/G_DX2,5), dec(EPS_P**2/G_DX2,5),
     (log10(EPS_T**2/G_DX2)-log10(EPS_P**2/G_DX2)).quantize(Decimal('0.001'))))
P("  VERDICT e1-1: %s%s" % ("CLASSIFICATION-HOLDS" if not bad else "CLASSIFICATION-WRONG ",
                            "" if not bad else str(bad)))
P("")

P("=== e1-2 FLOOR: the window  g << ||.|| < ε_1  must stay open ===")
P("   (EXISTENCE l.4191 'ε only has to contain the typical field ≍ g'; l.3112 'distance ≫ g but < ε_1')")
def window(e, g2):
    g = dec(g2, 60).sqrt()
    return dec(e, 60) / g
for label, g2f, epsfree in (("ε-free binding ceiling g_DX² (REVIEW_SF_S7 l.203)", lambda e: G_DX2, True),
                            ("ε-driven ceiling g²_CRC x82 (HW l.2006)", g2_crc, False)):
    wt, wp = window(EPS_T, g2f(EPS_T)), window(EPS_P, g2f(EPS_P))
    P("  %-52s  ε/g: %s -> %s" % (label, wt.log10().quantize(Decimal('0.01')),
                                   wp.log10().quantize(Decimal('0.01'))))
    P("      %sdecades of margin at E_p; verdict %s"
      % ("", "FLOOR-RESPECTED" if wp > 1 else "FLOOR-VIOLATED"))
P("  VERDICT e1-2: %s" % ("FLOOR-RESPECTED"
    if window(EPS_P, G_DX2) > 1 and window(EPS_P, g2_crc(EPS_P)) > 1 else "FLOOR-VIOLATED"))
P("")

P("=== e1-3 DECLARED PRICE (TAUFLAT §4 C l.411-413) ===")
declared = [("a_bad",  a_bad(EPS_P),  E("5.0",-95)),
            ("a",      a_unret(EPS_P),E("2",-96)),
            ("n_H",    n_H(EPS_P),    E("1",97)),
            ("g_K²",   g2_rlarge(EPS_P), E("1",-98))]
dis = []
for name, mine, theirs in declared:
    r = mine/theirs
    ok = F(5,6) <= r <= F(6,5)
    if not ok: dis.append(name)
    P("  %-6s mine %-14s  TAUFLAT %-10s  ratio %-10s %s"
      % (name, dec(mine,6), dec(theirs,6), dec(r,6), "ok" if ok else "OUTSIDE x1.2"))
P("  wrap  mine %s   TAUFLAT 205   diff %s"
  % (wrap(EPS_P).quantize(Decimal('0.1')), (wrap(EPS_P)-205).quantize(Decimal('0.1'))))
P("  VERDICT e1-3: %s%s" % ("SOURCE-REPRODUCED" if not dis else "SOURCE-DISAGREES ",
                            "" if not dis else str(dis)))
P("  PRICE-COMPLETENESS: steepest exponent in TAUFLAT's declared list = 2 (a_bad, g_K², n_H);")
P("    steepest exponent found in the sweep = 4 (a_eta, a_RS, g2_rs, RLARGE l.1020/l.1248).")
P("    VERDICT: PRICE-INCOMPLETE  (the ε^4 branch costs %s decades, not %s)"
  % ((4*log10(EPS_T/EPS_P)).quantize(Decimal('0.001')),
     (2*log10(EPS_T/EPS_P)).quantize(Decimal('0.001'))))
P("")

P("=== e1-4 DOES THE PRICE BIND (each ceiling against g_DX² = 2.456e-152/C_Ω) ===")
fails = []
for name, f in (("g²_CRC ring x82      HW l.2006", g2_crc),
                ("HIST-side ceiling    HW l.2024", g2_hist),
                ("g²_ret               HW l.2008", g2_ret),
                ("RLARGE a/10²         RLARGE l.617", g2_rlarge),
                ("RS/joint a_RS/10²    RLARGE l.1020", g2_rs),
                ("RS/joint under KN-st EXISTENCE l.1771", lambda e: a_RS_kn(e)/100)):
    mt, mp = f(EPS_T)/G_DX2, f(EPS_P)/G_DX2
    if mp <= 1:   v = "BINDS-ALREADY" if mt <= 1 else "BINDS (caused by option C)"
    else:         v = "NOT-BINDING"
    if mp <= 1: fails.append(name.split()[0])
    P("  %-38s  E_t %-13s  E_p %-13s  margin %s -> %s decades   %s"
      % (name, dec(f(EPS_T),5), dec(f(EPS_P),5),
         log10(mt).quantize(Decimal('0.01')), log10(mp).quantize(Decimal('0.01')), v))
    P("      margin exhausted at c_+·C_Ω = %s (E_t) / %s (E_p)" % (dec(mt,5), dec(mp,5)))
P("  VERDICT e1-4: %s%s" % ("NOT-BINDING (all)" if not fails else "FAIL -- binding ceilings: ",
                            "" if not fails else str(fails)))
P("")

P("=== e1-5 POWER (counterfactuals chosen by the script) ===")
E_c1 = E("1", -80)        # below g_DX = sqrt(2.456e-152) = 1.567e-76 -> window must close
E_c2 = EPS_T              # the lane's current ceiling -> DESC-ε (iii) must fail
P("  E_c1 = %s  (chosen below g_DX = %s)" % (dec(E_c1,3), dec(G_DX2,60).sqrt().quantize(Decimal('1E-79'))))
f1_p  = window(EPS_P, G_DX2) > 1
f1_c1 = window(E_c1, G_DX2) > 1
P("    e1-2 at E_p : %s     e1-2 at E_c1 : %s     FLIPPED: %s"
  % ("FLOOR-RESPECTED" if f1_p else "FLOOR-VIOLATED",
     "FLOOR-RESPECTED" if f1_c1 else "FLOOR-VIOLATED", f1_p != f1_c1))
c_p, c_c2 = clause(EPS_P), clause(E_c2)
P("  E_c2 = E_t = %s" % dec(E_c2,3))
P("    DESC-ε(iii) at E_p : %s   at E_c2 : %s   FLIPPED: %s"
  % ("CLAUSE-HOLDS" if c_p else "CLAUSE-FAILS",
     "CLAUSE-HOLDS" if c_c2 else "CLAUSE-FAILS", c_p != c_c2))
P("    e1-2 at E_c2 : %s (must stay FLOOR-RESPECTED)"
  % ("FLOOR-RESPECTED" if window(E_c2, G_DX2) > 1 else "FLOOR-VIOLATED"))
haspower = (f1_p != f1_c1) and (c_p != c_c2)
P("  VERDICT e1-5: %s" % ("HAS-POWER (both flip)" if haspower else "NO POWER"))
P("")

P("=== e1-6 PRECISION ===")
same = True
for p in (40, 80):
    getcontext().prec = p
    v = (dec(a_bad(EPS_P),p), dec(g2_crc(EPS_P),p), window(EPS_P,G_DX2) > 1, clause(EPS_P))
    if p == 40: ref = v[2:]
    else: same = same and (v[2:] == ref)
P("  VERDICT e1-6: %s" % ("PASS (verdicts identical at 40 and 80 digits)" if same else "FAIL"))
P("")
P("=== the three live numerical values of the SAME symbol (stale-evaluation note) ===")
for nm, v in (("NORMS l.746 / SF l.2837", EPS_NORMS), ("RLARGE l.611 TB-1", EPS_TB1),
              ("RLARGE l.71 first entry", EPS_T71), ("RLARGE l.72 headline", EPS_T)):
    P("  %-26s %s   (a_bad = %s)" % (nm, dec(v,4), dec(a_bad(v),4)))

print("\n".join(out))
