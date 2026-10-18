#!/usr/bin/env python3
"""C7_check A: exact-solvability claims of the C7 Gamma-matrix model, with an independent Gamma basis,
independent bond labelling, independent geometry (k7_geom) and an independent Majorana derivation of every
closed-surface sign.

A0  find 7 mutually anticommuting 3-qubit Pauli strings by a seeded random clique search (not the
    JW-type basis XII,YII,ZXI,... used by C7); check Cl(7), Hermitian, product = +-i.
A1  dictionary in an explicit Jordan-Wigner realisation of 16 Majoranas (2 corners): G^a = i b^a c,
    G^7 = i d c obey the Cl(7) relations; u_e (i c_I c_J) = -G^a_I G^b_J; u_e (i d_I d_J) = -(iG^aG^7)_I (iG^bG^7)_J;
    the D_q = +1 subspace has dimension 8 per corner and commutes with every G.
A2  L = 2 torus (96 corners, 288 qubits): W_C = prod_m (-i G^in G^out) for all 232 faces; Hermitian, mutually
    commuting, commuting with every bond term of H_M, H_M2, H_R.
A3  all closed-surface relations: the GF(2) left kernel of the face-edge incidence on L = 2; for each kernel
    vector the Pauli product of the W's is +-1 x identity, and its sign equals the Majorana prediction
    prod_f (-1)^(n_f + 1) x prod_e (u_e u_e' = -1 for opposite traversals, +1 for equal).  The cuboctahedron
    (14 outward faces) individually: predicted and found +1.
A4  ED of the qubit model on clusters (triangle, square, tube, plaquette): spectrum in each W sector equals the
    free Majorana spectrum with prod u = (-1)^(n+1) W.
"""
import itertools, os, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_geom import Lat, TYPES, CORNERS, CI, gf2

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


# ---------------------------------------------------------------- Pauli algebra (phase i^k, X^x Z^z per qubit)
def pm(a, b):
    k1, x1, z1 = a; k2, x2, z2 = b
    return ((k1 + k2 + 2 * bin(z1 & x2).count('1')) % 4, x1 ^ x2, z1 ^ z2)


def comm(a, b):
    return (bin(a[1] & b[2]).count('1') + bin(a[2] & b[1]).count('1')) % 2 == 0


def lab2p(s, off=0):
    k = x = z = 0
    for t, ch in enumerate(s):
        q = off + t
        if ch in 'XY': x |= 1 << q
        if ch in 'ZY': z |= 1 << q
        if ch == 'Y': k += 1          # Y = i X Z
    return (k % 4, x, z)


def shift(P, off):
    return (P[0], P[1] << off, P[2] << off)


def sc(k, P): return ((P[0] + k) % 4, P[1], P[2])


ID = (0, 0, 0)

# ---------------------------------------------------------------- A0: an independent Cl(7) basis
print("A0: Cl(7) basis by random clique search")
LABS = [''.join(p) for p in itertools.product('IXYZ', repeat=3) if ''.join(p) != 'III']
rng = np.random.default_rng(20261018)
GL = None
for trial in range(20000):
    order = rng.permutation(len(LABS))
    cl = []
    for i in order:
        P = lab2p(LABS[i])
        if all(not comm(P, lab2p(q)) for q in cl):
            cl.append(LABS[i])
    if len(cl) == 7:
        GL = cl; break
print("   basis:", GL, f"(found at trial {trial})")
G1 = [lab2p(s) for s in GL]
ok = all((not comm(G1[a], G1[b])) == (a != b) for a in range(7) for b in range(7))
ok &= all(pm(P, P) == ID for P in G1)        # Hermitian Paulis (k = #Y mod 4 and squares to +1)
prod = ID
for P in G1: prod = pm(prod, P)
check("7 mutually anticommuting Hermitian 3-qubit Pauli strings (8-dim Cl(7) irrep), product = +-i",
      ok and prod[1:] == (0, 0) and prod[0] in (1, 3), f"product = i^{prod[0]}; differs from C7 basis: "
      f"{GL != ['XII','YII','ZXI','ZYI','ZZX','ZZY','ZZZ']}")


def G(a, q):          # a = 1..7 on corner q (qubits 3q..3q+2)
    return shift(G1[a - 1], 3 * q)


def iGG(a, b, q): return sc(1, pm(G(a, q), G(b, q)))


# ---------------------------------------------------------------- A1: JW realisation of the dictionary
print("\nA1: Jordan-Wigner check of the Majorana dictionary (2 corners, 16 Majoranas)")
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Zm = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
nq = 8


def kron(ms):
    out = np.eye(1, dtype=complex)
    for m in ms: out = np.kron(out, m)
    return out


