"""C5 R9-9: exact finite-lattice check of the normalisation of the static paramagnetic TT self-energy.
Free real scalar on an L^3 torus, H = 1/2 pi.pi + 1/2 phi.K phi, central gradient (grad_j phi)(x) = (phi(x+e_j) - phi(x-e_j))/2
(symbol i sin k_j, u = sin^2 k_j).  Static T_2g perturbation  -h sum_x cos(q z) (grad_x phi)(grad_y phi)(x), no seagull.
Exact zero-point energy E0(h) = 1/2 tr sqrt(K0 - h K1).  Prediction: E0(h) - E0(0) = (N/4) Pi_para(0,q) h^2 + O(h^4),
Pi_para(0,q) = -(1/4) <|V|^2/(eps eps' (eps+eps'))>_k,  |V|^2 = 4 u_x u_y  (the formula used in r99_tt_selfenergy.py)."""
import numpy as np, itertools
m = 1.0
for L, nq in [(6, 1), (8, 1), (8, 2)]:
    N = L**3
    idx = lambda x, y, z: ((x % L)*L + (y % L))*L + (z % L)
    G = [np.zeros((N, N)) for _ in range(3)]
    for x, y, z in itertools.product(range(L), repeat=3):
        i = idx(x, y, z)
        for j, (dx, dy, dz) in enumerate([(1,0,0), (0,1,0), (0,0,1)]):
            G[j][i, idx(x+dx, y+dy, z+dz)] += 0.5; G[j][i, idx(x-dx, y-dy, z-dz)] -= 0.5
    K0 = m*m*np.eye(N) + sum(g.T @ g for g in G)
    q = 2*np.pi*nq/L
    zc = np.array([np.cos(q*z) for x, y, z in itertools.product(range(L), repeat=3)])
    C = np.diag(zc)
    K1 = G[0].T @ C @ G[1] + G[1].T @ C @ G[0]
    def E0(h):
        w = np.linalg.eigvalsh(K0 - h*K1)
        return 0.5*np.sum(np.sqrt(w))
    hs = 2e-3
    c2 = (E0(hs) + E0(-hs) - 2*E0(0))/(2*hs*hs)
    k = 2*np.pi*np.arange(L)/L
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    u = lambda a: np.sin(a)**2
    eps = np.sqrt(m*m + u(KX) + u(KY) + u(KZ)); epsp = np.sqrt(m*m + u(KX) + u(KY) + u(KZ - q))
    Pi = -0.25*np.mean(4*u(KX)*u(KY)/(eps*epsp*(eps+epsp)))
    print('L=%d q=%.4f: exact c2/N = %+.10e ; predicted Pi_para/4 = %+.10e ; ratio %.8f' % (L, q, c2/N, Pi/4, (c2/N)/(Pi/4)))
