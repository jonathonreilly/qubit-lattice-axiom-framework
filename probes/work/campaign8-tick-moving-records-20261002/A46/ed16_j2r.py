"""A46 ed16_j2r: 16-site cubic cluster, dual frame, H' = sum s.s + J2 sum_fd s.s + R sum_faces (P + P^-1)
(face diagonals: 6N oriented bonds, each unordered pair twice on this cluster, as in A44 star_j2).
Exact ground state vs the projected pi-flux singlet and the AF family, at points of the A46 window."""
import sys, time, signal, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
signal.alarm(250)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; bits = bits_table(N); plaq = plaquettes(cl)
HJ = sparse_terms(cl)["J"]; HR = ring_sparse(cl, plaq)
b = np.arange(2 ** N, dtype=np.int64); diag = np.zeros(2 ** N); rows, cols = [], []
for i, s in enumerate(cl.sites):
    for d in FD:
        j = cl.idx[tuple(cl.canon(np.array(s) + np.array(d))[0])]
        zi = 1 - 2 * ((b >> i) & 1); zj = 1 - 2 * ((b >> j) & 1); diag += zi * zj; sel = zi != zj
        rows.append((b ^ ((1 << i) | (1 << j)))[sel]); cols.append(b[sel])
r = np.concatenate(rows).astype(np.int32); c = np.concatenate(cols).astype(np.int32)
H2 = (sp.csr_matrix((np.full(len(r), 2.0), (r, c)), shape=(2 ** N, 2 ** N)) + sp.diags(diag)).tocsr(); del rows, cols, r, c
nb = 3 * N
st = {}
for m in (0.0, 0.1, 0.3, 1.0):
    Phi, gap = mf_dual(cl, 0., 1., m=m); p = projected_vector(Phi, bits); p /= np.linalg.norm(p)
    st[m] = (np.array([np.vdot(p, M @ p).real / nb for M in (HJ, H2, HR)]), p)
    print(f"m={m}: (e_J', fd per NN bond, ring) = {np.round(st[m][0], 5)}", flush=True)
print(" J2    R    | E0/bond (gap) | pi-flux E ov | best AF E (m) ov | FM")
for J2, R in ((0.25, -1.0), (0.3, -0.8), (0.4, -0.65), (0.25, -0.5), (0.0, -1.0)):
    H = HJ + J2 * H2 + R * HR
    vals, vecs = sla.eigsh(H, k=3, which='SA', tol=1e-8); o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
    deg = int(np.sum(vals - vals[0] < 1e-7)); gs = vecs[:, :deg]
    ov = lambda p: float(np.sum(np.abs(gs.conj().T @ p) ** 2))
    Jv = np.array([1., J2, R]); E = {m: (v @ Jv, ov(p)) for m, (v, p) in st.items()}
    mb = min((m for m in E if m > 0), key=lambda m: E[m][0])
    print(f" {J2:.2f} {R:+.2f} | {vals[0]/nb:+.5f} ({(vals[deg]-vals[0])/nb if deg < 3 else np.nan:.4f}, deg {deg}) | {E[0.0][0]:+.5f} {E[0.0][1]:.4f} | "
          f"{E[mb][0]:+.5f} ({mb}) {E[mb][1]:.4f} | {1 + 2*R + 2*J2:+.4f}", flush=True)
