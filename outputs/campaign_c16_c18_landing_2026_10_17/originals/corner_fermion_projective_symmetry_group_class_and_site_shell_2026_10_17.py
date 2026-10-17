#!/usr/bin/env python3
"""Corner fermion at the emergent level: projective symmetry group (PSG) of the cube
rotation group O for a spinless fermion on the 12 corners (perpendicular direction pairs)
of every site, hopping in a uniform Z2 background flux; its class, the site shell, and the
single-site cluster spectrum.

Companion note: docs/CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md
"""
"""Exploration: a fermion on the 12 corners (perpendicular direction pairs) of every
site, hopping in a Z2 gauge field with uniform fluxes; projective symmetry group (PSG)
of the site rotation group O, its class, and the single-site shell spectrum."""
import itertools, sys
import numpy as np

L = 4
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def add(v, d): return tuple((a+b) % L for a, b in zip(v, d))
def perp(d, e): return sum(a*b for a, b in zip(d, e)) == 0 and d != e
CORNERS = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if sum(a*b for a,b in zip(d,e)) == 0]
assert len(CORNERS) == 12
SITES = list(itertools.product(range(L), repeat=3))
VERTS = [(v, c) for v in SITES for c in CORNERS]
VID = {q: i for i, q in enumerate(VERTS)}

edges = {}
def add_edge(q, r, kind):
    key = frozenset((VID[q], VID[r]))
    if key not in edges:
        edges[key] = kind
for v in SITES:
    for c in CORNERS:
        d, e = tuple(c)
        for a, b in ((d, e), (e, d)):           # share a, other directions b and f perpendicular
            for f in DIRS:
                if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                    add_edge((v, c), (v, frozenset((a, f))), 'onsite')
        for a, b in ((d, e), (e, d)):
            add_edge((v, c), (add(v, a), frozenset((neg(a), b))), 'link')
EDGES = list(edges)
EID = {k: i for i, k in enumerate(EDGES)}
nE = len(EDGES)

deg = np.zeros(len(VERTS), int)
for k in EDGES:
    for i in k: deg[i] += 1
assert set(deg) == {6}

def eid(q, r):
    return EID[frozenset((VID[q], VID[r]))]

def cycle_edges(qs):
    return [eid(qs[i], qs[(i+1) % len(qs)]) for i in range(len(qs))]

def axes_perp(d):
    return [f for f in DIRS if perp(f, d) and f != neg(d)]

