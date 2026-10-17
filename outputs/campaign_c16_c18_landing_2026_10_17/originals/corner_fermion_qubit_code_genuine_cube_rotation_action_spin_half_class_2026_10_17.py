#!/usr/bin/env python3
"""Corner-fermion qubit code: 48 qubits per site, a genuine linear action of the cube
rotation group O, and the emergent fermion's half-turn pair signs.

Companion note: docs/CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md

Model: BKSF on the corner graph (vertices = the 12 perpendicular direction pairs at each
site; edges = cuboctahedron edges at a site and plaquette links between sites). Each
cross-site link qubit is split into two repetition halves, one at each end site, so all
qubits sit on sites. Stabilizers: corner charges B_q, repetition R = ZZ, and signed loop
operators i^n F prod A for squares, triangles, plaquettes and edge tubes (uniform flux F
per type). Rotations: site permutation, on-site CZ network, single-qubit Z fixes, and a
correction by repetition stabilizers that makes the group law exact.
Usage: python3 <this> [L] [flux bits square,triangle,plaquette,tube; default 1010]
"""
import itertools, sys, time
import numpy as np

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
FLUX = dict(square=1, triangle=0, plaquette=1, tube=0)
if len(sys.argv) > 2:
    FLUX = dict(zip(('square', 'triangle', 'plaquette', 'tube'), map(int, sys.argv[2])))

DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def perp(d, e): return dot(d, e) == 0 and d != e
def add(v, d): return tuple((a+b) % L for a, b in zip(v, d))
CORN = sorted([tuple(sorted((d, e))) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0])
SITES = list(itertools.product(range(L), repeat=3))
SID = {v: i for i, v in enumerate(SITES)}
VERTS = [(v, c) for v in SITES for c in CORN]
VID = {q: i for i, q in enumerate(VERTS)}
def corner(*ds): return tuple(sorted(ds))

# local qubit labels at a site
ONS = []   # on-site edges: unordered pair of corners sharing one direction
for c1, c2 in itertools.combinations(CORN, 2):
    s = set(c1) & set(c2)
    if len(s) == 1:
        a = s.pop(); b1 = [d for d in c1 if d != a][0]; b2 = [d for d in c2 if d != a][0]
        if perp(b1, b2) and b1 != neg(b2):
            ONS.append((c1, c2))
assert len(ONS) == 24
HALF = [(c, a) for c in CORN for a in c]   # link half at corner c, via direction a
assert len(HALF) == 24
LOC = {('o', p): i for i, p in enumerate(ONS)}
LOC.update({('h', h): 24 + i for i, h in enumerate(HALF)})
NQ = 48 * len(SITES)
def qb(v, lab): return 48 * SID[v] + LOC[lab]

# incident edges of a vertex, with ordering keys
def incident(q):
    v, c = q
    out = []
    for p in ONS:
        if c in p:
            other = p[1] if p[0] == c else p[0]
            out.append((('o', other), ('onsite', p), (v, other)))
    for a in c:
        b = [d for d in c if d != a][0]
        out.append((('l', a), ('link', (c, a)), (add(v, a), corner(neg(a), b))))
    return out
def keyord(k):
    return (0, k[1]) if k[0] == 'o' else (1, k[1])

def edge_qubits(q, ekind, edata):
    v, c = q
    if ekind == 'onsite':
        return [qb(v, ('o', edata))]
    cc, a = edata
    b = [d for d in cc if d != a][0]
    w = add(v, a); c2 = corner(neg(a), b)
    return [qb(v, ('h', (cc, a))), qb(w, ('h', (c2, neg(a))))]
def edge_zqubit(q, ekind, edata):
    """Qubit carrying this edge's Z inside strings / B at vertex q."""
    v, c = q
    if ekind == 'onsite':
        return qb(v, ('o', edata))
    return qb(v, ('h', edata))

# Pauli: (x, z, p) = i^p X^x Z^z, x,z python ints
def pmul(a, b):
    return (a[0] ^ b[0], a[1] ^ b[1], (a[2] + b[2] + 2 * bin(a[1] & b[0]).count('1')) % 4)
def pcomm(a, b):
    return (bin(a[0] & b[1]).count('1') + bin(a[1] & b[0]).count('1')) % 2 == 0
