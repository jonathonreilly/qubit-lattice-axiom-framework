#!/usr/bin/env python3
"""Core for gate_ex: SU(2) lattice in d dims, Balaban comb block map, true constrained Wilson minimiser. Criteria: CRITERIA.md."""
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import scipy.sparse.linalg as sla
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


def qmul(a, b):
    w = a[..., 0] * b[..., 0] - (a[..., 1:] * b[..., 1:]).sum(-1)
    v = a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:] + torch.linalg.cross(a[..., 1:], b[..., 1:], dim=-1)
    return torch.cat([w[..., None], v], -1)


def qinv(a):
    return torch.cat([a[..., :1], -a[..., 1:]], -1)


def qexp(t):
    n2 = (t * t).sum(-1, keepdim=True)
    small = n2 < 1e-6
    nn = torch.sqrt(torch.clamp(n2, min=1e-12))
    s = torch.where(small, 1 - n2 / 6 + n2 * n2 / 120, torch.sin(nn) / nn)
    c = torch.where(small, 1 - n2 / 2 + n2 * n2 / 24, torch.cos(nn))
    return torch.cat([c, s * t], -1)


def qlog(q):
    w = q[..., :1]
    v = q[..., 1:]
    t = (v * v).sum(-1, keepdim=True) / (w * w)
    small = t < 1e-6
    r = torch.sqrt(torch.clamp(t, min=1e-12))
    s = torch.where(small, 1 - t / 3 + t * t / 5 - t**3 / 7, torch.atan(r) / r)
    return s * v / w


def rot(q, v):
    """q v q^-1 on 3-vectors."""
    q0 = torch.cat([torch.zeros_like(v[..., :1]), v], -1)
    return qmul(qmul(q, q0), qinv(q))[..., 1:]


def ident(shape):
    x = torch.zeros(tuple(shape) + (4,))
    x[..., 0] = 1
    return x


def plaquettes(U):
    """U shape (N..., d, 4). Returns list of ((mu, nu), plaq at x)."""
    d = U.shape[-2]
    out = []
    for mu in range(d):
        for nu in range(mu + 1, d):
            a = U[..., mu, :]
            b = torch.roll(U[..., nu, :], -1, dims=mu)
            c = qinv(torch.roll(U[..., mu, :], -1, dims=nu))
            e = qinv(U[..., nu, :])
            out.append(((mu, nu), qmul(qmul(qmul(a, b), c), e)))
    return out


def centres(shape, d, spacing=1.0):
    g = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) * spacing for n in shape[:d]], indexing="ij")
    return g


def wilson(U, W=None):
    """W: None or callable(pos tuple in *this lattice's* cell units as array, mu, nu) -> weight array."""
    tot = 0.0
    for (mu, nu), p in plaquettes(U):
        dens = 2 * (1 - p[..., 0])
        if W is not None:
            dens = dens * W(mu, nu)
        tot = tot + dens.sum()
    return tot


def flux_stats(V):
    d = V.shape[-2]
    ps = plaquettes(V)
    th = [qlog(p) for _, p in ps]
    f = max(float(torch.sqrt((t * t).sum(-1)).max()) for t in th)
    E = sum(float((t * t).sum()) for t in th)
    return f, E


def I_grad(V, W=None, theta=None):
    d = V.shape[-2]
    th = [qlog(p) for _, p in plaquettes(V)] if theta is None else theta
    tot = 0.0
    for idx, t in enumerate(th):
        for e in range(d):
            tp = rot(V[..., e, :], torch.roll(t, -1, dims=e))
            dens = ((tp - t) ** 2).sum(-1)
            if W is not None:
                dens = dens * W(idx, e)
            tot = tot + dens.sum()
    return tot


