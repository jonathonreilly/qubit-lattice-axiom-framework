# la55_1: exact-arithmetic checks of constants re-derived in LANEA55. Criteria: la55_1_criteria.md (written first).
from fractions import Fraction as F
import sys
results = []
def rep(name, ok, detail, control=False):
    results.append((name, ok, control))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")

r87 = F(8, 7) ** 5
v1 = 4 * 3 * 80 * 2 * r87
rep("C1", v1 < 3744 and v1 < 10**4, f"4*3*80*2*(8/7)^5 = {v1} = {v1.numerator}/{v1.denominator}")
v2 = 2592 * r87
rep("C2", v2 < 5054 and v2 < 10**4, f"2592*(8/7)^5 = {v2}")
ok3 = True
for t in range(1, 2001):
    lhs = (2*t+1)**4 - (2*t-1)**4
    if lhs != 64*t**3 + 16*t or lhs > 80*t**3:
        ok3 = False; break
# polynomial identity: (2t+1)^4-(2t-1)^4 = 2*(4*(2t)^3*1 + 4*(2t)*1) = 64t^3+16t
coeffs_ok = (2*4*8 == 64) and (2*4*2 == 16)
rep("C3", ok3 and coeffs_ok, "shell identity and <= 80t^3 for t<=2000; coefficient identity")
N = 10**5
partial = [F(0)] * 1
# cumulative tail sums: S(n) = sum_{t=n}^{N} 1/t^2 + 1/(N-1)  (rigorous bound for the tail beyond N: sum_{t>N} 1/t^2 <= 1/N <= 1/(N-1))
s = F(0)
tails = {}
for t in range(N, 0, -1):
    s += F(1, t*t)
    if t <= 200:
        tails[t] = s + F(1, N - 1)
ok4 = all(tails[n] <= F(2, n) for n in range(1, 201))
rep("C4", ok4, f"tail bound at n=1: {float(tails[1]):.6f} vs 2 (display only); n=200: {float(tails[200]*200):.6f}*(1/200)")
v5 = 48 * F(41, 20) ** 5
rep("C5", v5 <= 1738 and 1738 * 2 == 3476, f"48*(41/20)^5 = {v5}")
ok6 = (3 + 72 == 75) and (75 + 8*10 == 155) and (8*5 == 40) and (5*155 == 775) and (5*8 == 40) and (5*40 + 5 == 205) and (775 + 205*F(3, 2) <= 1083)
rep("C6", ok6, f"775 + 205*3/2 = {775 + 205*F(3,2)}")
ok7 = True
for L in (3, 5, 7, 9):
    for k in range(1, 13):
        lhs = 10 * L * (L-1) * sum(L**(k-1-i) * L**(2*i) for i in range(k))
        if lhs > 10 * L**(2*k):
            ok7 = False
rep("C7", ok7, "Lemma Lambda telescoping sum <= 10 n^2")
ctrl = (v5 <= 1737)
rep("CONTROL", ctrl, "designed to FAIL: 48*(41/20)^5 <= 1737", control=True)
bad = [n for (n, ok, c) in results if not c and not ok]
ctrl_fired = any((c and not ok) for (n, ok, c) in results)
print("SUMMARY:", "non-control FAILs =", bad, "| control fired (FAILed as designed) =", ctrl_fired)
sys.exit(0 if (not bad and ctrl_fired) else 1)
