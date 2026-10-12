# O3: massive (staggered) M1 chain, Q = sum_i lam_i c_i^dag P_i, lam = 1 (even i), lam (odd i).
# Unbroken SUSY => every E>0 level is a doublet between fermion-number sectors F, F+1.
# Question: do the lowest massive excitations come with L-independent partner levels (degenerate partners)?
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
from o3_fs_susy import torus, indep_sets
def build_stag(L, lam):
    N, N1, _, _, _ = torus(L,1)
    st = indep_sets(N,N1); idx = {s:a for a,s in enumerate(st)}
    r,c,v = [],[],[]
    for a,s in enumerate(st):
        for i in range(N):
            if (s>>i)&1 or any((s>>j)&1 for j in N1[i]): continue
            t = s|(1<<i); sg = -1.0 if bin(s&((1<<i)-1)).count('1')%2 else 1.0
            r.append(idx[t]); c.append(a); v.append(sg*(lam if i%3==0 else 1.0))
    D = len(st); Q = sp.csr_matrix((v,(r,c)),shape=(D,D)); H = (Q@Q.T+Q.T@Q).tocsr()
    F = np.array([bin(s).count('1') for s in st]); return H, F, st
for lam in [0.4, 2.0]:
    print("staggered M1 chain, lam(i%%3==0) = %.2f" % lam)
    for L in [12, 18, 24]:
        H, F, st = build_stag(L, lam)
        W = int(np.sum((-1.0)**F))
        out = []
        for f in range(L//3-2, L//3+3):
            idxs = np.where(F==f)[0]
            if len(idxs)==0: continue
            Hf = H[idxs][:,idxs]
            k = min(4, len(idxs)-1)
            ev = np.sort(np.linalg.eigvalsh(Hf.toarray())) if len(idxs) < 1500 else np.sort(sla.eigsh(Hf, k=k, which='SA', return_eigenvectors=False, tol=1e-12))
            out.append((f, ev[:4]))
        print("  L=%d  W=%+d" % (L, W))
        for f, ev in out:
            print("     F=%2d lowest: %s" % (f, np.array2string(ev, precision=6, suppress_small=True)))
