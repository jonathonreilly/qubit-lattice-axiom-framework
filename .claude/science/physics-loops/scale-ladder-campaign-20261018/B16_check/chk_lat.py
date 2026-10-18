"""Independent lattice kernel for the B16 check (fresh code; imports nothing from B14/B16).

Conventions read from B14/B16 (not imported):
  * periodic L^3 torus, sites x, links (x,j) from x to x+e_j, plaquettes (y,(i,j)) i<j with
    F_ij(y) = A(y+i,j) - A(y,j) - A(y+j,i) + A(y,i);
  * canonical pairs (A_l, E_l); bracket {f,g} = df/dA dg/dE - df/dE dg/dA;
  * H_EM(N) = sum_l n_l(N) (g^2/2) E_l^2 + sum_p m_p(N) (c/(2 g^2)) F_p^2, with arbitrary linear lapse
    smearings n_l(N) = sum_s u[l][s] N_s, m_p(N) = sum_s w[p][s] N_s.

Instead of a generic polynomial Poisson bracket, the EM bracket is evaluated from the closed incidence
formula (derived by hand in REPORT notes):
  {H(N),H(M)} = c * sum_{k,p} dF_p/dA_k * E_k F_p * [ m_p(N) n_k(M) - n_k(N) m_p(M) ]
(g cancels identically).  A brute-force dense-matrix bracket (bf_bracket) cross-checks it.
"""
from fractions import Fraction as Fr
from itertools import product

import numpy as np


class Lat:
    def __init__(self, L):
        self.L = L
        self.sites = list(product(range(L), repeat=3))
        self.sidx = {x: i for i, x in enumerate(self.sites)}
        self.links = [(x, j) for x in self.sites for j in range(3)]
        self.lidx = {l: i for i, l in enumerate(self.links)}
        self.pairs = ((0, 1), (0, 2), (1, 2))
        self.plaqs = [(y, ij) for y in self.sites for ij in self.pairs]
        self.pidx = {p: i for i, p in enumerate(self.plaqs)}
        # F_p as dict link-index -> sign
        self.Fp = []
        for (y, (i, j)) in self.plaqs:
            d = {}
            for lk, s in (((self.sh(y, i), j), 1), ((y, j), -1), ((self.sh(y, j), i), -1), ((y, i), 1)):
                k = self.lidx[lk]
                d[k] = d.get(k, 0) + s
            self.Fp.append({k: v for k, v in d.items() if v})
        # incidence: link k -> list of (plaquette index, sign)
        self.inc = {k: [] for k in range(len(self.links))}
        for pi, d in enumerate(self.Fp):
            for k, s in d.items():
                self.inc[k].append((pi, s))

    def sh(self, x, j, s=1):
        return tuple((x[k] + (s if k == j else 0)) % self.L for k in range(3))

    def add(self, x, v):
        return tuple((x[k] + v[k]) % self.L for k in range(3))

    def is_bond(self, a, b):
        d = [(a[k] - b[k]) % self.L for k in range(3)]
        nz = [k for k in range(3) if d[k]]
        return len(nz) == 1 and d[nz[0]] in (1, self.L - 1)

    def corners(self, p):
        y, (i, j) = self.plaqs[p]
        return {"00": y, "10": self.sh(y, i), "01": self.sh(y, j), "11": self.sh(self.sh(y, i), j)}

    def div_matrix(self):
        D = np.zeros((len(self.sites), len(self.links)))
        for k, (x, j) in enumerate(self.links):
            D[self.sidx[x], k] -= 1  # link leaves x  (Gauss_x = sum_j E(x,j) - E(x-j,j) up to overall sign)
            D[self.sidx[self.sh(x, j)], k] += 1
        return -D  # Gauss_x = sum_j (E(x,j) - E(x-j,j))

    def transverse_projector(self):
        D = self.div_matrix()
        # projector onto ker D (orthogonal complement of the gradients, im D^T)
        Lap = D @ D.T
        Lp = np.linalg.pinv(Lap)
        return np.eye(len(self.links)) - D.T @ Lp @ D


def em_pair_coeffs(lat, u, w, c=Fr(1)):
    """u: list over links of dict site->weight; w: list over plaquettes of dict site->weight.
    Returns dict (s,t) [site tuples] -> dict (Eidx, Aidx) -> coeff, the coefficient of N_s M_t in {H(N),H(M)}.
    (Exact Fractions; uses the incidence formula.)"""
    out = {}

    def acc(s, t, key, v):
        if v == 0:
            return
        d = out.setdefault((s, t), {})
        d[key] = d.get(key, 0) + v
        if d[key] == 0:
            del d[key]

    for k in range(len(lat.links)):
        for (p, sg) in lat.inc[k]:
            for s, ws in w[p].items():
                for t, ut in u[k].items():
                    # term c sg E_k F_p [ w_ps u_kt N_s M_t - u_ks w_pt N_s M_t ]
                    for a, fa in lat.Fp[p].items():
                        v = c * sg * ws * ut * fa
                        acc(s, t, (k, a), v)
                        acc(t, s, (k, a), -v)
    return {k: v for k, v in out.items() if v}


def uniform_timing(lat, link_w, plaq_w):
    """link_w[j] = (u_tail, u_head); plaq_w[(i,j)] = dict corner-name -> weight."""
    u = []
    for (x, j) in lat.links:
        d = {}
        for s, wt in ((x, link_w[j][0]), (lat.sh(x, j), link_w[j][1])):
            if wt:
                d[s] = d.get(s, 0) + wt
        u.append(d)
    w = []
    for p, (y, ij) in enumerate(lat.plaqs):
        cs = lat.corners(p)
        d = {}
        for name, wt in plaq_w[ij].items():
            if wt:
                d[cs[name]] = d.get(cs[name], 0) + wt
        w.append(d)
    return u, w


# --------------------------------------------------------------- brute force dense bracket (float)
def em_quadform(lat, nl, mp, g2, c):
    """matrix M with H = 1/2 z^T M z, z = (A, E). nl, mp: numeric link / plaquette lapses."""
    nL = len(lat.links)
    M = np.zeros((2 * nL, 2 * nL))
    for k in range(nL):
        M[nL + k, nL + k] += g2 * nl[k]
    for p, d in enumerate(lat.Fp):
        v = np.zeros(nL)
        for a, s in d.items():
            v[a] = s
        M[:nL, :nL] += (c / g2) * mp[p] * np.outer(v, v)
    return M


def bf_bracket(Mf, Mg):
    n = Mf.shape[0] // 2
    Jm = np.zeros_like(Mf)
    Jm[:n, n:] = np.eye(n)
    Jm[n:, :n] = -np.eye(n)
    return Mf @ Jm @ Mg - Mg @ Jm @ Mf  # {f,g} = 1/2 z^T (this) z
