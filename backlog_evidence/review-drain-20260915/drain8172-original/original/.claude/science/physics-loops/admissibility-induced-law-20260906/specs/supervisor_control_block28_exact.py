"""Control (exact parts) for block 28: (1) block 08's criterion at (p,1,2): c(p) exactly at rational p; (2) block 12's eroder bound
on random islands (noiseless rule), and the exact region count against 18(D+1)^3; (3) the influence recursion identity."""
from fractions import Fraction as F
from itertools import product
import random
def cond(p, q, r, a, b, c):
    phi = [[r]*6 for _ in range(6)]
    for v in range(6): phi[v][v] = p; phi[v][v ^ 1] = q
    w = [phi[v][a]*phi[v][b]*phi[v][c] for v in range(6)]; Z = sum(w); return [x / Z for x in w]
def c_of(p):
    worst = F(0)
    for a, b, c in product(range(6), repeat=3):
        k1 = cond(p, F(1), F(2), a, b, c)
        for a2 in range(6):
            if a2 == a: continue
            k2 = cond(p, F(1), F(2), a2, b, c)
            worst = max(worst, sum(abs(x - y) for x, y in zip(k1, k2)) / 2)
    return worst
for p in (F(37, 10), F(38, 10)):
    c = c_of(p); print(f"(1) p = {p}: c = {c} = {float(c):.5f}; 3c = {float(3*c):.5f} ({'<' if 3*c < 1 else '>'} 1)")
# (2) eroder bound: noiseless majority from an island at level 0; coordinates x with x1+x2+x3 = 0 represented by (x1, x2)
random.seed(4); ok = True; worst_ratio = 0
def step(ones):
    # ones: set of (x1, x2) at level t; level t+1 sites y = x + e_j have preds y - e_1, y - e_2, y - e_3
    cand = set()
    for (a, b) in ones:
        cand |= {(a+1, b), (a, b+1), (a, b)}   # y = x + e1 -> (a+1, b); x + e2 -> (a, b+1); x + e3 -> (a, b) [x3 absorbs]
    new = set()
    for (a, b) in cand:
        preds = [(a-1, b), (a, b-1), (a, b)]   # y - e1, y - e2, y - e3 in (x1, x2) coordinates
        if sum(1 for q in preds if q in ones) >= 2: new.add((a, b))
    return new
for trial in range(300):
    n = random.randint(1, 12); ones = {(random.randint(-4, 4), random.randint(-4, 4)) for _ in range(n)}
    M1 = max(a for a, b in ones); M2 = max(b for a, b in ones); M3 = max(-a-b for a, b in ones); D = M1 + M2 + M3
    cur = ones; t = 0
    while cur and t <= D + 2:
        cur = step(cur); t += 1
    ok = ok and (not cur) and t <= D + 1
print(f"(2) 300 random islands: all dead within D + 1 levels (D = M1 + M2 + M3): {ok}")
# region count, exact: U = {y : 1 <= tau(y) <= D+1, exists island site i with tau(max(i, y)) <= D+1}; bound 18 (D+1)^3
def region_size(island3):
    M = [max(i[j] for i in island3) for j in range(3)]; D = sum(M); B = 2*D + 1; cnt = 0
    for y1 in range(-3*B - 3, B + 1):
        for y2 in range(-3*B - 3, B + 1):
            for s in range(1, D + 2):
                y = (y1, y2, s - y1 - y2)
                if y[2] > B: continue
                if any(sum(max(i[j], y[j]) for j in range(3)) <= D + 1 for i in island3): cnt += 1
    return cnt, D
ok3 = True; worst = 0
for trial in range(200):
    n = random.randint(1, 10); ones = {(random.randint(-4, 4), random.randint(-4, 4)) for _ in range(n)}
    cnt, D = region_size([(a, b, -a-b) for a, b in ones]); ok3 = ok3 and cnt <= 18 * (D + 1) ** 3; worst = max(worst, cnt / (D + 1) ** 3)
print(f"(2) exact count of the noise-sensitive region U <= 18 (D+1)^3 on 200 random islands: {ok3}; worst |U|/(D+1)^3 = {worst:.3f}")
# (3) influence identity: D_{t+1}(x) = (beta/sqrt3) sum_j D_t(x - e_j) from D_0 = 2 delta gives 2 (beta/sqrt3)^t 3^t p_t(x - x0) = 2 (sqrt3 beta)^t p_t
from math import factorial
def p_t(t, a, b):
    c = t - a - b
    return F(factorial(t), factorial(a)*factorial(b)*factorial(c)) / 3**t if min(a, b, c) >= 0 else F(0)
g = F(1, 5)   # stands for beta/sqrt3 as a rational placeholder
Dt = {(0, 0): F(2)}; okk = True
for t in range(1, 6):
    new = {}
    for (a, b), v in Dt.items():
        for da, db in ((1, 0), (0, 1), (0, 0)):
            new[(a+da, b+db)] = new.get((a+da, b+db), F(0)) + g * v
    Dt = new
    okk = okk and all(v == 2 * (3*g)**t * p_t(t, a, b) for (a, b), v in Dt.items())
print(f"(3) the influence recursion gives exactly 2 (3 g)^t p_t for t <= 5 (g = beta/sqrt3): {okk}")
