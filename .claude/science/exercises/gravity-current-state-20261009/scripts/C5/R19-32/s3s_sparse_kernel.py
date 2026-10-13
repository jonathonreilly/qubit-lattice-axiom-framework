"""R19-32 s3s (pre-registered 07:29Z): same test as s3 (formula lowering parts, dim V and best residual) for sizes beyond
dense reach, via the smallest eigenvalues of M^dag M per total-parity sector (sparse shift-invert at sigma = -1e-9).
dim V = number of eigenvalues below 1e-18 * ||M||^2 among the 6 smallest; min sing = sqrt(smallest eigenvalue)."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *
sec, L, tw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ds = [int(a) for a in sys.argv[4].split(',')]; nus = [float(a) for a in sys.argv[5].split(',')]
for d in ds:
    for nu in nus:
        t0 = time.time(); S = Sector(sec, L, d, nu, tw); Ds = S.constraints()
        par = np.zeros(S.dim, int); idx = np.arange(S.dim)
        for s in range(S.ns): par += (idx // S.d**(S.ns - s - 1)) % S.d
        par %= 2
        res = []
        for p in (0, 1):
            cols = np.where(par == p)[0]; rows = np.where(par != p)[0]
            M = sp.vstack([D[rows][:, cols] for D in Ds]).tocsc()
            MtM = (M.conj().T@M).tocsc()
            nrm = sla.norm(MtM, 1)
            ev = sla.eigsh(MtM, k=6, sigma=-1e-9, which='LM', return_eigenvectors=False)
            ev = np.sort(ev.real); res.append(ev)
        ev = np.sort(np.concatenate(res)); tol = 1e-12   # 07:38Z: kernel iff singular value < 1e-6 (shift-invert accuracy ~1e-7 in s; observed nonzero minima >= 4e-4)
        print(f"{sec} L={L} {'AP' if tw<0 else 'P '} d={d} nu={nu:.4f}: dim {S.dim}; dim V (among 12 smallest; >=6 per parity means more) = {(ev < tol).sum()}; "
              f"min sing = {np.sqrt(max(ev[0],0)):.3e}; next {np.round(np.sqrt(np.maximum(ev[1:4],0)),6)}  [{time.time()-t0:.1f}s]", flush=True)