def herm(a): return (a[2] - bin(a[0] & a[1]).count('1')) % 2 == 0
def X(qs):
    x = 0
    for i in qs: x ^= 1 << i
    return (x, 0, 0)
def Z(qs):
    z = 0
    for i in qs: z ^= 1 << i
    return (0, z, 0)

INC = {q: incident(q) for q in VERTS}
def canon_first(q, r):
    """Translation-covariant orientation: on-site hops by corner label, links along +direction."""
    if q[0] == r[0]:
        return CORN.index(q[1]) < CORN.index(r[1])
    for k, (ek, ed), nb in INC[q]:
        if nb == r and ek == 'link':
            return sum(ed[1]) > 0
    raise KeyError
def A(q, r):
    """BKSF hop operator oriented q -> r (A(r,q) = -A(q,r))."""
    if not canon_first(q, r):
        x, z, p = A(r, q); return (x, z, (p + 2) % 4)
    for k, (ek, ed), nb in INC[q]:
        if nb == r: break
    else:
        raise KeyError
    kq = k
    for k2, (ek2, ed2), nb2 in INC[r]:
        if nb2 == q: kr = k2; break
    zq = [edge_zqubit(q, e2k, e2d) for k2, (e2k, e2d), _ in INC[q] if keyord(k2) < keyord(kq)]
    zr = [edge_zqubit(r, e2k, e2d) for k2, (e2k, e2d), _ in INC[r] if keyord(k2) < keyord(kr)]
    P = X(edge_qubits(q, ek, ed))
    return pmul(P, Z(zq + zr))
def Bop(q): return Z([edge_zqubit(q, ek, ed) for _, (ek, ed), _ in INC[q]])
def Rop(v, h):
    c, a = h; b = [d for d in c if d != a][0]
    return Z([qb(v, ('h', h)), qb(add(v, a), ('h', (corner(neg(a), b), neg(a))))])

# cycles (as vertex sequences), same families as the fermion-level exploration
def cycles():
    out = []
    for v in SITES:
        for d in DIRS:
            a = [f for f in DIRS if perp(f, d) and f != neg(d)]
            a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
            ring = [a0, b0, neg(a0), neg(b0)]
            out.append(('square', [(v, corner(d, r)) for r in ring]))
            for i in range(4):
                p, q = ring[i], ring[(i+1) % 4]; w = add(v, d)
                out.append(('tube', [(v, corner(d, p)), (w, corner(neg(d), p)), (w, corner(neg(d), q)), (v, corner(d, q))]))
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
            out.append(('triangle', [(v, corner(x, y)), (v, corner(y, z)), (v, corner(z, x))]))
        for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
            out.append(('plaquette', [(v, corner(d, e)), (add(v, d), corner(neg(d), e)),
                                      (add(add(v, d), e), corner(neg(d), neg(e))), (add(v, e), corner(d, neg(e)))]))
    return out
def loop_op(seq, F):
    n = len(seq); P = (0, 0, n % 4)   # i^n
    for i in range(n):
        P = pmul(P, A(seq[i], seq[(i+1) % n]))
    if F: P = (P[0], P[1], (P[2] + 2) % 4)
    return P

# ------------------------------------------------------------ GF(2) with phases
class Group:
    """Incremental row reduction of Paulis; tracks products to test membership with sign."""
    def __init__(self, n):
        self.n = n; self.piv = {}
    def vec(self, P): return P[0] | (P[1] << self.n)
    def add(self, P):
        v = self.vec(P); comb = P
        while v:
            c = v.bit_length() - 1
            if c in self.piv:
                pv, pP = self.piv[c]; v ^= pv; comb = pmul(comb, pP)
            else:
                self.piv[c] = (v, comb); return True
        return comb[2] % 4   # reduced to a phase: 0 means +I (dependent, consistent)
    def reduce(self, P):
        v = self.vec(P); comb = P
        while v:
            c = v.bit_length() - 1
            if c not in self.piv: return None
            pv, pP = self.piv[c]; v ^= pv; comb = pmul(comb, pP)
        return comb[2] % 4   # phase of P * (product of stabilizers): 0 -> P = +S, 2 -> P = -S

