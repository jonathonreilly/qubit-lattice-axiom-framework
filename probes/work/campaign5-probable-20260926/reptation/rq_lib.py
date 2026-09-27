import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import numba as nb
import numpy as np
ALPHA = 0.2


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




# ---------------------------------------------------------------- reptation kernels: one path, two end states (0 = tail, 1 = head)
@nb.njit(cache=False)
def rq_apply(e, ev, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl, gam, bl, gg,
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
            s_[l] = -s_[l]
            for j in range(4):
                q = pol4[l, j]
                if cstamp[q] != tk:
                    cstamp[q] = tk; cbuf[nC] = q; nC += 1
    else:
        l = ev - Np
        sv = s_[l]
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
def rq_grow(e, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl,
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
        EL = Mq * sq2[e] - lam
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
        rq_apply(e, ev, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab, tl, gam, bl, gg,
                 stamp, tick, cbuf, cstamp)


@nb.njit(cache=False)
def rq_copy(src, dst, sig, C, flp, Q, nflp, sq2, rate, bs):
    sig[dst, :] = sig[src, :]; C[dst, :] = C[src, :]; flp[dst, :] = flp[src, :]; Q[dst, :] = Q[src, :]
    nflp[dst] = nflp[src]; sq2[dst] = sq2[src]; rate[dst, :] = rate[src, :]; bs[dst, :] = bs[src, :]


@nb.njit(cache=False)
def rq_run(nmoves, dur, meas_every, wlo, whi, segE, segN, segW, pos, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols,
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
        rq_copy(lead, lead + 2, sig, C, flp, Q, nflp, sq2, rate, bs)
        W, n, over = rq_grow(lead, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
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
                    rq_apply(0, segE[old, i], sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, stamp, tick, cbuf, cstamp)
                slot = old                                   # the freed slot becomes the new head segment
                for i in range(n):
                    segE[slot, i] = evbuf[i]
                segN[slot] = n; segW[slot] = W
                start = (start + 1) % Mcap
            else:
                # remove the head segment: undo its events in reverse path order on the head state
                for i in range(segN[old] - 1, -1, -1):
                    rq_apply(1, segE[old, i], sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, stamp, tick, cbuf, cstamp)
                slot = old                                   # the freed slot becomes the new tail segment (path order = reversed growth)
                for i in range(n):
                    segE[slot, i] = evbuf[n - 1 - i]
                segN[slot] = n; segW[slot] = W
                start = (start - 1) % Mcap
            stats[0] += 1
        else:
            rq_copy(lead + 2, lead, sig, C, flp, Q, nflp, sq2, rate, bs)
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
            el0 = Mq * sq2[0]; el1 = Mq * sq2[1]
            for b in range(bs.shape[1]):
                el0 -= bs[0, b]; el1 -= bs[1, b]
            out[nout, 0] = nl_ev; out[nout, 1] = np_ev; out[nout, 2] = el0; out[nout, 3] = el1
            nout += 1
            for i in range(Mseg):
                sl = (start + i) % Mcap
                c_l = 0
                for k in range(segN[sl]):
                    if segE[sl, k] >= Np:
                        c_l += 1
                prof[i] += c_l
    pos[0] = start; pos[2] = d
    return nout


@nb.njit(cache=False)
def rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head, exptab,
             tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp):
    """Grow the initial path at the head from the common start state; returns the number of overflowing segments."""
    kmax = segE.shape[1]
    evbuf = np.zeros(kmax, dtype=np.int32)
    bad = 0
    for i in range(Mseg):
        W, n, over = rq_grow(1, dur, evbuf, kmax, sig, C, flp, Q, nflp, sq2, rate, bs, plaq, sign, A, M, dynf, pol4, pols, inc6, tail, head,
                             exptab, tl, gam, bl, gg, Mq, stamp, tick, cbuf, cstamp)
        if over:
            bad += 1
        for k in range(n):
            segE[i, k] = evbuf[k]
        segN[i] = n; segW[i] = W
    return bad


def reptation(ice, T, start_sig, t, gam, Mq, Mseg, dur, nmoves, therm_moves, meas_every, window, seed, kmax=512, chunk=20000, alpha=0.2):
    """One reptation chain. Returns per-measurement arrays: link and plaquette events in the middle window, E_L at both ends,
    and move statistics. window = number of middle segments counted."""
    nb_seed(seed)
    nl, npl, nv = ice.nl, ice.np_, ice.nv
    ne = npl + nl
    nblk = (ne + 63) // 64
    sig = np.array([start_sig] * 4, dtype=np.int64)
    C = np.zeros((4, npl), dtype=np.int64); flp = np.zeros((4, npl), dtype=np.bool_); Q = np.zeros((4, nv), dtype=np.int64)
    nflp = np.zeros(4, dtype=np.int64); sq2 = np.zeros(4, dtype=np.int64); Fh = np.zeros(4); rate = np.zeros((4, ne)); bs = np.zeros((4, nblk))
    dynf = np.ones(npl, dtype=np.bool_); tl = np.full(nl, t); z = np.zeros(nl)
    exptab = np.exp(alpha * (np.arange(33) - 16.0))
    q_init(sig, C, flp, Q, nflp, sq2, Fh, rate, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6, T.incs6, T.tail, T.head, exptab, tl, gam, z, z, 1.0)
    for e in range(4):
        rq_resum(e, rate, bs)
    stamp = np.zeros(ne, dtype=np.int64); cstamp = np.zeros(npl, dtype=np.int64); tick = np.zeros(1, dtype=np.int64); cbuf = np.zeros(64, dtype=np.int64)
    segE = np.zeros((Mseg, kmax), dtype=np.int32); segN = np.zeros(Mseg, dtype=np.int32); segW = np.zeros(Mseg)
    bad = rq_build(Mseg, dur, segE, segN, segW, sig, C, flp, Q, nflp, sq2, rate, bs, T.plaq, T.sign, T.A, T.M, dynf, T.pol4, T.pols, T.inc6,
                   T.tail, T.head, exptab, tl, gam, z, 1.0, Mq, stamp, tick, cbuf, cstamp)
    pos = np.array([0, Mseg, 1], dtype=np.int64)
    wlo = (Mseg - window) // 2; whi = wlo + window
    stats = np.zeros(3, dtype=np.int64)
    prof = np.zeros(Mseg)
    rows = []
    done = 0
    total = therm_moves + nmoves
    while done < total:
        nm = min(chunk, total - done)
        out = np.zeros((nm // meas_every + 1, 4))
        k = rq_run(nm, dur, meas_every, wlo, whi, segE, segN, segW, pos, sig, C, flp, Q, nflp, sq2, rate, bs, T.plaq, T.sign, T.A, T.M, dynf,
                   T.pol4, T.pols, T.inc6, T.tail, T.head, exptab, tl, gam, z, 1.0, Mq, stamp, tick, cbuf, cstamp, out, stats, prof)
        for e in range(2):
            rq_resum(e, rate, bs)
        if done >= therm_moves:
            rows.append(out[:k])
        else:
            prof[:] = 0.0
        done += nm
    return (np.concatenate(rows) if rows else np.zeros((0, 4))), stats, bad, prof
