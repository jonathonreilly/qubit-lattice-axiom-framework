#!/usr/bin/env python3
# tf1_tau.py -- the tau_flat binding-entry adjudication, exact arithmetic.
# Criteria: checks/tf1_criteria.md, written BEFORE this file. Verdicts TF1-A..TF1-H are fixed there.
# Plain python3 -I, single thread, fractions only. No numpy, no BLAS, no numeric lock.
#
# NOTHING here is re-derived. Every constant is TRANSCRIBED from an owning file with a line citation.
# This script's only job is arithmetic consistency between two transcriptions (tf1_criteria.md Sec. 0).

from fractions import Fraction as F
from decimal import Decimal, getcontext
import sys

def E(mant, exp):
    """Exact decimal literal mant * 10**exp as a Fraction."""
    return F(mant) * F(10) ** exp

def d10(x, prec=40):
    """log10 of a positive Fraction, to `prec` digits, by exact integer scaling."""
    getcontext().prec = prec + 15
    return Decimal(x.numerator).log10() - Decimal(x.denominator).log10()

def sci(x, prec=6):
    getcontext().prec = prec
    return str(+Decimal(x.numerator) / Decimal(x.denominator))

out = []
def p(s=""):
    out.append(s)
    print(s)

p("=" * 100)
p("tf1 -- tau_flat binding-entry adjudication.  Exact Fraction arithmetic.")
p("Criteria: checks/tf1_criteria.md (written before this script).  Verdicts are those of its Sec. 2-3.")
p("=" * 100)

# ---------------------------------------------------------------------------
# BLOCK T.  TRANSCRIPTION TABLE.  Every value below is read off an owning file.
# ---------------------------------------------------------------------------
p("")
p("BLOCK T -- TRANSCRIPTION (no value below is computed here)")
p("-" * 100)

# C' := L^2 + 4A_d + 8 = 53 at L = 3.  SQ.md Lemma FORCE (l.~213-215).
Cp = F(53)
p("  C'            = 53                      [SQ.md, Lemma FORCE: C' := L^2 + 4A_d + 8, = 53 at L = 3]")

# c_b := min{1/(4C_1), 1/(2N), kappa_-/(4N)} = 1/640 at N = 2.  SQ.md Lemma DESC (a) (l.~294-296).
cb = F(1, 640)
p("  c_flat        = 1/640                   [SQ.md, Lemma DESC (a): c_b := min{1/(4C_1),1/(2N),k_-/(4N)}]")

# tau_R <= 2.75e-15.  REVIEW_SQ_S4 S4-14 (l.309).
tauR = E(275, -17)
p("  tau_R         = 2.75e-15                [REVIEW_SQ_S4 S4-14 l.309]")

# C_err = 1.655e7 * C_D^2  ;  theta_0^SUP = 1/(2 C_err) = 1/(3.31e7 C_D^2).
# REVIEW_SQ_S4 S4-16 (l.363-367); the 1/(2 C_err) form is SQ.md Theorem SUP-price (l.~188).
C_err_coeff = E(1655, 4)          # 1.655e7
th0sup_coeff = 2 * C_err_coeff    # 3.31e7, so theta_0^SUP = 1/(th0sup_coeff * C_D^2)
p("  C_err         = 1.655e7 * C_D^2         [REVIEW_SQ_S4 S4-16 l.364]")
p("  theta_0^SUP   = 1/(2 C_err)             [SQ.md Thm SUP-price l.188; = 1/(3.31e7 C_D^2), S4-16 l.364]")

# C_D ~ (0.5-0.9)e3 * C_T.  REVIEW_SQ_S4 S4-16 (l.374).  Worst (largest C_D) end = 0.9e3.
CD_lo_coeff, CD_hi_coeff = E(5, 2), E(9, 2)
p("  C_D           = (0.5-0.9)e3 * C_T       [REVIEW_SQ_S4 S4-16 l.374]")

# C_T = 5.288e12 at q = 12.  EPSSTAR.md Sec. 7.1 (l.549, 555).
C_T = E(5288, 9)
p("  C_T           = 5.288e12  (q = 12)      [EPSSTAR.md Sec.7.1 l.549/555; CONDITIONAL on its (H2)]")

# eps_1 <~ 6.7e-40, RLARGE.md Sec.0 l.71-72 ("current eps_1 ceiling", TB-1).
eps1 = E(67, -41)
p("  eps_1         = 6.7e-40                 [RLARGE.md Sec.0 l.71-72, current ceiling, TB-1]")