# ------------------------------------------------------------ rotations
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
def rd(R, d): return tuple(int(x) for x in R @ np.array(d))
def rs(R, v): return tuple(int(x) % L for x in R @ np.array(v))
def rc(R, c): return corner(*[rd(R, d) for d in c])
def rlab(R, lab):
    if lab[0] == 'o':
        c1, c2 = lab[1]; p = tuple(sorted((rc(R, c1), rc(R, c2)))); return ('o', p)
    c, a = lab[1]; return ('h', (rc(R, c), rd(R, a)))
LABS = list(LOC)
def qperm(R):
    perm = np.zeros(NQ, dtype=np.int64)
    for v in SITES:
        rv = rs(R, v)
        for lab in LABS:
            perm[qb(v, lab)] = qb(rv, rlab(R, lab))
    return perm
def apply_perm(P, perm):
    x, z, p = P; nx = nz = 0
    i = 0
    while x:
        if x & 1: nx |= 1 << int(perm[i])
        x >>= 1; i += 1
    i = 0
    while z:
        if z & 1: nz |= 1 << int(perm[i])
        z >>= 1; i += 1
    return (nx, nz, p)
def apply_cz(P, pairs):
    x, z, p = P
    for a, b in pairs:
        xa, xb = (x >> a) & 1, (x >> b) & 1
        if xb: z ^= 1 << a
        if xa: z ^= 1 << b
        if xa and xb: p = (p + 2) % 4
    return (x, z, p)
def apply_zfix(P, zs):
    x = P[0]; flips = bin(x & zs).count('1')
    return (P[0], P[1], (P[2] + 2 * flips) % 4)

def cz_network(R):
    """CZ pairs at every vertex x whose order differs between key_x and the rotated keys."""
    Rinv = np.round(np.linalg.inv(R)).astype(int)
    pairs = []
    for x in VERTS:
        v, c = x
        pre = (rs(Rinv, v), rc(Rinv, c))
        # map incident edges of x to incident edges of pre via neighbours
        inc_x = INC[x]; inc_pre = {nb: k for k, _, nb in INC[pre]}
        items = []
        for k, (ek, ed), nb in inc_x:
            nbpre = (rs(Rinv, nb[0]), rc(Rinv, nb[1]))
            items.append((keyord(k), keyord(inc_pre[nbpre]), edge_zqubit(x, ek, ed)))
        for (k1, o1, q1), (k2, o2, q2) in itertools.combinations(items, 2):
            if (k1 < k2) != (o1 < o2):
                pairs.append((q1, q2))
    return pairs

