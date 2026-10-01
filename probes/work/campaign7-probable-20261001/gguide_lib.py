#!/usr/bin/env python3
"""Fixed-population continuous-time projector for the pure ring model with a Gaussian-mode guide.

Supplied model (nothing adopted): link fields sigma = +-1 on the cubic L^3 torus, exact vertex Gauss law, H = -(U_p + U_p^dag)
summed over plaquettes (pure ring point, V = 0), restricted to the flip component of the canonical zero-winding state.

Guide: psi_T(sigma) = exp( alpha N_flip(sigma) - sum_q beta_q |O_q(sigma)|^2 ),  O_q = sum_l PH[l, q] sigma_l.
Importance sampling (derivation, f = psi_T phi):  d_tau f(s) = -V N(s) f(s) + sum_p [psi_T(s)/psi_T(s_p)] f(s_p), so a walker at s
leaves along plaquette p at rate r_p(s) = psi_T(s_p)/psi_T(s); lambda(s) = sum_p r_p(s); E_L(s) = V N_flip(s) - lambda(s);
log weight accumulates -int E_L dt.

Mode term in the rates.  A flippable plaquette p has all four link products sigma_l sign_l equal to c = C_p / 4 (C_p = circulation).
Flipping p changes O_q by Delta_{q,p} = c D[p,q], D[p,q] = -2 sum_k sign[p,k] PH[plaq[p,k], q] (a property of the plaquette alone).
Hence  r_p = exp(alpha dN_p) * f_cls(p,c)(O),  f_cls(O) = exp( - sum_q beta_q (2 Re(conj(O_q) E_q) + |E_q|^2) ),  E = c D[p,:].
Plaquettes with the same effective vector E form a "class"; for a few momenta along the cyclic axis there are only K ~ 3 L classes
(not N_plaq).  Per walker we keep R_c = sum over flippable plaquettes of class c of exp(alpha dN_p), so
lambda = sum_c f_c(O) R_c  costs O(K) per hop instead of O(N_plaq).  The hop is chosen by class (weight f_c R_c) and then
among the members of the class (weight exp(alpha dN_p)).

Imports the Ice geometry, nb_init, _dN, loop_vmc-style helpers and `corrected` from fw_lib.py (unmodified).
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

import numba as nb
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fw_lib import Ice, exact_L2, triple, corrected, nb_init, _dN, nb_seed, ALPHA, DTAU  # noqa: E402,F401


# ------------------------------------------------------------------------------------------------ modes and classes
def cyclic_modes(ice, ms):
    """Cyclic triples O_a(k) = N^-1/2 sum_{a-links} e^{i k x_(a+1)} sigma at k = 2 pi m / L for m in ms.
    Returns PH of shape (nl, 3 len(ms)) (columns: for each m, a = 0, 1, 2)."""
    cols = []
    for m in ms:
        _, PH = triple(ice, 2 * np.pi * m / ice.L)
        cols.append(PH)
    return np.ascontiguousarray(np.concatenate(cols, axis=0).T)


def build_classes(ice, PH, beta, tol=1e-9):
    """Group (plaquette, circulation sign) pairs by their effective mode-change vector E = c D[p, :]."""
    Np = ice.np_
    D = -2.0 * np.einsum("pk,pkq->pq", ice.sign.astype(float), PH[ice.plaq])           # (Np, nq) complex
    E = np.concatenate([D, -D])                                                       # row c_idx*Np + p, c_idx 0 <-> c=+1
    key = np.rint(np.concatenate([E.real, E.imag], axis=1) / tol).astype(np.int64)
    uniq, first, inv = np.unique(key, axis=0, return_index=True, return_inverse=True)
    inv = np.asarray(inv).reshape(-1)
    K = len(uniq)
    Ecls = E[first]                                                                    # (K, nq)
    dev = float(np.abs(E - Ecls[inv]).max())
    clsof = np.ascontiguousarray(inv.reshape(2, Np).T.astype(np.int64))                # (Np, 2)
    members = [sorted({int(p) for p in range(Np) if clsof[p, 0] == c or clsof[p, 1] == c}) for c in range(K)]
    maxm = max(len(m) for m in members)
    mem = np.full((K, maxm), -1, dtype=np.int64)
    nmem = np.zeros(K, dtype=np.int64)
    for c, m in enumerate(members):
        mem[c, :len(m)] = m
        nmem[c] = len(m)
    beta = np.asarray(beta, dtype=float)
    BE = np.ascontiguousarray(beta[None, :] * Ecls)
    c0 = np.ascontiguousarray((beta[None, :] * np.abs(Ecls) ** 2).sum(axis=1))
    return dict(K=K, clsof=clsof, mem=mem, nmem=nmem, BE=BE, c0=c0, Ecls=Ecls, class_dev=dev, D=D)


# ------------------------------------------------------------------------------------------------ brute-force references
def log_guide(ice, sigma, alpha, PH, beta):
    C = ice.circ(sigma)[:ice.np_]
    nfl = int((np.abs(C) == 4).sum())
    O = sigma.astype(float) @ PH
    return alpha * nfl - float((np.asarray(beta) * np.abs(O) ** 2).sum())


def EL_brute(ice, sigma, alpha, PH, beta, V=0.0):
    """E_L = V N_flip - sum over flippable plaquettes of psi_T(sigma_p) / psi_T(sigma), evaluated from scratch for each plaquette."""
    C = ice.circ(sigma)[:ice.np_]
    flp = np.flatnonzero(np.abs(C) == 4)
    lp0 = log_guide(ice, sigma, alpha, PH, beta)
    tot = 0.0
    for p in flp:
        s2 = sigma.copy()
        s2[ice.plaq[p]] *= -1
        tot += np.exp(log_guide(ice, s2, alpha, PH, beta) - lp0)
    return V * len(flp) - tot


# ------------------------------------------------------------------------------------------------ initial population
def loop_vmc_g(ice, alpha, PH, beta, sweeps, therm, r, start=None, fix_winding=False):
    """loop_vmc of fw_lib with the |psi_T|^2 weight exp(2 alpha dN_flip - 2 sum beta_q d|O_q|^2) (a population start only)."""
    beta = np.asarray(beta, dtype=float)
    sigma = np.ones(ice.nl, dtype=int) if start is None else start.copy()
    C = ice.circ(sigma)
    W0 = ice.winding_fast(sigma)
    O = sigma.astype(float) @ PH
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
            dO = (PH[cyc] * (-2.0 * sigma[cyc])[:, None]).sum(axis=0)
            sigma[cyc] *= -1
            C_new = (sigma[ice.plaq[aff]] * ice.sign[aff]).sum(axis=1)
            after = int((np.abs(C_new) == 4).sum())
            On = O + dO
            logacc = 2 * alpha * (after - before) - 2 * float((beta * (np.abs(On) ** 2 - np.abs(O) ** 2)).sum())
            keep = np.log(r.random()) < logacc
            if keep and fix_winding and ice.winding_fast(sigma) != W0:
                keep = False
            if keep:
                C[aff] = C_new
                O = On
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            samples.append(sigma.copy())
    return samples


# ------------------------------------------------------------------------------------------------ kernels
@nb.njit(cache=False)
def nb_init_g(sig, C, flp, dN, nflp, rate0, cls, plaq, sign, A, M, dynf, exptab, clsof):
    nb_init(sig, C, flp, dN, nflp, plaq, sign, A, M, dynf)
    n_w, Np = C.shape
    for i in range(n_w):
        for s in range(Np):
            if flp[i, s]:
                rate0[i, s] = exptab[dN[i, s] + 16]
                cls[i, s] = clsof[s, 0 if C[i, s] > 0 else 1]
            else:
                rate0[i, s] = 0.0
                cls[i, s] = -1


@nb.njit(cache=False)
def _lam_classes(R_, Om_i, BE, c0, fc):
    """Class factors fc[c] = exp(-sum_q beta_q (2 Re(conj(O_q) E_cq) + |E_cq|^2)) (0 for empty classes); returns lambda = sum_c fc R_c."""
    K = R_.shape[0]
    nq = Om_i.shape[0]
    lam = 0.0
    for c in range(K):
        if R_[c] > 0.0:
            x = c0[c]
            for m in range(nq):
                x += 2.0 * (Om_i[m].real * BE[c, m].real + Om_i[m].imag * BE[c, m].imag)
            fc[c] = np.exp(-x)
            lam += fc[c] * R_[c]
        else:
            fc[c] = 0.0
    return lam


@nb.njit(cache=False)
def _select(R_, fc, mem, nmem, k_, r_, u):
    """Plaquette chosen by the cumulative weight u in [0, lambda): first the class (weight fc R_c), then a member (weight r_)."""
    K = R_.shape[0]
    acc = 0.0
    cs = -1
    clast = -1
    for c in range(K):
        w = fc[c] * R_[c]
        if w > 0.0:
            clast = c
            if acc + w > u:
                cs = c
                break
            acc += w
    if cs < 0:
        cs = clast
        acc = 0.0
    if cs < 0:
        return -1
    u2 = (u - acc) / fc[cs]
    a2 = 0.0
    p = -1
    for jm in range(nmem[cs]):
        s = mem[cs, jm]
        if k_[s] == cs:
            a2 += r_[s]
            p = s
            if a2 > u2:
                break
    return p


@nb.njit(cache=False)
def nb_walk_g(sig, C, flp, dN, rate0, cls, Rc, nflp, Om, plaq, A, M, dynf, exptab, V, PH, BE, c0, mem, nmem, clsof,
              dtau, stamp, tick, sbuf, rbuf, cbuf, logw, ELend):
    """Advance every walker by imaginary time dtau under the guided jump process (guide: alpha N_flip - sum beta |O|^2),
    accumulating log weights -int E_L dt, with E_L = V N_flip - sum_p r_p exact for the current state."""
    n_w, Np = C.shape
    W = A.shape[1]
    nq = Om.shape[1]
    K = Rc.shape[1]
    fc = np.zeros(K)
    for i in range(n_w):
        s_ = sig[i]; C_ = C[i]; f_ = flp[i]; d_ = dN[i]; r_ = rate0[i]; k_ = cls[i]; R_ = Rc[i]
        for c in range(K):
            R_[c] = 0.0
        for s in range(Np):
            c = k_[s]
            if c >= 0:
                R_[c] += r_[s]
        t = 0.0
        lw = 0.0
        while True:
            lam = _lam_classes(R_, Om[i], BE, c0, fc)
            EL = V * nflp[i] - lam
            h = -np.log(1.0 - np.random.random()) / lam if lam > 0 else 1e300
            if t + h >= dtau:
                lw -= EL * (dtau - t)
                ELend[i] = EL
                break
            lw -= EL * h
            t += h
            u = np.random.random() * lam
            p = _select(R_, fc, mem, nmem, k_, r_, u)
            if p < 0:                       # unreachable unless the class sums are inconsistent; fail loudly rather than wrap
                lw = np.nan
                ELend[i] = np.nan
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
                        cbuf[nB] = k_[s]
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
                for m in range(nq):
                    Om[i, m] += PH[l, m] * (-2.0 * sv)
                s_[l] = -sv
            for jj in range(nB):
                s = sbuf[jj]
                if f_[s]:
                    d_[s] = _dN(s, s_, plaq, A, M, dynf, C_)
                    rn = exptab[d_[s] + 16]
                    cn_ = clsof[s, 0 if C_[s] > 0 else 1]
                else:
                    rn = 0.0
                    cn_ = -1
                r_[s] = rn
                k_[s] = cn_
                co = cbuf[jj]
                if co >= 0:
                    R_[co] -= rbuf[jj]
                    if R_[co] < 1e-9:
                        R_[co] = 0.0
                if cn_ >= 0:
                    R_[cn_] += rn
        logw[i] = lw


# ------------------------------------------------------------------------------------------------ projector
class GProjector:
    """Fixed-population projector with guide exp(alpha N_flip - sum_q beta_q |O_q|^2); the same modes are the recorded observables."""
    def __init__(self, ice, alpha, beta, PH, V=0.0, seed=1):
        self.ice = ice
        self.alpha, self.V = alpha, V
        self.PH = np.ascontiguousarray(PH.astype(np.complex128))
        nq = self.PH.shape[1]
        self.beta = np.broadcast_to(np.asarray(beta, dtype=float), (nq,)).copy()
        self.plaq = ice.plaq.astype(np.int64)
        self.sign = ice.sign.astype(np.int64)
        A = ice.A.astype(np.int64).copy()
        A[A == ice.np_] = -1
        self.A = A
        self.M = np.rint(ice.M).astype(np.int64)
        self.dyn = np.ones(ice.np_, dtype=np.bool_)
        self.ndyn = ice.np_
        self.exptab = np.exp(alpha * (np.arange(33) - 16.0))
        self.cl = build_classes(ice, self.PH, self.beta)
        self.K = self.cl["K"]
        self.stamp = np.zeros(ice.np_, dtype=np.int64)
        self.tick = np.zeros(1, dtype=np.int64)
        self.sbuf = np.zeros(4096, dtype=np.int64)
        self.rbuf = np.zeros(4096)
        self.cbuf = np.zeros(4096, dtype=np.int64)
        nb_seed(seed)

    def _walk(self, st, dtau, logw, ELend):
        cl = self.cl
        nb_walk_g(st["sig"], st["C"], st["flp"], st["dN"], st["rate0"], st["cls"], st["Rc"], st["nflp"], st["Om"], self.plaq,
                  self.A, self.M, self.dyn, self.exptab, self.V, self.PH, cl["BE"], cl["c0"], cl["mem"], cl["nmem"], cl["clsof"],
                  dtau, self.stamp, self.tick, self.sbuf, self.rbuf, self.cbuf, logw, ELend)

    def make_state(self, init, n_w, rng):
        ice = self.ice
        Np = ice.np_
        picks0 = rng.integers(len(init), size=n_w)
        sig = np.array([init[k] for k in picks0], dtype=np.int8)
        st = dict(sig=sig, C=np.zeros((n_w, Np), dtype=np.int8), flp=np.zeros((n_w, Np), dtype=np.bool_),
                  dN=np.zeros((n_w, Np), dtype=np.int8), nflp=np.zeros(n_w, dtype=np.int64),
                  rate0=np.zeros((n_w, Np)), cls=np.full((n_w, Np), -1, dtype=np.int16), Rc=np.zeros((n_w, self.K)))
        nb_init_g(st["sig"], st["C"], st["flp"], st["dN"], st["nflp"], st["rate0"], st["cls"], self.plaq, self.sign, self.A,
                  self.M, self.dyn, self.exptab, self.cl["clsof"])
        st["Om"] = np.ascontiguousarray(sig.astype(np.float64) @ self.PH)
        return st

    def run(self, init, n_w, n_gen, dtau, therm, lags, rng, track_fw=False, record_states=None):
        """Per generation: advance, record (mixed energy, log mean weight, effective sample fraction, spread of walker log weights,
        hop count, ancestor fractions at `lags` generations), resample by systematic resampling. Om is recomputed from sigma
        every 10 generations (guards float drift)."""
        st = self.make_state(init, n_w, rng)
        nq = st["Om"].shape[1]
        Lmax = max(lags) if len(lags) else 0
        anc = np.tile(np.arange(n_w), (Lmax + 1, 1)).T.copy()
        nobs = nq + 1
        hist = np.zeros((n_w, Lmax + 1, nobs)) if track_fw else None
        logw = np.zeros(n_w)
        ELend = np.zeros(n_w)
        out = dict(e=[], lwbar=[], ess=[], lwsd=[], hops=[], mix=[], nd=[], fw=[], nflp=[])
        t_start = time.time()
        for g in range(n_gen):
            if g % 10 == 0 and g > 0:
                st["Om"] = np.ascontiguousarray(st["sig"].astype(np.float64) @ self.PH)
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
            o = np.empty((n_w, nobs))
            o[:, :nq] = np.abs(st["Om"]) ** 2
            o[:, nq] = st["nflp"] / self.ndyn
            if Lmax:
                slot = g % (Lmax + 1)
                anc[:, slot] = np.arange(n_w)
                if track_fw:
                    hist[:, slot] = o
            if g >= therm:
                out["mix"].append(wn @ o)
                out["nflp"].append(float(wn @ (st["nflp"] / self.ndyn)))
                if Lmax:
                    out["nd"].append([len(np.unique(anc[:, (g - L) % (Lmax + 1)])) / n_w for L in lags])
                    if track_fw:
                        out["fw"].append(np.array([wn @ hist[:, (g - L) % (Lmax + 1)] for L in lags]))
            if record_states is not None and g >= therm:
                record_states(g, st, wn)
            cum = np.cumsum(wn)
            picks = np.minimum(np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w), n_w - 1)
            for key in ("sig", "C", "flp", "dN", "rate0", "cls", "nflp", "Om"):
                st[key] = st[key][picks]
            anc = anc[picks]
            if track_fw:
                hist = hist[picks]
        res = {k: np.array(v) for k, v in out.items()}
        res["therm"] = therm
        res["wall"] = time.time() - t_start
        return res


def energy_summary(res, Lcs=(0, 40)):
    """Population-control-corrected mixed energy with 10-bin errors (as energy_run in fw_lib), for the windows Lcs."""
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
