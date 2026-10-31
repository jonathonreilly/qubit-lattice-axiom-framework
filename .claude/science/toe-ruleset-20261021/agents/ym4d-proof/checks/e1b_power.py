#!/usr/bin/env python3 -I
# checks/e1b_power.py -- RE-RUN of criterion e1-5 only, under a new id, with
# checks/e1_criteria.md UNTOUCHED.  e1_sweep.py returned NO POWER on the clause half
# because TAUFLAT's quoted value 9.38496e-45 sits just ABOVE the exact requirement, so
# DESC-ε (iii) fails at it and the verdict could not flip.  This run substitutes the EXACT
# requirement E_x (the largest admissible threshold, computed here) for TAUFLAT's rounded
# figure and re-asks the same pre-registered question.  Nothing else is changed.
# Exact Fraction; Decimal for display only; plain python -I, single thread, no BLAS.

from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60

def dec(x, p=40):
    getcontext().prec = p
    if isinstance(x, Decimal):
        return +x
    return Decimal(x.numerator) / Decimal(x.denominator)
def L10(x, p=50):
    getcontext().prec = p
    return dec(x, p).log10()
def E(m, e): return F(m) * F(10)**e

# transcribed, identical to e1_sweep.py
T_PR = E("1.33384", -39)                 # TAUFLAT §2.2 l.203
C_FLAT, C_PRIME = F(1, 640), F(53)       # RLARGE l.90
EPS_T = E("6.7", -40)                    # RLARGE l.72
EPS_TAUFLAT = E("9.38496", -45)          # TAUFLAT §4 C l.408
G_DX2 = E("2.456", -152)                 # REVIEW_SF_S7 l.203
C3 = F(1)                                # HIST A5 (A) reference value

eta_flat = C_FLAT * T_PR**2 / C_PRIME**4
# exact requirement: 4 C_3 ε² ≤ η_♭  <=>  ε ≤ sqrt(η_♭/(4C_3)).  Exact rational bound by
# integer square root of the rational η_♭/(4C_3) scaled by 10^100, truncated DOWNWARD.
import math
S = 10**100
q = eta_flat / (4*C3)
isq = math.isqrt(q.numerator * S * S // q.denominator)
E_x = F(isq, S)                                   # E_x ≤ sqrt(η_♭/4) exactly, by truncation
assert 4*C3*E_x**2 <= eta_flat

def clause(e): return 4*C3*e*e <= eta_flat
def window(e, g2): return dec(e, 60) / dec(g2, 60).sqrt()

o = []
def P(s=""): o.append(s)
P("e1b_power.py -- re-run of criterion e1-5; checks/e1_criteria.md untouched.")
P("")
P("=== the exact requirement, computed (this is why e1-5 had no power) ===")
P("  eta_flat                          = %s" % dec(eta_flat, 12))
P("  exact bound sqrt(eta_flat/4C_3)   = %s" % dec(E_x, 12))
P("  TAUFLAT §4 C quotes               = %s" % dec(EPS_TAUFLAT, 12))
P("  quoted / exact                    = %s   -> quoted value is ABOVE the bound"
  % dec(EPS_TAUFLAT / E_x, 10))
P("  clause at TAUFLAT's quoted value  : %s" % ("HOLDS" if clause(EPS_TAUFLAT) else "FAILS"))
P("  clause at the exact bound E_x     : %s" % ("HOLDS" if clause(E_x) else "FAILS"))
P("  shortfall at the quoted value     : %s decades of energy"
  % (L10(4*C3*EPS_TAUFLAT**2 / eta_flat)).quantize(Decimal('1E-9')))
P("  decades below E_t required        : %s" % (L10(EPS_T/E_x)).quantize(Decimal('0.0001')))
P("")
P("=== e1-5 POWER, re-asked at E_x (criteria unchanged) ===")
E_c1 = E("1", -80)     # below g_DX = sqrt(2.456e-152)
E_c2 = EPS_T
f_x, f_c1 = window(E_x, G_DX2) > 1, window(E_c1, G_DX2) > 1
c_x, c_c2 = clause(E_x), clause(E_c2)
P("  e1-2 at E_x  : %s      e1-2 at E_c1 : %s      FLIPPED: %s"
  % ("FLOOR-RESPECTED" if f_x else "FLOOR-VIOLATED",
     "FLOOR-RESPECTED" if f_c1 else "FLOOR-VIOLATED", f_x != f_c1))
P("  clause at E_x: %s        clause at E_c2: %s        FLIPPED: %s"
  % ("CLAUSE-HOLDS" if c_x else "CLAUSE-FAILS",
     "CLAUSE-HOLDS" if c_c2 else "CLAUSE-FAILS", c_x != c_c2))
P("  VERDICT e1-5 (re-run id e1b): %s"
  % ("HAS-POWER (both flip)" if (f_x != f_c1 and c_x != c_c2) else "NO POWER"))
P("")
P("=== third flip, pre-registered in e1_criteria §e1-5 as the independent construction ===")
P("  the floor check is tested against EXISTENCE.md's own window statement, a different file")
P("  from the one proposing the change.  Boundary: the window closes at ε = g_DX = %s;"
  % dec(G_DX2, 60).sqrt().quantize(Decimal('1E-79')))
P("  E_x is %s decades above it, E_c1 is %s decades below it."
  % ((dec(E_x,60)/dec(G_DX2,60).sqrt()).log10().quantize(Decimal('0.01')),
     (-(dec(E_c1,60)/dec(G_DX2,60).sqrt()).log10()).quantize(Decimal('0.01'))))
print("\n".join(o))
