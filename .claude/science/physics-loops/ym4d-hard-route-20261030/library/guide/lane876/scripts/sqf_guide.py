# GUIDE only: check p_chi(a) <= (1+S_ev(a/2)) max(S_ev(a)^g, e^(-g a)), g=(kappa-1)/(8 kappa), on 2D Ising ring transfer operators
import numpy as np, itertools
def ising_strip(N, K):
    S = np.array(list(itertools.product([-1, 1], repeat=N)))
    intra = K*(S*np.roll(S, -1, axis=1)).sum(1)
    L = np.exp(0.5*intra[:, None] + 0.5*intra[None, :] + K*S@S.T)
    idx = {tuple(s): i for i, s in enumerate(S)}
    inv = np.array([idx[tuple(-s)] for s in S])
    return L, inv
worst = -1e9
for N in (6, 8):
    for K in (0.1, 0.2, 0.3, 0.4, 0.4407, 0.5, 0.6, 0.8):
        L, inv = ising_strip(N, K); n = L.shape[0]
        Pi = np.zeros((n, n)); Pi[np.arange(n), inv] = 1
        Pe = (np.eye(n)+Pi)/2; Po = (np.eye(n)-Pi)/2
        we = np.sort(np.linalg.eigvalsh(Pe@L@Pe))[::-1][:n//2]
        wo, Vo = np.linalg.eigh(Po@L@Po); wo_s = np.sort(wo)[::-1][:n//2]
        w, V = np.linalg.eigh(L); Om = np.abs(V[:, -1]); lam0 = w[-1]
        Psi = Vo[:, -1]; g = Psi/Om; kappa = ((Om**2)*g**4).sum()
        gam = (kappa-1)/(8*kappa)
        for a in (6, 8, 12, 20):
            Zo = (wo_s/lam0)**a; Ze = (we/lam0)**a
            p = Zo.sum()/Ze.sum(); Sev = Ze.sum()-1; Sev_half = ((we/lam0)**(a//2)).sum()-1
            bound = (1+Sev_half)*max(Sev**gam, np.exp(-gam*a))
            worst = max(worst, p-bound)
            if a == 12 and N == 8:
                print("N=%d K=%.4f a=%d kappa=%.3f gamma=%.4f p=%.3e S_ev=%.3e bound=%.3e" % (N, K, a, kappa, gam, p, Sev, bound))
print("max of p - bound over all cases:", worst)
