# la55_2: rigorous exact-rational check of the BCH plaquette tail (BA-3's coefficient 9). Criteria: la55_2_criteria.md.
from fractions import Fraction as F
from math import factorial
import sys

def exp_encl(x, M=20):
    lo = sum(F(x)**m / factorial(m) for m in range(M + 1))
    up = lo + 2 * F(x)**(M + 1) / factorial(M + 1)
    return lo, up

def f_of(sig, E):
    a = E - 1 - sig - sig**2 / 2
    b = sig * (E - 1 - sig)
    c = (E - 1 - sig)**2 / 2
    u = E - 1
    assert u < 1
    d = u**3 / (3 * (1 - u))
    return a + b + c + d, u

res = []
def rep(name, ok, detail, control=False):
    res.append((name, ok, control)); print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")

sig = F(1, 10); s = F(1, 40)
lo, up = exp_encl(sig)
Fup, uup = f_of(sig, up)
rep("B1", 6*s**2 + Fup <= 9*s**2, f"6s^2+F_up = {6*s**2+Fup} (~{float(6*s**2+Fup):.3e}) vs 9s^2 = {9*s**2}; ratio (6s^2+F_up)/s^2 <= {float((6*s**2+Fup)/s**2):.4f}")
rep("B2", uup < 1, f"u_up = {float(uup):.6f}")

# B3: Taylor coefficients of f up to degree 12
D = 13
def mul(p, q):
    r = [F(0)] * D
    for i, x in enumerate(p):
        if x == 0: continue
        for j, y in enumerate(q):
            if i + j < D: r[i+j] += x * y
    return r
E = [F(1, factorial(m)) for m in range(D)]
sigp = [F(0)] * D; sigp[1] = F(1)
A = E[:]; A[0] -= 1; A[1] -= 1; A[2] -= F(1, 2)
Em1s = E[:]; Em1s[0] -= 1; Em1s[1] -= 1
B = mul(sigp, Em1s)
C = [x / 2 for x in mul(Em1s, Em1s)]
u = E[:]; u[0] -= 1
u3 = mul(mul(u, u), u)
geo = [F(0)] * D; geo[0] = F(1)
term = [F(1)] + [F(0)] * (D - 1)
for t in range(1, D):
    term = mul(term, u)
    geo = [g + x for g, x in zip(geo, term)]
Dd = [x / 3 for x in mul(u3, geo)]
fco = [a + b + c + d for a, b, c, d in zip(A, B, C, Dd)]
rep("B3", all(c >= 0 for c in fco) and fco[0] == fco[1] == fco[2] == 0, f"coeffs deg 3..6 = {[str(c) for c in fco[3:7]]}")

# B4: degree-2 part of log(prod_{i=1}^4 e^{a_i}) in noncommuting letters 0..3
def nmul(p, q, maxdeg=2):
    r = {}
    for w1, c1 in p.items():
        for w2, c2 in q.items():
            w = w1 + w2
            if len(w) <= maxdeg:
                r[w] = r.get(w, F(0)) + c1 * c2
    return {w: c for w, c in r.items() if c != 0}
P = {(): F(1)}
for i in range(4):
    Ei = {(): F(1), (i,): F(1), (i, i): F(1, 2)}
    P = nmul(P, Ei)
Y = {w: c for w, c in P.items() if w != ()}
Y2 = nmul(Y, Y)
logP = dict(Y)
for w, c in Y2.items():
    logP[w] = logP.get(w, F(0)) - c / 2
deg2 = {w: c for w, c in logP.items() if len(w) == 2 and c != 0}
target = {}
for i in range(4):
    for j in range(i + 1, 4):
        target[(i, j)] = target.get((i, j), F(0)) + F(1, 2)
        target[(j, i)] = target.get((j, i), F(0)) - F(1, 2)
deg1 = {w: c for w, c in logP.items() if len(w) == 1}
rep("B4", deg2 == target and deg1 == {(i,): F(1) for i in range(4)}, f"deg-2 part has {len(deg2)} words; equals (1/2)sum_(i<j)[a_i,a_j]")

# CONTROL-1: must FAIL
lo2, up2 = exp_encl(F(1, 5))
Flo2, _ = f_of(F(1, 5), lo2)
rep("CONTROL-1", Flo2 <= 3 * F(1, 20)**2, f"F_lo(1/5) = {float(Flo2):.6e} vs 3/400 = 0.0075 (designed to FAIL)", control=True)
# information: lower value of the bound's coefficient at s = 1/40
Flo, _ = f_of(sig, lo)
print(f"INFO: bound coefficient at s=1/40 lies in [{float((6*s**2+Flo)/s**2):.4f}, {float((6*s**2+Fup)/s**2):.4f}] (true |q_p|/s^2 may be smaller)")
bad = [n for n, ok, c in res if not c and not ok]
fired = any(c and not ok for n, ok, c in res)
print("SUMMARY: non-control FAILs =", bad, "| control fired =", fired)
sys.exit(0 if not bad and fired else 1)
