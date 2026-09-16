"""Refuting pass, block 25 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the spanning lemma on random ABSTRACT instances independent of the automaton: random points of one level plane partitioned into
     random clusters, random forks between clusters (sibling pairs across clusters), random poles; the bipartite cause graph made connected;
     the runner's pole rule re-implemented from scratch here and the identity sum_X Span(X) = sum_k M_k(u_k) checked with Fractions;
(R2) the noise map against direct floating-point enumeration of the rule's conditional at random positive weights (not integers);
(R3) the explanation tree's checks with an independent graph implementation (numpy arrays for predecessor/sibling tests) on random cones;
(R4) the series constant by direct summation of sum_{k<=K} 2 96^k / 96^K for K up to 40 in floats and the closed-form bound at epsilon_0;
(R5) stability far above the rigorous threshold: the noisy automaton simulated on a periodic 96x96 level plane from all-zero for 300 levels at
     epsilon in {0.01, 0.02, 0.03, 0.05, 0.08}, reporting the final density of ones and its maximum over levels (a physics sanity check only:
     the rigorous threshold is 5.9e-9; the true one is known to be near 0.05 by simulation in the literature)."""
import math
import random
import sys, os
from collections import deque
from fractions import Fraction as F
from itertools import combinations, product

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
core = importlib.import_module("supervisor_control_block25_toom_core")

random.seed(255); np.random.seed(255)
E3 = core.E; FORK_OFFSETS = core.FORK_OFFSETS
# ---- R1: abstract spanning-lemma instances ----
def Mk(k, z):
    return F(z[k]) - F(sum(z), 3)
ok1 = True; tested = 0
for trial in range(300):
    # points of the level plane tau = 0: z = (a, b, -a-b)
    pts = list({(a, b, -a - b) for a in range(-4, 5) for b in range(-4, 5)})
    random.shuffle(pts)
    npts = random.randint(6, 20)
    pts = pts[:npts]
    ncl = random.randint(2, min(6, npts))
    # random partition into clusters
    labels = [random.randrange(ncl) for _ in pts]
    clusters = {}
    for z, l in zip(pts, labels):
        clusters.setdefault(l, set()).add(z)
    clusters = [frozenset(c) for c in clusters.values()]
    if len(clusters) < 2:
        continue
    cl_of = {z: c for c in clusters for z in c}
    # forks: sibling pairs across clusters
    forks = set()
    for z in pts:
        for off in FORK_OFFSETS:
            w = core.add(z, off)
            if w in cl_of and cl_of[w] != cl_of[z]:
                forks.add(frozenset([z, w]))
    forks = list(forks)
    # bipartite graph must be connected: check
    fam = [("cluster", c) for c in clusters] + [("fork", f) for f in forks]
    n = len(fam)
    adj = {i: set() for i in range(n)}
    for i, j in combinations(range(n), 2):
        if fam[i][0] != fam[j][0] and (fam[i][1] & fam[j][1]):
            adj[i].add(j); adj[j].add(i)
    seen = {0}; dq = deque([0])
    while dq:
        a = dq.popleft()
        for b in adj[a]:
            if b not in seen:
                seen.add(b); dq.append(b)
    if len(seen) != n:
        continue
    poles_u = [random.choice(pts) for _ in range(3)]
    # independent implementation of the lemma's construction
    term = [next(i for i in range(n) if fam[i][0] == "cluster" and poles_u[j] in fam[i][1]) for j in range(3)]
    def path(src, dsts):
        prev = {src: None}; dq = deque([src])
        while dq:
            a = dq.popleft()
            if a in dsts:
                out = []
                while a is not None:
                    out.append(a); a = prev[a]
                return out[::-1]
            for b in adj[a]:
                if b not in prev:
                    prev[b] = a; dq.append(b)
    p12 = path(term[0], {term[1]}); tn = set(p12); p3 = path(term[2], tn); tn |= set(p3)
    te = set()
    for pth in (p12, p3):
        for a, b in zip(pth, pth[1:]):
            te.add(frozenset([a, b]))
    ch = True
    while ch:
        ch = False
        for i in list(tn):
            if sum(1 for e in te if i in e) <= 1 and i not in term:
                tn.discard(i); te = {e for e in te if i not in e}; ch = True
    nb = {i: set() for i in tn}
    for e in te:
        a, b = tuple(e); nb[a].add(b); nb[b].add(a)
    def meet(i, j):
        c = fam[i][1] & fam[j][1]; assert len(c) == 1; return next(iter(c))
    def toward(i, target):
        if i == target: return None
        prev = {i: None}; dq = deque([i])
        while dq:
            a = dq.popleft()
            if a == target:
                b = a
                while prev[b] != i: b = prev[b]
                return b
            for b in nb[a]:
                if b not in prev: prev[b] = a; dq.append(b)
    total = F(0)
    for i in tn:
        red = {poles_u[j] for j in range(3) if term[j] == i} | {meet(i, x) for x in nb[i]}
        for k in range(3):
            if poles_u[k] in red:
                pole = poles_u[k]
            else:
                pole = meet(i, toward(i, term[k]))
            total += Mk(k, pole)
    ok1 = ok1 and total == sum(Mk(k, poles_u[k]) for k in range(3))
    tested += 1
