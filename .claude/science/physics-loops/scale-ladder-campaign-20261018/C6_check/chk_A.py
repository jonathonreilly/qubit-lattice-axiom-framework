#!/usr/bin/env python3
"""C6_check part A (independent): A1 cycle-space rank and relation type-parities (galois GF(2), own
geometry), uniform-pattern consistency on L = 3, 4; A4 target selection via an independent PSG
(BFS sign propagation on the signed adjacency) and an independent fixed-momentum test (joint
eigenspaces of the magnetic translations, mapped by the rotation operators); convention statement
for the repo's t1 = -1 Hamiltonian."""
import itertools, os, sys, time
import numpy as np
import galois

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chk_geometry import Corner, VEC, CORN, cid, opp, perp, dir_of

GF = galois.GF(2)
TYPES = ('square', 'triangle', 'plaquette', 'tube')
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


def incidence(G, extra=()):
    fl = G.face_list()
    M = np.zeros((len(fl) + len(extra), G.E), np.uint8)
    for r, (_, f) in enumerate(fl):
        for e in f:
            M[r, e] ^= 1
    for r, f in enumerate(extra):
        for e in f:
            M[len(fl) + r, e] ^= 1
    return fl, M


def straight_loop(G, ax):
    """noncontractible loop along axis ax using corners {+ax, -t} (t a perpendicular positive axis)."""
    a = 2 * ax; t = 2 * ((ax + 1) % 3) + 1; u = 2 * ((ax + 2) % 3)
    seq = []
    for n in range(G.L):
        v = VEC[a] * n
        w = VEC[a] * (n + 1)
        seq += [(v, (a, t)), (w, (opp(a), t)), (w, (t, u))]
    es = []
    pts = seq + [(VEC[a] * G.L, (a, t))]
    for (p, c), (q, c2) in zip(pts[:-1], pts[1:]):
        es.append(G.edge(p, c, q, c2))
    return es


def solve_gauge(M, rhs):
    """solve M u = rhs over GF(2) (M faces x edges); returns u or None."""
    A = GF(np.concatenate([M, rhs[:, None]], axis=1))
    R = A.row_reduce()
    R = np.array(R, dtype=np.uint8)
    nE = M.shape[1]
    u = np.zeros(nE, np.uint8)
    for row in R:
        nz = np.nonzero(row[:nE])[0]
        if len(nz) == 0:
            if row[nE]:
                return None
            continue
        u[nz[0]] = row[nE]   # reduced row echelon: free variables set to 0
    return u


T0 = time.time()
print("A1 (independent): GF(2) ranks via galois, own geometry")
store = {}
for L in (3, 4):
    G = Corner(L)
    nonc = [straight_loop(G, a) for a in range(3)]
    fl, M = incidence(G)
    _, M3 = incidence(G, nonc)
    rk = np.linalg.matrix_rank(GF(M)); rk3 = np.linalg.matrix_rank(GF(M3))
    cyc = G.E - G.V + 1
    print(f"  L={L}: V={G.V} E={G.E} faces={len(fl)} cyc={cyc} rank(faces)={rk} rank(+3 loops)={rk3}; t={time.time()-T0:.0f}s")
    check(f"L={L}: rank(faces) = E - V + 1 - 3 and the 3 straight loops complete the cycle space", rk == cyc - 3 and rk3 == cyc)
    # left null space: relations among faces
    Nl = np.array(GF(M.T).null_space(), dtype=np.uint8)     # rows r with r M = 0
    tid = np.array([TYPES.index(k) for k, _ in fl])
    par = np.stack([(Nl[:, tid == t].sum(1) % 2) for t in range(4)], 1)
    # span of parity vectors (4-dim, small): reduce
    P = GF(par) if len(par) else GF(np.zeros((1, 4), np.uint8))
    prk = np.linalg.matrix_rank(P)
    basis = np.array(P.row_reduce()[:prk], dtype=np.uint8) if prk else np.zeros((0, 4), np.uint8)
    spanv = sorted({tuple((np.array(c, dtype=np.uint8) @ basis) % 2) for c in itertools.product((0, 1), repeat=prk)})
    print(f"  L={L}: {len(Nl)} independent relations; span of their type-parity vectors = {spanv}")
    if L % 2 == 0:
        check(f"L={L}: all relations have even type parity (so all 16 uniform patterns are consistent)", spanv == [(0, 0, 0, 0)])
    else:
        check(f"L={L}: relation type-parity span is {{0000, 1010}} (square,plaquette) wrapped relation", spanv == [(0, 0, 0, 0), (1, 0, 1, 0)])
    ok = True; nsol = 0
    for Fb in itertools.product((0, 1), repeat=4):
        rhs = np.array([Fb[TYPES.index(k)] for k, _ in fl], np.uint8)
        u = solve_gauge(M, rhs)
        pred = all((np.dot(b, Fb) % 2) == 0 for b in basis)
        if u is None:
            ok &= not pred
        else:
            nsol += 1
            meas = (M.astype(np.int64) @ u) % 2
            ok &= pred and (meas == rhs).all()
    check(f"L={L}: uniform patterns solvable exactly as predicted by the relation parities ({nsol}/16 solvable)", ok)
    store[L] = (G, fl, M)

