#!/usr/bin/env python3
"""C7 part A: a translation-invariant Gamma-matrix (Kitaev-type) qubit model on the fine cubic
lattice whose exact solution is fermions hopping on the corner graph in a static Z2 gauge field.

Construction (supplied model, new here; standard Kitaev / Wu-Arovas-Hung / Ryu / Yao-Lee recipe).
 * Every fine site carries 12 corners q = {d, e}; every corner carries 3 qubits (an 8-dim space),
   36 qubits per site.  The corner graph is 6-regular (4 on-site cuboctahedron edges + 2 links),
   so each corner needs 6 'bond' Gamma matrices; Cl(7) has the 8-dim irrep
       G1..G7 = XII, YII, ZXI, ZYI, ZZX, ZZY, ZZZ   (mutually anticommuting, G1...G7 = -i).
 * Bond labels: the 6 edges at a corner are labelled 1..6 by a fixed rule depending only on the
   corner type and the edge's relative position (translation invariant).
 * Majorana dictionary (physical = D_q = +1 subspace of 8 Majoranas b1..b6, c, d per corner):
       G^a = i b^a c (a <= 6),  G^7 = i d c,  so  b^a b^b = G^a G^b,  i b^a d = i G^a G^7.
   For an edge e = (I -> J) with labels (alpha at I, beta at J), u_e := i b^alpha_I b^beta_J and
       u_e (i c_I c_J) = - G^alpha_I G^beta_J                       (A)
       u_e (i d_I d_J) = - (i G^alpha G^7)_I (i G^beta G^7)_J
       u_e (i c_I d_J) = - G^alpha_I (i G^beta G^7)_J,  u_e (i d_I c_J) = - (i G^alpha G^7)_I G^beta_J.
 * Hamiltonians (all are sums of Pauli strings on the qubits, translation invariant):
       H_M   = sum_e J_e u_e (i c c)                         one Majorana per corner (d spectators)
       H_M2  = sum_e J_e u_e (i c c + i d d)                  two Majorana flavours = complex parton
                                                              f = (c + i d)/2 with hopping i J u
       H_R   = sum_e t_e u_e (i/2)(c_I d_J - d_I c_J)         = sum t_e u_e (f+_I f_J + h.c.): real
                                                              hopping = the C6 / corner-model problem
   plus an on-site chemical potential (i c d = -G^7) if wanted.
 * Conserved fluxes: for every face C traversed j1 -> ... -> jn, W_C := prod_m (-i G^{in} G^{out})_{j_m}
   (Pauli string) satisfies prod_{e in C} u_{traversal} = (-1)^(n+1) W_C, commutes with every bond
   term and with every other W.

Checks
 A0  Gamma matrices: anticommutation, product = -i; dictionary identities (A) etc. verified in an
     explicit Jordan-Wigner representation of 8 Majoranas projected to D = +1 (two corners).
 A1  (L = 2 torus, 96 corners, 288 qubits; exact symplectic Pauli algebra) every W_C commutes with
     every term of H_M, H_M2, H_R and with every other W_C; closed-surface relation
     prod over the 14 faces of a cuboctahedron of W (outward) = +1 (with phase, exact).
 A2  (exact diagonalisation of the qubit model on clusters: triangle, square, plaquette, tube,
     and an open chain) in each W sector, the qubit spectrum equals the free-fermion many-body
     spectrum with the fluxes given by the dictionary, with uniform multiplicity, for H_M, H_M2, H_R.
"""
import itertools, os, sys, time
import numpy as np
import scipy.sparse as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c7_common import Lattice, TYPES

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


# ------------------------------------------------------------------ Pauli strings with phases
# a Pauli string on n qubits: (phase k: i^k, x bits, z bits); operator = i^k prod X^x Z^z (X before Z per qubit)
def pmul(a, b):
    k1, x1, z1 = a; k2, x2, z2 = b
    # (X^x1 Z^z1)(X^x2 Z^z2) = (-1)^{z1.x2} X^{x1+x2} Z^{z1+z2}
    s = bin(z1 & x2).count('1')
    return ((k1 + k2 + 2 * s) % 4, x1 ^ x2, z1 ^ z2)


