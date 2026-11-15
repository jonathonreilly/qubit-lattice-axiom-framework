#!/usr/bin/env python3
# ar1 — a_RS / eta_1 repair check.  Criteria: checks/ar1_criteria.md (written first, untouched).
# Exact fractions.Fraction throughout; decimal.Decimal for DISPLAY and for log10 only, at two precisions.
# Plain python3 -I, single thread, no numpy, no BLAS.  No numeric lock needed (exact rational arithmetic).
#
# Every constant below is TRANSCRIBED from an owning file with its citation.  A number reproduced here is
# NOT an endorsement of its source.  pi and e are truncated high-precision decimals (noted in the report);
# they enter only inequalities with >10 decades of slack, and the truncation direction is stated.

from fractions import Fraction as F
from decimal import Decimal, getcontext

# ---------------------------------------------------------------- transcribed constants
L   = 3                      # RLARGE l.37 (L >= 3 odd); l.1009 uses L = 3
d   = 4                      # RLARGE l.37
A_d = F((d - 1) * L * (L - 1), 2)          # RLARGE l.973: A_d(L) = (d-1)L(L-1)/2  -> 9
L2  = F(L * L)                             # 9
KAPPA = F(1)                               # RLARGE l.1248's c32 setting (kappa = 1)
c_RS  = F(5) ** 4                          # RLARGE l.1021: c_RS := 5^4
C10SQ = F(100)                             # RLARGE l.616-617: the 10^2 of "g^2 <~ a/10^2"
BETA_M = F(186, 1000)                      # RLARGE l.612: beta_- = beta_0'/2 ~ 0.186 at N = 2

# KN-step, EXISTENCE l.1774-1775
c_1    = F(1, 2) / (L2 + F(11, 2) * A_d)   # 1/(2(L^2 + 5.5 A_d))  -> 1/117
KN_106 = F(106)                            # EXISTENCE l.1775's coefficient in t <= 1/(106 sqrt(N) A_d^2 c_1^2)
KN_55  = F(11, 2)                           # EXISTENCE l.1771's 5.5 in c_1
KN_12  = F(12)                              # EXISTENCE l.1758: t >= 12 sqrt(N) delta^2
KN_DEN = F(8)                               # EXISTENCE l.1781: the kernel is applied at t/8

# DX' -- REVIEW_SF_S7 l.203, DX'-1 (iii): g_0^2 <~ 2.456e-152 / C_Omega.  C_Omega = 1 here (uncertified
# hand constant, REVIEW_SF_S7 l.225); the whole table is linear in C_Omega.
DXP = F(2456, 1000) * F(10) ** -152

# HW session 6, ring x82 (PLD session 7's settled CLOSED-column price) -- HW.md l.2007, l.2010
G2_CRC_82 = F(185835, 100000) * F(10) ** -96     # HW l.2007  (per c_+ = 82 already folded in, /c_+ = 1)
G2_RET    = F(367644, 100000) * F(10) ** -98     # HW l.2010

# live values of eps_1 (symbol 1 of EPS1_SWEEP sec.1 = RLARGE l.58's chi_Q cut), each from its owning file
EPS_LIVE = [
    ("1.27e-39  (SF.md l.2837; quoted NORMS l.746)", F(127, 100) * F(10) ** -39),
    ("9.52e-40  (RLARGE l.71, first entry of the min)", F(952, 100) * F(10) ** -40),
    ("8.95e-40  (RLARGE l.611 / REVIEW_SF_S7 l.200 TB-1)", F(895, 100) * F(10) ** -40),
    ("6.7e-40   (RLARGE l.72, the headline)", F(67, 10) * F(10) ** -40),
]
# the owner-gated PROPOSED value (TAUFLAT sec.4 option C, exact bound per EPS1_SWEEP sec.4.5).
# Transcribed only; this script does NOT assume the move happens.
EPS_PROP = ("9.38495112638e-45 (proposed; TAUFLAT sec.4 C / EPS1_SWEEP sec.4.5)",
            F(938495112638, 10 ** 12) * F(10) ** -44)

PI_50 = F(Decimal("3.1415926535897932384626433832795028841971693993751"))
E_50  = F(Decimal("2.7182818284590452353602874713526624977572470936999"))

# ---------------------------------------------------------------- display helpers (Decimal, 2 precisions)
def log10F(x, prec):
    getcontext().prec = prec
    return (Decimal(x.numerator) / Decimal(x.denominator)).log10()

