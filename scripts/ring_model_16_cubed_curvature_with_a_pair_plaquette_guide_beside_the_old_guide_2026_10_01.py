#!/usr/bin/env python3
"""Pair-plaquette guide in the probe fields: the per-field curvature estimate on 16^3 at k = pi/8 in three projection-time windows (ring component, supplied model).

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss law and the clause -g (U + U^dag) at V = 0, g = 1,
restricted to the connected flip component of the canonical zero-winding state, with the cyclic transverse probe fields H(h) = H - h sum_l hv_l sigma_l, hv = cos(k x_b) on the
a-links, b = (a + 1) mod 3, of the landed ring-component notes.  The curvature estimate chi = 4 a / (3 N), a = (15 E0 - 16 E1 + E2) / (12 h^2), uses E(0), E(H1), E(2 H1) with
H1 = 0.15, from the fixed-population projector (resampling interval 0.015, a guide field 0.5 h hv per probe field, mixed energy averaged over a window of generations).

Guide.  The landed estimates use the guide psi_T = exp(0.2 N_flip) (N_flip = number of flippable plaquettes, circulation +-4).  Here the guide is the pair-plaquette Jastrow guide
psi_T(sigma) = exp(alpha N_flip + gamma N_pair + sum_l bl_l sigma_l), N_pair = number of unordered pairs of flippable plaquettes that share at least one link, with the
per-field factor exp(sum_l bl_l sigma_l), bl = 0.5 h hv.  A flippable plaquette s is flipped at rate r_s = psi_T(sigma_s)/psi_T(sigma) = exp(alpha dN_s + gamma dP_s - 2 sum_{l in s}
bl_l sigma_l), the walker's log weight accumulates -int E_L dt with E_L = V N_flip - sum_l hl_l sigma_l - sum_s r_s, hl = h hv.  The mixed energy estimator is exact for ANY positive
guide in the limit of infinite population and projection time; the guide changes the population statistics (distinct ancestors, spread of weights), which is what this runner
measures.  The change dP_s of N_pair under a flip is maintained incrementally (F_u the flippability indicator, n[q] the number of flippable neighbours of q, S_s the neighbours of s
whose flippability toggles with change a_q = +-1: dP_s = sum_{q in S_s} a_q n[q] + sum over adjacent pairs {q, q'} in S_s of a_q a_q'); the field sum Fh = sum_l hl_l sigma_l is
updated on the four links of a flipped plaquette and recomputed from scratch every 500 generations (largest correction reported).

Checks: (1) the field-extended pair kernel against brute-force evaluation (psi_T of every flipped state from scratch, adjacency from the link sets independently of the
neighbour tables, field included) on random 4^3 and 3^3 states: E_L, every rate, every maintained table; (2) exact 2^3 control with the probe field: projected ground energies in the
cyclic-triple field at k = pi, h = 0, 0.15, 0.3, against exact diagonalization of the canonical flip component, for the old guide (alpha 0.2, gamma 0: the code-path control) and the
pair guide (alpha 0.35, gamma -0.049), independent runs per field; (3) 16^3 at k = pi/8, 960 walkers, seed 411, projection to 90 (6000 generations), windows [7.5, 30), [30, 60),
[60, 90), run for BOTH guides in sequence through the identical code and the same seed streams (first the pair guide (0.35, -0.049), then the old guide (0.2, 0), which is the pair
kernel with gamma = 0 and the landed guide exp(0.2 N_flip)): per window chi and u for each guide, the pair-minus-old differences with the quadrature sum of the 10-bin errors, each
guide's rise from the first to the last window (and the two steps), distinct-ancestor fractions at projection-time lags 1 and 2 (E(0) run), ESS fraction and walker sd(E_L),
reported beside the landed old-guide values of the fw_lib kernel (guide exp(0.2 N_flip): 960 walkers chi 1.0264, 1.0579, 1.1130 with u 0.28676, 0.28682, 0.28670; 1920 walkers chi
1.0209, 1.0856, 1.1047).  Check (3) passes if every value is finite; it does not assert a direction.  Finite diagnostics: estimated values with 10-bin errors for ONE seed per guide
(the bin error does not include the seed-to-seed scatter, and the three windows share walkers, so the quadrature sums treat them as independent), not certified values, population
convergence or a limit.  Expected run time about 4.3 h (six 6000-generation field runs at roughly 0.4 s per generation, plus about 1 minute for the controls); a partial result
(chi, u, ancestors per window) is logged as soon as the first guide finishes.  PCHI_SMOKE=1 runs a 6^3 version of (3) with a tiny population and shorter controls (well under a
minute); PCHI_SEED overrides the seed of (3); PCHI_SAVE_DIR=<dir> additionally saves the per-generation records of every run as .npz.  Prints TOTAL: PASS=N FAIL=M.
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

AUDIT_TIMEOUT_SEC = 21600

SMOKE = os.environ.get("PCHI_SMOKE", "") == "1"
SAVE_DIR = os.environ.get("PCHI_SAVE_DIR", "")
RESULTS = []
T0 = time.time()
ALPHA, DTAU, H1 = 0.2, 0.015, 0.15
PAIR_ALPHA, PAIR_GAMMA = 0.35, -0.049
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




# ------------------------------------------------------------------------------------------------ brute-force references (field included)
class Brute:
    """From-scratch references: adjacency from link sets (independent of the neighbour tables), psi_T of each flipped state evaluated directly,
    psi_T = exp(alpha N_flip + sum_t gamma_t N_pair,t + sum_l bl_l sigma_l); E_L = V N_flip - sum_l hl_l sigma_l - sum_s psi_T(sigma_s)/psi_T(sigma)."""
    def __init__(self, ice, alpha, gammas, scheme, hl=None, bl=None):
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
        self.hl = np.zeros(ice.nl) if hl is None else np.asarray(hl, dtype=float)
        self.bl = np.zeros(ice.nl) if bl is None else np.asarray(bl, dtype=float)

    def counts(self, sigma):
        F = (np.abs(self.ice.circ(sigma)[:self.ice.np_]) == 4)
        return int(F.sum()), np.bincount(self.PT[F[self.P1] & F[self.P2]], minlength=self.nt)

    def logpsi(self, sigma):
        nf, npair = self.counts(sigma)
        return self.alpha * nf + float(self.gam @ npair) + float(self.bl @ sigma)

    def rates(self, sigma):
        C = self.ice.circ(sigma)[:self.ice.np_]
        l0 = self.logpsi(sigma)
        out = {}
        for p in np.flatnonzero(np.abs(C) == 4):
            s2 = sigma.copy()
            s2[self.ice.plaq[p]] *= -1
            out[int(p)] = np.exp(self.logpsi(s2) - l0)
        return out

    def EL(self, sigma, V=0.0):
        r = self.rates(sigma)
        return V * len(r) - float(self.hl @ sigma) - sum(r.values())


# ------------------------------------------------------------------------------------------------ pair-guide kernels with the probe field
@nb.njit(cache=False)
def nb_fh(sig, hl, out):
    """Field sum Fh_i = sum_l hl_l sigma_{i,l} from scratch."""
    for i in range(sig.shape[0]):
        f = 0.0
        for l in range(sig.shape[1]):
            f += hl[l] * sig[i, l]
        out[i] = f


@nb.njit(cache=False)
def nb_init_p(sig, C, flp, nn, nflp, npair, rate0, Fh, plaq, sign, A, ptype, adjm, mtab, exptabN, exptabP, hl, bl, usebl):
    n_w, Np = C.shape
    nt = nn.shape[2]
    W = A.shape[1]
    dPs = np.zeros(nt, np.int64)
    Sj = np.zeros(W, np.int64)
    Sa = np.zeros(W, np.int64)
    for i in range(n_w):
        f = 0.0
        for l in range(sig.shape[1]):
            f += hl[l] * sig[i, l]
        Fh[i] = f
        cnt = 0
        for q in range(Np):
            c = 0
            for k in range(4):
                c += sig[i, plaq[q, k]] * sign[q, k]
            C[i, q] = c
            fl = (c == 4 or c == -4)
            flp[i, q] = fl
            cnt += 1 if fl else 0
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
                if usebl:
                    g = 0.0
                    for k in range(4):
                        g += bl[plaq[s, k]] * sig[i, plaq[s, k]]
                    x *= np.exp(-2.0 * g)
                rate0[i, s] = x
            else:
                rate0[i, s] = 0.0


@nb.njit(cache=False)
def nb_walk_p(sig, C, flp, nn, rate0, nflp, npair, Fh, plaq, A, ptype, adjm, mtab, exptabN, exptabP, V, hl, bl, usebl, dtau,
              stampQ, stampS, tick, sbuf, rbuf, qbuf, logw, ELend):
    """Guided jump process with rates r_s = exp(alpha dN_s + sum_t gamma_t dP_{s,t} - 2 sum_{l in s} bl_l sigma_l) for flippable s (rate0 holds them), block sums of 64
    plaquettes for the selection; E_L = V N_flip - Fh - sum_s r_s with Fh = sum_l hl_l sigma_l updated on the four links of each flipped plaquette."""
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
            # plaquettes whose rate must be refreshed: s in A[q], q in Q = A[p] u A[u] (u in S_p); the field factor of s changes only when a link of s flips, i.e. s in A[p] (inside this set)
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
                sv = s_[l]
                Fh[i] += hl[l] * (-2.0 * sv)
                s_[l] = -sv
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    dn = _dNP(s, mtab, A, adjm, C_, f_, n_, dPs, Sj, Sa)
                    rn = exptabN[dn + 16]
                    for tt in range(nt):
                        rn *= exptabP[tt, dPs[tt] + OFFP]
                    if usebl:
                        g = 0.0
                        for k in range(4):
                            g += bl[plaq[s, k]] * s_[plaq[s, k]]
                        rn *= np.exp(-2.0 * g)
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
    """Fixed-population projector, guide exp(alpha N_flip + sum_t gamma_t N_pair,t + sum_l bl_l sigma_l) in the probe field -sum_l hl_l sigma_l (set_field).  Tables per
    (torus, scheme) are cached."""
    KEYS = ("sig", "C", "flp", "nn", "nflp", "npair", "rate0", "Fh")

    def __init__(self, ice, alpha, gammas, scheme="one", V=0.0, seed=1, hl=None, bl=None):
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
        self.set_field(hl, bl)
        nb_seed(seed)

    def set_field(self, hl, bl):
        nl = self.ice.nl
        self.hl = np.zeros(nl) if hl is None else np.ascontiguousarray(hl, dtype=np.float64)
        self.bl = np.zeros(nl) if bl is None else np.ascontiguousarray(bl, dtype=np.float64)
        assert self.hl.shape == (nl,) and self.bl.shape == (nl,)
        self.usebl = bool(np.any(self.bl != 0.0))

    def _walk(self, st, dtau, logw, ELend):
        nb_walk_p(st["sig"], st["C"], st["flp"], st["nn"], st["rate0"], st["nflp"], st["npair"], st["Fh"], self.plaq, self.A, self.ptype, self.adjm, self.mtab,
                  self.exptabN, self.exptabP, self.V, self.hl, self.bl, self.usebl, dtau, self.stampQ, self.stampS, self.tick, self.sbuf, self.rbuf, self.qbuf,
                  logw, ELend)

    def state_from_sigma(self, sig):
        Np = self.ice.np_
        n_w = len(sig)
        st = dict(sig=np.ascontiguousarray(sig.astype(np.int8)), C=np.zeros((n_w, Np), dtype=np.int8), flp=np.zeros((n_w, Np), dtype=np.bool_),
                  nn=np.zeros((n_w, Np, self.nt), dtype=np.int8), nflp=np.zeros(n_w, dtype=np.int64), npair=np.zeros((n_w, self.nt), dtype=np.int64),
                  rate0=np.zeros((n_w, Np)), Fh=np.zeros(n_w))
        nb_init_p(st["sig"], st["C"], st["flp"], st["nn"], st["nflp"], st["npair"], st["rate0"], st["Fh"], self.plaq, self.sign, self.A, self.ptype, self.adjm,
                  self.mtab, self.exptabN, self.exptabP, self.hl, self.bl, self.usebl)
        return st

    def make_state(self, init, n_w, rng):
        picks0 = rng.integers(len(init), size=n_w)
        return self.state_from_sigma(np.array([init[k] for k in picks0], dtype=np.int8))

    def run(self, init, n_w, n_gen, dtau, lags, rng, fh_every=500, record_states=None, prog=0):
        """Per generation: advance, record the mixed energy, the log mean weight, the effective sample fraction, the spread of walker log weights, the unweighted sd of E_L,
        the hops, and (from generation Lmax on) the fraction of distinct ancestors `lag` generations back; then resample (systematic).  Every fh_every generations Fh is
        recomputed from the links (the largest correction is returned as fh_drift)."""
        st = self.make_state(init, n_w, rng)
        Lmax = max(lags) if len(lags) else 0
        anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
        logw = np.zeros(n_w)
        ELend = np.zeros(n_w)
        fresh = np.zeros(n_w)
        drift = 0.0
        out = dict(e=np.zeros(n_gen), lwbar=np.zeros(n_gen), ess=np.zeros(n_gen), lwsd=np.zeros(n_gen), elsd=np.zeros(n_gen), hops=np.zeros(n_gen, dtype=np.int64),
                   nd=np.full((n_gen, max(1, len(lags))), np.nan), nflp=np.zeros(n_gen))
        t_start = time.time()
        for g in range(n_gen):
            if fh_every and g % fh_every == 0 and g > 0:
                nb_fh(st["sig"], self.hl, fresh)
                drift = max(drift, float(np.abs(fresh - st["Fh"]).max()))
                st["Fh"][:] = fresh
            tk0 = int(self.tick[0])
            self._walk(st, dtau, logw, ELend)
            out["hops"][g] = int(self.tick[0]) - tk0
            mx = logw.max()
            if not np.isfinite(mx):
                raise RuntimeError(f"non-finite log weight at generation {g}")
            w = np.exp(logw - mx)
            Wt = w.sum()
            wn = w / Wt
            out["lwbar"][g] = mx + np.log(Wt / n_w)
            out["e"][g] = float(wn @ ELend)
            out["ess"][g] = float(Wt ** 2 / (w ** 2).sum() / n_w)
            out["lwsd"][g] = float(logw.std())
            out["elsd"][g] = float(ELend.std())
            out["nflp"][g] = float(wn @ (st["nflp"] / self.ice.np_))
            if Lmax:
                anc[:, g % (Lmax + 1)] = np.arange(n_w)
                if g >= Lmax:
                    out["nd"][g] = [len(np.unique(anc[:, (g - L) % (Lmax + 1)])) / n_w for L in lags]
            if record_states is not None:
                record_states(g, st, wn)
            if prog and (g + 1) % prog == 0:
                log(f"   generation {g + 1}/{n_gen}: mean E of the last {prog} generations {out['e'][g + 1 - prog:g + 1].mean():.4f}, {time.time() - t_start:.0f} s in this run")
            cum = np.cumsum(wn)
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
            for key in self.KEYS:
                st[key] = st[key][picks]
            anc = anc[picks]
        out["fh_drift"] = drift
        out["wall"] = time.time() - t_start
        return out


# ------------------------------------------------------------------------------------------------ estimators
def triple(ice, k):
    """The cyclic triple of transverse modes: a-links modulated along axis (a + 1) mod 3, so the three modes cover each plaquette orientation once.  Returns the field
    pattern hv = cos(k x_b) on the a-links."""
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    return np.cos(k * xb)


def chi_fit(E0, s0, E1, s1, E2, s2, h1, N, pref):
    """Mode-averaged chi from E(0), E(h1), E(2 h1), h^4 eliminated: E(h) = E0 - a h^2 - b h^4, a = 3 pref N chi / 4 (three modes)."""
    a = (15 * E0 - 16 * E1 + E2) / (12 * h1 ** 2)
    sa = np.sqrt(225 * s0 ** 2 + 256 * s1 ** 2 + s2 ** 2) / (12 * h1 ** 2)
    return 4 * a / (3 * pref * N), 4 * sa / (3 * pref * N)


def window_stats(res, windows):
    """Per window [lo, hi) of generations: mean mixed energy with a 10-bin error (no population-control correction, as in the landed estimate), and the window means of the
    distinct-ancestor fractions, effective sample fraction, walker sd of E_L and sd of the log mean weight."""
    out = []
    for lo, hi in windows:
        seg = res["e"][lo:hi]
        bins = np.array([c.mean() for c in np.array_split(seg, 10)])
        out.append(dict(E=float(seg.mean()), Ee=float(bins.std(ddof=1) / np.sqrt(10)), nd=np.nanmean(res["nd"][lo:hi], axis=0), ess=float(res["ess"][lo:hi].mean()),
                        elsd=float(res["elsd"][lo:hi].mean()), lwsd=float(res["lwbar"][lo:hi].std()), nflp=float(res["nflp"][lo:hi].mean())))
    return out


def run_field(pr, init, nw, ngen, rng, hvec, h, windows, lags=(), beta=0.5, tag=""):
    """Projected mixed energy in the probe field h hvec with the guide field beta h hvec, per window; the per-generation record is saved when PCHI_SAVE_DIR is set."""
    pr.set_field(h * hvec, beta * h * hvec)
    res = pr.run(init, nw, ngen, DTAU, lags, rng, prog=1000 if ngen >= 3000 else 0)
    if SAVE_DIR:
        os.makedirs(SAVE_DIR, exist_ok=True)
        np.savez(os.path.join(SAVE_DIR, f"pchi_{tag}_h{h:g}.npz"), **{k: v for k, v in res.items() if isinstance(v, np.ndarray)})
    log(f"{tag} h = {h}: {ngen} generations, {res['wall']:.0f} s ({res['wall'] / ngen:.3f} s/gen), hops/gen {res['hops'].mean():.0f}, largest field-sum correction {res['fh_drift']:.2e}")
    return window_stats(res, windows), res


def sig_of_codes(order, nl):
    bits = np.arange(nl)
    return np.array([((c >> bits) & 1) * 2 - 1 for c in order], dtype=np.int64)


# ------------------------------------------------------------------------------------------------ checks
def check_brute():
    """The field-extended pair kernel against brute force on random states: E_L, every flippable plaquette's rate, the typed pair counts, and every maintained table against a fresh
    recomputation (generic random fields and the cyclic-triple field with its guide)."""
    t0 = time.time()
    cases = [
        (4, "one", 0.35, [-0.049], "triple", 0.0),
        (4, "one", 0.2, [0.0], "random", 0.0),
        (4, "SD", 0.3, [0.05, -0.08], "random", 0.3),
        (3, "one", 0.35, [-0.049], "triple", 0.0),
    ]
    rows, ok = [], True
    for L, scheme, alpha, gam, kind, V in cases:
        ice = Ice(L)
        rr = np.random.default_rng(7 + L)
        if kind == "triple":
            hv = triple(ice, 2 * np.pi / L)
            hl, bl = 0.3 * hv, 0.5 * 0.3 * hv
        else:
            hl, bl = 0.4 * rr.standard_normal(ice.nl), 0.25 * rr.standard_normal(ice.nl)
        init = loop_vmc_log(ice, 0.2, sweeps=40, therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
        pr = PProjector(ice, alpha, gam, scheme, V=V, seed=5, hl=hl, bl=bl)
        br = Brute(ice, alpha, gam, scheme, hl=hl, bl=bl)
        n_w = 24 if L == 4 else 48
        st = pr.make_state(init, n_w, rr)
        logw = np.zeros(n_w); EL = np.zeros(n_w)
        w_el = w_rate = w_cnt = w_state = w_fh = w_r0 = 0.0
        hops0 = int(pr.tick[0])
        for call in range(6):
            pr._walk(st, 0.2, logw, EL)
            for i in range(n_w):
                sg = st["sig"][i].astype(np.int64)
                elb = br.EL(sg, V)
                w_el = max(w_el, abs(EL[i] - elb) / abs(elb))
                nf, npc = br.counts(sg)
                w_cnt = max(w_cnt, float(np.abs(npc - st["npair"][i]).max()), abs(nf - st["nflp"][i]))
                rb = br.rates(sg)
                flp_idx = np.flatnonzero(st["flp"][i])
                assert set(rb.keys()) == set(int(x) for x in flp_idx)
                w_rate = max(w_rate, max(abs(st["rate0"][i][p] - rb[p]) / rb[p] for p in rb))
                w_fh = max(w_fh, abs(st["Fh"][i] - float(hl @ sg)))
            fr = pr.state_from_sigma(st["sig"].copy())
            d_int = max(float(np.abs(fr["C"] - st["C"]).max()), float((fr["flp"] != st["flp"]).sum()), float((fr["nflp"] != st["nflp"]).sum()),
                        float(np.abs(fr["nn"].astype(int) - st["nn"].astype(int)).max()), float(np.abs(fr["npair"] - st["npair"]).max()))
            w_state = max(w_state, d_int)
            w_r0 = max(w_r0, float(np.abs(fr["rate0"] - st["rate0"]).max()))
        hops = int(pr.tick[0]) - hops0
        good = (w_el < 1e-12 and w_rate < 1e-12 and w_cnt == 0 and w_state == 0 and w_fh < 1e-10 and w_r0 < 1e-12 and hops > 100)
        ok &= good
        rows.append(f"L={L} {scheme} alpha {alpha} gamma {gam} {kind} field V {V}: {hops} hops; max rel |E_L - brute| {w_el:.1e}; max rel |rate - brute| {w_rate:.1e}; "
                    f"max |N_flip, N_pair - brute| {w_cnt:.0f}; max |maintained C/flp/nflp/nn/npair - fresh| {w_state:.0f}; max |maintained rate0 - fresh| {w_r0:.1e}; "
                    f"max |Fh - sum hl sigma| {w_fh:.1e}")
    check("field-extended pair kernel: E_L, every flippable plaquette's rate (field factor included), the typed pair counts and every maintained table agree with brute-force "
          "recomputation on random states", ok, "; ".join(rows) + f"; {time.time() - t0:.0f} s")


def check_exact(nruns, nw, ngen):
    """Exact 2^3 control with the probe field: projected ground energies (independent runs per field) for the old guide (code-path control) and the pair guide."""
    t0 = time.time()
    ice2 = Ice(2)
    canon2 = ice2.sector_state(0)
    ncodes, order, H2 = exact_L2(ice2, canon2)
    Sg = sig_of_codes(order, ice2.nl).astype(float)
    hv2 = triple(ice2, np.pi)
    Ftot = Sg @ hv2
    Ex = {h: float(eigsh((H2 - h * diags(Ftot)).tocsr(), k=1, which="SA")[0][0]) for h in (0.0, H1, 2 * H1)}
    for tag, alpha, gam in (("old guide (alpha 0.2, gamma 0: code-path control)", ALPHA, 0.0), (f"pair guide (alpha {PAIR_ALPHA}, gamma {PAIR_GAMMA})", PAIR_ALPHA, PAIR_GAMMA)):
        rows, ok = [], True
        for h in (0.0, H1, 2 * H1):
            vs, bs = [], []
            for j in range(nruns):
                pr = PProjector(ice2, alpha, [gam], "one", seed=101 + 10 * j + int(20 * h))
                pr.set_field(h * hv2, 0.5 * h * hv2)
                res = pr.run([canon2], nw, ngen, DTAU, (), np.random.default_rng(102 + 10 * j + int(20 * h)))
                seg = res["e"][ngen // 4:]
                vs.append(float(seg.mean()))
                bs.append(float(np.array([c.mean() for c in np.array_split(seg, 10)]).std(ddof=1) / np.sqrt(10)))
            v, b = np.array(vs), np.array(bs)
            m, e = float(v.mean()), float(max(v.std(ddof=1), b.mean()) / np.sqrt(nruns))
            z = (m - Ex[h]) / e
            ok &= abs(z) <= 3
            rows.append(f"h = {h}: exact {Ex[h]:.6f}, projector {m:.5f}+-{e:.5f} ({z:+.1f} sigma; {nruns} runs, scatter {v.std(ddof=1):.4f}, mean bin error {b.mean():.4f})")
        check(f"exact 2^3 control with the probe field, {tag}: projected ground energies in the cyclic-triple field at k = pi (guide field 0.5 h hv) agree with exact "
              f"diagonalization of the canonical flip component ({nw} walkers, {ngen} generations)", ok, "; ".join(rows) + f"; {time.time() - t0:.0f} s")


# landed old-guide values of the same estimate on 16^3 at k = pi/8 (fw_lib kernel, guide exp(0.2 N_flip), a guide field per probe field): 960 walkers (seeds 401/402) chi 1.0264, 1.0579, 1.1130
# with u 0.28676, 0.28682, 0.28670; 1920 walkers chi 1.0209, 1.0856, 1.1047
LANDED_OLD = {960: (1.0264, 1.0579, 1.1130), 1920: (1.0209, 1.0856, 1.1047)}
LANDED_OLD_U960 = (0.28676, 0.28682, 0.28670)
GUIDES = (("pair", PAIR_ALPHA, PAIR_GAMMA), ("old", ALPHA, 0.0))        # run in this order, the same seed streams and code path for both


def big_run(ice, NW, NGEN, seed, alpha, gamma, name, hv, WIN, NAMES, lags):
    """One guide on the torus `ice`: the three probe fields in sequence, per window chi and u (10-bin errors, one seed), distinct ancestors, ESS, walker sd(E_L).  The random
    streams depend only on (seed, L, NW), so both guides start from the same population with the same generator state."""
    t0 = time.time()
    L = ice.L
    rr = np.random.default_rng(seed * 100 + L + NW + 7)
    init = loop_vmc_log(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    log(f"{L}^3 {name} guide ({alpha}, {gamma}): initial population of {len(init)} loop-Metropolis states built")
    pr = PProjector(ice, alpha, [gamma], "one", seed=seed * 1000 + L + NW + 7)
    Es, ress = [], []
    for h in (0.0, H1, 2 * H1):
        ws, res = run_field(pr, init, NW, NGEN, rr, hv, h, WIN, lags=lags, tag=f"L{L}_seed{seed}_{name}")
        Es.append(ws)
        ress.append(res)
    out = []
    for w_ in range(3):
        E0, E1, E2 = Es[0][w_], Es[1][w_], Es[2][w_]
        c, ce = chi_fit(E0["E"], E0["Ee"], E1["E"], E1["Ee"], E2["E"], E2["Ee"], H1, ice.nv, 1.0)
        out.append(dict(chi=c, che=ce, u=-E0["E"] / ice.np_, ue=E0["Ee"] / ice.np_, nd=E0["nd"], ess=E0["ess"], elsd=E0["elsd"], lwsd=E0["lwsd"]))
    drift = max(r_["fh_drift"] for r_ in ress)
    ndall = [np.nanmean(r_["nd"][NGEN // 12:], axis=0) for r_ in ress]
    fin = bool(all(np.isfinite([o["chi"], o["che"], o["u"], o["ue"], o["ess"], o["elsd"], o["lwsd"]]).all() and np.isfinite(o["nd"]).all() for o in out)
               and all(np.isfinite(x).all() for x in ndall))
    for w_, o in enumerate(out):                      # partial result in the log as soon as a guide is finished
        log(f"{name} guide, {NAMES[w_]}: chi {o['chi']:.4f}+-{o['che']:.4f}, u {o['u']:.5f}+-{o['ue']:.5f}, distinct ancestors lag 1 {o['nd'][0]:.4f} lag 2 {o['nd'][1]:.4f}")
    return dict(win=out, drift=drift, finite=fin, wall=time.time() - t0)


def check_big(L, NW, NGEN, seed):
    t0 = time.time()
    ice = Ice(L)
    hv = triple(ice, 2 * np.pi / L)
    WIN = ((NGEN // 12, NGEN // 3), (NGEN // 3, 2 * NGEN // 3), (2 * NGEN // 3, NGEN))     # [7.5, 30), [30, 60), [60, 90) at dtau 0.015 when NGEN = 6000
    NAMES = tuple(f"window [{lo * DTAU:g}, {hi * DTAU:g})" for lo, hi in WIN)
    lags = [max(1, int(round(t / DTAU))) for t in (1.0, 2.0)]
    R = {name: big_run(ice, NW, NGEN, seed, a, g, name, hv, WIN, NAMES, lags) for name, a, g in GUIDES}
    P_, O_ = R["pair"]["win"], R["old"]["win"]
    rows = []
    for name, a, g in GUIDES:
        W_ = R[name]["win"]
        rise = W_[2]["chi"] - W_[0]["chi"]
        rise_e = float(np.hypot(W_[2]["che"], W_[0]["che"]))
        rows.append(f"{name} guide ({a}, {g}): " + "; ".join(
            f"{NAMES[w_]}: chi {o['chi']:.4f}+-{o['che']:.4f}, u {o['u']:.5f}+-{o['ue']:.5f}, distinct ancestors (E(0)) lag 1 {o['nd'][0]:.4f} lag 2 {o['nd'][1]:.4f}, "
            f"ESS {o['ess']:.4f}, walker sd(E_L) {o['elsd']:.3f}, sd(log mean weight) {o['lwsd']:.4f}" for w_, o in enumerate(W_))
            + f"; rise first to last window {rise:+.4f}+-{rise_e:.4f}, steps {W_[1]['chi'] - W_[0]['chi']:+.4f} and {W_[2]['chi'] - W_[1]['chi']:+.4f}")
    drows = []
    for w_ in range(3):
        dc = P_[w_]["chi"] - O_[w_]["chi"]
        dce = float(np.hypot(P_[w_]["che"], O_[w_]["che"]))
        du = P_[w_]["u"] - O_[w_]["u"]
        due = float(np.hypot(P_[w_]["ue"], O_[w_]["ue"]))
        drows.append(f"{NAMES[w_]}: chi {dc:+.4f}+-{dce:.4f} ({dc / dce:+.1f} sigma), u {du:+.5f}+-{due:.5f} ({du / due:+.1f} sigma)")
    rp = P_[2]["chi"] - P_[0]["chi"]
    ro = O_[2]["chi"] - O_[0]["chi"]
    rpe = float(np.hypot(P_[2]["che"], P_[0]["che"]))
    roe = float(np.hypot(O_[2]["che"], O_[0]["che"]))
    rd, rde = rp - ro, float(np.hypot(rpe, roe))
    old = " ; ".join(f"{nw_} walkers {', '.join(f'{x:.4f}' for x in v)}" for nw_, v in LANDED_OLD.items())
    ok = bool(R["pair"]["finite"] and R["old"]["finite"])
    check(f"{L}^3 at k = 2 pi/{L}, pair guide ({PAIR_ALPHA}, {PAIR_GAMMA}) and old guide ({ALPHA}, 0) in sequence through the same code with the same seed {seed} streams, a guide field per probe "
          f"field, {NW} walkers, projection {NGEN * DTAU:g}: curvature estimate and energy per plaquette in three windows, pair minus old, rise, distinct ancestors (reported, no direction asserted)",
          ok, " || ".join(rows) + " || pair minus old (one seed each; errors are the quadrature sum of the 10-bin errors, windows share walkers): " + "; ".join(drows)
          + f"; rise (last window minus first) pair minus old {rd:+.4f}+-{rde:.4f} ({rd / rde:+.1f} sigma); landed old-guide chi in the same three windows (fw_lib kernel, guide exp(0.2 N_flip), 16^3): {old}, "
          f"landed u at 960 walkers {', '.join(f'{x:.5f}' for x in LANDED_OLD_U960)}; field-sum correction at most {max(R['pair']['drift'], R['old']['drift']):.1e}; "
          f"run times {R['pair']['wall']:.0f} s and {R['old']['wall']:.0f} s; {time.time() - t0:.0f} s")


def main():
    print(f"pchi_runner: {'SMOKE' if SMOKE else 'FULL'} mode", flush=True)
    check_brute()
    if SMOKE:
        check_exact(3, 400, 1200)
        check_big(6, 120, 1200, 411)
    else:
        check_exact(8, 400, 4000)
        check_big(16, 960, 6000, int(os.environ.get("PCHI_SEED", "411")))
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")


if __name__ == "__main__":
    main()
