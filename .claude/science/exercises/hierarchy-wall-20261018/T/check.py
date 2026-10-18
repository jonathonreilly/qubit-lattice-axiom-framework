"""validation: K=0 iid; mu=0 nucleation fraction 1/(1+2d) (landed uniform-race value); score-derivative vs finite difference; timing"""
import numpy as np, time
from sim import nbr_table, many_runs, observables
for d, L in ((2, 64), (3, 16)):
    nb = nbr_table(L, d); N = L ** d
    t0 = time.time(); st, sc = many_runs(nb, N, 2 * d, 0.0, 0.0, 1, 8); t1 = time.time()
    st, sc = many_runs(nb, N, 2 * d, 0.0, 0.0, 1, 64); t2 = time.time()
    o = observables(st.reshape((64,) + (L,) * d), d)
    print(f"d={d} L={L}: compile+8 {t1-t0:.1f}s, 64 runs {t2-t1:.3f}s ({(t2-t1)/64/N*1e9:.0f} ns/site wall)")
    print(f"  K=0: nn={o[:,0].mean():+.4f}+-{o[:,0].std()/8:.4f} plaq={o[:,1].mean():+.4f}")
    print(f"  mu=0 nucleation fraction {sc[:,2].mean()/N:.4f} vs 1/(1+2d) = {1/(1+2*d):.4f} (+- {sc[:,2].std()/8/N:.4f})")
    for mu in (2.0, 4.0, 6.0):
        st, sc = many_runs(nb, N, 2 * d, 1.0, mu, 3, 32)
        print(f"  mu={mu}: nucleation fraction {sc[:,2].mean()/N:.5f}")
# score-function derivative check vs finite differences (d=2, L=32)
d, L = 2, 32; nb = nbr_table(L, d); N = L ** d; S = 4000
K0, mu0, h = 0.6, 1.0, 0.08
def A(K, mu, seed):
    st, sc = many_runs(nb, N, 4, K, mu, seed, S)
    o = observables(st.reshape((S, L, L)), 2)
    return o, sc
o, sc = A(K0, mu0, 11)
oc = o - o.mean(0); scc = sc[:, :2] - sc[:, :2].mean(0)
J = (oc[:, :, None] * scc[:, None, :]).mean(0)
oKp, _ = A(K0 + h, mu0, 21); oKm, _ = A(K0 - h, mu0, 31)
oMp, _ = A(K0, mu0 + h, 41); oMm, _ = A(K0, mu0 - h, 51)
fdK = (oKp.mean(0) - oKm.mean(0)) / (2 * h); fdM = (oMp.mean(0) - oMm.mean(0)) / (2 * h)
print("score dA/dK ", np.round(J[:, 0], 4)); print("fd    dA/dK ", np.round(fdK, 4))
print("score dA/dmu", np.round(J[:, 1], 4)); print("fd    dA/dmu", np.round(fdM, 4))
