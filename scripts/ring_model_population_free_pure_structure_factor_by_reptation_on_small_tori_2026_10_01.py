#!/usr/bin/env python3
"""Population-free transverse structure factor of the ring model by reptation (middle of the path), checked against exact diagonalisation on 2^3 and
against forward walking (3840 walkers) on 4^3 and 6^3.

SUPPLIED MODEL (nothing here is a framework premise): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law and the
ring clause H = -g sum_p (U_p + U_p^dag), g = 1 (V = 0), restricted to the canonical zero-winding flip component; guide exp(0.2 N_flip) (N_flip = number
of flippable plaquettes).  Observable: S = <0| (1/3) sum_a |O_a|^2 |0> with the cyclic triple O_a = N^-1/2 sum_{a-links} e^{i k x_(a+1)} sigma
(fw_lib.triple); the reptation code also measures the anticyclic triple (a-links modulated along axis a+2) and averages the six modes (equal by symmetry).

ESTIMATOR.  One path of Mseg segments of imaginary time dur is sampled by importance-sampled continuous-time bounce reptation (grow a segment at the leading
end by the guided jump process, delete one at the other end, accept min(1, exp(W_new - W_old)), W = -int E_L, bounce on rejection; code of
c7/rept/rq3_lib.py with the charge/link-hopping machinery removed; reproduces rq3_lib exactly for equal seeds).  For a long path the configuration at the
MIDDLE of the path is distributed as |psi_0|^2 (pure); the two ends give the mixed distribution psi_G psi_0.  The middle configuration is advanced
incrementally with every accepted move and checked against a replay from the tail at every measurement (integrity flag).  "Shift range" = (max - min of the
signed shift of the path)/Mseg: the interior of the path is replaced only when it exceeds one path length (bounce reptation moves the path sub-diffusively
on large tori), so burn-in runs until the shift range exceeds BURN_RANGE and production until it exceeds PROD_RANGE path lengths.  Forward walking = the
landed fixed-population projector (fw_lib.Projector, copied), lag 4.0 of the mixed-to-pure forward-walking curve.

WHAT IS EXACT / FLOAT.  Only the 2^3 reference values (E0, pure S, mixed S) are exact (dense/sparse diagonalisation of the 864-state component).  Everything
else is a Monte Carlo float diagnostic: errors are the scatter of independent chain means (reptation) and 10 bin errors of one run (forward walking);
agreement within 3 combined standard errors is a descriptive test, not a certification, convergence statement or physical identification.  The forward-walking
value carries its own lineage-collapse caveat (few distinct ancestors at long lags).

RS_SMOKE=1 runs tiny settings (code-path test only; chain-length and agreement criteria are then meaningless / the shift-range requirement is switched off).
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
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 3600
RESULTS = []
T0 = time.time()
SMOKE = os.environ.get("RS_SMOKE") == "1"
ALPHA = 0.2


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def info(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------------------------------------------------- lattice (copied from rq2_lib / fw_lib)

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


def triple(ice, k):
    """The cyclic triple of transverse modes: a-links modulated along axis (a + 1) mod 3, so the three modes cover each plaquette
    orientation once. Returns the field pattern sum over the triple of cos(k x_b) and the three mode vectors O = N^-1/2 sum e^{ikx_b} sigma."""
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    hv = np.cos(k * xb)
    PH = np.array([np.exp(1j * k * xb) * (ice.axis == a) / np.sqrt(ice.nv) for a in range(3)])
    return hv, PH


def exact_L2(ice, canon):
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    codes = []
    n = 1 << ice.nl
    step = 1 << 16
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



def make_tables(ice):
    plaq = ice.plaq.astype(np.int64)
    sign = ice.sign.astype(np.int64)
    A = ice.A.astype(np.int64).copy()
    A[A == ice.np_] = -1
    M = np.rint(ice.M).astype(np.int64)
    pol4 = np.zeros((ice.nl, 4), dtype=np.int64)
    cnt = np.zeros(ice.nl, dtype=np.int64)
    for p in range(ice.np_):
        for k in range(4):
            l = ice.plaq[p, k]
            pol4[l, cnt[l]] = p
            cnt[l] += 1
    assert np.all(cnt == 4)
    return plaq, sign, A, M, pol4


# ---------------------------------------------------------------------------------------------------------------- reptation kernels (plaquette flips only)
@nb.njit(cache=False)
def rate_plaq(s, sig, C, flp, plaq, A, M, dynf, exptab):
    if not flp[s]:
        return 0.0
    return exptab[_dN(s, sig, plaq, A, M, dynf, C) + 16]


@nb.njit(cache=False)
def rq_init(sig, C, flp, nflp, rate, plaq, sign, A, M, dynf, exptab):
    n_w, Np = C.shape
    for i in range(n_w):
        cnt = 0
        for q in range(Np):
            c = 0
            for k in range(4):
                c += sig[i, plaq[q, k]] * sign[q, k]
            C[i, q] = c
            f = c == 4 or c == -4
            flp[i, q] = f
            cnt += 1 if f else 0
        nflp[i] = cnt
        for s in range(Np):
            rate[i, s] = rate_plaq(s, sig[i], C[i], flp[i], plaq, A, M, dynf, exptab)


@nb.njit(cache=False)
def rq_apply(e, ev, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp):
    """Flip plaquette ev in end state e with every table and rate update."""
    Wd = A.shape[1]
    s_ = sig[e]
    C_ = C[e]
    f_ = flp[e]
    r_ = rate[e]
    b_ = bs[e]
    tick[0] += 1
    tk = tick[0]
    nC = 0
    for k in range(4):
        l = plaq[ev, k]
        s_[l] = -s_[l]
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
        newf = c == 4 or c == -4
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
                rn = rate_plaq(s, s_, C_, f_, plaq, A, M, dynf, exptab)
                b_[s // 64] += rn - r_[s]
                r_[s] = rn


@nb.njit(cache=False)
def rq_resum(e, rate, bs):
    for b in range(bs.shape[1]):
        bs[e, b] = 0.0
    for i in range(rate.shape[1]):
        bs[e, i // 64] += rate[e, i]


@nb.njit(cache=False)
def rq_copy(src, dst, sig, C, flp, nflp, rate, bs):
    sig[dst, :] = sig[src, :]
    C[dst, :] = C[src, :]
    flp[dst, :] = flp[src, :]
    nflp[dst] = nflp[src]
    rate[dst, :] = rate[src, :]
    bs[dst, :] = bs[src, :]


@nb.njit(cache=False)
def rq_grow(e, dur, evbuf, kmax, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp):
    """Importance-sampled jump process for time dur from end e; events into evbuf.  Returns (W = -int E_L dt, count, overflow); E_L = -(total rate)."""
    ne = rate.shape[1]
    nblk = bs.shape[1]
    t = 0.0
    W = 0.0
    n = 0
    while True:
        lam = 0.0
        for b in range(nblk):
            lam += bs[e, b]
        EL = -lam
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
        rq_apply(e, ev, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)


@nb.njit(cache=False)
def rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp):
    kmax = segE.shape[1]
    evbuf = np.zeros(kmax, dtype=np.int32)
    bad = 0
    for i in range(Mseg):
        W, n, over = rq_grow(1, dur, evbuf, kmax, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)
        if over:
            bad += 1
        for k in range(n):
            segE[i, k] = evbuf[k]
        segN[i] = n
        segW[i] = W
    return bad


@nb.njit(cache=False)
def flip_ev(sg, ev, plaq):
    for kk in range(4):
        l = plaq[ev, kk]
        sg[l] = -sg[l]


@nb.njit(cache=False)
def replay(sg, start, nseg, segE, segN, plaq):
    Mcap = segE.shape[0]
    for i in range(nseg):
        sl = (start + i) % Mcap
        for k in range(segN[sl]):
            flip_ev(sg, segE[sl, k], plaq)


@nb.njit(cache=False)
def mode_S(sg, cph, sph, axis, S6):
    """|O_m|^2 of six modes: m = a (cyclic triple, phases row 0) and m = 3 + a (anticyclic triple, row 1)."""
    re = np.zeros(6)
    im = np.zeros(6)
    for l in range(sg.shape[0]):
        a = axis[l]
        s = sg[l]
        re[a] += cph[0, l] * s
        im[a] += sph[0, l] * s
        re[3 + a] += cph[1, l] * s
        im[3 + a] += sph[1, l] * s
    for m in range(6):
        S6[m] = re[m] * re[m] + im[m] * im[m]


@nb.njit(cache=False)
def path_profile(start, Mseg, sig0, work, segE, segN, cph, sph, axis, plaq, row):
    """Triple-averaged |O|^2 at the nprof + 1 equally spaced path boundaries (0 = tail end), by replay from the tail: row[0] cyclic, row[1] anticyclic."""
    Mcap = segE.shape[0]
    nprof = row.shape[1] - 1
    per = Mseg // nprof
    re = np.zeros(6)
    im = np.zeros(6)
    for l in range(work.shape[0]):
        work[l] = sig0[l]
        a = axis[l]
        re[a] += cph[0, l] * work[l]
        im[a] += sph[0, l] * work[l]
        re[3 + a] += cph[1, l] * work[l]
        im[3 + a] += sph[1, l] * work[l]
    for t in range(2):
        row[t, 0] = (re[3 * t] ** 2 + im[3 * t] ** 2 + re[3 * t + 1] ** 2 + im[3 * t + 1] ** 2 + re[3 * t + 2] ** 2 + im[3 * t + 2] ** 2) / 3.0
    for i in range(Mseg):
        sl = (start + i) % Mcap
        for k in range(segN[sl]):
            ev = segE[sl, k]
            for kk in range(4):
                l = plaq[ev, kk]
                a = axis[l]
                re[a] -= 2.0 * cph[0, l] * work[l]
                im[a] -= 2.0 * sph[0, l] * work[l]
                re[3 + a] -= 2.0 * cph[1, l] * work[l]
                im[3 + a] -= 2.0 * sph[1, l] * work[l]
                work[l] = -work[l]
        if (i + 1) % per == 0:
            for t in range(2):
                row[t, (i + 1) // per] = (re[3 * t] ** 2 + im[3 * t] ** 2 + re[3 * t + 1] ** 2 + im[3 * t + 1] ** 2 + re[3 * t + 2] ** 2 + im[3 * t + 2] ** 2) / 3.0


@nb.njit(cache=False)
def rq_run_S(nmoves, dur, meas_every, segE, segN, segW, pos, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp,
             midsig, work, cph, sph, axis, Eout, Sout, Prof, stats, cnt):
    """Bounce reptation; the middle configuration midsig advances with every accepted shift.  Every meas_every moves record E_L at the two ends, the six mode
    intensities at middle / tail / head (Sout columns 0-5, 6-11, 12-17), the signed path shift (column 18) and the boundary profile (Prof).  pos = [start, Mseg, dir]."""
    Mcap, kmax = segE.shape
    evbuf = np.zeros(kmax, dtype=np.int32)
    S6 = np.zeros(6)
    start = pos[0]
    Mseg = pos[1]
    d = pos[2]
    h = Mseg // 2
    for mv in range(nmoves):
        lead = 1 if d > 0 else 0
        rq_copy(lead, lead + 2, sig, C, flp, nflp, rate, bs)
        W, n, over = rq_grow(lead, dur, evbuf, kmax, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)
        if d > 0:
            old = start % Mcap
        else:
            old = (start + Mseg - 1) % Mcap
        ok = (not over) and (np.random.random() < np.exp(min(0.0, W - segW[old])))
        if ok:
            if d > 0:
                sm = (start + h) % Mcap                      # forward shift: the middle advances over the old path segment h
                for i in range(segN[sm]):
                    flip_ev(midsig, segE[sm, i], plaq)
                for i in range(segN[old]):
                    rq_apply(0, segE[old, i], sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)
                for i in range(n):
                    segE[old, i] = evbuf[i]
                segN[old] = n
                segW[old] = W
                start = (start + 1) % Mcap
            else:
                sm = (start + h - 1) % Mcap                  # backward shift: the middle retreats over the old path segment h - 1
                for i in range(segN[sm]):
                    flip_ev(midsig, segE[sm, i], plaq)
                for i in range(segN[old] - 1, -1, -1):
                    rq_apply(1, segE[old, i], sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)
                for i in range(n):
                    segE[old, i] = evbuf[n - 1 - i]
                segN[old] = n
                segW[old] = W
                start = (start - 1) % Mcap
            stats[0] += 1
            stats[3] += d
        else:
            rq_copy(lead + 2, lead, sig, C, flp, nflp, rate, bs)
            d = -d
            stats[1] += 1
            if over:
                stats[2] += 1
        if (mv + 1) % meas_every == 0 and cnt[0] < Eout.shape[0]:
            r = cnt[0]
            el0 = 0.0
            el1 = 0.0
            for b in range(bs.shape[1]):
                el0 -= bs[0, b]
                el1 -= bs[1, b]
            Eout[r, 0] = el0
            Eout[r, 1] = el1
            mode_S(midsig, cph, sph, axis, S6)
            for m in range(6):
                Sout[r, m] = S6[m]
            mode_S(sig[0], cph, sph, axis, S6)
            for m in range(6):
                Sout[r, 6 + m] = S6[m]
            mode_S(sig[1], cph, sph, axis, S6)
            for m in range(6):
                Sout[r, 12 + m] = S6[m]
            Sout[r, 18] = stats[3]
            path_profile(start, Mseg, sig[0], work, segE, segN, cph, sph, axis, plaq, Prof[r])
            cnt[0] += 1
    pos[0] = start
    pos[2] = d


def run_chain(ice, tabs, init, k, Mseg, dur, seed, cfg):
    """One reptation chain with adaptive burn-in (until the path has shifted over cfg['burn_range'] path lengths, cap cfg['burn_cap'] moves) and production
    (until the production shift range exceeds cfg['prod_range'] and at least cfg['prod_min'] moves, cap cfg['prod_cap']).  Returns a dict of scalar summaries."""
    plaq, sign, A, M, pol4 = tabs
    nb_seed(seed)
    nl, npl, nv = ice.nl, ice.np_, ice.nv
    nblk = (npl + 63) // 64
    me, chunk = cfg["me"], cfg["chunk"]
    sig = np.array([init] * 4, dtype=np.int64)
    C = np.zeros((4, npl), dtype=np.int64)
    flp = np.zeros((4, npl), dtype=np.bool_)
    nflp = np.zeros(4, dtype=np.int64)
    rate = np.zeros((4, npl))
    bs = np.zeros((4, nblk))
    dynf = np.ones(npl, dtype=np.bool_)
    exptab = np.exp(ALPHA * (np.arange(33) - 16.0))
    rq_init(sig, C, flp, nflp, rate, plaq, sign, A, M, dynf, exptab)
    for e in range(4):
        rq_resum(e, rate, bs)
    stamp = np.zeros(npl, dtype=np.int64)
    cstamp = np.zeros(npl, dtype=np.int64)
    tick = np.zeros(1, dtype=np.int64)
    cbuf = np.zeros(64, dtype=np.int64)
    kmax = 512
    segE = np.zeros((Mseg, kmax), dtype=np.int32)
    segN = np.zeros(Mseg, dtype=np.int32)
    segW = np.zeros(Mseg)
    bad = rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp)
    tl_v = np.array([ice.verts[l // 3] for l in range(nl)])
    xb1 = tl_v[np.arange(nl), (ice.axis + 1) % 3]
    xb2 = tl_v[np.arange(nl), (ice.axis + 2) % 3]
    cph = np.ascontiguousarray(np.array([np.cos(k * xb1), np.cos(k * xb2)]) / np.sqrt(nv))
    sph = np.ascontiguousarray(np.array([np.sin(k * xb1), np.sin(k * xb2)]) / np.sqrt(nv))
    axis = np.ascontiguousarray(ice.axis, dtype=np.int64)
    pos = np.array([0, Mseg, 1], dtype=np.int64)
    midsig = sig[0].copy()
    replay(midsig, 0, Mseg // 2, segE, segN, plaq)
    work = np.zeros(nl, dtype=np.int64)
    stats = np.zeros(4, dtype=np.int64)
    cnt = np.zeros(1, dtype=np.int64)

    def chunk_run(nm, keep):
        rows = nm // me + 1
        Eo = np.zeros((rows, 2))
        So = np.zeros((rows, 19))
        Po = np.zeros((rows, 2, 17))
        cnt[0] = 0
        rq_run_S(nm, dur, me, segE, segN, segW, pos, sig, C, flp, nflp, rate, bs, plaq, sign, A, M, dynf, pol4, exptab, stamp, tick, cbuf, cstamp,
                 midsig, work, cph, sph, axis, Eo, So, Po, stats, cnt)
        for e in range(2):
            rq_resum(e, rate, bs)
        return (Eo[:cnt[0]], So[:cnt[0]], Po[:cnt[0]]) if keep else None

    burned, xmin, xmax = 0, 0, 0
    while burned < cfg["burn_cap"]:
        nm = min(chunk, cfg["burn_cap"] - burned)
        chunk_run(nm, False)
        burned += nm
        xmin, xmax = min(xmin, int(stats[3])), max(xmax, int(stats[3]))
        if (xmax - xmin) >= cfg["burn_range"] * Mseg:
            break
    burn_rng = (xmax - xmin) / Mseg
    stats[:] = 0
    E_, S_, P_ = [], [], []
    done = 0
    pmin = pmax = 0
    while done < cfg["prod_cap"]:
        nm = min(chunk, cfg["prod_cap"] - done)
        e_, s_, p_ = chunk_run(nm, True)
        E_.append(e_)
        S_.append(s_)
        P_.append(p_)
        done += nm
        pmin, pmax = min(pmin, int(stats[3])), max(pmax, int(stats[3]))
        if done >= cfg["prod_min"] and (pmax - pmin) >= cfg["prod_range"] * Mseg:
            break
    E_, S_, P_ = np.concatenate(E_), np.concatenate(S_), np.concatenate(P_)
    mid2 = sig[0].copy()
    replay(mid2, int(pos[0]), Mseg // 2, segE, segN, plaq)
    hd2 = sig[0].copy()
    replay(hd2, int(pos[0]), Mseg, segE, segN, plaq)
    diff = float(np.abs(P_.mean(axis=1)[:, 8] - S_[:, 0:6].mean(axis=1)).max())
    integ = bool(np.array_equal(mid2, midsig) and np.array_equal(hd2, sig[1]) and bad == 0 and stats[2] == 0 and diff < 1e-9)
    X = S_[:, 18]
    rng_prod = (max(X.max(), 0.0) - min(X.min(), 0.0)) / Mseg
    jl, jh = 4, 12
    return dict(mid_six=S_[:, 0:6].mean(), mid_cyc=S_[:, 0:3].mean(), mid_anti=S_[:, 3:6].mean(), win_six=P_[:, :, jl:jh + 1].mean(),
                ends_six=0.5 * (S_[:, 6:12].mean() + S_[:, 12:18].mean()), ends_cyc=0.5 * (S_[:, 6:9].mean() + S_[:, 12:15].mean()),
                u_ends=-0.5 * (E_[:, 0] + E_[:, 1]).mean() / npl, E_ends=0.5 * (E_[:, 0] + E_[:, 1]).mean(), acc=stats[0] / max(1, stats[0] + stats[1]),
                burn_rng=burn_rng, prod_rng=rng_prod, burn_moves=burned, prod_moves=done, integ=integ, diff=diff, rows=len(S_))


def start_state(ice, kind, rr):
    if kind == "canon":
        return ice.sector_state(0)
    return loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // ice.L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)[-1]


def chains(L, kind, nch, Mseg, dur, k, cfg, seed0):
    ice = Ice(L)
    tabs = make_tables(ice)
    out = []
    for c in range(nch):
        rr = np.random.default_rng(seed0 + c)
        init = start_state(ice, kind, rr)
        out.append(run_chain(ice, tabs, init, k, Mseg, dur, 1000 * (seed0 + c) + 7, cfg))
    return out


def se(x):
    x = np.asarray(x, dtype=float)
    return x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")


def agg(chs, key):
    v = [c[key] for c in chs]
    return float(np.mean(v)), se(v)


# ---------------------------------------------------------------------------------------------------------------- forward walking (fw_lib.Projector.run, copied)
def fw_run(ice, k, init, n_w, n_gen, therm, lags, seed, rng):
    nb_seed(seed)
    plaq = ice.plaq.astype(np.int64)
    sign = ice.sign.astype(np.int64)
    A = ice.A.astype(np.int64).copy()
    A[A == ice.np_] = -1
    M = np.rint(ice.M).astype(np.int64)
    dyn = np.ones(ice.np_, dtype=np.bool_)
    exptab = np.exp(ALPHA * (np.arange(33) - 16.0))
    PH = np.ascontiguousarray(triple(ice, k)[1].T.astype(np.complex128))
    stamp = np.zeros(ice.np_, dtype=np.int64)
    tick = np.zeros(1, dtype=np.int64)
    sbuf = np.zeros(4096, dtype=np.int64)
    rbuf = np.zeros(4096)
    picks0 = rng.integers(len(init), size=n_w)
    sig = np.array([init[j] for j in picks0], dtype=np.int8)
    C = np.zeros((n_w, ice.np_), dtype=np.int8)
    flp = np.zeros((n_w, ice.np_), dtype=np.bool_)
    dN = np.zeros((n_w, ice.np_), dtype=np.int8)
    nflp = np.zeros(n_w, dtype=np.int64)
    nb_init(sig, C, flp, dN, nflp, plaq, sign, A, M, dyn)
    Om = sig.astype(np.float64) @ PH
    nm = Om.shape[1]
    Lmax = max(lags)
    hist = np.zeros((n_w, Lmax + 1, nm))
    anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
    logw = np.zeros(n_w)
    ELend = np.zeros(n_w)
    out_fw, out_nd = [], []
    for g in range(n_gen):
        nb_walk(sig, C, flp, dN, nflp, Om, plaq, A, M, dyn, exptab, 0.0, 0.015, PH, stamp, tick, sbuf, rbuf, logw, ELend)
        w = np.exp(logw - logw.max())
        wn = w / w.sum()
        slot = g % (Lmax + 1)
        hist[:, slot] = np.abs(Om) ** 2
        anc[:, slot] = np.arange(n_w)
        if g >= therm:
            out_fw.append(np.array([wn @ hist[:, (g - Lg) % (Lmax + 1)] for Lg in lags]))
            out_nd.append([len(np.unique(anc[:, (g - Lg) % (Lmax + 1)])) / n_w for Lg in lags])
        cum = np.cumsum(wn)
        picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
        sig, C, flp, dN, nflp, Om, hist, anc = sig[picks], C[picks], flp[picks], dN[picks], nflp[picks], Om[picks], hist[picks], anc[picks]
    fw = np.array(out_fw)                                # (n_post, nlags, 3)
    S = fw.mean(axis=2)
    nbins = 10
    res = []
    for j in range(len(lags)):
        b = np.array([c.mean() for c in np.array_split(S[:, j], nbins)])
        res.append((float(S[:, j].mean()), float(b.std(ddof=1) / np.sqrt(nbins)), float(np.mean([r[j] for r in out_nd]))))
    return res


def fw_study(L, k, n_w, n_gen, lags, seed):
    ice = Ice(L)
    rr = np.random.default_rng(seed)
    init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    return fw_run(ice, k, init, n_w, n_gen, n_gen // 2, lags, seed, rr)


def fmt(pm):
    return f"{pm[0]:.4f}+-{pm[1]:.4f}"



# ---------------------------------------------------------------------------------------------------------------- exact 2^3 component
def exact_2cube():
    ice = Ice(2)
    codes, order, H, sig_of = exact_L2(ice, ice.sector_state(0))
    ev, vec = eigsh(H.astype(float), k=1, which="SA")
    E0 = float(ev[0])
    phi = np.abs(vec[:, 0])
    PH = triple(ice, np.pi)[1]
    sg = np.array([sig_of(c) for c in order], dtype=np.int64)
    Sm = (np.abs(sg.astype(float) @ PH.T) ** 2).mean(axis=1)
    nfl = np.array([(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4).sum() for s in sg])
    p2 = phi ** 2 / (phi ** 2).sum()
    pm = np.exp(ALPHA * nfl) * phi
    pm /= pm.sum()
    return E0, float(p2 @ Sm), float(pm @ Sm), len(order)


def zscore(a, ea, b, eb=0.0):
    return abs(a - b) / max(1e-12, float(np.hypot(ea, eb)))


# ---------------------------------------------------------------------------------------------------------------- settings
if SMOKE:
    CFG2 = dict(burn_range=1.0, burn_cap=20000, prod_range=0.0, prod_min=20000, prod_cap=20000, me=20, chunk=5000)
    CFG4 = dict(burn_range=0.5, burn_cap=20000, prod_range=0.0, prod_min=20000, prod_cap=20000, me=50, chunk=5000)
    CFG6 = dict(burn_range=0.3, burn_cap=30000, prod_range=0.0, prod_min=30000, prod_cap=30000, me=100, chunk=10000)
    N2, N4, N6C, N6L = 4, 3, 2, 2
    M2, D2, M4, D4, M6, D6 = 48, 0.4, 96, 0.2, 160, 0.125
    FW4 = dict(n_w=240, n_gen=330, lags=(0, 133, 200, 267))
    FW6 = dict(n_w=240, n_gen=330, lags=(0, 133, 200, 267))
    RANGE_REQ = 0.0
else:
    CFG2 = dict(burn_range=3.0, burn_cap=200000, prod_range=1.5, prod_min=600000, prod_cap=800000, me=20, chunk=50000)
    CFG4 = dict(burn_range=2.0, burn_cap=600000, prod_range=1.6, prod_min=300000, prod_cap=800000, me=100, chunk=50000)
    CFG6 = dict(burn_range=1.5, burn_cap=8000000, prod_range=1.6, prod_min=2000000, prod_cap=12000000, me=200, chunk=50000)
    N2, N4, N6C, N6L = 12, 10, 4, 4
    M2, D2, M4, D4, M6, D6 = 48, 0.4, 192, 0.1, 1600, 0.0125
    FW4 = dict(n_w=3840, n_gen=2500, lags=(0, 133, 200, 267, 400))
    FW6 = dict(n_w=3840, n_gen=1400, lags=(0, 133, 200, 267, 400))
    RANGE_REQ = 1.5
LAGI = 3                                                   # index of the forward-walking lag compared with the middle (267 generations x 0.015 = 4.0)


def main():
    t = time.time()
    E0, Sp, Sm, nst = exact_2cube()
    info(f"[exact 2^3, {nst}-state component] E0 = {E0:.6f}; pure S(pi) = {Sp:.5f}; mixed S (guide exp(0.2 N_flip)) = {Sm:.5f}   ({time.time() - t:.0f} s)")
    # (1) 2^3 control: canonical start (certainly inside the component)
    c2 = chains(2, "canon", N2, M2, D2, np.pi, CFG2, 11)
    mid, ends = agg(c2, "mid_six"), agg(c2, "ends_six")
    Ee = agg(c2, "E_ends")
    check(f"2^3 middle S vs exact {Sp:.5f}", zscore(mid[0], mid[1], Sp) <= 3.0,
          f"{fmt(mid)} (six modes, {N2} chains, path {M2 * D2:g}), {zscore(mid[0], mid[1], Sp):.1f} SE (limit 3); window {agg(c2, 'win_six')[0]:.4f}, cyclic {agg(c2, 'mid_cyc')[0]:.4f}")
    check(f"2^3 ends S vs exact mixed {Sm:.5f}", zscore(ends[0], ends[1], Sm) <= 3.0, f"{fmt(ends)}, {zscore(ends[0], ends[1], Sm):.1f} SE; E_ends {fmt(Ee)} vs exact {E0:.6f} (reported)")
    check("2^3 integrity (middle replay = incremental, head = replay, no overflow)", all(c["integ"] for c in c2), f"max profile-vs-middle diff {max(c['diff'] for c in c2):.1e}")
    # (2) 4^3 at k = pi/2
    c4 = chains(4, "loop", N4, M4, D4, np.pi / 2, CFG4, 700)
    fw4 = fw_study(4, np.pi / 2, FW4["n_w"], FW4["n_gen"], FW4["lags"], 41)
    m4, e4, w4 = agg(c4, "mid_six"), agg(c4, "ends_six"), agg(c4, "win_six")
    f4 = fw4[LAGI]
    z4 = zscore(m4[0], m4[1], f4[0], f4[1])
    info(f"[4^3, k=pi/2] FW ({FW4['n_w']} walkers) S at lags " + ", ".join(f"{FW4['lags'][j] * 0.015:.1f}: {fmt(fw4[j])} ({fw4[j][2]:.3f} distinct)" for j in range(len(FW4['lags']))))
    info("[4^3] landed 120-walker value 0.688 (supplied for comparison; not asserted)")
    check("4^3 middle S (reptation) vs forward walking", z4 <= 3.0, f"{fmt(m4)} ({N4} chains) vs {fmt(f4)} (lag {FW4['lags'][LAGI] * 0.015:.1f}): {z4:.1f} combined SE (limit 3); window {fmt(w4)}, cyclic {fmt(agg(c4, 'mid_cyc'))}")
    check("4^3 integrity", all(c["integ"] for c in c4), f"max diff {max(c['diff'] for c in c4):.1e}")
    check(f"4^3 production shift range >= {RANGE_REQ:g} path lengths in every chain{' (smoke: off)' if SMOKE else ''}", min(c["prod_rng"] for c in c4) >= RANGE_REQ,
          f"min/max {min(c['prod_rng'] for c in c4):.2f}/{max(c['prod_rng'] for c in c4):.2f}; burn-in range min {min(c['burn_rng'] for c in c4):.2f}; moves/chain ~{np.mean([c['prod_moves'] for c in c4]):.1e}")
    info(f"[4^3] mixed: reptation ends {fmt(e4)} vs FW lag 0 {fmt(fw4[0])}; middle {fmt(m4)}")
    # (3) 6^3 at k = pi/3: canonical-start and loop-start chains
    cc = chains(6, "canon", N6C, M6, D6, np.pi / 3, CFG6, 121)
    cl = chains(6, "loop", N6L, M6, D6, np.pi / 3, CFG6, 131)
    c6 = cc + cl
    fw6 = fw_study(6, np.pi / 3, FW6["n_w"], FW6["n_gen"], FW6["lags"], 61)
    m6, e6, w6 = agg(c6, "mid_six"), agg(c6, "ends_six"), agg(c6, "win_six")
    f6 = fw6[LAGI]
    z6 = zscore(m6[0], m6[1], f6[0], f6[1])
    for i, c in enumerate(c6):
        info(f"[6^3 chain {'canon' if i < N6C else 'loop '}{i % max(1, N6C) if i < N6C else i - N6C}] mid {c['mid_six']:.3f} win {c['win_six']:.3f} ends {c['ends_six']:.3f} | shift range burn/prod {c['burn_rng']:.2f}/{c['prod_rng']:.2f} path lengths, {c['prod_moves']:.1e} moves | integrity {'ok' if c['integ'] else 'FAILED'}")
    info(f"[6^3, k=pi/3] FW ({FW6['n_w']} walkers) S at lags " + ", ".join(f"{FW6['lags'][j] * 0.015:.1f}: {fmt(fw6[j])} ({fw6[j][2]:.3f} distinct)" for j in range(len(FW6['lags']))))
    check("6^3 middle S (reptation, canonical + loop starts) vs forward walking", z6 <= 3.0,
          f"{fmt(m6)} ({len(c6)} chains; canonical {agg(cc, 'mid_six')[0]:.4f}, loop {agg(cl, 'mid_six')[0]:.4f}) vs {fmt(f6)} (lag {FW6['lags'][LAGI] * 0.015:.1f}): {z6:.1f} combined SE (limit 3); window {fmt(w6)}")
    check("6^3 integrity", all(c["integ"] for c in c6), f"max diff {max(c['diff'] for c in c6):.1e}")
    check(f"6^3 production shift range >= {RANGE_REQ:g} path lengths in every chain{' (smoke: off)' if SMOKE else ''}", min(c["prod_rng"] for c in c6) >= RANGE_REQ,
          f"min/max {min(c['prod_rng'] for c in c6):.2f}/{max(c['prod_rng'] for c in c6):.2f}")
    info(f"[6^3] mixed: reptation ends {fmt(e6)} vs FW lag 0 {fmt(fw6[0])}; middle {fmt(m6)}")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   (runtime {time.time() - T0:.0f} s{', SMOKE settings' if SMOKE else ''})", flush=True)


if __name__ == "__main__":
    main()
