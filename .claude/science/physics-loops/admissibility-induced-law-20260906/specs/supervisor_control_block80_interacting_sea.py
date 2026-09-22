#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 80 (floating point; sparse exact diagonalisation; machinery disjoint from the exact runner).

W1  rings of 6, 8, 10 (reduced walk): the free sea against the hard-core (antisymmetric, one-per-site) many-record ground state at the filling that
    occupies the free negative branch: energy per site, second-order response Pi to u = eps cos(2 pi x/N), its local part and gradient part.
W2  2D tori 3x3, 4x3 with the two-dimensional walk: the same, at the filled-negative-branch filling (a jam) and at half filling.
W3  4x3 torus: the response to STRAINS through the reach-three coupling (isotropic stretch; traceless xx - yy) for the free sea, the half-filled
    crowd and the jammed filling, against the rates' response: does the interaction supply a lengths' stiffness?
"""
import itertools
import time
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


class Torus2:
    def __init__(self, Lx, Ly):
        self.Lx, self.Ly, self.n = Lx, Ly, Lx*Ly; self.grid = np.indices((Lx, Ly)).reshape(2, -1)
        self.T = [self.shift(a) for a in range(2)]
        self.S = [(t - t.T)/(2j) for t in self.T]; self.P = [(t@t - t.T@t.T)/(4j) for t in self.T]

    def shift(self, axis):
        g = self.grid.copy(); g[axis] = (g[axis] + 1) % (self.Lx, self.Ly)[axis]
        M = np.zeros((self.n, self.n)); M[np.arange(self.n), np.ravel_multi_index(g, (self.Lx, self.Ly))] = 1.0
        return M

    def hop(self, a, v): return 0.5*(np.diag(v)@self.T[a] + self.T[a].T@np.diag(v))

    def one_body(self, u, B=None):
        H = np.kron(self.S[0], sig[0]) + np.kron(self.S[1], sig[1])
        if B is not None:
            for a in range(2):
                for j in range(2):
                    if B[a][j] is None: continue
                    v = 0.5*(B[a][j] + self.T[a]@B[a][j])
                    H = H + 0.5*np.kron(self.hop(a, v)@self.P[j] + self.P[j]@self.hop(a, v), sig[a])
        Phi = np.kron(np.diag(np.exp(u/2)), np.eye(2)); return Phi@H@Phi


def one_body_ring(N, u):
    phi = np.exp(u/2); T = np.roll(np.eye(N), -1, axis=1); D = (T - T.T)/(2j)
    Phi = np.kron(np.diag(phi), np.eye(2)); return Phi@np.kron(D, sig[2])@Phi


def parity(perm):
    visited = [False]*len(perm); par = 0
    for k in range(len(perm)):
        if visited[k]: continue
        L = 0; j = k
        while not visited[j]: visited[j] = True; j = perm[j]; L += 1
        par += L - 1
    return -1 if par % 2 else 1


def hardcore_ground(H1, n_rec):
    """Ground energy of n_rec records with anticommuting composition under one-per-site exclusion (the compressed generator)."""
    d = H1.shape[0]; site = np.arange(d)//2
    basis = [s for s in itertools.combinations(range(d), n_rec) if len({site[o] for o in s}) == n_rec]
    index = {s: i for i, s in enumerate(basis)}
    by_o = {o: [o2 for o2 in range(d) if abs(H1[o2, o]) > 1e-14] for o in range(d)}
    rows, cols, vals = [], [], []
    for s, i in index.items():
        sset = set(s); sites_used = {site[o] for o in s}
        for pos, o in enumerate(s):
            for o2 in by_o[o]:
                if o2 != o and o2 in sset: continue
                if o2 != o and site[o2] != site[o] and site[o2] in sites_used: continue
                new = list(s); new[pos] = o2; order = sorted(range(n_rec), key=lambda k: new[k])
                rows.append(index[tuple(new[k] for k in order)]); cols.append(i); vals.append(parity(order)*H1[o2, o])
    Hm = sps.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))
    if len(basis) < 500: return np.linalg.eigvalsh(Hm.toarray())[0], len(basis)
    return spl.eigsh(Hm, k=1, which="SA", tol=1e-10)[0][0], len(basis)


def free_sea(H1):
    e = np.linalg.eigvalsh(H1); return e[e < 0].sum()


def second_order(E, mode, uniform, n, q2):
    E0 = E(0.0*mode); e1, e2 = 0.02, 0.04
    d1 = (E(e1*mode) + E(-e1*mode))/2 - E0; d2 = (E(e2*mode) + E(-e2*mode))/2 - E0
    c2 = (16*d1 - d2)/(12*e1**2)
    loc = (((E(e1*uniform) + E(-e1*uniform))/2 - E0)*16 - ((E(e2*uniform) + E(-e2*uniform))/2 - E0))/(12*e1**2)/2
    return E0/n, c2/n, loc/n, (c2 - loc)/n/q2


if __name__ == "__main__":
    print("[W1] rings (reduced walk), hard-core antisymmetric against free, mode cos(2 pi x/N), the free negative branch's filling:")
    for N in (6, 8, 10):
        x = np.arange(N); cos = np.cos(2*np.pi*x/N); q2 = 2 - 2*np.cos(2*np.pi/N); one = np.ones(N)
        n_neg = int((np.linalg.eigvalsh(one_body_ring(N, np.zeros(N))) < -1e-9).sum())
        out = []
        for label, E in (("free", lambda u: free_sea(one_body_ring(N, u))), ("hard-core", lambda u: hardcore_ground(one_body_ring(N, u), n_neg)[0])):
            e0, pi_, loc, grad = second_order(E, cos, one, N, q2)
            out.append(f"{label}: E0/site {e0:+.4f}, Pi {pi_:+.5f}, local {loc:+.5f}, gradient/q2 {grad:+.5f}")
        print(f"     ring N = {N}, {n_neg} records: " + "; ".join(out), flush=True)

    print("\n[W2] 2D tori with the two-dimensional walk, mode cos(2 pi x/Lx):")
    for Lx, Ly in ((3, 3), (4, 3)):
        tor = Torus2(Lx, Ly); n = tor.n; t0 = time.time()
        n_neg = int((np.linalg.eigvalsh(tor.one_body(np.zeros(n))) < -1e-9).sum())
        cos = np.cos(2*np.pi*tor.grid[0]/Lx); q2 = 2 - 2*np.cos(2*np.pi/Lx); one = np.ones(n)
        for n_rec, tag in ((n_neg, "the free branch's filling (a jam)"), (n//2, "half filling")):
            out = []
            gens = ((("free", lambda u: free_sea(tor.one_body(u))),) if n_rec == n_neg else ()) + (("hard-core", lambda u: hardcore_ground(tor.one_body(u), n_rec)[0]),)
            for label, E in gens:
                e0, pi_, loc, grad = second_order(E, cos, one, n, q2)
                out.append(f"{label}: E0/site {e0:+.4f}, Pi {pi_:+.5f}, local {loc:+.5f}, gradient/q2 {grad:+.5f}")
            dim = hardcore_ground(tor.one_body(np.zeros(n)), n_rec)[1]
            print(f"     {Lx}x{Ly}, {tag}: {n_rec} records of {n} sites (hard-core dim {dim}): " + "; ".join(out) + f" ({time.time() - t0:.0f} s)", flush=True)

    print("\n[W3] 4x3 torus: strains through the reach-three coupling against the rates (gradient parts per |q|^2):")
    tor = Torus2(4, 3); n = tor.n; cos = np.cos(2*np.pi*tor.grid[0]/4); one = np.ones(n); q2 = 2 - 2*np.cos(2*np.pi/4)
    n_neg = int((np.linalg.eigvalsh(tor.one_body(np.zeros(n))) < -1e-9).sum())
    none = [[None, None], [None, None]]
    modes = {"rates u": (lambda f: (f, none)), "isotropic stretch": (lambda f: (0*f, [[f, None], [None, f]])), "traceless xx - yy": (lambda f: (0*f, [[f, None], [None, -f]]))}
    for label, n_rec in (("free sea", None), ("hard-core half filling", n//2), ("hard-core jammed", n_neg)):
        t0 = time.time(); out = []
        for name, mk in modes.items():
            if n_rec is None:
                E = lambda f: free_sea(tor.one_body(*mk(f)))
            else:
                E = lambda f: hardcore_ground(tor.one_body(*mk(f)), n_rec)[0]
            e0, pi_, loc, grad = second_order(E, cos, one, n, q2)
            out.append(f"{name}: gradient/q2 {grad:+.5f} (total {pi_:+.5f}, local {loc:+.5f})")
        print(f"     {label} ({n_rec if n_rec else '-'} records): " + "; ".join(out) + f" ({time.time() - t0:.0f} s)", flush=True)
