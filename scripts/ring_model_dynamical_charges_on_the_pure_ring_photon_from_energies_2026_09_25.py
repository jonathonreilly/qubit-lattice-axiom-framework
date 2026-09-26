#!/usr/bin/env python3
"""Dynamical charges on the pure-ring photon: a charge-creating single-link term, from ground-state energies alone.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the clause
H = -g sum_p (U_p + U_p^dag) - t sum_l sigma^x_l + M sum_v Q_v^2 (V = 0, g = 1), where Q_v = div_v / 2 is the vertex charge.
At t = 0 the charge-free (ice) configurations decouple and H is the landed ring clause with the exact Gauss law; for t > 0 a
single-link flip creates, moves or removes a pair of unit charges, so the Gauss law holds with dynamical charges. Every
off-diagonal element is -g or -t, so the compiled projector stays sign-free; it is extended here with link events and the
charge mass (guide exp(alpha N_flip - gam sum Q^2 + sum bl sigma)). Supplied model, finite diagnostics, no physical reading.

From energies only (the mixed energy estimator is exact for any guide): E0; the link expectation <sigma^x> and the charge
density <Q^2> by Hellmann-Feynman differences in t and M; the ring expectation u from the degree-one homogeneity of E0 in
(g, t, M); the triple-averaged transverse susceptibility chi at the smallest momentum (open PR 9236's probe); and, in the
Gaussian comparator, U = 1/chi and alpha_G = (U/u)^(1/2) / (2 pi). The averaged f-sum now reads 2 u s^2 + 2 t <sigma^x>, so the
moment chain bounds the lowest transverse excitation by 2 ((u s^2 + t <sigma^x>) / chi)^(1/2), a bound that stays finite as
k -> 0 and is weak there. Checks: (1) exact 2^3 control with the single-link term on six links; (2) t = 0 against the
ring-model projector; (3) the scan t = 0-1 at M = 2 on 4^3 and 6^3, and t = 0, 0.5 on 8^3. Prints one line per check and TOTAL: PASS=N FAIL=M.
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

AUDIT_TIMEOUT_SEC = 12600

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
DTAU, H1 = 0.05, 0.15
MQ = 2.0
DT, DM = 0.1, 0.1


GAM = {0.25: 1.2, 0.5: 0.7, 0.75: 0.5, 1.0: 0.3}     # guide charge penalties tuned on 4^3 for the smallest energy variance (M = 2)


def gam_of(t, Mq):
    """The guide's charge penalty: the tuned table at M = 2, otherwise half the log of the pair cost over t (the first-order
    amplitude); the mixed energy estimator does not depend on it, the variance and the population bias do."""
    if t <= 0:
        return 1.0
    if abs(Mq - 2.0) < 1e-12 and t in GAM:
        return GAM[t]
    return 0.5 * np.log(2 * Mq / t)


# ---------------------------------------------------------------- 1. exact 2^3 control with dynamical charges
ice2 = Ice(2); T2 = QTables(ice2)
seed2 = ice2.sector_state(0)
S2 = [l for (l, sg) in ice2.inc[0]]                 # the six links at one vertex carry the single-link term
bits2 = np.arange(ice2.nl)
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
Sg2 = np.array([pp[2] for pp in props2], dtype=float)
NF2 = np.array([len(pp[0]) for pp in props2], dtype=float)
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
hv2, _ = triple(ice2, np.pi)
rows1, ok1 = [], True
for (t, Mq) in ((0.8, 1.5), (1.5, 2.0)):
    H = Hring + t * Hlink + diags(Mq * Q22)
    w, vec = eigsh(H, k=1, which="SA"); E0x = float(w[0]); psi = vec[:, 0]
    dEdg = float(psi @ (Hring @ psi)); dEdt = float(psi @ (Hlink @ psi)); dEdM = float(psi @ (Q22 * psi))
    homog = abs(E0x - (dEdg + t * dEdt + Mq * dEdM))
    Eh = float(eigsh(H - diags(H1 * (Sg2 @ hv2)), k=1, which="SA")[0][0])
    tl2 = np.zeros(ice2.nl); tl2[S2] = t
    rng = np.random.default_rng(int(10 * t))
    em = q_energy_run(ice2, T2, [seed2], 800, 400 if DRY else 3000, DTAU, 100 if DRY else 500, rng, 41 + int(10 * t), ALPHA,
                      gam_of(t, Mq), tl2, Mq)
    eh = q_energy_run(ice2, T2, [seed2], 800, 400 if DRY else 3000, DTAU, 100 if DRY else 500, rng, 43 + int(10 * t), ALPHA,
                      gam_of(t, Mq), tl2, Mq, hl=H1 * hv2, bl=0.5 * H1 * hv2)
    z0, zh = (em[0] - E0x) / em[1], (eh[0] - Eh) / eh[1]
    ok1 &= abs(z0) <= 3 and abs(zh) <= 3 and homog < 1e-9 and abs(float(abs(H - H.T).max())) < 1e-12
    rows1.append(f"t {t}, M {Mq}: {n2} states; exact E0 {E0x:.6f}, projector {em[0]:.5f}+-{em[1]:.5f} ({z0:+.1f} sigma); exact E(h) {Eh:.6f}, "
                 f"projector {eh[0]:.5f}+-{eh[1]:.5f} ({zh:+.1f} sigma); sum of sigma^x on the six links {-dEdt:.5f}, sum Q^2 {dEdM:.5f}; "
                 f"g dE/dg + t dE/dt + M dE/dM - E0 = {homog:.1e}")
check("exact 2^3 control with dynamical charges (the single-link term on the six links at one vertex): the projector's energies with and without "
      "a probe field agree with exact diagonalization of the reachable space, and the degree-one homogeneity of E0 in (g, t, M) holds exactly",
      ok1, "; ".join(rows1) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 2./3. the scan in t on the tori
def measure(L, t, seeds, nw, ngen):
    """Per seed: E0; E at t +- DT and M +- DT (Hellmann-Feynman); E at h, 2h on the cyclic triple at the smallest momentum."""
    ice = Ice(L); T = QTables(ice)
    k = 2 * np.pi / L
    hv, _ = triple(ice, k)
    pref = 2.0 if abs(np.cos(2 * k) - 1) < 1e-9 else 1.0
    res = []
    t0 = time.time()
    for sd in seeds:
        rr = np.random.default_rng(sd * 100 + L * 10 + int(10 * t))
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        gm = gam_of(t, MQ)
        run = lambda tt, mm, h, s2: q_energy_run(ice, T, init, nw, ngen, DTAU, ngen // 4, rr, s2, ALPHA, gm, np.full(ice.nl, tt), mm,
                                                 hl=h * hv, bl=0.5 * h * hv)
        base = sd * 1000 + L * 10 + int(10 * t)
        E0 = run(t, MQ, 0.0, base)
        E1 = run(t, MQ, H1, base + 1)
        E2 = run(t, MQ, 2 * H1, base + 2)
        chi, chie = chi_fit(E0[0], E0[1], E1[0], E1[1], E2[0], E2[1], H1, ice.nv, pref)
        if t > 0:
            Etp, Etm = run(t + DT, MQ, 0.0, base + 3), run(t - DT, MQ, 0.0, base + 4)
            x = -(Etp[0] - Etm[0]) / (2 * DT) / ice.nl
            xe = np.hypot(Etp[1], Etm[1]) / (2 * DT) / ice.nl
        else:
            x, xe = 0.0, 0.0
        EMp, EMm = run(t, MQ + DM, 0.0, base + 5), run(t, MQ - DM, 0.0, base + 6)
        nq = (EMp[0] - EMm[0]) / (2 * DM) / ice.nv
        nqe = np.hypot(EMp[1], EMm[1]) / (2 * DM) / ice.nv
        u = (-E0[0] - t * x * ice.nl + MQ * nq * ice.nv) / ice.np_
        res.append((E0[0] / ice.np_, chi, chie, x, xe, nq, nqe, u))
    R = np.array(res)
    n = len(R)
    def comb(j, je=None):
        m = R[:, j].mean()
        e = R[:, j].std(ddof=1) / np.sqrt(n) if n > 1 else 0.0
        if je is not None:
            e = max(e, R[:, je].mean() / np.sqrt(n))
        return float(m), float(e)
    cost = (time.time() - t0) / (len(seeds) * (7 if t > 0 else 5) * nw * ngen * DTAU)
    return dict(k=k, e0=comb(0), chi=comb(1, 2), x=comb(3, 4), nq=comb(5, 6), u=comb(7), cost=cost, s2=2 - 2 * np.cos(k))


PLAN = ({4: ((301, 302), 96, 120, (0.0, 0.5))} if DRY else
        {4: ((301, 302, 303, 304), 1920, 600, (0.0, 0.25, 0.5, 0.75, 1.0)),
         6: ((301, 302, 303, 304), 1920, 600, (0.0, 0.25, 0.5, 0.75, 1.0)),
         8: ((301, 302, 303), 1920, 600, (0.0, 0.5))})
D = {}
for L, (seeds, nw, ngen, ts) in PLAN.items():
    for t in ts:
        D[(L, t)] = measure(L, t, seeds, nw, ngen)

# 2. the t = 0 limit against the ring-model projector on the smallest torus of the plan
L0 = min(PLAN)
ice0 = Ice(L0)
e_ring = []
for sd in PLAN[L0][0]:
    rr = np.random.default_rng(sd * 100 + L0 * 10)
    init = loop_vmc(ice0, ALPHA, sweeps=max(40, 1600 // L0), therm=60, r=rr, start=ice0.sector_state(0), fix_winding=True)
    pr = Projector(ice0, np.ones(ice0.np_, bool), ALPHA, 0.0, np.zeros((1, ice0.nl), complex), sd * 1000 + L0 * 10 + 7)
    e_ring.append(run_E(pr, init, PLAN[L0][1], PLAN[L0][2], rr, np.zeros(ice0.nl), 0.0))
er = np.array([x[0] for x in e_ring]) / ice0.np_
er_m, er_e = float(er.mean()), float(max(er.std(ddof=1) / np.sqrt(len(er)), np.mean([x[1] for x in e_ring]) / ice0.np_ / np.sqrt(len(er))))
d0 = D[(L0, 0.0)]["e0"]
z2 = (d0[0] - er_m) / np.hypot(d0[1], er_e)
check(f"the single-link term switched off: on {L0}^3 the new projector's ground energy per plaquette agrees with the ring-model projector's, "
      "and no charge appears (Hellmann-Feynman density in M)", abs(z2) <= 3 and abs(D[(L0, 0.0)]["nq"][0]) <= 3 * max(D[(L0, 0.0)]["nq"][1], 1e-6),
      f"{d0[0]:.5f}+-{d0[1]:.5f} vs {er_m:.5f}+-{er_e:.5f} ({z2:+.1f} sigma); <sum Q^2>/N {D[(L0, 0.0)]['nq'][0]:+.5f}+-{D[(L0, 0.0)]['nq'][1]:.5f}")

# 3. the scan
rows3, ok3 = [], True
for L in PLAN:
    for t in PLAN[L][3]:
        d = D[(L, t)]
        c, ce = d["chi"]; u = d["u"][0]
        U = 1 / c
        a = np.sqrt(U / u) / (2 * np.pi)
        wb = 2 * np.sqrt((u * d["s2"] + t * d["x"][0]) / c)
        ok3 &= bool(np.isfinite(c) and c > 0 and ce / c < 0.25 and (t == 0 or d["x"][0] > 0))
        rows3.append(f"{L}^3 t={t}: e0 {d['e0'][0]:.5f}, sx {d['x'][0]:.4f}({d['x'][1] * 1e4:.0f}), Q2 {d['nq'][0]:.4f}({d['nq'][1] * 1e4:.0f}), "
                     f"u {u:.4f}, chi {c:.3f}({ce * 1e3:.0f}), alpha_G {a:.4f}, w-bound {wb:.3f}")
check("dynamical charges on 4^3-8^3 at M = 2, V = 0 (reported): against t, the energy per plaquette, <sigma^x> per link and <Q^2> per site "
      "(Hellmann-Feynman), the ring expectation u (homogeneity), chi at the smallest momentum (errors in the last digits), alpha_G = (1/chi u)^(1/2) "
      "/ (2 pi) and the moment-chain bound on the lowest transverse excitation", ok3, " || ".join(rows3) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