# ------------------------------------------------------------------ convention statement
print("\nConvention: repo H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c, t1 = -1, t2 > 0 (or < 0)")
# standard flux of a face = sign of prod(-h) where h = -t u ; = prod(sign t) * prod u
G4, fl4, M4 = store[4]
rhs = np.array([(1, 0, 1, 1)[TYPES.index(k)] for k, _ in fl4], np.uint8)
u1011 = solve_gauge(M4, rhs)
ok = True
for t2 in (0.2, -0.2):
    for k, f in fl4:
        prod = 1.0
        for e in f:
            t = -1.0 if G4.edges[e][3] == 'onsite' else t2
            h = -t * (-1) ** int(u1011[e])
            prod *= -h
        ok &= prod < 0          # pi flux in the standard convention (all-negative hops = 0 flux)
check("u-pattern 1011 with t1 = -1 (either sign of t2) has standard-convention flux pi through every face of all four types", ok)
# with t1 = +1 the triangles would be flux 0:
prods = []
for k, f in fl4:
    if k != 'triangle':
        continue
    prod = 1.0
    for e in f:
        prod *= (+1.0) * (-1) ** int(u1011[e])
    prods.append(prod)
check("control: with t1 = +1 the same u gives standard triangle flux 0 (sign is load-bearing)", all(p > 0 for p in prods))

# ------------------------------------------------------------------ A4 via independent PSG
print(f"\nA4 (independent PSG by BFS sign propagation, L = 4); t={time.time()-T0:.0f}s")
L = 4
G = G4
V = G.V
nbr = [[] for _ in range(V)]
for k, (i, j, w, kind) in enumerate(G.edges):
    nbr[i].append((j, k)); nbr[j].append((i, k))
pairedge = {}
for k, (i, j, w, kind) in enumerate(G.edges):
    key = frozenset((i, j)); assert key not in pairedge; pairedge[key] = k


def rot_mats():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for r in range(3):
                R[r, perm[r]] = sg[r]
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    return out


ROTS = rot_mats()
assert len(ROTS) == 24


def perm_rot(R):
    P = np.empty(V, int)
    for s in range(G.N):
        v = G.site(s)
        for (d, e) in CORN:
            d2, e2 = dir_of(R @ VEC[d]), dir_of(R @ VEC[e])
            P[G.vid(v, (d, e))] = G.vid(R @ v, (d2, e2))
    return P


def perm_trans(a):
    P = np.empty(V, int)
    for s in range(G.N):
        v = G.site(s)
        for c in CORN:
            P[G.vid(v, c)] = G.vid(v + np.array(a), c)
    return P


def psg_signs(P, u):
    """find D (+-1 per vertex) with D[P i] D[P j] s(P i,P j) = s(i,j) for every edge, s = (-1)^u; BFS."""
    s = 1 - 2 * u.astype(int)
    D = np.zeros(V, int)
    D[P[0]] = 1
    stack = [0]; seen = np.zeros(V, bool); seen[0] = True
    while stack:
        i = stack.pop()
        for j, k in nbr[i]:
            kk = pairedge[frozenset((P[i], P[j]))]
            val = D[P[i]] * s[kk] * s[k]       # required D[P j]
            if not seen[j]:
                seen[j] = True; D[P[j]] = val; stack.append(j)
            elif D[P[j]] != val:
                return None
    return D


def as_op(P, D):
    """operator U = D P: (U psi)[P i] = D[P i] psi[i]; returns (P, D) and apply function."""
    return (P, D)


def apply(op, x):
    P, D = op
    y = np.empty_like(x)
    y[P] = x
    return D[:, None] * y if x.ndim == 2 else D * y


def compose_sign(ops, m=None):
    """apply ops right-to-left to the basis; returns the diagonal if the product is diagonal, else None."""
    x = np.eye(V)
    for op in reversed(ops):
        x = apply(op, x)
    if not np.allclose(x, np.diag(np.diag(x))):
        return None
    return np.diag(x)


def classify(R):
    tr = int(np.trace(R))
    m = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
    if m == 2:
        return 'C2axis' if (np.abs(np.diag(R)) == 1).all() else 'C2edge'
    return {1: 'e', 3: 'C3', 4: 'C4'}[m]


