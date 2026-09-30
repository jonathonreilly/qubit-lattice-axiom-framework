"""Kill check T49: is M2 ("axiom group acts on the code by qubit permutation with trivial internal action, so that
A_ij -> +-A_{gi,gj}") true for the 09-03 Bravyi-Kitaev superfast encoding with direction order -x<-y<-z<+x<+y<+z?
Test on the 4^3 coarse torus (192 edge qubits): permute qubits by a proper cubic rotation about vertex 0 (and a translation),
compute the image of each A_ij as a Pauli string, and compare with A_{gi,gj}."""
import itertools, numpy as np
L = 4
def vid(x, y, z): return ((x % L) * L + (y % L)) * L + (z % L)
def vc(i): return (i // (L*L), (i // L) % L, i % L)
# direction order: -x<-y<-z<+x<+y<+z ; index 0..5
dirs = [(-1,0,0),(0,-1,0),(0,0,-1),(1,0,0),(0,1,0),(0,0,1)]
# edges: (v, a) means edge from v to v+e_a, a in 0..2  -> qubit index
qid = {}
for v in range(L**3):
    for a in range(3):
        qid[(v, a)] = len(qid)
nq = len(qid)
def edge_between(i, j):
    """qubit id of the edge joining i,j (nearest neighbours on the torus, L=4 so unique)"""
    ci, cj = vc(i), vc(j)
    for a in range(3):
        d = [0,0,0]; d[a] = 1
        if vid(ci[0]+d[0], ci[1]+d[1], ci[2]+d[2]) == j: return qid[(i, a)]
        if vid(cj[0]+d[0], cj[1]+d[1], cj[2]+d[2]) == i: return qid[(j, a)]
    raise ValueError
def incident(v):
    """list of (direction index, qubit id) at vertex v"""
    c = vc(v); out = []
    for k, d in enumerate(dirs):
        w = vid(c[0]+d[0], c[1]+d[1], c[2]+d[2])
        out.append((k, edge_between(v, w), w))
    return out
# Pauli as (xbits, zbits) numpy arrays; phase ignored (track only up to sign, we ask about Z-string ratios)
def pauli_A(i, j):
    x = np.zeros(nq, dtype=np.uint8); z = np.zeros(nq, dtype=np.uint8)
    e = edge_between(i, j); x[e] = 1
    for (a, b) in ((i, j), (j, i)):
        inc = incident(a)
        kk = [k for (k, q, w) in inc if w == b][0]
        for (k, q, w) in inc:
            if k < kk: z[q] ^= 1
    return x, z
def pauli_B(v):
    z = np.zeros(nq, dtype=np.uint8)
    for (k, q, w) in incident(v): z[q] ^= 1
    return np.zeros(nq, dtype=np.uint8), z
def qperm_from_vertex_map(f):
    """f: vertex coord tuple -> coord tuple (a lattice automorphism). Returns qubit permutation q -> q'."""
    perm = np.zeros(nq, dtype=int)
    for v in range(L**3):
        c = vc(v)
        for a in range(3):
            d = [0,0,0]; d[a] = 1
            w = tuple(c[t] + d[t] for t in range(3))
            fv, fw = f(c), f(w)
            perm[qid[(v, a)]] = edge_between(vid(*fv), vid(*fw))
    return perm
def apply_perm(p, xz):
    x, z = xz; nx = np.zeros(nq, dtype=np.uint8); nz = np.zeros(nq, dtype=np.uint8)
    nx[p] = x; nz[p] = z; return nx, nz
maps = {
  "C4z": lambda c: (-c[1], c[0], c[2]),
  "C4x": lambda c: (c[0], -c[2], c[1]),
  "C3 (xyz cyc)": lambda c: (c[1], c[2], c[0]),
  "C2z": lambda c: (-c[0], -c[1], c[2]),
  "Tx (coarse step)": lambda c: (c[0]+1, c[1], c[2]),
}
for name, f in maps.items():
    p = qperm_from_vertex_map(f)
    nbad = 0; ntot = 0; examples = []
    for i in range(L**3):
        ci = vc(i)
        for a in range(3):
            d = [0,0,0]; d[a] = 1
            j = vid(ci[0]+d[0], ci[1]+d[1], ci[2]+d[2])
            img = apply_perm(p, pauli_A(i, j))
            fi, fj = vid(*[t % L for t in f(ci)]), vid(*[t % L for t in f(vc(j))])
            tgt = pauli_A(fi, fj)
            ntot += 1
            if not (np.array_equal(img[0], tgt[0]) and np.array_equal(img[1], tgt[1])):
                nbad += 1
                if len(examples) < 1:
                    dz = np.nonzero(img[1] ^ tgt[1])[0]
                    examples.append((i, j, int(len(dz))))
    # B_v maps
    nbB = 0
    for v in range(L**3):
        img = apply_perm(p, pauli_B(v)); tgt = pauli_B(vid(*[t % L for t in f(vc(v))]))
        if not (np.array_equal(img[0], tgt[0]) and np.array_equal(img[1], tgt[1])): nbB += 1
    print(f"{name:18s}: A_ij images that differ from A_(gi,gj) even up to sign: {nbad}/{ntot}  (first example (i,j,#differing Z bits) = {examples[:1]});  B_v mismatches: {nbB}/{L**3}")

# ---- do rotations by pure qubit permutation even preserve the code space (face stabilizers S_f)? ----
def pauli_mul(p, q): return (p[0] ^ q[0], p[1] ^ q[1])
def S_face(v, a, b):
    """face spanned by e_a, e_b at vertex v: cycle v -> v+e_a -> v+e_a+e_b -> v+e_b -> v"""
    c = vc(v)
    def sh(cc, d): return tuple(cc[t] + d[t] for t in range(3))
    ea = [0,0,0]; ea[a] = 1; eb = [0,0,0]; eb[b] = 1
    p0, p1, p2, p3 = c, sh(c, ea), sh(sh(c, ea), eb), sh(c, eb)
    cyc = [p0, p1, p2, p3, p0]
    P = (np.zeros(nq, dtype=np.uint8), np.zeros(nq, dtype=np.uint8))
    for k in range(4):
        P = pauli_mul(P, pauli_A(vid(*cyc[k]), vid(*cyc[k+1])))
    return P
def face_key(cyc_pts):
    return frozenset(vid(*p) for p in cyc_pts)
faces = {}
for v in range(L**3):
    for (a, b) in ((0,1),(0,2),(1,2)):
        c = vc(v); ea=[0,0,0]; ea[a]=1; eb=[0,0,0]; eb[b]=1
        pts = [c, tuple(c[t]+ea[t] for t in range(3)), tuple(c[t]+ea[t]+eb[t] for t in range(3)), tuple(c[t]+eb[t] for t in range(3))]
        faces[face_key(pts)] = S_face(v, a, b)
print("\nCode-space preservation by pure qubit permutation: g(S_f) == +-S_{g f}?")
for name, f in maps.items():
    p = qperm_from_vertex_map(f)
    bad = 0
    for key, S in faces.items():
        pts = [vc(i) for i in key]
        gkey = frozenset(vid(*[t % L for t in f(c)]) for c in pts)
        img = apply_perm(p, S); tgt = faces[gkey]
        if not (np.array_equal(img[0], tgt[0]) and np.array_equal(img[1], tgt[1])): bad += 1
    print(f"  {name:18s}: faces whose stabilizer image differs (Pauli string, ignoring sign): {bad}/{len(faces)}")

# ---- can a diagonal Clifford (CZ/S dressing, X_e -> X_e Z^{w_e}) repair it?  Need W (rows w_e) symmetric. ----
print("\nDiagonal-Clifford soldering test: W[e,:] = Zpart(g(A_e)) xor Zpart(A_{g e}); needs W symmetric mod 2")
for name, f in maps.items():
    if name.startswith("Tx"): continue
    p = qperm_from_vertex_map(f)
    Wm = np.zeros((nq, nq), dtype=np.uint8)
    for i in range(L**3):
        ci = vc(i)
        for a in range(3):
            d = [0,0,0]; d[a] = 1
            j = vid(ci[0]+d[0], ci[1]+d[1], ci[2]+d[2])
            img = apply_perm(p, pauli_A(i, j))
            fi, fj = vid(*[t % L for t in f(ci)]), vid(*[t % L for t in f(vc(j))])
            tgt = pauli_A(fi, fj)
            e_img = np.nonzero(img[0])[0][0]
            Wm[e_img] = img[1] ^ tgt[1]
    sym = np.array_equal(Wm, Wm.T)
    print(f"  {name:14s}: W symmetric: {sym};  nonzeros: {int(Wm.sum())};  asymmetric entries: {int((Wm != Wm.T).sum())}")
