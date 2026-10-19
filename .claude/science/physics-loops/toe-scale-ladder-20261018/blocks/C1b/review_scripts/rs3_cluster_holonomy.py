#!/usr/bin/env python3
"""Reviewer check of C1b claim 0.2(a) at L=2 (mod 2), written independently of ctqmc.py.
A single SW plaquette cluster's time-slice link set S(tau) can change at a vertex on plaquette p only by
S -> S xor dp with dp ∩ S = 0 (add) or dp ⊆ S (remove).  A union of clusters obeys the same rule.
Over one period S returns to S(0); the change of the net-flip class mod 2 is the set of plaquettes toggled an
odd number of times.  We compute, for EVERY S(0) in 2^24 link sets, the group of achievable mod-2 classes
(holonomy of the graph S -- S xor dp), and test whether an elementary-cube boundary lies in their span.
Own lattice construction (no import from the block)."""
import numpy as np, numba as nb, itertools, sys

L = 2
def vid(x, y, z): return ((x % L) * L + y % L) * L + z % L
nv = L**3; nl = 3*nv
def link(x, y, z, a): return 3*vid(x, y, z) + a
plaqs = []   # list of 4-link lists
pnorm = []
for x, y, z in itertools.product(range(L), repeat=3):
    c = np.array([x, y, z])
    for a, b in ((0, 1), (1, 2), (0, 2)):
        ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
        ls = [link(*c, a), link(*(c+ea), b), link(*(c+eb), a), link(*c, b)]
        assert len(set(ls)) == 4
        plaqs.append(ls); pnorm.append(3 - a - b)
npl = len(plaqs)
mask = np.array([sum(1 << l for l in ls) for ls in plaqs], dtype=np.int64)
assert len(set(mask.tolist())) == npl

@nb.njit(cache=True)
def holonomy(mask, nl):
    N = 1 << nl
    npl = mask.shape[0]
    phi = np.zeros(N, dtype=np.int64)
    seen = np.zeros(N, dtype=np.uint8)
    q = np.empty(N, dtype=np.int64)
    basis = np.zeros(64, dtype=np.int64)   # GF(2) basis indexed by leading bit
    ncomp = 0
    for s0 in range(N):
        if seen[s0]:
            continue
        ncomp += 1
        seen[s0] = 1; phi[s0] = 0
        h, t = 0, 0
        q[t] = s0; t += 1
        while h < t:
            s = q[h]; h += 1
            for p in range(npl):
                m = mask[p]
                inter = s & m
                if inter != 0 and inter != m:
                    continue
                s2 = s ^ m
                val = phi[s] ^ (1 << p)
                if not seen[s2]:
                    seen[s2] = 1; phi[s2] = val; q[t] = s2; t += 1
                else:
                    x = val ^ phi[s2]
                    for bit in range(npl - 1, -1, -1):
                        if (x >> bit) & 1 == 0:
                            continue
                        if basis[bit] == 0:
                            basis[bit] = x
                            break
                        x ^= basis[bit]
    return basis, ncomp

def gf2_rank(vecs):
    b = {}
    for v in vecs:
        x = int(v)
        while x:
            hb = x.bit_length() - 1
            if hb in b: x ^= b[hb]
            else: b[hb] = x; break
    return b

def in_span(b, v):
    x = int(v)
    while x:
        hb = x.bit_length() - 1
        if hb not in b: return False
        x ^= b[hb]
    return True

# cycle space Z = ker(boundary mod 2)
Bmat = np.zeros((nl, npl), dtype=np.int64)
for p, ls in enumerate(plaqs):
    for l in ls: Bmat[l, p] ^= 1
# cubes
def pidx(x, y, z, o): return 3*vid(x, y, z) + o   # o: 0 (x,y) normal z, 1 (y,z) normal x, 2 (x,z) normal y
cubes = []
for x, y, z in itertools.product(range(L), repeat=3):
    fs = [pidx(x, y, z, 0), pidx(x, y, z+1, 0), pidx(x, y, z, 1), pidx(x+1, y, z, 1), pidx(x, y, z, 2), pidx(x, y+1, z, 2)]
    v = sum(1 << f for f in fs)
    assert all(((Bmat @ np.array([(v >> p) & 1 for p in range(npl)])) % 2) == 0)
    cubes.append(v)
planes = []
for o in range(3):
    for k in range(L):
        v = 0
        for x, y, z in itertools.product(range(L), repeat=3):
            if (o == 0 and z == k) or (o == 1 and x == k) or (o == 2 and y == k):
                v |= 1 << pidx(x, y, z, o)
        planes.append(v)
# dim Z by brute force rank: Z dim = npl - rank(B)
def rank_mod2(M):
    M = M.copy() % 2; r = 0
    for c in range(M.shape[1]):
        piv = [i for i in range(r, M.shape[0]) if M[i, c]]
        if not piv: continue
        M[[r, piv[0]]] = M[[piv[0], r]]
        for i in range(M.shape[0]):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
    return r
dimZ = npl - rank_mod2(Bmat)
bZ = gf2_rank(cubes + planes)
print(f"[INFO] L=2: {npl} plaquettes, dim Z(mod2 2-cycles) = {dimZ}, rank(cubes+planes) = {len(bZ)}")
basis, ncomp = holonomy(mask, nl)
H = [int(x) for x in basis if x != 0]
bH = gf2_rank(H)
bP = gf2_rank(planes)
print(f"[INFO] S-graph components over all 2^24 S(0): {ncomp}; dim span(holonomies) = {len(bH)}; dim span(planes) = {len(bP)}")
npass = nfail = 0
def chk(name, ok):
    global npass, nfail
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"); npass += ok; nfail += (not ok)
chk("every holonomy is a 2-cycle (sanity)", all(in_span(bZ, h) for h in H))
chk("dim span(cubes+planes) == dim Z (sanity)", len(bZ) == dimZ)
chk("no single elementary cube boundary lies in the cluster holonomy span (claim 0.2a, mod 2)",
    not any(in_span(bH, c) for c in cubes))
# v1 of this script had a reviewer conjecture "span(H) within span(planes)" as a check; it is false (dim 9 > 6)
# and is not a C1b claim, so it is now INFO only (v1 log kept: logs/rs3_cluster_holonomy.log).
print(f"[INFO] span(H) within span(planes): {all(in_span(bP, h) for h in H)} (reviewer conjecture, not a C1b claim)")
chk("dim span(H) = dim Z - 1 (a single Z2 obstruction)", len(bH) == dimZ - 1)
chk("every sum of two distinct cubes lies in span(H) (obstruction = parity of cube number)",
    all(in_span(bH, cubes[i] ^ cubes[j]) for i in range(8) for j in range(i+1, 8)))
chk("all 6 plane classes lie in span(H) (plane classes reachable, as NOTE 3.2 says)", all(in_span(bH, p) for p in planes))
print(f"[INFO] single cubes in span(planes): {sum(in_span(bP, c) for c in cubes)} of {len(cubes)}")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