class Block:
    """One step of the comb block map from an n^d fine torus to (n/L)^d."""

    def __init__(self, n, L, d, order=None):
        assert L % 2 == 1 and n % L == 0
        self.n, self.L, self.d = n, L, d
        self.Np = n // L
        r = (L - 1) // 2
        self.r = r
        self.order = list(range(d)) if order is None else list(order)
        offs = list(itertools.product(range(-r, r + 1), repeat=d))
        self.offs = offs
        self.index = {o: i for i, o in enumerate(offs)}
        sort = sorted(offs, key=lambda o: self._stage(o))
        self.sequence = []
        for o in sort:
            if all(x == 0 for x in o):
                continue
            a = max(self.order.index(i) for i in range(d) if o[i] != 0)
            ax = self.order[a]
            s = 1 if o[ax] > 0 else -1
            p = list(o)
            p[ax] -= s
            self.sequence.append((o, tuple(p), ax, s))
        grids = torch.meshgrid(*[torch.arange(self.Np) * L for _ in range(d)], indexing="ij")
        self.base = torch.stack(grids, 0).reshape(d, -1)  # d x Np^d block centres

    def _stage(self, o):
        st = -1
        tot = 0
        for pos, ax in enumerate(self.order):
            if o[ax] != 0:
                st = pos
                tot = abs(o[ax])
        return (st, tot)

    def link(self, U, sites, mu):
        idx = tuple(sites[i] % self.n for i in range(self.d))
        return U[idx + (mu,)]

    def __call__(self, U):
        d, L, Np = self.d, self.L, self.Np
        m = Np**d
        G = [None] * len(self.offs)
        G[self.index[tuple([0] * d)]] = ident((m,))
        for o, p, ax, s in self.sequence:
            sites = self.base + torch.tensor(p).reshape(d, 1)
            if s > 0:
                step = self.link(U, sites, ax)
            else:
                sites2 = sites.clone()
                sites2[ax] -= 1
                step = qinv(self.link(U, sites2, ax))
            G[self.index[o]] = qmul(G[self.index[p]], step)
        G = torch.stack(G, 1).reshape((Np,) * d + (len(self.offs), 4))
        out = []
        for mu in range(d):
            lines = []
            for io, o in enumerate(self.offs):
                sites = self.base + torch.tensor(o).reshape(d, 1)
                ln = self.link(U, sites, mu)
                for t in range(1, L):
                    sites2 = sites.clone()
                    sites2[mu] += t
                    ln = qmul(ln, self.link(U, sites2, mu))
                lines.append(ln)
            lines = torch.stack(lines, 1).reshape((Np,) * d + (len(self.offs), 4))
            Gp = torch.roll(G, -1, dims=mu)
            Om = qmul(qmul(G, lines), qinv(Gp))
            i0 = self.index[tuple([0] * d)]
            O0 = Om[..., i0, :]
            v = qlog(qmul(Om, qinv(O0)[..., None, :]))
            A = v.mean(-2)
            out.append(qmul(qexp(A), O0))
        return torch.stack(out, d)


class Chain:
    def __init__(self, Ntop, L, d, k):
        self.L, self.d, self.k, self.Ntop = L, d, k, Ntop
        self.levels = [Block(Ntop * L ** (k - i), L, d) for i in range(k)]
        self.n = Ntop * L**k

    def fields(self, U):
        out = [U]
        for b in self.levels:
            out.append(b(out[-1]))
        return out

    def top(self, U):
        return self.fields(U)[-1]


