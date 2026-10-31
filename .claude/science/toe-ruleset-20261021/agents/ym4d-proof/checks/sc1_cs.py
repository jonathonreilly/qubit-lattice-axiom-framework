#!/usr/bin/env python3
# checks/sc1_cs.py  --  check sc1 for STAR_CONST.md (session 24, STAR-CONST worker).
#
# PRE-REGISTERED against checks/sc1_criteria.md, which was written before this file existed.
# Items SC1-1, SC1-2, SC1-3, SC1-5 have pre-registered PASS/FAIL verdicts there.
# Item SC1-4 is REPORTED ONLY (no pass value can be pre-registered: its inputs are this session's derivation).
# Blocks explicitly marked "POST-HOC" were added after reading an earlier output; they are labelled in the output.
#
# Plain python only: fractions + decimal. No numpy, no BLAS, single thread, no numeric lock.

from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext
import sys

PREC = int(sys.argv[1]) if len(sys.argv) > 1 else 40
getcontext().prec = PREC

out = []
def p(s=""):
    out.append(str(s))

# ---------------------------------------------------------------- helpers
def dln(x):
    return D(x).ln()

def Bm(m, imax=200):
    """B(m) = prod_{i>=0} (p_i-1)^{m/p_i}, p_i = 2^(i+1)."""
    s = D(0)
    for i in range(imax):
        pi = D(2) ** (i + 1)
        if pi - 1 == 0:
            continue
        s += (D(m) / pi) * (pi - 1).ln()
    return s.exp()

SQRT6 = D(6).sqrt()

def powD(base, expo):
    return (D(base).ln() * D(expo)).exp()

# ================================================================ SC1-1
p("=" * 78)
p("SC1-1  harness validation: the beta-telescope B(m)   [pre-registered]")
p("=" * 78)
targets = [(4, D("43.95")), (8, D("1931.5")), (D("4.17"), D("51.45"))]
ok1 = True
for m, tgt in targets:
    v = Bm(m)
    rel = abs(v - tgt) / tgt
    good = rel <= D("0.005")
    ok1 = ok1 and good
    p("  B(%-5s) = %-22s  CONST_T = %-8s  rel.dev = %.3e  %s"
      % (m, str(v)[:22], tgt, rel, "ok" if good else "OUT OF TOLERANCE"))
p("  SC1-1 VERDICT: %s" % ("PASS" if ok1 else "FAIL"))
p()

# ================================================================ SC1-2
p("=" * 78)
p("SC1-2  harness validation: reproduce CONST_T 6.3's q_min table   [pre-registered]")
p("=" * 78)
F_CT   = D("175.8")        # CONST_T 3.2, optimised schedule
MULT_CT = D(486)           # CONST_T 2.3
CEIL   = D("1e13")         # REVIEW_SQ_S4 S4-16
# CONST_T 4.2 reference point: A_c*gamma_c = 236.9*C_1 at (c_c, eps_*) = (50, 1e-4)
ACGC_PER_C1 = D("236.9")
# CONST_T 5.3 / 4.2: "288*C_1*Q ~ 6.5e6 at q = 100 with C_1 = 20"  =>  Q = 6.5e6/(288*20)
Q_CT = D("6.5e6") / (D(288) * D(20))

def C_T_constt(q, c1cv, c1_alone):
    a = D(q) / (D(q) - 4)
    base = D(36) * D(c1cv) * MULT_CT
    src = powD(base, a) / 2
    vc  = (ACGC_PER_C1 * D(c1_alone)) ** 2 / 2
    cut = D(288) * D(c1_alone) * Q_CT
    return SQRT6 * F_CT * Bm(4 * a) * (src + vc + cut)

def qmin_constt(c1cv, c1_rule, qhi=400):
    for q in range(5, qhi + 1):
        if C_T_constt(q, c1cv, c1_rule(c1cv)) <= CEIL:
            return q
    return None

# PRE-REGISTERED reading (sc1_criteria.md SC1-2): "CONST_T's reference point C_1 = 20 is used
# wherever C_1 appears alone."
rule_prereg = lambda c1cv: D(20)
table_ct = [(D(1), 9), (D(100), 16), (D(2000), 31), (D("1e4"), 132), (D("5e4"), None)]
ok2 = True
p("  pre-registered reading: C_1 = 20 wherever C_1 appears alone")
for c1cv, want in table_ct:
    got = qmin_constt(c1cv, rule_prereg)
    good = (got == want)
    ok2 = ok2 and good
    p("    C_1C_V = %-8s  q_min got = %-6s  CONST_T = %-6s  %s"
      % (c1cv, got, want, "ok" if good else "MISMATCH"))
p("  SC1-2 VERDICT: %s" % ("PASS" if ok2 else "FAIL"))
p()

