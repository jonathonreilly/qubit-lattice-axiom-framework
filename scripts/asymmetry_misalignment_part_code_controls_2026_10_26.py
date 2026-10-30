#!/usr/bin/env python3
"""(a) logical action of the 168-group on N(S)/S; (b) best alignment of code symmetries with cube O_h;
(c) Hamming/RM(1,3) common cause: projections of S; (d) numerology controls: [[8,3,2]] cube colour code,
random 8-qubit stabiliser codes, and how often perm x uniform-frame groups contain an order-7 element."""
import itertools, collections, random, time
t0 = time.time(); n = 8
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
FR = {'id': lambda x, z: (x, z), 'XYZ': lambda x, z: (x ^ z, x), 'ZYX': lambda x, z: (z, x ^ z),
      'H': lambda x, z: (z, x), 'S': lambda x, z: (x, x ^ z), 'HSH': lambda x, z: (x ^ z, z)}
def act(p, perm, fr):
    x = z = 0
    for j in range(n):
        a, b = fr((p[0] >> j) & 1, (p[1] >> j) & 1); t = perm[j]; x |= a << t; z |= b << t
    return (x, z)
def symgroup(gens, frames=('id', 'XYZ', 'ZYX', 'H', 'S', 'HSH'), perms=None):
    S = span(gens); out = []
    for perm in (perms or itertools.permutations(range(n))):
        for f in frames:
            if all(act(g, perm, FR[f]) in S for g in gens): out.append((perm, f))
    return out
e = tuple(range(n))
def comp(p, q): return tuple(p[q[j]] for j in range(n))
def order(p):
    x = p; k = 1
    while x != e: x = comp(p, x); k += 1
    return k
