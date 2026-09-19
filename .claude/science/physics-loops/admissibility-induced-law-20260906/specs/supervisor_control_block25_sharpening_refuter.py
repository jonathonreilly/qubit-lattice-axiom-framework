"""Refuting pass, block 25 sharpening: independent machinery against the sharpened count and bound.
(a) The recursion iterated in floating point from (1,1,1) at (t, s): its fixed point against the exact certificate; at s scaled by 1.06 the
iteration diverges (the certificate sits near the edge of the domain for this accounting).  (b) The crude alternative — the binomial split
sum_{a<=3f} C(a+f,a) 24^{a+f} <= (24/23)(96^4/27)^f, threshold 1/6291456 — as a second valid bound, weaker than the recursion's.
(c) The Peierls partial sum over the enumerated trees of G in the family (forks = n-1, arrows <= 3(n-1), marks read off) at eps_0,
against eps_0 R-bar.  (d) An independent recount of the up-arrows (BFS from the root, different code) on the exhaustive depth-2 cone and
the depth-3 cases with <= 4 noise sites.  (e) Simulation of the automaton at eps = 7e-6 on a 300 x 300 torus for 400 levels: the
density of ones against the bound 3e-5."""
import sys, os, random
from fractions import Fraction as F
from math import comb
from collections import deque, defaultdict
from itertools import product, combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block25_toom_core as core
x = (0, 0, 0)
tf, sf = 0.091, 1000 / 107653
def iterate(tt, ss, nit=6000):
    D = U = Fv = 1.0
    for i in range(nit):
        D2 = (1 + tt * U) ** 2 * (1 + 3 * tt * D) * (1 + ss * Fv) ** 6; U2 = (1 + tt * U) ** 3 * (1 + ss * Fv) ** 6; F2 = (1 + tt * U) ** 3 * (1 + 3 * tt * D) * (1 + ss * Fv) ** 5
        if max(D2, U2, F2) > 1e9: return None
        D, U, Fv = D2, U2, F2
    return D, U, Fv
fp = iterate(tf, sf)
print(f"(a) float fixed point at (t, s): {[round(v, 6) for v in fp]}; certificate (3.290958, 2.058190, 3.774966) lies above it: {fp[0] < 3.290958 and fp[1] < 2.058190 and fp[2] < 3.774966}")
print(f"(a) at s * 1.06 the iteration diverges: {iterate(tf, sf * 1.06) is None}; at s * 1.03: {'diverges' if iterate(tf, sf * 1.03) is None else 'still bounded'}")
# (b)
okb = all(sum(comb(a + f, a) * 24 ** (a + f) for a in range(3 * f + 1)) <= F(24, 23) * (96 ** 4 // 27) ** f for f in range(0, 12)) and 96 ** 4 % 27 == 0
print(f"(b) binomial-split bound sum_{{a<=3f}} C(a+f,a) 24^(a+f) <= (24/23) 3145728^f for f <= 11: {okb}; its threshold 1/(2 3145728) = {1/6291456:.3e} < 7e-6 (the recursion wins by {7e-6*6291456:.1f})")
# (c)
TYPES = [("down", j) for j in range(3)] + [("up", j) for j in range(3)] + [("fork", (i, j)) for i in range(3) for j in range(3) if i != j]
def step(v, ty):
    kind, d = ty
    if kind == "down": return core.sub(v, core.E[d])
    if kind == "up": return core.add(v, core.E[d])
    return core.add(core.sub(v, core.E[d[1]]), core.E[d[0]])
trees = {frozenset()}; fam = 0; peierls = F(0); eps0 = F(7, 10 ** 6)
for k in range(4):
    nxt = set()
    for T in trees:
        nodes = {x} | {c for (_p, c, _t) in T}; downs = defaultdict(int)
        for (p, c, ty) in T:
            if ty[0] == "down": downs[p] += 1
            if ty[0] == "up": downs[c] += 1
        for v in nodes:
            for ty in TYPES:
                w = step(v, ty)
                if w in nodes or (ty[0] == "down" and downs[v] >= 1): continue
                nxt.add(T | {(v, w, ty)})
    trees = nxt
    for T in trees:
        nodes = {x} | {c for (_p, c, _t) in T}; downs = defaultdict(int)
        for (p, c, ty) in T:
            if ty[0] == "down": downs[p] += 1
            if ty[0] == "up": downs[c] += 1
        n = sum(1 for v in nodes if downs[v] == 0); a = sum(1 for e in T if e[2][0] != "fork"); f = len(T) - a
        if f == n - 1 and a <= 3 * (n - 1): fam += 1; peierls += eps0 ** n
Rbar = F(391, 100)
print(f"(c) trees of G with 1-4 edges in the family (forks = n-1, arrows <= 3(n-1)): {fam}; their Peierls sum at eps_0: {float(peierls):.4e} <= eps_0 R-bar = {float(eps0 * Rbar):.4e}: {peierls <= eps0 * Rbar}")
# (d)
def up_arrows(nodes, edges, root):
    adj = defaultdict(list)
    for e, kind in edges.items():
        a, b = tuple(e); adj[a].append((b, kind)); adj[b].append((a, kind))
    dist = {root: 0}; dq = deque([root]); ups = 0
    while dq:
        v = dq.popleft()
        for w, kind in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1; dq.append(w)
                if kind == "arrow" and core.level(w) > core.level(v): ups += 1
    return ups
sites2 = core.cone(x, 2); sites3 = core.cone(x, 3)
configs = [{z: b for z, b in zip(sites2, bits) if b} for bits in product((0, 1), repeat=len(sites2))]
for k in range(1, 5):
    for combo in combinations(sites3, k): configs.append({z: 1 for z in combo})
cases = 0; with_up = 0
for zeta in configs:
    depth = max(-core.level(z) for z in zeta) if zeta else 0
    sites = core.cone(x, max(depth, 1)); eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta); nodes, edges, nn, refs = ex.explain(x)
    cases += 1; with_up += (up_arrows(nodes, edges, x) > 0)
print(f"(d) independent recount: {with_up} of {cases} exhaustive trees (depth-2 cone and depth-3 with <= 4 noise sites) contain an arrow traversed upward from the root")
# (e)
random.seed(5); L = 300; T = 400; eps = 7e-6
prev = [[0] * L for _ in range(L)]; dens = []
for tlev in range(T):
    cur = [[0] * L for _ in range(L)]
    for i in range(L):
        pi = prev[i]; pim = prev[i - 1]
        for j in range(L):
            m = pi[j] + pim[j] + pi[j - 1]
            cur[i][j] = 1 if (m >= 2 or random.random() < eps) else 0
    prev = cur
    if tlev >= T // 2: dens.append(sum(map(sum, cur)) / (L * L))
print(f"(e) simulation at eps = 7e-6, {L}x{L} torus, levels {T//2}-{T}: mean density of ones {sum(dens)/len(dens):.3e} (bound 3e-5; noise alone 7e-6)")
