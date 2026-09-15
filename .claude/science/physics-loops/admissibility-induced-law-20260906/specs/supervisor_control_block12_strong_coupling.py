"""Supervisor control, block 12: the strong-coupling side of the three-dimensional formation law.  Exact arithmetic.
(1) the noise map: the kernel r(.|a,b,c) at large p — the probability of the majority value for the triple patterns
    (a,a,a), (a,a,b perp), (a,a,-a), and the tie pattern (a,b,c distinct axes), as exact rationals and as functions of p;
(2) the deterministic limit is a majority eroder on the level lattice: simulate the majority rule on levels from finite
    islands and compare the death time with the bound M_1 + M_2 + M_3 - t_0 + 1 (exact integers);
(3) finite cross-section slowdown: the 2x2 orbit quotient's TV contraction after n steps at p = 3, 10, 30, 100 (q = 1, r = 2);
(4) two dimensions: the row flip probability 1 - p/Z_1 and the row correlation eigenvalue (p - q)/Z_1 at the same p.
"""
from fractions import Fraction as F
from itertools import product, combinations
import sys, time, random
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
r08 = importlib.import_module("admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15")
M = 6
def dec(x, n=8):
    s = x.numerator * 10**n // x.denominator; return f"{s // 10**n}.{str(s % 10**n).zfill(n)}"

print("=== (1) the noise map at (p, 1, 2): P(majority) for the triple patterns; deviation = 1 - P(majority)")
x, mx, y, z = 0, 1, 2, 4
for p in (3, 10, 30, 100, 1000):
    rule = r08.Rule((p, 1, 2))
    c_aaa = rule.cond((x, x, x))[x]
    c_aab = rule.cond((x, x, y))[x]
    c_aam = rule.cond((x, x, mx))[x]
    tie = rule.cond((x, y, z))
    print(f"p={p}: P(a|a,a,a)={dec(c_aaa)} dev={dec(1-c_aaa)}; P(a|a,a,b⊥)={dec(c_aab)} dev={dec(1-c_aab)}; P(a|a,a,-a)={dec(c_aam)} dev={dec(1-c_aam)}; tie (a,b,c): P(a)=P(b)=P(c)={dec(tie[x])}, P(-a)={dec(tie[mx])}")
# closed forms
import sympy as sp
P, Q, R_ = sp.symbols('p q r', positive=True)
Z1 = P + Q + 4*R_
print("closed forms: P(a|a,a,a) = p^3/(p^3+q^3+4r^3); P(a|a,a,b⊥) = p^2 r/(r(p^2+q^2)+r^2(p+q)+2r^3); P(a|a,a,-a) = p^2 q/(pq(p+q)+4r^3); tie P(a) = p r^2/(3 r^2 (p+q)) = p/(3(p+q))")
# verify the closed forms against the definition symbolically
def orbit(s, u): return 'p' if s == u else ('q' if s//2 == u//2 else 'r')
w = {'p': P, 'q': Q, 'r': R_}
def cond_sym(rec, s):
    num = sp.prod([w[orbit(s, a)] for a in rec]); den = sum(sp.prod([w[orbit(u, a)] for a in rec]) for u in range(M)); return sp.simplify(num/den)
print("   verified:", sp.simplify(cond_sym((x,x,x), x) - P**3/(P**3+Q**3+4*R_**3)) == 0, sp.simplify(cond_sym((x,x,y), x) - P**2*R_/(R_*(P**2+Q**2)+R_**2*(P+Q)+2*R_**3)) == 0, sp.simplify(cond_sym((x,x,mx), x) - P**2*Q/(P*Q*(P+Q)+4*R_**3)) == 0, sp.simplify(cond_sym((x,y,z), x) - P/(3*(P+Q))) == 0)
print()
print("=== (2) the deterministic majority rule on levels is an eroder: death time vs the bound M1+M2+M3 - t0 + 1")
def evolve_majority(island):
    """island: set of sites (x1,x2,x3) with a common level t0; evolve the binary majority rule (1 iff >= 2 of the three
    predecessors x-e_i are 1) level by level until empty; return the number of levels until empty."""
    cur = set(island); t = 0
    while cur:
        # candidates at the next level: successors of current 1s
        cand = set()
        for (a, b, c) in cur:
            cand |= {(a+1, b, c), (a, b+1, c), (a, b, c+1)}
        nxt = set()
        for (a, b, c) in cand:
            n1 = ((a-1, b, c) in cur) + ((a, b-1, c) in cur) + ((a, b, c-1) in cur)
            if n1 >= 2: nxt.add((a, b, c))
        cur = nxt; t += 1
        if t > 10**5: return None
    return t
random.seed(20260915)
worst = 0
for trial in range(300):
    t0 = random.randint(3, 12)
    # random island on level t0: choose sites with nonnegative coords summing to t0
    pts = [(a, b, t0-a-b) for a in range(t0+1) for b in range(t0+1-a)]
    k = random.randint(1, min(12, len(pts)))
    isl = set(random.sample(pts, k))
    T = evolve_majority(isl)
    M1 = max(s[0] for s in isl); M2 = max(s[1] for s in isl); M3 = max(s[2] for s in isl)
    bound = M1 + M2 + M3 - t0 + 1
    assert T is not None and T <= bound, (isl, T, bound)
    worst = max(worst, T)
print(f"   300 random islands (up to 12 sites, levels 3..12): every island dies; max death time {worst}; bound M1+M2+M3-t0+1 always holds")
# a "row" island: a line of L ones along e2 at level t0: dies in 1 step? and a triangle: dies slowly
line = {(0, b, 10-b) for b in range(0, 6)}
print(f"   line of 6 ones on level 10: death time {evolve_majority(line)}; bound {0+5+10-10+1}")
tri = {(a, b, 12-a-b) for a in range(5) for b in range(5-a)}  # a filled triangle
print(f"   filled triangle of 15 ones on level 12: death time {evolve_majority(tri)}; bound {4+4+12-12+1}")
print()
print("=== (3) the 2x2 orbit quotient at (p,1,2): TV contraction after n steps (max over row pairs), n = 1, 2, 4, 8")
for p in (3, 10, 30, 100):
    t0 = time.time()
    rule = r08.Rule((p, 1, 2))
    states, orbit_of, reps, sizes = r08.orbits_2x2()
    n = len(reps)
    Q = [[F(0)] * n for _ in range(n)]
    for o, wv in enumerate(reps):
        for v in states:
            Q[o][orbit_of[v]] += r08.plane_transfer(rule, wv, v)
    Qn = [row[:] for row in Q]; out = []
    step = 1
    for k in range(1, 9):
        if k in (1, 2, 4, 8):
            d = max(sum(abs(Qn[o1][o] - Qn[o2][o]) for o in range(n)) / 2 for o1 in range(n) for o2 in range(n))
            out.append((k, dec(d, 6)))
        Qn = [[sum(Qn[i][kk] * Q[kk][j] for kk in range(n)) for j in range(n)] for i in range(n)]
    print(f"   p={p}: {out}  ({time.time()-t0:.1f}s)")
print()
print("=== (4) two dimensions at (p,1,2): row flip probability 1 - p/Z1 and the row correlation eigenvalue (p-q)/Z1")
for p in (3, 10, 30, 100, 1000):
    Z = p + 1 + 8
    print(f"   p={p}: flip prob {dec(F(Z-p, Z))}, eigenvalue {dec(F(p-1, Z))} (< 1 for every finite p: no long-range order along rows)")