def sci(x, prec=24, sig=6):
    getcontext().prec = prec
    return format(Decimal(x.numerator) / Decimal(x.denominator), ".%de" % (sig - 1))

def dec(x, prec=50, places=3):
    return format(log10F(x, prec), ".%df" % places)

# ---------------------------------------------------------------- the formulas, from owning files
def eta1_RS(eps, N):
    "RLARGE l.64 / l.976: eta_1 := min{eps/(2L^2), eps^2/(512 N A_d)}"
    return min(eps / (2 * L2), eps * eps / (512 * N * A_d))

def eta1_KN(eps, N):
    "EXISTENCE l.1771 / l.1774: eta_1 := c_1 eps, c_1 = 1/(2(L^2 + 5.5 A_d))"
    return c_1 * eps

def eta_q(eps, N):
    "RLARGE l.64: eta_q := min{eps/(2L^2), eps/(256 N A_d), delta_0/A_d}; delta_0 entry omitted (unevaluated)"
    return min(eps / (2 * L2), eps / (256 * N * A_d))

def a_eta_bare(eta, N):
    "RLARGE l.1026 / (R5) l.981: a_eta at its bare-level value eta_1^2/(2N)"
    return eta * eta / (2 * N)

def a_eta_PLD(eta, N):
    "PLD l.1044/l.1048: a(tau) = 49 tau^2/(256 sigma_*^2), Gaussian instance sigma_*^2 = N(1+18/kappa) (l.341)"
    sig2 = N * (1 + F(18) / KAPPA)
    return F(49) * eta * eta / (256 * sig2)

def a_RS(eps, N, form, aeta=a_eta_bare):
    "RLARGE l.1020: a_RS := min{a_eta, kappa eps^2/(256 N)}"
    eta = eta1_RS(eps, N) if form == "RS" else eta1_KN(eps, N)
    return min(aeta(eta, N), KAPPA * eps * eps / (256 * N)), aeta(eta, N), KAPPA * eps * eps / (256 * N)

def ceiling(eps, N, form, with_cRS, aeta=a_eta_bare):
    "RLARGE l.616-617's convention g^2 <~ a/10^2, applied to the RS exponent actually priced per cube"
    a, _, _ = a_RS(eps, N, form, aeta)
    return a / (c_RS * C10SQ) if with_cRS else a / C10SQ

out = []
def P(s=""):
    out.append(s)

P("=" * 100)
P("ar1 -- a_RS ceiling and KN-step's linear eta_1.  Criteria: checks/ar1_criteria.md (pre-registered).")
P("Exact Fraction arithmetic; Decimal for log10/display only, at 50 and 100 digits (ar1-6).")
P("C_Omega = 1 throughout (uncertified hand constant, REVIEW_SF_S7 l.225); every row is linear in it.")
P("=" * 100)
P()
P("Constants in force: L=%d d=%d A_d=%s L^2=%s kappa=%s c_RS=%s c_1=%s (=%s) beta_-=%s"
  % (L, d, A_d, L2, KAPPA, c_RS, c_1, sci(c_1), BETA_M))
P("DX' = %s   (REVIEW_SF_S7 l.203, DX'-1 (iii), at C_Omega = 1)" % sci(DXP))
P()

# ================================================================ ar1-1
P("#" * 100)
P("# ar1-1  branch identification and the eps_1-exponent of a_RS.   EXP-4 / EXP-2 / EXP-OTHER")
P("#" * 100)
verdicts_1 = []
for N in (2, 3):
    for lab, eps in EPS_LIVE + [EPS_PROP]:
        lin, quad = eps / (2 * L2), eps * eps / (512 * N * A_d)
        eta_branch = "LINEAR eps/(2L^2)" if lin < quad else "QUADRATIC eps^2/(512 N A_d)"
        a, ae, ak = a_RS(eps, N, "RS")
        rs_branch = "a_eta" if ae <= ak else "kernel"
        p = 4 if (quad <= lin and ae <= ak) else 2
        v = "EXP-4" if p == 4 else "EXP-2"
        verdicts_1.append(v)
        P("  N=%d eps=%-52s eta_1 branch=%-32s a_RS branch=%-7s -> %s"
          % (N, lab, eta_branch, rs_branch, v))