table = {}
for Fb in itertools.product((0, 1), repeat=4):
    rhs = np.array([Fb[TYPES.index(k)] for k, _ in fl4], np.uint8)
    u = solve_gauge(M4, rhs)
    Tops = []
    for a in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        P = perm_trans(a); D = psg_signs(P, u); assert D is not None
        Tops.append((P, D))
    Tinv = [(np.argsort(P), D[P].copy()) for (P, D) in Tops]   # inverse of U=DP: U^-1 = P^-1 D
    # check inverse
    for op, oi in zip(Tops, Tinv):
        assert np.allclose(compose_sign([oi, op]), 1)
    comm = compose_sign([Tinv[1], Tinv[0], Tops[1], Tops[0]])
    commute = np.allclose(comm, 1)
    anti = np.allclose(comm, -1)
    res = {'TxTy': '+1' if commute else ('-1' if anti else 'non-scalar')}
    rops = {}
    for R in ROTS:
        P = perm_rot(R); D = psg_signs(P, u)
        if D is None:
            res = None; break
        rops[tuple(R.ravel())] = (P, D)
        kind = classify(R); m = {'e': 1, 'C2axis': 2, 'C2edge': 2, 'C3': 3, 'C4': 4}[kind]
        dg = compose_sign([(P, D)] * m)
        vals = set(np.round(dg).astype(int).tolist())
        res.setdefault(kind, set()).update(vals)
    if res is None:
        table[Fb] = None; continue
    fixed = None
    if commute:
        # magnetic translation eigenspaces: T_a^4 = c_a
        c = [compose_sign([Tops[a]] * 4) for a in range(3)]
        assert all(np.allclose(ci, ci[0]) for ci in c)
        cs = [int(round(ci[0])) for ci in c]
        # orthonormal basis of each joint eigenspace via projector applied to the identity
        def proj(k):
            X = np.eye(V, dtype=complex)
            for a in range(3):
                acc = np.zeros_like(X); Y = X.copy()
                for n in range(4):
                    acc += np.exp(-1j * k[a] * n) * Y
                    Y = apply(Tops[a], Y)
                X = acc / 4
            return X
        ks = []
        for nn in itertools.product(range(4), repeat=3):
            k = [(2 * np.pi * nn[a] + (np.pi if cs[a] == -1 else 0)) / 4 for a in range(3)]
            ks.append((nn, np.array(k)))
        bases = {}
        for nn, k in ks:
            Pk = proj(k)
            w, U = np.linalg.eigh((Pk + Pk.conj().T) / 2)
            Q = U[:, w > 0.5]
            assert Q.shape[1] == 12, Q.shape
            bases[nn] = Q
        fixed = []
        for nn, Q in bases.items():
            ok = True
            for key, op in rops.items():
                Y = apply(op, Q)
                # residual outside the k-space
                r = Y - Q @ (Q.conj().T @ Y)
                if np.abs(r).max() > 1e-8:
                    ok = False; break
            if ok:
                fixed.append(nn)
        res['T^4'] = cs
    res['fixed'] = fixed
    table[Fb] = res
    print('  ', ''.join(map(str, Fb)), {k: (sorted(v) if isinstance(v, set) else v) for k, v in res.items()}, f"t={time.time()-T0:.0f}s", flush=True)

check("PSG exists for all 16 uniform patterns (BFS sign propagation consistent for all 24 rotations and 3 translations)",
      all(v is not None for v in table.values()))
check("C4^4 = -1 exactly when square = pi (u-convention)", all((v['C4'] == {-1}) == (F[0] == 1) for F, v in table.items()))
check("translations commute exactly when square = plaquette (otherwise anticommute)",
      all((v['TxTy'] == '+1') == (F[0] == F[2]) and v['TxTy'] in ('+1', '-1') for F, v in table.items()))
targets = sorted(F for F, v in table.items() if v['C4'] == {-1} and v['TxTy'] == '+1' and v['fixed'])
print("  patterns with C4^4 = -1, commuting translations and an O-fixed momentum:", targets)
check("design targets select exactly {1011, 1111}", targets == [(1, 0, 1, 1), (1, 1, 1, 1)])
print("  fixed momenta (units of 2pi/4, plus pi/4 offsets if T^4 = -1):", {''.join(map(str, F)): (v['fixed'], v.get('T^4')) for F, v in table.items() if v['TxTy'] == '+1'})
check("square = 0 patterns with commuting translations: an O-fixed momentum exists iff tube = 0 (Gamma-type), so tube = pi is needed only together with square = pi",
      all(bool(table[F]['fixed']) == (F[3] == 0) for F in table if F[0] == 0 and F[2] == 0))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time()-T0:.0f}s)")
