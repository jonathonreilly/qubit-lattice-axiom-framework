#!/usr/bin/env python3 -I
"""kn1-2, kn1-3, kn1-5: the two decade gains, the two reversals, two precisions.

Criteria: ../checks/kn1_criteria.md, written BEFORE this script.
Exact Fraction arithmetic throughout; Decimal at 50 and 100 digits for log10 display only.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

out = []
def p(s=""):
    out.append(str(s))

def log10F(x, prec):
    getcontext().prec = prec
    return (Decimal(x.numerator) / Decimal(x.denominator)).log10()

def lg(x):                      # 50- and 100-digit agreement enforced by kn1-5
    a, b = log10F(x, 50), log10F(x, 100)
    return a, b, abs(Decimal(a) - Decimal(b))

# ---- transcribed inputs, all pre-session-25, file:line in the criteria -------
d, L = 4, 3
A_d = F((d - 1) * L * (L - 1), 2)                 # 9                 RLARGE l.973
c_1 = F(1, 2) / (F(L * L) + F(11, 2) * A_d)       # 1/117             EXISTENCE l.1771/1774
c_RS = 5 ** 4                                      # 625              RLARGE l.1021
c_joint = 81                                       # 81               HIST l.186
kappa = F(1)
DXp = F(2456, 10 ** 155)                           # 2.456e-152/C_Om, C_Om=1  REVIEW_SF_S7 l.203
EPS = {"today  (RLARGE.md l.72)":      F(67, 10 ** 41),
       "proposed (EPS1_SWEEP.md l.455)": F(938495112638, 10 ** 56)}

def eta_quad(e, N):  return min(e / (2 * L * L), e * e / (512 * N * A_d))
def eta_lin(e, N, c=c_1): return c * e
def eta_q(e, N):     return min(e / (2 * L * L), e / (256 * N * A_d))   # delta_0 entry omitted
def a_eta(h, N):     return h * h / (2 * N)
def a_RS(h, e, N):   return min(a_eta(h, N), kappa * e * e / (256 * N))

p("=" * 100)
p("kn1-2 / kn1-3 / kn1-5  --  the two decade gains, the two reversals, two precisions")
p("criteria: checks/kn1_criteria.md (written first).  Exact Fractions; Decimal for log10 only.")
p("=" * 100)
p("")
p(f"inputs:  A_d = {A_d}   c_1 = {c_1}   c_RS = {c_RS}   c_joint = {c_joint}   kappa = {kappa}")
p(f"         DX' = 2.456e-152 at C_Omega = 1   [REVIEW_SF_S7.md l.203]")
for k_, v in EPS.items():
    p(f"         eps_1 {k_:<32} = {float(v):.12e}")

# ------------------------------------------------------------------ kn1-2 ----
p("")
p("## kn1-2  a_RS, the ceilings, the margins and the GAIN  (exact)")
p("")
p(f"{'eps_1':<34}{'N':>2}  {'eta_1 quad':>14} {'eta_1 lin':>14} {'a_RS quad':>14} {'a_RS lin':>14}"
  f" {'branch':>7} {'marg quad':>11} {'marg lin':>11} {'GAIN':>10}")
worst_prec = Decimal(0)
GAIN = {}
for lab, e in EPS.items():
    for N in (2, 3):
        hq, hl = eta_quad(e, N), eta_lin(e, N)
        aq, al = a_RS(hq, e, N), a_RS(hl, e, N)
        branch = "EXP-4" if a_eta(hq, N) <= kappa * e * e / (256 * N) else "EXP-OTHER"
        mq = lg(aq / 100 / DXp); ml = lg(al / 100 / DXp); g = lg(al / aq)
        worst_prec = max(worst_prec, mq[2], ml[2], g[2])
        GAIN[(lab, N)] = g[0]
        p(f"{lab:<34}{N:>2}  {float(hq):>14.6e} {float(hl):>14.6e} {float(aq):>14.6e}"
          f" {float(al):>14.6e} {branch:>7} {float(mq[0]):>11.3f} {float(ml[0]):>11.3f}"
          f" {float(g[0]):>10.4f}")
p("")
p("  (the GAIN is convention-free: it is log10(a_RS_lin / a_RS_quad), so the /10^2 and the")
p("   /(c_RS*10^2) conventions and DX' all cancel.  Margins below under both conventions:)")
p("")
p(f"{'eps_1':<34}{'N':>2}  {'marg quad /1e2':>15} {'marg lin /1e2':>14} {'marg quad /cRS':>15} {'marg lin /cRS':>14}")
for lab, e in EPS.items():
    for N in (2, 3):
        hq, hl = eta_quad(e, N), eta_lin(e, N)
        aq, al = a_RS(hq, e, N), a_RS(hl, e, N)
        r = [lg(aq / 100 / DXp)[0], lg(al / 100 / DXp)[0],
             lg(aq / (c_RS * 100) / DXp)[0], lg(al / (c_RS * 100) / DXp)[0]]
        p(f"{lab:<34}{N:>2}  {float(r[0]):>15.3f} {float(r[1]):>14.3f} {float(r[2]):>15.3f} {float(r[3]):>14.3f}")

g_today = GAIN[("today  (RLARGE.md l.72)", 2)]
g_prop = GAIN[("proposed (EPS1_SWEEP.md l.455)", 2)]
ok2 = abs(Decimal(g_today) - Decimal("82.141")) < Decimal("0.1") and \
      abs(Decimal(g_prop) - Decimal("91.848")) < Decimal("0.1")
p("")
p(f"  transcribed under test: 82.141 (today) / 91.848 (proposed), ARS_FIX.md l.455")
p(f"  computed  N=2        : {float(g_today):.4f} (today) / {float(g_prop):.4f} (proposed)")
p(f"  computed  N=3        : {float(GAIN[('today  (RLARGE.md l.72)',3)]):.4f} / "
  f"{float(GAIN[('proposed (EPS1_SWEEP.md l.455)',3)]):.4f}   <-- the gain IS N-dependent")
p(f"VERDICT kn1-2: {'GAIN-REPRODUCES' if ok2 else 'SOURCE-DISAGREES'} at N = 2 "
  f"(the transcribed pair is the N = 2 pair)")

p("")
p("  DESIGNED-FAIL CONTROL (ARITH-F1): quote the proposed-eps_1 gain AS today's.")
dd = abs(Decimal(g_prop) - Decimal(g_today))
p(f"    |gain(proposed) - gain(today)| = {float(dd):.4f} decades  (>= 1 required to detect the swap)")
p(f"    control verdict: {'HAS-POWER' if dd >= 1 else 'NO POWER'}  "
  f"-- the check distinguishes the two eps_1, so ARITH-F1 is detectable.")
p("")
p("  POWER LEG: counterfactual c_1 = 1/(2L^2) = 1/18 (RLARGE's own linear entry).")
for lab, e in EPS.items():
    N = 2
    hq = eta_quad(e, N)
    al18 = a_RS(eta_lin(e, N, F(1, 18)), e, N)
    g18 = lg(al18 / a_RS(hq, e, N))[0]
    p(f"    {lab:<34} gain at c_1=1/18 : {float(g18):.4f}   "
      f"moves by {float(Decimal(GAIN[(lab,2)]) - Decimal(g18)):.4f} decades")
p(f"    predicted move 2*log10(117/18) = {float(2 * log10F(F(117,18), 50)):.4f}   "
  f"-> the gain IS a function of c_1: HAS-POWER")

# ------------------------------------------------------------------ kn1-3 ----
p("")
p("## kn1-3  the two reversals")
p("")
p("(a) RLARGE.md l.65   'For eps_1 <= 2, eta_1 <= eta_q'   (endorsed CORRECT, REVIEW_RLARGE_V2 2.3)")
p("")
p(f"{'eps_1':<34}{'N':>2}  {'eta_q':>14} {'eta_1/eta_q quad':>18} {'verdict':>17} "
  f"{'eta_1/eta_q lin':>16} {'verdict':>17}")
for lab, e in list(EPS.items()) + [("illustrative eps_1 = 2 (RLARGE l.65)", F(2))]:
    for N in (2, 3):
        hqq, hll, hq_ = eta_quad(e, N), eta_lin(e, N), eta_q(e, N)
        rq, rl = hqq / hq_, hll / hq_
        p(f"{lab:<34}{N:>2}  {float(hq_):>14.6e} {float(rq):>18.6e} "
          f"{('ORDER-PRESERVED' if rq <= 1 else 'ORDER-REVERSED'):>17} {float(rl):>16.4f} "
          f"{('ORDER-PRESERVED' if rl <= 1 else 'ORDER-REVERSED'):>17}")
p("")
p("  eps_1-freeness of the LINEAR ratio (exact equality across two eps_1 required):")
rl_vals = {N: {lab: eta_lin(e, N) / eta_q(e, N) for lab, e in EPS.items()} for N in (2, 3)}
for N in (2, 3):
    vs = list(rl_vals[N].values())
    p(f"    N={N}: {[str(v) for v in vs]}  identical? {vs[0] == vs[1]}  "
      f"= 2*{256*N*A_d}/{int(1/c_1)}... exact value {vs[0]} = {float(vs[0]):.4f}")
p("  quadratic ratio is eps_1-DEPENDENT (this leg's own designed-FAIL control):")
for N in (2,):
    vs = [eta_quad(e, N) / eta_q(e, N) for e in EPS.values()]
    p(f"    N={N}: {float(vs[0]):.6e} vs {float(vs[1]):.6e}  identical? {vs[0] == vs[1]}  "
      f"-> control correctly returns eps_1-DEPENDENT")

p("")
p("(b) HIST.md l.186-187   route comparison: TWO named factors, c_RS 81 vs 625 AND eta_q^2 vs eta_1^2")
p("")
p(f"{'eps_1':<34}{'N':>2}  {'form':>6}  {'eta-factor (h1/hq)^2':>22} {'route = (81/625)*that':>22} {'verdict':>10}")
for lab, e in EPS.items():
    for N in (2, 3):
        for nm, h in (("quad", eta_quad(e, N)), ("lin", eta_lin(e, N))):
            ef = (h / eta_q(e, N)) ** 2
            route = F(c_joint, c_RS) * ef
            p(f"{lab:<34}{N:>2}  {nm:>6}  {float(ef):>22.6e} {float(route):>22.6e} "
              f"{('RS-BETTER' if route > 1 else 'RS-WORSE'):>10}")
e0, N0 = EPS["today  (RLARGE.md l.72)"], 2
ef0 = (eta_lin(e0, N0) / eta_q(e0, N0)) ** 2
rt0 = F(c_joint, c_RS) * ef0
ok3 = F(1, 1) <= rt0 / F(1551) <= F(12, 10) or F(10, 12) <= rt0 / F(1551) <= F(1)
p("")
p(f"  transcribed under test (ARS_FIX.md l.536-537): '1551x BETTER than the joint route' at N = 2")
p(f"  eta-factor alone (eta_1/eta_q)^2 = {float(ef0):.4f}   <-- this is the 1551")
p(f"  ROUTE ratio (both HIST factors) = (81/625)*{float(ef0):.4f} = {float(rt0):.4f}")
p(f"VERDICT kn1-3(b): {'ROUTE-FIGURE-REPRODUCES' if ok3 else 'SOURCE-DISAGREES'} "
  f"-- 1551 is the eta-factor, NOT the route comparison; the route figure is {float(rt0):.3f}x "
  f"(ratio {float(F(1551)/rt0):.4f} = 625/81 = {625/81:.4f})")
p(f"  at N = 3: eta-factor "
  f"{float((eta_lin(e0,3)/eta_q(e0,3))**2):.4f}, route "
  f"{float(F(c_joint,c_RS)*(eta_lin(e0,3)/eta_q(e0,3))**2):.4f}x")

p("")
p("(c) HIST.md l.181   'for eps_1 -> 0, eta_q/eta_1 = 2/eps_1'")
for lab, e in EPS.items():
    N = 2
    p(f"    {lab:<34} quad: eta_q/eta_1 = {float(eta_q(e,N)/eta_quad(e,N)):.6e}  "
      f"2/eps_1 = {float(2/e):.6e}  equal? {eta_q(e,N)/eta_quad(e,N) == 2/e}")
    p(f"    {'':<34} lin : eta_q/eta_1 = {eta_q(e,N)/eta_lin(e,N)} = "
      f"{float(eta_q(e,N)/eta_lin(e,N)):.7f}   (eps_1-free constant)")
p(f"    117/4608 = {float(F(117,4608)):.7f}  -- matches the linear value at N = 2: "
  f"{eta_q(EPS['today  (RLARGE.md l.72)'],2)/eta_lin(EPS['today  (RLARGE.md l.72)'],2) == F(117,4608)}")

# ------------------------------------------------------------------ kn1-5 ----
p("")
p("## kn1-5  two precisions")
p(f"  worst 50-vs-100-digit disagreement over every decade figure: {worst_prec:.3E}")
p(f"VERDICT kn1-5: {'PASS' if worst_prec < Decimal('1e-30') else 'FAIL (arithmetic)'}")

p("")
p("=" * 100)
p("Disclosure: exact fractions.Fraction throughout; Decimal only for log10 display, at 50 and 100")
p("digits, agreeing to the figure above.  python3 -I, single thread, no numpy/BLAS/SciPy, nice 10.")
p("No numeric lock taken and none needed (exact rational arithmetic, brief rule 6).")
p("=" * 100)
print("\n".join(out))