gam = []
for m in range(16):
    q = m // 2
    gam.append(kron([Zm] * q + [X if m % 2 == 0 else Y] + [I2] * (nq - q - 1)))
# corner q: b1..b6 = gam[8q+1..8q+6], c = gam[8q], d = gam[8q+7]   (ordering differs from C7)
b = lambda a, q: gam[8 * q + a]
c = lambda q: gam[8 * q]
d = lambda q: gam[8 * q + 7]
Gm = lambda a, q: 1j * (b(a, q) if a <= 6 else d(q)) @ c(q)
okA = True
for q in range(2):
    for a in range(1, 8):
        for a2 in range(1, 8):
            ac = Gm(a, q) @ Gm(a2, q) + Gm(a2, q) @ Gm(a, q)
            okA &= np.allclose(ac, 2 * np.eye(256) * (a == a2))
        okA &= np.allclose(Gm(a, q), Gm(a, q).conj().T)
Dq = []
for q in range(2):
    P = np.eye(256, dtype=complex)
    for a in range(1, 8): P = P @ Gm(a, q)
    # P = G1..G7 squares to -1 -> eigenvalues +-i; D := i P or -i P, Hermitian, squares to 1
    D = 1j * P
    okA &= np.allclose(D @ D, np.eye(256)) and np.allclose(D, D.conj().T)
    okA &= all(np.allclose(D @ Gm(a, q), Gm(a, q) @ D) for a in range(1, 8))
    Dq.append(D)
Pp = (np.eye(256) + Dq[0]) @ (np.eye(256) + Dq[1]) / 4
okA &= abs(np.trace(Pp).real - 64) < 1e-9
check("JW: G^a = i b^a c, G^7 = i d c are Hermitian, generate Cl(7) per corner; D_q = i G1..G7 is a Z2 "
      "commuting with all G; physical dimension 8 per corner (64 for two)", okA)
okD = True
for al, be in itertools.product(range(1, 7), repeat=2):
    u = 1j * b(al, 0) @ b(be, 1)
    okD &= np.allclose(u @ (1j * c(0) @ c(1)), -Gm(al, 0) @ Gm(be, 1))
    okD &= np.allclose(u @ (1j * d(0) @ d(1)), -(1j * Gm(al, 0) @ Gm(7, 0)) @ (1j * Gm(be, 1) @ Gm(7, 1)))
    okD &= np.allclose(u @ (1j * c(0) @ d(1)), -Gm(al, 0) @ (1j * Gm(be, 1) @ Gm(7, 1)))
check("dictionary: u_e (i c_I c_J) = -G^a_I G^b_J, u_e (i d d) = -(iG^aG^7)(iG^bG^7), u_e (i c d) = -G^a (iG^bG^7) "
      "for all 36 label pairs (operator identities)", okD)

# ---------------------------------------------------------------- bond labels (mine) and Pauli bond terms
lat = Lat(2)
INC = {c: [] for c in CORNERS}
for t, (c1, c2, R, k) in enumerate(TYPES):
    INC[c1].append((t, 0, (k, sorted(c2), R)))
    INC[c2].append((t, 1, (k, sorted(c1), tuple(-x for x in R))))
LABEL = {}
for cc, lst in INC.items():
    assert len(lst) == 6
    for a, (t, end, key) in enumerate(sorted(lst, key=lambda z: (z[2][0], z[2][1], z[2][2]))):
        LABEL[(t, end)] = a + 1


def labels(e):
    t = lat.typ[e]
    return LABEL[(t, 0)], LABEL[(t, 1)]


def bond_terms(e, model):
    I, J = int(lat.I[e]), int(lat.J[e])
    a, bb = labels(e)
    if model == 'M': return [pm(G(a, I), G(bb, J))]
    if model == 'M2': return [pm(G(a, I), G(bb, J)), pm(iGG(a, 7, I), iGG(bb, 7, J))]
    if model == 'R': return [pm(G(a, I), iGG(bb, 7, J)), pm(iGG(a, 7, I), G(bb, J))]


def W_of(walk):
    W = ID; n = len(walk)
    for m in range(n):
        e_in, s_in = walk[m - 1]; e_out, s_out = walk[m]
        t_in = lat.typ[e_in]; t_out = lat.typ[e_out]
        lab_in = LABEL[(t_in, 1 if s_in == 1 else 0)]       # vertex is the head of the incoming traversal
        lab_out = LABEL[(t_out, 0 if s_out == 1 else 1)]
        q = int(lat.I[e_out]) if s_out == 1 else int(lat.J[e_out])
        q2 = int(lat.J[e_in]) if s_in == 1 else int(lat.I[e_in])
        assert q == q2
        W = pm(W, sc(3, pm(G(lab_in, q), G(lab_out, q))))
    return W


