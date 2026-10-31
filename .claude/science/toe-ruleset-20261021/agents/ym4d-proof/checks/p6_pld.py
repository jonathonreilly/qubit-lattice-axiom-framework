#!/usr/bin/env python3
# checks/p6_pld.py -- check p6 for PLD lane E session 6.
# Criteria: checks/p6_criteria.md (written BEFORE this file). Exact rational / elementary float only.
# No numpy, no BLAS, no sampling, single thread.
from fractions import Fraction as F
import math, sys

fails = []
def rep(cid, ok, msg):
    print(("PASS " if ok else "FAIL ") + cid + ": " + msg)
    if not ok: fails.append(cid)

# ---------- recorded inputs ----------
c_pr   = F(1, 640 * 53**2)
eps1   = 6.7e-40
gK2    = 1e-94
a_rec  = 1.0e-86
theta  = F(1, 24)
lam    = F(1, 2)
n_int  = 216
L, d   = 3, 4
Delta_sh = 3073361

# ---------- A1 ----------
kappa_min = 256 * c_pr / (24 * lam)
rep("A1", c_pr == F(1,1797760) and kappa_min == F(1,84270) and float(kappa_min) < 1.2e-5,
    "c_pr=%s=%.6e  kappa_min=%s=%.6e" % (c_pr, float(c_pr), kappa_min, float(kappa_min)))

# ---------- A2 / A3 ----------
def gap(e1, g2):
    u = 1.0/g2
    return u*e1*e1, (e1/math.sqrt(g2))**2
v1, v2 = gap(eps1, gK2)
rep("A2", abs(v1/v2 - 1.0) <= 1e-12 and 4.0e15 <= v1 <= 5.0e15,
    "u*eps1^2=%.6e  (eps1/gK)^2=%.6e  rel.diff=%.2e" % (v1, v2, abs(v1/v2-1.0)))
w1, w2 = gap(math.sqrt(gK2), gK2)
rep("A3", abs(w1 - 1.0) <= 1e-12, "control at eps1=gK: value=%.15f (must be 1)" % w1)

# ---------- B1 ----------
def b_n(cp, cU): return 531441*38418*cp + 38417*cU
def b_D(cp, cU): return 38416*(531441*cp + cU)
bn11, bD11 = b_n(1,1), b_D(1,1)
bn82, bD82 = b_n(82,82), b_D(82,82)
rep("B1", bn11 == 20416938755 and bn11//10**10 == 2
          and F(bn82, bn11) <= 82 and F(bD82, bD11) <= 82,
    "b_n(1,1)=%d (%.4e)  b_n(82,82)/b_n(1,1)=%.6f  b_D ratio=%.6f"
    % (bn11, bn11, bn82/bn11, bD82/bD11))

# ---------- B2 ----------
g2a = a_rec / bn11
g2b = a_rec / bn82
rep("B2", abs(g2a/4.9e-97 - 1.0) <= 0.10 and 81 <= g2a/g2b <= 83,
    "g2_CRC(c+=1)=%.4e (recorded 4.9e-97, rel.diff %.3f)  ratio before/after ring=%.4f"
    % (g2a, abs(g2a/4.9e-97 - 1.0), g2a/g2b))

# ---------- B3 / B3n ----------
shift = lambda x: (bn11 + x)/bn11
rep("B3",  shift(1e9)  <= 1.05, "shift(log c_lcr=1e9)=%.6f  (<=1.05)" % shift(1e9))
rep("B3n", shift(1e11) >= 5.0,  "control shift(log c_lcr=1e11)=%.4f  (>=5)" % shift(1e11))

# ---------- C1 ----------  (eps_1^2 cancels; compare lam*kappa/256 with theta*c_pr)
lhs = lambda kap: lam*kap/256
rhs = theta*c_pr
ok_eq  = lhs(kappa_min) == rhs
ok_str = lhs(F(1)) > rhs
ok_bad = lhs(kappa_min/2) < rhs
rep("C1", ok_eq and ok_str and ok_bad,
    "equality at kappa_min: %s ; strict at kappa=1: %s ; fails at kappa_min/2: %s" % (ok_eq, ok_str, ok_bad))