cycles = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for v in SITES:
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]
        a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
        ring = [a0, b0, neg(a0), neg(b0)]
        cycles['square'].append(cycle_edges([(v, frozenset((d, r))) for r in ring]))
        # tubes around edge (v, v+d): quadrants (ring[i], ring[i+1])
        for i in range(4):
            p, q = ring[i], ring[(i+1) % 4]
            w = add(v, d)
            qs = [(v, frozenset((d, p))), (w, frozenset((neg(d), p))), (w, frozenset((neg(d), q))), (v, frozenset((d, q)))]
            cycles['tube'].append(cycle_edges(qs))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
        cycles['triangle'].append(cycle_edges([(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]))
    for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
        qs = [(v, frozenset((d, e))), (add(v, d), frozenset((neg(d), e))),
              (add(add(v, d), e), frozenset((neg(d), neg(e)))), (add(v, e), frozenset((d, neg(e))))]
        cycles['plaquette'].append(cycle_edges(qs))


def gf2_solve(rows, rhs, n):
    """Solve A x = b over GF(2) with Python-int bitsets. Returns uint8 array or None."""
    piv = {}  # pivot column -> row bitset (bit n = rhs)
    for r, b in zip(rows, rhs):
        x = 0
        for j in r: x ^= (1 << j)
        if b: x ^= (1 << n)
        while True:
            low = x & ((1 << n) - 1)
            if low == 0:
                if x: return None
                break
            c = low.bit_length() - 1
            if c in piv: x ^= piv[c]
            else:
                piv[c] = x; break
    # back substitution: process pivots in increasing column order
    sol = 0
    for c in sorted(piv):
        x = piv[c]
        rest = (x & ((1 << c) - 1))
        val = ((x >> n) & 1) ^ (bin(rest & sol).count('1') & 1)
        if val: sol |= (1 << c)
    out = np.zeros(n, dtype=np.uint8)
    for j in range(n):
        if (sol >> j) & 1: out[j] = 1
    return out


def solve_u(F):
    rows, rhs = [], []
    for k, cs in cycles.items():
        for c in cs:
            rows.append(c); rhs.append(F[k])
    return gf2_solve(rows, rhs, nE)

# rotations about site 0
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
assert len(ROTS) == 24
def rot_dir(R, d): return tuple(int(x) for x in R @ np.array(d))
def rot_site(R, v): return tuple(int(x) % L for x in R @ np.array(v))
def rot_vert(R, q):
    v, c = q
    return (rot_site(R, v), frozenset(rot_dir(R, d) for d in c))
def trans_vert(t, q):
    v, c = q
    return (add(v, t), c)

def vperm(f):
    return np.array([VID[f(q)] for q in VERTS])

def psg_sign(f, u):
    """Find sigma (GF(2) per vertex) with sigma(q)+sigma(r) = u_e + u_{f e}."""
    P = vperm(f)
    rows, rhs = [], []
    for k in EDGES:
        i, j = tuple(k)
        fe = EID[frozenset((P[i], P[j]))]
        # sigma indexed by image vertex: c_q -> sigma(q) c_{fq}
        rows.append([i, j]); rhs.append(u[EID[k]] ^ u[fe])
    s = gf2_solve(rows, rhs, len(VERTS))
    return P, s

def mono(P, s):
    n = len(P)
    M = np.zeros((n, n))
    M[P, np.arange(n)] = (-1.0) ** s
    return M

def classify(F, verbose=True):
    u = solve_u(F)
    if u is None:
        return None
    res = {}
    Ms = []
    for R in ROTS:
        P, s = psg_sign(lambda q, R=R: rot_vert(R, q), u)
        if s is None:
            return 'not invariant'
        Ms.append((P, s))
    # squares of involutions and C4^4 via sparse application
    def apply(Ps, vec_sign):
        pass
    def power_sign(P, s, k):
        # (M)^k on basis vector q: returns sign if returns to q
        n = len(P); sign = np.zeros(n, np.uint8); idx = np.arange(n)
        cur = idx.copy()
        for _ in range(k):
            sign ^= s[cur]; cur = P[cur]
        return cur, sign
    out = {}
    for R, (P, s) in zip(ROTS, Ms):
        tr = int(np.trace(R)); order = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        cur, sign = power_sign(P, s, order)
        assert (cur == np.arange(len(P))).all()
        vals = set(sign.tolist())
        assert len(vals) == 1, "global sign expected"
        kind = {1: 'e', 3: 'C3', 4: 'C4'}.get(order)
        if order == 2:
            kind = 'C2axis' if np.allclose(np.abs(np.diag(R)), 1) else 'C2edge'
        out.setdefault(kind, set()).add(-1 if vals.pop() else 1)
    # translations
    tr_ok = []
    for t in ((1,0,0),(0,1,0)):
        P, s = psg_sign(lambda q, t=t: trans_vert(t, q), u)
        tr_ok.append((P, s))
    (Px, sx), (Py, sy) = tr_ok
    # commutator TxTy vs TyTx on a vertex: sign
    n = len(Px); q = np.arange(n)
    a = sx[q] ^ sy[Px[q]]   # Ty Tx: apply Tx then Ty
    b = sy[q] ^ sx[Py[q]]
    comm = set((a ^ b).tolist())
    out['TxTy'] = {(-1 if c else 1) for c in comm}
    return out, u, Ms

# 2O
def q2su(q):
    a,b,c,d=q; return np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]])
qs=[]
for i in range(4):
    for s in (1,-1):
        v=[0]*4; v[i]=s; qs.append(v)
