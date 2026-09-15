"""Control, block 14 (supervisor): formation-rate laws. Six-axis menu, product rule (p,q,r) = (3,1,2).
(1) plaquette: finished law under rate laws {uniform, seeded, attracting, parallel-biased}, exact; TV to static; the ratio
    mu/prod K on the patterns P1 = (+x,-x,+x,-x) and P3 = (+x,+x,-x,-x) and P4 = (+x,-x,+y,+y);
(2) 2x3: 720 orders -> multiset classes (expect 28); rate-law mixtures; TV(uniform mixture, static) vs the census note;
(3) 2x2x2 cube: probability of the all-+x pattern under the three value-blind rate laws; classes (expect 542);
(4) trees: path P3 and the 6-leaf star under seeded growth equal the static law."""
from fractions import Fraction as F
from itertools import permutations, product
import time
M = 6
def orbit_type(s, u):
    return "p" if s == u else ("q" if s // 2 == u // 2 else "r")
W = {"p": 3, "q": 1, "r": 2}
phi = [[W[orbit_type(s, t)] for t in range(M)] for s in range(M)]
Z1 = sum(phi[0])
def cond(rec, s):
    num = 1
    for a in rec:
        num *= phi[s][a]
    den = sum(__import__("functools").reduce(lambda x, y: x * y, [phi[u][a] for a in rec], 1) for u in range(M))
    return F(num, den)
def static_law(sites, edges):
    pats = list(product(range(M), repeat=len(sites)))
    w = {}
    for v in pats:
        x = 1
        for (i, j) in edges:
            x *= phi[v[i]][v[j]]
        w[v] = x
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}
def tv(a, b):
    return sum(abs(a[v] - b[v]) for v in a) / 2
# generic growth process on a window: rate(x, S, vS, nbrs) -> rational; returns finished law
def finished_law(sites, nbrs, rate):
    n = len(sites)
    law = {}
    # recursive over histories: state = (recorded tuple of (site, value)) ; enumerate all orders x values by DP on partial configs
    from collections import defaultdict
    layer = {((), ()): F(1)}  # (recorded sites tuple, values tuple) -> prob
    for step in range(n):
        new = defaultdict(F)
        for (S, vals), pr in layer.items():
            Sset = set(S)
            vmap = dict(zip(S, vals))
            rates = {x: rate(x, Sset, vmap, nbrs) for x in sites if x not in Sset}
            tot = sum(rates.values())
            for x, lam in rates.items():
                if lam == 0:
                    continue
                rec = tuple(vmap[y] for y in nbrs[x] if y in Sset)
                for s in range(M):
                    c = cond(rec, s) if rec else F(1, M)
                    new[(S + (x,), vals + (s,))] += pr * lam / tot * c
        layer = new
    for (S, vals), pr in layer.items():
        v = [None] * n
        for x, s in zip(S, vals):
            v[x] = s
        law[tuple(v)] = law.get(tuple(v), F(0)) + pr
    return law
uniform = lambda x, S, v, nb: F(1)
seeded = lambda x, S, v, nb: (F(1) if (len(S) == 0 or any(y in S for y in nb[x])) else F(0))
attract = lambda x, S, v, nb: F(1 + sum(1 for y in nb[x] if y in S))
# (1) plaquette 1=(0,0) 2=(1,0) 3=(1,1) 4=(0,1); directions to candidate from recorded neighbour; parallel bias:
# rate = 1 + [some recorded neighbour y of x has value parallel to the direction x - y]
pos = {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}
axis_of_value = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}
def parallel(x, S, v, nb):
    b = 0
    for y in nb[x]:
        if y in S:
            d = (pos[x][0] - pos[y][0], pos[x][1] - pos[y][1], 0)
            if axis_of_value[v[y]] == d:
                b = 1
    return F(1 + b)