# eta_AE = 1.776e-15 at C_S <= 1e2 (and 8.9e-16 at C_S = 1e4).  REVIEW_HIST_S4 l.368-370.
eta_AE = E(1776, -18)
eta_AE_CS4 = E(89, -17)
p("  eta_AE        = 1.776e-15 (C_S<=1e2)    [REVIEW_HIST_S4 l.368]; 8.9e-16 at C_S=1e4 [l.370]")

# C_3: HIST Theorem A5's energy coefficient, an UNKNOWN.  Reference value 1 only (criteria Sec.1).
C_3 = F(1)
p("  C_3           = 1  (REFERENCE ONLY)     [HIST.md Thm A5 l.1684; C_3 is not pinned anywhere]")

# EPSSTAR Sec.6.6's own three repair figures, transcribed for TF1-E.
eps_t_pr_req = E(301, -37)      # 3.01e-35 * sqrt(C_3)         EPSSTAR l.525
eps_CD_ceil  = E(317, 11)       # 3.17e13 / C_3^{1/4}          EPSSTAR l.525
eps_CT_ceil  = E(35, 9)         # 3.5e10  (worst end)          EPSSTAR l.525-526, l.781
p("  [EPSSTAR Sec.6.6 l.525-526, transcribed for comparison in TF1-E:")
p("     t_pr required >= 3.01e-35*sqrt(C_3);  C_D <= 3.17e13/C_3^(1/4);  C_T <~ 3.5e10 - 6.3e10]")

# The route's own floor on C_T, EPSSTAR Sec.7.4 l.608 (c_s >= 319.2 => C_T >= 4.4e12 at q = 12).
C_T_floor = E(44, 11)
p("  C_T floor     = 4.4e12                  [EPSSTAR Sec.7.4 l.608; c_s >= 319.2 forces it]")

# ---------------------------------------------------------------------------
# Definitions from SQ.md Corollary DESC-eps (l.317-319), used as definitions, not re-derived:
#   tau_flat := min{tau_F, tau_R, theta_0^SUP/C', eps_M/(C_D C'), theta_sharp/C', 1/(73.6 N c'^2 A'^2)}
#   eta_flat := c_flat * tau_flat^2 / C'^2
#   t_pr     := C' * tau_flat                  (REVIEW_SQ_S4 S4-15 l.337)
# ---------------------------------------------------------------------------
def theta0sup(CD):
    return 1 / (th0sup_coeff * CD * CD)

def eta_flat_from_tau(tau):
    return cb * tau * tau / (Cp * Cp)

def t_pr_from_tau(tau):
    return Cp * tau

CD_worst = CD_hi_coeff * C_T          # largest C_D, i.e. smallest theta_0^SUP
CD_best  = CD_lo_coeff * C_T

# ---------------------------------------------------------------------------
# TF1-A is a READING verdict and is recorded in TAUFLAT.md, not here.  The script only
# records that it treats the two theta_0 as DISTINCT symbols, both inside tau_flat's min.
# ---------------------------------------------------------------------------
p("")
p("TF1-A (reading verdict, recorded in TAUFLAT.md Sec.1): the script assumes DISTINCT-AND-BOTH-BIND,")
p("  i.e. tau_R (which itself contains theta_0^{SQ4}/C') and theta_0^SUP/C' are SEPARATE entries of")
p("  tau_flat's min (SQ.md l.317-319 vs l.1633; REVIEW_SQ_S4 S4-14 item 4 confirms both constraints apply).")

