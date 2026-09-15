"""Control, block 15 (supervisor): the formation unit. Six-axis menu, product rule (3,1,2).
Joint law on a unit U given outside records v_O: prod_{edges inside U and U-O} phi / Z_U(v_O).  Sequential law along an order:
prod_x r(v_x | v_{A_x}), A_x = (N(x) cap O) cup (inside neighbours recorded before x).
(1) isolated star (center + 6 leaves): classes by k = number of leaves before the center; TV(seq, joint) per k;
(2) isolated plaquette: joint = static; TV to the 4 class laws;
(3) star in an environment (outside values all +x, and a fixed mixed configuration): TV(joint, center-first) and (joint, leaves-first);
(4) domino and path-of-3 in an environment: all orders vs joint; the criterion 'no site records an inside neighbour together with a second neighbour';
(5) the lemma: K_k(a, b, ..., b) differs between a = b and a = -b for k = 2..6."""
from fractions import Fraction as F
from itertools import permutations, product
from functools import reduce
import random, time
M = 6
def orbit_type(s, u):
    return "p" if s == u else ("q" if s // 2 == u // 2 else "r")
W = {"p": 3, "q": 1, "r": 2}
phi = [[W[orbit_type(s, t)] for t in range(M)] for s in range(M)]
Z1 = sum(phi[0])
_C = {}
def cond(rec, s):
    key = (rec, s)
    if key not in _C:
        if not rec:
            _C[key] = F(1, M)
        else:
            num = reduce(lambda a, b: a * b, [phi[s][a] for a in rec], 1)
            den = sum(reduce(lambda a, b: a * b, [phi[u][a] for a in rec], 1) for u in range(M))
            _C[key] = F(num, den)
    return _C[key]
def nbrs(p):
    return [tuple(p[k] + d[k] for k in range(3)) for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
def make_unit(U):
    U = list(U); Uset = set(U)
    O = sorted({y for x in U for y in nbrs(x) if y not in Uset})
    return U, O
def joint_law(U, O, vO):
    Uset = set(U); idx = {x: i for i, x in enumerate(U)}
    w = {}
    for v in product(range(M), repeat=len(U)):
        x_ = 1
        for i, x in enumerate(U):
            for y in nbrs(x):
                if y in Uset:
                    j = idx[y]
                    if j > i:
                        x_ *= phi[v[i]][v[j]]
                elif y in vO:
                    x_ *= phi[v[i]][vO[y]]
        w[v] = x_
    Z = sum(w.values())
    return {v: F(x_, Z) for v, x_ in w.items()}
def seq_law(U, O, vO, order):
    Uset = set(U); idx = {x: i for i, x in enumerate(U)}
    law = {}
    for v in product(range(M), repeat=len(U)):
        S = set(); pr = F(1)
        for x in order:
            rec = []
            for y in nbrs(x):
                if y in Uset and y in S:
                    rec.append(v[idx[y]])
                elif y in vO:
                    rec.append(vO[y])
            pr *= cond(tuple(sorted(rec)), v[idx[x]])
            S.add(x)
        law[v] = pr
    return law
def tv(a, b):
    return sum(abs(a[v] - b[v]) for v in a) / 2
def violates(U, O, vO, order):
    """criterion: some site records an inside neighbour together with a second neighbour (inside or outside)"""
    Uset = set(U); S = set()
    for x in order:
        inside = [y for y in nbrs(x) if y in Uset and y in S]
        outside = [y for y in nbrs(x) if y in vO]
        if inside and len(inside) + len(outside) >= 2:
            return True
        S.add(x)
    return False
# (1) isolated star
center = (0, 0, 0); leaves = nbrs(center)
U, O = make_unit([center] + leaves)
J = joint_law(U, O, {})
t0 = time.time()
for k in range(7):
    order = leaves[:k] + [center] + leaves[k:]
    L = seq_law(U, O, {}, order)
    print(f"isolated star, {k} leaves before the center: TV(seq, joint) = {tv(L, J)} ({float(tv(L, J)):.5f}); violates criterion: {violates(U, O, {}, order)}")
print(f"  ({time.time()-t0:.1f}s)")
# (2) isolated plaquette
Up, Op = make_unit([(0,0,0),(1,0,0),(1,1,0),(0,1,0)])
Jp = joint_law(Up, Op, {})
seen = {}
for order in permutations(Up):
    L = seq_law(Up, Op, {}, order)
    key = tv(L, Jp)
    seen[key] = seen.get(key, 0) + 1
print("isolated plaquette: distinct TV(seq, joint) values over 24 orders:", {str(k): n for k, n in seen.items()})
# (3) star in an environment
vO_allx = {y: 0 for y in O}
random.seed(3); vO_mixed = {y: random.randrange(M) for y in O}
for name, vO in (("all +x", vO_allx), ("mixed", vO_mixed)):
    Je = joint_law(U, O, vO)
    for k, order in ((0, [center] + leaves), (6, leaves + [center]), (1, leaves[:1] + [center] + leaves[1:])):
        L = seq_law(U, O, vO, order)
        print(f"star in environment ({name}), {k} leaves first: TV(seq, joint) = {float(tv(L, Je)):.5f}; violates: {violates(U, O, vO, order)}")
# (4) domino and path in an environment
for name, sites in (("domino", [(0,0,0),(1,0,0)]), ("path3", [(0,0,0),(1,0,0),(2,0,0)]), ("single", [(0,0,0)])):
    Ud, Od = make_unit(sites)
    random.seed(5); vO = {y: random.randrange(M) for y in Od}
    Jd = joint_law(Ud, Od, vO)
    res = []
    for order in permutations(Ud):
        L = seq_law(Ud, Od, vO, order)
        res.append((tv(L, Jd) == 0, violates(Ud, Od, vO, order)))
    print(f"{name} in a mixed environment: (equal, violates) over orders:", res)
# isolated path3 and domino (no environment): criterion vs equality
for name, sites in (("domino", [(0,0,0),(1,0,0)]), ("path3", [(0,0,0),(1,0,0),(2,0,0)])):
    Ud, Od = make_unit(sites)
    Jd = joint_law(Ud, Od, {})
    res = [(tv(seq_law(Ud, Od, {}, order), Jd) == 0, violates(Ud, Od, {}, order)) for order in permutations(Ud)]
    print(f"{name} isolated: (equal, violates) over orders:", res)
# (5) lemma
for k in range(2, 7):
    b = 0
    same = sum(F(phi[s][b], Z1) ** k for s in range(M))
    anti = sum(F(phi[s][1], Z1) * F(phi[s][b], Z1) ** (k - 1) for s in range(M))
    print(f"K_{k}(b,...,b) = {same} vs K_{k}(-b,b,...,b) = {anti}: differ {same != anti}; predicted difference ((p-q)/Z1)[(p/Z1)^(k-1) - (q/Z1)^(k-1)] = {F(2, Z1) * (F(3, Z1) ** (k-1) - F(1, Z1) ** (k-1))} == {same - anti}")
