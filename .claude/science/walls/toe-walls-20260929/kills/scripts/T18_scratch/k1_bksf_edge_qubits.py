"""K1 (kill check on T18): does a bounded-range rule on ENLARGED qubit space escape Lemma L?

Bravyi-Kitaev-superfast (BKSF) edge-qubit code on an Lx x Ly grid graph (fermion modes on vertices,
one qubit per EDGE, bounded-weight Pauli hop operators, local loop stabilisers).  Independent
re-implementation (does not import the repo's runner).

Checks
  (a) BKSF algebra: A_jk (Hermitian Pauli, weight <= deg_j+deg_k-1), B_j = prod Z on incident edges;
      anticommutation pattern of the Majorana-bilinear algebra;  loop product A_ij A_jk A_kl A_li.
  (b) On the joint loop-eigenspace singled out by the fermion algebra (product = +1), the encoded
      nearest-neighbour hop Hamiltonian H_q = -sum_{<jk>} (i/2) A_jk (B_j - B_k)  has, in each
      particle-number sector N (n_j = (1-B_j)/2), EXACTLY the spectrum of the free-fermion hop model
      with Jordan-Wigner signs (dense JW reference), and DIFFERS from the hard-core-boson hop model
      at N=2 (the attack's Test A discriminator: 2x2 / 2x3 / 3x3 grids).
  (c) contrast: the same graph with ONE qubit per vertex and NO constraints is the hard-core boson.
"""
import itertools, sys
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

X = sp.csr_matrix(np.array([[0, 1], [1, 0]], dtype=complex))
Z = sp.csr_matrix(np.array([[1, 0], [0, -1]], dtype=complex))
I2 = sp.identity(2, dtype=complex, format="csr")


def pauli_string(n, ops):
    """ops: dict qubit->'X'|'Z'; returns sparse matrix on n qubits (qubit 0 = most significant)"""
    M = None
    for q in range(n):
        f = {'X': X, 'Z': Z}.get(ops.get(q), I2)
        M = f if M is None else sp.kron(M, f, format="csr")
    return M


def grid(Lx, Ly):
    verts = [(x, y) for y in range(Ly) for x in range(Lx)]
    vid = {v: i for i, v in enumerate(verts)}
    edges = []
    for (x, y) in verts:
        if x + 1 < Lx:
            edges.append((vid[(x, y)], vid[(x + 1, y)]))
        if y + 1 < Ly:
            edges.append((vid[(x, y)], vid[(x, y + 1)]))
    return verts, vid, edges


def incident_order(verts, vid, edges):
    """per vertex: incident edge indices in the order -x < -y < +x < +y (repo uses -x<-y<-z<+x<+y<+z)"""
    inc = {i: [] for i in range(len(verts))}
    rank = {'-x': 0, '-y': 1, '+x': 2, '+y': 3}
    for ei, (a, b) in enumerate(edges):
        (xa, ya), (xb, yb) = verts[a], verts[b]
        if xb == xa + 1:
            inc[a].append((rank['+x'], ei)); inc[b].append((rank['-x'], ei))
        else:
            inc[a].append((rank['+y'], ei)); inc[b].append((rank['-y'], ei))
    return {i: [e for _, e in sorted(l)] for i, l in inc.items()}


class Bksf:
    def __init__(self, Lx, Ly):
        self.verts, self.vid, self.edges = grid(Lx, Ly)
        self.V, self.E = len(self.verts), len(self.edges)
        self.inc = incident_order(self.verts, self.vid, self.edges)
        self.eidx = {frozenset(e): i for i, e in enumerate(self.edges)}
        self.cache = {}

    def A_ops(self, i, j):
        """support dict of A_ij for i<j (A_ji = -A_ij)"""
        e = self.eidx[frozenset((i, j))]
        ops = {e: 'X'}
        for v in (i, j):
            for e2 in self.inc[v]:
                if e2 == e:
                    break
                ops[e2] = 'Z'
        return ops

    def A(self, i, j):
        if i > j:
            return -self.A(j, i)
        k = (i, j)
        if k not in self.cache:
            self.cache[k] = pauli_string(self.E, self.A_ops(i, j))
        return self.cache[k]

    def B(self, i):
        k = ('B', i)
        if k not in self.cache:
            self.cache[k] = pauli_string(self.E, {e: 'Z' for e in self.inc[i]})
        return self.cache[k]

    def faces(self):
        out = []
        for (x, y) in self.verts:
            if (x + 1, y + 1) in self.vid:
                out.append([self.vid[(x, y)], self.vid[(x + 1, y)], self.vid[(x + 1, y + 1)], self.vid[(x, y + 1)]])
        return out

    def loop(self, cyc):
        P = sp.identity(2 ** self.E, dtype=complex, format="csr")
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            P = P @ self.A(a, b)
        return P


# ---------- fermion (JW) and hard-core-boson references ----------
def jw_annihilators(n):
    a = []
    sm = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=complex))  # |0><1| lowers n=1 -> 0 (basis |0>,|1>)
    for j in range(n):
        M = None
        for q in range(n):
            f = Z if q < j else (sm if q == j else I2)
            M = f if M is None else sp.kron(M, f, format="csr")
        a.append(M)
    return a


def hop_fermion(verts_edges, n, t=-1.0):
    a = jw_annihilators(n)
    H = sp.csr_matrix((2 ** n, 2 ** n), dtype=complex)
    for (i, j) in verts_edges:
        h = a[i].getH() @ a[j]
        H = H + t * (h + h.getH())
    return H


