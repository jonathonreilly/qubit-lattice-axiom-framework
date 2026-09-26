#!/usr/bin/env python3
"""Static test charges at the pure-ring point: the separation energy of a charge pair on the tori, against the lattice
Coulomb law whose strength the transverse susceptibility sets.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on L^3 tori with the vertex Gauss law exact except at
two test charges (a vertex with four arrows out and two in, and one with two out and four in; divergence +-2), and the clause
-g (U + U^dag) + V N_flip, g = 1 (landed). Supplied model, finite estimates, no physical reading.

Plaquette flips conserve every vertex divergence, so the charges are static and each separation d has its own flip component;
at the RK point the uniform superposition over any component is a zero-energy ground state, so the energy there does not
depend on d. At the pure-ring point the compiled projector of open PR 9236 gives the ground energy E(d) of a pair at separation
d along an axis. In the Gaussian comparator of the landed note on it, a static pair of divergence +-2Q costs 4 Q^2 U [G(0) - G(d)]
with G the torus lattice Green function and U = 1/chi, the inverse of the transverse susceptibility measured in open PR 9236.
Checks: (1) exact 2^3 control with a pair; (2) E(d) - E(1) on 8^3 against the Coulomb shape and a linear string tension;
(3) E(L/2) - E(1) on 4^3, 6^3, 8^3, 12^3; (4) charge 2 and V/g = 0.5. Prints TOTAL: PASS=N FAIL=M.
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

AUDIT_INPUT_PATHS = ['docs/RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25.md']
AUDIT_TIMEOUT_SEC = 4800

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


def div_matrix(ice):
    B = np.zeros((ice.nv, ice.nl))
    for l in range(ice.nl):
        B[ice.tail[l], l] += 1
        B[ice.head[l], l] -= 1
    return B


def directed_path(ice, s, A, B):
    """Shortest path from vertex A to vertex B along links whose arrows point forward (BFS on the arrow graph)."""
    from collections import deque
    prev = {A: None}
    q = deque([A])
    while q:
        v = q.popleft()
        if v == B:
            break
        for (l, sg) in ice.inc[v]:
            if s[l] * sg == 1:
                w = ice.head[l] if ice.tail[l] == v else ice.tail[l]
                if w not in prev:
                    prev[w] = (v, l)
                    q.append(w)
    path, v = [], B
    while prev[v] is not None:
        v0, l = prev[v]
        path.append(l)
        v = v0
    return path[::-1]


def charged(ice, d, Q=1):
    """Q directed strings from A = (0,0,0) to B = (d,0,0) reversed in the canonical zero-winding state: charges -Q at A, +Q at B."""
    s = ice.sector_state(0).copy()
    A, B = ice.vid[(0, 0, 0)], ice.vid[(d % ice.L, 0, 0)]
    for _ in range(Q):
        s[directed_path(ice, s, A, B)] *= -1
    return s


def green(L):
    ks = 2 * np.pi * np.arange(L) / L
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij")
    lam = (2 - 2 * np.cos(KX)) + (2 - 2 * np.cos(KY)) + (2 - 2 * np.cos(KZ))
    lam[0, 0, 0] = np.inf
    return np.real(np.fft.ifftn(1 / lam))


def pair_energy(L, d, Q, V, seeds, nw):
    ice = Ice(L)
    s0 = charged(ice, d, Q)
    vals, errs = [], []
    for sd in seeds:
        pr = Projector(ice, np.ones(ice.np_, bool), 0.2 * (1 - V), V, np.zeros((1, ice.nl), complex), sd)
        out, _ = energy_run(pr, [s0], nw, NGEN, DTAU, NGEN // 3, np.random.default_rng(sd + 7), np.zeros(ice.nl), np.zeros(ice.nl), Lcs=(0,))
        vals.append(out[0][0]); errs.append(out[0][1])
    vals, errs = np.array(vals), np.array(errs)
    n = len(vals)
    err = max(np.std(vals, ddof=1) / np.sqrt(n) if n > 1 else 0.0, errs.mean() / np.sqrt(n))
    return float(vals.mean()), float(err)


# ------------------------------------------------------------------------------------------------ main
DTAU = 0.05
NW, NGEN = (96, 240) if DRY else (1920, 1000)
SEEDS = (11, 12) if DRY else (11, 12, 13, 14)

# ---------------------------------------------------------------- 1. exact 2^3 control with a charge pair
ice2 = Ice(2)
B2 = div_matrix(ice2)
s2c = charged(ice2, 1, 1)
target = B2 @ s2c
bits = np.arange(ice2.nl)
codes = []
for start in range(0, 1 << ice2.nl, 1 << 18):
    ids = np.arange(start, min(1 << ice2.nl, start + (1 << 18)), dtype=np.int64)
    sig = (((ids[:, None] >> bits) & 1) * 2 - 1)
    ok = np.all(sig @ B2.T == target, axis=1)
    codes.append(ids[ok])
codes = np.concatenate(codes)
masks = [sum(1 << int(l) for l in links) for links in ice2.plaq]
def sig_of(c):
    return ((c >> bits) & 1) * 2 - 1
def flips(s):
    return np.flatnonzero(np.abs((s[ice2.plaq] * ice2.sign).sum(axis=1)) == 4)
c0 = int(((s2c + 1) // 2 * (1 << bits)).sum())
comp, order, q = {c0: 0}, [c0], 0
while q < len(order):
    c = order[q]; q += 1
    for p in flips(sig_of(c)):
        c2 = c ^ masks[p]
        if c2 not in comp:
            comp[c2] = len(order); order.append(c2)
div_ok = all(np.array_equal(B2 @ sig_of(c), target) for c in order)
rows, cols, nfl = [], [], np.zeros(len(order))
for i, c in enumerate(order):
    fp = flips(sig_of(c)); nfl[i] = len(fp)
    for p in fp:
        rows.append(comp[c ^ masks[p]]); cols.append(i)
Hc = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(len(order), len(order))).tocsr()
E0c = float(eigsh(Hc, k=1, which="SA")[0][0]) if len(order) > 2 else float(np.linalg.eigvalsh(Hc.toarray())[0])
Hrk = Hc + diags(nfl)
Erk = float(np.linalg.eigvalsh(Hrk.toarray())[0]) if len(order) < 3000 else float(eigsh(Hrk, k=1, which="SA")[0][0])
prq = Projector(ice2, np.ones(ice2.np_, bool), 0.2, 0.0, np.zeros((1, ice2.nl), complex), 21)
outq, _ = energy_run(prq, [s2c], 400, 1600 if not DRY else 400, DTAU, 400 if not DRY else 100, np.random.default_rng(22), np.zeros(ice2.nl), np.zeros(ice2.nl), Lcs=(0,))
prr = Projector(ice2, np.ones(ice2.np_, bool), 0.0, 1.0, np.zeros((1, ice2.nl), complex), 23)
outr, resr = energy_run(prr, [s2c], 100, 200, DTAU, 50, np.random.default_rng(24), np.zeros(ice2.nl), np.zeros(ice2.nl), Lcs=(0,))
check("exact 2^3 control with a charge pair: plaquette flips conserve every vertex charge, the RK clause has zero ground energy on the charged "
      "component and the projector's energy vanishes on every block there, and the projector reproduces the pure-ring ground energy",
      div_ok and abs(Erk) < 1e-9 and np.abs(resr["e"]).max() < 1e-12 and abs(outq[0][0] - E0c) <= 3 * outq[0][1],
      f"{len(codes)} configurations with charges -1 at (0,0,0) and +1 at (1,0,0); flip component {len(order)} states, all with the same charges: {div_ok}; "
      f"RK ground energy {Erk:.1e}, projector max |E| {np.abs(resr['e']).max():.1e}; pure ring: exact {E0c:.5f}, projector {outq[0][0]:.4f}+-{outq[0][1]:.4f}")

# ---------------------------------------------------------------- 2. the pair energy against separation on 8^3
L8 = 4 if DRY else 8
G8 = green(L8)
E8 = {d: pair_energy(L8, d, 1, 0.0, SEEDS, NW) for d in range(1, L8 // 2 + 1)}
ds = np.array(sorted(E8)); y = np.array([E8[d][0] - E8[1][0] for d in ds]); ye = np.array([np.hypot(E8[d][1], E8[1][1]) for d in ds])
xc = np.array([4 * (G8[1, 0, 0] - G8[d, 0, 0]) for d in ds])
m = ds > 1
U_c = float((xc[m] * y[m] / ye[m] ** 2).sum() / (xc[m] ** 2 / ye[m] ** 2).sum()); U_ce = float(1 / np.sqrt((xc[m] ** 2 / ye[m] ** 2).sum()))
chi_c = float((((y[m] - U_c * xc[m]) / ye[m]) ** 2).sum())
xl = (ds - 1).astype(float)
sig_l = float((xl[m] * y[m] / ye[m] ** 2).sum() / (xl[m] ** 2 / ye[m] ** 2).sum())
chi_l = float((((y[m] - sig_l * xl[m]) / ye[m]) ** 2).sum())
check(f"the pair energy against separation on {L8}^3 at the pure-ring point (charge 1): the lattice Coulomb law 4U[G(1) - G(d)] of the torus against a "
      "linear string tension (reported)", True,
      "; ".join(f"d={d}: E(d)-E(1) {yy:+.3f}+-{ee:.3f}, Coulomb shape {xx:.4f}" for d, yy, ee, xx in zip(ds, y, ye, xc))
      + f"; Coulomb fit U = {U_c:.3f}+-{U_ce:.3f} (chi^2 {chi_c:.2f}); linear fit sigma = {sig_l:.3f} per link (chi^2 {chi_l:.2f}); 1/chi of open PR 9236 on 8^3: "
        f"{1 / 1.182:.3f}-{1 / 1.064:.3f}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3. the separation energy against the size of the torus
SIZES = (4,) if DRY else (4, 6, 8, 12)
sep = {}
for L in SIZES:
    if L == L8:
        sep[L] = (E8[L // 2][0] - E8[1][0], np.hypot(E8[L // 2][1], E8[1][1]))
        continue
    seeds = SEEDS if L < 12 else SEEDS[:2]
    a = pair_energy(L, 1, 1, 0.0, seeds, NW); b = pair_energy(L, L // 2, 1, 0.0, seeds, NW)
    sep[L] = (b[0] - a[0], np.hypot(a[1], b[1]))
rows_s = []
for L in SIZES:
    GL = green(L)
    pred = 4 * U_c * (GL[1, 0, 0] - GL[L // 2, 0, 0])
    rows_s.append(f"{L}^3: E(L/2)-E(1) {sep[L][0]:+.3f}+-{sep[L][1]:.3f} (Coulomb with the 8^3 U: {pred:.3f}; a string tension sigma would add sigma (L/2 - 1))")
Ls = np.array(SIZES, dtype=float); ys = np.array([sep[L][0] for L in SIZES]); yse = np.array([sep[L][1] for L in SIZES])
pc = np.polyfit(Ls / 2 - 1, ys, 1, w=1 / yse) if len(SIZES) > 1 else (0.0, 0.0)
check("the separation energy against the size of the torus: E(L/2) - E(1) for L = 4, 6, 8, 12 (reported); a Coulomb phase keeps it bounded, a "
      "confining string makes it grow linearly with L/2", True, "; ".join(rows_s) + f"; slope in (L/2 - 1) {pc[0]:+.3f} per link; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. charge 2, and the RK potential halfway
E2_1 = pair_energy(L8, 1, 2, 0.0, SEEDS[:3], NW); E2_4 = pair_energy(L8, L8 // 2, 2, 0.0, SEEDS[:3], NW)
d2 = (E2_4[0] - E2_1[0], np.hypot(E2_4[1], E2_1[1]))
d1 = (E8[L8 // 2][0] - E8[1][0], np.hypot(E8[L8 // 2][1], E8[1][1]))
H_1 = pair_energy(L8, 1, 1, 0.5, SEEDS[:3], NW); H_4 = pair_energy(L8, L8 // 2, 1, 0.5, SEEDS[:3], NW)
dh = (H_4[0] - H_1[0], np.hypot(H_4[1], H_1[1]))
r2 = d2[0] / d1[0]; r2e = abs(r2) * np.hypot(d2[1] / d2[0], d1[1] / d1[0])
rh = dh[0] / d1[0]; rhe = abs(rh) * np.hypot(dh[1] / dh[0], d1[1] / d1[0])
check("charge 2 and the RK potential halfway (reported): the separation energy of a charge-2 pair against 4 times the charge-1 value (linear response), "
      "and of a charge-1 pair at V/g = 0.5 against the ratio chi(V = 0)/chi(V = 0.5) of open PR 9239", True,
      f"{L8}^3, E({L8 // 2}) - E(1): charge 1 {d1[0]:+.3f}+-{d1[1]:.3f}; charge 2 {d2[0]:+.3f}+-{d2[1]:.3f}, ratio {r2:.2f}+-{r2e:.2f} (linear response 4); "
      f"charge 1 at V/g = 0.5 {dh[0]:+.3f}+-{dh[1]:.3f}, ratio to V = 0 {rh:.2f}+-{rhe:.2f} (1/chi ratio 1.077/2.220 = {1.077 / 2.220:.2f}); {time.time() - T0:.0f} s")

print(f"elapsed_sec: {time.time() - T0:.0f}")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