# the crossover and the pre-registered POWER counterfactual
for N in (2, 3):
    cross = F(512 * N * A_d, 1) / (2 * L2)          # eps where the two eta_1 entries cross
    cross_a = (512 * N * A_d) ** 2 * 2 * N / (256 * N) / 1   # eps^2 where a_eta = kernel entry
    P()
    P("  N=%d  eta_1 min crossover at eps_1 = %s (= 512 N A_d/(2L^2)); a_eta vs kernel crossover at eps_1 = %s"
      % (N, cross, sci(F(Decimal(str(float(cross_a)))) ** F(1, 2)) if False else "see below"))
    # exact: a_eta = eps^4/(2N(512 N A_d)^2) ; kernel = eps^2/(256 N) -> eps^2 = (512 N A_d)^2 *2N/(256N)
    eps2 = (512 * N * A_d) ** 2 * F(2 * N, 256 * N)
    P("        exact: a_eta = kernel at eps_1^2 = %s, i.e. eps_1 = %s" % (eps2, sci(F(Decimal(eps2.numerator).sqrt() if eps2.denominator == 1 else Decimal(1)))))
for N in (2, 3):
    for cf in (F(1000), F(100000)):
        a, ae, ak = a_RS(cf, N, "RS")
        lin, quad = cf / (2 * L2), cf * cf / (512 * N * A_d)
        v = "EXP-4" if (quad <= lin and ae <= ak) else "EXP-2"
        P("  POWER counterfactual: N=%d eps_1=%-8s -> %s   (eta_1 branch %s, a_RS branch %s)"
          % (N, cf, v, "quad" if quad <= lin else "LINEAR", "a_eta" if ae <= ak else "KERNEL"))
        verdicts_1.append(v)
P()
P("  ar1-1 VERDICT: %s   (power: both EXP-4 and EXP-2 returned => HAS-POWER)"
  % ("EXP-4 at every live and proposed eps_1" if all(v == "EXP-4" for v in verdicts_1[:10]) else "MIXED"))
P("  power check: EXP-2 returned at counterfactuals = %s" % ("YES" if "EXP-2" in verdicts_1 else "NO -> NO POWER"))
P()

# ================================================================ ar1-2
P("#" * 100)
P("# ar1-2  does the a_RS ceiling bind?   BINDS (margin<0) / NOT-BINDING (margin>0)")
P("#" * 100)
P("  margin = log10[ (a_RS/conv) / DX' ].  conv = 10^2 (EPS1_SWEEP's reading of RLARGE l.617)")
P("                                        or  c_RS*10^2 (the exponent actually priced per cube, l.1023-1024)")
P()
rows = []
for N in (2,):
    for lab, eps in EPS_LIVE + [EPS_PROP]:
        for form in ("RS", "KN"):
            for wc in (False, True):
                cg = ceiling(eps, N, form, wc)
                m = log10F(cg / DXP, 50)
                v = "BINDS" if m < 0 else "NOT-BINDING"
                rows.append((N, lab, form, wc, cg, m, v))
P("  %-52s %-4s %-10s %-14s %-9s %s" % ("eps_1", "form", "conv", "ceiling", "margin", "verdict"))
for (N, lab, form, wc, cg, m, v) in rows:
    P("  %-52s %-4s %-10s %-14s %+9.3f %s" % (lab, form, "c_RS*10^2" if wc else "10^2", sci(cg), m, v))
P()
rs_rows = [r for r in rows if r[2] == "RS"]
kn_rows = [r for r in rows if r[2] == "KN"]
v2 = ("CONFIRMED" if all(r[6] == "BINDS" for r in rs_rows)
      else "REFUTED" if all(r[6] == "NOT-BINDING" for r in rs_rows) else "SIGN-FRAGILE")
v3 = ("CONFIRMED" if all(r[6] == "NOT-BINDING" for r in kn_rows)
      else "REFUTED" if all(r[6] == "BINDS" for r in kn_rows) else "SIGN-FRAGILE")
P("  ar1-2 (V2) the quadratic (RLARGE) form, all live + proposed eps_1, both conventions : %s" % v2)
P("  ar1-2 (V3, arithmetic half) the linear (KN-step) form, same grid                    : %s" % v3)
P("  POWER: the two forms return OPPOSITE verdicts from the same constants -> %s"
  % ("HAS-POWER" if v2 != v3 else "NO POWER"))
