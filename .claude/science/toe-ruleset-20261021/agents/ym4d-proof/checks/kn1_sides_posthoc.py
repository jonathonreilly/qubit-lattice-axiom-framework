#!/usr/bin/env python3 -I
"""kn1-6 POST-HOC (NOT pre-registered in kn1_criteria.md; carries no pre-registered verdict).

Three things the adoption patch needs as written text and that were not in the criteria:
  (A) the two side conditions of Corollary KN-step' at t = eps_1, d = 4, L = 3;
  (B) the two EXISTENCE constants the patch quotes (106 and 5.5), rebuilt;
  (C) the (PLD)_k in-step shortfall of REVIEW_PLD_S3 l.304-309, before and after the adoption.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60
import math

o = []
def p(s=""): o.append(str(s))

p("=" * 92)
p("kn1-6  POST-HOC  (not pre-registered; no pre-registered verdict attaches to any line here)")
p("=" * 92)

d, L, N_list = 4, 3, (2, 3)
A_d = F((d - 1) * L * (L - 1), 2)        # 9
c_1 = F(1, 117)
pi = Decimal(str(math.pi))
e_ = Decimal(1).exp()

p("")
p("(A) side conditions of Corollary KN-step' at t = eps_1   [EXISTENCE.md l.1774-1775]")
p("    (S1) t <= 1/(106*sqrt(N)*A_d^2*c_1^2)        (S2) (pi/3)*A_d*c_1*t <= 1/4")
num = F(1, 1) / (106 * A_d ** 2 * c_1 ** 2)          # = 117^2/(106*81)
p(f"    (S1): 1/(106*A_d^2*c_1^2) = {num} = {float(num):.6f};  divide by sqrt(N):")
for N in N_list:
    p(f"          N={N}:  eps_1 <= {float(num)/math.sqrt(N):.6f}")
s2 = Decimal(3) * Decimal(int(1 / c_1)) / (Decimal(4) * Decimal(int(A_d)) * pi)
p(f"    (S2): eps_1 <= 3/(4*A_d*c_1^-1^-1 ...) = 117*3/(4*9*pi) = 351/(36 pi) = {s2:.6f}")
p(f"    live eps_1 ~ 6.7e-40 (RLARGE l.72) clears BOTH by ~40 decades; both FAIL at eps_1 = 10.")
for t in (F(2), F(10)):
    p(f"      counterfactual t={t}: (S1) N=2 {'holds' if float(t) <= float(num)/math.sqrt(2) else 'FAILS'}"
      f" ; (S2) {'holds' if Decimal(float(t)) <= s2 else 'FAILS'}")

p("")
p("(B) the two EXISTENCE constants, rebuilt   [EXISTENCE.md l.1771 (5.5), l.1775 (106)]")
c106 = Decimal(8) * Decimal(12) * (pi / 3) ** 2
p(f"    106  rebuilds as 8*12*(pi/3)^2 = {c106:.6f}   ratio 106/that = {Decimal(106)/c106:.6f}")
c55 = Decimal(4) * ((Decimal("0.25").exp() - 1) / Decimal("0.25")) * (pi / 3)
p(f"    5.5  rebuilds as 4*((e^(1/4)-1)/(1/4))*(pi/3) = {c55:.6f}   <= 5.5 ? {c55 <= Decimal('5.5')}")
p(f"    (the patch keeps 5.5, the safe side; c_1 = 1/(2(L^2+5.5A_d)) = 1/117 depends on the 5.5)")

p("")
p("(C) (PLD)_k in-step shortfall   [REVIEW_PLD_S3.md l.304-305, l.307-309]")
p("    RS-compatibility ceiling : eta_RS <= eps_1/L^2 (1+o(1))           -> eps_1/9")
p("    PLD-desc in-step range   : tau >= 2*tau_bg, tau_bg >= eps_1/L^2(1-o(1)) -> tau >= 2*eps_1/9")
p("    refined range            : tau >= (1+delta)*tau_bg               -> tau >= (1+delta)*eps_1/9")
cands = {"RLARGE (R3) quadratic entry eps_1^2/(4608N)": None,
         "RLARGE (R3) linear entry   eps_1/18": F(1, 18),
         "RS-compatibility ceiling   eps_1/9.009": F(1000, 9009),
         "KN-step' c_1 eps_1         eps_1/117": c_1}
need2 = F(2, 9)
p("")
p(f"    {'threshold (as a multiple of eps_1)':<46}{'value':>12} {'/ (2 eps_1/9)':>15} {'reaches 2 tau_bg?':>19}")
for nm, v in cands.items():
    if v is None:
        p(f"    {nm:<46}{'~1e-41':>12} {'~1e-40':>15} {'NO':>19}")
    else:
        p(f"    {nm:<46}{float(v):>12.6f} {float(v/need2):>15.6f} "
          f"{('YES' if v >= need2 else 'NO'):>19}")
p("")
p("    Even the RS-compatibility CEILING itself (eps_1/9.009) falls short of 2*tau_bg by x2.002,")
p("    and of the refined (1+delta)*tau_bg for every delta > 1/1000.  So the shortfall is")
p("    structural in the RS-compatibility cap, not in the choice of c_1:  CONFIRMED.")
p("    c_1 eps_1 = eps_1/117 is x26.0 below 2*tau_bg -- the adoption moves the threshold")
p("    FURTHER from the in-step range, not closer.")
p("")
p("=" * 92)
print("\n".join(o))
