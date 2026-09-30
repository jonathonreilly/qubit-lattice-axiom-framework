#!/usr/bin/env python3
"""Kill-check T56: (1) does a SINGLE alpha close the lane's eta chain under the corrected kernel?
(2) what pins does each repo kernel give?  (3) is the April note's 0.048 reproduced by any code?
Claude Sonnet 5.5 (same family as attacker).  Own implementation (mpmath quad), not the attacker's file."""
import math, mpmath as mp
from scipy.optimize import brentq
mp.mp.dps = 25
R_BASE = 31/9

def avg(c, a, attractive):
    """<S> = int S(k*pi*alpha/v) v^2 e^{-a v^2} / int v^2 e^{-a v^2};  c = k*alpha_eff (k=1 pi-form, k=2 2pi-form)"""
    sgn = 1 if attractive else -1
    def S(z):
        z = sgn*mp.pi*z
        return mp.mpf(1) if abs(z) < mp.mpf('1e-30') else z/(1-mp.e**(-z))
    num = mp.quad(lambda v: S(c/v)*v*v*mp.e**(-a*v*v), [0, 1, 5, mp.inf])
    den = mp.quad(lambda v: v*v*mp.e**(-a*v*v), [0, 1, 5, mp.inf])
    return float(num/den)

def R(alpha_s, a=25/4, k=1):
    s1 = avg(k*4/3*alpha_s, a, True)
    s8 = avg(k*alpha_s/6, a, False)
    return R_BASE*(8*s1+s8)/9

# ---- lane eta chain (bypass note eq): eta = K xF /(sqrt(g*) Mpl pi aX^2 R 3.65e7) m^2
K, xF, gs, Mpl, m, ETA = 1.07e9, 25.0, 106.75, 1.2209e19, 3940.53, 6.12e-10
def eta(aX, Rv): return K*xF/(math.sqrt(gs)*Mpl*math.pi*aX**2*Rv*3.65e7)*m*m

print("== (1) single-alpha closure of the eta chain, corrected kernel (k=2, a=x/4), alpha_X = alpha_S = alpha")
for al in [0.06, 0.07, 0.075, 0.078, 0.0785, 0.08, 0.085, 0.0907]:
    Rv = R(al, k=2); e = eta(al, Rv)
    print(f"  alpha={al:.4f}  R={Rv:.4f}  eta={e:.3e}  ({e/ETA-1:+.1%})")
f = lambda al: eta(al, R(al, k=2))/ETA - 1
a_close = brentq(f, 0.05, 0.0907, xtol=1e-7)
print(f"  ROOT: single alpha closing eta_obs (corrected kernel) = {a_close:.5f}  (R={R(a_close,k=2):.3f}); alpha_LM=0.09067; alpha_s(3.94TeV, SM 1-loop)=0.0785")
f1 = lambda al: eta(al, R(al, k=1))/ETA - 1
a_close1 = brentq(f1, 0.05, 0.12, xtol=1e-7)
print(f"  ROOT lane pi-kernel = {a_close1:.5f} (R={R(a_close1,k=1):.3f})")

print("\n== (2) pins of R_obs under each repo kernel (colour-resolved 8:1 weights)")
for name, a, k in [("June/common.py: a=x/4, pi ", 25/4, 1), ("corrected physics: a=x/4, 2pi", 25/4, 2), ("April script (omega_lambda_derivation.py): a=x/2, pi", 25/2, 1)]:
    row = []
    for tgt in [5.364, 5.375, 5.48]:
        al = brentq(lambda x: R(x, a=a, k=k)-tgt, 0.005, 0.3, xtol=1e-7)
        row.append(f"R={tgt}: alpha={al:.4f}")
    print(f"  {name:55s} " + " | ".join(row))
print("  R at alpha_LM=0.09067:  pi/x4: %.4f  2pi/x4: %.4f  april(a=x/2,pi): %.4f" % (R(0.09067), R(0.09067,k=2), R(0.09067,a=25/2,k=1)))

print("\n== (3) which (kernel) reproduces the notes' hand numbers: alpha=0.048 -> R=5.48 (S=1.59); band alpha in [0.03,0.05] -> S in [1.4,1.7] / R in [4.8,5.3]")
for name, a, k in [("pi, a=x/4 (June)", 25/4, 1), ("2pi, a=x/4 (corrected)", 25/4, 2), ("pi, a=x/2 (April script)", 25/2, 1), ("2pi, a=x/2", 25/2, 2), ("pi, a=x", 25.0, 1)]:
    r048 = R(0.048, a=a, k=k); r03 = R(0.03, a=a, k=k); r05 = R(0.05, a=a, k=k)
    print(f"  {name:28s} R(0.048)={r048:.3f}  S band(0.03..0.05)=[{r03/R_BASE:.3f},{r05/R_BASE:.3f}]  R band=[{r03:.3f},{r05:.3f}]")
