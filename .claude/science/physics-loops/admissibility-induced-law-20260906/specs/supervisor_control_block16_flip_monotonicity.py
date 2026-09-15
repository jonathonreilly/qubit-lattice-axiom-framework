"""Control, block 16 (supervisor): the flip monotonicity behind 'no mixture over orders is the static law'.
Six-axis menu, (p,q,r) = (3,1,2). For an order sigma, w_sigma(v) = mu_sigma(v)/prod_edges K(v) = M^{-n0} prod_x 1/K_{|A_x|}(v_{A_x}).
Claim: with v = all b and v'_z = the flip of site z to -b, w_sigma(v') >= w_sigma(v), strict iff z lies in some A_x with |A_x| >= 2.
(1) plaquette (24 orders), 2x3 (720 orders), cube (40320 orders): check per order and per z, exactly;
(2) forest iff on the path P3 and the 4-leaf star: uniform mixture over 'good' orders = static; mixing in any bad order breaks it;
(3) the plaquette's value-dependent parallel law: the flip inequality can fail for P(sigma|v) (recorded)."""
from fractions import Fraction as F
from functools import reduce
from itertools import permutations, product
import random, time
M = 6
def orbit_type(s, u):
    return "p" if s == u else ("q" if s // 2 == u // 2 else "r")
W = {"p": 3, "q": 1, "r": 2}
phi = [[W[orbit_type(s, t)] for t in range(M)] for s in range(M)]
Z1 = sum(phi[0])
def Kk(vals):
    return sum(reduce(lambda a, b: a * b, [F(phi[s][a], Z1) for a in vals], F(1)) for s in range(M)) if vals else F(1)
def window(pos):
    sites = sorted(pos)
    edges = [(i, j) for i in sites for j in sites if i < j and sum(abs(pos[i][k] - pos[j][k]) for k in range(3)) == 1]
    nb = {i: [j for j in sites if (min(i, j), max(i, j)) in edges] for i in sites}
    return sites, edges, nb
def w_of(order, nb, v):
    S = set(); w = F(1)
    for x in order:
        A = [v[y] for y in nb[x] if y in S]
        if not A:
            w /= M
        else:
            w /= Kk(tuple(A))
        S.add(x)
    return w
def bad_sites(order, nb):
    S = set(); bad = set()
    for x in order:
        A = [y for y in nb[x] if y in S]
        if len(A) >= 2:
            bad |= set(A)
        S.add(x)
    return bad
windows = {"plaquette": {0: (0,0,0), 1: (1,0,0), 2: (1,1,0), 3: (0,1,0)}, "2x3": {i: (i // 3, i % 3, 0) for i in range(6)}, "cube": {i: (i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)}}
for name, pos in windows.items():
    sites, edges, nb = window(pos); n = len(sites)
    t0 = time.time(); ok = True; strict_count = 0; total = 0
    for order in permutations(sites):
        v = tuple([0] * n)
        w0 = w_of(order, nb, v)
        bad = bad_sites(order, nb)
        for z in sites:
            v2 = list(v); v2[z] = 1; w1 = w_of(order, nb, tuple(v2))
            total += 1
            if w1 > w0: strict_count += 1
            ok = ok and (w1 >= w0) and ((w1 > w0) == (z in bad))
    print(f"{name}: flip monotonicity and strictness-iff hold on all {total} (order, site) pairs: {ok}; strict in {strict_count}; time {time.time()-t0:.1f}s")
# (2) forest iff
def static_law(sites, edges):
    w = {}
    for v in product(range(M), repeat=len(sites)):
        x = 1
        for (i, j) in edges: x *= phi[v[i]][v[j]]
        w[v] = x
    Z = sum(w.values()); return {v: F(x, Z) for v, x in w.items()}
def seq_law(order, nb, sites):
    law = {}
    for v in product(range(M), repeat=len(sites)):
        S = set(); pr = F(1)
        for x in order:
            A = tuple(v[y] for y in nb[x] if y in S)
            num = reduce(lambda a, b: a * b, [phi[v[x]][a] for a in A], 1) if A else 1
            den = sum(reduce(lambda a, b: a * b, [phi[u][a] for a in A], 1) for u in range(M)) if A else M
            pr *= F(num, den); S.add(x)
        law[v] = pr
    return law
def tv(a, b): return sum(abs(a[v] - b[v]) for v in a) / 2
for name, pos in (("path3", {0: (0,0,0), 1: (1,0,0), 2: (2,0,0)}), ("star4", {0: (0,0,0), 1: (1,0,0), 2: (-1,0,0), 3: (0,1,0), 4: (0,-1,0)})):
    sites, edges, nb = window(pos); st = static_law(sites, edges)
    orders = list(permutations(sites)); good = [o for o in orders if not bad_sites(o, nb)]; badl = [o for o in orders if bad_sites(o, nb)]
    laws = {o: seq_law(o, nb, sites) for o in orders}
    mix_good = {v: sum(laws[o][v] for o in good) / len(good) for v in st}
    random.seed(1)
    res = []
    for _ in range(3):
        wts = {o: F(random.randint(1, 9)) for o in orders}
        tot = sum(wts.values())
        mix = {v: sum(wts[o] * laws[o][v] for o in orders) / tot for v in st}
        res.append(tv(mix, st) > 0)
    print(f"{name}: {len(good)} good / {len(badl)} bad orders; uniform mixture over good = static: {tv(mix_good, st) == 0}; three random full mixtures differ: {res}")