# ---------------------------------------------------------------------------
# TF1-B: the conflict
# ---------------------------------------------------------------------------
def run_block(label, CD, verdict_prefix):
    res = {}
    p("")
    p("=" * 100)
    p(label)
    p("=" * 100)
    th = theta0sup(CD)
    tau_from_th = th / Cp
    p("  C_D                       = %s" % sci(CD))
    p("  theta_0^SUP = 1/(3.31e7 C_D^2) = %s" % sci(th))
    p("  theta_0^SUP / C'          = %s   <- candidate entry B" % sci(tau_from_th))
    p("  tau_R                     = %s   <- candidate entry A" % sci(tauR))
    binding = "tau_R (A)" if tauR <= tau_from_th else "theta_0^SUP/C' (B)"
    p("  => the min is attained at   %s" % binding)

    eta_A = eta_flat_from_tau(tauR)
    eta_B = eta_flat_from_tau(tau_from_th)
    p("")
    p("  eta_flat at entry A (tau_flat = tau_R)            = %s" % sci(eta_A))
    p("  eta_flat at entry B (tau_flat = theta_0^SUP/C')   = %s" % sci(eta_B))
    ratio = eta_A / eta_B
    dec = d10(ratio)
    p("  exact ratio A/B = %d / %d" % (ratio.numerator, ratio.denominator))
    p("  log10(ratio)    = %s decades" % str(+dec.quantize(Decimal('0.001'))))
    vB = "CONFLICT-REAL" if abs(dec) >= 10 else "CONFLICT-ABSENT"
    p("  [%s-B] %s   (threshold: >= 10 decades)" % (verdict_prefix, vB))
    res['B'] = vB
    res['dec'] = dec

    # TF1-D: the DESC-eps clause at the binding entry
    tau_bind = min(tauR, tau_from_th)
    eta_bind = eta_flat_from_tau(tau_bind)
    t_pr = t_pr_from_tau(tau_bind)
    need = 4 * C_3 * eps1 * eps1
    p("")
    p("  DESC-eps (iii) hypothesis: E < eta_flat, with consumers supplying E <= 4 C_3 eps_1^2")
    p("    t_pr      = C' tau_flat          = %s" % sci(t_pr))
    p("    eta_flat  (at binding entry)     = %s" % sci(eta_bind))
    p("    4 C_3 eps_1^2                    = %s" % sci(need))
    holds = eta_bind >= need
    vD = "CLAUSE-HOLDS" if holds else "CLAUSE-FAILS"
    short = need / eta_bind
    sdec = d10(short)
    p("    [%s-D] %s" % (verdict_prefix, vD))
    if not holds:
        p("       shortfall = %s decades of ENERGY, %s decades of eps_1"
          % (str(+sdec.quantize(Decimal('0.001'))),
             str(+(sdec / 2).quantize(Decimal('0.001')))))
    else:
        mdec = d10(eta_bind / need)
        p("       margin    = %s decades of ENERGY, %s decades of eps_1"
          % (str(+mdec.quantize(Decimal('0.001'))),
             str(+(mdec / 2).quantize(Decimal('0.001')))))
    res['D'] = vD
    res['t_pr'] = t_pr
    res['eta'] = eta_bind
    return res