print(f"R1 spanning lemma on {tested} random abstract cluster/fork systems (independent implementation): identity holds in all: {ok1}")
# ---- R2: noise map vs direct float enumeration ----
MENU = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def phi(v, w, p, q, r):
    if v == w: return p
    if tuple(-c for c in v) == w: return q
    return r
ok2 = True; worst = 0.0
for trial in range(200):
    p, q, r = random.uniform(1, 50), random.uniform(0.1, 3), random.uniform(0.1, 3)
    a = (1, 0, 0); m = 0.0
    for triple in product(MENU, repeat=3):
        if sum(1 for w in triple if w == a) >= 2:
            num = 1.0
            for w in triple: num *= phi(a, w, p, q, r)
            den = sum(math.prod(phi(v, w, p, q, r) for w in triple) for v in MENU)
            m = max(m, 1 - num / den)
    d1 = 1 - p**3/(p**3 + q**3 + 4*r**3); d2 = 1 - p**2*q/(p*q*(p+q) + 4*r**3); d3 = 1 - p**2*r/(r*(p**2+q**2) + r**2*(p+q) + 2*r**3)
    ok2 = ok2 and abs(m - max(d1, d2, d3)) < 1e-12
    worst = max(worst, abs(m - max(d1, d2, d3)))
print(f"R2 noise map = max of the three closed-form deviations at 200 random real weights (max discrepancy {worst:.1e}): {ok2}")
# ---- R3: tree checks with an independent graph implementation on random cones ----
def preds_np(z): return [tuple(np.array(z) - np.array(e)) for e in E3]
def is_fork_np(u, v):
    d = np.array(u) - np.array(v)
    return int(np.abs(d).sum()) == 2 and int(d.sum()) == 0 and int((d == 0).sum()) == 1
x = (0, 0, 0); ok3 = True; cases = 0
for trial in range(400):
    depth = random.randint(3, 7); sites = core.cone(x, depth)
    zeta = {z: 1 for z in sites if random.random() < random.choice((0.15, 0.3, 0.5))}
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta)
    nodes, edges, nn, refs = ex.explain(x)
    for e, kind in edges.items():
        a, b = tuple(e)
        ok3 = ok3 and ((b in preds_np(a) or a in preds_np(b)) if kind == "arrow" else is_fork_np(a, b))
        ok3 = ok3 and eta[a] == 1 and eta[b] == 1
    ok3 = ok3 and all(zeta.get(z, 0) == 1 and sum(eta.get(p, 0) for p in preds_np(z)) < 2 for z in nn)
    ok3 = ok3 and len(edges) == len(nodes) - 1 and len(edges) <= 4 * (len(nn) - 1)
    cases += 1
print(f"R3 independent graph checks (numpy predecessors/siblings) on {cases} explained random cones: {ok3}")
# ---- R4: series constant and bound ----
ratios = [sum(2 * 96.0**k for k in range(K + 1)) / 96.0**K for K in range(0, 41)]
eps0 = 1 / (2 * 96**4)
print(f"R4 max_K sum_{{k<=K}} 2 96^k / 96^K = {max(ratios):.9f} (192/95 = {192/95:.9f}); bound at eps0 = {192/95*eps0/(1-96**4*eps0):.6e} = 1/42024960 = {1/42024960:.6e}")
# ---- R5: simulation far above the rigorous threshold ----
L = 96
for eps in (0.01, 0.02, 0.03, 0.05, 0.08):
    rng = np.random.default_rng(7)
    eta = np.zeros((L, L), dtype=np.int8)
    dens_max = 0.0
    for t in range(300):
        center = eta; west = np.roll(eta, 1, axis=0); south = np.roll(eta, 1, axis=1)
        maj = ((center + west + south) >= 2).astype(np.int8)
        noise = (rng.random((L, L)) < eps).astype(np.int8)
        eta = np.maximum(maj, noise)
        dens_max = max(dens_max, float(eta.mean()))
    print(f"R5 simulation eps={eps}: final density {float(eta.mean()):.4f}, max density over 300 levels {dens_max:.4f}")
