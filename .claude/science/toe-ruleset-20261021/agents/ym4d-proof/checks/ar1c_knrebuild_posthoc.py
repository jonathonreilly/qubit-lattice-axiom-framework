#!/usr/bin/env python3
# ar1c -- POST-HOC. Written AFTER ar1/ar1b produced their verdicts; it carries NO pre-registered verdict.
# Purpose: verify the internal inequalities of EXISTENCE's Lemma KN and Corollary KN-step as part of
# REBUILDING them (standing rule: load-bearing cited mathematics is rebuilt, not cited), and verify the
# chart condition that lets RLARGE's Lemma RS (R1) data be fed to KN.
# Exact Fraction arithmetic; Decimal for e, pi and display only. python3 -I, single thread, no numpy.

from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60

PI = F(Decimal("3.14159265358979323846264338327950288419716939937510"))
E  = F(Decimal("2.71828182845904523536028747135266249775724709369996"))

def ex(x, terms=40):                     # exp of a Fraction by its series (exact rational partial sum)
    s, t = F(1), F(1)
    for n in range(1, terms):
        t = t * x / n
        s += t
    return s

L, d, N_list = 3, 4, (2, 3, 8, 38)
A_d = F((d - 1) * L * (L - 1), 2)
L2 = F(L * L)
c_1 = F(1, 2) / (L2 + F(11, 2) * A_d)

def sci(x, sig=6):
    getcontext().prec = 30
    return format(Decimal(x.numerator) / Decimal(x.denominator), ".%de" % (sig - 1))

print("=" * 96)
print("ar1c  POST-HOC rebuild checks for Lemma KN / Corollary KN-step (EXISTENCE l.1756-1784).")
print("No pre-registered verdict. A_d=%s L^2=%s c_1=%s" % (A_d, L2, c_1))
print("=" * 96)

# ---- KN step 1: ||R|| <= (e^d - 1)^2 + d^2 e^d <= 3 d^2 for d <= 1/4   (EXISTENCE l.1761)
print()
print("[1] Lemma KN's  ||R|| <= (e^delta-1)^2 + delta^2 e^delta <= 3 delta^2  for delta <= 1/4.")
print("    The ratio ((e^d-1)^2 + d^2 e^d)/d^2 is increasing in d, so the worst case is d = 1/4:")
worst = None
for num in (1, 10, 50, 100, 200, 250):
    dlt = F(num, 1000)
    r = ((ex(dlt) - 1) ** 2 + dlt * dlt * ex(dlt)) / (dlt * dlt)
    print("      delta=%-7s ratio = %s" % (dlt, sci(r)))
    worst = r
print("    worst (delta=1/4) ratio = %s  <= 3 ?  %s" % (sci(worst), "YES -- STEP-1-HOLDS" if worst <= 3 else "NO -- FAILS"))
print("    (and e^{1/2}+e^{1/4} = %s <= 3, which is the bound EXISTENCE actually writes)"
      % sci(ex(F(1, 2)) + ex(F(1, 4))))

# ---- KN step 2: 1/2 x^2 - 3 sqrt(N) d^2 x >= 1/4 x^2  <=>  x >= 12 sqrt(N) d^2   (EXISTENCE l.1762)
print()
print("[2] Lemma KN's threshold is EXACT algebra, not an estimate:")
print("    1/2 x^2 - 3 sqrt(N) delta^2 x >= 1/4 x^2  <=>  1/4 x >= 3 sqrt(N) delta^2  <=>  x >= 12 sqrt(N) delta^2.")
print("    So the '12' of EXISTENCE l.1758 is forced by the 1/2 -> 1/4 margin; STEP-2-IDENTITY.")

# ---- KN step 3: Re tr(1 - Z^{-1}) = 1/2 ||1 - Z||_HS^2 for unitary Z     (EXISTENCE l.1762)
print()
print("[3] For unitary Z: ||1-Z||_HS^2 = tr((1-Z)*(1-Z)^dag) = tr(2 - Z - Z^dag) = 2 Re tr(1 - Z^{-1}).")
print("    Exact identity (Z^dag = Z^{-1}); STEP-3-IDENTITY.")

