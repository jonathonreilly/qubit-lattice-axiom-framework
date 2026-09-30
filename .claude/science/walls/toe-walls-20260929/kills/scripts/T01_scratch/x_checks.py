#!/usr/bin/env python3
"""T01 exact side-checks X1-X3 and the exact targets for validation V1.

Exact arithmetic (fractions). Rule: six-axis menu, phi = p equal, q opposite, r orthogonal.
Window for X1/V1: the open 4-cycle (plaquette). Author: Claude Sonnet 5.5.
"""
import itertools, json, sys
from fractions import Fraction as F

p, q, r = 3, 1, 2
AX = list(range(6))  # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z ; opposite of a is a^1


def phi(a, b):
    if a == b:
        return p
    if a ^ 1 == b:
        return q
    return r


def kernel(recorded_vals):
    """distribution over the 6 axes given recorded neighbour values (list)"""
    w = [F(1)] * 6
    if not recorded_vals:
        return [F(1, 6)] * 6
    w = [F(1)] * 6
    for a in AX:
        for b in recorded_vals:
            w[a] *= phi(a, b)
    Z = sum(w)
    return [x / Z for x in w]


# ---------- graph: open 4-cycle ----------
N = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
nbr = {i: [] for i in range(N)}
for a, b in edges:
    nbr[a].append(b)
    nbr[b].append(a)


def order_law(order):
    """dict config-tuple -> Fraction, formation law of a fixed order"""
    law = {}
    def rec(i, formed, vals, pr):
        if i == N:
            law[tuple(vals[x] for x in range(N))] = law.get(tuple(vals[x] for x in range(N)), 0) + pr
            return
        x = order[i]
        rn = [vals[y] for y in nbr[x] if y in formed]
        K = kernel(rn)
        for a in AX:
            if K[a] == 0:
                continue
            vals[x] = a
            rec(i + 1, formed | {x}, vals, pr * K[a])
        vals.pop(x, None)
    rec(0, frozenset(), {}, F(1))
    return law


def race_order_probs(f):
    """exact probability of each order under hazard f(k), k = # formed in-window nbrs"""
    out = {}
    for order in itertools.permutations(range(N)):
        pr = F(1)
        formed = set()
        for x in order:
            rates = {}
            for s in range(N):
                if s in formed:
                    continue
                k = sum(1 for y in nbr[s] if y in formed)
                rates[s] = f(k)
            pr *= rates[x] / sum(rates.values())
            formed.add(x)
        out[order] = pr
    return out


def edge_agree(law):
    tot = F(0)
    for cfg, pr in law.items():
        tot += pr * F(sum(1 for a, b in edges if cfg[a] == cfg[b]), len(edges))
    return tot


def mix(orderlaws, probs):
    law = {}
    for o, pr in probs.items():
        for cfg, v in orderlaws[o].items():
            law[cfg] = law.get(cfg, 0) + pr * v
    return law


results = {}
orders = list(itertools.permutations(range(N)))
olaws = {o: order_law(o) for o in orders}
# X1: distinct laws
distinct = {}
for o in orders:
    key = tuple(sorted(olaws[o].items()))
    distinct.setdefault(key, []).append(o)
results['X1_distinct_order_laws'] = len(distinct)
results['X1_class_sizes'] = sorted(len(v) for v in distinct.values())
classes = list(distinct.values())
class_of = {}
for ci, cl in enumerate(classes):
    for o in cl:
        class_of[o] = ci

clauses = {
    'U': lambda k: F(1),
    'E': lambda k: F((1 + k) ** 2),
    'A': lambda k: F(1, 1 + k),
}
static_w = {}
for cfg in itertools.product(AX, repeat=N):
    w = F(1)
    for a, b in edges:
        w *= phi(cfg[a], cfg[b])
    static_w[cfg] = w
Zs = sum(static_w.values())
static = {c: w / Zs for c, w in static_w.items()}
results['plaquette_Z'] = int(Zs)
results['a1_exact'] = {}
results['barycentric'] = {}
for name, f in clauses.items():
    probs = race_order_probs(f)
    assert sum(probs.values()) == 1
    law = mix(olaws, probs)
    assert sum(law.values()) == 1
    a1 = edge_agree(law)
    results['a1_exact'][name] = [str(a1), float(a1)]
    bary = [F(0)] * len(classes)
    for o, pr in probs.items():
        bary[class_of[o]] += pr
    results['barycentric'][name] = [str(b) for b in bary]
results['a1_exact']['S'] = [str(edge_agree(static)), float(edge_agree(static))]
results['a1_exact']['uniform_baseline'] = ['1/6', 1 / 6]

# X2: projectivity lemma on path z-x-y, symbolic in f0,f1,f2 (numeric spot checks)
def p_x_before_y_path3(f0, f1):
    # sites z,x,y ; edges z-x, x-y ; ranks: first event
    tot = 3 * f0
    pr_first_z = F(f0) / tot
    pr_first_x = F(f0) / tot
    pr_first_y = F(f0) / tot
    # after z: x has k=1 (rate f1), y has k=0 (rate f0)
    after_z = F(f1) / (f0 + f1)
    return pr_first_x + pr_first_z * after_z

vals = []
for f0, f1 in [(1, 1), (1, 2), (2, 1), (1, 4), (3, 3)]:
    vals.append(((f0, f1), str(p_x_before_y_path3(F(f0), F(f1)))))
results['X2_path3_P_x_before_y'] = vals

# star window: centre c with m leaves; leaf-leaf order symmetric. Check f2=f0 needed: plaquette
# P(site 0 before site 1) for adjacent sites in plaquette under hazard f; equals 1/2 by symmetry
# ALWAYS, so plaquette alone does not force f2; use the path of 4 (w-z-x-y) probability of x<y
def path_probs(n, f):
    nb = {i: [j for j in (i - 1, i + 1) if 0 <= j < n] for i in range(n)}
    probs = {}
    for order in itertools.permutations(range(n)):
        pr = F(1)
        formed = set()
        for x in order:
            rates = {s: f(sum(1 for y in nb[s] if y in formed)) for s in range(n) if s not in formed}
            pr *= rates[x] / sum(rates.values())
            formed.add(x)
        probs[order] = pr
    return probs

def p_before(probs, a, b):
    return sum(pr for o, pr in probs.items() if o.index(a) < o.index(b))

# projectivity test: order law of the pair (1,2) inside a bigger path vs alone (=1/2)
res = {}
for name, f in clauses.items():
    for n in (3, 4, 5):
        pr = path_probs(n, f)
        res[f'{name}_path{n}_P(1<2)'] = str(p_before(pr, 1, 2))
results['X2_projectivity_paths'] = res

# X3: orbits of NN occupancy patterns under the 24 proper cubic rotations
import numpy as np
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1:
            rots.append(M)
assert len(rots) == 24
def act(M, i):
    v = np.array(dirs[i])
    w = tuple(M @ v)
    return dirs.index(w)
seen = set()
orbits = []
for mask in range(64):
    S = frozenset(i for i in range(6) if mask >> i & 1)
    if S in seen:
        continue
    orb = {frozenset(act(M, i) for i in S) for M in rots}
    seen |= orb
    orbits.append((len(S), len(orb)))
results['X3_orbits'] = len(orbits)
results['X3_orbit_sizes_by_k'] = sorted(orbits)

json.dump(results, open(sys.argv[1] if len(sys.argv) > 1 else 'x_checks_results.json', 'w'), indent=1)
print(json.dumps(results, indent=1))
