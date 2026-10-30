#!/usr/bin/env python3
"""Independent re-derivation of the [[8,3,3]] code symmetry group (perm x uniform frame),
its isomorphism type, the full LC x perm automorphism group (different method: GL(5,2) acting on
the stabiliser space S, permuting the 8 subspaces K_j = {s in S : s|_j = I}), and the logical action."""
import itertools, collections, sys, time
t0 = time.time()
n = 8
# Pauli on n qubits as pair (x, z) of n-bit ints; phases ignored (stabiliser group mod phases)
def pauli(s):
    x = z = 0
    for i, c in enumerate(s):
        if c in 'XY': x |= 1 << i
        if c in 'ZY': z |= 1 << i
    return (x, z)
GENS = [pauli(s) for s in "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()]
def mul(a, b): return (a[0] ^ b[0], a[1] ^ b[1])
def symp(a, b): return (bin(a[0] & b[1]).count('1') + bin(a[1] & b[0]).count('1')) & 1
assert all(symp(a, b) == 0 for a in GENS for b in GENS)
S = {(0, 0)}
for g in GENS: S |= {mul(s, g) for s in S}
assert len(S) == 32
# local frame maps on one qubit as functions (x,z)->(x',z'); uniform frames
FR = {'id': lambda x, z: (x, z), 'XYZ': lambda x, z: (x ^ z, x), 'ZYX': lambda x, z: (z, x ^ z),
      'H': lambda x, z: (z, x), 'S': lambda x, z: (x, x ^ z), 'HSH': lambda x, z: (x ^ z, z)}
# sanity of XYZ: X=(1,0)->(1,1)=Y ; Y=(1,1)->(0,1)=Z ; Z=(0,1)->(1,0)=X
assert FR['XYZ'](1, 0) == (1, 1) and FR['XYZ'](1, 1) == (0, 1) and FR['XYZ'](0, 1) == (1, 0)
def act(p, perm, fr):
    x = z = 0
    for j in range(n):
        a, b = fr((p[0] >> j) & 1, (p[1] >> j) & 1)
        t = perm[j]; x |= a << t; z |= b << t
    return (x, z)
def preserves(perm, fr): return all(act(g, perm, fr) in S for g in GENS)
G = []
for perm in itertools.permutations(range(n)):
    for f in ('id', 'XYZ', 'ZYX', 'H', 'S', 'HSH'):
        if preserves(perm, FR[f]): G.append((perm, f))
cnt = collections.Counter(f for _, f in G)
print("uniform-frame symmetries by frame:", dict(cnt), " total", len(G))
perms_only = [p for p, f in G]
assert len(set(perms_only)) == len(perms_only), "projection to S_8 not injective"
# group ops on permutations (p as tuple: qubit j -> p[j])
def comp(p, q): return tuple(p[q[j]] for j in range(n))   # p after q
def order(p):
    e = tuple(range(n)); x = p; k = 1
    while x != e: x = comp(p, x); k += 1
    return k
P = set(perms_only)
assert all(comp(a, b) in P for a in P for b in P), "not closed"
oc = collections.Counter(order(p) for p in P)
print("element orders:", dict(sorted(oc.items())))
# orders by frame
of = collections.defaultdict(collections.Counter)
for p, f in G: of[f][order(p)] += 1
print("orders by frame:", {f: dict(sorted(c.items())) for f, c in of.items()})
def ctype(p):
    seen = set(); cyc = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        cyc.append(L)
    return tuple(sorted(cyc))
print("cycle types:", dict(collections.Counter(ctype(p) for p in P)))
# --- structure: normal subgroup T = {e} + involutions; regular? abelian?
e = tuple(range(n))
inv = [p for p in P if order(p) == 2]
T = [e] + inv
inverse = lambda p: tuple(sorted(range(n), key=lambda j: p[j]))
assert all(comp(a, b) in set(T) for a in T for b in T), "T not closed"
assert all(comp(a, b) == comp(b, a) for a in T for b in T)
assert all(comp(comp(g, t), inverse(g)) in set(T) for g in P for t in T), "T not normal"
assert all(t[0] != 0 for t in inv) and len({t[0] for t in T}) == 8, "T not regular"
print("T = 2^3 elementary abelian, normal, regular on the 8 qubits: OK")
center = [z for z in P if all(comp(z, g) == comp(g, z) for g in P)]
print("centre order:", len(center))
# derived subgroup
def closure(gens):
    H = {e}; fr = [e]
    while fr:
        nf = []
        for a in fr:
            for b in gens:
                c = comp(a, b)
                if c not in H: H.add(c); nf.append(c)
        fr = nf
    return H
comms = {comp(comp(a, b), comp(inverse(a), inverse(b))) for a in P for b in P}
D = closure(list(comms)); D2 = closure(list({comp(comp(a, b), comp(inverse(a), inverse(b))) for a in D for b in D}))
print("derived series orders:", len(P), len(D), len(D2))
# --- explicit permutation isomorphism with AGammaL(1,8)
# label qubit q <-> vector v(q) in F_2^3 via translations: v(q0)=0, v(t(q0)) = coordinates of t in a basis of T
q0 = 0
tb = []   # basis of T as perms
def tspan(bs):
    H = {e}
    for b in bs: H |= {comp(h, b) for h in H}
    return H
for t in inv:
    if t not in tspan(tb): tb.append(t)
    if len(tb) == 3: break
lab = {}
for bits in range(8):
    t = e
    for i in range(3):
        if bits >> i & 1: t = comp(t, tb[i])
    lab[t[q0]] = bits
assert sorted(lab.values()) == list(range(8))
# F_8 arithmetic with a Singer cycle from the group: element of order 7 fixing q0 acts linearly
s7 = next(p for p in P if order(p) == 7 and p[q0] == q0)
A = [lab[s7[{v: q for q, v in lab.items()}[1 << i]]] for i in range(3)]   # images of basis vectors
def lin(M, v):
    r = 0
    for i in range(3):
        if v >> i & 1: r ^= M[i]
    return r
# check s7 acts linearly on labels
assert all(lab[s7[q]] == lin(A, lab[q]) for q in range(8)), "Singer element not linear"
# minimal polynomial of A: field F_2[A] = F_8 ; represent field elements as matrices powers of A
powA = [1]   # vector images: alpha^k * 1 where '1' := basis vector e1 = 1
v = 1
for k in range(7): v = lin(A, v); powA.append(v)
assert len(set(powA[:7])) == 7 and powA[7] == 1, "not a Singer cycle"
# field: element x (nonzero) = alpha^k where powA[k] = x ; multiplication via exponents
log = {powA[k]: k for k in range(7)}
def fmul(a, b):
    if a == 0 or b == 0: return 0
    return powA[(log[a] + log[b]) % 7]
def fpow2(a, i):
    for _ in range(i): a = fmul(a, a)
    return a
# check x -> x+y is the field addition (XOR) by construction; verify all of P = {x -> a x^(2^i) + b}
qof = {v: q for q, v in lab.items()}
AGL = {}
for a in range(1, 8):
    for i in range(3):
        for b in range(8):
            perm = tuple(qof[fmul(a, fpow2(lab[q], i)) ^ b] for q in range(8))
            AGL[perm] = (a, i, b)
assert len(AGL) == 168
print("P == AGammaL(1,8) in its natural action (explicit F_8 labelling):", set(AGL) == P)
# frame vs Galois exponent
lock = collections.Counter((AGL[p][1], f) for p, f in G)
print("(Galois exponent i, frame) pairs:", dict(lock))
# Compare with PSL(2,7) on 8 points: orders {1:1,2:21,3:56,4:42,7:48}
print("GL(3,2)=PSL(2,7) order stats would be {1:1,2:21,3:56,4:42,7:48}; observed has order-6 elements and only 7 involutions -> not PSL(2,7)")
print("AGL(1,8) x Z3 would have elements of order 21 and centre Z3; observed max order", max(oc), "centre", len(center))
# ---- full LC x perm automorphism group via GL(S) permuting K_j (independent method)
Sl = sorted(S)
basis = GENS
def coords(s):
    # solve s = sum c_i GENS_i  (brute force over 32)
    for c in range(32):
        acc = (0, 0)
        for i in range(5):
            if c >> i & 1: acc = mul(acc, GENS[i])
        if acc == s: return c
    raise ValueError
C = {s: coords(s) for s in S}
elem = {c: s for s, c in C.items()}
K = []
for j in range(n):
    Kj = frozenset(C[s] for s in S if not ((s[0] >> j) & 1) and not ((s[1] >> j) & 1))
    assert len(Kj) == 8
    K.append(Kj)
assert len(set(K)) == 8
Kidx = {k: j for j, k in enumerate(K)}
def kbasis(Kj):
    b = []
    sp = {0}
    for v in sorted(Kj):
        if v not in sp: b.append(v); sp |= {x ^ v for x in sp}
    return b
KB = [kbasis(k) for k in K]
def applyM(Mcols, v):
    r = 0
    for i in range(5):
        if v >> i & 1: r ^= Mcols[i]
    return r
def span(vs):
    sp = {0}
    for v in vs: sp |= {x ^ v for x in sp}
    return sp
# enumerate M: choose image of K_0 as K_i with a linear iso, then images of 2 complement vectors
b0 = KB[0]
comp_vecs = []
sp0 = span(b0)
for v in range(1, 32):
    if v not in span(list(sp0) + comp_vecs) and len(comp_vecs) < 2: comp_vecs.append(v)
full_basis = b0 + comp_vecs   # basis of F_2^5
# matrix from basis images: need Mcols (images of unit vectors). Solve via change of basis.
def cols_from_basis_images(imgs):
    # find, for each unit vector u_i, its expression in full_basis
    cols = []
    for i in range(5):
        u = 1 << i
        for c in range(32):
            acc = 0
            for k in range(5):
                if c >> k & 1: acc ^= full_basis[k]
            if acc == u: break
        r = 0
        for k in range(5):
            if c >> k & 1: r ^= imgs[k]
        cols.append(r)
    return cols
autos = []
GL32 = []
for Ki in K:
    kb = kbasis(Ki); kel = [v for v in Ki if v]
    for a, b, c in itertools.permutations(kel, 3):
        if len(span([a, b, c])) == 8: GL32.append((Ki, (a, b, c)))
assert len(GL32) == 8 * 168
for Ki, (a, b, c) in GL32:
    for d in range(1, 32):
        if d in span([a, b, c]): continue
        spd = span([a, b, c, d])
        for f in range(1, 32):
            if f in spd: continue
            cols = cols_from_basis_images([a, b, c, d, f])
            ok = True; pi = [None] * 8
            for j in range(8):
                img = frozenset(applyM(cols, v) for v in K[j])
                if img not in Kidx: ok = False; break
                pi[j] = Kidx[img]
            if ok: autos.append((tuple(pi), cols))
print("full LC x perm automorphism group order (GL(S) method):", len(autos))
# induced local frame per qubit: c_j : S/K_j -> S/K_pi(j) read through restriction to qubit j
def restr(s, j): return ((s[0] >> j) & 1, (s[1] >> j) & 1)
uniform = 0; frames_seen = collections.Counter()
for pi, cols in autos:
    fr_j = []
    for j in range(8):
        mp = {}
        for v in range(32):
            s = elem[v]; s2 = elem[applyM(cols, v)]
            k = restr(s, j); im = restr(s2, pi[j])
            if k in mp: assert mp[k] == im
            mp[k] = im
        fr_j.append(tuple(sorted(mp.items())))
    if len(set(fr_j)) == 1: uniform += 1
    frames_seen[len(set(fr_j))] += 1
print("automorphisms with a uniform frame:", uniform, "of", len(autos), " (#distinct per-qubit frames histogram:", dict(frames_seen), ")")
print("perm images of full group == P:", {pi for pi, _ in autos} == P)
print("time %.1fs" % (time.time() - t0))