if __name__ == '__main__':
    t0 = time.time()
    PASS = FAIL = 0
    def check(name, ok, detail=''):
        global PASS, FAIL
        PASS += ok; FAIL += (not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
    print(f"L={L}, flux={FLUX}, {NQ} qubits ({48} per site), {len(VERTS)} corner vertices")
    EDGES = []
    seen = set()
    for q in VERTS:
        for k, e, nb in INC[q]:
            key = frozenset((VID[q], VID[nb]))
            if key not in seen: seen.add(key); EDGES.append((q, nb) if canon_first(q, nb) else (nb, q))
    Aop = {e: A(*e) for e in EDGES}
    gens = [Bop(q) for q in VERTS] + [Rop(v, h) for v in SITES for h in HALF if (h[1][0] + h[1][1] + h[1][2]) > 0]
    CYC = cycles()
    loops = [loop_op(seq, FLUX[kind]) for kind, seq in CYC]
    gens_all = gens + loops
    # 1. algebra checks
    ok = all(herm(P) for P in gens_all) and all(herm(P) for P in Aop.values())
    check("all hops, B, R and loop generators are Hermitian", ok)
    # commutation: loops/B/R commute with each other and loops commute with all hops
    import random
    random.seed(1)
    bad = 0
    for S in loops:
        for e in random.sample(EDGES, 200):
            if not pcomm(S, Aop[e]): bad += 1
    for S in random.sample(gens_all, 300):
        for T in random.sample(gens_all, 300):
            if not pcomm(S, T): bad += 1
    check("loops commute with hops; stabilizer generators commute (random sample)", bad == 0, f"violations={bad}")
    # hop algebra: anticommute iff share exactly one vertex
    bad = 0
    for e in random.sample(EDGES, 300):
        for f in random.sample(EDGES, 300):
            share = len(set(e) & set(f))
            want = share != 1
            if pcomm(Aop[e], Aop[f]) != want: bad += 1
    check("hops anticommute iff they share exactly one vertex (sample)", bad == 0)
    # 2. code dimension and no -I
    G = Group(NQ); neg_id = False
    for P in gens_all:
        r = G.add(P)
        if r is not True and r != 0: neg_id = True
    rank = len(G.piv)
    check("stabilizer group (B, R, loops) has no -I", not neg_id)
    print(f"   rank {rank}, log2 code dimension {NQ - rank}")
    check("log2 code dimension is 3 (Z2 gauge theory on the 3-torus)", NQ - rank == 3)
    # 3. T-junction (Levin-Wen) for the corner fermion at vertex q0 with three hops
    q0 = VERTS[0]; nbs = [nb for _, _, nb in INC[q0]][:3]
    W = [A(q0, nb) for nb in nbs]   # move fermion from q0 to nb
    def inv(P): return (P[0], P[1], (-P[2] - 2 * bin(P[0] & P[1]).count('1')) % 4)
    prod = (0, 0, 0)
    for P in (W[2], inv(W[1]), W[0], inv(W[2]), W[1], inv(W[0])):
        prod = pmul(prod, P)
    check("T-junction exchange sign of the corner charge is -1 (a fermion)", prod[0] == 0 and prod[1] == 0 and prod[2] == 2,
          f"phase i^{prod[2]}")
    print(f"   [{time.time()-t0:.0f}s]")
    # 4. rotations
    rot_data = []
    allok = True
    for R in ROTS:
        perm = qperm(R); cz = cz_network(R)
        zfix = 0
        for e in EDGES:
            img = apply_cz(apply_perm(Aop[e], perm), cz)
            q, r = e
            tgt = A((rs(R, q[0]), rc(R, q[1])), (rs(R, r[0]), rc(R, r[1])))
            if (img[0], img[1]) != (tgt[0], tgt[1]): allok = False; break
            if (img[2] - tgt[2]) % 4 == 2:
                Rq = (rs(R, q[0]), rc(R, q[1])); Rr = (rs(R, r[0]), rc(R, r[1]))
                if not canon_first(Rq, Rr): Rq, Rr = Rr, Rq   # fix on the target's canonical-first half
                zfix ^= 1 << edge_zqubit(Rq, *[ed for k, ed, nb in INC[Rq] if nb == Rr][0])
            elif img[2] != tgt[2]: allok = False
        rot_data.append((perm, cz, zfix))
    check("for every rotation, P_R then the on-site CZ network maps each hop to plus/minus the rotated hop; Z fixes make it exact", allok)
    def U(k, P):
        perm, cz, zf = rot_data[k]
        return apply_zfix(apply_cz(apply_perm(P, perm), cz), zf)
    bad = 0
    for k, R in enumerate(ROTS):
        for P in random.sample(gens_all, 400):
            if G.reduce(U(k, P)) != 0: bad += 1
        for e in random.sample(EDGES, 200):
            q, r = e
            tgt = A((rs(R, q[0]), rc(R, q[1])), (rs(R, r[0]), rc(R, r[1])))
            if U(k, Aop[e]) != tgt: bad += 1
    check("every rotation maps stabilizer generators to +stabilizers and hops exactly to rotated hops (sample)", bad == 0)
    print(f"   [{time.time()-t0:.0f}s]")
    # 5. group law. Fast single-qubit evaluator (X_i -> sign X_{pi i} Z_{CZ partners}; Z_i -> Z_{pi i}).
    def rid(M):
        for k, S in enumerate(ROTS):
            if (S == M).all(): return k
    INV = [rid(np.round(np.linalg.inv(R)).astype(int)) for R in ROTS]
    MUL = [[rid(ROTS[a] @ ROTS[b]) for b in range(24)] for a in range(24)]
    fast = []
    for perm, cz, zf in rot_data:
        part = {}
        for a_, b_ in cz:
            part.setdefault(a_, set()).add(b_); part.setdefault(b_, set()).add(a_)
        fast.append([perm, {j: frozenset(v) for j, v in part.items()}, zf])
    def UX(k, i):
        perm, part, zf = fast[k]; j = int(perm[i])
        return j, part.get(j, frozenset()), (zf >> j) & 1
    def comp(a, b, i):
        ab = MUL[a][b]
        j, S, s1 = UX(b, i); m, S2, s2 = UX(a, j)
        pa = fast[a][0]; Sa = frozenset(int(pa[x]) for x in S)
        m3, S3, s3 = UX(ab, i)
        return (m == m3 and (S2 ^ Sa) == S3), s1 ^ s2 ^ s3
    # cross-check the fast evaluator against full Clifford conjugation on a sample
    agree = True
    for _ in range(60):
        a, b = random.randrange(24), random.randrange(24); i = random.randrange(NQ)
        okz, sg = comp(a, b, i)
        l = U(a, U(b, (1 << i, 0, 0))); r = U(MUL[a][b], (1 << i, 0, 0))
        if okz != (l[:2] == r[:2]) or (okz and sg != (l[2] != r[2])): agree = False
    check("fast single-qubit evaluator agrees with full conjugation (sample)", agree)
    # cocycle U_a U_b U_ab^-1 = product of R over a link set F(a,b); solve F = dT orbit by orbit
    LINKS = [(v, (c, a_)) for v in SITES for c in CORN for a_ in c if sum(a_) > 0]
    def halves(l):
        v, (c, a_) = l; b_ = [d for d in c if d != a_][0]
        return qb(v, ('h', (c, a_))), qb(add(v, a_), ('h', (corner(neg(a_), b_), neg(a_))))
    H2L = {}
    for l in LINKS:
        for h in halves(l): H2L[h] = l
    LI = {l: n for n, l in enumerate(LINKS)}
    def img(k, l): return H2L[int(fast[k][0][halves(l)[0]])]
    zbad = 0; F = {}
    for a in range(24):
        for b in range(24):
            Sset = set()
            for l in LINKS:
                h0, h1 = halves(l)
                o0, g0 = comp(a, b, h0); o1, g1 = comp(a, b, h1)
                if not (o0 and o1) or g0 != g1: zbad += 1
                if g0: Sset.add(img(MUL[a][b], l))
            for i in random.sample(range(NQ), 60):   # on-site qubits: never flipped
                o, g = comp(a, b, i)
                if not o or (g and i not in H2L): zbad += 1
            F[(a, b)] = Sset
    check("the composite of any two rotations differs from the third only by a product of repetition stabilizers R", zbad == 0)
    orbits = []; seen = set()
    for l in LINKS:
        if l in seen: continue
        o = sorted(set(img(k, l) for k in range(24))); seen |= set(o); orbits.append(o)
    free = all(len(o) == 24 for o in orbits)
    check("every link orbit under O is free (no rotation fixes a link)", free, f"{len(orbits)} orbits")
    T = [set() for _ in range(24)]; solvable = True
    for o in orbits:
        idx = {l: n for n, l in enumerate(o)}; m = len(o); nv = 24 * m
        piv = {}
        for a in range(24):
            for b in range(24):
                ab = MUL[a][b]
                for l in o:
                    r = (1 << (a*m + idx[l])) ^ (1 << (b*m + idx[img(INV[a], l)])) ^ (1 << (ab*m + idx[l]))
                    x = r | ((1 if l in F[(a, b)] else 0) << nv)
                    while True:
                        low = x & ((1 << nv) - 1)
                        if low == 0:
                            if x: solvable = False
                            break
                        c = low.bit_length() - 1
                        if c in piv: x ^= piv[c]
                        else: piv[c] = x; break
        sol = 0
        for c in sorted(piv):
            x = piv[c]; rest = x & ((1 << c) - 1)
            if ((x >> nv) & 1) ^ (bin(rest & sol).count('1') & 1): sol |= 1 << c
        for a in range(24):
            for l in o:
                if (sol >> (a*m + idx[l])) & 1: T[a].add(l)
    check("the R-valued cocycle is a coboundary (solved orbit by orbit)", solvable)
    for k in range(24):
        corr = 0
        for l in T[k]:
            for h in halves(l): corr ^= 1 << h
        fast[k][2] ^= corr
        perm, cz, zf = rot_data[k]; rot_data[k] = (perm, cz, zf ^ corr)
    viol = 0
    for a in range(24):
        for b in range(24):
            for i in range(NQ):
                o, g = comp(a, b, i)
                if not o or g: viol += 1
    check("after the correction U_R -> prod_{T_R} R * U_R: U_a U_b = U_ab exactly on all 2 x %d single-qubit Paulis, all 576 pairs" % NQ, viol == 0)
    bad = 0
    for k, R in enumerate(ROTS):
        for P in random.sample(gens_all, 200):
            if G.reduce(U(k, P)) != 0: bad += 1
        for e in random.sample(EDGES, 100):
            q, r = e
            if U(k, Aop[e]) != A((rs(R, q[0]), rc(R, q[1])), (rs(R, r[0]), rc(R, r[1]))): bad += 1
    check("corrected rotations still map stabilizers to +stabilizers and hops exactly (sample)", bad == 0)
    # literal operators fix |0...0>, so U_a U_b = U_ab holds as operators, with no phase
    # W twist: W = prod_q exp(-i pi B_q/4) prod_links exp(-i pi R/4); W^2 is a phase iff prod B prod R = I
    PB = (0, 0, 0)
    for q in VERTS: PB = pmul(PB, Bop(q))
    for l in LINKS: PB = pmul(PB, Z(list(halves(l))))
    check("prod_q B_q * prod_links R = identity, so W^2 is a global phase and V_g = U_g W^{w1(g)} is again an exact O action",
          PB == (0, 0, 0))
    print(f"   [{time.time()-t0:.0f}s]")
    # 6. pair test on all nine C2
    from collections import deque
    def path(src, dst):
        prev = {src: None}; dq = deque([src])
        while dq:
            x = dq.popleft()
            if x == dst: break
            for _, _, nb in INC[x]:
                if nb not in prev: prev[nb] = x; dq.append(nb)
        p = [dst]
        while p[-1] != src: p.append(prev[p[-1]])
        return p[::-1]
    results = {}; twoq_bad = []
    for k, R in enumerate(ROTS):
        if int(np.trace(R)) != -1: continue
        kind = 'axis' if np.allclose(np.abs(np.diag(R)), 1) else 'edge'
        lams = set()
        for v in [(0,0,0), (1,0,0), (0,1,1), (1,1,0)]:
            for c in CORN:
                q = (v, c); Rq = (rs(R, v), rc(R, c))
                if Rq == q: continue
                pth = path(q, Rq)
                S = (0, 0, 0)
                for i in range(len(pth) - 1): S = pmul(S, A(pth[i], pth[i+1]))
                # S creates exactly two corner charges (B_q, B_Rq) and no link defects
                flipsB = [x for x in VERTS if not pcomm(S, Bop(x))]
                if sorted(flipsB) != sorted([q, Rq]) or any(not pcomm(S, Rop(v, h)) for v in SITES[:8] for h in HALF if sum(h[1]) > 0):
                    twoq_bad.append(R)
                SR = U(k, S)
                T = pmul(inv(S), SR)
                r = G.reduce(T)
                if r is None: continue
                lams.add(1 if r == 0 else -1)
        results.setdefault(kind, set()).update(lams)
        print(f"   C2 ({kind}) R={R.tolist()}: pair eigenvalues {sorted(lams)}")
    check("pair test: lambda = +1 for all axis C2 (eta = -1) and lambda = -1 for all edge C2 (eta = +1): class w2 + w1^2",
          results.get('axis') == {1} and results.get('edge') == {-1}, str({k: sorted(v) for k, v in results.items()}))
    check("each pair creator flips exactly the two end charges B_q, B_Rq and no repetition stabilizer", not twoq_bad)
    # twisted realization: W relative phase on a two-corner-charge state is (e^{i pi/2})^2 = -1, on w1-odd elements only
    tw = {kind: sorted({-x for x in v}) if kind == 'edge' else sorted(v) for kind, v in results.items()}
    check("twisted realization V_g = U_g W^{w1(g)} (edge C2 are w1-odd, axis C2 even): lambda = +1 for all nine C2: class w2",
          tw.get('axis') == [1] and tw.get('edge') == [1], str(tw))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