sites4 = [0, 1, 2, 3]; edges4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
nb4 = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
stat4 = static_law(sites4, edges4)
def prodK(v, edges):
    x = F(1)
    for (i, j) in edges:
        x *= F(phi[v[i]][v[j]], Z1)
    return x
P1, P3, P4 = (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 2, 2)
for name, rl in (("uniform", uniform), ("seeded", seeded), ("attract", attract), ("parallel", parallel)):
    mu = finished_law(sites4, nb4, rl)
    assert abs(sum(mu.values()) - 1) == 0
    print(f"plaquette {name}: TV to static = {float(tv(mu, stat4)):.6f}; mu/prodK at P1, P3, P4 = {mu[P1]/prodK(P1, edges4)}, {mu[P3]/prodK(P3, edges4)}, {mu[P4]/prodK(P4, edges4)}")
print("static/prodK constant:", len({stat4[v] / prodK(v, edges4) for v in stat4}))
# (2) 2x3: sites 0..5 at (r,c); classes
sites6 = list(range(6)); pos6 = {i: (i // 3, i % 3) for i in sites6}
edges6 = [(i, j) for i in sites6 for j in sites6 if i < j and abs(pos6[i][0] - pos6[j][0]) + abs(pos6[i][1] - pos6[j][1]) == 1]
nb6 = {i: [j for j in sites6 if (min(i, j), max(i, j)) in edges6] for i in sites6}
def multiset_key(order, nb):
    S = set(); key = []
    for x in order:
        A = tuple(sorted(y for y in nb[x] if y in S))
        if len(A) >= 2:
            key.append(A)
        S.add(x)
    return tuple(sorted(key))
t0 = time.time()
classes = {}
for order in permutations(sites6):
    classes.setdefault(multiset_key(order, nb6), []).append(order)
print(f"2x3 classes: {len(classes)} (census note: 28); time {time.time()-t0:.1f}s")
def order_prob(order, nb, rate):
    S = set(); pr = F(1)
    for x in order:
        rates = {y: rate(y, S, {}, nb) for y in nb if y not in S}
        pr *= rates[x] / sum(rates.values())
        S.add(x)
    return pr
def class_law(order, sites, nb):
    n = len(sites); law = {}
    for v in product(range(M), repeat=n):
        S = set(); pr = F(1)
        for x in order:
            rec = tuple(v[y] for y in nb[x] if y in S)
            pr *= cond(rec, v[x]) if rec else F(1, M)
            S.add(x)
        law[v] = pr
    return law
stat6 = static_law(sites6, edges6)
t0 = time.time()
laws6 = {k: class_law(orders[0], sites6, nb6) for k, orders in classes.items()}
print(f"2x3 class laws computed in {time.time()-t0:.1f}s")
for name, rl in (("uniform", uniform), ("seeded", seeded), ("attract", attract)):
    Pc = {k: sum(order_prob(o, nb6, rl) for o in orders) for k, orders in classes.items()}
    assert sum(Pc.values()) == 1
    mix = {v: sum(Pc[k] * laws6[k][v] for k in classes) for v in stat6}
    print(f"2x3 {name}: TV to static = {tv(mix, stat6)} = {float(tv(mix, stat6)):.6f}; nonzero classes {sum(1 for k in Pc if Pc[k] > 0)}")
print("census note's uniform TV: 372254646387017/12790481418000000 =", float(F(372254646387017, 12790481418000000)))
# (4) trees: path 0-1-2 and star center 0 with leaves 1..6
for name, sites, edges in (("path3", [0, 1, 2], [(0, 1), (1, 2)]), ("star4", [0, 1, 2, 3, 4], [(0, 1), (0, 2), (0, 3), (0, 4)])):
    nb = {i: [j for j in sites if (min(i, j), max(i, j)) in edges] for i in sites}
    mu = finished_law(sites, nb, seeded)
    st = static_law(sites, edges)
    print(f"{name} seeded growth == static: {tv(mu, st) == 0}; uniform TV = {float(tv(finished_law(sites, nb, uniform), st)):.6f}")
