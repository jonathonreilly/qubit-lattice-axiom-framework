"""K4: per-configuration vacuum ENERGY DENSITY (scalar sector) of the same frozen-Poisson toy (R3 C2 model, m2 = 1).
White if sd(E0/N)*sqrt(N) is constant.  A white static energy density sources a static Newtonian potential
with <Phi^2> growing linearly with region size R in 3D (the scalar twin of the TT tadpole in K1/K3)."""
import numpy as np, scipy.sparse as sps, scipy.linalg as sl
rng = np.random.default_rng(99); R = 1.8; m2 = 1.0
def E0(X, Lb):
    n = len(X); D = X[None] - X[:, None]; D -= Lb*np.round(D/Lb); d2 = np.einsum('ijk,ijk->ij', D, D)
    iu = np.triu_indices(n, 1); m = d2[iu] < R**2; w = (1 - d2[iu][m]/R**2)**4
    L = np.zeros((n, n)); L[iu[0][m], iu[1][m]] = -w; L = L + L.T; L[np.diag_indices(n)] = -L.sum(1)
    return 0.5*np.sqrt(np.clip(sl.eigvalsh(L), 0, None) + m2).mean()
for Lb, nr in [(6, 300), (8, 150), (10, 80), (12, 40)]:
    e = np.array([E0(rng.uniform(0, Lb, (Lb**3, 3)), Lb) for _ in range(nr)]); N = Lb**3
    print(f"N={N}: e0/site mean {e.mean():.5f}  sd {e.std(ddof=1):.2e}  sd*sqrtN {e.std(ddof=1)*np.sqrt(N):.4f} +- {e.std(ddof=1)*np.sqrt(N)/np.sqrt(2*(nr-1)):.4f}", flush=True)