def commute(a, b):
    return (bin(a[2] & b[1]).count('1') + bin(a[1] & b[2]).count('1')) % 2 == 0


def from_label(lbl, offset):
    """lbl like 'ZZX' on qubits offset.. ; Y = i X Z."""
    k = x = z = 0
    for t, ch in enumerate(lbl):
        q = offset + t
        if ch == 'X':
            x |= 1 << q
        elif ch == 'Z':
            z |= 1 << q
        elif ch == 'Y':
            x |= 1 << q; z |= 1 << q; k += 1
    return (k % 4, x, z)


GLBL = ['XII', 'YII', 'ZXI', 'ZYI', 'ZZX', 'ZZY', 'ZZZ']


def G(a, q):
    """Gamma^a (a = 1..7) on corner q (qubits 3q..3q+2)."""
    return from_label(GLBL[a - 1], 3 * q)


def scal(k, P):
    return ((P[0] + k) % 4, P[1], P[2])


I0 = (0, 0, 0)


def iGG(a, b, q):
    """i G^a G^b on corner q."""
    return scal(1, pmul(G(a, q), G(b, q)))


# dense matrices for small clusters
PX = np.array([[0, 1], [1, 0]], complex); PZ = np.array([[1, 0], [0, -1]], complex); P1 = np.eye(2)


def to_sparse(P, n):
    k, x, z = P
    m = sp.identity(1, dtype=complex, format='csr')
    for q in range(n):  # qubit 0 is the leftmost factor
        f = P1
        if (x >> q) & 1 and (z >> q) & 1:
            f = PX @ PZ
        elif (x >> q) & 1:
            f = PX
        elif (z >> q) & 1:
            f = PZ
        m = sp.kron(m, sp.csr_matrix(f), format='csr')
    return (1j ** k) * m


# ------------------------------------------------------------------ A0: Gamma algebra + JW dictionary
print("A0: Gamma matrices and the Majorana dictionary")
ok = True
for a in range(1, 8):
    for b in range(1, 8):
        ok &= commute(G(a, 0), G(b, 0)) == (a == b)
    ok &= pmul(G(a, 0), G(a, 0)) == I0
prod = I0
for a in range(1, 8):
    prod = pmul(prod, G(a, 0))
check("G1..G7 Hermitian Pauli strings, mutually anticommuting, square to 1; G1 G2 ... G7 = -i",
      ok and prod == (3, 0, 0), f"product phase i^{prod[0]}")

# Jordan-Wigner for 16 Majoranas (two corners): gamma_{2m} = Z..Z X, gamma_{2m+1} = Z..Z Y
NM = 16; nq = NM // 2
def jw(m):
    q = m // 2
    lbl = 'Z' * q + ('X' if m % 2 == 0 else 'Y') + 'I' * (nq - q - 1)
    return to_sparse(from_label(lbl, 0), nq).toarray()
gam = [jw(m) for m in range(NM)]
# corner q: Majoranas b1..b6 = gam[8q+0..5], c = gam[8q+6], d = gam[8q+7]
def bmaj(a, q): return gam[8 * q + a - 1]
def cmaj(q): return gam[8 * q + 6]
def dmaj(q): return gam[8 * q + 7]
def Gm(a, q):
    return 1j * (bmaj(a, q) if a <= 6 else dmaj(q)) @ cmaj(q)
# D_q chosen so that G1...G7 = -i on the D = +1 subspace
Dq = []
for q in range(2):
    Pq = np.eye(2 ** nq, dtype=complex)
    for a in range(1, 8):
        Pq = Pq @ Gm(a, q)
    Dq.append(1j * Pq)        # = +1 iff G1..G7 = -i
