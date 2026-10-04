#!/usr/bin/env python3
"""Population dependence of the pair-guide projector energy on the 16^3 ring component (supplied model, nothing adopted).

Setting (all supplied): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law, H = -g sum_p (U_p + U_p^dag), g = 1 (V = 0), restricted to the
connected flip component of the canonical zero-winding state.  A flippable plaquette (circulation +-4) is flipped by U_p.  The projector is a fixed-population (continuous-time,
importance-sampled, resampled every dtau = 0.015) walk with a positive guide psi_T: a walker at sigma flips the flippable plaquette p at rate r_p = psi_T(sigma_p)/psi_T(sigma),
accumulates the log weight -int E_L dt with E_L(sigma) = -sum_p r_p, and the mixed energy estimator sum_w w E_L / sum_w w is exact for any positive guide in the limit of infinite
population and projection time.

Guides.  old: psi_T = exp(0.2 N_flip) (the pair code with gamma = 0).  pair: psi_T = exp(alpha N_flip + gamma N_pair), N_flip = number of flippable plaquettes, N_pair = number of
unordered pairs of flippable plaquettes that share at least one link; alpha 0.35, gamma -0.049.  The change of N_pair under a flip is maintained incrementally (code and
brute-force reference copied from the offset runner this one follows).  u is minus the energy per plaquette; Lc is the population-control correction window in generations
(Lc = 0: plain average); standard errors are 10-bin errors (lower bounds for correlated data).  N_eff = mean_g Var_walkers(E_L) / Var_g(population-mean E_L) over the
post-thermalisation generations (NGEN/4 onward), the population-mean E_L being the unweighted mean over walkers before resampling.

Question: the landed 16^3 results at 960 walkers, seed 1, were old u(Lc=0) = 0.28687 +- 0.00009 and pair u(Lc=0) = 0.28755 +- 0.00007, and the old guide's population series
N_w = 240, 480, 960, 1920 gave 0.28606, 0.28662, 0.28664, 0.28699 (N_eff 9 to 25).  This runner measures the pair guide's own population series, so the two guides'
series can be compared.  The landed numbers enter as the literal reference values LANDED_* below and are not recomputed here.

Runs (16^3, NGEN 2000, therm = NGEN/4, seeds fix the walk and the resampling stream):
 pair guide, seed 1, N_w = 240, 480, 960.
Checks:
 0. pair-guide implementation against brute force on random 4^3 states (E_L, every flippable plaquette's rate, typed pair counts), machine precision.
 1. every run completes with finite u(Lc=0), u(Lc=40), ESS/N_w, N_eff and ancestor fractions (PASS/FAIL).
 2. reported: spread (max minus min) of the pair series next to the spread of the landed old series; the numbers are printed and no conclusion is asserted.
 3. reported: the 960-walker pair run here minus the landed seed-1 pair value (a fresh realisation of the same settings).
Finite diagnostics: estimated values with bin errors; no limit, certification or population convergence is claimed.  The autocorrelation continuation of the landed runner is not
repeated here (it draws extra random numbers, so a seed-1 pair run here is a fresh realisation, not bit-identical to the landed one).  OFF_SMOKE=1 runs a 4^3 version with tiny
populations in about a minute (statistical criteria reported, not asserted).  Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import time

import numba as nb
import numpy as np

AUDIT_TIMEOUT_SEC = 5400

SMOKE = os.environ.get("OFF_SMOKE", "") == "1"
RESULTS = []
T0 = time.time()
DTAU = 0.015
OFFP = 256                                  # index offset of the pair-factor table: dP in [-256, 256]

# Landed reference values (16^3, supplied ring model): literals read from the landed run, not recomputed here.
LANDED_OLD_NW = (240, 480, 960, 1920)       # old guide population series, seed 1, NGEN 2000
LANDED_OLD_U = (0.28606, 0.28662, 0.28664, 0.28699)
LANDED_OLD_UE = (0.00010, 0.00011, 0.00004, 0.00008)
LANDED_S1_OLD = (0.28687, 0.00009)          # 960 walkers, seed 1, old guide through the pair code: u(Lc=0), bin error
LANDED_S1_PAIR = (0.28755, 0.00007)         # 960 walkers, seed 1, pair guide

NCHARS = [0]                                # characters printed so far (stdout budget)


def emit(msg):
    NCHARS[0] += len(msg) + 1
    print(msg, flush=True)


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    emit(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


def log(msg):
    emit(f"   [{time.time() - T0:6.0f} s] {msg}")


# ------------------------------------------------------------------------------------------------ geometry
class Ice:
    """Cubic L^3 torus: links 3 v + a (a = axis), plaquettes 3 v + (0: (0,1), 1: (1,2), 2: (0,2)); A[p] = plaquettes sharing a link with p (p included, padded with N_plaq),
    M[p,j,k] = change coefficient of the circulation of A[p,j] under the flip of link k of p."""
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


def loop_vmc_log(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    """Population start: loop Metropolis with weight |exp(alpha N_flip)|^2 inside the winding sector (acceptance test written log(U) < 2 alpha dN).  A start
    population; the projected energies do not depend on it."""
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
            keep = np.log(r.random()) < 2 * alpha * (after - before)
            if keep and fix_winding and ice.winding_fast(sigma) != W0:
                keep = False
            if keep:
                C[aff] = C_new
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            samples.append(sigma.copy())
    return samples


# ------------------------------------------------------------------------------------------------ random-number seeding for the jit kernels
@nb.njit(cache=False)
def nb_seed(s):
    np.random.seed(s)


# ------------------------------------------------------------------------------------------------ pair-guide structure
def plaquette_orientation(ice):
    ax = ice.axis[ice.plaq]
    ids = {}
    out = np.zeros(ice.np_, dtype=np.int64)
    for p in range(ice.np_):
        out[p] = ids.setdefault(tuple(sorted(set(int(a) for a in ax[p]))), len(ids))
    assert len(ids) == 3
    return out


def pair_scheme(scheme):
    if scheme == "one":
        return 1, (lambda o1, o2: 0)
    if scheme == "SD":
        return 2, (lambda o1, o2: 0 if o1 == o2 else 1)
    if scheme == "orient6":
        pairs = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
        return 6, (lambda o1, o2: pairs.index((min(o1, o2), max(o1, o2))))
    raise ValueError(scheme)


def build_pairs(ice, A, scheme):
    """ptype[p,j]: pair type of (p, A[p,j]) (-1 for p itself / padding); adjm[p,j1,j2]: type + 1 if A[p,j1], A[p,j2] are distinct adjacent plaquettes else 0."""
    Np, W = A.shape
    nt, tfun = pair_scheme(scheme)
    orient = plaquette_orientation(ice)
    nbr = [set(int(q) for q in A[p] if q >= 0 and q != p) for p in range(Np)]
    ptype = np.full((Np, W), -1, dtype=np.int64)
    adjm = np.zeros((Np, W, W), dtype=np.int8)
    for p in range(Np):
        for j in range(W):
            q = int(A[p, j])
            if q >= 0 and q != p:
                ptype[p, j] = tfun(orient[p], orient[q])
        for j1 in range(W):
            q1 = int(A[p, j1])
            if q1 < 0 or q1 == p:
                continue
            for j2 in range(W):
                q2 = int(A[p, j2])
                if q2 < 0 or q2 == p or q2 == q1:
                    continue
                if q2 in nbr[q1]:
                    adjm[p, j1, j2] = tfun(orient[q1], orient[q2]) + 1
    return nt, ptype, adjm

class Brute:
    """Direct references: adjacency from link sets (independent of the neighbour tables), psi_T of each flipped state evaluated non-incrementally."""
    def __init__(self, ice, alpha, gammas, scheme):
        self.ice, self.alpha = ice, alpha
        self.gam = np.asarray(gammas, dtype=float)
        nt, tfun = pair_scheme(scheme)
        self.nt = nt
        ls = [set(int(l) for l in ice.plaq[p]) for p in range(ice.np_)]
        key = [tuple(sorted(set(int(a) for a in ice.axis[ice.plaq[p]]))) for p in range(ice.np_)]
        ids = {}
        ori = [ids.setdefault(k, len(ids)) for k in key]
        P1, P2, PT = [], [], []
        for p in range(ice.np_):
            for q in range(p + 1, ice.np_):
                if ls[p] & ls[q]:
                    P1.append(p); P2.append(q); PT.append(tfun(ori[p], ori[q]))
        self.P1, self.P2, self.PT = np.array(P1), np.array(P2), np.array(PT)
        assert len(self.gam) == nt

    def counts(self, sigma):
        F = (np.abs(self.ice.circ(sigma)[:self.ice.np_]) == 4)
        return int(F.sum()), np.bincount(self.PT[F[self.P1] & F[self.P2]], minlength=self.nt)

    def logpsi(self, sigma):
        nf, npair = self.counts(sigma)
        return self.alpha * nf + float(self.gam @ npair)

    def rates(self, sigma):
        C = self.ice.circ(sigma)[:self.ice.np_]
        l0 = self.logpsi(sigma)
        out = {}
        for p in np.flatnonzero(np.abs(C) == 4):
            s2 = sigma.copy()
            s2[self.ice.plaq[p]] *= -1
            out[int(p)] = np.exp(self.logpsi(s2) - l0)
        return out


# ------------------------------------------------------------------------------------------------ pair-guide kernels
@nb.njit(cache=False)
def _dNP(s, mtab, A, adjm, C, flp, nn, dP, Sj, Sa):
    """Change dn of N_flip and change dP[t] of the typed pair counts if the flippable plaquette s is flipped (state C, flp, nn of one walker).  For flippable s every link has
    sigma_l sign_l = C_s/4, so the circulation of neighbour A[s,j] changes by -(C_s/2) mtab[s,j], mtab[s,j] = sum_k M[s,j,k] sign[s,k]."""
    nt = dP.shape[0]
    W = A.shape[1]
    for t in range(nt):
        dP[t] = 0
    dn = 0
    nS = 0
    for j in range(W):
        q = A[s, j]
        if q < 0:
            break
        if q == s:
            continue
        cn = np.int64(C[q]) - (np.int64(C[s]) // 2) * mtab[s, j]
        nf = (cn == 4 or cn == -4)
        if nf != flp[q]:
            a = 1 if nf else -1
            dn += a
            Sj[nS] = j
            Sa[nS] = a
            nS += 1
            for t in range(nt):
                dP[t] += a * nn[q, t]
    for i1 in range(nS):
        for i2 in range(i1 + 1, nS):
            tp = adjm[s, Sj[i1], Sj[i2]]
            if tp > 0:
                dP[tp - 1] += Sa[i1] * Sa[i2]
    return dn


@nb.njit(cache=False)
def nb_init_p(sig, C, flp, nn, nflp, npair, rate0, plaq, sign, A, ptype, adjm, mtab, exptabN, exptabP):
    n_w, Np = C.shape
    nt = nn.shape[2]
    W = A.shape[1]
    dPs = np.zeros(nt, np.int64)
    Sj = np.zeros(W, np.int64)
    Sa = np.zeros(W, np.int64)
    for i in range(n_w):
        cnt = 0
        for q in range(Np):
            c = 0
            for k in range(4):
                c += sig[i, plaq[q, k]] * sign[q, k]
            C[i, q] = c
            f = (c == 4 or c == -4)
            flp[i, q] = f
            cnt += 1 if f else 0
        nflp[i] = cnt
        for q in range(Np):
            for t in range(nt):
                nn[i, q, t] = 0
        for t in range(nt):
            npair[i, t] = 0
        for q in range(Np):
            for j in range(W):
                r = A[q, j]
                if r < 0:
                    break
                if r != q and flp[i, r]:
                    nn[i, q, ptype[q, j]] += 1
                    if flp[i, q] and r > q:
                        npair[i, ptype[q, j]] += 1
        for s in range(Np):
            if flp[i, s]:
                dn = _dNP(s, mtab, A, adjm, C[i], flp[i], nn[i], dPs, Sj, Sa)
                x = exptabN[dn + 16]
                for t in range(nt):
                    x *= exptabP[t, dPs[t] + OFFP]
                rate0[i, s] = x
            else:
                rate0[i, s] = 0.0


@nb.njit(cache=False)
def nb_walk_p(sig, C, flp, nn, rate0, nflp, npair, plaq, A, ptype, adjm, mtab, exptabN, exptabP, V, dtau,
              stampQ, stampS, tick, sbuf, rbuf, qbuf, logw, ELend):
    """Guided jump process with rates r_s = exp(alpha dN_s + sum_t gamma_t dP_{s,t}) for flippable s (rate0 holds them), block sums of 64 plaquettes for the selection."""
    n_w, Np = C.shape
    W = A.shape[1]
    nt = nn.shape[2]
    nblk = (Np + 63) // 64
    R_ = np.zeros(nblk)
    dPs = np.zeros(nt, np.int64)
    Sj = np.zeros(W, np.int64)
    Sa = np.zeros(W, np.int64)
    cnew = np.zeros(W, np.int64)
    Spq = np.zeros(W, np.int64)
    Spa = np.zeros(W, np.int64)
    for i in range(n_w):
        s_ = sig[i]; C_ = C[i]; f_ = flp[i]; n_ = nn[i]; r_ = rate0[i]
        for b in range(nblk):
            R_[b] = 0.0
        for s in range(Np):
            if f_[s]:
                R_[s // 64] += r_[s]
        t = 0.0
        lw = 0.0
        while True:
            lam = 0.0
            for b in range(nblk):
                if R_[b] > 0.0:
                    lam += R_[b]
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
            cs = -1
            clast = -1
            for b in range(nblk):
                w = R_[b]
                if w > 0.0:
                    clast = b
                    if acc + w > u:
                        cs = b
                        break
                    acc += w
            if cs < 0:
                cs = clast
                acc = 0.0
            p = -1
            if cs >= 0:
                u2 = u - acc
                a2 = 0.0
                lo = cs * 64
                hi = min(lo + 64, Np)
                for s in range(lo, hi):
                    if f_[s]:
                        a2 += r_[s]
                        p = s
                        if a2 > u2:
                            break
            if p < 0:                       # unreachable unless the block sums are inconsistent; fail loudly rather than wrap
                lw = np.nan
                ELend[i] = np.nan
                break
            tick[0] += 1
            tk = tick[0]
            # new circulations on A[p] and the set S_p of plaquettes whose flippability toggles
            nSp = 0
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                cn = np.int64(C_[q]) - (np.int64(C_[p]) // 2) * mtab[p, j]
                cnew[j] = cn
                if q != p:
                    newf = (cn == 4 or cn == -4)
                    if newf != f_[q]:
                        Spq[nSp] = q
                        Spa[nSp] = 1 if newf else -1
                        nSp += 1
            # plaquettes whose rate must be refreshed: s in A[q], q in Q = A[p] u A[u] (u in S_p)
            nQ = 0
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                if stampQ[q] != tk:
                    stampQ[q] = tk
                    qbuf[nQ] = q
                    nQ += 1
            for iu in range(nSp):
                u_ = Spq[iu]
                for j in range(W):
                    q = A[u_, j]
                    if q < 0:
                        break
                    if stampQ[q] != tk:
                        stampQ[q] = tk
                        qbuf[nQ] = q
                        nQ += 1
            nB = 0
            for iq in range(nQ):
                q = qbuf[iq]
                for j in range(W):
                    s = A[q, j]
                    if s < 0:
                        break
                    if stampS[s] != tk:
                        stampS[s] = tk
                        sbuf[nB] = s
                        rbuf[nB] = r_[s]
                        nB += 1
            # pair counts of the walker change by dP[p] (evaluated on the state before the flip)
            _dNP(p, mtab, A, adjm, C_, f_, n_, dPs, Sj, Sa)
            for tt in range(nt):
                npair[i, tt] += dPs[tt]
            for j in range(W):
                q = A[p, j]
                if q < 0:
                    break
                cn = cnew[j]
                oldf = f_[q]
                C_[q] = cn
                newf = (cn == 4 or cn == -4)
                f_[q] = newf
                nflp[i] += (1 if newf else 0) - (1 if oldf else 0)
            for iu in range(nSp):
                u_ = Spq[iu]
                for j in range(W):
                    r = A[u_, j]
                    if r < 0:
                        break
                    if r != u_:
                        n_[r, ptype[u_, j]] += Spa[iu]
            for k in range(4):
                l = plaq[p, k]
                s_[l] = -s_[l]
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    dn = _dNP(s, mtab, A, adjm, C_, f_, n_, dPs, Sj, Sa)
                    rn = exptabN[dn + 16]
                    for tt in range(nt):
                        rn *= exptabP[tt, dPs[tt] + OFFP]
                else:
                    if rbuf[jj] <= 0.0:
                        continue                       # was not flippable and is not: nothing stored changes
                    rn = 0.0
                r_[s] = rn
                b = s // 64
                if rbuf[jj] > 0.0:
                    R_[b] -= rbuf[jj]
                    if R_[b] < 1e-9:
                        R_[b] = 0.0
                if f_[s]:
                    R_[b] += rn
        logw[i] = lw


_PAIR_CACHE = {}


class PProjector:
    """Fixed-population projector, guide exp(alpha N_flip + sum_t gamma_t N_pair,t).  Tables per (torus, scheme) are cached."""
    KEYS = ("sig", "C", "flp", "nn", "nflp", "npair", "rate0")

    def __init__(self, ice, alpha, gammas, scheme="one", V=0.0, seed=1):
        self.ice, self.alpha, self.V = ice, alpha, V
        self.plaq = ice.plaq.astype(np.int64)
        self.sign = ice.sign.astype(np.int64)
        A = ice.A.astype(np.int64).copy()
        A[A == ice.np_] = -1
        self.A = A
        key = (ice.L, scheme)
        if key not in _PAIR_CACHE:
            nt, ptype, adjm = build_pairs(ice, A, scheme)
            M = np.rint(ice.M).astype(np.int64)
            _PAIR_CACHE[key] = (nt, ptype, adjm, np.ascontiguousarray(np.einsum("pjk,pk->pj", M, self.sign)))
        self.nt, self.ptype, self.adjm, self.mtab = _PAIR_CACHE[key]
        self.gam = np.broadcast_to(np.asarray(gammas, dtype=float), (self.nt,)).copy()
        self.exptabN = np.exp(alpha * (np.arange(33) - 16.0))
        self.exptabP = np.exp(self.gam[:, None] * (np.arange(2 * OFFP + 1)[None, :] - OFFP))
        self.stampQ = np.zeros(ice.np_, dtype=np.int64)
        self.stampS = np.zeros(ice.np_, dtype=np.int64)
        self.tick = np.zeros(1, dtype=np.int64)
        self.sbuf = np.zeros(ice.np_ + 16, dtype=np.int64)
        self.rbuf = np.zeros(ice.np_ + 16)
        self.qbuf = np.zeros(ice.np_ + 16, dtype=np.int64)
        nb_seed(seed)

    def _walk(self, st, dtau, logw, ELend):
        nb_walk_p(st["sig"], st["C"], st["flp"], st["nn"], st["rate0"], st["nflp"], st["npair"], self.plaq, self.A, self.ptype, self.adjm, self.mtab,
                  self.exptabN, self.exptabP, self.V, dtau, self.stampQ, self.stampS, self.tick, self.sbuf, self.rbuf, self.qbuf, logw, ELend)

    def state_from_sigma(self, sig):
        Np = self.ice.np_
        n_w = len(sig)
        st = dict(sig=np.ascontiguousarray(sig.astype(np.int8)), C=np.zeros((n_w, Np), dtype=np.int8), flp=np.zeros((n_w, Np), dtype=np.bool_),
                  nn=np.zeros((n_w, Np, self.nt), dtype=np.int8), nflp=np.zeros(n_w, dtype=np.int64), npair=np.zeros((n_w, self.nt), dtype=np.int64),
                  rate0=np.zeros((n_w, Np)))
        nb_init_p(st["sig"], st["C"], st["flp"], st["nn"], st["nflp"], st["npair"], st["rate0"], self.plaq, self.sign, self.A, self.ptype, self.adjm,
                  self.mtab, self.exptabN, self.exptabP)
        return st

    def make_state(self, init, n_w, rng):
        picks0 = rng.integers(len(init), size=n_w)
        return self.state_from_sigma(np.array([init[k] for k in picks0], dtype=np.int8))

    def run(self, init, n_w, n_gen, dtau, therm, lags, rng):
        """Per generation: advance, record mixed energy, log mean weight, effective sample fraction, spread of walker log weights, unweighted mean and sd of E_L,
        ancestor fractions at `lags` generations (after thermalisation), then resample (systematic)."""
        st = self.make_state(init, n_w, rng)
        Lmax = max(lags) if len(lags) else 0
        anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
        logw = np.zeros(n_w)
        ELend = np.zeros(n_w)
        out = dict(e=[], lwbar=[], ess=[], lwsd=[], hops=[], nd=[], elsd=[], elmean=[], nflp=[], npair=[])
        t_start = time.time()
        for g in range(n_gen):
            tk0 = int(self.tick[0])
            self._walk(st, dtau, logw, ELend)
            out["hops"].append(int(self.tick[0]) - tk0)
            mx = logw.max()
            w = np.exp(logw - mx)
            Wt = w.sum()
            wn = w / Wt
            out["lwbar"].append(mx + np.log(Wt / n_w))
            out["e"].append(float(wn @ ELend))
            out["ess"].append(float(Wt ** 2 / (w ** 2).sum() / n_w))
            out["lwsd"].append(float(logw.std()))
            out["elsd"].append(float(ELend.std()))
            out["elmean"].append(float(ELend.mean()))
            if Lmax:
                anc[:, g % (Lmax + 1)] = np.arange(n_w)
            if g >= therm:
                out["nflp"].append(float(wn @ (st["nflp"] / self.ice.np_)))
                out["npair"].append(wn @ (st["npair"] / self.ice.np_))
                if Lmax:
                    out["nd"].append([len(np.unique(anc[:, (g - L) % (Lmax + 1)])) / n_w for L in lags])
            cum = np.cumsum(wn)
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
            for key in self.KEYS:
                st[key] = st[key][picks]
            anc = anc[picks]
        res = {k: np.array(v) for k, v in out.items()}
        res["therm"] = therm
        res["wall"] = time.time() - t_start
        return res


# ------------------------------------------------------------------------------------------------ estimators
def corrected(res, Lc, which="e"):
    """Population-control-corrected average: weight generation n by prod_{j=n-Lc+1..n} wbar_j (Lc = 0: plain average) over the post-thermalisation generations."""
    th = res["therm"]
    lw = res["lwbar"]
    n = len(lw)
    cs = np.concatenate([[0.0], np.cumsum(lw)])
    idx = np.arange(th, n)
    logG = cs[idx + 1] - cs[np.maximum(idx + 1 - Lc, 0)] if Lc > 0 else np.zeros(len(idx))
    G = np.exp(logG - logG.max())
    return float((G @ res[which][th:]) / G.sum())


def energy_summary(res, Lcs=(0, 40)):
    """Mixed energy (corrected with window Lc) and 10-bin error."""
    th = res["therm"]
    out = {}
    n = len(res["e"]) - th
    cs = np.concatenate([[0.0], np.cumsum(res["lwbar"])])
    for Lc in Lcs:
        est = corrected(res, Lc, "e")
        vals = []
        for c in np.array_split(np.arange(n), 10):
            idx = th + c
            logG = cs[idx + 1] - cs[np.maximum(idx + 1 - Lc, 0)] if Lc > 0 else np.zeros(len(idx))
            G = np.exp(logG - logG.max())
            vals.append(float(G @ res["e"][idx] / G.sum()))
        out[Lc] = (est, float(np.std(vals, ddof=1) / np.sqrt(10)))
    return out


# ------------------------------------------------------------------------------------------------ checks
def check_1a():
    """Pair-guide implementation against brute force on random 4^3 states (E_L, per-plaquette rates, typed pair counts, flippable counts)."""
    ice = Ice(4)
    cases = [("one", [0.07], 0.0), ("SD", [0.05, -0.08], 0.0), ("orient6", [0.03, -0.02, 0.06, 0.04, -0.05, 0.01], 0.3)]
    worst_el = worst_rate = 0.0
    worst_cnt = 0
    nhop = 0
    for scheme, gam, V in cases:
        rr = np.random.default_rng(7)
        init = loop_vmc_log(ice, 0.2, sweeps=40, therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = PProjector(ice, 0.2, gam, scheme, V=V, seed=5)
        br = Brute(ice, 0.2, gam, scheme)
        n_w = 24
        st = pr.make_state(init, n_w, rr)
        logw = np.zeros(n_w)
        EL = np.zeros(n_w)
        for call in range(6):
            pr._walk(st, 0.2, logw, EL)
            for i in range(n_w):
                sg = st["sig"][i].astype(int)
                rb = br.rates(sg)
                elb = V * len(rb) - sum(rb.values())
                worst_el = max(worst_el, abs(EL[i] - elb) / abs(elb))
                nf, npc = br.counts(sg)
                worst_cnt = max(worst_cnt, int(np.abs(npc - st["npair"][i]).max()), abs(nf - int(st["nflp"][i])))
                flp_idx = np.flatnonzero(st["flp"][i])
                assert set(rb.keys()) == set(int(x) for x in flp_idx)
                worst_rate = max(worst_rate, max(abs(st["rate0"][i][p] - rb[p]) / rb[p] for p in rb))
        nhop += int(pr.tick[0])
    check("check 0: pair guide on random 4^3 states: E_L, per-plaquette rates and typed N_pair, N_flip against brute force (schemes one, SD, orient6)",
          worst_el < 1e-12 and worst_rate < 1e-12 and worst_cnt == 0,
          f"{nhop} hops; max rel |E_L - brute| {worst_el:.2e}; max rel |rate - psi ratio| {worst_rate:.2e}; max integer difference of N_pair,t and N_flip {worst_cnt} (E_L and rates: float, tolerance 1e-12)")



# ------------------------------------------------------------------------------------------------ one run
def guide_run(ice, NW, seed, NGEN, alpha, gamma, tag=""):
    """One run (gamma = 0: the old guide through the same code): summary dict.  Initial population from the alpha-guide loop Metropolis; a two-generation warm-up population of
    8 walkers triggers the compilation before the run.  N_eff = mean_g Var_walkers(E_L) / Var_g(population-mean E_L), generations >= NGEN/4."""
    t0 = time.time()
    L = ice.L
    rr = np.random.default_rng(seed * 100 + L + NW)
    init = loop_vmc_log(ice, alpha, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    pr = PProjector(ice, alpha, [gamma], "one", seed=seed)
    pr.run(init, 8, 2, DTAU, 1, [], rr)
    therm = NGEN // 4
    lags = [max(1, int(round(t / DTAU))) for t in (1.0, 2.0)]
    res = pr.run(init, NW, NGEN, DTAU, therm, lags, rr)
    es = energy_summary(res, Lcs=(0, 40))
    Np = ice.np_
    nd = res["nd"].mean(axis=0)
    neff = float(np.mean(res["elsd"][therm:] ** 2) / np.var(res["elmean"][therm:]))
    d = dict(tag=tag, nw=NW, seed=seed, u0=-es[0][0] / Np, u0e=es[0][1] / Np, u40=-es[40][0] / Np, u40e=es[40][1] / Np, ess=float(res["ess"][therm:].mean()), neff=neff,
             nd1=float(nd[0]), nd2=float(nd[1]), elsd=float(res["elsd"][therm:].mean()), wall=time.time() - t0)
    log(f"{tag} L {L} N_w {NW:4d} seed {seed} NGEN {NGEN} alpha {alpha} gamma {gamma}: u(Lc=0) {d['u0']:.5f}+-{d['u0e']:.5f}; u(Lc=40) {d['u40']:.5f}+-{d['u40e']:.5f}; "
        f"ESS/N_w {d['ess']:.4f}; N_eff {d['neff']:.1f}; nd@1.0 {d['nd1']:.4f}; nd@2.0 {d['nd2']:.4f}; sd(E_L) {d['elsd']:.2f}; {d['wall']:.0f} s")
    return d


# ------------------------------------------------------------------------------------------------ checks
def check_series():
    L, NGEN = (4, 600) if SMOKE else (16, 2000)
    nws = (30, 60, 120) if SMOKE else (240, 480, 960)
    ice = Ice(L)
    pair = [guide_run(ice, nw, 1, NGEN, 0.35, -0.049, tag="pair") for nw in nws]
    runs = pair

    keys = ("u0", "u0e", "u40", "u40e", "ess", "neff", "nd1", "nd2", "elsd")
    finite = bool(all(np.isfinite([r[k] for r in runs for k in keys])))
    check(f"check 1: all {len(runs)} runs on {L}^3 completed with finite u(Lc=0), u(Lc=40), ESS/N_w, N_eff and ancestor fractions", finite,
          f"pair seed 1 N_w {nws}; run time {sum(r['wall'] for r in runs):.0f} s")

    up = np.array([r["u0"] for r in pair])
    upe = np.array([r["u0e"] for r in pair])
    sp_pair = float(up.max() - up.min())
    uo = np.array(LANDED_OLD_U)
    sp_old4 = float(uo.max() - uo.min())
    sp_old3 = float(uo[:3].max() - uo[:3].min())
    note = " (smoke: the landed values are the 16^3 ones)" if SMOKE else ""
    check("check 2: spread (max minus min) of the pair-guide u(Lc=0) series next to the landed old-guide series (reported; no conclusion asserted)" + note,
          bool(np.isfinite(sp_pair)),
          f"pair, seed 1, N_w {list(nws)}: u {', '.join(f'{x:.5f}' for x in up)}, bin errors {', '.join(f'{x:.5f}' for x in upe)}, spread {sp_pair:.5f}, "
          f"u(N_w {nws[-1]}) - u(N_w {nws[0]}) {up[-1] - up[0]:+.5f}; "
          f"landed old, seed 1, N_w {list(LANDED_OLD_NW)}: u {', '.join(f'{x:.5f}' for x in LANDED_OLD_U)}, bin errors {', '.join(f'{x:.5f}' for x in LANDED_OLD_UE)}, "
          f"spread {sp_old4:.5f} (first three N_w: {sp_old3:.5f}), u(960) - u(240) {LANDED_OLD_U[2] - LANDED_OLD_U[0]:+.5f}; "
          f"spread ratio pair/old {sp_pair / sp_old3:.2f} (first three N_w), {sp_pair / sp_old4:.2f} (all four)")

    rr_d = pair[-1]["u0"] - LANDED_S1_PAIR[0]
    rr_z = rr_d / float(np.hypot(pair[-1]["u0e"], LANDED_S1_PAIR[1]))
    note3 = " (smoke: the landed value is the 16^3 one)" if SMOKE else ""
    check("check 3: the largest-population pair run here minus the landed seed-1 pair value at 960 walkers (reported; a fresh realisation of the same settings)" + note3,
          bool(np.isfinite(rr_d)),
          f"pair N_w {nws[-1]}: {pair[-1]['u0']:.5f}+-{pair[-1]['u0e']:.5f} vs landed {LANDED_S1_PAIR[0]:.5f}+-{LANDED_S1_PAIR[1]:.5f}: {rr_d:+.5f} ({rr_z:+.1f} combined se); "
          f"landed old at 960 through the pair code {LANDED_S1_OLD[0]:.5f}+-{LANDED_S1_OLD[1]:.5f}")


def main():
    emit(f"pseries_runner: {'SMOKE' if SMOKE else 'FULL'} mode")
    check_1a()
    check_series()
    n_pass = sum(RESULTS)
    emit(f"elapsed {time.time() - T0:.0f} s; stdout {NCHARS[0]} characters before this line")
    emit(f"TOTAL: PASS={n_pass} FAIL={len(RESULTS) - n_pass}")


if __name__ == "__main__":
    main()