class Problem:
    def __init__(self, chain, Vtop):
        self.chain = chain
        self.V = Vtop
        d, n = chain.d, chain.n
        self.shape = (n,) * d + (d, 3)
        self.cshape = (chain.Ntop,) * d + (d, 3)
        self.nv = int(np.prod(self.shape))
        self.nc = int(np.prod(self.cshape))
        self.tau = 1.0 / n**2
        d_ = d
        k = [torch.fft.fftfreq(n, 1.0 / n) * 2 * np.pi / n for _ in range(d_)]
        g = torch.meshgrid(*k, indexing="ij")
        self.lap = sum(4 * torch.sin(x / 2) ** 2 for x in g) + self.tau
        self._g0 = None

    def kinv(self, x):
        X = torch.fft.fftn(x, dim=list(range(self.chain.d)))
        return torch.fft.ifftn(X / self.lap[..., None, None], dim=list(range(self.chain.d))).real

    def resid(self, U):
        return qlog(qmul(self.chain.top(U), qinv(self.V)))

    def s(self, H, U0):
        return wilson(qmul(qexp(H), U0))

    def grad_s(self, U0):
        H = torch.zeros(self.shape, requires_grad=True)
        val = self.s(H, U0)
        g, = torch.autograd.grad(val, H)
        return g, float(val)

    def lag_grad(self, H, U0, lam):
        H = H.detach().requires_grad_(True)
        Up = qmul(qexp(H), U0)
        val = wilson(Up) + (lam * self.resid(Up)).sum()
        g, = torch.autograd.grad(val, H)
        return g

    def jt(self, U0, lam):
        H = torch.zeros(self.shape, requires_grad=True)
        val = (lam * self.resid(qmul(qexp(H), U0))).sum()
        g, = torch.autograd.grad(val, H)
        return g

    def j(self, U0, v):
        # forward difference free: double-vjp trick
        H = torch.zeros(self.shape, requires_grad=True)
        r = self.resid(qmul(qexp(H), U0))
        y = torch.zeros_like(r, requires_grad=True)
        g, = torch.autograd.grad(r, H, grad_outputs=y, create_graph=True)
        out, = torch.autograd.grad(g, y, grad_outputs=v)
        return out

    def build_g0(self, U0=None):
        """Dense Schur complement at the flat field (colour diagonal, parent translation invariant)."""
        U1 = ident(self.shape[:-1])
        d = self.chain.d
        Nt = self.chain.Ntop
        cols = {}
        for mu in range(d):
            lam = torch.zeros(self.cshape)
            lam[(0,) * d + (mu, 0)] = 1.0
            w = self.j(U1, self.kinv(self.jt(U1, lam)))
            cols[mu] = w[..., 0]  # (Nt^d, d)
        Gh = torch.zeros((Nt,) * d + (d, d), dtype=torch.complex128)
        for mu in range(d):
            Gh[..., mu] = torch.fft.fftn(cols[mu], dim=list(range(d)))
        self._gh_inv = torch.linalg.inv(Gh)

    def g0inv(self, r):
        d = self.chain.d
        R = torch.fft.fftn(r, dim=list(range(d)))
        out = torch.einsum("...ab,...bc->...ac", self._gh_inv, R)
        return torch.fft.ifftn(out, dim=list(range(d))).real

    def kkt_solve(self, U0, lam, rhs_v, rhs_c, tol, maxiter):
        nv, nc = self.nv, self.nc
        g0 = self.lag_grad(torch.zeros(self.shape), U0, lam)

        def hv(v):
            nrm = float(v.abs().max())
            if nrm == 0:
                return torch.zeros_like(v)
            eps = 1e-4 / nrm
            gp = self.lag_grad(eps * v, U0, lam)
            gm = self.lag_grad(-eps * v, U0, lam)
            return (gp - gm) / (2 * eps)

        def matvec(z):
            guard()
            z = torch.from_numpy(np.asarray(z).copy())
            v, y = z[:nv].reshape(self.shape), z[nv:].reshape(self.cshape)
            a = hv(v) + self.jt(U0, y)
            b = self.j(U0, v)
            return torch.cat([a.reshape(-1), b.reshape(-1)]).numpy()

        def prec(z):
            z = torch.from_numpy(np.asarray(z).copy())
            v, y = z[:nv].reshape(self.shape), z[nv:].reshape(self.cshape)
            return torch.cat([self.kinv(v).reshape(-1), self.g0inv(y).reshape(-1)]).numpy()

        A = sla.LinearOperator((nv + nc, nv + nc), matvec=matvec)
        M = sla.LinearOperator((nv + nc, nv + nc), matvec=prec)
        b = torch.cat([rhs_v.reshape(-1), rhs_c.reshape(-1)]).numpy()
        sol, info = sla.minres(A, b, M=M, rtol=tol, maxiter=maxiter)
        sol = torch.from_numpy(sol)
        return sol[:nv].reshape(self.shape), sol[nv:].reshape(self.cshape)

    def solve(self, U, lam=None, newton=25, gtol=1e-9, ctol=1e-10, verbose=False):
        if not hasattr(self, "_gh_inv"):
            self.build_g0()
        if lam is None:
            lam = torch.zeros(self.cshape)
        for it in range(newton):
            g = self.lag_grad(torch.zeros(self.shape), U, lam)
            r = self.resid(U)
            gn, rn = float(g.abs().max()), float(r.abs().max())
            if verbose:
                print(f"   newton {it} |g|={gn:.3e} |r|={rn:.3e} S={float(wilson(U)):.10f}", flush=True)
            if gn < gtol and rn < ctol:
                break
            dv, dl = self.kkt_solve(U, lam, -g, -r, 1e-4, 200)
            step = 1.0
            mx = float(dv.abs().max())
            if mx > 0.3:
                step = 0.3 / mx
            U = qmul(qexp(step * dv), U)
            U = U / torch.sqrt((U * U).sum(-1, keepdim=True))
            lam = lam + step * dl
        g = self.lag_grad(torch.zeros(self.shape), U, lam)
        r = self.resid(U)
        return U, lam, float(g.abs().max()), float(r.abs().max())

    def initial(self):
        """Flat-field lift of the log of V."""
        if not hasattr(self, "_gh_inv"):
            self.build_g0()
        U1 = ident(self.shape[:-1])
        a = qlog(self.V)
        return qmul(qexp(self.kinv(self.jt(U1, self.g0inv(a)))), U1)


def constant_links(dirs, a):
    """N' = 1: links exp(a n_mu)."""
    d = len(dirs)
    t = torch.tensor(dirs, dtype=torch.float64) * a
    V = qexp(t)
    return V.reshape((1,) * d + (d, 4))


def random_gauge(shape, d, seed=0):
    g = torch.Generator().manual_seed(seed)
    t = torch.randn(tuple(shape) + (3,), generator=g)
    return qexp(t)


def gauge_transform(U, g):
    d = U.shape[-2]
    out = []
    for mu in range(d):
        out.append(qmul(qmul(g, U[..., mu, :]), qinv(torch.roll(g, -1, dims=mu))))
    return torch.stack(out, d)