Pphys = (np.eye(2 ** nq) + Dq[0]) @ (np.eye(2 ** nq) + Dq[1]) / 4
ok = np.allclose(Dq[0] @ Dq[0], np.eye(2 ** nq)) and abs(np.trace(Pphys).real - 64) < 1e-9
# identities (A) on the physical subspace, edge I = corner 0 (label alpha = 2), J = corner 1 (beta = 5)
al, be = 2, 5
u = 1j * bmaj(al, 0) @ bmaj(be, 1)
iGG7 = lambda a, q: 1j * Gm(a, q) @ Gm(7, q)
pairs = [
    (u @ (1j * cmaj(0) @ cmaj(1)), -Gm(al, 0) @ Gm(be, 1)),
    (u @ (1j * dmaj(0) @ dmaj(1)), -iGG7(al, 0) @ iGG7(be, 1)),
    (u @ (1j * cmaj(0) @ dmaj(1)), -Gm(al, 0) @ iGG7(be, 1)),
    (u @ (1j * dmaj(0) @ cmaj(1)), -iGG7(al, 0) @ Gm(be, 1)),
    (bmaj(al, 0) @ bmaj(3, 0), Gm(al, 0) @ Gm(3, 0)),
    (1j * bmaj(al, 0) @ dmaj(0), iGG7(al, 0)),
]
for lhs, rhs in pairs:
    ok &= np.allclose(lhs, rhs)          # these hold as operator identities on the full space
# complex parton f = (c + i d)/2: f+_0 f_1 + h.c. = (i/2)(c0 d1 - d0 c1);  i(f+_0 f_1 - h.c.) = (i/2)(c0 c1 + d0 d1)
f0 = (cmaj(0) + 1j * dmaj(0)) / 2; f1 = (cmaj(1) + 1j * dmaj(1)) / 2
hop = f0.conj().T @ f1; hop = hop + hop.conj().T
ok &= np.allclose(hop, 0.5j * (cmaj(0) @ dmaj(1) - dmaj(0) @ cmaj(1)))
ihop = f0.conj().T @ f1; ihop = 1j * (ihop - ihop.conj().T)
ok &= np.allclose(ihop, 0.5j * (cmaj(0) @ cmaj(1) + dmaj(0) @ dmaj(1)))
# the projected bilinears realise the Pauli algebra: physical operators commute with D_q
for a in range(1, 8):
    ok &= np.allclose(Gm(a, 0) @ Dq[0], Dq[0] @ Gm(a, 0))
check("JW realisation: D_q^2 = 1, physical dim 8 per corner; dictionary identities (A), the parton hopping "
      "identities and [G^a, D_q] = 0 hold", ok)

# ------------------------------------------------------------------ bond labels on the corner graph
lat = Lattice(2)
Gr = lat.G


def corner_key(c):
    return tuple(sorted(c))


def incident_descriptors(G_):
    """per vertex: list of (edge, end) with end = 0 if the vertex is the stored I end; label by sorted
    translation-invariant descriptor (displacement to the neighbour, neighbour corner)."""
    inc = {i: [] for i in range(G_.nV)}
    for e, (v, c, disp, c2) in enumerate(G_.edesc):
        I, J, _, _ = G_.edges[e]
        inc[I].append((e, 0, (tuple(disp), corner_key(c2))))
        inc[J].append((e, 1, (tuple(-x for x in disp), corner_key(c))))
    lab = {}
    for i, lst in inc.items():
        lst = sorted(lst, key=lambda t: t[2])
        assert len(lst) == 6
        for a, (e, end, _) in enumerate(lst):
            lab[(e, end)] = a + 1
    return lab


