import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
from itertools import product

class Box:
    def __init__(self, n):
        self.n = n
        self.idx = {}
        self.pts = list(product(range(n), repeat=3))
        for i, p in enumerate(self.pts):
            self.idx[p] = i
        self.N = n**3
        c = n // 2
        self.c = c
        # bonds inside (interior), with eta; wall bonds listing
        bi, bj, eta = [], [], []
        wall_cnt = np.zeros(self.N)  # number of wall neighbours
        for p in self.pts:
            for mu in range(3):
                q = list(p); q[mu] += 1; q = tuple(q)
                if q in self.idx:
                    bi.append(self.idx[p]); bj.append(self.idx[q])
                    s = (-1) ** sum(p[:mu])
                    eta.append(s)
            for mu in range(3):
                for d in (-1, 1):
                    q = list(p); q[mu] += d
                    if tuple(q) not in self.idx:
                        wall_cnt[self.idx[p]] += 1
        self.bi = np.array(bi); self.bj = np.array(bj); self.eta = np.array(eta, float)
        self.wall_cnt = wall_cnt
        self.eps = np.array([(-1) ** (sum(p) - 3 * c) for p in self.pts], float)
        # Dirichlet laplacian (interior), Delta = sum_nbrs (f_y - f_x) incl. walls f=0 -> -(6) diag
        A = sp.coo_matrix((np.ones(len(bi)), (self.bi, self.bj)), shape=(self.N, self.N))
        A = A + A.T
        self.A = A.tocsr()
        self.L = (A - 6 * sp.identity(self.N)).tocsc()  # Delta with zero walls
        self.Lsolve = sla.splu(-self.L)
        self.center = self.idx[(c, c, c)]

    def G(self, src):
        return self.Lsolve.solve(src)


def solve(box, K, m, alpha=0.3, tol=1e-13, maxit=4000, init=None, verbose=False, hop=1.0):
    N = box.N
    chi = np.ones(N); Nn = np.ones(N)
    if init is not None:
        chi, Nn = init[0].copy(), init[1].copy()
    bi, bj, eta = box.bi, box.bj, box.eta
    for it in range(maxit):
        w = Nn / chi
        c = hop * np.sqrt(w[bi] * w[bj]) / (chi[bi] * chi[bj])
        H = np.zeros((N, N))
        H[bi, bj] = 0.5 * eta * c
        H[bj, bi] = 0.5 * eta * c
        H[np.arange(N), np.arange(N)] = m * box.eps * w
        ev, V = np.linalg.eigh(H)
        # lowest positive eigenvalue
        k = np.searchsorted(ev, 0.0)
        E = ev[k]; phi = V[:, k]
        r = m * box.eps * w * phi**2
        tb = eta * c * phi[bi] * phi[bj]
        tau = np.zeros(N)
        np.add.at(tau, bi, 0.5 * tb); np.add.at(tau, bj, 0.5 * tb)
        e = r + tau
        # inner field solve
        chin, Nnn = chi.copy(), Nn.copy()
        for _ in range(200):
            chi2 = 1 + box.G(e / (8 * K * Nnn))
            N2 = 1 - box.G((e + 2 * tau) / (8 * K * chi2))
            d = max(abs(chi2 - chin).max(), abs(N2 - Nnn).max())
            chin, Nnn = chi2, N2
            if d < 1e-15: break
        res = max(abs(chin - chi).max(), abs(Nnn - Nn).max())
        if verbose and it % 20 == 0: print(it, res, E)
        if res < tol:
            chi, Nn = chin, Nnn
            break
        chi = (1 - alpha) * chi + alpha * chin
        Nn = (1 - alpha) * Nn + alpha * Nnn
        if Nn.min() <= 0: raise RuntimeError("N<=0")
    return dict(chi=chi, N=Nn, phi=phi, E=E, r=r, tau=tau, e=e, tb=tb, res=res, it=it, H=H, w=Nn / chi)


def charges(box, K, S):
    chi, Nn, e, tau, tb, r = S['chi'], S['N'], S['e'], S['tau'], S['tb'], S['r']
    Q = (e / (8 * K * Nn)).sum()
    P = ((e + 2 * tau) / (8 * K * chi)).sum()
    # flux versions
    Qf = -(box.L @ (chi - 1)).sum() - 0  # sum Delta chi with chi-1 giving walls contributions
    # careful: Delta chi (with wall chi=1) = L@(chi-1)
    Qf = -(box.L @ (chi - 1)).sum()
    Pf = (box.L @ (Nn - 1)).sum()
    T = tb.sum()
    # F = -8K sum over bonds (N_y-N_x)(chi_y-chi_x) incl wall bonds; wall: N=chi=1
    dN = Nn[box.bj] - Nn[box.bi]; dc = chi[box.bj] - chi[box.bi]
    F = -8 * K * (dN * dc).sum()
    # wall bonds
    for ax in range(3):
        pass
    wall_term = -8 * K * (box.wall_cnt * (1 - Nn) * (1 - chi)).sum()
    F += wall_term
    return dict(Q=Q, P=P, Qf=Qf, Pf=Pf, T=T, F=F, Hrest=r.sum())


from scipy.optimize import brentq
def pinned(box, K, m):
    mu = m / (8 * K)
    e0 = np.zeros(box.N); e0[box.center] = 1.0
    g = box.G(e0); g0 = g[box.center]
    Q = brentq(lambda q: q * (1 + q * g0) - mu, 0, mu + 1)
    P = Q / (1 + 2 * Q * g0)
    chi = 1 + Q * g; Nn = 1 - P * g
    return chi, Nn, Q, P, g0, g
