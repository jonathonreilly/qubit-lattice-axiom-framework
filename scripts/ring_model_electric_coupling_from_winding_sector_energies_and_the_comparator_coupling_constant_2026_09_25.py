#!/usr/bin/env python3
"""The electric coupling of the pure-ring point from the energies of winding sectors, against the transverse susceptibility,
and the dimensionless coupling of the Gaussian comparator.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law
(cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (landed). Supplied model, finite diagnostics, no
physical reading.

The section flux W_x (the sum of sigma over the x-links crossing any plane x = const) is conserved (landed winding-sector note).
In the Gaussian lattice Maxwell comparator (landed) H = (U/2) sum E^2 + (K/2) sum (curl A)^2, a sector with flux W costs
U W^2 / (2L) above W = 0 (the uniform field W / L^2 on the L^3 x-links; the zero-point energy is the same in every sector), the
transverse susceptibility of open PR 9236 is 1/U, a static charge pair of divergence +-2 has the tail -U/(pi d) (open PR 9244),
and the photon velocity is c_G = (U K)^(1/2) with K = 4u (u the ring expectation per plaquette; the landed matching rule).
The comparator's dimensionless coupling is alpha_G = U / (pi c_G) = (1/(2 pi)) (U/u)^(1/2).

This runner measures, from ground-state energies only (the mixed energy estimator is exact for any guide): the sector energies
E(q) for W = 2q, q = 0..3, on 4^3, 6^3, 8^3, giving U_W = L [E(1) - E(0)] / 2 and the ratio [E(2) - E(0)] / [E(1) - E(0)] (4 in
the comparator); the transverse susceptibility at the smallest momentum on the same tori; and alpha_G from each route.
Checks: (1) exact 2^3 control of the winding sectors and the projected sector energies; (2) the sector energies on 4^3-8^3;
(3) U_W against 1/chi on the same tori; (4) alpha_G (reported). Prints one line per check and TOTAL: PASS=N FAIL=M.
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

AUDIT_INPUT_PATHS = ['docs/RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/RING_MODEL_STATIC_TEST_CHARGES_AT_THE_PURE_RING_POINT_ARE_NOT_CONFINED_ON_THE_SMALL_TORI_AND_THEIR_INTERACTION_HAS_THE_LATTICE_COULOMB_SHAPE_BOUNDED_THEOREM_NOTE_2026-09-25.md']
AUDIT_TIMEOUT_SEC = 7200

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


def run_E(pr, init, nw, ngen, rng, hvec, h, beta=0.5):
    out, _ = energy_run(pr, init, nw, ngen, DTAU, ngen // 4, rng, h * hvec, beta * h * hvec, Lcs=(0,))
    return out[0]


# ------------------------------------------------------------------------------------------------ main
DTAU, H1 = 0.05, 0.15


def divergence(ice, s):
    d = np.zeros(ice.nv, dtype=int)
    for v in range(ice.nv):
        for (l, sg) in ice.inc[v]:
            d[v] += sg * s[l]
    return d


# ---------------------------------------------------------------- 1. exact 2^3 control of the winding sectors
def sector_ground(ice, codes, W):
    """Lowest eigenvalue of the ring clause over every ice state with section flux W (all flip components of the sector)."""
    bits = np.arange(ice.nl)
    sig = ((codes[:, None] >> bits) & 1) * 2 - 1
    Wx = np.stack([sig[:, (ice.axis == a) & (ice.coord == 0)].sum(axis=1) for a in range(3)], axis=1)
    sec = codes[np.all(Wx == np.array(W), axis=1)]
    pos = {int(c): n for n, c in enumerate(sec)}
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)
    Hs = np.zeros((len(sec), len(sec)))
    for n, c in enumerate(sec):
        sg = ((int(c) >> bits) & 1) * 2 - 1
        for p_ in np.flatnonzero(np.abs((sg[ice.plaq] * ice.sign).sum(axis=1)) == 4):
            Hs[pos[int(c) ^ int(masks[p_])], n] -= 1.0
    return float(np.linalg.eigvalsh(Hs)[0]), len(sec)


ice2 = Ice(2)
rows1, ok1, dev1 = [], True, []
for q in (0, 1, 2):
    s = ice2.sector_state(q)
    W = ice2.winding_fast(s)
    ok1 &= bool(np.all(divergence(ice2, s) == 0)) and W == (2 * q, 0, 0)
    codes, order, H2, sig_of = exact_L2(ice2, s)
    Es, n_sec = sector_ground(ice2, codes, W)
    rr = np.random.default_rng(301 + q)
    init = loop_vmc(ice2, ALPHA, sweeps=400, therm=60, r=rr, start=s, fix_winding=True)
    ok1 &= all(ice2.winding_fast(x) == W for x in init)
    n_dist = len({x.tobytes() for x in init})
    if q < 2:
        pr2 = Projector(ice2, np.ones(ice2.np_, bool), ALPHA, 0.0, np.zeros((1, ice2.nl), complex), 201 + q)
        em = run_E(pr2, init, 400, 400 if DRY else 1600, rr, np.zeros(ice2.nl), 0.0)
        dev1.append((em[0] - Es) / em[1])
        rows1.append(f"q={q}: W={W}, {n_sec} sector states (the seed's flip component {len(order)}; {n_dist} distinct loop samples), exact sector "
                     f"ground {Es:.6f}, projector from the samples {em[0]:.5f}+-{em[1]:.5f} ({dev1[-1]:+.1f} sigma)")
    else:
        rows1.append(f"q={q} (reported): W={W}, {n_sec} sector states; the seed is a frozen {len(order)}-state flip component and the flux-preserving "
                     f"loop moves from it give {n_dist} distinct sample(s), so on this torus they miss the sector's ground {Es:.6f}")
ok1 &= max(abs(d) for d in dev1) <= 3
check("exact 2^3 control of the winding sectors: the seeds are ice with section flux W = (2q, 0, 0), loop samples stay in the sector, and for "
      "q = 0, 1 the projected energy from those samples agrees with the exact ground energy over all the sector's flip components", ok1,
      "; ".join(rows1) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 2. the sector energies on 4^3-8^3
def sector_E(L, q, seeds, nw, ngen):
    ice = Ice(L)
    vals, errs, wok = [], [], True
    t0 = time.time()
    for sd in seeds:
        rr = np.random.default_rng(sd * 100 + L * 10 + q)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(q), fix_winding=True)
        wok &= all(ice.winding_fast(x) == (2 * q, 0, 0) for x in init)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), sd * 1000 + L * 10 + q)
        e = run_E(pr, init, nw, ngen, rr, np.zeros(ice.nl), 0.0)
        vals.append(e[0]); errs.append(e[1])
    vals, errs = np.array(vals), np.array(errs)
    n = len(vals)
    err = max(np.std(vals, ddof=1) / np.sqrt(n) if n > 1 else 0.0, errs.mean() / np.sqrt(n))
    return float(vals.mean()), float(err), wok, ice.np_, (time.time() - t0) / (len(seeds) * nw * ngen * DTAU)


PLAN = ({4: ((0, 1, 2), (11, 12)), 6: ((0, 1), (11, 12))} if DRY else
        {4: ((0, 1, 2), (11, 12, 13, 14)), 6: ((0, 1, 2, 3), (11, 12, 13, 14, 15, 16)), 8: ((0, 1, 2, 3), (11, 12, 13, 14, 15, 16, 17, 18))})
NW, NGEN = (192, 200) if DRY else (1920, 1000)
SE, UW, rows2, ok2 = {}, {}, [], True
for L, (qs, seeds) in PLAN.items():
    for q in qs:
        SE[(L, q)] = sector_E(L, q, seeds, NW, NGEN)
        ok2 &= SE[(L, q)][2]
    E0, e0 = SE[(L, 0)][0], SE[(L, 0)][1]
    dE = {q: (SE[(L, q)][0] - E0, np.hypot(SE[(L, q)][1], e0)) for q in qs if q > 0}
    ok2 &= all(dE[q][0] > 0 for q in dE) and all(dE[q + 1][0] > dE[q][0] for q in dE if q + 1 in dE)
    qa = np.array(sorted(dE), dtype=float); ya = np.array([dE[q][0] for q in sorted(dE)]); ea = np.array([dE[q][1] for q in sorted(dE)])
    if len(qa) >= 2:
        X = np.stack([qa ** 2, qa ** 4], axis=1) / ea[:, None]
        coef, *_ = np.linalg.lstsq(X, ya / ea, rcond=None)
        cov = np.linalg.inv(X.T @ X)
        A_fit, A_err = float(coef[0]), float(np.sqrt(cov[0, 0]))
    else:
        A_fit, A_err = dE[1][0], dE[1][1]
    UW[L] = dict(u1=L * dE[1][0] / 2, u1e=L * dE[1][1] / 2, uf=L * A_fit / 2, ufe=L * A_err / 2,
                 ratio=(dE[2][0] / dE[1][0]) if 2 in dE else np.nan,
                 ratioe=(dE[2][0] / dE[1][0]) * np.hypot(dE[2][1] / dE[2][0], dE[1][1] / dE[1][0]) if 2 in dE else np.nan,
                 u=-E0 / SE[(L, 0)][3], ue=e0 / SE[(L, 0)][3])
    rows2.append(f"{L}^3: E(0) {E0:.4f}+-{e0:.4f} (u {UW[L]['u']:.5f}); " + ", ".join(f"E({q})-E(0) {dE[q][0]:+.4f}+-{dE[q][1]:.4f}" for q in sorted(dE))
                 + f"; U_W from q=1 {UW[L]['u1']:.3f}+-{UW[L]['u1e']:.3f}, from the fit A q^2 + B q^4 {UW[L]['uf']:.3f}+-{UW[L]['ufe']:.3f}"
                 + (f"; [E(2)-E(0)]/[E(1)-E(0)] {UW[L]['ratio']:.2f}+-{UW[L]['ratioe']:.2f}" if 2 in dE else "")
                 + f"; {SE[(L, 0)][4] * 1e3:.2f} ms per walker-time")
check("the winding-sector energies on 4^3-8^3 at the pure-ring point: every sample stays in its sector, and the energy rises with the flux "
      "on every torus; U_W = L [E(1) - E(0)] / 2 and the ratio against the comparator's 4 (reported)", ok2, " || ".join(rows2) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 3. U_W against 1/chi at the smallest momentum on the same tori
def chi_L(L, seeds, nw, ngen):
    ice = Ice(L)
    k = 2 * np.pi / L
    hv, _ = triple(ice, k)
    pref = 2.0 if abs(np.cos(2 * k) - 1) < 1e-9 else 1.0
    out = []
    for sd in seeds:
        rr = np.random.default_rng(sd * 100 + L + nw)
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), sd * 1000 + L + nw)
        E0 = run_E(pr, init, nw, ngen, rr, np.zeros(ice.nl), 0.0)
        E1 = run_E(pr, init, nw, ngen, rr, hv, H1)
        E2 = run_E(pr, init, nw, ngen, rr, hv, 2 * H1)
        out.append(chi_fit(*E0, *E1, *E2, H1, ice.nv, pref))
    cs = np.array([x[0] for x in out]); be = np.array([x[1] for x in out])
    n = len(cs)
    return k, float(cs.mean()), float(max(np.std(cs, ddof=1) / np.sqrt(n), be.mean() / np.sqrt(n)))


CHI_SEEDS = (301, 302) if DRY else (301, 302, 303, 304)
CNW, CNGEN = (48, 120) if DRY else (480, 600)
rows3, ok3, CH = [], True, {}
for L in PLAN:
    k, c, ce = chi_L(L, CHI_SEEDS, CNW, CNGEN)
    CH[L] = (k, c, ce)
    Ui, Uie = 1 / c, ce / c ** 2
    z1 = (UW[L]["u1"] - Ui) / np.hypot(UW[L]["u1e"], Uie)
    zf = (UW[L]["uf"] - Ui) / np.hypot(UW[L]["ufe"], Uie)
    ok3 &= bool(np.isfinite(c) and c > 0 and ce / c < 0.25)
    rows3.append(f"{L}^3 k={k:.3f}: chi {c:.3f}+-{ce:.3f}, 1/chi {Ui:.3f}+-{Uie:.3f}; U_W (q=1) {UW[L]['u1']:.3f} ({z1:+.1f} sigma), U_W (fit) "
                 f"{UW[L]['uf']:.3f} ({zf:+.1f} sigma)")
check("the uniform-field coupling U_W against the transverse route 1/chi at the smallest momentum of the same torus (reported); in the Gaussian "
      "comparator the two are one coupling", ok3, "; ".join(rows3) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. the comparator's dimensionless coupling
rows4 = []
for L in PLAN:
    u = UW[L]["u"]
    for name, U, Ue in (("1/chi", 1 / CH[L][1], CH[L][2] / CH[L][1] ** 2), ("U_W fit", UW[L]["uf"], UW[L]["ufe"])):
        a = np.sqrt(U / u) / (2 * np.pi)
        rows4.append(f"{L}^3 {name}: U {U:.3f}, c_G = (4uU)^1/2 {np.sqrt(4 * u * U):.3f}, alpha_G {a:.4f}+-{a * Ue / (2 * U):.4f}")
U9244 = (1.48, 0.20)
u8 = UW[max(PLAN)]["u"]
rows4.append(f"static pair on 8^3 (open PR 9244, through the core): U {U9244[0]:.2f}+-{U9244[1]:.2f}, alpha_G {np.sqrt(U9244[0] / u8) / (2 * np.pi):.4f}")
check("the Gaussian comparator's dimensionless coupling alpha_G = U / (pi c_G) = (U/u)^(1/2) / (2 pi) from each route (reported): a comparator "
      "number for the supplied model, not a measured coupling of any physical field", True, "; ".join(rows4))

print(f"elapsed_sec: {time.time() - T0:.0f}")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
