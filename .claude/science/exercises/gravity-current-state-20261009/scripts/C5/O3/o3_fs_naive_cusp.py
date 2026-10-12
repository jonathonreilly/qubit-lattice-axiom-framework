# O3: strain applied to H directly (not through Q) on the M1 model: first-order (cusp) vacuum response
# from the degenerate E=0 manifold, versus E0(eps) == 0 when the same-channel deformation enters through Q.
import numpy as np, scipy.sparse.linalg as sla
from o3_fs_susy import torus, indep_sets, build, naive_strain
for (Lx,Ly,dense) in [(4,4,True),(4,6,False),(5,5,False)]:
    N, N1, N2x, N2y, dirx = torus(Lx,Ly)
    st = indep_sets(N,N1); idx = {s:a for a,s in enumerate(st)}
    Q0, H0 = build(N,N1,N2x,N2y,0.0,st,idx)
    def e0(M):
        if dense: return np.linalg.eigvalsh(M.toarray())[0]
        return sla.eigsh(M, k=1, which='SA', return_eigenvectors=False, tol=1e-13)[0]
    print("%dx%d torus (N=%d):" % (Lx,Ly,N))
    for e in [1e-3, 1e-2, 5e-2, 0.2]:
        ep, em = e0(naive_strain(H0,st,dirx,e)), e0(naive_strain(H0,st,dirx,-e))
        _, Hq = build(N,N1,N2x,N2y,e,st,idx)
        print("   eps=%6.3f  naive: E0(+)/N=%+.5e E0(-)/N=%+.5e  [E0/(N|eps|) = %.4f, %.4f]   via Q: E0=%+.1e" %
              (e, ep/N, em/N, ep/(N*e), em/(N*e), e0(Hq)))
