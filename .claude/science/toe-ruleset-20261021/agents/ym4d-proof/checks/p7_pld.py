#!/usr/bin/env python3
# checks/p7_pld.py -- check p7 for PLD.md session 7 (lane E).
# Criteria: checks/p7_criteria.md (md5 ceaf6aa8f145413a3dd4f35ea673c955), written BEFORE this script.
# Exact arithmetic only: fractions.Fraction and decimal.Decimal(60). No numpy, no BLAS, no sampling, no lock.
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import sys
getcontext().prec = 60

res = []
def rec(name, ok, msg):
    res.append((name, ok, msg))
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)

# ---------- recorded inputs (all pre-session-7, sourced in the criteria file) ----------
eps1  = Fr(67, 10**41)          # 6.7e-40  (RLARGE §0 / p6 A2)
gK2   = Fr(1, 10**94)           # 1e-94    (RLARGE §0 / p6 A2)
u     = 1/gK2
dof   = 52488                   # p6 D1
heur  = Decimal("18190.95")     # p6 D1
ceil9 = Decimal(10)**9          # §18.8 (ii) clause 5
n_int = 216                     # HW §0
theta = Fr(1, 24)               # p6 C2
d     = 4

# ---------- A ----------
X = u * eps1**2
Y = eps1**2 / gK2
okA1 = (X == Y) and (float("%.4g" % float(X)) == 4.489e15)
rec("A1", okA1, "u*eps1^2 = (eps1/gK)^2 exactly: %s ; value = %.6e (p6 A2 recorded 4.489e15)" % (X == Y, float(X)))

lam = Fr(1, 2)
M   = (1 - lam) * X
rho = lam * X / Fr(10**9)
okA2 = (Fr(22, 10) * Fr(10)**15 <= M <= Fr(23, 10) * Fr(10)**15) and \
       (Fr(22, 10) * Fr(10)**6 <= rho <= Fr(23, 10) * Fr(10)**6)
rec("A2", okA2, "margin (1-lam)*u*eps1^2 = %.4e ; log-miss ratio vs 1e9 ceiling = %.4e" % (float(M), float(rho)))

Xctrl = u * gK2                 # eps1 := gK
rec("A3", Xctrl == 1, "negative control: with eps1 := gK the quantity is %s (must be exactly 1)" % Xctrl)

# ---------- B ----------
def E(dofv, lam_fr):
    if lam_fr == 0:
        return Decimal(0)
    one_minus = Decimal(1) - (Decimal(lam_fr.numerator) / Decimal(lam_fr.denominator))
    return (Decimal(dofv) / Decimal(2)) * (Decimal(1) / one_minus).ln()

B1 = E(dof, Fr(1, 2))
okB1 = abs(B1 - heur) < Decimal("0.01")
rec("B1", okB1, "(dof/2)*ln(1/(1-lam)) at dof=52488, lam=1/2 = %s ; p6 D1 recorded %s ; diff %s"
    % (str(B1)[:12], heur, str(abs(B1 - heur))[:10]))

B2a = E(dof, Fr(0))
B2b = E(dof, Fr(10**6 - 1, 10**6))
okB2 = (B2a == 0) and (B2b > Decimal(10)**5)
rec("B2", okB2, "negative control: E(lam=0) = %s (must be 0); E(lam=1-1e-6) = %s (must exceed 1e5)"
    % (B2a, str(B2b)[:12]))

Bval = Decimal(dof) / (Decimal(2) * (Decimal(1) - Decimal("0.5")))
okB3 = Bval <= ceil9 / Decimal("0.5")
dec_margin = ((ceil9 / Decimal("0.5")) / Bval).log10()
rec("B3", okB3, "equipartition B = dof/(2(1-lam)) = %s vs restated ceiling 1e9/lam = %s ; margin %s decades"
    % (Bval, ceil9 / Decimal("0.5"), str(dec_margin)[:6]))

# ---------- C ----------
bad = [x for x in [Fr(1, 2**j) for j in range(1, 11)] if not (1 / (1 - x) <= 1 + 2 * x)]
rec("C1", not bad, "1/(1-x) <= 1+2x for x in {2^-1..2^-10}: %d violations" % len(bad))
xc = Fr(3, 4)
rec("C1n", not (1 / (1 - xc) <= 1 + 2 * xc),
    "negative control at x=3/4: 1/(1-x) = %s vs 1+2x = %s (inequality must FAIL)" % (1 / (1 - xc), 1 + 2 * xc))

L0 = (Decimal(3 * n_int - 3) / Decimal(2)) * (Decimal(1) / (Decimal(1) - Decimal(1) / Decimal(24))).ln()
okC2 = Decimal("13.0") <= L0 <= Decimal("14.5")
rec("C2", okC2, "level-0 window log C_fc = ((3*216-3)/2)*ln(1/(1-1/24)) = %s" % str(L0)[:10])

# ---------- D ----------
def expo(dd):
    return (dd - 1) - 2 * (dd - 2)

def T(dd, Mx):
    e = expo(dd)
    s = Fr(0)
    for r in range(1, Mx + 1):
        s += Fr(1, r**(-e)) if e < 0 else Fr(r**e)
    return s

ln10 = Decimal(10).ln()
e4 = expo(4)
T3, T4, T5 = T(4, 10**3), T(4, 10**4), T(4, 10**5)
d1a = Decimal(T4.numerator) / Decimal(T4.denominator) - Decimal(T3.numerator) / Decimal(T3.denominator)
d1b = Decimal(T5.numerator) / Decimal(T5.denominator) - Decimal(T4.numerator) / Decimal(T4.denominator)
okD1 = (e4 == -1) and all(abs(x - ln10) / ln10 < Decimal("0.01") for x in (d1a, d1b))
rec("D1", okD1, "d=4 exponent = %d ; increments %s and %s vs ln10 = %s (log-divergent)"
    % (e4, str(d1a)[:8], str(d1b)[:8], str(ln10)[:8]))

e5 = expo(5)
T5_5 = T(5, 10**5)
basel = Decimal(T5_5.numerator) / Decimal(T5_5.denominator)
pi2_6 = Decimal("1.6449340668482264364724151666460251892189499012068")
okD2 = (e5 == -2) and abs(basel - pi2_6) < Decimal("0.001")
rec("D2", okD2, "negative control d=5: exponent = %d ; sum to 1e5 = %s vs pi^2/6 = %s (convergent)"
    % (e5, str(basel)[:10], str(pi2_6)[:10]))

# ---------- E ----------
chi = 5**d
th_max = Fr(1, 24 * chi)
okE1 = (chi == 625) and (th_max > Fr(8, 10**7))
rec("E1", okE1, "chi = 5^4 = %d ; theta_max = 1/(24*chi) = %.4e ; recorded fallback theta 8e-7"
    % (chi, float(th_max)))

# ---------- F ----------
okF1 = (1 + 3**d == 82) and (1 + 2**d == 17)
rec("F1", okF1, "closed-column price 1+3^d = %d ; open-column price 1+2^d = %d ; ratio 3^d/2^d = %s"
    % (1 + 3**d, 1 + 2**d, Fr(3**d, 2**d)))

# ---------- summary ----------
fails = [n for n, ok, _ in res if not ok]
print("")
print("SUMMARY: %d criteria, %d FAIL" % (len(res), len(fails)))
print("FAILS: " + (", ".join(fails) if fails else "none"))
sys.exit(0)
