"""R15-1 (c): does the <N> = 1 CMC lapse collapse to zero in a black-hole throat?
Lapse equation (R14-5 Sec. 4.1): -D^2 N + Qt N = S(t), <N> = 1 (site/volume average), so N = N1/<N1>, -D^2 N1 + Qt N1 = 1, S = 1/<N1> > 0.
Maximum principle (proved in report): at the minimum of N, Qt N >= S, so N_min >= S / sup(Qt).
Toy: a 1D chain = throat (length ell, cross-section area A_t, Qt = Qth = 0.889/m^2, the maximal limiting surface r = 3m/2,
K_ij K^ij = 1.5 (4 sqrt3/9)^2/m^2) attached to a 'cosmos' (Qt = Qc, volume weight W_c).  Units m = 1.
Compare: (i) CMC with <N> = 1 (S > 0);  (ii) maximal-type S = 0 with N = 1 at the throat mouth (GR collapse of the lapse ~ exp(-sqrt(Qth) ell)).
"""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
Qth = 1.5*(4*np.sqrt(3)/9)**2
print(f"K_ijK^ij on r = 3m/2 limiting maximal surface = {Qth:.4f} / m^2")
def solve(ell, Qc, Lc=400.0, h=0.05, Wthroat=1.0, Wc=1e6):
    n_t = int(ell/h); n_c = int(Lc/h); n = n_t + n_c
    Q = np.concatenate([np.full(n_t, Qth), np.full(n_c, Qc)])
    main = 2/h**2 + Q; main[0] = 1/h**2 + Q[0]; main[-1] = 1/h**2 + Q[-1]   # Neumann both ends
    Aop = diags([main, -np.ones(n-1)/h**2, -np.ones(n-1)/h**2], [0, -1, 1], format='csc')
    N1 = spsolve(Aop, np.ones(n))
    w = np.concatenate([np.full(n_t, Wthroat/n_t if n_t else 0), np.full(n_c, Wc/n_c)])   # volume weights
    S = w.sum()/(w*N1).sum()
    N = S*N1
    # maximal-type: S = 0 inside throat, N = 1 at mouth: N = cosh(sqrt(Q)(x))/cosh(sqrt(Q) ell)
    Nmax = 1/np.cosh(np.sqrt(Qth)*ell)
    return N.min(), S, S/Q.max(), Nmax
for Qc in [1e-2, 1e-4]:
    print(f"cosmos Qt = {Qc:g} /m^2 (stands for ~1.35 H0^2; real value ~(mH0)^2 ~ 1e-46 for a stellar BH)")
    for ell in [1, 5, 10, 20, 40, 80]:
        Nmin, S, bound, Nmaxsl = solve(ell, Qc)
        print(f"   throat length {ell:3d} m: CMC <N>=1: N_min = {Nmin:.4e}, S = {S:.4e}, bound S/supQ = {bound:.4e}, ratio = {Nmin/bound:.4f} | maximal (S=0) throat lapse = {Nmaxsl:.3e}")
