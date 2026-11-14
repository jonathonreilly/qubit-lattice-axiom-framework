#!/usr/bin/env python3
"""Search for a slice on a dense family: all closed currents in a box, with one gauge function per current per site, one flavour (colour-isotropic) or nine (colour mixing).

System (Text 3.13). For a basis J_i of the cycles of a box on a torus, E_i := G J_i in Feynman gauge, X_i^I functions on the sites of the box, I = 0 the trace flavour, I = 1..8 the traceless colour parts
with metric eta_I = +1 (antisymmetric, 3) and -1 (symmetric traceless, 5), after rescaling:
    R_ijk = V0(i, j, k) + W_jk(X_i^0) + W_ki(X_j^0) + W_ij(X_k^0) + sum_I eta_I [ Theta_i(X_j^I, X_k^I) + Theta_j(X_k^I, X_i^I) + Theta_k(X_i^I, X_j^I) ],
    V0 := VV(E_i, E_j, E_k), W_ij(th) := - <J_i, thbar E_j> + <J_j, thbar E_i>, Theta_J(th, th') := <J, thbar d th'>.
K_total - K_comp[C] is 24 R_ijk on triples (colour-isotropic), and the same in the colour form by (3.4).

PRE-REGISTERED CRITERIA (written before the first run).
 D0 FORMULA: R_ijk against the direct VV of E + d X, with X extended by zero, on a small family, relative 1e-10. FAIL stops everything.
 D1 CONTROL: colour flavours on the unit hypercube, under-determined (2295 unknowns, 680 equations): the solver must reach relative residual < 1e-9. If not, the solver is too weak and nothing below counts.
 D2 REPORT: one flavour on boxes 2^4, 2 2 3 3, 2 3 3 3. Report the smallest relative residual of the starts. Numerical evidence only.
 D4 (added after D3, before its run): nine flavours on 3 3 3 3, over-determined by 4.2. Report only: if the residual is above the 2.7e-2 of 2 3 3 3, the trend is against an exact solution; if it is below 1e-3, the trend is toward one, and the gap may be a real counterexample at this order.
 D3 DECISION on colour mixing: nine flavours on 2 3 3 3, over-determined by 2.26. Residual < 1e-9 from two starts: a colour-mixing slice exists on that box; record it, and the gap is possibly a real counterexample at this order.
    Residual > 1e-3 from all starts with agreement within a factor 2: evidence (only) of no such slice. Anything else: UNRESOLVED.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import resource
import sys
import time

import numpy as np
from scipy.sparse.linalg import LinearOperator, lsmr


def check_rss(limit_gb=2.0):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3
    if r > limit_gb:
        raise MemoryError(f"rss {r:.2f} GB")
    return r


class Setup:
    def __init__(self, T, sides):
        self.T = T
        self.sides = sides
        self.d = 4
        self.shape = (T,) * 4
        self.sites = list(itertools.product(*[range(s) for s in sides]))
        self.sidx = {x: i for i, x in enumerate(self.sites)}
        self.Lam = len(self.sites)
        # all plaquettes in the box, greedy basis of their currents
        links = []
        for x in self.sites:
            for mu in range(4):
                y = list(x)
                y[mu] += 1
                if tuple(y) in self.sidx:
                    links.append((x, mu))
        self.links = links
        self.lidx = {l: i for i, l in enumerate(links)}
        plaqs = []
        for x in self.sites:
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    xm = list(x)
                    xm[mu] += 1
                    xn = list(x)
                    xn[nu] += 1
                    xmn = list(xm)
                    xmn[nu] += 1
                    if tuple(xmn) in self.sidx:
                        plaqs.append((x, mu, nu, tuple(xm), tuple(xn)))
        rows = []
        Q = []
        basis = []
        for p in plaqs:
            v = np.zeros(len(links))
            x, mu, nu, xm, xn = p
            v[self.lidx[(x, mu)]] += 1
            v[self.lidx[(xm, nu)]] += 1
            v[self.lidx[(xn, mu)]] -= 1
            v[self.lidx[(x, nu)]] -= 1
            w = v.copy()
            for q in Q:
                w = w - (q @ w) * q
            n = np.linalg.norm(w)
            if n > 1e-9:
                Q.append(w / n)
                basis.append(p)
                rows.append(v)
        self.basis = basis
        self.n = len(basis)
        self.Jbox = np.array(rows)  # n x links
        expected = len(links) - self.Lam + 1
        if self.n != expected:
            raise RuntimeError(f"basis size {self.n} vs {expected}")

    def fields(self):
        T = self.T
        n = self.n
        E = np.zeros((n, 4) + self.shape)
        J = np.zeros((n, 4) + self.shape)
        for i in range(n):
            for l, val in zip(self.links, self.Jbox[i]):
                if val != 0:
                    x, mu = l
                    J[(i, mu) + x] = val
        idx = np.indices(self.shape)
        khat2 = sum(4 * np.sin(np.pi * idx[m] / T) ** 2 for m in range(4))
        khat2[0, 0, 0, 0] = 1.0
        inv = 1.0 / khat2
        inv[0, 0, 0, 0] = 0.0
        for i in range(n):
            E[i] = np.fft.ifftn(np.fft.fftn(J[i], axes=(1, 2, 3, 4)) * inv, axes=(1, 2, 3, 4)).real
        self.E = E
        self.J = J
        return E

    def plaq_values(self):
        """Arrays F, M, N of shape (P, n) with curl, mean mu, mean nu of each E_i on each plaquette of the torus."""
        E = self.E
        n = self.n
        Fs, Ms, Ns = [], [], []
        for mu in range(4):
            for nu in range(mu + 1, 4):
                Emu = E[:, mu]
                Enu = E[:, nu]
                Enu_up = np.roll(Enu, -1, axis=mu + 1)
                Emu_up = np.roll(Emu, -1, axis=nu + 1)
                Fs.append((Emu + Enu_up - Emu_up - Enu).reshape(n, -1).T)
                Ms.append((0.5 * (Emu + Emu_up)).reshape(n, -1).T)
                Ns.append((0.5 * (Enu + Enu_up)).reshape(n, -1).T)
        return np.concatenate(Fs), np.concatenate(Ms), np.concatenate(Ns)

    def V0(self):
        F, M, N = self.plaq_values()
        n = self.n
        U = np.zeros((n, n, n))
        for i in range(n):
            U[i] = (M * F[:, i, None]).T @ N
        V = U + U.transpose(1, 2, 0) + U.transpose(2, 0, 1) - U.transpose(0, 2, 1) - U.transpose(2, 1, 0) - U.transpose(1, 0, 2)
        return V

    def psi_theta(self):
        """psi[i, j, x] with W_ij(th) = sum_x psi[i, j, x] th_x, and for each current the list of (x, y, J) of its links."""
        n, Lam = self.n, self.Lam
        psi = np.zeros((n, n, Lam))
        loops = []
        Evals = np.zeros((n, len(self.links)))
        for b, (x, mu) in enumerate(self.links):
            Evals[:, b] = self.E[(slice(None), mu) + x]
        ends = []
        for (x, mu) in self.links:
            y = list(x)
            y[mu] += 1
            ends.append((self.sidx[x], self.sidx[tuple(y)]))
        ends = np.array(ends)
        for i in range(n):
            nz = np.nonzero(self.Jbox[i])[0]
            loops.append((ends[nz, 0], ends[nz, 1], self.Jbox[i, nz]))
        for b in range(len(self.links)):
            xa, xb = ends[b]
            # thbar on link b = (th_a + th_b) / 2
            term = np.outer(self.Jbox[:, b], Evals[:, b])  # J_i(b) E_j(b)
            contrib = -0.5 * (term - term.T)
            psi[:, :, xa] += contrib
            psi[:, :, xb] += contrib
        return psi, loops, ends, Evals


class System:
    def __init__(self, setup, flavours):
        self.s = setup
        self.n = setup.n
        self.Lam = setup.Lam
        self.flavours = flavours
        self.eta = np.array([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0])[: flavours]
        self.V0 = setup.V0()
        self.psi, self.loops, self.ends, self.Evals = setup.psi_theta()
        self.iu = np.array([(i, j, k) for i in range(self.n) for j in range(i + 1, self.n) for k in range(j + 1, self.n)])
        self.m = len(self.iu)
        self.Nz = flavours * self.n * (self.Lam - 1)

    def unpack(self, z):
        X = np.zeros((self.flavours, self.n, self.Lam))
        X[:, :, 1:] = z.reshape(self.flavours, self.n, self.Lam - 1)
        return X

    def Q(self, X, Y):
        """Q[i, j, k] = sum_I eta_I Theta_i(X_j^I, Y_k^I)."""
        n = self.n
        out = np.zeros((n, n, n))
        for i, (xa, xb, val) in enumerate(self.loops):
            tot = np.zeros((n, n))
            for I in range(self.flavours):
                A = X[I][:, xa] * val  # n x links
                tot += self.eta[I] * 0.5 * (A @ Y[I][:, xb].T - X[I][:, xb] @ (Y[I][:, xa] * val).T)
            out[i] = tot
        return out

    def residual_tensor(self, X):
        Q = self.Q(X, X)
        R = self.V0.copy()
        X0 = X[0]
        L = np.einsum("jkx,ix->ijk", self.psi, X0)
        R += L + L.transpose(1, 2, 0) + L.transpose(2, 0, 1)
        R += Q + Q.transpose(1, 2, 0) + Q.transpose(2, 0, 1)
        return R

    def residual(self, z):
        R = self.residual_tensor(self.unpack(z))
        return R[self.iu[:, 0], self.iu[:, 1], self.iu[:, 2]]

    def jvec(self, z, v):
        X = self.unpack(z)
        V = self.unpack(v)
        Q = self.Q(V, X) + self.Q(X, V)
        L = np.einsum("jkx,ix->ijk", self.psi, V[0])
        D = L + L.transpose(1, 2, 0) + L.transpose(2, 0, 1) + Q + Q.transpose(1, 2, 0) + Q.transpose(2, 0, 1)
        return D[self.iu[:, 0], self.iu[:, 1], self.iu[:, 2]]

    def jtvec(self, z, r):
        X = self.unpack(z)
        n = self.n
        S = np.zeros((n, n, n))
        i, j, k = self.iu.T
        S[i, j, k] = r
        S[j, k, i] = r
        S[k, i, j] = r
        S[j, i, k] = -r
        S[i, k, j] = -r
        S[k, j, i] = -r
        G = np.zeros((self.flavours, n, self.Lam))
        G[0] += 0.5 * np.einsum("ijk,jkx->ix", S, self.psi)
        for i2, (xa, xb, val) in enumerate(self.loops):
            Si = S[i2]
            for I in range(self.flavours):
                # - eta S_i X Theta_i, Theta_i[x_a, x_b] = J / 2, antisymmetric
                SX = Si @ X[I]
                np.add.at(G[I], (slice(None), xb), (-self.eta[I] * 0.5 * SX[:, xa] * val))
                np.add.at(G[I], (slice(None), xa), (+self.eta[I] * 0.5 * SX[:, xb] * val))
        return G[:, :, 1:].ravel()


def gauss_newton(sysm, z0, maxit=40, inner=300, tol=1e-12, verbose=False):
    z = z0.copy()
    r = sysm.residual(z)
    nr0 = np.linalg.norm(sysm.residual(np.zeros_like(z)))
    lam = 1e-3
    best = np.linalg.norm(r)
    for it in range(maxit):
        Jop = LinearOperator((sysm.m, sysm.Nz), matvec=lambda v: sysm.jvec(z, v), rmatvec=lambda u: sysm.jtvec(z, u))
        scale = max(np.linalg.norm(sysm.jtvec(z, r)) / max(best, 1e-300), 1e-12)
        sol = lsmr(Jop, -r, damp=np.sqrt(lam) * scale, atol=1e-8, btol=1e-8, maxiter=inner)[0]
        for _ in range(12):
            znew = z + sol
            rnew = sysm.residual(znew)
            nnew = np.linalg.norm(rnew)
            if nnew < best:
                z, r, best = znew, rnew, nnew
                lam = max(lam * 0.3, 1e-12)
                break
            lam *= 5
            sol = lsmr(Jop, -r, damp=np.sqrt(lam) * scale, atol=1e-8, btol=1e-8, maxiter=inner)[0]
        else:
            break
        if verbose:
            print(f"      it {it}: rel residual {best/nr0:.3e} lam {lam:.1e} rss {check_rss():.2f}GB", flush=True)
        if best / nr0 < tol:
            break
    return z, best / nr0


def check_formula(setup, sysm, rng):
    # direct VV with X extended by zero, on a few triples, torus sum
    T = setup.T
    n = setup.n
    z = rng.normal(size=sysm.Nz) * 0.1
    X = sysm.unpack(z)
    R = sysm.residual_tensor(X)
    worst = 0.0
    for _ in range(6):
        i, j, k = rng.choice(n, 3, replace=False)
        fields = []
        for a in (i, j, k):
            th = np.zeros(setup.shape)
            for s, x in enumerate(setup.sites):
                th[x] = X[0, a, s]
            f = setup.E[a].copy()
            for mu in range(4):
                f[mu] = f[mu] + np.roll(th, -1, axis=mu) - th
            fields.append(f)
        tot = 0.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                vals = []
                for f in fields:
                    a_, b_ = f[mu], f[nu]
                    bu = np.roll(b_, -1, axis=mu)
                    au = np.roll(a_, -1, axis=nu)
                    vals.append((a_ + bu - au - b_, 0.5 * (a_ + au), 0.5 * (b_ + bu)))
                (p1, m1, n1), (p2, m2, n2), (p3, m3, n3) = vals
                tot += np.sum(p1 * (m2 * n3 - n2 * m3) - m1 * (p2 * n3 - n2 * p3) + n1 * (p2 * m3 - m2 * p3))
        worst = max(worst, abs(tot - R[i, j, k]) / max(abs(tot), 1e-300))
    return worst


def run(T, sides, flavours, starts, seed, label, maxit=40, inner=300, amp=1e-2):
    rng = np.random.default_rng(seed)
    t0 = time.time()
    s = Setup(T, sides)
    s.fields()
    sysm = System(s, flavours)
    print(f"{label}: T={T} box={sides} flavours={flavours} n={s.n} sites={s.Lam} unknowns={sysm.Nz} equations={sysm.m} |V0|={np.linalg.norm(sysm.residual(np.zeros(sysm.Nz))):.3e} setup={time.time()-t0:.0f}s rss={check_rss():.2f}GB", flush=True)
    if flavours == 1:  # the direct sum below knows only the trace flavour, so D0 means nothing with more flavours
        print(f"   D0 formula worst rel diff {check_formula(s, sysm, rng):.1e}", flush=True)
    out = []
    for st in range(starts):
        t1 = time.time()
        z0 = rng.normal(size=sysm.Nz) * amp
        z, rel = gauss_newton(sysm, z0, maxit=maxit, inner=inner)
        out.append(rel)
        print(f"   start {st}: relative residual {rel:.3e}, max |X| {np.abs(z).max():.2e}, time={time.time()-t1:.0f}s rss={check_rss():.2f}GB", flush=True)
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "small"
    if mode == "small":
        run(12, (2, 2, 2, 2), 1, 3, 1, "D2 one flavour, hypercube")
        run(12, (2, 2, 2, 2), 9, 2, 2, "D1 control, nine flavours, hypercube", maxit=30)
        run(12, (2, 2, 3, 3), 1, 3, 3, "D2 one flavour, 2 2 3 3")
    elif mode == "col1":
        run(12, (2, 2, 3, 3), 9, 2, 4, "colour, 2 2 3 3", maxit=25, inner=200)
    elif mode == "col3":
        run(12, (3, 3, 3, 3), 9, 1, 7, "D4 colour, 3 3 3 3, over-determined by 4.2", maxit=15, inner=120)
    elif mode == "col2":
        run(12, (2, 3, 3, 3), 1, 2, 5, "D2 one flavour, 2 3 3 3", maxit=25, inner=200)
        run(12, (2, 3, 3, 3), 9, 2, 6, "D3 colour, 2 3 3 3", maxit=20, inner=150)


if __name__ == "__main__":
    main()