print(f"\nA2: L = 2 torus: {lat.n} corners, {3*lat.n} qubits, {lat.nE} edges, {len(lat.faces)} faces")
Ws = [W_of(w) for _, w, _ in lat.faces]
okH = all(pm(W, W) == ID for W in Ws)
okC = all(comm(Ws[i], Ws[j]) for i in range(len(Ws)) for j in range(i))
check("all 232 W_C square to +1 (Hermitian) and mutually commute", okH and okC)
res = {}
for model in ('M', 'M2', 'R'):
    terms = [P for e in range(lat.nE) for P in bond_terms(e, model)]
    res[model] = all(comm(P, W) for P in terms for W in Ws)
check("every bond term of H_M, H_M2 and H_R commutes with every W_C", all(res.values()), str(res))
nac = sum(not comm(P, Q) for P, Q in itertools.combinations([bond_terms(e, 'M')[0] for e in range(lat.nE)], 2))
check("control: H_M bond terms anticommute iff they share a corner (96 x C(6,2) = 1440 pairs)", nac == 1440, f"{nac}")

# ---------------------------------------------------------------- A3: closed-surface relations
print(f"\nA3: closed-surface relations (left kernel of the face-edge incidence); t = {time.time()-T0:.1f}s")
nF = len(lat.faces)
# kernel of M^T (faces x edges) over GF(2): Gaussian elimination on [M | I]
rowsM = []
for f, (_, w, _) in enumerate(lat.faces):
    r = 0
    for e, _ in w: r ^= 1 << e
    rowsM.append((r, 1 << f))
piv = {}; kern = []
for r, tag in rowsM:
    while r:
        cbit = r.bit_length() - 1
        if cbit in piv:
            r ^= piv[cbit][0]; tag ^= piv[cbit][1]
        else:
            piv[cbit] = (r, tag); break
    if not r:
        kern.append(tag)
print(f"   rank {len(piv)}, kernel dim {len(kern)} (faces {nF}, edges {lat.nE}, corners {lat.n})")


def predicted_sign(fs):
    sgn = 1; dirs = {}
    for f in fs:
        _, w, _ = lat.faces[f]
        sgn *= (-1) ** (len(w) + 1)
        for e, s in w:
            dirs.setdefault(e, []).append(s)
    for e, ss in dirs.items():
        assert len(ss) % 2 == 0
        # pairs of traversals: u_e u_e = +1 for same direction, u_e (-u_e) = -1 for opposite
        sgn *= int(np.prod(ss)) if len(ss) == 2 else int(np.prod(ss))
        # (for len 2: s1*s2 = +1 same, -1 opposite; and u_ij u_ji = -1, u_ij u_ij = +1 -> equal to s1*s2)
    return sgn


okK = True; signs = []
for tag in kern:
    fs = [f for f in range(nF) if (tag >> f) & 1]
    P = ID
    for f in fs: P = pm(P, Ws[f])
    okK &= P[1] == 0 and P[2] == 0 and P[0] in (0, 2)
    found = 1 if P[0] == 0 else -1
    pred = predicted_sign(fs)
    okK &= found == pred
    signs.append(found)
check("every closed-surface relation (kernel basis) gives prod W = +-1 x identity with the sign predicted by the "
      "Majorana identity W_C = (-1)^(n+1) prod_C u", okK, f"{len(kern)} relations, signs {sorted(set(signs))}")
cub = [f for f, (k, _, (v, _)) in enumerate(lat.faces) if v == (0, 0, 0) and k in ('square', 'triangle')]
P = ID
for f in cub: P = pm(P, Ws[f])
check("cuboctahedron of site (0,0,0): product of the 14 outward W = +1 x identity (prediction +1)",
      len(cub) == 14 and P == ID and predicted_sign(cub) == 1, f"phase i^{P[0]}")
# a second closed surface: the 4 tubes around a link plus the two end squares
v = (0, 0, 0)
tub = [f for f, (k, _, (vv, lab)) in enumerate(lat.faces) if k == 'tube' and vv == v and lab[0] == (1, 0, 0)]
sqs = [f for f, (k, _, (vv, lab)) in enumerate(lat.faces) if k == 'square' and
       ((vv == v and lab == (1, 0, 0)) or (vv == (1, 0, 0) and lab == (-1, 0, 0)))]
fs = tub + sqs
tot = 0
for f in fs:
    for e, _ in lat.faces[f][1]: tot ^= 1 << e
P = ID
for f in fs: P = pm(P, Ws[f])
check("link prism (4 tubes + 2 end squares) is closed and prod W = (Majorana-predicted sign) x identity",
      tot == 0 and P[1:] == (0, 0) and (1 if P[0] == 0 else -1) == predicted_sign(fs),
      f"sign {1 if P[0]==0 else -1 if P[0]==2 else 'complex'}")