for sg in itertools.product((1,-1),repeat=4): qs.append([x/2 for x in sg])
r=1/np.sqrt(2)
for i,j in itertools.combinations(range(4),2):
    for si,sj in itertools.product((1,-1),repeat=2):
        v=[0]*4; v[i],v[j]=si*r,sj*r; qs.append(v)
G2=[q2su(q) for q in qs]
P=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(P[i]@U@P[j]@U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
def rid(R): return [k for k,S in enumerate(ROTS) if (S==R).all()][0]
proj=[rid(so3(U)) for U in G2]
def w1(R):
    p=[DIRS.index(rot_dir(R,d)) for d in DIRS]
    s=1; p=list(p)
    for i in range(6):
        while p[i]!=i:
            j=p[i]; p[i],p[j]=p[j],p[i]; s=-s
    return 0 if s==1 else 1
W1=[w1(R) for R in ROTS]

def run(F, twist=True, verbose=True):
    out,u,Ms=classify(F)
    loc=[VID[((0,0,0),c)] for c in CORNERS]
    li={g:i for i,g in enumerate(loc)}
    def Mloc(k):
        Pm,s=Ms[k]; M=np.zeros((12,12),complex)
        for i,g in enumerate(loc):
            M[li[Pm[g]],i]=(-1.0)**s[g]
        return M*(1j**W1[k] if twist else 1)
    Ml=[Mloc(k) for k in range(24)]
    # find homomorphism lift: for each 2O element g with image R choose sign so that it's a rep
    # brute: choose sign for one lift per R via GF(2) solve on consistency
    sec=[proj.index(k) for k in range(24)]
    def gidx(U):
        for k,V in enumerate(G2):
            if np.allclose(U,V): return k
    rows=[];rhs=[]
    for a in range(24):
        for b in range(24):
            prod=G2[sec[a]]@G2[sec[b]]; ab=proj[gidx(prod)]
            w=0 if np.allclose(prod,G2[sec[ab]]) else 1
            X=Ml[a]@Ml[b]; Y=Ml[ab]
            if np.allclose(X,Y): e=0
            elif np.allclose(X,-Y): e=1
            else: return None
            rows.append([a,b,ab]); rhs.append(e^w)
    # solve beta(a)+beta(b)+beta(ab)=rhs (mod 2) with repeated indices handled
    rows2=[]
    for rr in rows:
        cnt={}
        for x in rr: cnt[x]=cnt.get(x,0)^1
        rows2.append([x for x,v in cnt.items() if v])
    beta=gf2_solve(rows2,rhs,24)
    if beta is None:
        if verbose: print("   no lift to 2O: class is not w2 (twist=%s)"%twist)
        return None
    sg=[((-1.0)**int(beta[proj[k]]))*(1 if np.allclose(G2[k],G2[sec[proj[k]]]) else -1) for k in range(48)]
    Mt=[sg[k]*Ml[proj[k]] for k in range(48)]
    # verify homomorphism
    for a in range(48):
        for b in range(48):
            ab=gidx(G2[a]@G2[b])
            assert np.allclose(Mt[a]@Mt[b],Mt[ab])
    return Mt, loc, u

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

def spin_char(j2, U):
    tr = max(-1, min(1, np.real(np.trace(U)) / 2)); th = 2 * np.arccos(tr)
    if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
    return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
E12 = np.array([spin_char(1, U) for U in G2]); G32 = np.array([spin_char(3, U) for U in G2])
E52 = np.array([spin_char(5, U) for U in G2]) - G32
IRR = {'E1/2': E12, 'E5/2': E52, 'G3/2': G32}
def dec(ch):
    d = {k: int(round(np.real(np.sum(np.conj(v) * ch) / 48))) for k, v in IRR.items()}
    return {k: v for k, v in d.items() if v}

NAMES = ('square', 'triangle', 'plaquette', 'tube')
table = {}
for Fb in itertools.product((0, 1), repeat=4):
    Fd = dict(zip(NAMES, Fb)); r = classify(Fd)
    table[Fb] = r if r in (None, 'not invariant') else {k: sorted(v) for k, v in r[0].items()}
    print('  ', {k: ('pi' if v else '0') for k, v in Fd.items()}, table[Fb])
check("all 16 uniform flux patterns are consistent and invariant under O and translations",
      all(isinstance(v, dict) for v in table.values()))
check("square flux pi: axis C2 lifts square to -1, edge C2 to +1, C4^4 = -1 (class w2 + w1^2); square flux 0: all +1",
      all(v['C2axis'] == ([-1] if Fb[0] else [1]) and v['C2edge'] == [1] and v['C4'] == ([-1] if Fb[0] else [1])
          for Fb, v in table.items()))
check("translations commute exactly when square and plaquette fluxes agree",
      all(v['TxTy'] == ([1] if Fb[0] == Fb[2] else [-1]) for Fb, v in table.items()))

ok_lift = True; ok_shell = True; ok_real = True; clus = {}
for tri, tub in itertools.product((0, 1), (0, 1)):
    F = dict(square=1, triangle=tri, plaquette=1, tube=tub)
    r = run(F, twist=True, verbose=False)
    if r is None: ok_lift = False; continue
    Mt, loc, u = r
    if dec(np.array([np.trace(M) for M in Mt])) != {'E1/2': 1, 'E5/2': 1, 'G3/2': 2}: ok_shell = False
    li = {g: i for i, g in enumerate(loc)}
    def cluster(t1, lam):
        Hc = np.zeros((12, 12), complex)
        for k in EDGES:
            i, j = tuple(k)
            if edges[k] == 'onsite' and i in li and j in li:
                a = -t1 * (-1.0) ** u[EID[k]]; Hc[li[i], li[j]] += a; Hc[li[j], li[i]] += a
        v = (0, 0, 0)
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
            cyc = [(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]
            if round(np.linalg.det(np.array([x, y, z]))) < 0: cyc = cyc[::-1]
            for a in range(3):
                q, rr = cyc[a], cyc[(a+1) % 3]; i, j = li[VID[q]], li[VID[rr]]
                amp = 1j * lam * (-1.0) ** u[eid(q, rr)]; Hc[j, i] += amp; Hc[i, j] += np.conj(amp)
        for M in Mt: assert np.allclose(M @ Hc, Hc @ M)
        ev, V = np.linalg.eigh(Hc); m = int(np.sum(np.abs(ev - ev[0]) < 1e-8)); Pj = V[:, :m] @ V[:, :m].conj().T
        return dec(np.array([np.trace(Pj @ M) for M in Mt])), round(float(ev[m] - ev[0]), 4)
    for t1 in (1, -1):
        d, g = cluster(t1, 0.0)
        if d not in ({'E1/2': 1, 'E5/2': 1}, {'G3/2': 1}): ok_real = False
        clus[(tri, tub, t1, 0.0)] = (d, g)
    for t1, lam in ((-1, -0.5), (-1, 0.5), (1, -0.5), (1, 0.5)):
        clus[(tri, tub, t1, lam)] = cluster(t1, lam)
for k, v in clus.items(): print('   cluster (triangle, tube, t1, chiral) =', k, '-> ground', v[0], 'gap', v[1])
check("with the U(1) twist i^{w1}, the action on the 12 corners of a site lifts to a linear representation of 2O (class w2), for square flux pi", ok_lift)
check("the site shell decomposes as E1/2 + E5/2 + 2 G3/2", ok_shell)
check("real (time-reversal-symmetric) on-site hopping: the lowest cluster level is E1/2 + E5/2 or a G3/2 quartet, never a single doublet", ok_real)
check("with the O-invariant chiral term, the cluster ground level is a single E1/2 doublet (triangle 0, t1 = -1, chiral -0.5; also triangle pi, t1 = +1) with gap 2.54",
      clus[(0, 0, -1, -0.5)] == ({'E1/2': 1}, 2.5434) and clus[(1, 0, 1, -0.5)] == ({'E1/2': 1}, 2.5434)
      and clus[(0, 0, -1, 0.5)][0] == {'E5/2': 1})
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