# ---------------------------------------------------------------------------
# TF1-C: the consistency window.  tau_R <= theta_0^SUP/C'  <=>  C_D <= CD_star
# ---------------------------------------------------------------------------
p("")
p("=" * 100)
p("TF1-C -- the window in which S4-14 item 2 and S4-16 are JOINTLY CONSISTENT")
p("=" * 100)
CD_star_sq = 1 / (th0sup_coeff * Cp * tauR)
p("  condition: tau_R <= theta_0^SUP/C'  <=>  C_D^2 <= 1/(3.31e7 * C' * tau_R)")
p("  C_D^2 <= %d / %d = %s" % (CD_star_sq.numerator, CD_star_sq.denominator, sci(CD_star_sq)))
# exact integer sqrt bracket
n, d = CD_star_sq.numerator, CD_star_sq.denominator
import math
isq = math.isqrt(n * 10**40 // d)
CD_star = F(isq, 10**20)
p("  C_D <= %s   (exact to 20 digits)" % sci(CD_star, 10))
p("  chain's current C_D (worst end) = %s" % sci(CD_worst))
inside = CD_worst <= CD_star
p("  [TF1-C] current C_D is %s the window" % ("INSIDE" if inside else "OUTSIDE"))
p("  window exceeded by a factor %s" % sci(CD_worst / CD_star))

# ---------------------------------------------------------------------------
# MAIN RUN (the chain's current C_D) and the two ends of the C_D band
# ---------------------------------------------------------------------------
main = run_block("MAIN RUN -- chain's current C_D = 0.9e3 * C_T (worst/largest end)",
                 CD_worst, "TF1")
alt  = run_block("BAND CHECK -- other end of S4-16's band, C_D = 0.5e3 * C_T",
                 CD_best, "TF1(band)")

# ---------------------------------------------------------------------------
# TF1-G: the designed counterfactual.  One input changed: C_D := CD_star/2.
# ---------------------------------------------------------------------------
cf = run_block("TF1-G COUNTERFACTUAL -- C_D := (TF1-C window boundary)/2, nothing else changed",
               CD_star / 2, "TF1(cf)")
p("")
p("=" * 100)
p("TF1-G -- POWER CHECK")
p("=" * 100)
p("  main run:        B = %-16s D = %s" % (main['B'], main['D']))
p("  counterfactual:  B = %-16s D = %s" % (cf['B'], cf['D']))
powered = (cf['B'] != main['B']) and (cf['D'] != main['D'])
p("  [TF1-G] %s" % ("PASS -- the check can return BOTH verdicts; it has the power to fail"
                    if powered else
                    "NO POWER -- the check returned the same verdicts under the counterfactual."
                    " Per tf1_criteria.md Sec.3 this is reported as NO POWER, not as a PASS."))

# ---------------------------------------------------------------------------
# TF1-E: the repair bar, and EPSSTAR's own three figures
# ---------------------------------------------------------------------------
p("")
p("=" * 100)
p("TF1-E -- the repair bar, and a check on EPSSTAR Sec.6.6's own arithmetic")
p("=" * 100)
# eta_flat = c_b (t_pr/C')^2 / C'^2 = t_pr^2 * c_b / C'^4 ; need eta_flat >= 4 C_3 eps_1^2
k = cb / Cp**4                    # eta_flat = k * t_pr^2
p("  eta_flat = c_b t_pr^2 / C'^4, with 1/k = %s   (EPSSTAR writes t_pr^2/5.05e9)"
  % sci(1 / k))
# t_pr^2 >= 4 C_3 eps_1^2 / k
t_pr_req_sq = 4 * C_3 * eps1 * eps1 / k
isq2 = math.isqrt(t_pr_req_sq.numerator * 10**80 // t_pr_req_sq.denominator)
t_pr_req = F(isq2, 10**40)
p("  (a) t_pr required  = %s * sqrt(C_3)" % sci(t_pr_req))
p("      EPSSTAR states = %s * sqrt(C_3)" % sci(eps_t_pr_req))
r_a = t_pr_req / eps_t_pr_req
p("      ratio mine/EPSSTAR = %s" % sci(r_a))
# C_D ceiling: t_pr = theta_0^SUP = 1/(3.31e7 C_D^2) >= t_pr_req
CD_ceil_sq = 1 / (th0sup_coeff * t_pr_req)
isq3 = math.isqrt(CD_ceil_sq.numerator * 10**40 // CD_ceil_sq.denominator)
CD_ceil = F(isq3, 10**20)
p("  (b) C_D ceiling    = %s / C_3^(1/4)" % sci(CD_ceil))
p("      EPSSTAR states = %s / C_3^(1/4)" % sci(eps_CD_ceil))
r_b = CD_ceil / eps_CD_ceil
p("      ratio mine/EPSSTAR = %s" % sci(r_b))
CT_ceil_worst = CD_ceil / CD_hi_coeff
CT_ceil_best = CD_ceil / CD_lo_coeff
p("  (c) C_T ceiling    = %s (at C_D=0.9e3 C_T) to %s (at 0.5e3 C_T)"
  % (sci(CT_ceil_worst), sci(CT_ceil_best)))
p("      EPSSTAR states = 3.5e10 to 6.3e10")
r_c = CT_ceil_worst / eps_CT_ceil
p("      ratio mine/EPSSTAR (worst end) = %s" % sci(r_c))
tol = F(12, 10)
agree = all(max(r, 1 / r) <= tol for r in (r_a, r_b, r_c))
vE = "SOURCE-REPRODUCED" if agree else "SOURCE-DISAGREES"
p("  [TF1-E] %s   (tolerance: factor 1.2)" % vE)
if not agree:
    p("     direction: my required t_pr is LARGER and my C_T ceiling LOWER than EPSSTAR's,")
    p("     i.e. the correction makes the reported failure WORSE, not better.")
p("  route floor C_T >= %s, so the ceiling is below the floor by %s decades"
  % (sci(C_T_floor), str(+d10(C_T_floor / CT_ceil_worst).quantize(Decimal('0.001')))))

# the strengthening factor:  eps_1 <= t_pr / (2 sqrt(1/k) sqrt(C_3))
strength = 2 / F(isq2, 10**40) * 0  # placeholder, computed below properly
sf = t_pr_req / eps1              # = 2*sqrt(1/k), the factor by which the clause beats eps_1 < t_pr
p("  strengthening over the linear clause eps_1 < t_pr: factor %s = %s decades"
  % (sci(sf), str(+d10(sf).quantize(Decimal('0.001')))))

# ---------------------------------------------------------------------------
# TF1-F: AE-red's own clause at the same eps_1 and C_3
# ---------------------------------------------------------------------------
p("")
p("=" * 100)
p("TF1-F -- the ALTERNATIVE route's number: AE-red's own clause 4 C_3 eps_1^2 <= eta_AE")
p("=" * 100)
need = 4 * C_3 * eps1 * eps1
for nm, ea in (("C_S <= 1e2", eta_AE), ("C_S = 1e4", eta_AE_CS4)):
    ok = ea >= need
    m = d10(ea / need) if ok else d10(need / ea)
    p("  eta_AE (%-10s) = %s  vs  4 C_3 eps_1^2 = %s   -> %s by %s decades of energy (%s of eps_1)"
      % (nm, sci(ea), sci(need), "HOLDS" if ok else "FAILS",
         str(+m.quantize(Decimal('0.01'))), str(+(m / 2).quantize(Decimal('0.01')))))
vF = "AE-CLAUSE-HOLDS" if eta_AE >= need and eta_AE_CS4 >= need else "AE-CLAUSE-FAILS"
p("  [TF1-F] %s  at both ends of REVIEW_HIST_S4's C_S range" % vF)
p("  NOTE: this is the alternative route's NUMBER only. Its STATUS is CONDITIONAL <= (MS-Sob) [OPEN],")
p("        HIST.md l.1323 / l.1784 / REVIEW_HIST_S4 l.50, and no script here bears on that.")

# ---------------------------------------------------------------------------
# POST-HOC BLOCK, labelled.  The eps_1 lever: how far must eps_1 fall instead?
# Written AFTER reading the main run.  Labelled [POST-HOC, TF1-P1] per criteria Sec.3.
# ---------------------------------------------------------------------------
p("")
p("=" * 100)
p("[POST-HOC, TF1-P1] -- the eps_1 lever, not pre-registered, labelled post-hoc")
p("=" * 100)
eps1_req = main['t_pr'] / sf
p("  To satisfy eta_flat >= 4 C_3 eps_1^2 at the CURRENT t_pr, eps_1 must fall to")
p("    eps_1 <= t_pr/%s = %s   (vs RLARGE's current ceiling %s)" % (sci(sf), sci(eps1_req), sci(eps1)))
drop = eps1 / eps1_req
p("    i.e. a drop of %s decades in eps_1" % str(+d10(drop).quantize(Decimal('0.001'))))
p("  Price, at a_bad = c_pr eps_1^2 (RLARGE l.88-93): a_bad falls by %s decades;"
  % str(+d10(drop * drop).quantize(Decimal('0.001'))))
p("  eps_1 < t_pr is PRESERVED (ratio t_pr/eps_1 = %s)." % sci(main['t_pr'] / eps1_req))

# ---------------------------------------------------------------------------
# TF1-H: precision
# ---------------------------------------------------------------------------
p("")
p("=" * 100)
p("TF1-H -- precision")
p("=" * 100)
a40 = d10(eta_flat_from_tau(tauR) / main['eta'], 40)
a80 = d10(eta_flat_from_tau(tauR) / main['eta'], 80)
p("  log10 of the 52-decade ratio at prec 40: %s" % str(+a40.quantize(Decimal('0.000000001'))))
p("  log10 of the 52-decade ratio at prec 80: %s" % str(+a80.quantize(Decimal('0.000000001'))))
same = a40.quantize(Decimal('0.000001')) == a80.quantize(Decimal('0.000001'))
p("  every decade comparison above was made on exact Fractions, not on these displays")
p("  [TF1-H] %s" % ("PASS" if same else "FAIL -- displays disagree"))

p("")
p("=" * 100)
p("VERDICT SUMMARY (against checks/tf1_criteria.md Sec.2-3)")
p("=" * 100)
p("  TF1-A  DISTINCT-AND-BOTH-BIND   (reading; TAUFLAT.md Sec.1)")
p("  TF1-B  %s" % main['B'])
p("  TF1-C  current C_D %s the joint-consistency window (boundary %s)"
  % ("INSIDE" if inside else "OUTSIDE", sci(CD_star, 6)))
p("  TF1-D  %s" % main['D'])
p("  TF1-E  %s" % vE)
p("  TF1-F  %s" % vF)
p("  TF1-G  %s" % ("PASS (has power to fail)" if powered else "NO POWER"))
p("  TF1-H  %s" % ("PASS" if same else "FAIL"))
p("=" * 100)

with open(sys.argv[1], "w") as fh:
    fh.write("\n".join(out) + "\n")