P()
# interpolating exponent: eta_1^(s) = c_1^(1-s) * B^s * eps^(1+s), B = 1/(512 N A_d); p = 2+2s
P("  POWER, second leg: interpolate eta_1^(s) = c_1^(1-s) B^s eps^(1+s), B = 1/(512 N A_d);")
P("  then a_eta ~ eps^p with p = 2+2s (s=0 linear/KN, s=1 quadratic/RLARGE).  Zero-margin exponent p*:")
for lab, eps in [EPS_LIVE[3], EPS_PROP]:
    N = 2
    B = F(1, 512 * N * A_d)
    def margin_s(s_num, s_den, wc=False):
        s = F(s_num, s_den)
        # exact rational power only for rational s with small denominator -> use Decimal logs instead
        getcontext().prec = 60
        lc1 = log10F(c_1, 60); lB = log10F(B, 60); le = log10F(eps, 60)
        leta = (1 - Decimal(s.numerator) / Decimal(s.denominator)) * lc1 \
               + (Decimal(s.numerator) / Decimal(s.denominator)) * lB \
               + (1 + Decimal(s.numerator) / Decimal(s.denominator)) * le
        la = 2 * leta - log10F(F(2 * N), 60)
        conv = log10F(c_RS * C10SQ if wc else C10SQ, 60)
        return la - conv - log10F(DXP, 60)
    lo, hi = 0, 1
    for _ in range(60):
        mid = F(lo + hi, 2)
        if margin_s(mid.numerator, mid.denominator) > 0:
            lo = mid
        else:
            hi = mid
    sstar = F(lo + hi, 2)
    pstar = 2 + 2 * sstar
    P("    eps_1 = %-52s p* = %s = %s   margin(p*-0.01)=%+.3f  margin(p*+0.01)=%+.3f"
      % (lab, pstar, format(Decimal(pstar.numerator) / Decimal(pstar.denominator), ".5f"),
         margin_s((pstar - F(1, 100) - 2).numerator * 1, (pstar - F(1, 100) - 2).denominator * 2)
         if False else margin_s((sstar - F(1, 200)).numerator, (sstar - F(1, 200)).denominator),
         margin_s((sstar + F(1, 200)).numerator, (sstar + F(1, 200)).denominator)))
P("    -> the verdict is a function of the exponent and changes sign across p*, as pre-registered.")
P()

# ================================================================ ar1-3
P("#" * 100)
P("# ar1-3  are KN-step's arithmetic hypotheses available at t = eps_1?   HYP-AVAILABLE / HYP-FAILS")
P("#" * 100)
ok3 = True
for N in (2, 3):
    bnd_a = F(1) / (KN_106 * F(Decimal(N).sqrt() if False else Decimal(str(N))) ** F(1, 2) * A_d ** 2 * c_1 ** 2) \
        if False else None
    # sqrt(N) exactly is irrational; use a RATIONAL LOWER bound on 1/sqrt(N) -> conservative (smaller bound)
    getcontext().prec = 60
    sqrtN = F(Decimal(N).sqrt())            # 60-digit truncation; direction noted in the report
    bnd_a = F(1) / (KN_106 * sqrtN * A_d ** 2 * c_1 ** 2)
    P("  N=%d  (a) KN-step l.1775: t <= 1/(106 sqrt(N) A_d^2 c_1^2) = %s" % (N, sci(bnd_a)))
    for lab, eps in EPS_LIVE + [EPS_PROP]:
        hold = eps <= bnd_a
        ok3 &= hold
        P("        t=eps_1=%-52s %s" % (lab, "HOLDS" if hold else "FAILS"))
    for cf in (F(2), F(10), F(1000)):
        P("        POWER counterfactual t=%-6s %s" % (cf, "HOLDS" if cf <= bnd_a else "FAILS"))
    bnd_b = F(1, 4) / (PI_50 / 3 * A_d * c_1)
    P("  N=%d  (b) KN-step l.1775: (pi/3) A_d c_1 t <= 1/4  <=>  t <= %s" % (N, sci(bnd_b)))
    for lab, eps in [EPS_LIVE[0], EPS_PROP]:
        P("        t=eps_1=%-52s %s" % (lab, "HOLDS" if eps <= bnd_b else "FAILS"))
    for cf in (F(2), F(10)):
        P("        POWER counterfactual t=%-6s %s" % (cf, "HOLDS" if cf <= bnd_b else "FAILS"))