# ---- POST-HOC (written after reading the pre-registered SC1-2 output) ----
p("  [POST-HOC, SC1-2b] same formula, C_1 = C_V = sqrt(C_1C_V):")
rule_sqrt = lambda c1cv: D(c1cv).sqrt()
ok2b = True
for c1cv, want in table_ct:
    got = qmin_constt(c1cv, rule_sqrt)
    good = (got == want)
    ok2b = ok2b and good
    ct = C_T_constt(got, c1cv, rule_sqrt(c1cv)) if got else None
    p("    C_1C_V = %-8s  q_min got = %-6s  CONST_T = %-6s  C_T at q_min = %-10s %s"
      % (c1cv, got, want, ("%.2e" % ct) if ct else "-", "ok" if good else "MISMATCH"))
p("  SC1-2b (post-hoc, NOT a pre-registered verdict): %s" % ("reproduces" if ok2b else "does not reproduce"))
p()

# ================================================================ SC1-3
p("=" * 78)
p("SC1-3  monotonicity   [pre-registered]")
p("=" * 78)
grid = [D(1), D(10), D(100), D(1000), D("1e4")]
qs = [qmin_constt(c, rule_sqrt) for c in grid]
mono_q = all((qs[i] is not None and qs[i + 1] is not None and qs[i] <= qs[i + 1])
             or qs[i + 1] is None for i in range(len(qs) - 1))
p("  q_min over C_1C_V grid %s : %s  -> non-decreasing: %s"
  % ([str(g) for g in grid], qs, mono_q))
mono_ct = True
for c in grid:
    prev = None
    for q in range(8, 401):
        v = C_T_constt(q, c, rule_sqrt(c))
        if prev is not None and v >= prev:
            mono_ct = False
            p("  C_T NOT decreasing at C_1C_V=%s, q=%d" % (c, q))
            break
        prev = v
p("  C_T(q) strictly decreasing on q in [8,400] for every grid point: %s" % mono_ct)
ok3 = mono_q and mono_ct
p("  SC1-3 VERDICT: %s" % ("PASS" if ok3 else "FAIL"))
p()

# ================================================================ SC1-4
p("=" * 78)
p("SC1-4  THE RESULT (reported; no pre-registered pass value)")
p("=" * 78)

# ---- the budget optimisation of STAR_CONST 6.2, in exact rationals where possible
def cs_of_T(T, d2, rho):
    # c_s(T) = 8*(9/T + 2)/(1 - d2 - rho - T)
    return D(8) * (D(9) / D(T) + 2) / (1 - D(d2) - D(rho) - D(T))

def opt_T(d2, rho):
    # minimise 8(9/T+2)/(K-T), K = 1-d2-rho  =>  2T^2 + 18T - 9K = 0
    K = D(1) - D(d2) - D(rho)
    T = (-D(18) + (D(324) + D(72) * K).sqrt()) / 4
    return T, cs_of_T(T, d2, rho)

p("  budget allocations (STAR_CONST 6.2):")
for (d2, rho, tag) in [(D(1) / 16, D(1) / 16, "chosen"),
                       (D(0), D(0), "unattainable floor"),
                       (D(1) / 8, D(1) / 4, "generous curvature")]:
    T, cs = opt_T(d2, rho)
    K = 1 - d2 - rho
    p("    d2=%-8s rho=%-8s T*=%-10s t=%-10s s0=%-10s kappa=%-10s c_s=%-10s  (%s)"
      % (d2, rho, str(T)[:9], str(T / 3)[:9], str(2 * T / 3)[:9], str(K - T)[:9], str(cs)[:9], tag))

D2, RHO = D(1) / 16, D(1) / 16
T_STAR, C_S = opt_T(D2, RHO)
KAPPA = 1 - D2 - RHO - T_STAR
# c_g = 8*C_B^tot/kappa + 272 ; C_B^tot = 8(2/d2+4) + 20 + 2
C_B_TOT = D(8) * (D(2) / D2 + 4) + 20 + 2
C_G = D(8) * C_B_TOT / KAPPA + 272
p("  => c_s = %s   (rounded up: %d)" % (str(C_S)[:10], int(C_S) + 1))
p("  => C_B^tot = %s, c_g = %s" % (C_B_TOT, str(C_G)[:10]))
p()

R0 = D(32)          # CONST_T 3.2, optimised schedule
def mu_lit(q):  return powD(14406, 1 - D(2) / D(q)) * powD(486, D(2) / D(q))
def mu_ct(q):   return D(486)
def mu_sharp(q):return powD(3, 1 - D(2) / D(q)) * powD(3, D(2) / D(q))
def Nplaq(tag): return {"M-lit": D(14406), "M-ct": D(486), "M-sharp": D(3)}[tag]

def C_T_star(q, mu, Nmult, acgc, bconv, cs=None, cg=None):
    cs = C_S if cs is None else cs
    cg = C_G if cg is None else cg
    a = D(q) / (D(q) - 4)
    src = powD(D(36) * cs * mu, a) / 2
    vc = D(acgc) ** 2 / 2
    Vinf = cs * powD(R0, -2 + D(8) / D(q))
    cut = D(288) * (cg + 18 * Vinf * Nmult)
    m = 4 * a if bconv == "P-ct" else 4 * max(a, D(2))
    return SQRT6 * F_CT * Bm(m) * (src + vc + cut), src, vc, cut, Vinf

