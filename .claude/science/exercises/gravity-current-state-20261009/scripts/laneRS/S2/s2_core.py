"""Lane RS probe S2: staggered QED (Kogut-Susskind fermion + noncompact Yee photon, Coulomb gauge) on Z^d.
Conventions (self-contained): c_x = N^-1/2 sum_K e^{iKx} c_K, full-zone K = k + pi n, k in reduced zone [-pi/2,pi/2)^d,
n in {0,1}^d.  Hop (-i/2) eta_i(x) c+_x c_{x+i} + h.c., eta_i = (-1)^{x_1+..+x_{i-1}}  ->  K -> K + pi e_{<i}, amp sin K_i.
Mass m(-1)^{sum x} -> K -> K + pi(1..1), amp m.
O(e) vertex (absorb photon p, pol eps): K -> K + p + pi e_{<i}, amp eps_i cos(K_i + p_i/2)   [x 1/sqrt(2w)].
O(e^2) seagull (absorb p, emit p'): K -> K + p - p' + pi e_{<i}, amp -eps_i eps'_i sin(K_i + (p_i-p'_i)/2)  [x 1/sqrt(4ww')].
Coulomb: (e^2/2) sum rho G rho, G(q) = 1/sum 4 sin^2(q_i/2); density vertex K -> K + q, amp 1.
Photon: w(p) = sqrt(sum 4 sin^2(p_i/2)), transverse to s(p) = 2 sin(p/2)."""
import itertools
import numpy as np

def nodes(d): return np.array(list(itertools.product(range(2), repeat=d)))
def wrapr(k): return (k + np.pi/2) % np.pi - np.pi/2          # reduced zone
def wrapf(k): return (k + np.pi) % (2*np.pi) - np.pi          # full zone
def eps(k, m): return np.sqrt(np.sum(np.sin(k)**2, axis=-1) + m*m)
def omega(p): return np.sqrt(np.sum(4*np.sin(p/2)**2, axis=-1))
def Gc(q): return 1.0/np.sum(4*np.sin(q/2)**2, axis=-1)

class Stag:
    def __init__(self, d, m):
        self.d, self.m = d, m
        self.N = nodes(d); self.nn = len(self.N)
        self.idx = {tuple(n): a for a, n in enumerate(self.N)}
        self.elt = [np.array([1 if j < i else 0 for j in range(d)]) for i in range(d)]
    def ix(self, n): return self.idx[tuple(np.asarray(n) % 2)]
    def h(self, k):
        H = np.zeros((self.nn, self.nn))
        for a, n in enumerate(self.N):
            K = k + np.pi*n
            for i in range(self.d):
                H[self.ix(n + self.elt[i]), a] += np.sin(K[i])
            H[self.ix(n + 1), a] += self.m
        return H
    def Uplus(self, k):
        w, U = np.linalg.eigh(self.h(k))
        e = eps(k, self.m)
        sel = np.nonzero(np.abs(w - e) < 1e-8)[0]
        assert len(sel) == self.nn//2, (w, e)
        return U[:, sel]
    def shift(self, kin, Q, kout):
        s = (kin + Q - kout)/np.pi
        si = np.round(s).astype(int); assert np.allclose(s, si, atol=1e-9), s
        return si
    def dens(self, kin, Q, kout):
        """density vertex, full-zone transfer Q, from reduced kin to reduced kout"""
        sh = self.shift(kin, Q, kout); M = np.zeros((self.nn, self.nn))
        for a, n in enumerate(self.N): M[self.ix(n + sh), a] = 1.0
        return M
    def vert(self, kin, Q, kout, i):
        """O(e) vertex, component i, absorbing full-zone momentum Q (Q -> -Q for emission of +Q)"""
        sh = self.shift(kin, Q, kout); M = np.zeros((self.nn, self.nn))
        for a, n in enumerate(self.N):
            K = kin + np.pi*n
            M[self.ix(n + sh + self.elt[i]), a] += np.cos(K[i] + Q[i]/2)
        return M
    def seag(self, kin, Q, kout, i):
        """seagull bond operator, component i, net absorbed momentum Q = p - p'"""
        sh = self.shift(kin, Q, kout); M = np.zeros((self.nn, self.nn))
        for a, n in enumerate(self.N):
            K = kin + np.pi*n
            M[self.ix(n + sh + self.elt[i]), a] += np.sin(K[i] + Q[i]/2)
        return M

def transverse(p, d):
    s = 2*np.sin(p/2); ns = np.linalg.norm(s)
    if d == 1: return np.zeros((1, 0))
    sh = s/ns
    Pi = np.eye(d) - np.outer(sh, sh)
    w, V = np.linalg.eigh(Pi)
    return V[:, w > 0.5]          # d x (d-1) orthonormal transverse basis