# ---------- C2 ----------
aA_over_abad = min(lam*F(1)/(256*c_pr), 6*theta)
kappa_crit   = 256*6*theta*c_pr/lam
rep("C2", aA_over_abad == F(1,4) and kappa_crit == F(1,14045),
    "a_A/a_bad=%s  kappa_crit=%s=%.6e" % (aA_over_abad, kappa_crit, float(kappa_crit)))

# ---------- C3 ----------
CA, x = F(7), F(1,3)
bad = 0
for n in range(1, 21):
    for b1 in (F(0), CA/4, CA/2):
        for b2 in (F(0), CA/4, CA/2):
            if (b1*x + b2*x)**n > (CA*x)**n: bad += 1
rep("C3", bad == 0, "2-branch assembly: %d violations over 20*9 cases" % bad)

# ---------- D1 ----------
dof = 3*n_int*81
logc1 = (dof/2)*math.log(1/(1 - 0.5))
rep("D1", dof == 52488 and 1.8e4 <= logc1 <= 1.85e4 and logc1 <= 1e9,
    "dof=%d  log c_1(Gaussian, lambda_f=1/2)=%.4f" % (dof, logc1))

# ---------- D2 ----------
r = 3.17e-3/6.6e-10
aret_new = 8.03e-7/r
rep("D2", 4.7e6 <= r <= 4.9e6 and 1.6e-13 <= aret_new <= 1.75e-13,
    "lambda_min ratio=%.4e   a_ret/a_bad would become %.4e (from 8.03e-7)" % (r, aret_new))

# ---------- E1 / E1n ----------
bad = 0
for k in range(1, 31):
    for i in range(1, k+1):
        s = sum(3**(k-rr) for rr in range(1, i+1))
        if s != (3**k - 3**(k-i))//2: bad += 1
        if not (s < 3**k): bad += 1
        if not (s <= 3**k//2 + 1): bad += 1   # s <= L^k/(L-1) = 3^k/2
rep("E1", bad == 0, "sum_{r=1..i}3^{k-i} identity and bound: %d violations over k<=30" % bad)
viol = None
for k in range(2, 20):
    for i in range(2, k+1):
        s = sum(2**(k-rr) for rr in range(1, i+1))
        if s >= 2**k/2 and viol is None: viol = (k, i, s, 2**k/2)
rep("E1n", viol is not None, "control at L=2: first violation (k,i,sum,2^k/2)=%s" % (viol,))

# ---------- F1 ----------
vals = [1 + 81 + 256*(D-2) for D in range(2, 11)]
ok = all(v == 82 + 256*(D-2) for v, D in zip(vals, range(2, 11))) and all(vals[i] < vals[i+1] for i in range(len(vals)-1))
rep("F1", ok, "detached-cube ||{y}||_sh for depth K-j=2..10: %s" % vals)

# ---------- F2 ----------
dsh = 81 + F(2401*32*80, 1)*sum(F(1, 3**m) for m in range(1, 200))
rep("F2", dsh == Delta_sh and 256 <= Delta_sh,
    "81 + 2401*32*80*sum 3^-m = %s (recorded Delta_sh=%d); p4 D2b excess 256 <= Delta_sh" % (dsh, Delta_sh))

# ---------- G1 ----------
m_star = math.log(2/eps1)/(2*math.log(L))
price  = 6*(L**4)*a_rec/gK2
rep("G1", 41 <= m_star <= 42 and 4.5e10 <= price <= 5.0e10 and price > m_star*math.log(324),
    "m_star=%.4f  6*L^4*a/g^2=%.4e  m_star*ln324=%.4f" % (m_star, price, m_star*math.log(324)))

print("")
print("SUMMARY: " + ("ALL PASS" if not fails else "FAIL: " + ",".join(fails)))
sys.exit(0)
