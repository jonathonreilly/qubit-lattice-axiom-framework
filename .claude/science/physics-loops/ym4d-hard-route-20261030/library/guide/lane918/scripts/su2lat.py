#!/usr/bin/env python3
"""GUIDE sampler for FINISH row 918 (decides nothing; no proof step rests on it).

4D SU(2) Wilson lattice gauge theory, weight exp(beta * sum_p c_p x_p), x_p = tr(U_p)/2, with a per-plaquette
coefficient field c_p (c = 1 Wilson, c = -1 a twisted plaquette, c = s an interpolation, c = 0 a free wall).
Links are unit quaternions. Direction 0 is time. Shape (L0, L1, L2, L3), all directions wrap; free walls are made
by c = 0 on every plaquette that contains a wrap-crossing link of that direction.

Updates: Kennedy-Pendleton/Creutz heat bath (the h1 sampler of typinf.py) and overrelaxation U -> V^+ U^+ V^+,
V = A/|A|. Both leave the conditional law of a link given the others invariant. Links of one direction are updated
in colour classes such that no two links of a class share a plaquette with nonzero coefficient: for each other
direction nu the class records x_nu mod 2 when L_nu is even or the direction is free, and a proper 3-colouring of
the cycle (x mod 2, with L-1 -> 2) when L_nu is odd and periodic. (Row 869 found a 2-colouring on an odd periodic
extent invalid; this partition avoids that.)
"""
import numpy as np
from scipy.special import ive

PLANES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
PIDX = {p: k for k, p in enumerate(PLANES)}


def pl_index(mu, nu):
    return PIDX[(min(mu, nu), max(mu, nu))]


def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    out = np.empty(np.broadcast(a0, b0).shape + (4,))
    out[..., 0] = a0*b0 - a1*b1 - a2*b2 - a3*b3
    out[..., 1] = a0*b1 + a1*b0 + a2*b3 - a3*b2
    out[..., 2] = a0*b2 - a1*b3 + a2*b0 + a3*b1
    out[..., 3] = a0*b3 + a1*b2 - a2*b1 + a3*b0
    return out


def qconj(a):
    c = a.copy(); c[..., 1:] *= -1; return c