P()
P("  (c) reconstruction identity: (L^2 + 5.5 A_d) * c_1 must equal exactly 1/2")
lhs_c = (L2 + KN_55 * A_d) * c_1
P("      (L^2 + 5.5A_d)*c_1 = %s  -> %s" % (lhs_c, "IDENTITY-HOLDS" if lhs_c == F(1, 2) else "IDENTITY-FAILS"))
P()
P("  (d) reconstruction of KN-step's coefficient 106 from Lemma KN's 12, independently:")
P("      KN needs t/8 >= 12 sqrt(N) delta^2 with delta <= (pi/3) A_d eta and eta < c_1 t, so")
P("      t <= 1/( 8*12*(pi/3)^2 sqrt(N) A_d^2 c_1^2 ) = 1/( %s sqrt(N) A_d^2 c_1^2 )")
coef_d = KN_DEN * KN_12 * (PI_50 / 3) ** 2
P("      my coefficient  = %s" % sci(coef_d))
P("      EXISTENCE l.1775 = %s" % sci(KN_106))
ratio_d = KN_106 / coef_d
P("      ratio (theirs/mine) = %s  -> %s (tolerance 1.2)"
  % (sci(ratio_d), "REPRODUCES" if F(1, 1) / F(12, 10) <= ratio_d <= F(12, 10) else "SOURCE-DISAGREES"))
ok3 &= (F(1, 1) / F(12, 10) <= ratio_d <= F(12, 10))
P()
P("  (e) reconstruction of the 5.5 in c_1: need 4(e^delta - 1) <= 5.5 A_d eta given delta <= (pi/3)A_d eta,")
P("      delta <= 1/4.  Worst case 4*(e^{1/4}-1)/(1/4)*(pi/3) must be <= 5.5:")
# (e^{1/4}-1)/(1/4), with e^{1/4} from the 50-digit e
getcontext().prec = 60
e14 = Decimal(E_50.numerator) / Decimal(E_50.denominator)
e14 = e14 ** (Decimal(1) / Decimal(4))
coef_e = 4 * (F(e14) - 1) / F(1, 4) * (PI_50 / 3)
P("      my coefficient = %s   vs EXISTENCE's 5.5  -> %s"
  % (sci(coef_e), "RECONSTRUCTS (<= 5.5)" if coef_e <= KN_55 else "SOURCE-DISAGREES (> 5.5)"))
ok3 &= (coef_e <= KN_55)
P()
P("  (f) the kernel branch is UNCHANGED by the adoption: RLARGE (R4) l.979 gives kappa eps^2/(256 N g^2);")
P("      KN-step l.1776 gives kappa t^2/(256 N g^2) at t = eps_1.  Identical -> %s"
  % "SAME-CONSTANT")
P()
P("  ar1-3 VERDICT: %s" % ("HYP-AVAILABLE (arithmetic clauses)" if ok3 else "HYP-FAILS"))
P()

# ================================================================ ar1-4
P("#" * 100)
P("# ar1-4  consumer sweep")
P("#" * 100)
P("  (a) RLARGE l.65 records eta_1 <= eta_q on the admissible range.  Under each form:")
for N in (2, 3):
    for lab, eps in [EPS_LIVE[3], EPS_PROP]:
        for form, f in (("RS", eta1_RS), ("KN", eta1_KN)):
            e1, eq = f(eps, N), eta_q(eps, N)
            v = "ORDER-PRESERVED (eta_1<=eta_q)" if e1 <= eq else "ORDER-REVERSED (eta_1>eta_q)"
            P("      N=%d form=%-3s eps=%-52s eta_1/eta_q = %-12s %s"
              % (N, form, lab, sci(e1 / eq), v))
P()
P("  (b) REVIEW_PLD_S3 l.302/l.305: any RS-compatible threshold obeys eta <= eps_1/(1.001 L^2).")
for N in (2,):
    for form, f in (("RS", eta1_RS), ("KN", eta1_KN)):
        eps = EPS_LIVE[3][1]
        bnd = eps / (F(1001, 1000) * L2)
        P("      form=%-3s eta_1 = %-14s bound = %-14s -> %s"
          % (form, sci(f(eps, N)), sci(bnd), "RS-COMPATIBLE" if f(eps, N) <= bnd else "RS-INCOMPATIBLE"))
    for cf_c1 in (F(1, 2) / L2, F(3, 2) / L2):
        eps = EPS_LIVE[3][1]
        bnd = eps / (F(1001, 1000) * L2)
        P("      POWER counterfactual c_1=%-10s eta_1 = %-14s -> %s"
          % (cf_c1, sci(cf_c1 * eps), "RS-COMPATIBLE" if cf_c1 * eps <= bnd else "RS-INCOMPATIBLE"))
