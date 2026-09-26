#!/usr/bin/env python3
"""Round-four synthesis: the pure-ring photon from energies alone. One exact identity recomputed per block.

Supplied model, exact identities on small components, no physical reading; nothing adopted. The blocks synthesised (open PRs):
9236 (energy-only bounds on the photon from the mode-averaged transverse susceptibility), 9239 (the bounds along the RK potential),
9244 (static test charges), 9247 (the bounds in a region bounded by records). Each check recomputes one exact identity the block
rests on, with its own code; the last prints the register. Prints TOTAL: PASS=N FAIL=M.
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

AUDIT_INPUT_PATHS = ['docs/ROUND_FOUR_SYNTHESIS_THE_PURE_RING_PHOTON_FROM_ENERGIES_ALONE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_IN_A_REGION_BOUNDED_BY_RECORDS_THE_ENERGY_ONLY_PHOTON_BOUND_MATCHES_THE_TORUS_AND_THE_RECORDS_REDUCE_ONLY_THE_RESPONSE_AMPLITUDE_BOUNDED_THEOREM_NOTE_2026-09-25.md']
AUDIT_TIMEOUT_SEC = 600

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
def nb_init_rates(sig, flp, dN, rate, Fh, plaq, exptab, hl, bl, gp):
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
                rate[i, s] = gp[s] * exptab[dN[i, s] + 16] * np.exp(-2.0 * g)
            else:
                rate[i, s] = 0.0


@nb.njit(cache=False)
def nb_walk_f(sig, C, flp, dN, rate, nflp, Fh, Om, plaq, A, M, dynf, exptab, V, hl, bl, gp, dtau, PH, stamp, tick, sbuf, rbuf, logw, ELend):
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
                    rn = gp[s] * exptab[d_[s] + 16] * np.exp(-2.0 * g)
                else:
                    rn = 0.0
                r_[s] = rn
                bs[s // 64] += rn - rbuf[jj]
        logw[i] = lw


def energy_run(pr, init, n_w, n_gen, dtau, therm, rng, hl, bl, Lcs=(0, 20, 40, 80), gp=None):
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
    gp = np.ones(ice.np_) if gp is None else np.asarray(gp, dtype=np.float64)
    nb_init_rates(sig, flp, dN, rate, Fh, pr.plaq, pr.exptab, hl, bl, gp)
    Om = np.zeros((n_w, 1), dtype=np.complex128)
    PHz = np.zeros((ice.nl, 1), dtype=np.complex128)
    logw = np.zeros(n_w); ELend = np.zeros(n_w)
    es, lws = [], []
    for g in range(n_gen):
        nb_walk_f(sig, C, flp, dN, rate, nflp, Fh, Om, pr.plaq, pr.A, pr.M, pr.dyn, pr.exptab, pr.V, hl, bl, gp, dtau, PHz,
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
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    return np.array([np.exp(1j * k * xb) * (ice.axis == a) / np.sqrt(ice.nv) for a in range(3)])


def component(ice, start, dynmask=None):
    """Exact flip component of a configuration (bit codes), its configurations, and the transition list (from, to, plaquette)."""
    masks = [sum(1 << int(l) for l in links) for links in ice.plaq]              # Python integers: no overflow beyond 63 links
    dyn = np.arange(ice.np_) if dynmask is None else np.flatnonzero(dynmask)
    def sig_of(c):
        return np.array([1 if (c >> l) & 1 else -1 for l in range(ice.nl)])
    def flips(s):
        return dyn[np.abs((s[ice.plaq[dyn]] * ice.sign[dyn]).sum(axis=1)) == 4]
    c0 = sum(1 << int(l) for l in np.flatnonzero(start > 0))
    comp, order, q = {c0: 0}, [c0], 0
    while q < len(order):
        c = order[q]; q += 1
        for p in flips(sig_of(c)):
            c2 = c ^ masks[p]
            if c2 not in comp:
                comp[c2] = len(order); order.append(c2)
    S = np.array([sig_of(c) for c in order]).astype(float)
    tr = [(i, comp[c ^ masks[p]], p) for i, c in enumerate(order) for p in flips(S[i].astype(int))]
    return S, np.array(tr)


def hamiltonian(n, tr, V=0.0, nflip=None, coupling=None):
    g = np.ones(len(tr)) if coupling is None else coupling[tr[:, 2]]
    H = coo_matrix((-g, (tr[:, 1], tr[:, 0])), shape=(n, n)).tocsr()
    if V and nflip is not None:
        H = H + V * diags(nflip)
    return H


# ------------------------------------------------------------------------------------------------ main
# ---------------------------------------------------------------- 1. open PR 9236: the averaged f-sum and the moment chain on 2^3
ice2 = Ice(2)
S2, tr2 = component(ice2, ice2.sector_state(0))
n2 = len(S2)
H2 = hamiltonian(n2, tr2)
v, Vv = np.linalg.eigh(H2.toarray())
assert np.max(np.abs(H2 @ Vv - Vv * v)) < 1e-9
assert np.max(np.abs(Vv.T @ Vv - np.eye(n2))) < 1e-9
E0 = float(v[0]); psi = Vv[:, 0] * np.sign(Vv[:, 0].sum())
PH = triple(ice2, np.pi)
chis, Ss, fs, coup = [], [], [], np.zeros(len(v))
for a in range(3):
    O = np.real(S2 @ PH[a])
    rhs = O * psi; rhs -= psi * (psi @ rhs)
    response_matrix = (H2 - E0 * diags(np.ones(n2))).tocsr()
    x, info = minres(response_matrix, rhs, rtol=1e-12)
    assert info == 0 and np.linalg.norm(response_matrix @ x - rhs) < 1e-8
    x -= psi * (psi @ x)
    chis.append(2 * float(rhs @ x)); Ss.append(float(rhs @ rhs)); fs.append(float(rhs @ (H2 @ rhs)) - E0 * float(rhs @ rhs))
    coup += (Vv.T @ rhs) ** 2
chi, S, f = np.mean(chis), np.mean(Ss), np.mean(fs)
u = -E0 / ice2.np_
wmin = min(v[k] - E0 for k in range(1, len(v)) if coup[k] > 1e-12)
chain = [wmin, S / (chi / 2), np.sqrt(f / (chi / 2)), f / S]
check("open PR 9236: on the exact 2^3 component the cyclic-triple average of the f-sum equals 2 u s^2 and the moment chain orders the lowest coupled "
      "level below the energy-only bound", abs(f - 2 * u * 4) < 1e-9 and chain[0] <= chain[1] <= chain[2] <= chain[3] and S <= np.sqrt(chi * f / 2),
      f"{n2} states; f {f:.6f} = 2us^2 {2 * u * 4:.6f}; chain {' <= '.join(f'{c:.4f}' for c in chain)}; S {S:.5f} <= sqrt(chi f/2) {np.sqrt(chi * f / 2):.5f}")

# ---------------------------------------------------------------- 2. open PR 9239: Hellmann-Feynman in V
nfl2 = (np.abs((S2[:, ice2.plaq] * ice2.sign).sum(axis=2)) == 4).sum(axis=1).astype(float)
def E_V(V):
    return float(eigsh(hamiltonian(n2, tr2, V, nfl2), k=1, which="SA")[0][0])
V0, dV = 0.5, 1e-4
wv, Vv0 = eigsh(hamiltonian(n2, tr2, V0, nfl2), k=1, which="SA")
nf_exp = float((Vv0[:, 0] ** 2) @ nfl2)
dEdV = (E_V(V0 + dV) - E_V(V0 - dV)) / (2 * dV)
check("open PR 9239: on the exact 2^3 component dE_0/dV equals the ground-state flippable count at V/g = 0.5 (Hellmann-Feynman), and at V = g the "
      "ground energy is zero", abs(dEdV - nf_exp) < 1e-5 and abs(E_V(1.0)) < 1e-9,
      f"dE0/dV {dEdV:.6f}, <N_flip> {nf_exp:.6f}; E0(V = g) {E_V(1.0):.1e}")

# ---------------------------------------------------------------- 3. open PR 9244: static charges on 2^3
s_ch = ice2.sector_state(0).copy()
l0 = 3 * ice2.vid[(0, 0, 0)]
s_ch[l0] *= -1
Bd = np.zeros((ice2.nv, ice2.nl))
for l in range(ice2.nl):
    Bd[ice2.tail[l], l] += 1; Bd[ice2.head[l], l] -= 1
Sc, trc = component(ice2, s_ch)
divs = Sc @ Bd.T
nflc = (np.abs((Sc[:, ice2.plaq] * ice2.sign).sum(axis=2)) == 4).sum(axis=1).astype(float)
Erk = float(np.linalg.eigvalsh(hamiltonian(len(Sc), trc, 1.0, nflc).toarray())[0])
check("open PR 9244: on the exact 2^3 component of a charge pair every configuration carries the same charges, and the RK clause has zero ground energy",
      np.all(divs == divs[0]) and abs(Erk) < 1e-9,
      f"{len(Sc)} states, charges {sorted(set(int(x) for x in divs[0]))}, RK ground energy {Erk:.1e}")

# ---------------------------------------------------------------- 4. open PR 9247: Hellmann-Feynman first moment in a region bounded by records
ice5 = Ice(5)
frame5 = loop_vmc(ice5, 0.0, sweeps=60, therm=60, r=np.random.default_rng(11))[-1]
reg5 = Region(ice5, 3)
S5, tr5 = component(ice5, frame5, reg5.dyn)
n5 = len(S5)
H5 = hamiltonian(n5, tr5)
v5, V5 = eigsh(H5, k=1, which="SA"); E05 = float(v5[0]); psi5 = V5[:, 0] * np.sign(V5[:, 0].sum())
tail5 = np.array([ice5.verts[l // 3] for l in range(ice5.nl)])
xb5 = tail5[np.arange(ice5.nl), (ice5.axis + 1) % 3]
w5 = np.sin(np.pi * xb5 / 4) * (~reg5.rec)
cp5 = 4 * ((w5[ice5.plaq] * ice5.sign).sum(axis=1)) ** 2 * reg5.dyn
W5 = S5 @ w5
rhs5 = (W5 - psi5 ** 2 @ W5) * psi5; rhs5 -= psi5 * (psi5 @ rhs5)
m1_dc = float(rhs5 @ (H5 @ rhs5)) - E05 * float(rhs5 @ rhs5)
eps = 1e-4
Ep = float(eigsh(hamiltonian(n5, tr5, coupling=1 + eps * cp5), k=1, which="SA")[0][0])
Em = float(eigsh(hamiltonian(n5, tr5, coupling=1 - eps * cp5), k=1, which="SA")[0][0])
m1_hf = -(Ep - Em) / (4 * eps)
check("open PR 9247: on an exact region bounded by records the Hellmann-Feynman first moment -dE/d eps /2 equals the double commutator",
      abs(m1_hf - m1_dc) < 1e-5, f"{n5} states; double commutator {m1_dc:.6f}, Hellmann-Feynman {m1_hf:.6f}")

# ---------------------------------------------------------------- 5. the register
REGISTER = ["D-gauss (exact vertex Gauss law; with two static test charges in open PR 9244)", "D-roles", "D-ring (-g (U + U^dag))",
            "D-RK (the potential V n_p and its sweep, open PR 9239)", "D-records at a region's boundary (uniform-ice and canonical frames, open PR 9247)",
            "method: compiled local-update fixed-population projector", "method: probe fields on a cyclic mode triple or standing waves",
            "method: Hellmann-Feynman derivatives in V and in per-plaquette ring couplings", "comparison: the Gaussian lattice-Maxwell comparator (landed)"]
check("register of decision points, methods and comparisons touched by the four blocks (none adopted)", len(REGISTER) == 9, "; ".join(REGISTER))
print(f"elapsed_sec: {time.time() - T0:.0f}")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
