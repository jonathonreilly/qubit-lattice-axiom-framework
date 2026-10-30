#!/usr/bin/env python3
"""Structure of the logical orbits (7, 28, 28) of the 168-group on N(S)/S: is the 7-orbit a Lagrangian
(logical stabiliser state => G fixes a logical stabiliser basis) or a maximal anticommuting set (Cl(0,7),
octonion left multiplications)?  Also: does the logical image preserve any 3-qubit tensor decomposition?"""
import itertools, collections
n = 8
def pauli(s):
    x = z = 0
    for i, c in enumerate(s):
        if c in 'XY': x |= 1 << i
        if c in 'ZY': z |= 1 << i
    return (x, z)
def mul(a, b): return (a[0] ^ b[0], a[1] ^ b[1])
def symp(a, b): return (bin(a[0] & b[1]).count('1') + bin(a[1] & b[0]).count('1')) & 1
def span(gs):
    S = {(0, 0)}
    for g in gs: S |= {mul(s, g) for s in S}
    return S
FR = {'id': lambda x, z: (x, z), 'XYZ': lambda x, z: (x ^ z, x), 'ZYX': lambda x, z: (z, x ^ z)}
def act(p, perm, fr):
    x = z = 0
    for j in range(n):
        a, b = fr((p[0] >> j) & 1, (p[1] >> j) & 1); t = perm[j]; x |= a << t; z |= b << t
    return (x, z)
GENS = [pauli(s) for s in "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()]
S = span(GENS)
G = [(p, f) for p in itertools.permutations(range(n)) for f in FR if all(act(g, p, FR[f]) in S for g in GENS)]
assert len(G) == 168
N = [(x, z) for x in range(256) for z in range(256) if all(symp((x, z), g) == 0 for g in GENS)]
canon = lambda p: min(mul(p, s) for s in S)
reps = sorted({canon(p) for p in N}); zero = canon((0, 0))
orb = []; seen = set()
for r in reps:
    if r == zero or r in seen: continue
    o = {r}; fr = [r]
    while fr:
        nf = []
        for a in fr:
            for p, f in G:
                b = canon(act(a, p, FR[f]))
                if b not in o: o.add(b); nf.append(b)
        fr = nf
    seen |= o; orb.append(sorted(o))
wt = lambda p: bin(p[0] | p[1]).count('1')
minw = lambda r: min(wt(mul(r, s)) for s in S)
for o in orb:
    comm = collections.Counter(symp(a, b) for a, b in itertools.combinations(o, 2))
    closed = all(canon(mul(a, b)) in set(o) | {zero} for a, b in itertools.combinations(o, 2))
    print(f"orbit size {len(o)}: min weights {dict(collections.Counter(minw(r) for r in o))}; pairwise symplectic products {dict(comm)}; closed under product (+0): {closed}")
o7 = next(o for o in orb if len(o) == 7)
if all(symp(a, b) == 0 for a, b in itertools.combinations(o7, 2)) and len(span(o7)) // 32 >= 1:
    L = {canon(p) for p in span(o7)}
    print("7-orbit spans a subspace of N/S of size", len(L), "-> isotropic (Lagrangian if 8):", len(L) == 8)
# 3-qubit tensor decompositions of N/S: unordered triples of mutually orthogonal hyperbolic planes
nz = [r for r in reps if r != zero]
planes = set()
for a, b in itertools.combinations(nz, 2):
    if symp(a, b) == 1:
        planes.add(frozenset({a, b, canon(mul(a, b))}))
planes = list(planes)
orth = lambda P1, P2: all(symp(a, b) == 0 for a in P1 for b in P2)
decs = set()
for P1, P2 in itertools.combinations(planes, 2):
    if not orth(P1, P2): continue
    for P3 in planes:
        if P3 in (P1, P2) or not (orth(P1, P3) and orth(P2, P3)): continue
        decs.add(frozenset({P1, P2, P3}))
print("hyperbolic planes:", len(planes), " 3-qubit decompositions of the logical space:", len(decs))
def gimg(P, g): return frozenset(canon(act(a, g[0], FR[g[1]])) for a in P)
stab_sizes = collections.Counter()
for D in decs:
    st = sum(1 for g in G if frozenset(gimg(P, g) for P in D) == D)
    stab_sizes[st] += 1
print("stabiliser orders in G of the decompositions (order -> how many decompositions):", dict(stab_sizes))
# for the best decomposition: what does its stabiliser do (permute the 3 qubits?)
best = max(decs, key=lambda D: sum(1 for g in G if frozenset(gimg(P, g) for P in D) == D))
stab = [g for g in G if frozenset(gimg(P, g) for P in best) == best]
Dl = list(best)
acts = collections.Counter()
for g in stab:
    pi = tuple(Dl.index(gimg(P, g)) for P in Dl)
    acts[(pi, g[1])] += 1
print("best decomposition: stabiliser", len(stab), "; induced logical-qubit permutations (perm, frame): count", dict(acts))
