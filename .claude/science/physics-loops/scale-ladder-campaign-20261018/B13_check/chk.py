"""B13_check: independent continuous-time DMC for the ring model (own implementation; not dmclib).

State: sigma (int8, +-1) per link; plaquette circ = (s0+s1-s2-s3)/4 in {+-1} if flippable else 0 (same link
order/sign as the probe).  Imaginary harmonic twist eta along a unit plaquette source c: H(i eta)_{m,n} =
-J exp(eta c_p circ_p(n)) for m = flip_p n (column n, before the flip); diagonal V N_f.  Walkers do the exact
Gillespie jump process with these rates (O(1) flippable list + rejection), carry log-weight
-int(E_L - E_T)dt with E_L(n) = V N_f(n) - sum_p J exp(eta c_p circ_p(n)) (mixed estimator with uniform left
vector: exact for the Perron eigenvalue E0(i eta) = E0 - chi eta^2/2 + O(eta^4)).  Fixed E_T, comb resampling every
dt; logs log mean weight per step so population-control (UNR-type) reweighting can be applied offline.
Optional forward-walking accumulators M_s (eta = 0 runs).  Independent checker code; no claim.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import numpy as np
import numba as nb

ORI = [(0, 1), (1, 2), (2, 0)]


class Lat:
    def __init__(self, dims):
        self.dims = dims = tuple(dims)
        verts = list(itertools.product(*[range(d) for d in dims]))
        vid = {v: k for k, v in enumerate(verts)}
        self.nv = len(verts); self.nl = 3 * self.nv
        add = lambda v, a: tuple((v[k] + (k == a)) % dims[k] for k in range(3))
        link = lambda v, a: 3 * vid[v] + a
        P, root, ori = [], [], []
        for v in verts:
            for o, (i, j) in enumerate(ORI):
                P.append([link(v, i), link(add(v, i), j), link(add(v, j), i), link(v, j)]); root.append(v); ori.append(o)
        self.plaq = np.array(P, np.int64); self.root = np.array(root); self.ori = np.array(ori)
        self.np_ = len(P)
        l2p = [[] for _ in range(self.nl)]
        for p, ls in enumerate(P):
            for l in ls:
                l2p[l].append(p)
        assert all(len(x) == 4 for x in l2p)
        self.l2p = np.array(l2p, np.int64)
        D = np.zeros((self.nv, self.nl), np.int64)
        for v in verts:
            for a in range(3):
                D[vid[v], link(v, a)] += 1; D[vid[add(v, a)], link(v, a)] -= 1
        self.div = D
        self.verts, self.vid, self.link, self.add = verts, vid, link, add

    def harm(self, o):
        c = (self.ori == o).astype(float)
        return c / np.linalg.norm(c)

    def fourier(self, q, o, kind):
        ph = (self.root * np.array(q)).sum(1)
        f = np.cos(ph) if kind == 0 else np.sin(ph)
        c = np.where(self.ori == o, f, 0.0); c[np.abs(c) < 1e-12] = 0
        return c / np.linalg.norm(c)

    def circ(self, s):
        C = s[self.plaq[:, 0]] + s[self.plaq[:, 1]] - s[self.plaq[:, 2]] - s[self.plaq[:, 3]]
        return np.where(np.abs(C) == 4, C // 4, 0)

    def winding(self, s):
        crd = np.array(self.verts)
        return tuple(int(sum(s[self.link(tuple(v), a)] for v in crd if v[a] == 0)) for a in range(3))


@nb.njit(cache=True)
def _c(s, plaq, p):
    C = s[plaq[p, 0]] + s[plaq[p, 1]] - s[plaq[p, 2]] - s[plaq[p, 3]]
    if C == 4:
        return 1
    if C == -4:
        return -1
    return 0


@nb.njit(cache=True)
def nbseed(x):
    np.random.seed(x)


@nb.njit(cache=True)
def init(N, s0, plaq):
    NP = plaq.shape[0]
    S = np.empty((N, s0.shape[0]), np.int8)
    ci = np.zeros((N, NP), np.int8); fl = np.zeros((N, NP), np.int32); pos = -np.ones((N, NP), np.int32)
    nf = np.zeros(N, np.int64)
    for i in range(N):
        S[i] = s0
        for p in range(NP):
            c = _c(S[i], plaq, p); ci[i, p] = c
            if c != 0:
                fl[i, nf[i]] = p; pos[i, p] = nf[i]; nf[i] += 1
    return S, ci, fl, pos, nf


@nb.njit(cache=True)
def _rate_sum(ci_i, fl_i, n, ctw, eta, J):
    R = 0.0
    for k in range(n):
        p = fl_i[k]
        R += J * np.exp(eta * ctw[p] * ci_i[p])
    return R


@nb.njit(parallel=True, cache=True)
def el_all(ci, fl, nf, ctw, eta, V, J):
    N = ci.shape[0]
    out = np.empty(N)
    for i in nb.prange(N):
        out[i] = V * nf[i] - _rate_sum(ci[i], fl[i], nf[i], ctw, eta, J)
    return out


@nb.njit(parallel=True, cache=True)
def step(S, ci, fl, pos, nf, M, logw, plaq, l2p, ctw, eta, Cm, V, J, ET, dt):
    N = S.shape[0]
    maxfac = np.exp(abs(eta) * np.max(np.abs(ctw)))
    ns = Cm.shape[0]
    for i in nb.prange(N):
        t = 0.0
        acc = 0.0
        R = _rate_sum(ci[i], fl[i], nf[i], ctw, eta, J)
        while True:
            n = nf[i]
            EL = V * n - R
            if R <= 0.0:
                acc += (dt - t) * EL
                break
            tau = -np.log(1.0 - np.random.random()) / R
            if t + tau >= dt:
                acc += (dt - t) * EL
                break
            acc += tau * EL
            t += tau
            while True:
                p = fl[i, np.random.randint(n)]
                if np.random.random() * maxfac < np.exp(eta * ctw[p] * ci[i, p]):
                    break
            cb = ci[i, p]
            for s in range(ns):
                M[i, s] += Cm[s, p] * cb
            for k in range(4):
                S[i, plaq[p, k]] = -S[i, plaq[p, k]]
            for k in range(4):
                l = plaq[p, k]
                for u in range(4):
                    q = l2p[l, u]
                    old = ci[i, q]
                    new = _c(S[i], plaq, q)
                    if new != old:
                        if old != 0:
                            R -= J * np.exp(eta * ctw[q] * old)
                        if new != 0:
                            R += J * np.exp(eta * ctw[q] * new)
                        if old != 0 and new == 0:
                            k2 = pos[i, q]; last = fl[i, nf[i] - 1]
                            fl[i, k2] = last; pos[i, last] = k2; pos[i, q] = -1; nf[i] -= 1
                        elif old == 0 and new != 0:
                            fl[i, nf[i]] = q; pos[i, q] = nf[i]; nf[i] += 1
                        ci[i, q] = new
        logw[i] = -(acc - ET * dt)


@nb.njit(cache=True)
def comb(logw, idx):
    N = logw.shape[0]
    mx = logw.max()
    w = np.exp(logw - mx)
    tot = w.sum()
    cum = np.cumsum(w) / tot
    u0 = np.random.random() / N
    j = 0
    for k in range(N):
        u = u0 + k / N
        while cum[j] < u and j < N - 1:
            j += 1
        idx[k] = j
    return mx + np.log(tot / N), (w * w).sum() / tot ** 2 * N  # log mean weight, N/ESS


def run(lat, s0, V, N, dt, ttherm, nblocks, block_t, ctw, eta, Cm, seed, J=1.0, ET=None):
    nbseed(seed)
    S, ci, fl, pos, nf = init(N, s0.astype(np.int8), lat.plaq)
    M = np.zeros((N, Cm.shape[0])); logw = np.zeros(N); idx = np.zeros(N, np.int64)
    ctw = np.asarray(ctw, float)
    def EL_all():
        return el_all(ci, fl, nf, ctw, eta, V, J)
    et = EL_all().mean() if ET is None else ET
    nth = int(round(ttherm / dt))
    for it in range(nth):
        step(S, ci, fl, pos, nf, M, logw, lat.plaq, lat.l2p, ctw, eta, Cm, V, J, et, dt)
        lm, _ = comb(logw, idx)
        S[:] = S[idx]; ci[:] = ci[idx]; fl[:] = fl[idx]; pos[:] = pos[idx]; nf[:] = nf[idx]
        if ET is None and it >= nth // 2:  # adapt E_T during the 2nd half of thermalisation, then freeze
            et = et - lm / dt * 0.1
    nst = int(round(block_t / dt))
    LM = np.zeros((nblocks, nst)); EM = np.zeros((nblocks, nst)); NF = np.zeros((nblocks, nst)); IESS = np.zeros((nblocks, nst))
    M2 = np.zeros((nblocks, nst, Cm.shape[0]))
    for b in range(nblocks):
        M[:] = 0.0
        for k in range(nst):
            step(S, ci, fl, pos, nf, M, logw, lat.plaq, lat.l2p, ctw, eta, Cm, V, J, et, dt)
            lm, iess = comb(logw, idx)
            S[:] = S[idx]; ci[:] = ci[idx]; fl[:] = fl[idx]; pos[:] = pos[idx]; nf[:] = nf[idx]; M[:] = M[idx]
            LM[b, k] = lm; IESS[b, k] = iess
            if k % 5 == 4 or k == nst - 1:
                EM[b, k] = EL_all().mean()
            else:
                EM[b, k] = np.nan
            NF[b, k] = nf.mean()
            M2[b, k] = (M * M).mean(0)
    return dict(LM=LM, EM=EM, NF=NF, IESS=IESS, M2=M2, ET=et, dt=dt, N=N, tau=dt * np.arange(1, nst + 1))


def simple_ice(lat):
    """sigma_a(r) = (-1)^(sum of the other two coordinates): divergence-free, W = 0 (even extents)."""
    s = np.zeros(lat.nl, np.int64)
    for v in lat.verts:
        for a in range(3):
            s[lat.link(v, a)] = (-1) ** (sum(v) - v[a])
    assert np.abs(lat.div @ s).max() == 0
    return s


def component(lat, s0, maxn=10**6):
    """BFS flip component (exact ED helper for tiny tori). Returns states, nf, moves (m, n, p, circ_before_n)."""
    key = lambda s: (s > 0).tobytes()
    states = [s0.copy()]; index = {key(s0): 0}; moves = []
    q = 0
    while q < len(states):
        s = states[q]; c = lat.circ(s)
        for p in np.flatnonzero(c):
            t = s.copy(); t[lat.plaq[p]] *= -1
            k = key(t)
            if k not in index:
                index[k] = len(states); states.append(t)
                assert len(states) <= maxn
            moves.append((index[k], q, p, c[p]))
        q += 1
    S = np.array(states)
    nf = np.array([int((lat.circ(s) != 0).sum()) for s in S])
    return S, nf, np.array(moves)


def H_twist(nstates, nf, moves, V, b, c, J=1.0, imag=True):
    """dense H; imag: H_{m,n} = -J exp(eta c_p circ_p(n)) with eta=b; else Hermitian -J exp(-i b c_p circ_p(n))."""
    m, n, p, cb = moves.T
    if imag:
        H = np.zeros((nstates, nstates))
        np.add.at(H, (m, n), -J * np.exp(b * c[p] * cb))
    else:
        H = np.zeros((nstates, nstates), complex)
        np.add.at(H, (m, n), -J * np.exp(-1j * b * c[p] * cb))
    H[np.arange(nstates), np.arange(nstates)] += V * nf
    return H