def qmin_star(mufn, Nmult, acgc, bconv, qhi=400):
    for q in range(5, qhi + 1):
        v = C_T_star(q, mufn(q), Nmult, acgc, bconv)[0]
        if v <= CEIL:
            return q
    return None

p("  six combinations (multiplicity convention x beta-power convention), A_c*gamma_c = 1:")
p("  %-8s %-7s %-12s %-12s %-8s" % ("mult", "beta", "mu(q=8)", "C_T(q=8)", "q_min"))
res = {}
for mtag, mufn in [("M-lit", mu_lit), ("M-ct", mu_ct), ("M-sharp", mu_sharp)]:
    for bconv in ["P-ct", "P-max"]:
        N = Nplaq(mtag)
        qm = qmin_star(mufn, N, 1, bconv)
        ct8 = C_T_star(8, mufn(8), N, 1, bconv)[0]
        res[(mtag, bconv)] = (qm, ct8)
        p("  %-8s %-7s %-12s %-12s %-8s"
          % (mtag, bconv, "%.4g" % mufn(8), "%.3e" % ct8, qm))
p()

p("  detail, M-sharp (mu = 3 exactly, q-free):")
for bconv in ["P-ct", "P-max"]:
    p("    beta convention %s:" % bconv)
    for q in [8, 9, 10, 11, 12, 16, 20, 30, 50, 100]:
        tot, src, vc, cut, Vinf = C_T_star(q, mu_sharp(q), D(3), 1, bconv)
        p("      q=%-4d a=%-7s src=%-10s cut=%-10s ||V_s||inf=%-10s C_T=%-10s %s"
          % (q, str(D(q) / (D(q) - 4))[:6], "%.3e" % src, "%.3e" % cut,
             "%.3e" % Vinf, "%.3e" % tot, "UNDER" if tot <= CEIL else "over"))
p()

p("  sensitivity in A_c*gamma_c (the Stage-1 / eps_* input I do not own), M-sharp:")
for bconv in ["P-ct", "P-max"]:
    row = []
    for acgc in [1, 10, 100, 1000, 4738]:
        row.append("%s:%s" % (acgc, qmin_star(mu_sharp, D(3), acgc, bconv)))
    p("    %s   q_min at A_c*gamma_c = %s" % (bconv, ", ".join(row)))
# critical A_c*gamma_c at a few q (M-sharp)
p("  largest A_c*gamma_c still clearing 1e13 (M-sharp), by q:")
for bconv in ["P-ct", "P-max"]:
    row = []
    for q in [10, 12, 16, 30, 100]:
        tot, src, vc, cut, _ = C_T_star(q, mu_sharp(q), D(3), 0, bconv)
        a = D(q) / (D(q) - 4)
        m = 4 * a if bconv == "P-ct" else 4 * max(a, D(2))
        pref = SQRT6 * F_CT * Bm(m)
        slack = CEIL / pref - src - cut
        row.append("q=%d:%s" % (q, ("%.3g" % (2 * slack).sqrt()) if slack > 0 else "none"))
    p("    %s   %s" % (bconv, ", ".join(row)))
p()

p("  sensitivity in c_s (floor 319 / chosen 412 / generous 821), M-sharp, A_c*gamma_c = 1:")
for bconv in ["P-ct", "P-max"]:
    row = []
    for cs in [D(319), D(412), D(821)]:
        q = None
        for qq in range(5, 401):
            if C_T_star(qq, mu_sharp(qq), D(3), 1, bconv, cs=cs)[0] <= CEIL:
                q = qq
                break
        row.append("c_s=%s:q_min=%s" % (cs, q))
    p("    %s   %s" % (bconv, ", ".join(row)))
p()

# ================================================================ SC1-5
p("=" * 78)
p("SC1-5  precision control   [pre-registered; run this file at 40 and at 60 and diff]")
p("=" * 78)
p("  precision used in this run: %d significant digits" % PREC)
p("  key values for the diff:")
p("    B(4)=%s  B(8)=%s" % (str(Bm(4))[:20], str(Bm(8))[:20]))
p("    c_s=%s  c_g=%s  T*=%s" % (str(C_S)[:20], str(C_G)[:20], str(T_STAR)[:20]))
for mtag, mufn in [("M-lit", mu_lit), ("M-ct", mu_ct), ("M-sharp", mu_sharp)]:
    for bconv in ["P-ct", "P-max"]:
        qm, ct8 = res[(mtag, bconv)]
        p("    %-8s %-6s q_min=%-6s floor(log10 C_T(8))=%s"
          % (mtag, bconv, qm, int(ct8.log10())))
p()
p("=" * 78)
p("SUMMARY: SC1-1 %s | SC1-2 %s | SC1-3 %s | SC1-4 reported | SC1-5 by diff"
  % ("PASS" if ok1 else "FAIL", "PASS" if ok2 else "FAIL", "PASS" if ok3 else "FAIL"))
p("=" * 78)

print("\n".join(out))