class Lattice:
    def __init__(self, shape, beta, seed, free=(False, False, False, False)):
        self.shape = tuple(shape); self.beta = float(beta)
        self.free = tuple(free)
        self.V = int(np.prod(shape))
        self.rng = np.random.default_rng(seed)
        coords = np.indices(shape).reshape(4, -1)
        self.coords = coords
        lin = np.arange(self.V).reshape(shape)
        self.fwd = [np.roll(lin, -1, axis=m).ravel() for m in range(4)]
        self.bwd = [np.roll(lin, 1, axis=m).ravel() for m in range(4)]
        self.U = np.zeros((4, self.V, 4)); self.U[..., 0] = 1.0
        self.C = np.ones((6, self.V))
        for i in range(4):
            if free[i]:
                edge = coords[i] == shape[i] - 1
                for nu in range(4):
                    if nu != i:
                        self.C[pl_index(i, nu), edge] = 0.0
        self._classes()
        self.refresh()

    def _classes(self):
        self.classes = []
        for mu in range(4):
            key = np.zeros(self.V, dtype=np.int64); mult = 1
            par = np.zeros(self.V, dtype=np.int64)
            for nu in range(4):
                if nu == mu: continue
                L = self.shape[nu]; x = self.coords[nu]
                if L % 2 == 1 and not self.free[nu] and L > 1:
                    c = x % 2; c = np.where(x == L - 1, 2, c)
                    key += mult * c; mult *= 3
                else:
                    par += x
            key += mult * (par % 2)
            cl = [np.nonzero(key == k)[0] for k in np.unique(key)]
            self.classes.append(cl)

    def refresh(self):
        """Gather neighbour indices and coefficients per (direction, class). Call after changing C."""
        self.plan = []
        for mu in range(4):
            lst = []
            for idx in self.classes[mu]:
                terms = []
                for nu in range(4):
                    if nu == mu: continue
                    k = pl_index(mu, nu)
                    xp_mu = self.fwd[mu][idx]; xp_nu = self.fwd[nu][idx]
                    xm_nu = self.bwd[nu][idx]; xm_nu_p_mu = self.fwd[mu][xm_nu]
                    terms.append((nu, xp_mu, xp_nu, xm_nu, xm_nu_p_mu, self.C[k, idx], self.C[k, xm_nu]))
                lst.append((idx, terms))
            self.plan.append(lst)

    def staple(self, mu, idx, terms):
        U = self.U
        A = np.zeros((idx.size, 4))
        for (nu, xp_mu, xp_nu, xm_nu, xm_nu_p_mu, cf, cb) in terms:
            if np.any(cf != 0):
                f = qmul(qmul(U[nu][xp_mu], qconj(U[mu][xp_nu])), qconj(U[nu][idx]))
                A += cf[:, None] * f
            if np.any(cb != 0):
                b = qmul(qmul(qconj(U[nu][xm_nu_p_mu]), qconj(U[mu][xm_nu])), U[nu][xm_nu])
                A += cb[:, None] * b
        return A

    def _h1(self, k):
        out = np.empty_like(k); todo = np.arange(k.size)
        rng = self.rng
        while todo.size:
            kk = k[todo]; u = rng.random(todo.size)
            with np.errstate(divide='ignore', invalid='ignore'):
                x = 1.0 + np.log(u + (1.0 - u) * np.exp(-2.0 * kk)) / np.maximum(kk, 1e-300)
            x = np.where(kk < 1e-9, 2*u - 1, x)
            acc = rng.random(todo.size) < np.sqrt(np.clip(1 - x*x, 0, 1))
            out[todo[acc]] = x[acc]; todo = todo[~acc]
        return out

    def heatbath(self):
        b = self.beta
        for mu in range(4):
            for idx, terms in self.plan[mu]:
                A = self.staple(mu, idx, terms)
                k = np.sqrt((A*A).sum(axis=1))
                h = self._h1(b * k)
                v = self.rng.normal(size=(idx.size, 3)); v /= np.sqrt((v*v).sum(axis=1))[:, None]
                w = np.empty((idx.size, 4)); w[:, 0] = h; w[:, 1:] = np.sqrt(np.clip(1 - h*h, 0, 1))[:, None] * v
                Vh = qconj(A) / np.maximum(k, 1e-300)[:, None]
                new = qmul(w, Vh)
                zero = k < 1e-12
                if np.any(zero):  # Haar draw for decoupled links
                    g = self.rng.normal(size=(int(zero.sum()), 4)); g /= np.sqrt((g*g).sum(axis=1))[:, None]
                    new[zero] = g
                self.U[mu][idx] = new

    def overrelax(self):
        for mu in range(4):
            for idx, terms in self.plan[mu]:
                A = self.staple(mu, idx, terms)
                k = np.sqrt((A*A).sum(axis=1))
                ok = k > 1e-12
                Vq = A[ok] / k[ok][:, None]          # V = A/|A|
                Vd = qconj(Vq)
                Uo = self.U[mu][idx[ok]]
                self.U[mu][idx[ok]] = qmul(qmul(Vd, qconj(Uo)), Vd)

    def sweep(self, n_or=3):
        self.heatbath()
        for _ in range(n_or): self.overrelax()
        # re-unitarize against rounding drift
        for mu in range(4):
            n = np.sqrt((self.U[mu]**2).sum(axis=1)); self.U[mu] /= n[:, None]

    def plaquettes(self):
        """x_p for every plane and base site, shape (6, V)."""
        U = self.U; out = np.empty((6, self.V))
        for k, (mu, nu) in enumerate(PLANES):
            p = qmul(qmul(U[mu], U[nu][self.fwd[mu]]), qmul(qconj(U[mu][self.fwd[nu]]), qconj(U[nu])))
            out[k] = p[:, 0]
        return out

    def polyakov(self, mu):
        """Product of U_mu along direction mu starting at each site with x_mu = 0; returns tr/2 per site of the slice."""
        L = self.shape[mu]
        start = np.nonzero(self.coords[mu] == 0)[0]
        P = self.U[mu][start].copy(); cur = self.fwd[mu][start]
        for _ in range(L - 1):
            P = qmul(P, self.U[mu][cur]); cur = self.fwd[mu][cur]
        return start, P

    def spin_weights(self, plane_k, sites, nmax=11):
        """One-link-integrated estimator (row 860) of P(spin n/2 on plaquette) for plaquettes (plane_k, base sites),
        integrating the link U_mu(x), mu = first direction of the plane. Requires c_p = 1 on these plaquettes.
        Returns array (nmax+1, len(sites))."""
        mu, nu = PLANES[plane_k]
        b = self.beta; U = self.U
        # full staple for the link U_mu(x) at these sites
        terms = []
        for nn in range(4):
            if nn == mu: continue
            k = pl_index(mu, nn)
            xp_mu = self.fwd[mu][sites]; xp_nu = self.fwd[nn][sites]
            xm = self.bwd[nn][sites]; xm_p_mu = self.fwd[mu][xm]
            terms.append((nn, xp_mu, xp_nu, xm, xm_p_mu, self.C[k, sites], self.C[k, xm]))
        A = self.staple(mu, sites, terms)
        Sig = qmul(qmul(U[nu][self.fwd[mu][sites]], qconj(U[mu][self.fwd[nu][sites]])), qconj(U[nu][sites]))
        Ap = A - Sig
        kA = np.sqrt((A*A).sum(axis=1)); kp = np.sqrt((Ap*Ap).sum(axis=1))
        bA = b*kA; bp = b*kp
        c = (Ap*Sig).sum(axis=1)/kp
        # (2/b') I_{n+1}(b') / ((2/b) I_1(b)) with exponential scaling
        lnratio = (np.log(2/bp) - np.log(2/bA)) + (bp - bA)
        base = np.exp(lnratio) / ive(1, bA)
        ch = [np.ones_like(c), 2*c]
        for n in range(2, nmax+1): ch.append(2*c*ch[-1] - ch[-2])
        coef = [(n+1)*(2/b)*ive(n+1, b)*np.exp(b) for n in range(nmax+1)]
        out = np.empty((nmax+1, sites.size))
        for n in range(nmax+1):
            out[n] = coef[n] * base * ive(n+1, bp) * ch[n]
        return out