# ---- KN-step's re-centring algebra: L^2 eta + 4(e^delta - 1) <= (L^2 + 5.5 A_d) eta = t/2 on {eta < c_1 t}
print()
print("[4] KN-step's re-centring: ||1-W'_P|| <= L^2 eta + 4(e^delta - 1), delta <= (pi/3) A_d eta (RS (R1)).")
print("    Need 4(e^delta - 1) <= 5.5 A_d eta.  Worst case delta = 1/4 gives coefficient")
coef = 4 * (ex(F(1, 4)) - 1) / F(1, 4) * (PI / 3)
print("      4*(e^{1/4}-1)/(1/4)*(pi/3) = %s   <= 5.5 ?  %s" % (sci(coef), "YES" if coef <= F(11, 2) else "NO"))
print("    and (L^2 + 5.5 A_d) * c_1 = %s  -> the first part is exactly t/2 on {eta < c_1 t}: %s"
      % ((L2 + F(11, 2) * A_d) * c_1, "EXACT-HALF" if (L2 + F(11, 2) * A_d) * c_1 == F(1, 2) else "NOT-HALF"))
print("    exhaustiveness: t/2 + 4*(t/8) = t, so {eta < c_1 t} and all four ||V_c - W'_c|| < t/8")
print("    forces ||1 - V_P|| < t.  The dichotomy is exhaustive by construction: DICHOTOMY-EXHAUSTIVE.")

# ---- KN-step's t-bound, rebuilt
print()
print("[5] KN-step's t <= 1/(106 sqrt(N) A_d^2 c_1^2), rebuilt: KN is applied at t/8, so t/8 >= 12 sqrt(N) delta^2")
print("    with delta <= (pi/3) A_d c_1 t gives t <= 1/(8*12*(pi/3)^2 sqrt(N) A_d^2 c_1^2).")
coef5 = 8 * 12 * (PI / 3) ** 2
print("      my coefficient 8*12*(pi/3)^2 = %s ; EXISTENCE writes 106 -> ratio %s (REPRODUCES)"
      % (sci(coef5), sci(F(106) / coef5)))

# ---- the chart condition that feeds RLARGE's (R1) data into KN's hypothesis T_i = S e^{X_i}, X_i in su(N)
print()
print("[6] Feeding RS (R1) into KN's hypothesis.  RS (R1) gives ||T^sigma_y - S_c||_op <= A_d eta, i.e.")
print("    ||S_c^{-1} T - 1||_op <= A_d eta.  A traceless X with e^X = S_c^{-1}T and ||X||_op <= (pi/3)A_d eta")
print("    exists iff the eigenphases can be chosen in (-pi,pi) summing to EXACTLY 0.  det = 1 puts the sum")
print("    in 2 pi Z, and each |theta_j| <= (pi/3) A_d eta, so the sum is 0 whenever N (pi/3) A_d eta < 2 pi,")
print("    i.e. eta < 6/(N A_d).  At eta = c_1 eps_1 that reads eps_1 < 6/(N A_d c_1):")
for N in N_list:
    bnd = F(6) / (N * A_d * c_1)
    print("      N=%-3d chart condition: eps_1 < %s" % (N, sci(bnd)))
print("    Every live eps_1 is ~1e-40, so CHART-AVAILABLE at every N up to astronomically large values.")
print("    (EXISTENCE l.1772's 'A_d eta <= 1' is the weaker, sufficient-for-the-ribbon-step form.)")

# ---- the two kernel exponents coincide
print()
print("[7] The kernel branch constant is the SAME before and after:")
print("    RS (R4) l.998-999: bracket >= eps^2/(128N) - 2 A_d eta_1 >= eps^2/(256N)  (needs eta_1 <= eps^2/(512 N A_d))")
print("    KN at t/8       : exponent kappa (t/8)^2/(4N) = kappa t^2/(256N)          (needs only delta <= 1/4)")
print("    Both land on kappa eps_1^2/(256 N): SAME-CONSTANT, by different routes. So a_RS's SECOND entry")
print("    is untouched by the adoption and only a_eta moves.")
print()
print("=" * 96)