P()
P("  (c) PLD l.765-776 LD-arith: summability needs alpha t^2 beta_1 > log(n_U)/log(L), n_U = 24 L^4,")
P("      alpha = 1/(2(N-1)) (PLD l.770), beta_1 = 11 N^2/(12 pi^2) (RLARGE l.42).  Least N:")
getcontext().prec = 60
lnU = (Decimal(24 * L ** 4)).ln() / Decimal(L).ln()
P("      log(n_U)/log(L) = %s   (PLD l.766 states 6.893)" % format(lnU, ".5f"))
for tlab, t in (("t = 2 (PLD l.771)", F(2)), ("t = 1/2 (PLD l.772)", F(1, 2)),
                ("t = 2/117 = c_1*2 (PLD l.772)", c_1 * 2)):
    least = None
    for N in range(2, 1200000):
        alpha = F(1, 2 * (N - 1))
        beta1 = F(11 * N * N, 12) / (PI_50 ** 2)
        if alpha * t * t * beta1 > F(lnU):
            least = N
            break
    P("      %-32s least N = %s" % (tlab, least))
for N in (2, 3):
    for lab, eps in [EPS_LIVE[3]]:
        for form, f in (("RS", eta1_RS), ("KN", eta1_KN)):
            t = f(eps, N)
            alpha = F(1, 2 * (N - 1))
            beta1 = F(11 * N * N, 12) / (PI_50 ** 2)
            holds = alpha * t * t * beta1 > F(lnU)
            P("      at t = eta_1 (form %-3s), N=%d, eps_1=6.7e-40 : summable? %s"
              % (form, N, "YES" if holds else "NO"))
P("      -> PLD's conclusion 'route (a) is no for SU(2), SU(3)' : %s" % "SU23-STANDS (NO at N=2,3 under both forms)")
P()
P("  (d) REVIEW_PLD_S3 (Arch-3) m_tau: least m with (L^2/(2C_I))^m eta_1 >= 2 C_I eps_1/L^2.")
for C_I in (F(1), F(3, 2), F(2)):
    line = "      C_I=%-4s" % C_I
    for N, eps, tag in ((2, F(2), "eps=2,N=2"), (2, F(517, 1000), "eps=0.517"),
                        (2, F(10) ** -3, "eps=1e-3"), (2, F(2) * F(10) ** -32, "eps=2e-32"),
                        (2, EPS_LIVE[3][1], "eps=6.7e-40"), (2, EPS_PROP[1], "eps=prop")):
        res = []
        for form, f in (("RS", eta1_RS), ("KN", eta1_KN)):
            e1 = f(eps, N)
            m, cur = 0, e1
            tgt = 2 * C_I * eps / L2
            while cur < tgt and m < 5000:
                cur *= (L2 / (2 * C_I)); m += 1
            res.append(m)
        line += "  %s: RS=%-4d KN=%-2d" % (tag, res[0], res[1])
    P(line)
P("      REVIEW_PLD_S3 l.347 states 5/7/10 at eps=2 N=2 and 6/8/12 at 0.517, 10/14/19 at 1e-3,")
P("      54/74/101 at 2e-32 (RLARGE's eta_1); l.349 states 3/4/5 with c_1 eps_1.  Compare the columns.")
P()

# ================================================================ ar1-5
P("#" * 100)
P("# ar1-5  does the claimed gain reproduce?   GAIN-REPRODUCES / SOURCE-DISAGREES")
P("#" * 100)
for lab, eps in [EPS_LIVE[3], EPS_PROP]:
    N = 2
    for wc in (False, True):
        mRS = log10F(ceiling(eps, N, "RS", wc) / DXP, 50)
        mKN = log10F(ceiling(eps, N, "KN", wc) / DXP, 50)
        P("  eps_1=%-52s conv=%-10s margin RS=%+9.3f  KN=%+9.3f  GAIN=%+9.3f"
          % (lab, "c_RS*10^2" if wc else "10^2", mRS, mKN, mKN - mRS))
