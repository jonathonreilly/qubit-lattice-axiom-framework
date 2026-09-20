"""Refuting pass, block 38 (machinery disjoint from the runner's exact recursions):
 (a) Z of the 2x3 rectangle by brute enumeration of all 6^6 patterns (the runner eliminates sites), against D_sigma for all 720 orders;
 (b) a linear program: is the static law of the plaquette a mixture of the 24 value-blind order laws?  (scipy linprog; infeasible expected)
 (c) Monte Carlo of an adversarial ADAPTED scheme on the plaquette that tries to favour constant patterns (always form next the site
     whose recorded neighbours agree most), against the static weight of the constant patterns;
 (d) causal structure: Monte Carlo of a value-dependent readiness-gated scheme on the diamond against the product of kernels.
usage: refuter.py samples seed"""
import sys, itertools, numpy as np
from fractions import Fraction
from scipy.optimize import linprog
samples = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
p, q, r = 3.0, 1.0, 2.0
W = np.array([[p if a == b else q if a == (b ^ 1) else r for b in range(6)] for a in range(6)])
def Nk(k): return 6.0 if k == 0 else p**k + q**k + 4 * r**k
# (a)
sites = list(range(6)); edges = [(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]; nb = {x: [] for x in sites}
for a, b in edges: nb[a].append(b); nb[b].append(a)
Z = 0.0
for pat in itertools.product(range(6), repeat=6):
    w = 1.0
    for a, b in edges: w *= W[pat[a], pat[b]]
    Z += w
worst = min(np.prod([Nk(sum(1 for y in nb[x] if y in order[:i])) for i, x in enumerate(order)]) for order in itertools.permutations(sites))
print(f"(a) rectangle 2x3 at (3,1,2): Z by enumeration = {Z:.0f}; least D_sigma over 720 orders = {worst:.0f}; Z < D: {Z < worst}")
# (b)
ps = [0, 1, 2, 3]; pe = [(0,1),(1,2),(2,3),(3,0)]; pn = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
pats = list(itertools.product(range(6), repeat=4))
stat = np.array([np.prod([W[v[a], v[b]] for a, b in pe]) for v in pats]); stat /= stat.sum()
cols = []
for order in itertools.permutations(ps):
    col = []
    for v in pats:
        w = 1.0; formed = []
        for x in order:
            ws = np.array([np.prod([W[a, v[y]] for y in pn[x] if y in formed]) for a in range(6)]); w *= ws[v[x]] / ws.sum(); formed.append(x)
        col.append(w)
    cols.append(col)
A = np.array(cols).T
res = linprog(np.zeros(A.shape[1]), A_eq=np.vstack([A, np.ones(A.shape[1])]), b_eq=np.append(stat, 1.0), bounds=(0, None), method="highs")
print(f"(b) plaquette: static law as a mixture of the 24 value-blind order laws: linear program status {res.status} ({'infeasible' if res.status == 2 else res.message})")
# (c) adversarial adapted scheme on the plaquette
const = 0
for _ in range(samples):
    rec = {}
    while len(rec) < 4:
        cand = [x for x in ps if x not in rec]
        def score(x):
            vals = [rec[y] for y in pn[x] if y in rec]; return (len(vals) >= 2 and len(set(vals)) == 1, -len(vals))
        x = max(cand, key=lambda x: (score(x), rng.random()))
        ws = np.array([np.prod([W[a, rec[y]] for y in pn[x] if y in rec]) for a in range(6)]); rec[x] = rng.choice(6, p=ws / ws.sum())
    const += len(set(rec.values())) == 1
static_const = 6 * p**4 / 20784.0
print(f"(c) adversarial adapted scheme on the plaquette, {samples} runs: P(constant pattern) = {const/samples:.5f} +- {np.sqrt(const)/samples:.5f}; static law: {static_const:.5f}; bound 6 p^4/D_min = {6*p**4/22464:.5f}")
# (d) diamond, value-dependent readiness-gated scheme
par = {0: [], 1: [0], 2: [0], 3: [1, 2]}; counts = {}
for _ in range(samples):
    rec = {}
    while len(rec) < 4:
        ready = [x for x in par if x not in rec and all(y in rec for y in par[x])]
        wts = np.array([1.0 + 3.0 * (rec.get(0, 0) == x % 6) + x for x in ready]); x = ready[rng.choice(len(ready), p=wts / wts.sum())]
        ws = np.array([np.prod([W[a, rec[y]] for y in par[x]]) for a in range(6)]); rec[x] = rng.choice(6, p=ws / ws.sum())
    key = (rec[0] == rec[3], rec[1] == rec[2]); counts[key] = counts.get(key, 0) + 1
exact = {}
for v in itertools.product(range(6), repeat=4):
    w = 1 / 6
    for x in (1, 2, 3):
        ws = np.array([np.prod([W[a, v[y]] for y in par[x]]) for a in range(6)]); w *= ws[v[x]] / ws.sum()
    key = (v[0] == v[3], v[1] == v[2]); exact[key] = exact.get(key, 0) + w
print("(d) diamond, events (v0 = v3, v1 = v2): " + "; ".join(f"{k}: sampled {counts.get(k, 0)/samples:.4f} exact {exact[k]:.4f}" for k in sorted(exact)))
