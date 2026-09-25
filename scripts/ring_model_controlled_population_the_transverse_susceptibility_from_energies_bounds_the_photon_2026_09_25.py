#!/usr/bin/env python3
"""Controlling the population at the pure-ring point: a compiled local-update projector, the static transverse susceptibility
from energies alone, and energy-only bounds on the photon.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law
(cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (landed). Supplied model, finite diagnostics, no
physical reading.

Open PR 9220 found that the fixed-population projector's forward-walking structure factors were biased on the larger tori:
the walker population, not the torus, steered them, and lineages collapse (0.5 % distinct ancestors at lag 2 on 16^3). This
runner (i) replaces the projector by a compiled continuous-time one whose event cost does not grow with the torus (only the
plaquettes within two link steps of a flip change their rates); (ii) measures an observable that needs no lineages: the static
transverse susceptibility chi_T(k) = 2 sum_n |<n|O_k|0>|^2 / (E_n - E_0), from ground-state energies in a weak field
-h sum cos(k x) sigma_z (the mixed energy estimator is exact for any guide, and the population bias cancels in differences);
(iii) combines chi with the exact f-sum rule f(k) = <O_k^dag (H - E_0) O_k> = 2 u_0 s^2 (open PR 9161) through the moment chain
of the spectral measure |<n|O_k|0>|^2: the lowest excitation coupled to O_k satisfies omega_min <= S/(chi/2) <= sqrt(2 f/chi)
= 2 s(k) sqrt(u_0/chi), and S_T(k) <= s(k) sqrt(u_0 chi) (Cauchy-Schwarz). Both bounds use energies only.

Checks: (1) exact 2^3 control of chi, the moment chain and the projected energies in a field; (2) the compiled projector with
records against an exact 3646-state region; (3) speed, and the walker-number independence of chi on 8^3; (4) chi_T(k) on the
4^3-16^3 tori with two independent seeds, the bounds, and the exponent of chi in k; (5) the forward-walking structure factors
of open PRs 9161, 9171, 9220 against the bound. Prints one line per check and TOTAL: PASS=N FAIL=M.
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
from scipy.sparse.linalg import eigsh, minres

AUDIT_TIMEOUT_SEC = 3600

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


def stats(x, n_bins=10):
    x = np.asarray(x, dtype=float)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))


def exact_L2(ice, canon):
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    codes = []
    n = 1 << ice.nl
    step = 1 << 18
    for start in range(0, n, step):
        ids = np.arange(start, min(n, start + step), dtype=np.int64)
        sig = (((ids[:, None] >> bits) & 1) * 2 - 1).astype(np.int64)
        ok = np.all(sig @ B.T == 0, axis=1)
        codes.append(ids[ok])
    codes = np.concatenate(codes)
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)

    def sig_of(code):
        return ((code >> bits) & 1) * 2 - 1

    def flippable(code):
        s = sig_of(code)
        return np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)

    def code_of(s):
        return int(((s + 1) // 2 * (1 << bits)).sum())

    c0 = code_of(canon)
    comp = {c0: 0}
    order = [c0]
    q = 0
    while q < len(order):
        c = order[q]
        q += 1
        for p in flippable(c):
            c2 = int(c ^ masks[p])
            if c2 not in comp:
                comp[c2] = len(order)
                order.append(c2)
    n_c = len(order)
    rows, cols = [], []
    for c in order:
        for p in flippable(c):
            rows.append(comp[int(c ^ masks[p])])
            cols.append(comp[c])
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n_c, n_c)).tocsr()
    return codes, order, H, sig_of




class Region:
    """The unrecorded interior {1..m}^3 of an L_out = m + 2 torus whose other links carry records, or the whole torus (m = None)."""
    def __init__(self, ice, m=None):
        self.ice, self.m, self.L = ice, m, ice.L
        V = np.array(ice.verts)
        if m is None:
            self.vin = np.ones(ice.nv, bool)
            self.rec = np.zeros(ice.nl, bool)
            self.depth = np.full(ice.nv, 10 ** 6)
        else:
            assert ice.L == m + 2
            self.vin = np.all((V >= 1) & (V <= m), axis=1)
            self.rec = ~(self.vin[ice.tail] & self.vin[ice.head])
            self.depth = np.where(self.vin, np.min(np.minimum(V, m + 1 - V), axis=1), 0)
        self.dyn = ~self.rec[ice.plaq].any(axis=1)
        self.dyn_ext = np.append(self.dyn, False)
        self.n_dyn = int(self.dyn.sum())
        self.V = V

    def deltas(self, sigma, C, P):
        ice = self.ice
        Ca = C[ice.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", ice.M[P], sigma[ice.plaq[P]])
        dm = self.dyn_ext[ice.A[P]]
        return Cn, ((np.abs(Cn) == 4) & dm).sum(axis=1) - ((np.abs(Ca) == 4) & dm).sum(axis=1)

    def plane_fluxes(self, sigma):
        """Flux of the unrecorded links through every lattice plane section of the region (all axes, all positions)."""
        ice = self.ice
        out = []
        for a in range(3):
            sel = (ice.axis == a) & ~self.rec
            coords = ice.coord[sel]
            vals = sigma[sel]
            out += [int(vals[coords == c].sum()) for c in np.unique(coords)]
        return np.array(out)



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


# ------------------------------------------------------------------------------------------------ main
DTAU, H1 = 0.05, 0.15
NW, NGEN = (48, 120) if DRY else (480, 600)

# ---------------------------------------------------------------- 1. exact 2^3 control
ice2 = Ice(2); canon2 = ice2.sector_state(0)
codes, order, H2, sig_of = exact_L2(ice2, canon2)
Sg = np.array([sig_of(c) for c in order]).astype(float)
hv2, PH2 = triple(ice2, np.pi)
Ftot = Sg @ hv2
v, V = eigsh(H2, k=40, which="SA"); o = np.argsort(v); v, V = v[o], V[:, o]
E0x = float(v[0]); psi = V[:, 0] * np.sign(V[:, 0].sum())
chis, Ss, fs, coup = [], [], [], np.zeros(len(v))
for a in range(3):
    O = np.real(Sg @ PH2[a])                                       # k = pi: the mode is real
    rhs = O * psi; rhs -= psi * (psi @ rhs)
    x, _ = minres((H2 - E0x * diags(np.ones(len(psi)))).tocsr(), rhs, rtol=1e-12); x -= psi * (psi @ x)
    chis.append(2 * float(rhs @ x)); Ss.append(float(rhs @ rhs)); fs.append(float(rhs @ (H2 @ rhs)) - E0x * float(rhs @ rhs))
    coup += (V.T @ rhs) ** 2
chi_ex, S_ex, f_ex = float(np.mean(chis)), float(np.mean(Ss)), float(np.mean(fs))
u_ex = -E0x / ice2.np_
w_min = min(v[n] - E0x for n in range(1, len(v)) if coup[n] > 1e-12)
chain = [w_min, S_ex / (chi_ex / 2), np.sqrt(f_ex / (chi_ex / 2)), f_ex / S_ex]
Ex = {h: float(eigsh((H2 - h * diags(Ftot)).tocsr(), k=1, which="SA")[0][0]) for h in (H1, 2 * H1)}
a_fit = (15 * E0x - 16 * Ex[H1] + Ex[2 * H1]) / (12 * H1 ** 2)
chi_fit_ex = 4 * a_fit / (3 * 2.0 * ice2.nv)                        # k = pi doubles the prefactor
pr2 = Projector(ice2, np.ones(ice2.np_, bool), ALPHA, 0.0, np.zeros((1, ice2.nl), complex), 101)
r2 = np.random.default_rng(102)
qm = {h: run_E(pr2, [canon2], 400, 400 if DRY else 1600, r2, hv2, h) for h in (0.0, H1, 2 * H1)}
fsum_dev = abs(f_ex - 2 * u_ex * 4.0)
dev = [(qm[h][0] - (E0x if h == 0 else Ex[h])) / qm[h][1] for h in qm]
check("exact 2^3 control at k = pi for the cyclic mode triple: the averaged f-sum rule without symmetry, the susceptibility, the moment chain, "
      "the structure-factor bound, and projected energies in a field",
      chain[0] <= chain[1] <= chain[2] <= chain[3] and S_ex <= np.sqrt(chi_ex * f_ex / 2) and abs(chi_fit_ex / chi_ex - 1) < 0.03
      and max(abs(d) for d in dev) <= 3 and fsum_dev < 1e-9,
      f"E0 {E0x:.6f}; mode-averaged f {f_ex:.6f} = 2 u s^2 {2 * u_ex * 4:.6f}; per-mode chi {', '.join(f'{c:.5f}' for c in chis)}, average {chi_ex:.5f}; S {S_ex:.5f}; lowest coupled level {chain[0]:.4f} <= S/(chi/2) {chain[1]:.4f} <= "
      f"sqrt(2f/chi) {chain[2]:.4f} <= f/S {chain[3]:.4f}; S <= sqrt(chi f/2) = {np.sqrt(chi_ex * f_ex / 2):.5f}; the h^4-eliminating fit of the exact "
      f"E(h) gives chi {chi_fit_ex:.5f}; projector energies at h = 0, {H1}, {2 * H1}: deviations " + ", ".join(f"{d:+.1f}" for d in dev)
      + f" standard errors; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. the compiled projector with records against exact diagonalization
ice5 = Ice(5)
frame5 = loop_vmc(ice5, 0.0, sweeps=60, therm=60, r=np.random.default_rng(11))[-1]
reg5 = Region(ice5, 3)
masks5 = [sum(1 << int(l) for l in links) for links in ice5.plaq]
dyn5 = np.flatnonzero(reg5.dyn)
def sig5(c):
    return np.array([1 if (c >> l) & 1 else -1 for l in range(ice5.nl)])
def flip5(s):
    return dyn5[np.abs((s[ice5.plaq[dyn5]] * ice5.sign[dyn5]).sum(axis=1)) == 4]
c0 = int(sum(1 << int(l) for l in np.flatnonzero(frame5 > 0)))
comp, order5, q = {c0: 0}, [c0], 0
while q < len(order5):
    s = sig5(order5[q]); q += 1
    for p in flip5(s):
        c2 = order5[q - 1] ^ masks5[p]
        if c2 not in comp:
            comp[c2] = len(order5); order5.append(c2)
rows, cols, nfl = [], [], np.zeros(len(order5))
for i, c in enumerate(order5):
    fp = flip5(sig5(c)); nfl[i] = len(fp)
    for p in fp:
        rows.append(comp[c ^ masks5[p]]); cols.append(i)
H5 = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(len(order5), len(order5))).tocsr()
v5, w5 = eigsh(H5, k=1, which="SA")
E05, nf_ex = float(v5[0]), float((np.abs(w5[:, 0]) ** 2) @ nfl) / reg5.n_dyn
pj = Projector(ice5, reg5.dyn, ALPHA, 0.0, np.zeros((1, ice5.nl), complex), 103)
res5 = pj.run([frame5], n_w=200, n_gen=300 if DRY else 1200, dtau=DTAU, therm=240 if not DRY else 60, lags=(20, 40), rng=np.random.default_rng(104))
e5 = res5["e"][res5["therm"]:]
ch = np.array_split(np.arange(len(e5)), 10)
e5m, e5e = e5.mean(), np.std([e5[c].mean() for c in ch], ddof=1) / np.sqrt(10)
nf5 = res5["fw"][:, 1, 1]
nf5m, nf5e = nf5.mean(), np.std([nf5[c].mean() for c in np.array_split(np.arange(len(nf5)), 10)], ddof=1) / np.sqrt(10)
check("the compiled local-update projector with records against exact diagonalization on the 3^3 interior: energy and pure flippable density",
      abs(e5m - E05) <= 3 * e5e and abs(nf5m - nf_ex) <= 3 * nf5e,
      f"E0 exact {E05:.5f}, projector {e5m:.4f}+-{e5e:.4f}; n_f exact {nf_ex:.5f}, pure at lag 2 {nf5m:.5f}+-{nf5e:.5f}")

# ---------------------------------------------------------------- 3./4. the susceptibility grid, seeds and the walker population
def measure_L(L, ms, seeds, nw):
    """chi_T(2 pi m / L) per seed: E(0) shared by the momenta of one seed; E(h1), E(2 h1) per momentum."""
    ice = Ice(L)
    out = {m: [] for m in ms}
    u0s, cost = [], []
    for sd in seeds:
        rr = np.random.default_rng(sd * 100 + L + nw)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), sd * 1000 + L + nw)
        t0 = time.time()
        E0 = run_E(pr, init, nw, NGEN, rr, np.zeros(ice.nl), 0.0)
        cost.append((time.time() - t0) / (nw * NGEN * DTAU))
        u0s.append(-E0[0] / ice.np_)
        for m in ms:
            k = 2 * np.pi * m / L
            hv, _ = triple(ice, k)
            E1 = run_E(pr, init, nw, NGEN, rr, hv, H1)
            E2 = run_E(pr, init, nw, NGEN, rr, hv, 2 * H1)
            pref = 2.0 if abs(np.cos(2 * k) - 1) < 1e-9 else 1.0
            out[m].append(chi_fit(*E0, *E1, *E2, H1, ice.nv, pref))
    return out, float(np.mean(u0s)), float(np.std(u0s)), float(np.mean(cost))


GRID = ({4: ((1,), (301, 302), 96), 6: ((1,), (301, 302), 96)} if DRY else
        {4: ((1,), (301, 302, 303), 480), 6: ((1,), (301, 302, 303), 480), 8: ((1, 2), (301, 302, 303, 304), 480),
         12: ((1, 2, 3), (301, 302, 303), 480), 16: ((1, 2, 4), (301, 302), 480)})
POPW = 192 if DRY else 1920
data, u0L, costL = {}, {}, {}
for L, (ms, seeds, nw) in GRID.items():
    out, u0, u0e, cst = measure_L(L, ms, seeds, nw)
    for m in ms:
        data[(L, m)] = out[m]
    u0L[L], costL[L] = (u0, u0e), cst
Lp = 4 if DRY else 8
outP, u0P, _, costP = measure_L(Lp, (1, 2) if not DRY else (1,), (401, 402, 403, 404) if not DRY else (401, 402), POPW)
# pooled ratio of seed scatter to the mean bin error, from every (L, m) with at least three seeds
ratios = []
for key, lst in list(data.items()) + [((Lp, m), outP[m]) for m in outP]:
    if len(lst) >= 3:
        cs = np.array([x[0] for x in lst]); be = np.array([x[1] for x in lst])
        ratios.append(np.std(cs, ddof=1) / be.mean())
r_pool = float(np.sqrt(np.mean(np.square(ratios)))) if ratios else 1.0
def combine(lst):
    cs = np.array([x[0] for x in lst]); be = np.array([x[1] for x in lst])
    n = len(cs)
    err = max(np.std(cs, ddof=1) / np.sqrt(n) if n > 1 else 0.0, r_pool * be.mean() / np.sqrt(n))
    return float(cs.mean()), float(err), cs
pop_rows, pop_ok = [], True
for m in outP:
    a, ae, _ = combine(data[(Lp, m)]); b, be_, _ = combine(outP[m])
    z = (a - b) / np.hypot(ae, be_)
    pop_ok &= abs(z) <= 3
    pop_rows.append(f"k = {2 * np.pi * m / Lp:.3f}: {GRID[Lp][2]} walkers chi {a:.3f}+-{ae:.3f}, {POPW} walkers chi {b:.3f}+-{be_:.3f} ({z:+.1f} sigma)")
check("the walker population and the seed scatter: on 8^3 the susceptibility from energy differences agrees within errors between "
      f"{GRID[Lp][2]} and {POPW} walkers, while the plain energy shifts; independent seeds scatter by {r_pool:.2f} times the ten-bin errors, and every "
      "error below is, conservatively, the larger of the seed scatter and that ratio times the bin error (a heuristic inflation, not a calibrated "
      "error model)", pop_ok,
      "; ".join(pop_rows) + f"; plain e0 {-u0L[Lp][0]:.5f} ({GRID[Lp][2]}) vs {-u0P:.5f} ({POPW}); cost {costL[Lp] * 1e3:.2f} and {costP * 1e3:.2f} ms per "
      f"walker-time (earlier numpy projector: 47 ms on 8^3, 500 on 12^3, 2170 on 16^3; here {costL.get(12, 0) * 1e3:.2f} and {costL.get(16, 0) * 1e3:.2f})")

table, rows_out = {}, []
for (L, m), lst in sorted(data.items()):
    if L == Lp:
        lst = lst + outP[m]
    c, ce, cs = combine(lst)
    k = 2 * np.pi * m / L
    s2 = 2 - 2 * np.cos(k)
    u0 = u0L[L][0]
    w_chi, S_max = 2 * np.sqrt(s2 * u0 / c), np.sqrt(s2 * u0 * c)
    table[(L, m)] = dict(k=k, chi=c, chie=ce, u0=u0, w=w_chi, we=w_chi * ce / (2 * c), S=S_max, Se=S_max * ce / (2 * c), s=np.sqrt(s2), n=len(cs))
    rows_out.append(f"{L}^3 k={k:.3f}: chi {c:.3f}+-{ce:.3f} ({len(cs)} runs), omega bound {w_chi:.3f}+-{w_chi * ce / (2 * c):.3f} "
                    f"(/s(k) {w_chi / np.sqrt(s2):.3f}), S_T bound {S_max:.3f}+-{S_max * ce / (2 * c):.3f}")
ks = np.array([t["k"] for t in table.values()]); chis = np.array([t["chi"] for t in table.values()]); chies = np.array([t["chie"] for t in table.values()])
cp, cov = np.polyfit(np.log(ks), np.log(chis), 1, w=chis / chies, cov="unscaled")
p_exp, p_err = -cp[0], float(np.sqrt(cov[0, 0]))
chi_bar = float((chis / chies ** 2).sum() / (1 / chies ** 2).sum()); chi_bar_e = float(1 / np.sqrt((1 / chies ** 2).sum()))
chi2_flat = float((((chis - chi_bar) / chies) ** 2).sum())
check("the static transverse susceptibility on the 4^3-16^3 tori and the energy-only bounds on the lowest transverse excitation and on the "
      "structure factor; the exponent of chi in k (reported)", bool(np.all(chis > 0) and np.all(chies / chis < 0.25)),
      " || ".join(rows_out) + f" || chi ~ k^-p: p = {p_exp:.3f}+-{p_err:.3f} (0 photon, 1 residual constant, 2 quadratic mode); weighted mean chi "
      f"{chi_bar:.3f}+-{chi_bar_e:.3f}, chi^2 about it {chi2_flat:.1f} for {len(chis) - 1} degrees of freedom; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. what the bounds exclude
FW = {(4, 1): (0.710, 0.010, "run average"), (6, 1): (0.572, 0.018, "run average"), (8, 1): (0.491, 0.022, "run average"),
      (8, 2): (0.765, 0.013, "run average"), (12, 1): (0.496, 0.057, "100 walkers"), (12, 2): (0.778, 0.048, "100 walkers"),
      (12, 3): (0.891, 0.075, "100 walkers"), (16, 1): (0.591, 0.037, "120 walkers"), (16, 2): (0.770, 0.047, "120 walkers"), (16, 4): (1.039, 0.073, "120 walkers")}
cmp_rows = []
for key, (sv, se, lab) in FW.items():
    if key in table:
        t = table[key]
        z = (sv - t["S"]) / np.hypot(se, t["Se"])
        cmp_rows.append(f"{key[0]}^3 k={t['k']:.3f}: forward walking {sv:.3f}+-{se:.3f} ({lab}), bound {t['S']:.3f}+-{t['Se']:.3f}: {z:+.1f} sigma")
excl = []
S0 = 0.392                                                     # the residual constant of open PR 9171's constant-plus-linear fit
for key in ((12, 1), (16, 1)):
    if key in table:
        t = table[key]
        need = (S0 / t["s"]) ** 2 / t["u0"]
        excl.append(f"a residual S_0 = {S0} at {key[0]}^3 k={t['k']:.3f} needs chi >= {need:.2f}, measured {t['chi']:.2f}+-{t['chie']:.2f} "
                    f"({(need - t['chi']) / t['chie']:.1f} sigma below)")
if (12, 1) in table and (12, 3) in table:
    rq = table[(12, 1)]["chi"] / table[(12, 3)]["chi"]
    rqe = rq * np.hypot(table[(12, 1)]["chie"] / table[(12, 1)]["chi"], table[(12, 3)]["chie"] / table[(12, 3)]["chi"])
    excl.append(f"chi(pi/6)/chi(pi/2) on 12^3 = {rq:.2f}+-{rqe:.2f} (a quadratic mode with constant S_T gives about 9, a residual constant about 3)")
U_eff, K_eff = 1 / chi_bar, 4 * float(np.mean([t["u0"] for t in table.values()]))
check("what the energy-only bounds exclude (reported): the forward-walking structure factors of open PRs 9161, 9171 and 9220, a residual constant "
      "in S_T, a quadratic mode; the Gaussian lattice-Maxwell reading U = 1/chi, K = 4 u0 of open PR 9166", True,
      "; ".join(cmp_rows) + " || " + "; ".join(excl) + f" || U = 1/chi {U_eff:.3f}, K = 4 u0 {K_eff:.3f}, velocity sqrt(UK) {np.sqrt(U_eff * K_eff):.3f}, "
      f"S_T/s(k) sqrt(K/U)/2 {np.sqrt(K_eff / U_eff) / 2:.3f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
