#!/usr/bin/env python3
"""On 8^3 at k = pi/4: the curvature estimate in both guide schemes, with and without a walker population.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law and
the clause -g (U + U^dag) at V = 0, g = 1 (landed), in the cyclic-triple transverse probe field of the landed ring-component note,
H(h) = H - h sum_l hv_l sigma_l. The curvature estimate uses E(0), E(H1), E(2 H1) with H1 = 0.15. Open PR 9328 found that the
fixed-population projector's estimate depends on the guide scheme by about a quarter on 16^3 and 24^3. Here the same estimate is
formed on 8^3 from reptation mixed energies (one continuous-time importance-sampled path, moves accepted with exp of the change in
minus the integrated local energy, bounce on rejection; mixed energy at the two path ends), which carry no population-control bias,
and from the projector in both schemes with the settings of open PRs 9298 and 9328.

Checks: (1) incremental rate tables and local energy against brute-force recomputation on 4^3 with charges present; (2) exact 2^3
control of the reptation energies and three-point curvature; (3) 8^3 reptation with one guide for the three fields; (4) 8^3
reptation with a guide per field (the energies at 0 and 2 H1 rerun with their own guides): energies and curvature within three
combined errors of (3), the scheme difference reported; (5) 8^3 projector, 960 walkers, both schemes: each within three combined
errors of (3); (6) 12^3 projector in both schemes, the scheme difference reported. Reptation errors are from blocks of one path per
field; the scheme differences in (4) show they understate the reptation uncertainty. Finite diagnostics: estimated values, not
certified values, population convergence or a limit.
Prints TOTAL: PASS=N FAIL=M.
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
def rq_apply(e, ev, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl, gam, bl, gg,
             stamp, tick, cbuf, cstamp):
    """Apply event ev (plaquette index < Np, else link Np + l) to end state e, with every table and rate update."""
    Np = C.shape[1]
    Wd = A.shape[1]
    s_ = sig[e]; C_ = C[e]; f_ = flp[e]; Q_ = Q[e]; r_ = rate[e]; b_ = bs[e]
    tick[0] += 1
    tk = tick[0]
    nC = 0
    if ev < Np:
        for k in range(4):
            l = plaq[ev, k]
            Fh[e] -= 2.0 * hl[l] * s_[l]
            s_[l] = -s_[l]
            for j in range(4):
                q = pol4[l, j]
                if cstamp[q] != tk:
                    cstamp[q] = tk; cbuf[nC] = q; nC += 1
    else:
        l = ev - Np
        sv = s_[l]
        Fh[e] -= 2.0 * hl[l] * sv
        s_[l] = -sv
        a_, b2 = tail[l], head[l]
        qa, qb = Q_[a_], Q_[b2]
        Q_[a_] = qa - sv
        Q_[b2] = qb + sv
        sq2[e] += (qa - sv) * (qa - sv) - qa * qa + (qb + sv) * (qb + sv) - qb * qb
        for j in range(4):
            q = pol4[l, j]
            if cstamp[q] != tk:
                cstamp[q] = tk; cbuf[nC] = q; nC += 1
    for jj in range(nC):
        q = cbuf[jj]
        c = 0
        for k in range(4):
            c += s_[plaq[q, k]] * sign[q, k]
        oldf = f_[q]
        C_[q] = c
        newf = dynf[q] and (c == 4 or c == -4)
        f_[q] = newf
        nflp[e] += (1 if newf else 0) - (1 if oldf else 0)
    for jj in range(nC):
        q = cbuf[jj]
        for j2 in range(Wd):
            s = A[q, j2]
            if s < 0:
                break
            if stamp[s] != tk:
                stamp[s] = tk
                rn = q_rate_plaq(s, s_, C_, f_, plaq, A, M, dynf, exptab, bl, gg)
                b_[s // 64] += rn - r_[s]; r_[s] = rn
        for k in range(4):
            m = plaq[q, k]
            e2 = Np + m
            if stamp[e2] != tk:
                stamp[e2] = tk
                rn = q_rate_link(m, s_, C_, f_, Q_, pol4, pols, dynf, tail, head, exptab, tl, gam, bl)
                b_[e2 // 64] += rn - r_[e2]; r_[e2] = rn
    if ev >= Np:
        l = ev - Np
        for vv in range(2):
            v = tail[l] if vv == 0 else head[l]
            for j in range(6):
                m = inc6[v, j]
                e2 = Np + m
                if stamp[e2] != tk:
                    stamp[e2] = tk
                    rn = q_rate_link(m, s_, C_, f_, Q_, pol4, pols, dynf, tail, head, exptab, tl, gam, bl)
                    b_[e2 // 64] += rn - r_[e2]; r_[e2] = rn


@nb.njit(cache=False)
def rq_resum(e, rate, bs):
    for b in range(bs.shape[1]):
        bs[e, b] = 0.0
    for i in range(rate.shape[1]):
        bs[e, i // 64] += rate[e, i]


@nb.njit(cache=False)
def rq_grow(e, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl,
            gam, bl, gg, Mq, stamp, tick, cbuf, cstamp):
    """Run the importance-sampled jump process for time dur from end e; events into evbuf. Returns (W = -int E_L, count, overflow)."""
    ne = rate.shape[1]
    nblk = bs.shape[1]
    t = 0.0
    W = 0.0
    n = 0
    while True:
        lam = 0.0
        for b in range(nblk):
            lam += bs[e, b]
        EL = Mq * sq2[e] - Fh[e] - lam
        h = -np.log(1.0 - np.random.random()) / lam if lam > 0 else 1e300
        if t + h >= dur:
            W -= EL * (dur - t)
            return W, n, False
        W -= EL * h
        t += h
        u = np.random.random() * lam
        acc = 0.0
        ev = -1
        for b in range(nblk):
            if acc + bs[e, b] > u:
                lo = b * 64
                hi = min(lo + 64, ne)
                for i in range(lo, hi):
                    if rate[e, i] > 0.0:
                        acc += rate[e, i]
                        ev = i
                        if acc > u:
                            break
                break
            acc += bs[e, b]
        if ev < 0:
            for i in range(ne - 1, -1, -1):
                if rate[e, i] > 0.0:
                    ev = i
                    break
        if n >= kmax:
            return W, n, True
        evbuf[n] = ev
        n += 1
        rq_apply(e, ev, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl, gam, bl, gg,
                 stamp, tick, cbuf, cstamp)


@nb.njit(cache=False)
def rq_copy(src, dst, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl):
    sig[dst, :] = sig[src, :]; C[dst, :] = C[src, :]; flp[dst, :] = flp[src, :]; Q[dst, :] = Q[src, :]
    nflp[dst] = nflp[src]; sq2[dst] = sq2[src]; rate[dst, :] = rate[src, :]; bs[dst, :] = bs[src, :]; Fh[dst] = Fh[src]


@nb.njit(cache=False)
def rq_run(nmoves, dur, meas_every, wlo, whi, segE, segN, segW, pos, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols,
           inc6, tail, head, exptab, tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp, out, stats, prof):
    """Bounce reptation. pos = [start, Mseg, direction]. Ends: 0 = tail (left), 1 = head (right); slots 2, 3 back up the ends.
    Every meas_every moves record (link events, plaquette events) over path segments [wlo, whi), E_L at both ends."""
    Mcap, kmax = segE.shape
    Np = C.shape[1]
    evbuf = np.zeros(kmax, dtype=np.int32)
    start = pos[0]; Mseg = pos[1]; d = pos[2]
    nout = 0
    for mv in range(nmoves):
        lead = 1 if d > 0 else 0
        rq_copy(lead, lead + 2, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl)
        W, n, over = rq_grow(lead, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp)
        if d > 0:
            old = start % Mcap
        else:
            old = (start + Mseg - 1) % Mcap
        ok = (not over) and (np.random.random() < np.exp(min(0.0, W - segW[old])))
        if ok:
            if d > 0:
                # remove the tail segment: replay its events in path order on the tail state
                for i in range(segN[old]):
                    rq_apply(0, segE[old, i], sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, stamp, tick, cbuf, cstamp)
                slot = old                                   # the freed slot becomes the new head segment
                for i in range(n):
                    segE[slot, i] = evbuf[i]
                segN[slot] = n; segW[slot] = W
                start = (start + 1) % Mcap
            else:
                # remove the head segment: undo its events in reverse path order on the head state
                for i in range(segN[old] - 1, -1, -1):
                    rq_apply(1, segE[old, i], sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, stamp, tick, cbuf, cstamp)
                slot = old                                   # the freed slot becomes the new tail segment (path order = reversed growth)
                for i in range(n):
                    segE[slot, i] = evbuf[n - 1 - i]
                segN[slot] = n; segW[slot] = W
                start = (start - 1) % Mcap
            stats[0] += 1
        else:
            rq_copy(lead + 2, lead, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl)
            d = -d
            stats[1] += 1
            if over:
                stats[2] += 1
        if (mv + 1) % meas_every == 0 and nout < out.shape[0]:
            nl_ev = 0; np_ev = 0
            for i in range(wlo, whi):
                sl = (start + i) % Mcap
                for k in range(segN[sl]):
                    if segE[sl, k] >= Np:
                        nl_ev += 1
                    else:
                        np_ev += 1
            el0 = Mq * sq2[0] - Fh[0]; el1 = Mq * sq2[1] - Fh[1]
            for b in range(bs.shape[1]):
                el0 -= bs[0, b]; el1 -= bs[1, b]
            out[nout, 0] = nl_ev; out[nout, 1] = np_ev; out[nout, 2] = el0; out[nout, 3] = el1
            nout += 1
            for i in range(Mseg if prof.shape[0] == Mseg else 0):
                sl = (start + i) % Mcap
                c_l = 0
                for k in range(segN[sl]):
                    if segE[sl, k] >= Np:
                        c_l += 1
                prof[i] += c_l
    pos[0] = start; pos[2] = d
    return nout


@nb.njit(cache=False)
def rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab,
             tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp):
    """Grow the initial path at the head from the common start state; returns the number of overflowing segments."""
    kmax = segE.shape[1]
    evbuf = np.zeros(kmax, dtype=np.int32)
    bad = 0
    for i in range(Mseg):
        W, n, over = rq_grow(1, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp)
        if over:
            bad += 1
        for k in range(n):
            segE[i, k] = evbuf[k]
        segN[i] = n; segW[i] = W
    return bad


def reptation(ice, T, start_sig, t, gam, Mq, Mseg, dur, nmoves, therm_moves, meas_every, window, seed, kmax=512, chunk=20000, alpha=0.2, hfield=None, bguide=None, profile=True):
    """One reptation chain. Returns per-measurement arrays: link and plaquette events in the middle window, E_L at both ends,
    and move statistics. window = number of middle segments counted."""
    nb_seed(seed)
    nl, npl, nv = ice.nl, ice.np_, ice.nv
    ne = npl + nl
    nblk = (ne + 63) // 64
    sig = np.array([start_sig] * 4, dtype=np.int64)
    C = np.zeros((4, npl), dtype=np.int64); flp = np.zeros((4, npl), dtype=np.bool_); Q = np.zeros((4, nv), dtype=np.int64)
    nflp = np.zeros(4, dtype=np.int64); sq2 = np.zeros(4, dtype=np.int64); Fh = np.zeros(4); rate = np.zeros((4, ne)); bs = np.zeros((4, nblk))
    dynf = np.ones(npl, dtype=np.bool_); tl = np.full(nl, t)
    hl = np.zeros(nl) if hfield is None else np.asarray(hfield, dtype=float)
    blg = np.zeros(nl) if bguide is None else np.asarray(bguide, dtype=float)
    exptab = np.exp(alpha * (np.arange(33) - 16.0))
    q_init(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head, exptab, tl, gam, hl, blg, 1.0)
    for e in range(4):
        rq_resum(e, rate, bs)
    stamp = np.zeros(ne, dtype=np.int64); cstamp = np.zeros(npl, dtype=np.int64); tick = np.zeros(1, dtype=np.int64); cbuf = np.zeros(64, dtype=np.int64)
    segE = np.zeros((Mseg, kmax), dtype=np.int32); segN = np.zeros(Mseg, dtype=np.int32); segW = np.zeros(Mseg)
    bad = rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6,
                   T.tail, T.head, exptab, tl, gam, blg, 1.0, Mq, stamp, tick, cbuf, cstamp)
    pos = np.array([0, Mseg, 1], dtype=np.int64)
    wlo = (Mseg - window) // 2; whi = wlo + window
    stats = np.zeros(3, dtype=np.int64)
    prof = np.zeros(Mseg if profile else 1)
    rows = []
    done = 0
    total = therm_moves + nmoves
    while done < total:
        nm = min(chunk, total - done)
        out = np.zeros((nm // meas_every + 1, 4))
        k = rq_run(nm, dur, meas_every, wlo, whi, segE, segN, segW, pos, sig, C, flp, Q, nflp, sq2, rate, bs, Fh, hl, T.plaq, T.sign, T.A, T.M, dynf,
                   T.pol4, T.pols, T.inc6, T.tail, T.head, exptab, tl, gam, blg, 1.0, Mq, stamp, tick, cbuf, cstamp, out, stats, prof)
        for e in range(2):
            rq_resum(e, rate, bs)
            Fh[e] = float(hl @ sig[e])
        if done >= therm_moves:
            rows.append(out[:k])
        else:
            prof[:] = 0.0
        done += nm
    return (np.concatenate(rows) if rows else np.zeros((0, 4))), stats, bad, prof



# ------------------------------------------------------------------------------------------------ main
DTAU, H1, BETA, DUR = 0.015, 0.15, 0.5, 0.025


def run_Ed(pr, init, nw, ngen, rng, hvec, h, hg=None, beta=0.5):
    """Projected energy in the probe field h hvec with the guide field beta hg hvec (hg = h: a field's own guide)."""
    hg = h if hg is None else hg
    out, res = energy_run(pr, init, nw, ngen, DTAU, ngen // 4, rng, h * hvec, beta * hg * hvec, Lcs=(0,))
    return out[0]


def pattern(ice):
    """Cyclic-triple field pattern: a-links modulated as cos(k x_b), b = (a + 1) mod 3, k = 2 pi / L."""
    return triple(ice, 2 * np.pi / ice.L)[0]


def energies(ice, T, hv, h, nch, nmoves, Mseg, dur, seed0, canon_start, guide=None, therm=None):
    """Reptation mixed energies at the path ends; guide = guide field amplitude (default the common 0.5 H1).
    Returns per-path means, block errors and the mean acceptance."""
    g = BETA * H1 if guide is None else guide
    ms, bes, accs = [], [], []
    for c in range(nch):
        rr = np.random.default_rng(seed0 + 17 * c)
        start = ice.sector_state(0) if canon_start else loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // ice.L), therm=60, r=rr,
                                                                   start=ice.sector_state(0), fix_winding=True)[-1]
        out, st, bad, prof = reptation(ice, T, start, 0.0, 1.0, 2.0, Mseg, dur, nmoves, nmoves // 5 if therm is None else therm, 100, Mseg // 4,
                                       seed0 + 17 * c + 1, hfield=h * hv, bguide=g * hv, profile=False)
        assert st[2] == 0 and bad == 0
        el = 0.5 * (out[:, 2] + out[:, 3])
        ms.append(el.mean())
        bes.append(np.array([x.mean() for x in np.array_split(el, 20)]).std(ddof=1) / np.sqrt(20))
        accs.append(st[0] / (st[0] + st[1]))
    return np.array(ms), np.array(bes), float(np.mean(accs))


def curvature(res, N):
    (E0, s0), (E1, s1), (E2, s2) = res
    a = (15 * E0 - 16 * E1 + E2) / (12 * H1 ** 2)
    sa = np.sqrt(225 * s0 ** 2 + 256 * s1 ** 2 + s2 ** 2) / (12 * H1 ** 2)
    return 4 * a / (3 * N), 4 * sa / (3 * N)


# ---------------------------------------------------------------- 1. rate tables against brute force on 4^3 with charges
ice4 = Ice(4); T4 = QTables(ice4)
rng = np.random.default_rng(5)
t_, g_ = 0.3, 1.2


def logpsi(ice, s):
    C = (s[ice.plaq] * ice.sign).sum(axis=1)
    div = np.zeros(ice.nv, dtype=np.int64)
    for v in range(ice.nv):
        for (l, sg) in ice.inc[v]:
            div[v] += sg * s[l]
    Q = div // 2
    return ALPHA * np.sum(np.abs(C) == 4) - g_ * np.sum(Q * Q), Q


def brute_rates(ice, s):
    lp, Q = logpsi(ice, s)
    r = np.zeros(ice.np_ + ice.nl)
    C = (s[ice.plaq] * ice.sign).sum(axis=1)
    for p in range(ice.np_):
        if abs(C[p]) == 4:
            s2 = s.copy(); s2[ice.plaq[p]] *= -1
            r[p] = np.exp(logpsi(ice, s2)[0] - lp)
    for l in range(ice.nl):
        s2 = s.copy(); s2[l] *= -1
        r[ice.np_ + l] = t_ * np.exp(logpsi(ice, s2)[0] - lp)
    return r, int(np.sum(Q * Q))


def fresh(ice, T, s):
    nl, npl, nv = ice.nl, ice.np_, ice.nv
    arr = dict(sig=np.array([s] * 4, dtype=np.int64), C=np.zeros((4, npl), dtype=np.int64), flp=np.zeros((4, npl), dtype=np.bool_),
               Q=np.zeros((4, nv), dtype=np.int64), nflp=np.zeros(4, dtype=np.int64), sq2=np.zeros(4, dtype=np.int64), Fh=np.zeros(4),
               rate=np.zeros((4, npl + nl)), bs=np.zeros((4, (npl + nl + 63) // 64)))
    z = np.zeros(nl)
    q_init(arr["sig"], arr["C"], arr["flp"], arr["Q"], arr["nflp"], arr["sq2"], arr["Fh"], arr["rate"], T.plaq, T.sign, T.A, T.M,
           np.ones(npl, dtype=np.bool_), T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head, np.exp(ALPHA * (np.arange(33) - 16.0)),
           np.full(nl, t_), g_, z, z, 1.0)
    for e in range(4):
        rq_resum(e, arr["rate"], arr["bs"])
    return arr


s0 = ice4.sector_state(0).astype(np.int64).copy()
for l in rng.choice(ice4.nl, size=ice4.nl // 10, replace=False):
    s0[l] *= -1
A_ = fresh(ice4, T4, s0)
rb0, q0 = brute_rates(ice4, s0)
d0 = float(np.abs(A_["rate"][0] - rb0).max())
stamp = np.zeros(ice4.np_ + ice4.nl, dtype=np.int64); cstamp = np.zeros(ice4.np_, dtype=np.int64)
tick = np.zeros(1, dtype=np.int64); cbuf = np.zeros(64, dtype=np.int64); hl0 = np.zeros(ice4.nl)
exptab = np.exp(ALPHA * (np.arange(33) - 16.0))
for it in range(3000):
    ev = rng.choice(ice4.np_ + ice4.nl, p=A_["rate"][0] / A_["rate"][0].sum())
    rq_apply(0, ev, A_["sig"], A_["C"], A_["flp"], A_["Q"], A_["nflp"], A_["sq2"], A_["rate"], A_["bs"], A_["Fh"], hl0, T4.plaq, T4.sign,
             T4.A, T4.M, np.ones(ice4.np_, dtype=np.bool_), T4.pol4, T4.pols, T4.inc6, T4.tail, T4.head, exptab, np.full(ice4.nl, t_), g_,
             np.zeros(ice4.nl), 1.0, stamp, tick, cbuf, cstamp)
s1 = A_["sig"][0].copy()
rb1, q1 = brute_rates(ice4, s1)
d1 = float(np.abs(A_["rate"][0] - rb1).max())
EL_inc = 2.0 * A_["sq2"][0] - A_["bs"][0].sum()
EL_bf = 2.0 * q1 - rb1.sum()
ok1 = d0 < 1e-10 and d1 < 1e-10 and A_["sq2"][0] == q1 and abs(EL_inc - EL_bf) < 1e-8
check("rate tables and local energy on 4^3 with charges (hopping 0.3, charge penalty 1.2): fresh tables and 3000 incremental "
      "events agree with brute-force wave-function ratios", ok1,
      f"max rate difference {max(d0, d1):.1e}; local energy {EL_inc:.6f} vs {EL_bf:.6f}; {int(np.sum(logpsi(ice4, s1)[1] != 0))} charges")

# ---------------------------------------------------------------- 2. exact 2^3 control
ice2 = Ice(2); T2 = QTables(ice2)
hv2 = pattern(ice2)
codes, order, H2, sig_of = exact_L2(ice2, ice2.sector_state(0))
F2 = np.array([sig_of(c) for c in order]).astype(float) @ hv2
NC2, NM2 = (6, 300000) if DRY else (24, 2000000)
res2, rows2, ok2 = [], [], True
for j, h in enumerate((0.0, H1, 2 * H1)):
    Ex = float(eigsh((H2 - h * diags(F2)).tocsr(), k=1, which="SA")[0][0])
    ms, _, acc = energies(ice2, T2, hv2, h, NC2, NM2, 400, 0.05, 1000 + 100 * j, True)
    m, e = float(ms.mean()), float(ms.std(ddof=1) / np.sqrt(NC2))
    res2.append((m, e)); z = (m - Ex) / e
    ok2 &= abs(z) <= 3
    rows2.append(f"h = {h}: {m:.4f}+-{e:.4f} vs exact {Ex:.6f} ({z:+.1f} sigma)")
Ee = [float(eigsh((H2 - h * diags(F2)).tocsr(), k=1, which="SA")[0][0]) for h in (0.0, H1, 2 * H1)]
chi2, chi2e = curvature(res2, ice2.nv)
chi2x = 4 * (15 * Ee[0] - 16 * Ee[1] + Ee[2]) / (12 * H1 ** 2) / (3 * ice2.nv)
ok2 &= abs(chi2 - chi2x) <= 3 * chi2e
check("exact 2^3 control: reptation mixed energies (path 20) in the probe field at k = pi agree with exact diagonalization of the "
      "canonical flip component, and so does the three-point curvature", ok2,
      "; ".join(rows2) + f"; curvature {chi2:.3f}+-{chi2e:.3f} vs exact three-point {chi2x:.4f}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 3. 8^3 reptation, one guide for the three fields
L8 = 4 if DRY else 8
ice = Ice(L8); T = QTables(ice)
hv = pattern(ice)
MSEG, NM, TH = (400, 200000, 100000) if DRY else (1600, 10000000, 5000000)
res, rows3 = {}, []
for j, h in enumerate((0.0, H1, 2 * H1)):
    ms, bes, acc = energies(ice, T, hv, h, 1, NM, MSEG, DUR, 3000 + 100 * j, False, therm=TH)
    res[h] = (float(ms[0]), float(bes[0]))
    rows3.append(f"E({h}) {res[h][0]:.3f}+-{res[h][1]:.3f} (acceptance {acc:.2f})")
chi_c, chi_ce = curvature([res[0.0], res[H1], res[2 * H1]], ice.nv)
u_r = -res[0.0][0] / ice.np_
check(f"{L8}^3 at k = 2 pi/{L8}, reptation path {MSEG * DUR:g}, one guide field (0.5 H1) for the three fields: the curvature estimate "
      "(reported)", bool(np.isfinite(chi_c) and chi_c > 0 and chi_ce / chi_c < 0.05),
      "; ".join(rows3) + f"; chi {chi_c:.4f}+-{chi_ce:.4f}; u {u_r:.5f}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. 8^3 reptation, a guide per field
rpf = {H1: res[H1]}
rows4 = []
for j, h in ((0, 0.0), (2, 2 * H1)):
    ms, bes, acc = energies(ice, T, hv, h, 1, NM, MSEG, DUR, 4000 + 100 * j, False, guide=BETA * h, therm=TH)
    rpf[h] = (float(ms[0]), float(bes[0]))
    rows4.append(f"E({h}) with guide {BETA * h:g}: {rpf[h][0]:.3f}+-{rpf[h][1]:.3f}")
chi_p, chi_pe = curvature([rpf[0.0], rpf[H1], rpf[2 * H1]], ice.nv)
z_chi = (chi_p - chi_c) / np.hypot(chi_pe, chi_ce)
z_e0 = (rpf[0.0][0] - res[0.0][0]) / np.hypot(rpf[0.0][1], res[0.0][1])
z_e2 = (rpf[2 * H1][0] - res[2 * H1][0]) / np.hypot(rpf[2 * H1][1], res[2 * H1][1])
check(f"{L8}^3 reptation with a guide field per probe field (0.5 h; E(H1) shared): the zero-field and 2 H1 energies and the curvature "
      "lie within three combined errors of the one-guide values (the scheme difference is reported)", abs(z_chi) <= 3 and abs(z_e0) <= 3 and abs(z_e2) <= 3,
      "; ".join(rows4) + f" ({z_e0:+.1f} and {z_e2:+.1f} sigma from the one-guide energies); chi {chi_p:.4f}+-{chi_pe:.4f}, scheme difference "
      f"{chi_p - chi_c:+.4f} ({z_chi:+.1f} sigma); {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. 8^3 projector in both schemes
NW, NGEN = (96, 200) if DRY else (960, 2000)
rows5, ok5 = [], True
for scheme, hgsel in (("one guide", "common"), ("a guide per field", "own")):
    chis, us = [], []
    for sd in (401, 402):
        rr = np.random.default_rng(sd * 100 + L8 + NW)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L8), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), sd * 1000 + L8 + NW)
        Es = [run_Ed(pr, init, NW, NGEN, rr, hv, h, hg=(H1 if hgsel == "common" else None)) for h in (0.0, H1, 2 * H1)]
        us.append(-Es[0][0] / ice.np_)
        chis.append(chi_fit(*Es[0], *Es[1], *Es[2], H1, ice.nv, 1.0))
    cs = np.array([x[0] for x in chis]); be = np.array([x[1] for x in chis])
    c, ce = float(cs.mean()), float(max(np.std(cs, ddof=1) / np.sqrt(2), be.mean() / np.sqrt(2)))
    z = (c - chi_c) / np.hypot(ce, chi_ce)
    ok5 &= abs(z) <= 3
    rows5.append(f"{scheme}: chi {c:.4f}+-{ce:.4f} (seeds {cs[0]:.4f}, {cs[1]:.4f}; {z:+.1f} sigma from reptation), u {np.mean(us):.5f}")
check(f"{L8}^3 projector with {NW} walkers, projection 30, resampling interval 0.015, seeds 401 and 402, in both guide schemes: each "
      "curvature estimate lies within three combined errors of the reptation value", ok5,
      "; ".join(rows5) + f"; reptation u {u_r:.5f}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 6. 12^3 projector in both schemes (the split's size trend)
L12 = 6 if DRY else 12
ice12 = Ice(L12)
hv12 = pattern(ice12)
rows6, split = [], []
for scheme, hgsel in (("one guide", "common"), ("a guide per field", "own")):
    chis = []
    for sd in (401, 402):
        rr = np.random.default_rng(sd * 100 + L12 + NW)
        init = loop_vmc(ice12, ALPHA, sweeps=max(40, 1600 // L12), therm=60, r=rr, start=ice12.sector_state(0), fix_winding=True)
        pr = Projector(ice12, np.ones(ice12.np_, bool), ALPHA, 0.0, np.zeros((1, ice12.nl), complex), sd * 1000 + L12 + NW)
        Es = [run_Ed(pr, init, NW, NGEN, rr, hv12, h, hg=(H1 if hgsel == "common" else None)) for h in (0.0, H1, 2 * H1)]
        chis.append(chi_fit(*Es[0], *Es[1], *Es[2], H1, ice12.nv, 1.0))
    cs = np.array([x[0] for x in chis]); be = np.array([x[1] for x in chis])
    c, ce = float(cs.mean()), float(max(np.std(cs, ddof=1) / np.sqrt(2), be.mean() / np.sqrt(2)))
    split.append((c, ce))
    rows6.append(f"{scheme}: chi {c:.4f}+-{ce:.4f} (seeds {cs[0]:.4f}, {cs[1]:.4f})")
d12, d12e = split[1][0] - split[0][0], float(np.hypot(split[0][1], split[1][1]))
check(f"{L12}^3 projector at k = 2 pi/{L12}, same population and settings, both guide schemes: the scheme difference (reported beside "
      "8^3 above and 16^3 in open PR 9328)", bool(all(np.isfinite(x[0]) and x[0] > 0 for x in split)),
      "; ".join(rows6) + f"; scheme difference {d12:+.4f}+-{d12e:.4f} ({d12 / d12e:+.1f} sigma); {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
