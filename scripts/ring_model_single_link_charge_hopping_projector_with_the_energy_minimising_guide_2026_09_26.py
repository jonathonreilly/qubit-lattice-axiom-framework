#!/usr/bin/env python3
"""Single-link charge hopping on the ring clause: the fixed-population projector with the energy-minimising guide penalty.

Setting (all supplied, none adopted): the ring clause with the single-link charge term of the landed notes,
H = -g sum_p (U_p + U_p^dag) - t sum_l sigma^x_l + M sum_v Q_v^2 (g = 1, M = 2), Q_v = div_v / 2, and the fixed-population
continuous-time projector with guide exp(alpha N_flip - gam sum_v Q_v^2), alpha = 0.2, as in the landed note
RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_THE_PROJECTOR_MISSES_THE_EXACT_2_CUBED_ENERGY_WITH_A_MISMATCHED_GUIDE_AND_ITS_6_CUBED_ENERGY_SPANS_TWO_PERCENT_ACROSS_GUIDES_BOUNDED_THEOREM_NOTE_2026-09-26.md.
A natural remedy for its guide dependence is to take, at each hopping value, the penalty that minimises the projector energy.

Checks: (1) numerical Ritz references for the full 2^3 torus (24 links, 2^24 states) at t = 0.35 and 0.5 by matrix-free Lanczos;
(2) on 2^3 with 2000 walkers the projector energies at penalties 0.3 ... 1.1 (three runs each) lie within 0.01 of the reference
except where the penalty is clearly mismatched, and the lowest of them within 0.006; (3) on 6^3 at t = 0.35 the penalty 1.2 gives the
lowest of three energies with both 1920 and 3840 walkers, and doubling the population lowers the energy at every penalty, by more than
0.3 at the lowest. Finite diagnostics; no controlled 6^3 energy or link expectation, phase or physical reading.
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

AUDIT_TIMEOUT_SEC = 3000

RESULTS = []
T0 = time.time()
ALPHA = 0.2
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




def q_series(ice, T, init, n_w, n_gen, dtau, rng, seed, alpha, gam, tl, Mq):
    """Fixed-population projection with comb resampling every dtau. Per generation: mixed energy, weighted variance of the
    local energy, and effective sample size / n_w."""
    nb_seed(seed)
    hl = np.zeros(ice.nl); bl = np.zeros(ice.nl); dynf = np.ones(ice.np_, dtype=np.bool_)
    exptab = np.exp(alpha * (np.arange(33) - 16.0))
    picks0 = rng.integers(len(init), size=n_w)
    sig = np.array([init[k] for k in picks0], dtype=np.int64)
    C = np.zeros((n_w, ice.np_), dtype=np.int64); flp = np.zeros((n_w, ice.np_), dtype=np.bool_)
    Q = np.zeros((n_w, ice.nv), dtype=np.int64); nflp = np.zeros(n_w, dtype=np.int64); sq2 = np.zeros(n_w, dtype=np.int64)
    Fh = np.zeros(n_w); rate = np.zeros((n_w, ice.np_ + ice.nl))
    q_init(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head,
           exptab, tl, gam, hl, bl, 1.0)
    stamp = np.zeros(ice.np_ + ice.nl, dtype=np.int64); cstamp = np.zeros(ice.np_, dtype=np.int64)
    tick = np.zeros(1, dtype=np.int64); cbuf = np.zeros(64, dtype=np.int64)
    logw = np.zeros(n_w); ELend = np.zeros(n_w)
    es, vs, ess = np.zeros(n_gen), np.zeros(n_gen), np.zeros(n_gen)
    for g in range(n_gen):
        q_walk(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head,
               exptab, tl, gam, hl, bl, 1.0, 0.0, Mq, dtau, stamp, tick, cbuf, cstamp, logw, ELend)
        mx = logw.max(); w = np.exp(logw - mx); Wt = w.sum()
        e = (w @ ELend) / Wt
        es[g] = e; vs[g] = (w @ (ELend - e) ** 2) / Wt; ess[g] = Wt ** 2 / (w @ w) / n_w
        cum = np.cumsum(w / Wt)
        picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
        sig, C, flp, Q, nflp, sq2, Fh, rate = sig[picks], C[picks], flp[picks], Q[picks], nflp[picks], sq2[picks], Fh[picks], rate[picks]
    return es, vs, ess



# ---------------------------------------------------------------- exact full 2^3 torus: matrix-free Lanczos
@nb.njit(cache=False)
def ex_tables(nl, inc6, incs6, pl, ps):
    n = 1 << nl
    q2 = np.zeros(n, dtype=np.int8)
    fm = np.zeros(n, dtype=np.int32)
    for s in range(n):
        tot = 0
        for v in range(inc6.shape[0]):
            d = 0
            for j in range(6):
                d += incs6[v, j] * (2 * ((s >> inc6[v, j]) & 1) - 1)
            q = d // 2
            tot += q * q
        q2[s] = tot
        m = 0
        for p in range(pl.shape[0]):
            c = 0
            for k in range(4):
                c += ps[p, k] * (2 * ((s >> pl[p, k]) & 1) - 1)
            if c == 4 or c == -4:
                m |= 1 << p
        fm[s] = m
    return q2, fm


@nb.njit(cache=False)
def ex_matvec(x, y, q2, fm, pm, nl, g, t, M):
    for s in range(x.shape[0]):
        acc = M * q2[s] * x[s]
        for l in range(nl):
            acc -= t * x[s ^ (1 << l)]
        m = fm[s]
        p = 0
        while m:
            if m & 1:
                acc -= g * x[s ^ pm[p]]
            m >>= 1
            p += 1
        y[s] = acc


@nb.njit(cache=False)
def ex_axpy(w, v, vprev, a, b):
    for i in range(w.shape[0]):
        w[i] -= a * v[i] + b * vprev[i]


def ex_lanczos(q2, fm, pm, nl, g, t, M, iters=240, seed=1):
    """Three-vector Lanczos from a random start; returns (iterations, lowest Ritz value, change over the last ten steps)."""
    n = 1 << nl
    v = np.random.default_rng(seed).standard_normal(n); v /= np.linalg.norm(v)
    w = np.empty(n); vprev = np.zeros(n)
    al, be = [], []
    b = 0.0
    last = None
    for it in range(iters):
        ex_matvec(v, w, q2, fm, pm, nl, g, t, M)
        a = float(v @ w); al.append(a)
        ex_axpy(w, v, vprev, a, b)
        b = float(np.linalg.norm(w)); be.append(b)
        w /= b
        vprev, v, w = v, w, vprev
        if it >= 10 and it % 10 == 0:
            e0 = float(np.linalg.eigvalsh(np.diag(al) + np.diag(be[:-1], 1) + np.diag(be[:-1], -1))[0])
            if last is not None and abs(e0 - last) < 1e-11:
                return it, e0, abs(e0 - last)
            last = e0
    return iters, last, np.inf



ice2 = Ice(2); T2 = QTables(ice2)
pm2 = np.array([sum(1 << int(l) for l in ice2.plaq[p]) for p in range(ice2.np_)], dtype=np.int64)
q2tab, fmtab = ex_tables(ice2.nl, T2.inc6, T2.incs6, T2.plaq, T2.sign)
EX = {}
for t in (0.35, 0.5):
    it, e0, de = ex_lanczos(q2tab, fmtab, pm2, ice2.nl, 1.0, t, 2.0)
    EX[t] = (e0, it, de)
del q2tab, fmtab
check("numerical Ritz references of the full 2^3 torus (24 links, 2^24 states), matrix-free Lanczos, converged",
      all(v[2] < 1e-10 for v in EX.values()),
      "; ".join(f"t = {t}: {v[0]:.9f} ({v[1]} steps, last change {v[2]:.1e})" for t, v in EX.items()) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2^3: energy against penalty
NG2 = 600 if DRY else 3000
GS = (0.3, 0.5, 0.7, 0.9, 1.1)
rows2, ok2 = [], True
for t in (0.35, 0.5):
    Es = []
    for gm in GS:
        vals = []
        for sd in range(3):
            rr = np.random.default_rng(800 + sd + int(100 * gm) + int(1000 * t))
            es, vs, ess = q_series(ice2, T2, [ice2.sector_state(0)], 2000, NG2, 0.05, rr, 21 + sd + int(100 * gm) + int(1000 * t), ALPHA, gm, np.full(ice2.nl, t), 2.0)
            vals.append(es[NG2 // 6:].mean())
        Es.append(float(np.mean(vals)))
    b = np.array(Es) - EX[t][0]
    low = int(np.argmin(Es))
    ok2 &= abs(b[low]) < 0.006 and int(np.sum(np.abs(b) < 0.01)) >= len(GS) - 1
    rows2.append(f"t {t}: biases " + ", ".join(f"{g}:{x:+.4f}" for g, x in zip(GS, b)) + f"; lowest at gam {GS[low]} ({b[low]:+.4f})")
check("full 2^3 torus, 2000 walkers, penalties 0.3-1.1: the lowest projector energy lies within 0.006 of the reference at t = 0.35 and 0.5, "
      "and all but at most one penalty within 0.01", ok2, "; ".join(rows2) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 6^3: population doubling at the minimising penalty
L6 = 4 if DRY else 6
ice6 = Ice(L6); T6 = QTables(ice6)
NG6, TH6 = (400, 100) if DRY else (2000, 400)
res = {}
for nw in (1920, 3840):
    for gm in (1.2, 1.4, 1.6):
        rr = np.random.default_rng(9000 + int(100 * gm) + nw + L6)
        init = loop_vmc(ice6, ALPHA, sweeps=max(40, 1600 // L6), therm=60, r=rr, start=ice6.sector_state(0), fix_winding=True)
        es, vs, ess = q_series(ice6, T6, init, nw, NG6, 0.05, rr, 91 + int(100 * gm) + nw + L6, ALPHA, gm, np.full(ice6.nl, 0.35), 2.0)
        blk = np.array([c.mean() for c in np.array_split(es[TH6:], 8)])
        res[(nw, gm)] = (float(es[TH6:].mean()), float(blk.std(ddof=1) / np.sqrt(8)))
lo1 = min((1.2, 1.4, 1.6), key=lambda g: res[(1920, g)][0])
lo2 = min((1.2, 1.4, 1.6), key=lambda g: res[(3840, g)][0])
drops = {g: res[(1920, g)][0] - res[(3840, g)][0] for g in (1.2, 1.4, 1.6)}
ok3 = lo1 == lo2 == 1.2 and all(d > 0 for d in drops.values()) and drops[1.2] > 0.3
check(f"{L6}^3, t = 0.35: the penalty 1.2 gives the lowest of three energies with 1920 and with 3840 walkers, and doubling the population "
      "lowers the energy at every penalty, by more than 0.3 at the lowest", ok3,
      "; ".join(f"gam {g}: {res[(1920, g)][0]:.3f}+-{res[(1920, g)][1]:.3f} -> {res[(3840, g)][0]:.3f}+-{res[(3840, g)][1]:.3f} (drop {drops[g]:.2f})" for g in (1.2, 1.4, 1.6))
      + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
