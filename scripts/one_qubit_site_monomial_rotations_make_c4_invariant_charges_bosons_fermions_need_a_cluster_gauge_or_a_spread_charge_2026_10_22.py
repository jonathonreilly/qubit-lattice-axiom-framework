AUDIT_INPUT_PATHS = ('docs/ONE_QUBIT_SITE_MONOMIAL_ROTATIONS_MAKE_C4_INVARIANT_CHARGES_BOSONS_FERMIONS_NEED_A_CLUSTER_GAUGE_OR_A_SPREAD_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Rotation-covariant emergent fermions on one qubit per site: a lattice spin-statistics test.

Setting: commuting Pauli stabilizer codes on qubits at the sites of Z^3 (one qubit per
site). A rotation R acts MONOMIALLY if it moves each site's qubit to the image site with
at most a single-site Clifford (and a Pauli frame / phase). Exact results checked here:

A. Involution lemma: for any Pauli P and monomial involution s,
   omega(P, sP) = sum over FIXED sites of omega(P_x, c_x P_x).  Every hom O -> S3 and
   C4 -> S3 kills the axis C2, so an axis C2 (square of a C4 fixing its axis pointwise)
   acts label-trivially on its fixed sites: omega(P, R P) = 0 for EVERY Pauli P.
B. Exact identity theta = lambda_R * sigma_R for a C2 R preserving the code and the
   charge's local excitation (lambda_R = [T1, R T1], sigma_R = [T1, T3 R(T3)], T3 on the
   axis); if R = Q^2 with a C4 Q preserving the excitation, sigma_R = +1 (proof in note).
   Checked on a D3-invariant BKSF code (bare permutation, edge C2): theta = -1,
   lambda = +1, sigma = -1.
C. Corollary: monomial + C4-invariant charge => lambda = sigma = +1 => BOSON. A
   rotation-covariant fermion needs a non-monomial (cluster) action, or a charge whose
   excitation is not C4-invariant (spread over a shell, sigma = -1), or non-Pauli terms.
D. Positive composite model: one qubit per fine site, coarse vertices 3Z^3, the 6 arm
   sites of each vertex carry 12 Majoranas (Jordan-Wigner inside the 7-site star),
   B = Z on the 6 arms, R = ZZ on fine nearest-neighbour arm pairs, S = BKSF plaquettes:
   commuting, log2 dim 3, theta = -1, all 24 rotations preserve the code when they act
   by a star-local Majorana permutation (non-monomial); lambda(axis C2) = -1 there.