GENS = [pauli(s) for s in "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()]
S = span(GENS)
G = symgroup(GENS, frames=('id', 'XYZ', 'ZYX'))
assert len(G) == 168
# ---------- (a) logical action ----------
allP = [(x, z) for x in range(256) for z in range(256)]
N = [p for p in allP if all(symp(p, g) == 0 for g in GENS)]
assert len(N) == 2048
# coset representatives: canonical rep = min over coset
def canon(p): return min(mul(p, s) for s in S)
reps = sorted({canon(p) for p in N})
assert len(reps) == 64
ridx = {r: i for i, r in enumerate(reps)}
def logical_perm(perm, f):
    return tuple(ridx[canon(act(r, perm, FR[f]))] for r in reps)
LG = collections.Counter(); kernel = []
img = {}
for perm, f in G:
    lp = logical_perm(perm, f); img.setdefault(lp, []).append((perm, f))
    if lp == tuple(range(64)): kernel.append((perm, f, order(perm)))
print("(a) logical image order:", len(img), " kernel order:", len(kernel), " kernel element orders:", collections.Counter(k[2] for k in kernel))
# which elements act trivially / orders of logical images
def lorder(lp):
    x = lp; k = 1; idt = tuple(range(64))
    while x != idt: x = tuple(lp[i] for i in x); k += 1
    return k
byord = collections.defaultdict(collections.Counter)
for lp, els in img.items():
    for perm, f in els: byord[order(perm)][lorder(lp)] += 1
print("    physical order -> logical order histogram:", {k: dict(v) for k, v in sorted(byord.items())})
# orbits on 63 nonzero logical classes
orbits = []; seen = set()
zero = ridx[canon((0, 0))]
for i in range(64):
    if i in seen or i == zero: continue
    orb = {i}; fr = [i]
    while fr:
        nf = []
        for a in fr:
            for lp in img:
                b = lp[a]
                if b not in orb: orb.add(b); nf.append(b)
        fr = nf
    seen |= orb; orbits.append(len(orb))
print("    orbit sizes on the 63 nonzero logical classes:", sorted(orbits))
# does any order-7 element act nontrivially on the logical space?
o7 = [(lp, els) for lp, els in img.items() if any(order(p) == 7 for p, _ in els)]
print("    order-7 physical elements acting nontrivially on logicals:", sum(lorder(lp) == 7 for lp, _ in o7), "of", len(o7))
# weights of logical classes (min weight in coset) and the 2^3 translations' logical action
def wt(p): return bin(p[0] | p[1]).count('1')
minw = {r: min(wt(mul(r, s)) for s in S) for r in reps}
print("    min-weight distribution of 63 nonzero logical classes:", dict(collections.Counter(minw[r] for r in reps if r != (0, 0))))
# ---------- (b) cube alignment ----------
V = list(itertools.product((0, 1), repeat=3))
vid = {v: i for i, v in enumerate(V)}
Oh = []
for P3 in itertools.permutations(range(3)):
    for b in itertools.product((0, 1), repeat=3):
        Oh.append(tuple(vid[tuple(v[P3[k]] ^ b[k] for k in range(3))] for v in V))
assert len(set(Oh)) == 48
# rotation subgroup: proper ones; classify by cycle type on vertices
def ctype(p):
    seen = set(); cyc = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        cyc.append(L)
    return tuple(sorted(cyc))
Pset = {p for p, f in G}; fof = {p: f for p, f in G}
best = 0; bestlabs = []
for lab in itertools.permutations(range(n)):   # qubit q sits on vertex lab[q]
    inv = [0] * n
    for q in range(n): inv[lab[q]] = q
    # cube element g (on vertices) -> qubit perm q -> inv[g[lab[q]]]
    c = 0
    for g in Oh:
        qp = tuple(inv[g[lab[q]]] for q in range(n))
        if qp in Pset: c += 1
    if c > best: best = c; bestlabs = [lab]
    elif c == best: bestlabs.append(lab)
lab = bestlabs[0]; inv = [0] * n
for q in range(n): inv[lab[q]] = q
common = [g for g in Oh if tuple(inv[g[lab[q]]] for q in range(n)) in Pset]
print("(b) max |O_h cap code group| over all 8! labellings:", best, " #labellings achieving it:", len(bestlabs))
print("    cycle types (on vertices) of the common subgroup:", dict(collections.Counter(ctype(g) for g in common)))
def det3(P3):
    M = [[1 if P3[r] == c else 0 for c in range(3)] for r in range(3)]
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
# geometric type: x -> P x + b on {0,1}^3 corresponds to R^3 map x -> P'(x - c) + c with sign flips; proper iff det(P) * (-1)^{|b|} = +1
ohinfo = {}
for P3 in itertools.permutations(range(3)):
    for b in itertools.product((0, 1), repeat=3):
        g = tuple(vid[tuple(v[P3[k]] ^ b[k] for k in range(3))] for v in V)
        ohinfo[g] = det3(P3) * (-1) ** sum(b)
print("    proper rotations in common subgroup:", sum(ohinfo[g] == 1 for g in common), " improper:", sum(ohinfo[g] == -1 for g in common))
print("    frames of the common elements:", dict(collections.Counter(fof[tuple(inv[g[lab[q]]] for q in range(n))] for g in common)))
# ---------- (c) RM(1,3) projections ----------
def proj(Sset, which):
    out = set()
    for x, z in Sset:
        out.add({'X': x, 'Z': z, 'Y': x ^ z}[which] if which != 'Y' else (x ^ z))
    return out
# careful: "Y-part" = positions where Pauli is Y; X-part = positions with X or Y; Z-part = Z or Y
for w in ('X', 'Z'):
    pr = {(x if w == 'X' else z) for x, z in S}
    wts = collections.Counter(bin(v).count('1') for v in pr)
    print(f"(c) {w}-support projection of S: size {len(pr)}, weights {dict(sorted(wts.items()))}")
pr = {x ^ z for x, z in S}
print("    (X xor Z)-projection: size", len(pr), "weights", dict(sorted(collections.Counter(bin(v).count('1') for v in pr).items())))
# is the X-projection RM(1,3) in the F_8 labelling? RM(1,3) = affine functionals on F_2^3; under an affine relabelling check: Aut of X-projection
Xp = {x for x, z in S}
autXp = sum(1 for p in itertools.permutations(range(n)) if all(sum(((v >> j) & 1) << p[j] for j in range(n)) in Xp for v in Xp))
print("    |Aut(X-projection)| =", autXp, "(AGL(3,2) has order 1344: projection is the [8,4,4] extended Hamming = RM(1,3))")
# ---------- (d) numerology controls ----------
# [[8,3,2]] cube colour code on vertices {0,1}^3: X-stab all-ones; Z-stabs RM(1,3) = all-ones + 3 coordinate faces
ones = (1 << 8) - 1
face = [sum(1 << vid[v] for v in V if v[k] == 1) for k in range(3)]
G832 = [(ones, 0), (0, ones)] + [(0, f) for f in face]
S832 = span(G832)
N832 = [p for p in allP if all(symp(p, g) == 0 for g in G832)]
d832 = min(wt(p) for p in N832 if p not in S832)
G8 = symgroup(G832)
print("(d) [[8,3,2]] colour code: |S| =", len(S832), "k =", 3, "d =", d832, " |perm x uniform-frame group| =", len(G8), "frames", dict(collections.Counter(f for _, f in G8)))
P8 = {p for p, f in G8}
print("    contains all 48 cube symmetries (standard labelling):", all(g in P8 for g in Oh), "; order stats", dict(sorted(collections.Counter(order(p) for p in P8).items())))
# logical action of cube 3-fold rotation about (1,1,1) on [[8,3,2]]: cyclic perm of the 3 logical qubits?
c3 = tuple(vid[(v[1], v[2], v[0])] for v in V)
LX = [(f, 0) for f in face]       # logical X_k: X on face x_k = 1 (weight 4)
# logical Z_k: Z on an edge along direction k (weight 2): vertices 0 and e_k
LZ = [(0, (1 << vid[(0, 0, 0)]) | (1 << vid[tuple(1 if t == k else 0 for t in range(3))])) for k in range(3)]
cr = [[symp(LX[a], LZ[b]) for b in range(3)] for a in range(3)]
print("    [[8,3,2]] logical X_k/Z_k anticommutation matrix:", cr)
canon832 = lambda p: min(mul(p, s) for s in S832)
imgX = [[k2 for k2 in range(3) if canon832(act(LX[k], c3, FR['id'])) == canon832(LX[k2])] for k in range(3)]
imgZ = [[k2 for k2 in range(3) if canon832(act(LZ[k], c3, FR['id'])) == canon832(LZ[k2])] for k in range(3)]
print("    cube C3 about (111), no frame: logical X_k ->", imgX, " Z_k ->", imgZ)
# random [[8,3]] stabiliser codes: how often does the perm x uniform-frame group contain an order-7 element?
random.seed(1)
def rand_code(k=3):
    gens = []
    while len(gens) < n - k:
        p = (random.randrange(256), random.randrange(256))
        if p == (0, 0): continue
        if any(symp(p, g) for g in gens): continue
        if p in span(gens): continue
        gens.append(p)
    return gens
o7perms = [p for p in itertools.permutations(range(n)) if order(p) == 7]
trials = 100; hits = 0; nontriv = 0
for t in range(trials):
    gs = rand_code(3); Sg = span(gs)
    if any(all(act(g, p, FR[f]) in Sg for g in gs) for p in o7perms for f in ('id', 'XYZ', 'ZYX', 'H', 'S', 'HSH')): hits += 1
print(f"    random [[8,3]] codes with an order-7 perm x uniform-frame symmetry: {hits}/{trials}")
print("time %.1fs" % (time.time() - t0))