def moller_T(S, k1, k2, k3, k4, include_tr=True, return_parts=False):
    """Born O(e^2) Moller amplitude on + band, antisymmetrised, as (n+^2 x n+^2) matrix [(a@k3,b@k4),(c@k1,d@k2)]."""
    d = S.d; m = S.m
    U = [S.Uplus(k) for k in (k1, k2, k3, k4)]
    e1, e2, e3, e4 = [eps(k, m) for k in (k1, k2, k3, k4)]
    def direct(ka, kb, kc, kd, Ua, Ub, Uc, Ud, ea, eb, ec, ed):
        # particle at ka -> kc, particle at kb -> kd; returns [(c-int, d-int),(a-int,b-int)]
        npl = Ua.shape[1]; T = np.zeros((npl*npl, npl*npl), complex); minden = np.inf
        for mvec in itertools.product(range(2), repeat=d):
            Q = wrapf(ka - kc + np.pi*np.array(mvec))     # photon momentum flowing from particle a to particle b
            if np.linalg.norm(Q) < 1e-9: continue
            A1 = Uc.conj().T @ S.dens(ka, -Q, kc) @ Ua
            A2 = Ud.conj().T @ S.dens(kb, Q, kd) @ Ub
            T += Gc(Q)*np.kron(A1, A2)
            if include_tr and d > 1:
                w = omega(Q); Dl = ea - ec
                den = w*w - Dl*Dl; minden = min(minden, abs(den)/w**2)
                Pt = transverse(Q, d); Pi = Pt @ Pt.T
                V1 = [Uc.conj().T @ S.vert(ka, -Q, kc, i) @ Ua for i in range(d)]
                V2 = [Ud.conj().T @ S.vert(kb, Q, kd, j) @ Ub for j in range(d)]
                for i in range(d):
                    for j in range(d):
                        if abs(Pi[i, j]) > 1e-14:
                            T -= Pi[i, j]*np.kron(V1[i], V2[j])/den
        return T, minden
    Td, md1 = direct(k1, k2, k3, k4, U[0], U[1], U[2], U[3], e1, e2, e3, e4)   # [(a3,b4),(c1,d2)]
    Tx, md2 = direct(k1, k2, k4, k3, U[0], U[1], U[3], U[2], e1, e2, e4, e3)   # [(b4,a3),(c1,d2)]
    n = U[0].shape[1]
    Tx = Tx.reshape(n, n, n*n).transpose(1, 0, 2).reshape(n*n, n*n)
    T = Td - Tx
    if return_parts: return T, U, min(md1, md2)
    return T, U

def sample_moller(S, ns, rng, mode='generic', kscale=1.0, grid=801, maxtries=None):
    d, m = S.d, S.m; out = []; tries = 0
    g = np.linspace(-np.pi/2, np.pi/2, grid)
    maxtries = maxtries or ns*300
    while len(out) < ns and tries < maxtries:
        tries += 1
        if mode == 'lowK':
            k1 = rng.uniform(-np.pi/2, np.pi/2, d); k2 = wrapr(-k1 + rng.normal(0, 0.15, d))
        elif mode == 'lowE':
            k1 = rng.normal(0, 0.35*kscale, d); k2 = rng.normal(0, 0.35*kscale, d)
        else:
            k1 = rng.uniform(-np.pi/2, np.pi/2, d); k2 = rng.uniform(-np.pi/2, np.pi/2, d)
        k1, k2 = wrapr(k1), wrapr(k2)
        E = eps(k1, m) + eps(k2, m); K = k1 + k2
        k30 = rng.uniform(-np.pi/2, np.pi/2, d) if mode != 'lowE' else wrapr(rng.normal(0, 0.35*kscale, d))
        ax = rng.integers(d)
        T = np.tile(k30, (len(g), 1)); T[:, ax] = g
        fv = eps(T, m) + eps(wrapr(K - T), m) - E
        idx = np.nonzero(np.sign(fv[:-1])*np.sign(fv[1:]) < 0)[0]
        for ii in idx:
            a, b = g[ii], g[ii+1]
            def F(t):
                x = k30.copy(); x[ax] = t; return eps(x, m) + eps(wrapr(K - x), m) - E
            fa = F(a)
            for _ in range(70):
                c = 0.5*(a+b); fc = F(c)
                if np.sign(fa)*np.sign(fc) <= 0: b = c
                else: a, fa = c, fc
            k3 = k30.copy(); k3[ax] = 0.5*(a+b); k3 = wrapr(k3); k4 = wrapr(K - k3)
            same = lambda x, y: np.max(np.abs(wrapr(x - y))) < 1e-5
            if (same(k3, k1) and same(k4, k2)) or (same(k3, k2) and same(k4, k1)): continue
            if min(np.max(np.abs(wrapr(k3-k1))), np.max(np.abs(wrapr(k3-k2)))) < 1e-3: continue
            out.append((k1, k2, k3, k4))
            if len(out) >= ns: break
    return out

def odd_basis(d, R):
    ms = [np.array(v) for v in itertools.product(range(-R, R+1), repeat=d)]
    return np.array([v for v in ms if any(v) and [x for x in v if x != 0][0] > 0])

def nullity(sv, ncols, atol=1e-10, rtol=1e-9):
    thr = max(atol, rtol*(sv[0] if len(sv) else 0))
    return int(np.sum(sv < thr)) + max(0, ncols - len(sv))