Seeded; exact GF(2) arithmetic with Python integers; no dense matrices.
"""
import itertools
import random
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
random.seed(20261022)
NP = 0
NF = 0


def check(tag, ok, msg, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}" + (f" | {detail}" if detail else ""))


def comm(p, q):
    """+1 if the (x, z) bitmask Paulis commute, -1 if they anticommute."""
    return -1 if bin((p[0] & q[1]) ^ (p[1] & q[0])).count("1") % 2 else 1


def bits(v):
    while v:
        b = v & -v
        yield b.bit_length() - 1
        v ^= b


def mul(p, q):
    return (p[0] ^ q[0], p[1] ^ q[1])


class Span:
    def __init__(self, n):
        self.n = n
        self.basis = {}

    def reduce(self, p):
        v = p[0] | (p[1] << self.n)
        while v:
            h = v.bit_length() - 1
            if h in self.basis:
                v ^= self.basis[h]
            else:
                return v
        return 0

    def add(self, p):
        v = self.reduce(p)
        if v:
            self.basis[v.bit_length() - 1] = v
            return True
        return False


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            m = np.zeros((3, 3), int)
            for i in range(3):
                m[perm[i], i] = sg[i]
            if round(np.linalg.det(m)) == 1:
                out.append(m)
    return out


ROTS = rotations()


def rot_from_axis_angle(n, k):
    """proper cube rotation matrix by angle 2pi/k about integer axis n (search ROTS)."""
    n = np.array(n)
    for m in ROTS:
        if np.array_equal(m @ n, n):
            order = next(j for j in range(1, 5) if np.array_equal(np.linalg.matrix_power(m, j), np.eye(3, dtype=int)))
            if order == k:
                return m
    raise ValueError


C2z = rot_from_axis_angle((0, 0, 1), 2)
C4z = rot_from_axis_angle((0, 0, 1), 4)
C3d = rot_from_axis_angle((1, 1, 1), 3)
C2e = rot_from_axis_angle((1, -1, 0), 2)
C2f = rot_from_axis_angle((1, 1, 0), 2)
AXIS_C2 = [m for m in ROTS if np.trace(m) == -1 and any(np.array_equal(m @ v, v) for v in np.eye(3, dtype=int))]

# ------------------------------------------------------------------- A. lemma
print("== A. involution lemma and label triviality of axis C2 (one qubit per site)")
SP2 = [np.array(m) for m in itertools.product((0, 1), repeat=4)]
SP2 = [m.reshape(2, 2) for m in SP2 if (m[0] * m[3] + m[1] * m[2]) % 2 == 1]
INV = {i: next(j for j, b in enumerate(SP2) if np.array_equal((SP2[i] @ b) % 2, np.eye(2, dtype=int))) for i in range(6)}
INVOL = [i for i in range(6) if INV[i] == i]


def om(a, b):
    return (a[0] * b[1] + a[1] * b[0]) % 2


bad = 0
for trial in range(3000):
    n = random.randint(1, 10)
    sites = list(range(n))
    random.shuffle(sites)
    perm = list(range(n))
    M = [None] * n
    k = random.randint(0, n // 2)
    for t in range(k):
        a, b = sites[2 * t], sites[2 * t + 1]
        perm[a], perm[b] = b, a
        i = random.randrange(6)
        M[a], M[b] = i, INV[i]
    fixed = [s for s in range(n) if perm[s] == s]
    for s in fixed:
        M[s] = random.choice(INVOL)
    P = [np.array([random.randint(0, 1), random.randint(0, 1)]) for _ in range(n)]
    sP = [None] * n
    for s in range(n):
        sP[perm[s]] = (SP2[M[s]] @ P[s]) % 2
    lhs = sum(om(P[s], sP[s]) for s in range(n)) % 2
    rhs = sum(om(P[s], (SP2[M[s]] @ P[s]) % 2) for s in fixed) % 2
    bad += lhs != rhs
check("A1 [T]", bad == 0,
      "omega(P, sP) = sum over fixed sites of omega(P_x, c_x P_x) for every monomial involution "
      "(swapped pairs cancel); with no relabelling on fixed sites, P and sP COMMUTE",
      f"3000 seeded instances, mismatches {bad}")


def key(m):
    return tuple(m.flatten())


S3 = list(itertools.permutations(range(3)))


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


homs = []
for a, b in itertools.product(S3, repeat=2):
    img = {key(np.eye(3, dtype=int)): (0, 1, 2)}
    frontier = [np.eye(3, dtype=int)]
    ok = True
    while frontier and ok:
        g = frontier.pop()
        for gen, im in ((C4z, a), (C3d, b)):
            h = g @ gen
            v = compose(img[key(g)], im)
            if key(h) in img:
                ok &= img[key(h)] == v
            else:
                img[key(h)] = v
                frontier.append(h)
    if ok and len(img) == 24:
        homs.append(img)
kill = all(h[key(m)] == (0, 1, 2) for h in homs for m in AXIS_C2)
c4sq = all(compose(x, x) == (0, 1, 2) for x in S3 if compose(compose(x, x), compose(x, x)) == (0, 1, 2))
edge_nontriv = sum(h[key(C2f)] != (0, 1, 2) for h in homs)
check("A2 [T]", len(homs) == 10 and kill and c4sq,
      "all 10 homs O -> S3 = Sp(2,2) (single-qubit Cliffords mod Paulis) send the 3 axis C2 to the "
      "identity, and every hom C4 -> S3 kills the square: an axis C2 never relabels a site of its "
      "axis (each such site is fixed by the whole C4); edge C2 can (soldering freedom)",
      f"homs {len(homs)}, axis C2 trivial in all: {kill}; homs moving an edge C2: {edge_nontriv}")

STAR = [(0, 0, 0)] + [tuple(int(c) for c in s * np.eye(3, dtype=int)[a]) for a in range(3) for s in (1, -1)]
SIDX = {p: i for i, p in enumerate(STAR)}


def star_counts(Rm, cen_label):
    perm = [SIDX[tuple(int(c) for c in Rm @ np.array(p))] for p in STAR]
    cnt = 0
    for P in itertools.product(range(4), repeat=7):
        tot = 0
        for s in range(7):
            ps = np.array([P[s] & 1, P[s] >> 1])
            if perm[s] == s:
                img = (SP2[cen_label] @ ps) % 2 if s == 0 else ps
                tot += om(ps, img)
        cnt += tot % 2
    return cnt


lab_id = next(i for i in range(6) if np.array_equal(SP2[i], np.eye(2, dtype=int)))
lab_h = next(i for i in INVOL if i != lab_id)
cz = star_counts(C2z, lab_id)
ce = star_counts(C2f, lab_h)
check("A3 [T]", cz == 0 and ce > 0,
      "on the 7-site star: no Pauli anticommutes with its axis-C2 image under any monomial action, so "
      "six mutually anticommuting 'Majorana per direction' operators permuted by O cannot exist at one "
      "qubit per site (gamma_+a and gamma_-a are swapped by an axis C2); an edge C2 with a relabelled "
      "centre does allow anticommuting pairs",
      f"anticommuting (P, RP): axis C2 {cz}/16384, edge C2 with centre relabel {ce}/16384")

# --------------------------------------------- B. identity on a BKSF code
print("== B. exact identity theta = lambda * sigma on a fermionic code (BKSF, bare permutation)")
DIRS = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]


def add(v, a, s, L):
    w = list(v)
    w[a] = (w[a] + s) % L
    return tuple(w)


def bksf(L, order):
    idx = {}
    for v in itertools.product(range(L), repeat=3):
        for a in range(3):
            idx[(v, a)] = len(idx)
    rank = {d: order.index(d) for d in DIRS}

    def inc(j):
        return {(a, 1): (j, a) for a in range(3)} | {(a, -1): (add(j, a, -1, L), a) for a in range(3)}
    A = {}
    for (v, a), i in idx.items():
        k = add(v, a, 1, L)
        z = 0
        for j, dj in ((v, (a, 1)), (k, (a, -1))):
            for d, e in inc(j).items():
                if rank[d] < rank[dj]:
                    z ^= 1 << idx[e]
        A[(v, a)] = (1 << i, z)
    B = {j: (0, sum(1 << idx[e] for e in inc(j).values())) for j in itertools.product(range(L), repeat=3)}
    S = []
    for v in itertools.product(range(L), repeat=3):
        for a, b in ((0, 1), (1, 2), (0, 2)):
            p = (0, 0)
            for e in ((v, a), (add(v, a, 1, L), b), (add(v, b, 1, L), a), (v, b)):
                p = mul(p, A[e])
            S.append(p)
    return idx, A, B, S


def rot_edge(e, Rm, L):
    v, a = e
    vv = tuple(int(c) % L for c in Rm @ np.array(v))
    d = Rm[:, a]
    b = int(np.nonzero(d)[0][0])
    return (vv, b) if d[b] == 1 else (add(vv, b, -1, L), b)


EMAP = {}


def rot_bare_edges(p, Rm, idx, L):
    kk = (L, key(Rm))
    if kk not in EMAP:
        inv = {i: e for e, i in idx.items()}
        EMAP[kk] = [idx[rot_edge(inv[i], Rm, L)] for i in range(len(inv))]
    em = EMAP[kk]
    x = z = 0
    for i in bits(p[0] | p[1]):
        ne = em[i]
        x |= (p[0] >> i & 1) << ne
        z |= (p[1] >> i & 1) << ne
    return (x, z)


def invariant(gens, Rms, idx, L):
    sp = Span(len(idx))
    for g in gens:
        sp.add(g)
    return all(sp.reduce(rot_bare_edges(g, Rm, idx, L)) == 0 for Rm in Rms for g in gens)


Ls = 4
found = None
for order in itertools.permutations(DIRS):
    idx, A, B, S = bksf(Ls, list(order))
    gens = list(B.values()) + S
    if invariant(gens, (C3d, C2e), idx, Ls):
        found = list(order)
        break
L = 14
idx, A, B, S = bksf(L, found)
gens = list(B.values()) + S
d3 = invariant(gens, (C3d, C2e), idx, L)
o = (0, 0, 0)


def path(steps, L):
    v, p = o, (0, 0)
    for a, s in steps:
        e = (v, a) if s == 1 else (add(v, a, -1, L), a)
        p = mul(p, A[e])
        v = add(v, a, s, L)
    return p, v


T1, _ = path([(2, 1)] * 6, L)
T3, F3 = path([(0, 1), (1, -1)] * 6, L)
RS = [rot_bare_edges(g, C2e, idx, L) for g in S]
LOC = list(B.values()) + S + RS
INVE = {i: e for e, i in idx.items()}


def cdist(u, v):
    return max(min((a - b) % L, (b - a) % L) for a, b in zip(u, v))


def near(p, r):
    """edge qubits with both endpoints within L-inf distance r of vertex p"""
    return [i for i, (v, a) in INVE.items() if cdist(v, p) <= r and cdist(add(v, a, 1, L), p) <= r]


def gens_near(p, r):
    """generators touching an edge with an endpoint within L-inf distance r of p"""
    out = []
    for g in LOC:
        sup = [INVE[i] for i in bits(g[0] | g[1])]
        if any(cdist(v, p) <= r or cdist(add(v, a, 1, L), p) <= r for v, a in sup):
            out.append(g)
    return out


def solve_dressing(T, conds, qubits):
    """find D on `qubits` with omega(T D, h) = rhs for each (h, rhs); returns T D or None."""
    rows = []
    m = len(qubits)
    for h, rhs in conds:
        row = 0
        for k, q in enumerate(qubits):
            if h[1] >> q & 1:
                row |= 1 << k          # D_x * h_z
            if h[0] >> q & 1:
                row |= 1 << (m + k)    # D_z * h_x
        b = (1 if comm(T, h) == -1 else 0) ^ rhs
        rows.append((row, b))
    piv = {}
    for row, b in rows:
        while row:
            hb = row.bit_length() - 1
            if hb in piv:
                row ^= piv[hb][0]
                b ^= piv[hb][1]
            else:
                piv[hb] = (row, b)
                break
        if not row and b:
            return None
    sol = 0
    for hb in sorted(piv):
        row, b = piv[hb]
        rest = row & ~(1 << hb)
        if bin(rest & sol).count("1") % 2 != b:
            sol |= 1 << hb
    x = z = 0
    for k, q in enumerate(qubits):
        x |= (sol >> k & 1) << q
        z |= (sol >> (m + k) & 1) << q
    return mul(T, (x, z))


def symdiff(h, g):
    return (h[0] ^ g[0], h[1] ^ g[1])


Q0, G0 = near(o, 2), gens_near(o, 3)
QF, GF = near(F3, 2), gens_near(F3, 3)
# T1': R-invariant excitation at the junction: omega(T1', g) = omega(T1', R g) for local g
T1d = solve_dressing(T1, [(symdiff(g, rot_bare_edges(g, C2e, idx, L)), 0) for g in G0], Q0)
T2d = rot_bare_edges(T1d, C2e, idx, L) if T1d else None
conds = [(g, 1 if comm(T1d, g) == -1 else 0) for g in G0] + \
        [(symdiff(g, rot_bare_edges(g, C2e, idx, L)), 0) for g in GF]
T3d = solve_dressing(T3, conds, Q0 + QF) if T1d else None
ok_solve = T1d is not None and T3d is not None
if ok_solve:
    RT3 = rot_bare_edges(T3d, C2e, idx, L)
    S3 = mul(T3d, RT3)
    zero_syn = all(comm(S3, g) == 1 for g in LOC)
    same0 = all(comm(T1d, g) == comm(T2d, g) == comm(T3d, g) for g in G0)
    far = [g for g in LOC if g not in G0 and g not in GF]
    clean = all(comm(T1d, g) == comm(T1, g) and comm(T3d, g) == comm(T3, g) for g in far)
    same0 = same0 and clean
    theta = comm(T1d, T2d) * comm(T1d, T3d) * comm(T2d, T3d)
    lam = comm(T1d, T2d)
    sig = comm(T1d, S3)
    fermi = comm(T1, path([(2, -1)] * 6, L)[0]) * comm(T1, T3) * comm(path([(2, -1)] * 6, L)[0], T3)
else:
    zero_syn = same0 = False
    theta = lam = sig = fermi = 0
check("B1 [T]", found is not None and d3 and ok_solve and zero_syn and same0,
      "a D3-invariant BKSF ordering exists (C3 about (1,1,1) and the edge C2 about (1,-1,0) act as bare "
      "qubit permutations); local dressings (GF(2) solve) give legs whose junction excitation is "
      "C2-invariant, and T3^-1 R(T3) has zero syndrome",
      f"ordering {[('xyz'[a] + ('+' if s > 0 else '-')) for a, s in found]}, L={L}, axis leg to {F3}")
check("B2 [T]", fermi == -1 and theta == -1 and lam == 1 and sig == -1 and theta == lam * sig,
      "fermion (bare-hop T-junction -1; dressed legs -1) with lambda = [T1, R T1] = +1 (no qubit on the "
      "edge-C2 axis: lemma) and axis sign sigma = [T1, T3 R(T3)] = -1: theta = lambda * sigma exactly; "
      "the axis sign carries the statistics (spinorial edge C2, cf. main bare-permutation note)",
      f"theta bare {fermi:+d}, dressed {theta:+d}, lambda {lam:+d}, sigma {sig:+d}")

# ------------------------------------------------- D. composite rung-3 model
print("== D. composite model: one qubit per fine site, 7-site stars at 3Z^3, star-local Majoranas")
MAJ = []
for k in range(6):
    zlow = sum(1 << j for j in range(k))
    MAJ.append((1 << k, zlow))
    MAJ.append((1 << k, zlow | (1 << k)))
TAB = {}
for m in range(4096):
    p = (0, 0)
    for b in range(12):
        if m >> b & 1:
            p = mul(p, MAJ[b])
    TAB[m] = p
INVTAB = {p: m for m, p in TAB.items()}


def model(L):
    N = 3 * L
    n = N ** 3

    def site(p):
        return ((p[0] % N) * N + p[1] % N) * N + p[2] % N
    verts = [tuple(3 * c for c in v) for v in itertools.product(range(L), repeat=3)]

    def arm(V, k):
        a, s = DIRS[k]
        p = list(V)
        p[a] += s
        return site(p)
    arms = {V: [arm(V, k) for k in range(6)] for V in verts}
    armset = {s for V in verts for s in arms[V]}

    def starp(V, m):
        x6, z6 = TAB[m]
        x = z = 0
        for k, s in enumerate(arms[V]):
            x |= (x6 >> k & 1) << s
            z |= (z6 >> k & 1) << s
        return (x, z)

    def nb(V, a, s):
        w = list(V)
        w[a] = (w[a] + 3 * s) % N
        return tuple(w)

    def Aop(V, a):
        return mul(starp(V, 1 << (2 * DIRS.index((a, 1)))), starp(nb(V, a, 1), 1 << (2 * DIRS.index((a, -1)))))
    Bs = [(0, sum(1 << s for s in arms[V])) for V in verts]
    Rs = [(0, (1 << arms[V][DIRS.index((a, 1))]) | (1 << arms[nb(V, a, 1)][DIRS.index((a, -1))])) for V in verts for a in range(3)]
    Ss = []
    for V in verts:
        for a, b in ((0, 1), (1, 2), (0, 2)):
            p = (0, 0)
            for q in (Aop(V, a), Aop(nb(V, a, 1), b), Aop(nb(V, b, 1), a), Aop(V, b)):
                p = mul(p, q)
            Ss.append(p)
    Fz = [(0, 1 << s) for s in range(n) if s not in armset]
    return dict(N=N, n=n, site=site, verts=verts, arms=arms, armset=armset, starp=starp, A=Aop,
                B=Bs, R=Rs, S=Ss, F=Fz, nb=nb)


def code_dim(md):
    sp = Span(md["n"])
    r = sum(sp.add(g) for g in md["F"] + md["B"] + md["R"] + md["S"])
    return md["n"] - r, sp


def rot_dir(k, Rm):
    a, s = DIRS[k]
    v = s * Rm[:, a]
    b = int(np.nonzero(v)[0][0])
    return DIRS.index((b, int(v[b])))


def rot_maj(p, Rm, md):
    """rotation about the origin vertex acting by a star-local Majorana permutation."""
    N, site = md["N"], md["site"]
    x = z = 0
    for s in bits(p[0] | p[1]):
        if s in md["armset"]:
            continue
        bx, bz = p[0] >> s & 1, p[1] >> s & 1
        if True:
            c = (s // (N * N), (s // N) % N, s % N)
            t = site(tuple(int(u) for u in Rm @ np.array(c)))
            x |= bx << t
            z |= bz << t
    for V in md["verts"]:
        x6 = z6 = 0
        for k, s in enumerate(md["arms"][V]):
            x6 |= (p[0] >> s & 1) << k
            z6 |= (p[1] >> s & 1) << k
        if not (x6 or z6):
            continue
        m = INVTAB[(x6, z6)]
        m2 = 0
        for b in range(12):
            if m >> b & 1:
                m2 |= 1 << (2 * rot_dir(b // 2, Rm) + (b & 1))
        RV = tuple(int(u) % N for u in Rm @ np.array(V))
        q = md["starp"](RV, m2)
        x ^= q[0]
        z ^= q[1]
    return (x, z)


def rot_bare(p, Rm, md):
    N, site = md["N"], md["site"]
    x = z = 0
    for s in bits(p[0] | p[1]):
        bx, bz = p[0] >> s & 1, p[1] >> s & 1
        if True:
            c = (s // (N * N), (s // N) % N, s % N)
            t = site(tuple(int(u) for u in Rm @ np.array(c)))
            x |= bx << t
            z |= bz << t
    return (x, z)


m3 = model(3)
k3, sp3 = code_dim(m3)
m4 = model(4)
k4, _ = code_dim(m4)
gB, gR, gS = m3["B"], m3["R"], m3["S"]
allc = all(comm(p, q) == 1 for p in gB + gR + gS for q in gB + gR + gS)
check("D1 [T]", allc and k3 == 3 and k4 == 3,
      "B (Z on the 6 fine neighbours of a coarse-vertex site), R (ZZ on fine nearest-neighbour arm pairs), "
      "S (BKSF plaquettes on 4 stars) and single-site Z on idle sites all commute; torus log2 dim 3 = b1(T^3)",
      f"commute {allc}; log2 dim coarse L=3: {k3}, L=4: {k4} (fine qubits {m3['n']}, {m4['n']})")
N3 = m3["N"]


def fd(a, b):
    ca = (a // (N3 * N3), (a // N3) % N3, a % N3)
    cb = (b // (N3 * N3), (b // N3) % N3, b % N3)
    return sum(min(abs(u - v), N3 - abs(u - v)) for u, v in zip(ca, cb))


def diam(p):
    s = [i for i in range(m3["n"]) if (p[0] | p[1]) >> i & 1]
    return max(fd(a, b) for a in s for b in s)


dB, dR, dS = diam(gB[0]), diam(gR[0]), max(diam(s) for s in gS[:3])
nmaj = nbare = 0
for Rm in ROTS:
    okm = all(sp3.reduce(rot_maj(g, Rm, m3)) == 0 for g in gB + gR + gS)
    okb = all(sp3.reduce(rot_bare(g, Rm, m3)) == 0 for g in gB + gR + gS)
    nmaj += okm
    nbare += okb
check("D2 [T]", nmaj == 24 and nbare < 24,
      "all 24 cube rotations about a coarse vertex preserve the code when each moves the stars and permutes "
      "their Majoranas as directions (a star-local Clifford gauge); bare site permutation does not",
      f"rotations preserving the code: star-Majorana action {nmaj}/24, bare permutation {nbare}/24; "
      f"diameters B {dB}, R {dR}, S {dS} fine steps")
O0 = (0, 0, 0)
nb = m3["nb"]
T1 = mul(m3["A"](O0, 0), m3["A"](nb(O0, 0, 1), 0))
T3 = mul(m3["A"](O0, 2), m3["A"](nb(O0, 2, 1), 2))
T2 = rot_maj(T1, C2z, m3)
RT3 = rot_maj(T3, C2z, m3)
theta = comm(T1, T2) * comm(T1, T3) * comm(T2, T3)
lam = comm(T1, T2)
sig = comm(T1, mul(T3, RT3))
in_code = all(comm(T2, g) == 1 for g in gR + gS) and sum(comm(T2, b) == -1 for b in gB) == 2
lam_bare = comm(T1, rot_bare(T1, C2z, m3))
X1 = (1 << m3["arms"][O0][0], 0)
supX = bin(rot_maj(X1, C2z, m3)[0] | rot_maj(X1, C2z, m3)[1]).count("1")
check("D3 [T]", theta == -1 and lam == -1 and sig == 1 and in_code and lam_bare == 1 and supX == 2,
      "the vertex charge is a FERMION (T-junction -1); under the axis C2 the pair sign is lambda = -1 and "
      "the axis sign sigma = +1 (C4-invariant charge), so theta = lambda: the statistics rides on the "
      "non-monomial gauge (X on one arm maps to a 2-site Pauli); the bare permutation gives lambda = +1 "
      "(lemma) and is not a symmetry",
      f"theta {theta:+d}, lambda {lam:+d}, sigma {sig:+d}, lambda_bare {lam_bare:+d}, |supp R(X_arm)| {supX}")

print(f"elapsed_seconds {time.time() - T0:.1f}")
print("supplied: the Pauli-stabilizer class, the monomial reading of rotation covariance, the BKSF ordering "
      "(found by search), the composite star placement, Jordan-Wigner order inside each star, idle-site Z terms.")
print("cited: Levin-Wen PRB 67 245316 (T-junction); Bravyi-Kitaev 2002; main BKSF orbit, bare-permutation, "
      "six-direction, Majorana-per-direction, site-localizable and one-qubit stabilizer notes (2026-10-17).")
print(f"TOTAL: PASS={NP} FAIL={NF}")