LAB = incident_descriptors(Gr)
# translation invariance of the labelling: label depends only on (corner type, descriptor)
tinv = {}
okT = True
for e, (v, c, disp, c2) in enumerate(Gr.edesc):
    for end, key in ((0, (corner_key(c), tuple(disp), corner_key(c2))),
                     (1, (corner_key(c2), tuple(-x for x in disp), corner_key(c)))):
        okT &= tinv.setdefault(key, LAB[(e, end)]) == LAB[(e, end)]
check("bond labels 1..6 at every corner, a function of (corner type, relative edge descriptor) only "
      "(translation invariant)", okT and len(tinv) == 72, f"{len(tinv)} oriented descriptors")


def bond_terms(e, model, J=1.0):
    """Pauli-string terms (coefficient, string) of edge e for the given model (qubits: 3 per vertex)."""
    I, Jv, _, _ = Gr.edges[e]
    a, b = LAB[(e, 0)], LAB[(e, 1)]
    GI, GJ = G(a, I), G(b, Jv)
    DI, DJ = iGG(a, 7, I), iGG(b, 7, Jv)
    if model == 'M':
        return [(-J, pmul(GI, GJ))]
    if model == 'M2':
        return [(-J, pmul(GI, GJ)), (-J, pmul(DI, DJ))]
    if model == 'R':  # t u (i/2)(c_I d_J - d_I c_J) = (t/2)[-G_I D_J + D_I G_J]
        return [(-J / 2, pmul(GI, DJ)), (J / 2, pmul(DI, GJ))]
    raise ValueError


def face_W(trav):
    """W_C for the oriented traversal [(edge, sigma)] (sigma = +1 along the stored orientation)."""
    W = I0
    n = len(trav)
    for m in range(n):
        e_in, s_in = trav[m - 1]
        e_out, s_out = trav[m]
        # vertex j_m: end of e_in (in traversal direction) and start of e_out
        lab_in = LAB[(e_in, 1 if s_in == 1 else 0)]
        lab_out = LAB[(e_out, 0 if s_out == 1 else 1)]
        I, Jv, _, _ = Gr.edges[e_out]
        q = I if s_out == 1 else Jv
        W = pmul(W, scal(3, pmul(G(lab_in, q), G(lab_out, q))))   # -i G^in G^out
    return W


# ------------------------------------------------------------------ A1: torus algebra
print(f"\nA1: L = 2 torus, {Gr.nV} corners = {3*Gr.nV} qubits, {Gr.nE} edges, {len(lat.faces)} faces; exact Pauli algebra")
Ws = [face_W(trav) for _, trav, _ in lat.faces]
ok_herm = all(pmul(W, W) == I0 for W in Ws)
ok_WW = all(commute(Ws[i], Ws[j]) for i in range(len(Ws)) for j in range(i + 1, len(Ws)))
ok_HW = {}
for model in ('M', 'M2', 'R'):
    terms = [P for e in range(Gr.nE) for _, P in bond_terms(e, model)]
    ok_HW[model] = all(commute(P, W) for P in terms for W in Ws)
check("every W_C is a Hermitian Pauli string squaring to 1, and all 232 W_C mutually commute", ok_herm and ok_WW)
check("every bond term of H_M, H_M2 and H_R commutes with every W_C (fluxes conserved)",
      all(ok_HW.values()), str(ok_HW))
# non-trivial: bond terms sharing a corner do not all commute (the model is not a commuting projector model)
tM = [P for e in range(Gr.nE) for _, P in bond_terms(e, 'M')]
nac = sum(not commute(tM[i], tM[j]) for i in range(len(tM)) for j in range(i + 1, len(tM)))
print(f"   (control) anticommuting pairs among the {len(tM)} H_M bond terms: {nac} (= pairs of edges sharing one corner: "
      f"{Gr.nV * 15})")
