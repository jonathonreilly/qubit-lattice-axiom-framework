#!/usr/bin/env python3
"""Single-link charge hopping on the ring clause: a fine scan of the link expectation across the rapid change, on 4^3-10^3.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the clause
H = -g sum_p (U_p + U_p^dag) - t sum_l sigma^x_l + M sum_v Q_v^2 (V = 0, g = 1, M = 2), Q_v = div_v / 2 the vertex charge, as in
open PR 9263. There the link expectation <sigma^x> and the charge density rose fastest between t = 0.25 and 0.5, and <sigma^x>
moved with size only at t = 0.5. Here the ground energy is measured on a grid of step 0.05 in t (compiled sign-free projector of
open PR 9263, fixed populations, the guide's charge penalty interpolated from the tuned values there). From energies alone
(Hellmann-Feynman): <sigma^x>(t) = -(1/N_l) dE/dt by central differences, and its slope d<sigma^x>/dt = -(1/N_l) d^2E/dt^2 by
second differences of step 0.1. Supplied model, finite diagnostics, no physical reading: the size dependence of the largest
slope is reported, and neither a crossover nor a transition is claimed.

Checks: (1) exact 2^3 control (the single-link term on the six links at one vertex): projected energies at t = 0.3, 0.4, 0.5 and
their first and second differences against exact diagonalization; (2) the grid reproduces open PR 9263's link expectations at
t = 0.25, 0.5, 0.75 on 4^3 and 6^3 (same difference step); (3) the scan on 4^3 and 6^3 (t = 0.15-0.85), 8^3 (0.25-0.75) and 10^3 (0.30-0.60):
<sigma^x>(t), the slope (never negative for exact energies, E0 being concave in t), and the location and height of the largest slope per
size (reported). Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numba as nb
import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 14400

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0
DRY = "--dry" in sys.argv


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


class Ice:
    def __init__(self, L):
        self.L = L
        self.nv, self.nl = L ** 3, 3 * L ** 3
        self.verts = list(itertools.product(range(L), repeat=3))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        self.axis = np.zeros(self.nl, dtype=int)
        self.coord = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
        self.xc = np.array([self.verts[l // 3][0] for l in range(self.nl)])      # x-coordinate of the link's tail vertex
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        plaq = []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % L
                vb[b] = (vb[b] + 1) % L
                plaq.append([3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b])
        self.plaq = np.array(plaq)
        self.sign = np.tile([1, 1, -1, -1], (len(plaq), 1))
        self.np_ = len(plaq)
        pol = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                pol[l].append(p)
        self.pol = pol
        width = max(len({q for l in links for q in pol[l]}) for links in self.plaq)
        self.A = np.full((self.np_, width), self.np_, dtype=int)
        self.M = np.zeros((self.np_, width, 4))
        for p, links in enumerate(self.plaq):
            aff = sorted({q for l in links for q in pol[l]})
            self.A[p, :len(aff)] = aff
            for j, q in enumerate(aff):
                for k, l in enumerate(links):
                    for h in np.flatnonzero(self.plaq[q] == l):
                        self.M[p, j, k] += self.sign[q, h]

    def circ(self, sigma):
        c = np.zeros(self.np_ + 1)
        c[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        return c

    def deltas(self, sigma, C, P):
        Ca = C[self.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", self.M[P], sigma[self.plaq[P]])
        return Cn, (np.abs(Cn) == 4).sum(axis=1) - (np.abs(Ca) == 4).sum(axis=1)

    def winding_fast(self, sigma):
        return tuple(int(sigma[(self.axis == a) & (self.coord == 0)].sum()) for a in range(3))

    def sector_state(self, quanta=0):
        sigma = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            i = self.vid[v]
            sigma[3 * i] = (-1) ** v[1]
            sigma[3 * i + 1] = (-1) ** v[0]
            sigma[3 * i + 2] = (-1) ** v[0]
        for q in range(quanta):
            for x in range(self.L):
                sigma[3 * self.vid[(x, 1, q)]] *= -1
        return sigma

    def modes(self, ms):
        """Transverse field modes O_b(k e_a) = N^{-1/2} sum over b-links of e^{i k x_a} sigma, b != a, k = 2 pi m / L:
        for each m the six (axis, polarisation) modes."""
        PH = np.zeros((len(ms), 6, self.nl), dtype=complex)
        tail_coord = np.array([self.verts[l // 3] for l in range(self.nl)])       # (nl, 3)
        for j, m in enumerate(ms):
            q = 0
            for a in range(3):
                e = np.exp(1j * 2 * np.pi * m / self.L * tail_coord[:, a]) / np.sqrt(self.nv)
                for b in range(3):
                    if b != a:
                        PH[j, q] = e * (self.axis == b)
                        q += 1
        return PH


def loop_vmc(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    sigma = np.ones(ice.nl, dtype=int) if start is None else start.copy()
    C = ice.circ(sigma)
    W0 = ice.winding_fast(sigma)
    samples = []
    per_sweep = max(1, ice.nl // 20)
    for sw in range(therm + sweeps):
        for _ in range(per_sweep):
            v = r.integers(ice.nv)
            seen, path_l = {v: 0}, []
            while True:
                outs = [l for (l, s) in ice.inc[v] if sigma[l] * s == 1]
                l = outs[r.integers(3)]
                v = ice.head[l] if ice.tail[l] == v else ice.tail[l]
                path_l.append(l)
                if v in seen:
                    cyc = path_l[seen[v]:]
                    break
                seen[v] = len(path_l)
            aff = sorted({p for l in cyc for p in ice.pol[l]})
            before = int((np.abs(C[aff]) == 4).sum())
            sigma[cyc] *= -1
            C_new = (sigma[ice.plaq[aff]] * ice.sign[aff]).sum(axis=1)
            after = int((np.abs(C_new) == 4).sum())
            keep = r.random() < np.exp(2 * alpha * (after - before))
            if keep and fix_winding and ice.winding_fast(sigma) != W0:
                keep = False
            if keep:
                C[aff] = C_new
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            samples.append(sigma.copy())
    return samples


OFF = 16
BS = 64


@nb.njit(cache=False)
def nb_seed(s):
    np.random.seed(s)


@nb.njit(cache=False)
def _dN(s, sig, plaq, A, M, dynf, C):
    d = 0
    for j in range(A.shape[1]):
        q = A[s, j]
        if q < 0:
            break
        if not dynf[q]:
            continue
        cn = np.int64(C[q])
        for k in range(4):
            cn -= 2 * M[s, j, k] * sig[plaq[s, k]]
        d += (1 if (cn == 4 or cn == -4) else 0) - (1 if (C[q] == 4 or C[q] == -4) else 0)
    return d


@nb.njit(cache=False)
def nb_init(sig, C, flp, dN, nflp, plaq, sign, A, M, dynf):
    """Circulations, flippable flags (unrecorded plaquettes only), flip-count changes and flippable counts of every walker."""
    n_w, Np = C.shape
    for i in range(n_w):
        cnt = 0
        for q in range(Np):
            c = 0
            for k in range(4):
                c += sig[i, plaq[q, k]] * sign[q, k]
            C[i, q] = c
            f = dynf[q] and (c == 4 or c == -4)
            flp[i, q] = f
            cnt += 1 if f else 0
        nflp[i] = cnt
        for s in range(Np):
            dN[i, s] = _dN(s, sig[i], plaq, A, M, dynf, C[i]) if flp[i, s] else 0


@nb.njit(cache=False)
def nb_walk(sig, C, flp, dN, nflp, Om, plaq, A, M, dynf, exptab, V, dtau, PH, stamp, tick, sbuf, rbuf, logw, ELend):
    """Advance every walker by imaginary time dtau under the guided jump process; accumulate log weights -int E_L dt."""
    n_w, Np = C.shape
    nblk = (Np + 63) // 64
    W = A.shape[1]
    nm = Om.shape[1]
    bs = np.zeros(nblk)
    for i in range(n_w):
        s_ = sig[i]; C_ = C[i]; f_ = flp[i]; d_ = dN[i]
        for b in range(nblk):
            bs[b] = 0.0
        for s in range(Np):
            if f_[s]:
                bs[s // 64] += exptab[d_[s] + 16]
        t = 0.0
        lw = 0.0
        while True:
            lam = 0.0
            for b in range(nblk):
                lam += bs[b]
            EL = V * nflp[i] - lam
            h = -np.log(1.0 - np.random.random()) / lam if lam > 0 else 1e300
            if t + h >= dtau:
                lw -= EL * (dtau - t)
                ELend[i] = EL
                break
            lw -= EL * h
            t += h
            u = np.random.random() * lam
            acc = 0.0
            p = -1
            for b in range(nblk):
                if acc + bs[b] > u:
                    lo = b * 64
                    hi = min(lo + 64, Np)
                    for s in range(lo, hi):
                        if f_[s]:
                            acc += exptab[d_[s] + 16]
                            p = s
                            if acc > u:
                                break
                    break
                acc += bs[b]
            if p < 0:
                for s in range(Np - 1, -1, -1):
                    if f_[s]:
                        p = s
                        break
            tick[0] += 1
            tk = tick[0]
            nB = 0
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                for j2 in range(W):
                    s = A[q, j2]
                    if s < 0:
                        break
                    if stamp[s] != tk:
                        stamp[s] = tk
                        sbuf[nB] = s
                        rbuf[nB] = exptab[d_[s] + 16] if f_[s] else 0.0
                        nB += 1
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                cn = np.int64(C_[q])
                for k in range(4):
                    cn -= 2 * M[p, j, k] * s_[plaq[p, k]]
                oldf = f_[q]
                C_[q] = cn
                newf = dynf[q] and (cn == 4 or cn == -4)
                f_[q] = newf
                nflp[i] += (1 if newf else 0) - (1 if oldf else 0)
            for k in range(4):
                l = plaq[p, k]
                sv = s_[l]
                for m in range(nm):
                    Om[i, m] += PH[l, m] * (-2.0 * sv)
                s_[l] = -sv
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    d_[s] = _dN(s, s_, plaq, A, M, dynf, C_)
                    rn = exptab[d_[s] + 16]
                else:
                    rn = 0.0
                bs[s // 64] += rn - rbuf[jj]
        logw[i] = lw


class Projector:
    """Fixed-population projector over a region (torus when nothing is recorded), with lineage histories of observables,
    log mean weights for the population-control correction, and ancestor tracking."""
    def __init__(self, ice, dyn, alpha, V, PH, seed):
        self.ice = ice
        self.plaq = ice.plaq.astype(np.int64)
        self.sign = ice.sign.astype(np.int64)
        A = ice.A.astype(np.int64).copy()
        A[A == ice.np_] = -1
        self.A = A
        self.M = np.rint(ice.M).astype(np.int64)
        self.dyn = dyn.astype(np.bool_)
        self.ndyn = int(dyn.sum())
        self.alpha, self.V = alpha, V
        self.exptab = np.exp(alpha * (np.arange(33) - 16.0))
        self.PH = np.ascontiguousarray(PH.T.astype(np.complex128))       # (nl, n_modes)
        self.stamp = np.zeros(ice.np_, dtype=np.int64)
        self.tick = np.zeros(1, dtype=np.int64)
        self.sbuf = np.zeros(4096, dtype=np.int64)
        self.rbuf = np.zeros(4096)
        nb_seed(seed)

    def run(self, init, n_w, n_gen, dtau, therm, lags, rng, obs_extra=None, n_extra=0):
        ice = self.ice
        picks0 = rng.integers(len(init), size=n_w)
        sig = np.array([init[k] for k in picks0], dtype=np.int8)
        C = np.zeros((n_w, ice.np_), dtype=np.int8)
        flp = np.zeros((n_w, ice.np_), dtype=np.bool_)
        dN = np.zeros((n_w, ice.np_), dtype=np.int8)
        nflp = np.zeros(n_w, dtype=np.int64)
        nb_init(sig, C, flp, dN, nflp, self.plaq, self.sign, self.A, self.M, self.dyn)
        Om = sig.astype(np.float64) @ self.PH
        nm = Om.shape[1]
        nobs = nm + 1 + n_extra
        Lmax = max(lags)
        hist = np.zeros((n_w, Lmax + 1, nobs))
        anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
        logw = np.zeros(n_w)
        ELend = np.zeros(n_w)
        out_e, out_lwbar, out_fw, out_mix, out_nd = [], [], [], [], []
        for g in range(n_gen):
            nb_walk(sig, C, flp, dN, nflp, Om, self.plaq, self.A, self.M, self.dyn, self.exptab, self.V, dtau, self.PH,
                    self.stamp, self.tick, self.sbuf, self.rbuf, logw, ELend)
            mx = logw.max()
            w = np.exp(logw - mx)
            Wt = w.sum()
            out_lwbar.append(mx + np.log(Wt / n_w))
            wn = w / Wt
            out_e.append(float(wn @ ELend))
            o = np.empty((n_w, nobs))
            o[:, :nm] = np.abs(Om) ** 2
            o[:, nm] = nflp / self.ndyn
            if n_extra:
                o[:, nm + 1:] = obs_extra(sig)
            slot = g % (Lmax + 1)
            hist[:, slot] = o
            anc[:, slot] = np.arange(n_w)
            if g >= therm:
                out_mix.append(wn @ o)
                out_fw.append(np.array([wn @ hist[:, (g - L) % (Lmax + 1)] for L in lags]))
                out_nd.append([len(np.unique(anc[:, (g - L) % (Lmax + 1)])) / n_w for L in lags])
            cum = np.cumsum(wn)
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
            sig, C, flp, dN, nflp, Om, hist, anc = sig[picks], C[picks], flp[picks], dN[picks], nflp[picks], Om[picks], hist[picks], anc[picks]
        return dict(e=np.array(out_e), lwbar=np.array(out_lwbar), fw=np.array(out_fw), mix=np.array(out_mix), nd=np.array(out_nd), therm=therm)


def corrected(res, Lc, which="fw", ncomp=None):
    """Population-control-corrected averages: weight generation n by prod_{j=n-Lc+1..n} wbar_j (Lc = 0: plain average).
    Returns the weighted mean over the post-thermalization generations of res[which] (energy: 'e')."""
    th = res["therm"]
    lw = res["lwbar"]
    n = len(lw)
    cs = np.concatenate([[0.0], np.cumsum(lw)])
    idx = np.arange(th, n)
    logG = cs[idx + 1] - cs[np.maximum(idx + 1 - Lc, 0)] if Lc > 0 else np.zeros(len(idx))
    G = np.exp(logG - logG.max())
    x = res[which] if which != "e" else res["e"][th:]
    x = np.asarray(x)
    if x.ndim == 1:
        return float((G @ x) / G.sum())
    return np.tensordot(G, x, axes=(0, 0)) / G.sum()


@nb.njit(cache=False)
def nb_init_rates(sig, flp, dN, rate, Fh, plaq, exptab, hl, bl):
    n_w, Np = flp.shape
    for i in range(n_w):
        f = 0.0
        for l in range(sig.shape[1]):
            f += hl[l] * sig[i, l]
        Fh[i] = f
        for s in range(Np):
            if flp[i, s]:
                g = 0.0
                for k in range(4):
                    g += bl[plaq[s, k]] * sig[i, plaq[s, k]]
                rate[i, s] = exptab[dN[i, s] + 16] * np.exp(-2.0 * g)
            else:
                rate[i, s] = 0.0


@nb.njit(cache=False)
def nb_walk_f(sig, C, flp, dN, rate, nflp, Fh, Om, plaq, A, M, dynf, exptab, V, hl, bl, dtau, PH, stamp, tick, sbuf, rbuf, logw, ELend):
    """As nb_walk, with the diagonal energy V N_flip - sum_l hl[l] sigma_l and guide factor exp(sum_l bl[l] sigma_l)."""
    n_w, Np = C.shape
    nblk = (Np + 63) // 64
    W = A.shape[1]
    nm = Om.shape[1]
    bs = np.zeros(nblk)
    for i in range(n_w):
        s_ = sig[i]; C_ = C[i]; f_ = flp[i]; d_ = dN[i]; r_ = rate[i]
        for b in range(nblk):
            bs[b] = 0.0
        for s in range(Np):
            bs[s // 64] += r_[s]
        t = 0.0
        lw = 0.0
        while True:
            lam = 0.0
            for b in range(nblk):
                lam += bs[b]
            EL = V * nflp[i] - Fh[i] - lam
            h = -np.log(1.0 - np.random.random()) / lam if lam > 0 else 1e300
            if t + h >= dtau:
                lw -= EL * (dtau - t)
                ELend[i] = EL
                break
            lw -= EL * h
            t += h
            u = np.random.random() * lam
            acc = 0.0
            p = -1
            for b in range(nblk):
                if acc + bs[b] > u:
                    lo = b * 64
                    hi = min(lo + 64, Np)
                    for s in range(lo, hi):
                        if r_[s] > 0.0:
                            acc += r_[s]
                            p = s
                            if acc > u:
                                break
                    break
                acc += bs[b]
            if p < 0:
                for s in range(Np - 1, -1, -1):
                    if f_[s]:
                        p = s
                        break
            tick[0] += 1
            tk = tick[0]
            nB = 0
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                for j2 in range(W):
                    s = A[q, j2]
                    if s < 0:
                        break
                    if stamp[s] != tk:
                        stamp[s] = tk
                        sbuf[nB] = s
                        rbuf[nB] = r_[s]
                        nB += 1
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                cn = np.int64(C_[q])
                for k in range(4):
                    cn -= 2 * M[p, j, k] * s_[plaq[p, k]]
                oldf = f_[q]
                C_[q] = cn
                newf = dynf[q] and (cn == 4 or cn == -4)
                f_[q] = newf
                nflp[i] += (1 if newf else 0) - (1 if oldf else 0)
            for k in range(4):
                l = plaq[p, k]
                sv = s_[l]
                for m in range(nm):
                    Om[i, m] += PH[l, m] * (-2.0 * sv)
                Fh[i] += hl[l] * (-2.0 * sv)
                s_[l] = -sv
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    d_[s] = _dN(s, s_, plaq, A, M, dynf, C_)
                    g = 0.0
                    for k in range(4):
                        g += bl[plaq[s, k]] * s_[plaq[s, k]]
                    rn = exptab[d_[s] + 16] * np.exp(-2.0 * g)
                else:
                    rn = 0.0
                r_[s] = rn
                bs[s // 64] += rn - rbuf[jj]
        logw[i] = lw


def energy_run(pr, init, n_w, n_gen, dtau, therm, rng, hl, bl, Lcs=(0, 20, 40, 80)):
    """Fixed-population projection of H - sum hl sigma with guide exp(alpha N_flip + sum bl sigma): returns the per-generation
    mixed energies, log mean weights, and population-corrected energy estimates for the windows Lcs, with 10-bin errors."""
    ice = pr.ice
    picks0 = rng.integers(len(init), size=n_w)
    sig = np.array([init[k] for k in picks0], dtype=np.int8)
    C = np.zeros((n_w, ice.np_), dtype=np.int8)
    flp = np.zeros((n_w, ice.np_), dtype=np.bool_)
    dN = np.zeros((n_w, ice.np_), dtype=np.int8)
    nflp = np.zeros(n_w, dtype=np.int64)
    nb_init(sig, C, flp, dN, nflp, pr.plaq, pr.sign, pr.A, pr.M, pr.dyn)
    rate = np.zeros((n_w, ice.np_))
    Fh = np.zeros(n_w)
    nb_init_rates(sig, flp, dN, rate, Fh, pr.plaq, pr.exptab, hl, bl)
    Om = np.zeros((n_w, 1), dtype=np.complex128)
    PHz = np.zeros((ice.nl, 1), dtype=np.complex128)
    logw = np.zeros(n_w); ELend = np.zeros(n_w)
    es, lws = [], []
    for g in range(n_gen):
        nb_walk_f(sig, C, flp, dN, rate, nflp, Fh, Om, pr.plaq, pr.A, pr.M, pr.dyn, pr.exptab, pr.V, hl, bl, dtau, PHz,
                  pr.stamp, pr.tick, pr.sbuf, pr.rbuf, logw, ELend)
        mx = logw.max(); w = np.exp(logw - mx); Wt = w.sum()
        lws.append(mx + np.log(Wt / n_w)); es.append(float((w @ ELend) / Wt))
        cum = np.cumsum(w / Wt)
        picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
        sig, C, flp, dN, rate, nflp, Fh = sig[picks], C[picks], flp[picks], dN[picks], rate[picks], nflp[picks], Fh[picks]
    res = dict(e=np.array(es), lwbar=np.array(lws), therm=therm)
    out = {}
    for Lc in Lcs:
        est = corrected(res, Lc, "e")
        # 10 contiguous bins of the post-thermalization generations, each corrected with the same window
        n = len(es) - therm
        chunks = np.array_split(np.arange(n), 10)
        cs = np.concatenate([[0.0], np.cumsum(res["lwbar"])])
        vals = []
        for c in chunks:
            idx = therm + c
            logG = cs[idx + 1] - cs[np.maximum(idx + 1 - Lc, 0)] if Lc > 0 else np.zeros(len(idx))
            G = np.exp(logG - logG.max())
            vals.append(float(G @ res["e"][idx] / G.sum()))
        out[Lc] = (est, float(np.std(vals, ddof=1) / np.sqrt(10)))
    return out, res


def triple(ice, k):
    """The cyclic triple of transverse modes: a-links modulated along axis (a + 1) mod 3, so the three modes cover each plaquette
    orientation once. Returns the field pattern sum over the triple of cos(k x_b) and the three mode vectors O = N^-1/2 sum e^{ikx_b} sigma."""
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    hv = np.cos(k * xb)
    PH = np.array([np.exp(1j * k * xb) * (ice.axis == a) / np.sqrt(ice.nv) for a in range(3)])
    return hv, PH


def chi_fit(E0, s0, E1, s1, E2, s2, h1, N, pref):
    """Mode-averaged chi from E(0), E(h1), E(2 h1), h^4 eliminated: E(h) = E0 - a h^2 - b h^4, a = 3 pref N chi / 4 (three modes)."""
    a = (15 * E0 - 16 * E1 + E2) / (12 * h1 ** 2)
    sa = np.sqrt(225 * s0 ** 2 + 256 * s1 ** 2 + s2 ** 2) / (12 * h1 ** 2)
    return 4 * a / (3 * pref * N), 4 * sa / (3 * pref * N)


def run_E(pr, init, nw, ngen, rng, hvec, h, beta=0.5):
    out, _ = energy_run(pr, init, nw, ngen, DTAU, ngen // 4, rng, h * hvec, beta * h * hvec, Lcs=(0,))
    return out[0]


# Compiled continuous-time projector for the ring clause with charge-creating single-link flips and a charge mass.
# H = -g sum_p (U_p + U_p^dag) + V N_flip - sum_l t_l sigma^x_l + M sum_v Q_v^2 - sum_l hl_l sigma_l,  Q_v = div_v / 2.
# Guide: log psi_G = alpha N_flip - gam sum_v Q_v^2 + sum_l bl_l sigma_l.  Sign-free: every off-diagonal element is <= 0.


class QTables:
    def __init__(self, ice):
        L = ice.L
        self.plaq = ice.plaq.astype(np.int64)
        self.sign = ice.sign.astype(np.int64)
        A = ice.A.astype(np.int64).copy()
        A[A == ice.np_] = -1
        self.A = A
        self.M = np.rint(ice.M).astype(np.int64)
        pol4 = np.zeros((ice.nl, 4), dtype=np.int64)
        pols = np.zeros((ice.nl, 4), dtype=np.int64)
        cnt = np.zeros(ice.nl, dtype=np.int64)
        for p in range(ice.np_):
            for k in range(4):
                l = ice.plaq[p, k]
                pol4[l, cnt[l]] = p
                pols[l, cnt[l]] = ice.sign[p, k]
                cnt[l] += 1
        assert np.all(cnt == 4)
        self.pol4, self.pols = pol4, pols
        inc6 = np.zeros((ice.nv, 6), dtype=np.int64)
        incs6 = np.zeros((ice.nv, 6), dtype=np.int64)
        for v in range(ice.nv):
            assert len(ice.inc[v]) == 6
            for j, (l, s) in enumerate(ice.inc[v]):
                inc6[v, j], incs6[v, j] = l, s
        self.inc6, self.incs6 = inc6, incs6
        self.tail = ice.tail.astype(np.int64)
        self.head = ice.head.astype(np.int64)


@nb.njit(cache=False)
def q_charges(sig, inc6, incs6, Q):
    for v in range(inc6.shape[0]):
        d = 0
        for j in range(6):
            d += incs6[v, j] * sig[inc6[v, j]]
        Q[v] = d // 2


@nb.njit(cache=False)
def q_rate_plaq(s, sig, C, flp, plaq, A, M, dynf, exptab, bl, gg):
    if not flp[s]:
        return 0.0
    d = _dN(s, sig, plaq, A, M, dynf, C)
    g = 0.0
    for k in range(4):
        g += bl[plaq[s, k]] * sig[plaq[s, k]]
    return gg * exptab[d + 16] * np.exp(-2.0 * g)


@nb.njit(cache=False)
def q_rate_link(l, sig, C, flp, Q, pol4, pols, dynf, tail, head, exptab, tl, gam, bl):
    if tl[l] <= 0.0:
        return 0.0
    s = sig[l]
    d = 0
    for j in range(4):
        q = pol4[l, j]
        cn = C[q] - 2 * pols[l, j] * s
        d += (1 if (dynf[q] and (cn == 4 or cn == -4)) else 0) - (1 if flp[q] else 0)
    dq2 = 2 + 2 * s * (Q[head[l]] - Q[tail[l]])
    return tl[l] * exptab[d + 16] * np.exp(-gam * dq2 - 2.0 * bl[l] * s)


@nb.njit(cache=False)
def q_init(sig, C, flp, Q, nflp, sq2, Fh, rate, plaq, sign, A, M, dynf, pol4, pols, inc6, incs6, tail, head, exptab, tl, gam, hl, bl, gg):
    n_w, Np = C.shape
    nl = sig.shape[1]
    for i in range(n_w):
        cnt = 0
        for q in range(Np):
            c = 0
            for k in range(4):
                c += sig[i, plaq[q, k]] * sign[q, k]
            C[i, q] = c
            f = dynf[q] and (c == 4 or c == -4)
            flp[i, q] = f
            cnt += 1 if f else 0
        nflp[i] = cnt
        q_charges(sig[i], inc6, incs6, Q[i])
        s2 = 0
        for v in range(Q.shape[1]):
            s2 += Q[i, v] * Q[i, v]
        sq2[i] = s2
        f = 0.0
        for l in range(nl):
            f += hl[l] * sig[i, l]
        Fh[i] = f
        for s in range(Np):
            rate[i, s] = q_rate_plaq(s, sig[i], C[i], flp[i], plaq, A, M, dynf, exptab, bl, gg)
        for l in range(nl):
            rate[i, Np + l] = q_rate_link(l, sig[i], C[i], flp[i], Q[i], pol4, pols, dynf, tail, head, exptab, tl, gam, bl)


@nb.njit(cache=False)
def q_walk(sig, C, flp, Q, nflp, sq2, Fh, rate, plaq, sign, A, M, dynf, pol4, pols, inc6, incs6, tail, head, exptab, tl, gam, hl, bl,
           gg, V, Mq, dtau, stamp, tick, cbuf, cstamp, logw, ELend):
    """One projection step of length dtau for every walker; logw gets -int EL, ELend the local energy at the end."""
    n_w, Np = C.shape
    nl = sig.shape[1]
    ne = Np + nl
    nblk = (ne + 63) // 64
    Wd = A.shape[1]
    bs = np.zeros(nblk)
    for i in range(n_w):
        s_ = sig[i]; C_ = C[i]; f_ = flp[i]; Q_ = Q[i]; r_ = rate[i]
        for b in range(nblk):
            bs[b] = 0.0
        for e in range(ne):
            bs[e // 64] += r_[e]
        t = 0.0
        lw = 0.0
        while True:
            lam = 0.0
            for b in range(nblk):
                lam += bs[b]
            EL = V * nflp[i] + Mq * sq2[i] - Fh[i] - lam
            h = -np.log(1.0 - np.random.random()) / lam if lam > 0 else 1e300
            if t + h >= dtau:
                lw -= EL * (dtau - t)
                ELend[i] = EL
                break
            lw -= EL * h
            t += h
            u = np.random.random() * lam
            acc = 0.0
            ev = -1
            for b in range(nblk):
                if acc + bs[b] > u:
                    lo = b * 64
                    hi = min(lo + 64, ne)
                    for e in range(lo, hi):
                        if r_[e] > 0.0:
                            acc += r_[e]
                            ev = e
                            if acc > u:
                                break
                    break
                acc += bs[b]
            if ev < 0:
                for e in range(ne - 1, -1, -1):
                    if r_[e] > 0.0:
                        ev = e
                        break
            # ---- apply the event: flip links, collect plaquettes whose circulation changes
            tick[0] += 1
            tk = tick[0]
            nC = 0
            if ev < Np:
                for k in range(4):
                    l = plaq[ev, k]
                    sv = s_[l]
                    Fh[i] += hl[l] * (-2.0 * sv)
                    s_[l] = -sv
                    for j in range(4):
                        q = pol4[l, j]
                        if cstamp[q] != tk:
                            cstamp[q] = tk
                            cbuf[nC] = q
                            nC += 1
            else:
                l = ev - Np
                sv = s_[l]
                Fh[i] += hl[l] * (-2.0 * sv)
                s_[l] = -sv
                a_, b_ = tail[l], head[l]
                qa, qb = Q_[a_], Q_[b_]
                Q_[a_] = qa - sv
                Q_[b_] = qb + sv
                sq2[i] += (qa - sv) * (qa - sv) - qa * qa + (qb + sv) * (qb + sv) - qb * qb
                for j in range(4):
                    q = pol4[l, j]
                    if cstamp[q] != tk:
                        cstamp[q] = tk
                        cbuf[nC] = q
                        nC += 1
            for jj in range(nC):
                q = cbuf[jj]
                c = 0
                for k in range(4):
                    c += s_[plaq[q, k]] * sign[q, k]
                oldf = f_[q]
                C_[q] = c
                newf = dynf[q] and (c == 4 or c == -4)
                f_[q] = newf
                nflp[i] += (1 if newf else 0) - (1 if oldf else 0)
            # ---- recompute the rates that can have changed
            for jj in range(nC):
                q = cbuf[jj]
                for j2 in range(Wd):
                    s = A[q, j2]
                    if s < 0:
                        break
                    if stamp[s] != tk:
                        stamp[s] = tk
                        rn = q_rate_plaq(s, s_, C_, f_, plaq, A, M, dynf, exptab, bl, gg)
                        bs[s // 64] += rn - r_[s]
                        r_[s] = rn
                for k in range(4):
                    m = plaq[q, k]
                    e = Np + m
                    if stamp[e] != tk:
                        stamp[e] = tk
                        rn = q_rate_link(m, s_, C_, f_, Q_, pol4, pols, dynf, tail, head, exptab, tl, gam, bl)
                        bs[e // 64] += rn - r_[e]
                        r_[e] = rn
            if ev >= Np:
                l = ev - Np
                for vv in range(2):
                    v = tail[l] if vv == 0 else head[l]
                    for j in range(6):
                        m = inc6[v, j]
                        e = Np + m
                        if stamp[e] != tk:
                            stamp[e] = tk
                            rn = q_rate_link(m, s_, C_, f_, Q_, pol4, pols, dynf, tail, head, exptab, tl, gam, bl)
                            bs[e // 64] += rn - r_[e]
                            r_[e] = rn
        logw[i] = lw


def q_energy_run(ice, T, init, n_w, n_gen, dtau, therm, rng, seed, alpha, gam, tl, Mq, V=0.0, gg=1.0, hl=None, bl=None, dynf=None):
    """Fixed-population projection; returns (energy estimate, 10-bin error) from the post-thermalization generations."""
    nb_seed(seed)
    hl = np.zeros(ice.nl) if hl is None else hl
    bl = np.zeros(ice.nl) if bl is None else bl
    dynf = np.ones(ice.np_, dtype=np.bool_) if dynf is None else dynf
    tl = np.asarray(tl, dtype=float)
    exptab = np.exp(alpha * (np.arange(33) - 16.0))
    picks0 = rng.integers(len(init), size=n_w)
    sig = np.array([init[k] for k in picks0], dtype=np.int64)
    C = np.zeros((n_w, ice.np_), dtype=np.int64)
    flp = np.zeros((n_w, ice.np_), dtype=np.bool_)
    Q = np.zeros((n_w, ice.nv), dtype=np.int64)
    nflp = np.zeros(n_w, dtype=np.int64)
    sq2 = np.zeros(n_w, dtype=np.int64)
    Fh = np.zeros(n_w)
    rate = np.zeros((n_w, ice.np_ + ice.nl))
    q_init(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head,
           exptab, tl, gam, hl, bl, gg)
    stamp = np.zeros(ice.np_ + ice.nl, dtype=np.int64)
    cstamp = np.zeros(ice.np_, dtype=np.int64)
    tick = np.zeros(1, dtype=np.int64)
    cbuf = np.zeros(64, dtype=np.int64)
    logw = np.zeros(n_w); ELend = np.zeros(n_w)
    es, qs = [], []
    for g in range(n_gen):
        q_walk(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head,
               exptab, tl, gam, hl, bl, gg, V, Mq, dtau, stamp, tick, cbuf, cstamp, logw, ELend)
        mx = logw.max(); w = np.exp(logw - mx); Wt = w.sum()
        es.append(float((w @ ELend) / Wt))
        qs.append(float((w @ sq2) / Wt))
        cum = np.cumsum(w / Wt)
        picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
        sig, C, flp, Q, nflp, sq2, Fh, rate = sig[picks], C[picks], flp[picks], Q[picks], nflp[picks], sq2[picks], Fh[picks], rate[picks]
    e = np.array(es[therm:])
    chunks = np.array_split(e, 10)
    vals = np.array([c.mean() for c in chunks])
    return float(e.mean()), float(vals.std(ddof=1) / np.sqrt(10)), float(np.mean(qs[therm:]))



# ------------------------------------------------------------------------------------------------ main
DTAU = 0.05
MQ = 2.0
GAM_T = (0.25, 0.5, 0.75, 1.0)
GAM_V = (1.2, 0.7, 0.5, 0.3)          # the guide's charge penalty tuned on 4^3 at M = 2 (open PR 9263); linear in between


def gam_of(t):
    """The guide's charge penalty: linear interpolation of the tuned values (held at the ends). The mixed energy estimator does not
    depend on it; the variance and the fixed-population bias do."""
    return float(np.interp(t, GAM_T, GAM_V))


# ---------------------------------------------------------------- 1. exact 2^3 control of the energy differences
ice2 = Ice(2); T2 = QTables(ice2)
seed2 = ice2.sector_state(0)
S2 = [l for (l, sg) in ice2.inc[0]]                 # the six links at one vertex carry the single-link term
masks2 = [sum(1 << int(l) for l in ice2.plaq[p]) for p in range(ice2.np_)]


def reach(ice, masks, seed, S):
    """Every configuration reachable from the seed by plaquette flips and flips of the links in S, with its flippable
    plaquettes, sum of squared charges and link values."""
    bits = np.arange(ice.nl)
    c0 = int(((seed + 1) // 2 * (1 << bits)).sum())
    idx = {c0: 0}; order = [c0]; q = 0
    out = []
    while q < len(order):
        c = order[q]; q += 1
        s = ((c >> bits) & 1) * 2 - 1
        fl = np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)
        Qv = np.zeros(ice.nv, dtype=int)
        for v in range(ice.nv):
            for (l, sg) in ice.inc[v]:
                Qv[v] += sg * s[l]
        out.append((fl, int(((Qv // 2) ** 2).sum()), s))
        for p in fl:
            c2 = c ^ masks[p]
            if c2 not in idx:
                idx[c2] = len(order); order.append(c2)
        for l in S:
            c2 = c ^ (1 << int(l))
            if c2 not in idx:
                idx[c2] = len(order); order.append(c2)
    return order, idx, out


order2, idx2, props2 = reach(ice2, masks2, seed2, S2)
n2 = len(order2)
Q22 = np.array([pp[1] for pp in props2], dtype=float)
rr_, cr_, rt_, ct_ = [], [], [], []
for a, (fl, q2, s) in enumerate(props2):
    c = order2[a]
    for p in fl:
        rr_.append(idx2[c ^ masks2[p]]); cr_.append(a)
    for l in S2:
        rt_.append(idx2[c ^ (1 << int(l))]); ct_.append(a)
Hring = coo_matrix((-np.ones(len(rr_)), (rr_, cr_)), shape=(n2, n2)).tocsr()
Hlink = coo_matrix((-np.ones(len(rt_)), (rt_, ct_)), shape=(n2, n2)).tocsr()
TS1 = (0.3, 0.4, 0.5)
ex1, pj1 = {}, {}
for j, t in enumerate(TS1):
    H = Hring + t * Hlink + diags(MQ * Q22)
    ex1[t] = float(eigsh(H, k=1, which="SA")[0][0])
    tl2 = np.zeros(ice2.nl); tl2[S2] = t
    pj1[t] = q_energy_run(ice2, T2, [seed2], 800 if DRY else 4000, 400 if DRY else 12000, DTAU, 100 if DRY else 1000,
                          np.random.default_rng(60 + j), 61 + j, ALPHA, gam_of(t), tl2, MQ)[:2]
rows1, ok1 = [], True
for t in TS1:
    z = (pj1[t][0] - ex1[t]) / pj1[t][1]
    ok1 &= abs(z) <= 3
    rows1.append(f"t {t}: exact {ex1[t]:.6f}, projector {pj1[t][0]:.5f}+-{pj1[t][1]:.5f} ({z:+.1f} sigma)")
d1x = -(ex1[0.5] - ex1[0.3]) / 0.2
d1p = -(pj1[0.5][0] - pj1[0.3][0]) / 0.2
d1e = np.hypot(pj1[0.5][1], pj1[0.3][1]) / 0.2
d2x = -(ex1[0.5] - 2 * ex1[0.4] + ex1[0.3]) / 0.01
d2p = -(pj1[0.5][0] - 2 * pj1[0.4][0] + pj1[0.3][0]) / 0.01
d2e = np.sqrt(pj1[0.5][1] ** 2 + 4 * pj1[0.4][1] ** 2 + pj1[0.3][1] ** 2) / 0.01
z1, z2 = (d1p - d1x) / d1e, (d2p - d2x) / d2e
ok1 &= abs(z1) <= 3 and abs(z2) <= 3
rows1.append(f"sum of <sigma^x> on the six links at t = 0.4, -dE/dt: exact {d1x:.4f}, projector {d1p:.4f}+-{d1e:.4f} ({z1:+.1f} sigma); "
             f"its slope -d2E/dt2: exact {d2x:.3f}, projector {d2p:.3f}+-{d2e:.3f} ({z2:+.1f} sigma)")
check(f"exact 2^3 control ({n2} states, the single-link term on the six links at one vertex, M = 2): projected energies at t = 0.3, 0.4, 0.5 "
      "and their first and second differences agree with exact diagonalization", ok1, "; ".join(rows1) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 2./3. the grid on the tori
def grid_energies(L, ts, seeds, nw, ngen):
    """E(t) on the grid: per seed one loop-move sample set of the ice sector, reused at every t; mean over seeds with the larger of
    the seed scatter and the mean bin error over sqrt(n)."""
    ice = Ice(L); T = QTables(ice)
    per = {t: [] for t in ts}
    t0 = time.time()
    for sd in seeds:
        rr = np.random.default_rng(sd * 100 + L)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        for j, t in enumerate(ts):
            per[t].append(q_energy_run(ice, T, init, nw, ngen, DTAU, ngen // 4, rr, sd * 1000 + L * 50 + j, ALPHA, gam_of(t),
                                       np.full(ice.nl, t), MQ)[:2])
    E = {}
    for t in ts:
        v = np.array([x[0] for x in per[t]]); b = np.array([x[1] for x in per[t]])
        n = len(v)
        E[t] = (float(v.mean()), float(max(v.std(ddof=1) / np.sqrt(n) if n > 1 else 0.0, b.mean() / np.sqrt(n))))
    cost = (time.time() - t0) / (len(seeds) * len(ts))
    return E, ice.nl, cost


def key(t):
    return round(t, 2)


def sx_at(E, nl, t, d):
    """<sigma^x>(t) = -(1/N_l) dE/dt, central difference of step d."""
    a, b = E[key(t + d)], E[key(t - d)]
    return -(a[0] - b[0]) / (2 * d * nl), np.hypot(a[1], b[1]) / (2 * d * nl)


def slope_at(E, nl, t, d=0.1):
    """d<sigma^x>/dt = -(1/N_l) d^2E/dt^2, second difference of step d."""
    a, b, c = E[key(t + d)], E[key(t)], E[key(t - d)]
    return -(a[0] - 2 * b[0] + c[0]) / (d * d * nl), np.sqrt(a[1] ** 2 + 4 * b[1] ** 2 + c[1] ** 2) / (d * d * nl)


FULL = tuple(key(0.15 + 0.05 * i) for i in range(15))          # 0.15 ... 0.85
MID = FULL[2:13]                                                  # 0.25 ... 0.75
NARROW = FULL[3:10]                                               # 0.30 ... 0.60
NW, NGEN = (192, 160) if DRY else (1920, 600)
PLAN = ({4: ((301, 302), FULL[4:11]), 6: ((301, 302), NARROW[1:6])} if DRY else
        {4: ((301, 302, 303, 304), FULL), 6: ((301, 302, 303), FULL), 8: ((301, 302, 303), MID), 10: ((301, 302, 303), NARROW)})
G = {}
for L, (seeds, ts) in PLAN.items():
    G[L] = grid_energies(L, ts, seeds, NW, NGEN)
    print(f"# {L}^3 grid done, {time.time() - T0:.0f} s", file=sys.stderr, flush=True)

# 2. against open PR 9263 (central differences of step 0.1 there and here)
REF = {4: {0.25: (0.1065, 0.0010), 0.5: (0.4378, 0.0028), 0.75: (0.6681, 0.0006)},
       6: {0.25: (0.1016, 0.0020), 0.5: (0.4562, 0.0015), 0.75: (0.6668, 0.0011)}}
rows2, ok2, n2c = [], True, 0
for L in (4, 6):
    if L not in G:
        continue
    E, nl, _ = G[L]
    for t, (rv, re) in REF[L].items():
        if key(t - 0.1) not in E or key(t + 0.1) not in E:
            continue
        v, e = sx_at(E, nl, t, 0.1)
        z = (v - rv) / np.hypot(e, re)
        ok2 &= abs(z) <= 3; n2c += 1
        rows2.append(f"{L}^3 t {t}: {v:.4f}+-{e:.4f} vs {rv:.4f}+-{re:.4f} ({z:+.1f} sigma)")
check("the grid reproduces open PR 9263's link expectations (quoted) at t = 0.25, 0.5, 0.75 on 4^3 and 6^3 with the same difference step",
      ok2 and n2c > 0, "; ".join(rows2))

# 3. the scan
rows3, ok3, peaks = [], True, {}
for L, (seeds, ts) in PLAN.items():
    E, nl, cost = G[L]
    sx = [(t, *sx_at(E, nl, t, 0.05)) for t in ts[1:-1]]
    sl = [(t, *slope_at(E, nl, t)) for t in ts[2:-2]]
    ok3 &= all(np.isfinite(x[1]) and np.isfinite(x[2]) for x in sx + sl)
    neg = [x for x in sl if x[1] < -4 * x[2]]                  # concavity: a slope of exact energies is never negative
    ok3 &= not neg
    j = int(np.argmax([x[1] for x in sl]))
    peaks[L] = sl[j]
    rows3.append(f"{L}^3 ({len(seeds)} seeds, {cost:.0f} s per energy): <sigma^x> " + " ".join(f"{t:.2f}:{v:.4f}({e * 1e4:.0f})" for t, v, e in sx)
                 + "; slope " + " ".join(f"{t:.2f}:{v:.2f}({e * 1e2:.0f})" for t, v, e in sl)
                 + f"; largest slope {sl[j][1]:.2f}+-{sl[j][2]:.2f} at t = {sl[j][0]:.2f}")
check("the scan at M = 2: <sigma^x>(t) from central differences of step 0.05 (errors in the last digits), its slope from second differences "
      "of step 0.1 (errors in hundredths), no slope below zero by more than four standard errors (concavity of E0 in t), and the largest slope "
      "per size (reported)", ok3, " || ".join(rows3) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