P()
P("  EPS1_SWEEP sec.4.3 / sec.7.1 item 2 quote: 'from -15.62 to +66.52 decades ... a gain of 92 decades")
P("  at today's eps_1'.  The gain is a difference of an eps^4 and an eps^2 margin, so it is itself")
P("  eps_1-dependent.  Compare the two GAIN rows above against the quoted 92.")
P()

# ================================================================ extra: the other eta_1-touched rows
P("#" * 100)
P("# ar1-5b  the other entries of RLARGE's ceiling/induction table that eta_1 touches  [POST-HOC: not a")
P("#         pre-registered verdict; reported for completeness]")
P("#" * 100)
P("  a'' = 0.9 eps^2/(4N) (RLARGE l.1245);  a_# = min{a'', a_flat, a_RS/c_RS} (l.1024);  n_# = 4/(a_# beta_-)")
for lab, eps in [EPS_LIVE[3], EPS_PROP]:
    N = 2
    app = F(9, 10) * eps * eps / (4 * N)
    for form in ("RS", "KN"):
        a, _, _ = a_RS(eps, N, form)
        a_sharp = min(app, a / c_RS)
        n_sharp = 4 / (a_sharp * BETA_M)
        which = "a''" if app <= a / c_RS else "a_RS/c_RS"
        P("    eps=%-52s form=%-3s a''=%-12s a_RS/c_RS=%-12s a_#=%-12s (%s) n_#=%-12s log_L(2n_#)=%s"
          % (lab, form, sci(app), sci(a / c_RS), sci(a_sharp), which, sci(n_sharp),
             format(log10F(2 * n_sharp, 50) / Decimal(L).log10(), ".1f")))
P()
P("  HIST l.1377-1379's chain-energy floor E_C(p) >= eta_1^2/(2 N C_cone) scales as eta_1^2, so it")
P("  improves by the same factor as a_eta:")
for lab, eps in [EPS_LIVE[3]]:
    N = 2
    r = (eta1_KN(eps, N) / eta1_RS(eps, N)) ** 2
    P("    eps=%-52s (eta_KN/eta_RS)^2 = %s = %s decades" % (lab, sci(r), dec(r)))
P()
P("  sensitivity: with PLD l.1048's effective-level a_eta = 49 eta^2/(256 sigma_*^2), sigma_*^2 = N(1+18/kappa):")
for lab, eps in [EPS_LIVE[3], EPS_PROP]:
    N = 2
    for form in ("RS", "KN"):
        cg = ceiling(eps, N, form, False, a_eta_PLD)
        P("    eps=%-52s form=%-3s margin = %+9.3f (vs bare-level a_eta above)"
          % (lab, form, log10F(cg / DXP, 50)))
P()
P("  cross-reference (NOT re-derived here, transcribed): HW l.2007 g^2_CRC(x82)=%s -> margin %+.3f;"
  % (sci(G2_CRC_82), log10F(G2_CRC_82 / DXP, 50)))
P("                                                      HW l.2010 g^2_ret      =%s -> margin %+.3f"
  % (sci(G2_RET), log10F(G2_RET / DXP, 50)))
P()

# ================================================================ ar1-6
P("#" * 100)
P("# ar1-6  precision.   PASS / FAIL")
P("#" * 100)
worst = Decimal(0)
for lab, eps in EPS_LIVE + [EPS_PROP]:
    for form in ("RS", "KN"):
        for wc in (False, True):
            cg = ceiling(eps, 2, form, wc)
            a = log10F(cg / DXP, 50)
            b = log10F(cg / DXP, 100)
            getcontext().prec = 110
            dd = abs(a - b)
            worst = max(worst, dd)
P("  worst |log10 at 50 digits - log10 at 100 digits| over all 20 margin rows = %s" % format(worst, ".3e"))
P("  ar1-6 VERDICT: %s (tolerance 0.1 decade)" % ("PASS" if worst < Decimal("0.1") else "FAIL"))
P()
P("=" * 100)
P("Truncation disclosure: pi and e are 50-digit truncations; sqrt(N) a 60-digit truncation. They enter")
P("only ar1-3 (c)-(e) and ar1-4 (c), where the slack is many orders of magnitude or the comparison is")
P("against an integer, so no verdict can turn on the truncation.")
P("=" * 100)

print("\n".join(out))