def hop_boson(verts_edges, n, t=-1.0):
    sm = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=complex))
    def site(op, j):
        M = None
        for q in range(n):
            f = op if q == j else I2
            M = f if M is None else sp.kron(M, f, format="csr")
        return M
    H = sp.csr_matrix((2 ** n, 2 ** n), dtype=complex)
    for (i, j) in verts_edges:
        h = site(sm, i).getH() @ site(sm, j)
        H = H + t * (h + h.getH())
    return H


def number_diag(n):
    """particle number of each JW/boson basis state (basis |0>,|1> per site)"""
    N = np.zeros(2 ** n, int)
    for s in range(2 ** n):
        N[s] = bin(s).count("1")
    return N


def spectrum_by_N(H, Nvec, Ns):
    out = {}
    for N in Ns:
        idx = np.nonzero(Nvec == N)[0]
        sub = H[idx][:, idx].toarray()
        out[N] = np.sort(np.linalg.eigvalsh(sub))
    return out


def run(Lx, Ly, Ns=(0, 2, 4)):
    bk = Bksf(Lx, Ly)
    n_v, n_e = bk.V, bk.E
    print(f"\n=== {Lx}x{Ly} grid: {n_v} modes, {n_e} edge qubits, {len(bk.faces())} loop constraints")
    # (a) algebra checks
    max_w_A = max(len(bk.A_ops(i, j)) for (i, j) in bk.edges)
    max_w_B = max(len(bk.inc[i]) for i in range(n_v))
    print(f"  max Pauli weight of A_jk: {max_w_A}   of B_j: {max_w_B}   (bounded by degree, independent of grid size)")
    herm_bad = 0
    for (i, j) in bk.edges:
        M = bk.A(i, j)
        herm_bad += int(abs(M - M.getH()).sum() > 1e-12)
    print(f"  A_jk Hermitian: {herm_bad == 0}")
    # anticommutation pattern
    bad = 0; tot = 0
    for e1, e2 in itertools.combinations(bk.edges, 2):
        shared = len(set(e1) & set(e2))
        M1, M2 = bk.A(*e1), bk.A(*e2)
        comm = M1 @ M2 - M2 @ M1
        anti = M1 @ M2 + M2 @ M1
        want_anti = (shared == 1)
        ok = (abs(anti).sum() < 1e-9) if want_anti else (abs(comm).sum() < 1e-9)
        bad += (not ok); tot += 1
    print(f"  A-A (anti)commutation pattern (anticommute iff edges share one vertex): violations {bad}/{tot}")
    # loop products
    for f in bk.faces():
        P = bk.loop(f)
        herm = abs(P - P.getH()).sum() < 1e-9
        sq = abs(P @ P - sp.identity(2 ** n_e)).sum() < 1e-9
        print(f"  loop {f}: Hermitian={herm}  P^2=I={sq}", end="")
        d = P.diagonal()
        print(f"  (Pauli has X-part: {abs(P - sp.diags(d)).sum() > 1e-9}, i.e. NOT a diagonal Z-basis support condition)")
        break
    # (b) code space: joint +1 eigenspace of the loop products; check the fermion algebra wants +1
    n = n_e
    dim = 2 ** n
    Pen = sp.csr_matrix((dim, dim), dtype=complex)
    for f in bk.faces():
        P = bk.loop(f)
        Pen = Pen + (sp.identity(dim) - P) * 0.5  # projector onto P=-1 if P^2=1 & Hermitian
    Hq = sp.csr_matrix((dim, dim), dtype=complex)
    for (i, j) in bk.edges:
        Hq = Hq + (-1.0) * (0.5j) * (bk.A(i, j) @ (bk.B(i) - bk.B(j)))
    assert abs(Hq - Hq.getH()).sum() < 1e-9, "H_q not Hermitian"
    # particle number from B's
    nvec_diag = np.zeros(dim)
    for i in range(n_v):
        nvec_diag += (1 - bk.B(i).diagonal().real) / 2
    nvec_diag = np.rint(nvec_diag).astype(int)
    # commutation of H_q with the loop projectors
    cm = max(abs(Hq @ bk.loop(f) - bk.loop(f) @ Hq).sum() for f in bk.faces())
    print(f"  [H_q, loop] max deviation: {cm:.2e}   max weight of a hop term (Pauli): {max_w_A + max_w_B}")
    lam = 50.0
    res = {}
    for N in Ns:
        idx = np.nonzero(nvec_diag == N)[0]
        if len(idx) == 0:
            continue
        sub = (Hq + lam * Pen)[idx][:, idx].toarray()
        ev = np.sort(np.linalg.eigvalsh(sub))
        res[N] = ev[ev < lam / 2]
    # references
    edges_v = bk.edges
    HF = hop_fermion(edges_v, n_v)
    HB = hop_boson(edges_v, n_v)
    Nv = number_diag(n_v)
    sf = spectrum_by_N(HF, Nv, Ns)
    sb = spectrum_by_N(HB, Nv, Ns)
    for N in Ns:
        if N not in res:
            continue
        q, f, b = res[N], sf[N], sb[N]
        same_f = len(q) == len(f) and np.allclose(q, f, atol=1e-8)
        same_b = len(q) == len(b) and np.allclose(q, b, atol=1e-8)
        print(f"  N={N}: code-space dim {len(q)} (Fock dim {len(f)});  spec(BKSF) == spec(fermion JW): {same_f};  == spec(hard-core boson): {same_b}")
    return res


if __name__ == "__main__":
    for (Lx, Ly) in [(2, 2), (2, 3), (3, 3)]:
        run(Lx, Ly)