check("control: H_M bond terms anticommute exactly for edges sharing a corner (Kitaev structure)", nac == Gr.nV * 15)
# closed surface: the cuboctahedron of site (0,0,0): 6 squares + 8 triangles, outward orientation
site0 = (0, 0, 0)
prod = I0; nf = 0
for f, (k, trav, chi) in enumerate(lat.faces):
    if k not in ('square', 'triangle'):
        continue
    seq_site = Gr.face_seq[k][[i for i, (kk, _, _) in enumerate(lat.faces) if kk == k].index(f)][0][0]
    if tuple(x % 2 for x in seq_site) != site0:
        continue
    W = Ws[f]
    if k == 'triangle' and chi == -1:
        W = scal(2, W)        # reversing a 3-cycle flips W: W(rev) = (-1)^n W
    prod = pmul(prod, W); nf += 1
check("closed-surface relation: product over the 14 faces of a cuboctahedron of W (outward) = +1 exactly",
      nf == 14 and prod == I0, f"{nf} faces, product = i^{prod[0]} x (identity: {prod[1:] == (0, 0)})")
print(f"   t = {time.time()-T0:.1f}s")


# ------------------------------------------------------------------ A2: cluster exact diagonalisation
def free_levels(Amat):
    """many-body levels of H = (i/4) sum A_jk g_j g_k for real antisymmetric A (Majoranas g)."""
    ev = np.linalg.eigvalsh(1j * Amat)
    pos = np.sort(ev[ev > 1e-12])
    nzero = int(np.sum(np.abs(ev) <= 1e-12)) // 2
    E0 = -0.5 * pos.sum()
    lev = np.array([E0])
    for p in pos:
        lev = np.concatenate([lev, lev + p])
    for _ in range(nzero):
        lev = np.concatenate([lev, lev])
    return np.sort(lev)


