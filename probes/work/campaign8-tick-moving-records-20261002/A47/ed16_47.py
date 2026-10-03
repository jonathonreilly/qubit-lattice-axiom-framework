"""A47 ed16_47: 16-site cubic cluster, dual frame, H' = sum_NN s.s + j sum_fd s.s at j = 0.3 (face diagonals
doubled on this cluster, as in A44/A46): exact ground state, its energy per NN bond, and overlaps with the
projected U(1) parton states lp:<x> and the weakly ordered projected states."""
import sys, signal, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
signal.alarm(200)
sys.path.insert(0, __file__.rsplit('/', 2)[0] + "/A46")
from a46lib import *
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; bits = bits_table(N)
HJ = sparse_terms(cl)["J"]
b = np.arange(2 ** N, dtype=np.int64); diag = np.zeros(2 ** N); rows, cols = [], []
for i, s in enumerate(cl.sites):
    for d in FD:
        j_ = cl.idx[tuple(cl.canon(np.array(s) + np.array(d))[0])]
        zi = 1 - 2 * ((b >> i) & 1); zj = 1 - 2 * ((b >> j_) & 1); diag += zi * zj; sel = zi != zj
        rows.append((b ^ ((1 << i) | (1 << j_)))[sel]); cols.append(b[sel])
r = np.concatenate(rows).astype(np.int32); c = np.concatenate(cols).astype(np.int32)
H2 = (sp.csr_matrix((np.full(len(r), 2.0), (r, c)), shape=(2 ** N, 2 ** N)) + sp.diags(diag)).tocsr(); del rows, cols, r, c
nb = 3 * N
for jv in (0.3,):
    H = HJ + jv * H2
    vals, vecs = sla.eigsh(H, k=3, which='SA', tol=1e-9); o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
    deg = int(np.sum(vals - vals[0] < 1e-7)); gs = vecs[:, :deg]
    print(f"j={jv}: exact E0/bond = {vals[0]/nb:+.5f} (degeneracy {deg}, next {vals[deg]/nb:+.5f})", flush=True)
    for lab, kw in [(f"lp:{x}", dict(lam2=x)) for x in (0.0, 0.1, 0.2, 0.3)] + [(f"neel:{m}", dict(m=m)) for m in (0.05, 0.1, 0.3)] + [(f"col:{m}", dict(m=m, pattern="collinear")) for m in (0.1, 0.4, 0.8)]:
        Phi, gap = mf_dual(cl, 0., 1., **kw)
        if gap < 1e-8: print(f"   {lab}: open shell"); continue
        p = projected_vector(Phi, bits); p /= np.linalg.norm(p)
        E = np.vdot(p, H @ p).real / nb; ov = float(np.sum(np.abs(gs.conj().T @ p) ** 2))
        print(f"   {lab:9s}: E/bond {E:+.5f}  overlap with exact ground space {ov:.4f}", flush=True)
