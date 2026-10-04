#!/usr/bin/env python3
"""Guide dependence of the fixed-population projector's finite-torus energy offset, ring component (supplied model, nothing adopted).

Setting (all supplied): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law, H = -g sum_p (U_p + U_p^dag), g = 1 (V = 0), restricted to the
connected flip component of the canonical zero-winding state (the same component as the landed ring-component notes).  A flippable plaquette (circulation +-4) is flipped by U_p.
The projector is a fixed-population (continuous-time, importance-sampled, resampled every dtau = 0.015) walk with a positive guide psi_T:
a walker at sigma flips the flippable plaquette p at rate r_p = psi_T(sigma_p)/psi_T(sigma), accumulates the log weight -int E_L dt with E_L(sigma) = -sum_p r_p, and the
mixed energy estimator sum_w w E_L / sum_w w is EXACT for ANY positive guide in the limit of infinite population and projection time.

Guides.  old: psi_T = exp(0.2 N_flip) (N_flip = number of flippable plaquettes).  pair: psi_T = exp(alpha N_flip + sum_t gamma_t N_pair,t), N_pair,t = number of unordered
pairs of flippable plaquettes that share at least one link (adjacent), pair types t: 'one' (all pairs), 'SD' (same orientation = coplanar neighbours / different orientation) or
'orient6' (the six orientation pairs).  The change of N_pair under a flip is maintained incrementally: with F_u the flippability indicator and n[q,t] the number of flippable
neighbours of q of pair type t, flipping a flippable s toggles F_q (a_q = +-1) on the set S_s of neighbours whose |circulation| enters or leaves 4, and
dP_{s,t} = sum_{q in S_s} a_q n[q,t] + sum over adjacent pairs {q,q'} in S_s of type t of a_q a_q' (F'_u F'_v - F_u F_v = a_u F_v + a_v F_u + a_u a_v).

Checks (all floating-point Monte Carlo unless stated; no certified or exact claim beyond the integer N_pair identity and the machine-precision brute-force comparison):
 (1) pair-guide implementation: E_L, every flippable plaquette's rate and the typed pair counts against brute-force evaluation (from-scratch psi_T of each flipped state, adjacency from
     link sets independently of the neighbour tables) on random 4^3 states, machine precision; the projected energy on the exact 2^3 component (exact diagonalisation) for two pair
     guides within 3 standard errors of eight independent runs; population scaling of the 2^3 offset for a stronger gamma (reported).
 (2) 8^3, 960 walkers, 2 seeds: old vs pair guide (alpha 0.35, gamma -0.049): u(Lc=0), u(Lc=40), distinct ancestors at projection-time lags 1.0 and 2.0 (67 and 133 generations),
     walker-level sd(E_L); PASS if both run and the pair guide's lag-2 ancestor fraction exceeds the old guide's.
 (3) 16^3, 960 walkers, seed 1: old vs pair guide u(Lc=0), u(Lc=40), ancestors, sd(E_L); PASS if the two u(Lc=0) differ by more than 4 combined standard errors, i.e. the converged
     mixed energy would be guide independent but the finite-population estimate is not.  u is minus the energy per plaquette; Lc is the population-control correction window in
     generations (Lc = 0: plain average); standard errors are 10-bin errors.
 (4) 16^3 old guide, N_w = 240, 480, 960, 1920 (seed 1, 2000 generations): u(Lc=0), effective sample fraction, Nemec N_eff = mean_g Var_walkers(E_L) / Var_g(population-mean E_L)
     over generations 500..1999, and a fit u = u_inf - c N_w^-k (profile over k; u_inf is reported, not asserted).
Finite diagnostics: estimated values with bin errors, one seed unless stated, no limit, certification or population convergence is claimed.  OFF_SMOKE=1 runs a 4^3/6^3 version
(tiny populations, statistical criteria reported but not asserted) in about a minute.  Prints TOTAL: PASS=N FAIL=M.
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

AUDIT_TIMEOUT_SEC = 7200

SMOKE = os.environ.get("OFF_SMOKE", "") == "1"
RESULTS = []
T0 = time.time()
ALPHA, DTAU = 0.2, 0.015
OFFP = 256                                  # index offset of the pair-factor table: dP in [-256, 256]


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def log(msg):
    print(f"   [{time.time() - T0:6.0f} s] {msg}", flush=True)


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


def loop_vmc(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    """Population start: loop Metropolis with weight |exp(alpha N_flip)|^2 inside the winding sector (a start only; projected energies do not depend on it)."""
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


def loop_vmc_log(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    """As loop_vmc with the acceptance test written log(U) < 2 alpha dN (the form of the pair-guide scans; same random draws)."""
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


def exact_L2(ice, canon):
    """Exact flip-component Hamiltonian on the 2^3 torus (all 2^24 link assignments filtered by the vertex Gauss law, then the component of `canon`)."""
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    n = 1 << ice.nl
    step = 1 << 18
    codes = []
    for start in range(0, n, step):
        ids = np.arange(start, min(n, start + step), dtype=np.int64)
        sig = (((ids[:, None] >> bits) & 1) * 2 - 1).astype(np.int64)
        codes.append(ids[np.all(sig @ B.T == 0, axis=1)])
    codes = np.concatenate(codes)
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)

    def sig_of(code):
        return ((code >> bits) & 1) * 2 - 1

    def flippable(code):
        s = sig_of(code)
        return np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)

    c0 = int(((canon + 1) // 2 * (1 << bits)).sum())
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
    rows, cols = [], []
    for c in order:
        for p in flippable(c):
            rows.append(comp[int(c ^ masks[p])])
            cols.append(comp[c])
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(len(order), len(order))).tocsr()
    return len(codes), order, H


# ------------------------------------------------------------------------------------------------ old-guide kernels (guide exp(alpha N_flip)), block sums of 64 plaquettes
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
    """Circulations, flippable flags, flip-count changes and flippable counts of every walker."""
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
def nb_walk(sig, C, flp, dN, nflp, plaq, A, M, dynf, exptab, V, dtau, stamp, tick, sbuf, rbuf, logw, ELend):
    """Advance every walker by imaginary time dtau under the guided jump process (rate exp(alpha dN) per flippable plaquette); accumulate log weights -int E_L dt."""
    n_w, Np = C.shape
    nblk = (Np + 63) // 64
    W = A.shape[1]
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
                s_[l] = -s_[l]
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    d_[s] = _dN(s, s_, plaq, A, M, dynf, C_)
                    rn = exptab[d_[s] + 16]
                else:
                    rn = 0.0
                bs[s // 64] += rn - rbuf[jj]
        logw[i] = lw


class OldProjector:
    """Tables of the old-guide projector (guide exp(alpha N_flip))."""
    def __init__(self, ice, alpha, seed):
        self.ice = ice
        self.plaq = ice.plaq.astype(np.int64)
        self.sign = ice.sign.astype(np.int64)
        A = ice.A.astype(np.int64).copy()
        A[A == ice.np_] = -1
        self.A = A
        self.M = np.rint(ice.M).astype(np.int64)
        self.dyn = np.ones(ice.np_, dtype=np.bool_)
        self.exptab = np.exp(alpha * (np.arange(33) - 16.0))
        self.stamp = np.zeros(ice.np_, dtype=np.int64)
        self.tick = np.zeros(1, dtype=np.int64)
        self.sbuf = np.zeros(4096, dtype=np.int64)
        self.rbuf = np.zeros(4096)
        nb_seed(seed)


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
    """From-scratch references: adjacency from link sets (independent of the neighbour tables), psi_T of each flipped state evaluated directly."""
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

    def run(self, init, n_w, n_gen, dtau, therm, lags, rng, acorr_at=(), record_states=None):
        """Per generation: advance, record mixed energy, log mean weight, effective sample fraction, spread of walker log weights, unweighted sd of E_L, ancestor
        fractions at `lags` generations (after thermalisation), then resample (systematic).  At generations in acorr_at the E_L autocorrelation is measured on a copy."""
        st = self.make_state(init, n_w, rng)
        Lmax = max(lags) if len(lags) else 0
        anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
        logw = np.zeros(n_w)
        ELend = np.zeros(n_w)
        out = dict(e=[], lwbar=[], ess=[], lwsd=[], hops=[], nd=[], elsd=[], nflp=[], npair=[], acorr=[])
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
            if Lmax:
                anc[:, g % (Lmax + 1)] = np.arange(n_w)
            if g >= therm:
                out["nflp"].append(float(wn @ (st["nflp"] / self.ice.np_)))
                out["npair"].append(wn @ (st["npair"] / self.ice.np_))
                if Lmax:
                    out["nd"].append([len(np.unique(anc[:, (g - L) % (Lmax + 1)])) / n_w for L in lags])
            if record_states is not None and g >= therm:
                record_states(g, st, wn)
            cum = np.cumsum(wn)
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
            for key in self.KEYS:
                st[key] = st[key][picks]
            anc = anc[picks]
            if g in acorr_at:
                cp = {key: st[key].copy() for key in st}
                out["acorr"].append(self.autocorr(cp, 70, dtau=dtau, ks=(7, 67)))
                del cp
        res = {k: (np.array(v) if k != "acorr" else v) for k, v in out.items()}
        res["therm"] = therm
        res["wall"] = time.time() - t_start
        return res

    def autocorr(self, st, ngen, dtau=DTAU, ks=(7, 67)):
        """Unweighted continuation of a population state WITHOUT resampling: autocorrelation C(k dtau) of the within-population fluctuation of E_L and the sd of the accumulated
        log weight (the memory of E_L along a path)."""
        n_w = len(st["sig"])
        logw = np.zeros(n_w)
        EL = np.zeros(n_w)
        E = np.zeros((ngen + 1, n_w))
        self._walk(st, 1e-9, logw, EL)
        E[0] = EL
        acc = np.zeros(n_w)
        accsd = []
        for g in range(1, ngen + 1):
            self._walk(st, dtau, logw, EL)
            E[g] = EL
            acc += logw
            accsd.append(acc.std())
        d = E - E.mean(axis=1, keepdims=True)
        var0 = d[0].var()
        return {k: float((d[0] * d[k]).mean() / var0) for k in ks if k <= ngen}, {k: float(accsd[k - 1]) for k in ks if k <= ngen}


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


def guide_run(ice, NW, seed, NGEN, alpha, gamma, scheme="one", tag=""):
    """One pair-guide run (gamma = 0: the old guide through the same code): summary dict.  Initial population from the alpha-guide loop Metropolis; a one-generation warm-up
    population of 8 walkers triggers the compilation before the run."""
    t0 = time.time()
    L = ice.L
    rr = np.random.default_rng(seed * 100 + L + NW)
    init = loop_vmc_log(ice, alpha, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    pr = PProjector(ice, alpha, [gamma], scheme, seed=seed)
    pr.run(init, 8, 2, DTAU, 1, [], rr)
    therm = NGEN // 4
    lags = [max(1, int(round(t / DTAU))) for t in (1.0, 2.0)]
    AC = [therm + (NGEN - therm) * f // 4 for f in (1, 2, 3)]
    res = pr.run(init, NW, NGEN, DTAU, therm, lags, rr, acorr_at=AC)
    C_ = {k: float(np.mean([a[0][k] for a in res["acorr"]])) for k in (7, 67)}
    acc = {k: float(np.mean([a[1][k] for a in res["acorr"]])) for k in (7, 67)}
    es = energy_summary(res, Lcs=(0, 40))
    Np = ice.np_
    nd = res["nd"].mean(axis=0)
    d = dict(u0=-es[0][0] / Np, u0e=es[0][1] / Np, u40=-es[40][0] / Np, u40e=es[40][1] / Np, nd1=float(nd[0]), nd2=float(nd[1]), elsd=float(res["elsd"][therm:].mean()),
             sdlw=float(res["lwbar"][therm:].std()), ess=float(res["ess"][therm:].mean()), wsd=float(res["lwsd"][therm:].mean()), c1=C_[7], c2=C_[67], acc=acc[67],
             nflip=float(res["nflp"].mean()), npair=float(res["npair"].mean()), wall=time.time() - t0)
    log(f"{tag} L {L} NW {NW} seed {seed} NGEN {NGEN} alpha {alpha} gamma {gamma}: sd(E_L) {d['elsd']:.3f}; sd(log mean wt) {d['sdlw']:.5f}; ESS {d['ess']:.4f}; "
        f"sd(walker log wt) {d['wsd']:.4f}; nd@1.0 {d['nd1']:.4f} nd@2.0 {d['nd2']:.4f}; C(0.105) {d['c1']:.3f} C(1.005) {d['c2']:.3f}; accsd(1.005) {d['acc']:.3f}; "
        f"u(Lc=0) {d['u0']:.5f}+-{d['u0e']:.5f}; u(Lc=40) {d['u40']:.5f}+-{d['u40e']:.5f}; Nflip/Np {d['nflip']:.4f}; Npair/Np {d['npair']:.4f}; {d['wall']:.0f} s")
    return d


def old_series_point(ice, nw, seed, ngen):
    """Old guide (nb_walk) at population nw: u(Lc=0), effective sample fraction, Nemec N_eff = mean_g Var_walkers(E_L) / Var_g(population-mean E_L), generations >= ngen/4."""
    t0 = time.time()
    L = ice.L
    rr = np.random.default_rng(seed * 100 + L + nw)
    init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    pr = OldProjector(ice, ALPHA, seed * 1000 + L + nw)
    picks0 = rr.integers(len(init), size=nw)
    sig = np.array([init[k] for k in picks0], dtype=np.int8)
    C = np.zeros((nw, ice.np_), dtype=np.int8)
    flp = np.zeros((nw, ice.np_), dtype=np.bool_)
    dN = np.zeros((nw, ice.np_), dtype=np.int8)
    nflp = np.zeros(nw, dtype=np.int64)
    nb_init(sig, C, flp, dN, nflp, pr.plaq, pr.sign, pr.A, pr.M, pr.dyn)
    logw = np.zeros(nw)
    ELend = np.zeros(nw)
    es, ess, varw, mel = [], [], [], []
    for g in range(ngen):
        nb_walk(sig, C, flp, dN, nflp, pr.plaq, pr.A, pr.M, pr.dyn, pr.exptab, 0.0, DTAU, pr.stamp, pr.tick, pr.sbuf, pr.rbuf, logw, ELend)
        mx = logw.max()
        w = np.exp(logw - mx)
        wn = w / w.sum()
        es.append(float(wn @ ELend))
        ess.append(float(1.0 / (wn @ wn) / nw))
        varw.append(float(ELend.var()))
        mel.append(float(ELend.mean()))
        picks = np.minimum(np.searchsorted(np.cumsum(wn), (np.arange(nw) + rr.random()) / nw), nw - 1)
        sig = sig[picks]; C = C[picks]; flp = flp[picks]; dN = dN[picks]; nflp = nflp[picks]
    th = ngen // 4
    e = np.array(es[th:])
    bins = np.array([c.mean() for c in np.array_split(e, 10)])
    nplaq = ice.np_
    d = dict(nw=nw, u=-e.mean() / nplaq, ue=bins.std(ddof=1) / np.sqrt(10) / nplaq, ess=float(np.mean(ess[th:])), neff=float(np.mean(varw[th:]) / np.var(mel[th:])), wall=time.time() - t0)
    log(f"old guide L {L} N_w {nw:5d} seed {seed} NGEN {ngen}: u(Lc=0) {d['u']:.5f}+-{d['ue']:.5f}; ESS/N_w {d['ess']:.3f}; N_eff {d['neff']:.1f} (N_eff/N_w {d['neff'] / nw:.3f}); {d['wall']:.0f} s")
    return d


def fit_power(nws, us, ues):
    """u = u_inf - c N^-k by profile over k (weighted linear least squares in (u_inf, c) at each k on a grid): returns k, u_inf, c, chi2, k-range with chi2 < min + 1, and the k = 1 fit."""
    nws = np.asarray(nws, float); us = np.asarray(us); w = 1.0 / np.asarray(ues) ** 2

    def lin(k):
        X = np.column_stack([np.ones(len(nws)), -nws ** (-k)])
        coef = np.linalg.solve(X.T @ (w[:, None] * X), X.T @ (w * us))
        return coef, float((w * (us - X @ coef) ** 2).sum())

    ks = np.linspace(0.05, 3.0, 592)
    chis = np.array([lin(k)[1] for k in ks])
    j = int(np.argmin(chis))
    ok = ks[chis < chis[j] + 1.0]
    coef, chi = lin(ks[j])
    c1, chi1 = lin(1.0)
    return dict(k=float(ks[j]), uinf=float(coef[0]), c=float(coef[1]), chi2=chi, krange=(float(ok.min()), float(ok.max())), uinf_k1=float(c1[0]), chi2_k1=chi1, at_bound=bool(j in (0, len(ks) - 1)))


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
    check("pair guide on random 4^3 states: E_L, per-plaquette rates and typed N_pair, N_flip against brute force (schemes one, SD, orient6)",
          worst_el < 1e-12 and worst_rate < 1e-12 and worst_cnt == 0,
          f"{nhop} hops; max rel |E_L - brute| {worst_el:.2e}; max rel |rate - psi ratio| {worst_rate:.2e}; max integer difference of N_pair,t and N_flip {worst_cnt} (E_L and rates: float, tolerance 1e-12)")


def check_1b():
    """Exact 2^3 projected energy for pair guides, and the population scaling of the offset for a stronger gamma."""
    ice = Ice(2)
    canon = ice.sector_state(0)
    ngauss, order, H = exact_L2(ice, canon)
    ev, _ = eigsh(H.astype(float), k=1, which="SA")
    E0 = float(ev[0])
    log(f"2^3: {ngauss} Gauss states, flip component {len(order)} states, exact E0 = {E0:.6f}")
    nruns, NW, NGEN = (4, 480, 1500) if SMOKE else (8, 960, 3000)
    for tag, alpha, scheme, gam in (("alpha 0.2, gamma -0.016 (one)", 0.2, "one", [-0.016]), ("alpha 0.3, SD gamma (-0.04, -0.04)", 0.3, "SD", [-0.04, -0.04])):
        e0 = []
        for seed in range(nruns):
            rr = np.random.default_rng(3000 + seed)
            init = loop_vmc_log(ice, alpha, sweeps=60, therm=60, r=rr, start=canon, fix_winding=True)
            pr = PProjector(ice, alpha, gam, scheme, seed=17 + seed)
            res = pr.run(init, NW, NGEN, DTAU, 500, [], rr)
            e0.append(energy_summary(res, Lcs=(0,))[0][0])
        e0 = np.array(e0)
        se = e0.std(ddof=1) / np.sqrt(len(e0))
        check(f"exact 2^3 projected energy, pair guide {tag}, within 3 standard errors ({nruns} independent runs, {NW} walkers)", abs(e0.mean() - E0) <= 3 * se,
              f"E {e0.mean():.5f} +- {se:.5f}; minus exact {e0.mean() - E0:+.5f} ({(e0.mean() - E0) / se:+.2f} se)")
    sizes = (480, 1920) if SMOKE else (960, 3840, 15360)
    rows = []
    for NWs in sizes:
        e = []
        for seed in range(4):
            rr = np.random.default_rng(4000 + seed)
            init = loop_vmc_log(ice, 0.2, sweeps=60, therm=60, r=rr, start=canon, fix_winding=True)
            pr = PProjector(ice, 0.2, [-0.05], "one", seed=41 + seed)
            res = pr.run(init, NWs, 800 if SMOKE else (1500 if NWs > 4000 else 3000), DTAU, 500 if not SMOKE else 200, [], rr)
            e.append(energy_summary(res, Lcs=(0,))[0][0])
        e = np.array(e)
        rows.append(f"N_w {NWs}: {e.mean() - E0:+.5f} +- {e.std(ddof=1) / 2:.5f}")
    check("exact 2^3 population scaling of the energy offset, pair guide alpha 0.2 gamma -0.05 (reported, 4 runs per size)", True, "; ".join(rows))


def check_2():
    L, NW, NGEN = (4, 120, 600) if SMOKE else (8, 960, 2500)
    ice = Ice(L)
    seeds = (1, 2)
    old = [guide_run(ice, NW, s, NGEN, 0.2, 0.0, tag="old") for s in seeds]
    new = [guide_run(ice, NW, s, NGEN, 0.35, -0.049, tag="pair") for s in seeds]
    m = lambda rs, k: float(np.mean([r[k] for r in rs]))
    s_ = lambda rs, k: float(np.std([r[k] for r in rs], ddof=1) / np.sqrt(len(rs)))
    detail = (f"old: u(Lc=0) {m(old, 'u0'):.5f}+-{s_(old, 'u0'):.5f}, u(Lc=40) {m(old, 'u40'):.5f}, nd@1.0 {m(old, 'nd1'):.4f}, nd@2.0 {m(old, 'nd2'):.4f}, sd(E_L) {m(old, 'elsd'):.3f}; "
              f"pair: u(Lc=0) {m(new, 'u0'):.5f}+-{s_(new, 'u0'):.5f}, u(Lc=40) {m(new, 'u40'):.5f}, nd@1.0 {m(new, 'nd1'):.4f}, nd@2.0 {m(new, 'nd2'):.4f}, sd(E_L) {m(new, 'elsd'):.3f}; "
              f"lag-2 ancestor ratio pair/old {m(new, 'nd2') / m(old, 'nd2'):.2f}")
    finite = all(np.isfinite([r[k] for r in old + new for k in ("u0", "nd2", "elsd")]))
    if SMOKE:
        check(f"{L}^3 smoke: old vs pair guide ran (statistical criterion not asserted in smoke mode)", finite, detail)
    else:
        check(f"{L}^3, {NW} walkers, 2 seeds: pair guide's lag-2 ancestor fraction exceeds the old guide's (alpha 0.35, gamma -0.049)", finite and m(new, "nd2") > m(old, "nd2"), detail)


def check_3():
    L, NW, NGEN = (6, 120, 600) if SMOKE else (16, 960, 2000)
    ice = Ice(L)
    old = guide_run(ice, NW, 1, NGEN, 0.2, 0.0, tag="old")
    new = guide_run(ice, NW, 1, NGEN, 0.35, -0.049, tag="pair")
    diff = new["u0"] - old["u0"]
    se = float(np.hypot(new["u0e"], old["u0e"]))
    detail = (f"old u(Lc=0) {old['u0']:.5f}+-{old['u0e']:.5f}, u(Lc=40) {old['u40']:.5f}; pair u(Lc=0) {new['u0']:.5f}+-{new['u0e']:.5f}, u(Lc=40) {new['u40']:.5f}; "
              f"difference {diff:+.5f} = {diff / se:.1f} combined se; nd@1.0 {old['nd1']:.4f} -> {new['nd1']:.4f}, nd@2.0 {old['nd2']:.4f} -> {new['nd2']:.4f}; "
              f"sd(E_L) {old['elsd']:.2f} -> {new['elsd']:.2f}")
    if SMOKE:
        check(f"{L}^3 smoke: old vs pair guide ran (statistical criterion not asserted in smoke mode)", all(np.isfinite([old["u0"], new["u0"], old["elsd"], new["elsd"]])), detail)
    else:
        check(f"{L}^3, {NW} walkers, seed 1: u(Lc=0) of old and pair guide differ by more than 4 combined standard errors (guide dependence of the estimator)", abs(diff) > 4 * se, detail)


def check_4():
    L, NGEN = (6, 600) if SMOKE else (16, 2000)
    nws = [30, 60, 120, 240] if SMOKE else [240, 480, 960, 1920]
    ice = Ice(L)
    rows = [old_series_point(ice, nw, 1, NGEN) for nw in nws]
    us = [r["u"] for r in rows]
    ues = [max(r["ue"], 1e-9) for r in rows]
    f = fit_power(nws, us, ues)
    detail = ("; ".join(f"N_w {r['nw']}: u {r['u']:.5f}+-{r['ue']:.5f}, ESS/N_w {r['ess']:.3f}, N_eff {r['neff']:.1f}" for r in rows) +
              f"; fit u = u_inf - c N_w^-k: k {f['k']:.2f} (chi2 < min+1 for k in [{f['krange'][0]:.2f}, {f['krange'][1]:.2f}]{', at the grid bound' if f['at_bound'] else ''}), "
              f"u_inf {f['uinf']:.5f}, c {f['c']:.3f}, chi2 {f['chi2']:.2f} (4 points, 3 parameters); k = 1 fit: u_inf {f['uinf_k1']:.5f}, chi2 {f['chi2_k1']:.2f}")
    check(f"{L}^3 old guide population series N_w = {nws} completed with finite u, N_eff and a fit (u_inf reported, not asserted)",
          all(np.isfinite(us)) and all(np.isfinite([r["neff"] for r in rows])) and np.isfinite(f["k"]), detail)


def main():
    print(f"offset_runner: {'SMOKE' if SMOKE else 'FULL'} mode", flush=True)
    check_1a()
    check_1b()
    check_2()
    check_3()
    check_4()
    n_pass = sum(RESULTS)
    print(f"elapsed {time.time() - T0:.0f} s")
    print(f"TOTAL: PASS={n_pass} FAIL={len(RESULTS) - n_pass}")


if __name__ == "__main__":
    main()