print(f"   t = {time.time()-T0:.1f}s")

# ---------------------------------------------------------------- A4: cluster ED
print("\nA4: cluster ED of H_M (random J) vs free Majoranas")


def to_dense(P, verts):
    loc = {v: i for i, v in enumerate(verts)}
    k, x, z = P
    mats = []
    for v in verts:
        for t in range(3):
            g = 3 * v + t
            xb, zb = (x >> g) & 1, (z >> g) & 1
            mats.append(X @ Zm if (xb and zb) else X if xb else Zm if zb else I2)
    # check support inside cluster
    mask = 0
    for v in verts:
        for t in range(3): mask |= 1 << (3 * v + t)
    assert (x & ~mask) == 0 and (z & ~mask) == 0
    return (1j ** k) * kron(mats)


def cluster(face_ids, model='M'):
    edges = sorted({e for f in face_ids for e, _ in lat.faces[f][1]})
    verts = sorted({int(lat.I[e]) for e in edges} | {int(lat.J[e]) for e in edges})
    N = len(verts); dim = 8 ** N
    rngc = np.random.default_rng(len(edges) * 7 + N)
    Jv = {e: rngc.uniform(0.4, 1.6) for e in edges}
    H = np.zeros((dim, dim), complex)
    for e in edges:
        H += -Jv[e] * to_dense(bond_terms(e, 'M')[0], verts)
    Wm = [to_dense(Ws[f], verts) for f in face_ids]
    ok = np.allclose(H, H.conj().T) and all(np.allclose(H @ W, W @ H) for W in Wm)
    worst = 0.0
    for sg in itertools.product((1, -1), repeat=len(face_ids)):
        # projector onto the W sector
        Pj = np.eye(dim, dtype=complex)
        for s, W in zip(sg, Wm): Pj = Pj @ (np.eye(dim) + s * W) / 2
        w, V = np.linalg.eigh(Pj)
        B = V[:, w > 0.5]
        Es = np.linalg.eigvalsh(B.conj().T @ H @ B)
        # free Majoranas: u_e with prod over face walk of (s * u_e) = (-1)^(n+1) * W
        rows = [[edges.index(e) for e, _ in lat.faces[f][1]] for f in face_ids]
        rhs = []
        for f, s in zip(face_ids, sg):
            w_ = lat.faces[f][1]
            # prod_m (sigma_m u_m) = (-1)^(n+1) s  ->  prod u = (-1)^(n+1) s prod sigma
            target = (-1) ** (len(w_) + 1) * s * int(np.prod([si for _, si in w_]))
            rhs.append(0 if target == 1 else 1)
        xb = gf2(rows, rhs, len(edges))
        A = np.zeros((N, N))
        li = {v: i for i, v in enumerate(verts)}
        for e, bit in zip(edges, xb):
            uval = (-1.0) ** bit
            i, j = li[int(lat.I[e])], li[int(lat.J[e])]
            A[i, j] += 2 * Jv[e] * uval; A[j, i] -= 2 * Jv[e] * uval   # H = (i/4) sum A_jk c_j c_k
        ev = np.linalg.eigvalsh(1j * A)
        pos = ev[ev > 1e-10]
        lev = np.array([-0.5 * pos.sum()])
        for p in pos: lev = np.concatenate([lev, lev + p])
        u1 = np.unique(np.round(Es, 8)); u2 = np.unique(np.round(lev, 8))
        same = len(u1) == len(u2) and np.allclose(u1, u2, atol=1e-7)
        if same:
            c1 = np.array([np.sum(np.abs(Es - x) < 1e-6) for x in u1], float)
            c2 = np.array([np.sum(np.abs(lev - x) < 1e-6) for x in u2], float)
            same &= np.allclose(c1 / c1.sum(), c2 / c2.sum())
            worst = max(worst, float(np.max(np.abs(u1 - u2))))
        else:
            worst = np.inf
        ok &= bool(same)
    return ok, N, len(edges), worst


def first(kind, v=(0, 0, 0)):
    return next(f for f, (k, _, (vv, _)) in enumerate(lat.faces) if k == kind and vv == v)


for name, fids in [('triangle', [first('triangle')]), ('square', [first('square')]),
                   ('tube', [first('tube')]), ('plaquette', [first('plaquette')])]:
    ok, N, nE, worst = cluster(fids)
    check(f"H_M on a {name}: qubit spectrum in each W sector = free Majorana levels (with relative multiplicities)",
          ok, f"N = {N} corners ({3*N} qubits), E = {nE}, max dev {worst:.1e}")
print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
