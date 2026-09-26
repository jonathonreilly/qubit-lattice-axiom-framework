#!/usr/bin/env python3
"""Supplied finite ring model H=-sum R+V sum n. Differentiable selected-component ground energies give u=-(E-V Eprime)/Np. The diagonal potential leaves the centered real-ground cyclic f-sum unchanged. At V=1 uniform component ground states satisfy the positive-measure susceptibility floor. The six-point L=8 finite-population sweep and loop samples are biased diagnostics, not exact spectral bounds, continuous trends, saturation, dispersion, velocity or phase determinations."""
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
AUDIT_INPUT_PATHS = ['docs/RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md']

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


def run_E(pr, init, nw, ngen, rng, hvec, h, beta=0.5):
    out, _ = energy_run(pr, init, nw, ngen, DTAU, ngen // 4, rng, h * hvec, beta * h * hvec, Lcs=(0,))
    return out[0]


def triple(ice, k):
    """The cyclic triple of transverse modes: a-links modulated along axis (a + 1) mod 3 (each plaquette orientation once)."""
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    hv = np.cos(k * xb)
    PH = np.array([np.exp(1j * k * xb) * (ice.axis == a) / np.sqrt(ice.nv) for a in range(3)])
    return hv, PH


def h_for(V):
    return 0.15 if V < 0.7 else (0.06 if V < 0.97 else 0.02)


def sweep_point(L, V, ms, seed, nw):
    """chi_T(k) for the momenta ms and the ring expectation u = -(E0 - V dE0/dV)/N_p (Hellmann-Feynman, backward step) at one V."""
    ice = Ice(L)
    rr = np.random.default_rng(seed)
    alpha = 0.2 * (1 - V)
    init = loop_vmc(ice, alpha, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    pr = Projector(ice, np.ones(ice.np_, bool), alpha, V, np.zeros((1, ice.nl), complex), seed)
    z = np.zeros(ice.nl)
    E0 = run_E(pr, init, nw, NGEN, rr, z, 0.0)
    pr.V = V - DV
    Em = run_E(pr, init, nw, NGEN, rr, z, 0.0)
    pr.V = V
    nf = (E0[0] - Em[0]) / DV / ice.np_
    u = -(E0[0] - V * nf * ice.np_) / ice.np_
    out = {}
    for m in ms:
        k = 2 * np.pi * m / L
        hv, _ = triple(ice, k)
        h1 = h_for(V)
        E1 = run_E(pr, init, nw, NGEN, rr, hv, h1)
        E2 = run_E(pr, init, nw, NGEN, rr, hv, 2 * h1)
        a = (15 * E0[0] - 16 * E1[0] + E2[0]) / (12 * h1 ** 2)
        sa = np.sqrt(225 * E0[1] ** 2 + 256 * E1[1] ** 2 + E2[1] ** 2) / (12 * h1 ** 2)
        out[m] = (4 * a / (3 * ice.nv), 4 * sa / (3 * ice.nv))
    return out, u, nf, E0[0] / ice.np_


# ------------------------------------------------------------------------------------------------ main
DTAU, DV = 0.05, 0.03
NW, NGEN = (48, 120) if DRY else (480, 600)
L8 = 4 if DRY else 8
VS = (0.0, 0.5, 1.0) if DRY else (0.0, 0.25, 0.5, 0.75, 0.9, 1.0)
SEEDS = (501,) if DRY else (501, 502, 503)
MS = (1, 2) if not DRY else (1,)

# ---------------------------------------------------------------- 1. uniform ice, sampled directly: the RK floor
ice8 = Ice(L8)
smp = loop_vmc(ice8, 0.0, sweeps=100 if DRY else 2000, therm=100, r=np.random.default_rng(510), start=ice8.sector_state(0), fix_winding=True)
Su, nfu = {}, float(np.mean([(np.abs(ice8.circ(s)[:-1]) == 4).mean() for s in smp]))
for m in MS:
    k = 2 * np.pi * m / L8
    _, PHt = triple(ice8, k)
    vals = np.array([np.mean(np.abs(PHt @ s) ** 2) for s in smp])
    ch = np.array_split(np.arange(len(vals)), 10)
    Su[m] = (float(vals.mean()), float(np.std([vals[c].mean() for c in ch], ddof=1) / np.sqrt(10)))

# ---------------------------------------------------------------- 2. the sweep
sweep = {}
for V in VS:
    print(f"Starting full V={V} grid", flush=True)
    for sd in SEEDS:
        out, u, nf, e0 = sweep_point(L8, V, MS, sd * 10 + int(round(100 * V)), NW)
        sweep.setdefault(V, []).append((out, u, nf, e0))
def comb(vals, errs):
    vals, errs = np.array(vals), np.array(errs)
    n = len(vals)
    return float(vals.mean()), float(max(np.std(vals, ddof=1) / np.sqrt(n) if n > 1 else 0.0, errs.mean() / np.sqrt(n)))
tab = {}
for V, lst in sweep.items():
    u = float(np.mean([x[1] for x in lst])); nf = float(np.mean([x[2] for x in lst])); e0 = float(np.mean([x[3] for x in lst]))
    for m in MS:
        c, ce = comb([x[0][m][0] for x in lst], [x[0][m][1] for x in lst])
        k = 2 * np.pi * m / L8
        s2 = 2 - 2 * np.cos(k)
        w = 2 * np.sqrt(s2 * u / c)
        tab[(V, m)] = dict(chi=c, chie=ce, u=u, nf=nf, e0=e0, w=w, we=w * ce / (2 * c), vs=w / np.sqrt(s2), vse=w / np.sqrt(s2) * ce / (2 * c),
                           S=np.sqrt(s2 * u * c), Se=np.sqrt(s2 * u * c) * ce / (2 * c), s2=s2)
# RK anchor: at V = g the ground state is uniform ice, u = n_f, and chi >= 2 S^2 / f = S^2 / (u s^2) with the directly sampled S
rk_rows, rk_ok = [], True
for m in MS:
    t = tab[(1.0, m)]
    floor = Su[m][0] ** 2 / (t["u"] * t["s2"])
    rk_ok &= t["chi"] >= floor - 3 * t["chie"] and abs(t["S"] - Su[m][0]) <= 3 * np.hypot(t["Se"], Su[m][1]) + 0.05 * Su[m][0]
    rk_rows.append(f"k={2 * np.pi * m / L8:.3f}: chi {t['chi']:.2f}+-{t['chie']:.2f} vs floor S^2/(u s^2) {floor:.2f}; S_T bound {t['S']:.3f}+-{t['Se']:.3f} "
                   f"vs uniform-ice S_T {Su[m][0]:.3f}+-{Su[m][1]:.3f}")
check("the RK anchor: at V = g the projector's energy vanishes identically, the Hellmann-Feynman ring expectation equals the flippable density, "
      "nominal susceptibility and structure-factor comparisons use finite loop samples; component matching and equilibration unproved",
      rk_ok and abs(tab[(1.0, MS[0])]["e0"]) < 1e-9 and abs(tab[(1.0, MS[0])]["u"] - nfu) < 0.01,
      f"e0 {tab[(1.0, MS[0])]['e0']:.1e}; u {tab[(1.0, MS[0])]['u']:.4f} vs sampled n_f {nfu:.4f}; " + "; ".join(rk_rows))

rows = []
for V in VS:
    rows.append(f"V={V:.2f}: u {tab[(V, MS[0])]['u']:.4f}, n_f {tab[(V, MS[0])]['nf']:.4f}, " + ", ".join(
        f"k={2 * np.pi * m / L8:.3f}: chi {tab[(V, m)]['chi']:.3f}+-{tab[(V, m)]['chie']:.3f}, omega/s bound {tab[(V, m)]['vs']:.3f}+-{tab[(V, m)]['vse']:.3f}, "
        f"S_T bound {tab[(V, m)]['S']:.3f}" for m in MS))
check("the sweep from the pure-ring point to the RK point on 8^3: susceptibility, ring expectation, and estimated moment upper bounds (finite diagnostics)",
      all(np.isfinite(list(tab[(V,m)].values())).all() and tab[(V,m)]["chi"] > 0 and tab[(V,m)]["u"] > 0 and tab[(V, m)]["chie"] / tab[(V, m)]["chi"] < 0.25 for V in VS for m in MS), " || ".join(rows) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3. the velocity law and the quadratic mode
Vfit = np.array([V for V in VS if V < 0.95])
y = np.array([tab[(V, MS[0])]["vs"] for V in Vfit]); ye = np.array([tab[(V, MS[0])]["vse"] for V in Vfit])
cf, cv = np.polyfit(np.log(1 - Vfit), np.log(y), 1, w=y / ye, cov="unscaled")
gam, game = float(cf[0]), float(np.sqrt(cv[0, 0]))
ratio_rows = []
if len(MS) > 1:
    for V in VS:
        r = tab[(V, 1)]["chi"] / tab[(V, 2)]["chi"]
        re = r * np.hypot(tab[(V, 1)]["chie"] / tab[(V, 1)]["chi"], tab[(V, 2)]["chie"] / tab[(V, 2)]["chi"])
        ratio_rows.append(f"V={V:.2f}: {r:.2f}+-{re:.2f}")
    s_ratio = tab[(0.0, 2)]["s2"] / tab[(0.0, 1)]["s2"]
check("descriptive fits of estimated upper bounds (not a dispersion or velocity law): the bound on omega/s at the smallest momentum against (1 - V/g)^gamma below the RK "
      "point, and chi(k_min)/chi(2 k_min) along the sweep (1 for a linear mode with k-independent chi, s(2k)^2/s(k)^2 for a quadratic one)", True,
      f"gamma {gam:.3f}+-{game:.3f} over V/g = {', '.join(f'{v:.2f}' for v in Vfit)} (1/2 for c ~ sqrt(1 - V/g)); chi ratio " + "; ".join(ratio_rows)
      + (f" (quadratic value {s_ratio:.2f})" if len(MS) > 1 else ""))

print(f"elapsed_sec: {time.time() - T0:.0f}")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