def binned_err(a, nb=10):
    a = np.asarray(a); m = (len(a)//nb)*nb
    if m < nb: return float('nan')
    bl = a[:m].reshape(nb, -1, *a.shape[1:]).mean(axis=1)
    return bl.std(axis=0, ddof=1)/np.sqrt(nb)


def sequential_sweep(lat):
    """Reference: one heat-bath update per link in a random order, no colouring (slow; validation only)."""
    order = lat.rng.permutation(4 * lat.V)
    b = lat.beta
    for code in order:
        mu = code // lat.V; s = np.array([code % lat.V])
        terms = []
        for nu in range(4):
            if nu == mu: continue
            k = pl_index(mu, nu)
            xp_mu = lat.fwd[mu][s]; xp_nu = lat.fwd[nu][s]; xm = lat.bwd[nu][s]; xm_p = lat.fwd[mu][xm]
            terms.append((nu, xp_mu, xp_nu, xm, xm_p, lat.C[k, s], lat.C[k, xm]))
        A = lat.staple(mu, s, terms); k = np.sqrt((A*A).sum(axis=1))
        h = lat._h1(b*k)
        v = lat.rng.normal(size=(1, 3)); v /= np.sqrt((v*v).sum())
        w = np.empty((1, 4)); w[:, 0] = h; w[:, 1:] = np.sqrt(max(0.0, 1 - h[0]**2)) * v
        lat.U[mu][s] = qmul(w, qconj(A)/k[:, None])


def improved_plaq(lat, plane_k, sites):
    """Conditional mean E[x_p | all links but U_mu(x)] for plaquettes (plane_k, base sites), mu = first direction of
    the plane: r(beta k) (A . Sigma)/k, r = I_2/I_1, A the full weighted staple of U_mu(x), Sigma the forward staple."""
    from scipy.special import ive as _ive
    mu, nu = PLANES[plane_k]; U = lat.U
    terms = []
    for nn in range(4):
        if nn == mu: continue
        k = pl_index(mu, nn)
        xp_mu = lat.fwd[mu][sites]; xp_nu = lat.fwd[nn][sites]
        xm = lat.bwd[nn][sites]; xm_p = lat.fwd[mu][xm]
        terms.append((nn, xp_mu, xp_nu, xm, xm_p, lat.C[k, sites], lat.C[k, xm]))
    A = lat.staple(mu, sites, terms)
    Sig = qmul(qmul(U[nu][lat.fwd[mu][sites]], qconj(U[mu][lat.fwd[nu][sites]])), qconj(U[nu][sites]))
    k = np.sqrt((A*A).sum(axis=1)); bk = lat.beta * k
    r = _ive(2, bk)/_ive(1, bk)
    return r * (A*Sig).sum(axis=1) / k