def cluster_test(name, verts_edges, model):
    """verts_edges: list of edges of the (sub)graph; vertices are their endpoints (global ids)."""
    edges = verts_edges
    verts = sorted({Gr.edges[e][0] for e in edges} | {Gr.edges[e][1] for e in edges})
    loc = {v: i for i, v in enumerate(verts)}
    N = len(verts); nqb = 3 * N
    # relabel Pauli strings to local qubits
    def relabel(P):
        k, x, z = P
        x2 = z2 = 0
        for v in verts:
            for t in range(3):
                if (x >> (3 * v + t)) & 1: x2 |= 1 << (3 * loc[v] + t)
                if (z >> (3 * v + t)) & 1: z2 |= 1 << (3 * loc[v] + t)
        return (k, x2, z2)
    H = sp.csr_matrix((2 ** nqb, 2 ** nqb), dtype=complex)
    rng = np.random.default_rng(abs(hash(name)) % 2 ** 32)
    Jv = {e: rng.uniform(0.5, 1.5) for e in edges}
    for e in edges:
        for cf, P in bond_terms(e, model, Jv[e]):
            H = H + cf * to_sparse(relabel(P), nqb)
    H = H.toarray()
    assert np.allclose(H, H.conj().T)
    # cycles of the cluster: faces of the lattice fully inside
    cyc = [(f, trav) for f, (_, trav, _) in enumerate(lat.faces) if all(e in edges for e, _ in trav)]
    Wm = [to_sparse(relabel(face_W(trav)), nqb).toarray() for _, trav in cyc]
    ok = all(np.allclose(H @ W, W @ H) for W in Wm)
    # H commutes with the W's and W^2 = 1, so the eigenvalues of H + sum_i kappa_i W_i are E + sum kappa_i s_i;
    # with kappa_i = 100 * 3^i >> ||H|| the sectors separate by value (eigenvalues only: fast)
    kap = [100.0 * 3 ** i for i in range(len(Wm))]
    Hp = H + sum(k * W for k, W in zip(kap, Wm))
    lam = np.linalg.eigvalsh(Hp)
    combos = list(itertools.product((1, -1), repeat=len(cyc)))
    offs = np.array([sum(k * s for k, s in zip(kap, c)) for c in combos])
    which = np.argmin(np.abs(lam[:, None] - offs[None, :]), axis=1)
    Hv = lam - offs[which]
    ok &= bool(np.max(np.abs(Hv)) < 40)
    Ws_val = np.array([[combos[w][i] for w in which] for i in range(len(cyc))]).reshape(len(cyc), -1)
    worst = 0.0; nsec = 0
    for signs in itertools.product((1, -1), repeat=len(cyc)):
        sel = np.all(np.round(Ws_val).T == np.array(signs), axis=1) if len(cyc) else np.ones(len(Hv), bool)
        Es = np.sort(Hv[sel])
        # free-fermion prediction: choose u with prod_{trav} u = (-1)^(n+1) W  for each cycle
        found = None
        for ubits in itertools.product((0, 1), repeat=len(edges)):
            uu = dict(zip(edges, [(-1) ** b for b in ubits]))
            good = True
            for (f, trav), s in zip(cyc, signs):
                pu = np.prod([uu[e] * sg for e, sg in trav])
                good &= pu == (-1) ** (len(trav) + 1) * s
            if good:
                found = uu; break
        nm = 8 * N   # all Majoranas of the cluster: b's dangling / gauge (zero modes here), c (and d) hop
        A = np.zeros((nm, nm))
        cidx = lambda q: 8 * loc[q] + 6
        didx = lambda q: 8 * loc[q] + 7
        def add(a, b, val):          # term val * (i g_a g_b)  ->  A_ab = 2 val, A_ba = -2 val
            A[a, b] += 2 * val; A[b, a] -= 2 * val
        for e in edges:
            I, Jx, _, _ = Gr.edges[e]
            t = Jv[e] * found[e]
            if model in ('M', 'M2'):
                add(cidx(I), cidx(Jx), t)
            if model == 'M2':
                add(didx(I), didx(Jx), t)
            if model == 'R':
                add(cidx(I), didx(Jx), t / 2); add(didx(I), cidx(Jx), -t / 2)
        lev = free_levels(A)
        uniq_s, cnt_s = np.unique(np.round(Es, 7), return_counts=True)
        uniq_p, cnt_p = np.unique(np.round(lev, 7), return_counts=True)
        same_levels = len(uniq_s) == len(uniq_p) and np.allclose(uniq_s, uniq_p, atol=1e-6)
        prop = same_levels and np.allclose(cnt_s / cnt_s.sum(), cnt_p / cnt_p.sum())
        ok &= bool(prop)
        worst = max(worst, np.inf if not same_levels else np.max(np.abs(uniq_s - uniq_p)))
        nsec += 1
    return ok, N, len(edges), len(cyc), nsec, worst


print("\nA2: exact diagonalisation of the qubit model on clusters vs free fermions in the dictionary's flux sector")
# clusters taken from faces at site 0, and an open 4-corner chain
def first_face(kind):
    for f, (k, trav, _) in enumerate(lat.faces):
        if k == kind:
            return [e for e, _ in trav]
tri = first_face('triangle'); sq = first_face('square'); pl = first_face('plaquette'); tu = first_face('tube')
chain = sq[:3]
CL = {'triangle (3 corners)': tri, 'square (4)': sq, 'plaquette (4, links)': pl, 'tube (4, mixed)': tu,
      'open chain (4)': chain}
for model in ('M', 'M2', 'R'):
    for name, edges in CL.items():
        if model != 'M' and not (name.startswith('triangle') or name.startswith('square') or name.startswith('tube')):
            continue
        ok, N, E, nc, nsec, worst = cluster_test(name, edges, model)
        check(f"H_{model} on {name}: qubit spectrum = free-fermion spectrum (levels and relative multiplicities) "
              f"in each of the {nsec} W sectors", ok, f"N={N}, E={E}, cycles={nc}, max level dev {worst:.1e}")
print(f"   t = {time.time()-T0:.1f}s")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
