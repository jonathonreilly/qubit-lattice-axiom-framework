"""B13: sign-free continuous-time diffusion (Green's-function-type) Monte Carlo for the supplied ring model,
with a forward-walking magnetic-source curvature ("flux-fluctuation") estimator.

Model: as in pqmclib.py / B6 ringlib.py.  H = V N_f - J sum_flippable |flip_p><.|, J = 1; all off-diagonal
elements -J <= 0, so exp(-tH) is entrywise non-negative on a flip component (no sign problem).
Guide: uniform psi_T on the component (exact ground state at the RK point V = J).  Each walker performs the
exact continuous-time jump process (rate J per flippable plaquette) and carries log-weight
-int (E_L - E_T) dt with E_L = (V - J) N_f.  Fixed-population comb reconfiguration every dt.
Curvature estimator: every walker accumulates M_c = sum_flips c_p * circ_sign(state before flip) for unit
plaquette source vectors c; walkers inherit M at reconfiguration (forward walking).  Since
sum_n psi_T(n) [exp(-tau H(i eta)) Psi_0](n) ~ exp(-tau (E0(i eta) - E0)) and E0(i eta) = E0 - chi eta^2/2,
the population average <M_c(tau)^2> = A + chi_c tau for tau beyond the relaxation time; chi_c = d^2E0/db^2.
Open (forward) paths carry no topological constraint on M (unlike periodic local world-line updates).
Exploratory worker code; no claim.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import numba as nb


@nb.njit(cache=True)
def _bitw(w, l):
    return (w[l >> 6] >> np.uint64(l & 63)) & np.uint64(1)


@nb.njit(cache=True)
def _circw(w, plaq, q):
    b0 = _bitw(w, plaq[q, 0]); b1 = _bitw(w, plaq[q, 1])
    b2 = _bitw(w, plaq[q, 2]); b3 = _bitw(w, plaq[q, 3])
    if b0 == b1 and b2 == b3 and b0 != b2:
        return 1 if b0 == 1 else -1
    return 0


@nb.njit(cache=True)
def seed(s):
    np.random.seed(s)


@nb.njit(cache=True)
def init_pop(N, s0, plaq):
    NP = plaq.shape[0]
    St = np.empty((N, s0.shape[0]), np.uint64)
    Ci = np.empty((N, NP), np.int8)
    nf = np.zeros(N, np.int64)
    for i in range(N):
        St[i] = s0
        for q in range(NP):
            c = _circw(s0, plaq, q)
            Ci[i, q] = c
            if c != 0:
                nf[i] += 1
    return St, Ci, nf


@nb.njit(parallel=True, cache=True)
def propagate(St, Ci, nf, Mac, logw, plaq, pmaskw, nbr_ptr, nbr_idx, Csrc, V, J, ET, dt, nfint):
    """advance every walker by dt with the exact jump process; nfint[i] = int N_f dt (for diagnostics)."""
    N = St.shape[0]
    NP = plaq.shape[0]
    ns = Csrc.shape[0]
    for i in nb.prange(N):
        t = 0.0
        acc_nf = 0.0
        while True:
            n = nf[i]
            if n == 0:
                acc_nf += (dt - t) * n
                break
            R = J * n
            tau = -np.log(1.0 - np.random.random()) / R
            if t + tau >= dt:
                acc_nf += (dt - t) * n
                break
            acc_nf += tau * n
            t += tau
            # pick a flippable plaquette uniformly (rejection)
            while True:
                p = np.random.randint(NP)
                if Ci[i, p] != 0:
                    break
            c = Ci[i, p]
            for s in range(ns):
                Mac[i, s] += Csrc[s, p] * c
            for w in range(St.shape[1]):
                St[i, w] ^= pmaskw[p, w]
            # update circulations of p and neighbours
            cnew = _circw(St[i], plaq, p)
            if (cnew != 0) != (Ci[i, p] != 0):
                nf[i] += 1 if cnew != 0 else -1
            Ci[i, p] = cnew
            for u in range(nbr_ptr[p], nbr_ptr[p + 1]):
                q = nbr_idx[u]
                cq = _circw(St[i], plaq, q)
                if (cq != 0) != (Ci[i, q] != 0):
                    nf[i] += 1 if cq != 0 else -1
                Ci[i, q] = cq
        nfint[i] = acc_nf
        logw[i] += -((V - J) * acc_nf - ET * dt)


@nb.njit(cache=True)
def reconfigure(St, Ci, nf, Mac, logw):
    """comb resampling to the same population; returns log(mean weight)."""
    N = St.shape[0]
    mx = logw.max()
    w = np.exp(logw - mx)
    tot = w.sum()
    cum = np.cumsum(w) / tot
    u0 = np.random.random() / N
    idx = np.empty(N, np.int64)
    j = 0
    for k in range(N):
        u = u0 + k / N
        while cum[j] < u and j < N - 1:
            j += 1
        idx[k] = j
    St[:] = St[idx]
    Ci[:] = Ci[idx]
    nf[:] = nf[idx]
    Mac[:] = Mac[idx]
    lm = mx + np.log(tot / N)
    logw[:] = 0.0
    return lm


def run(lat, sigma0, V, N, dt, ntherm_t, nblocks, block_t, Csrc, seed_=1, J=1.0, verbose=False):
    seed(seed_)
    np.random.seed(seed_)
    s0 = lat.words_of_sigma(sigma0)
    St, Ci, nf = init_pop(N, s0, lat.plaq)
    ns = Csrc.shape[0]
    Mac = np.zeros((N, ns))
    logw = np.zeros(N)
    nfint = np.zeros(N)
    ET = (V - J) * nf.mean()
    nst = int(round(block_t / dt))
    # thermalise
    nth = int(round(ntherm_t / dt))
    for it in range(nth):
        propagate(St, Ci, nf, Mac, logw, lat.plaq, lat.pmaskw, lat.nbr_ptr, lat.nbr_idx, Csrc, V, J, ET, dt, nfint)
        lm = reconfigure(St, Ci, nf, Mac, logw)
        Emix = (V - J) * nf.mean()
        ET = 0.9 * ET + 0.1 * Emix if it > 10 else Emix
    Es, Eg, M2 = [], [], np.zeros((nblocks, nst, ns))
    for b in range(nblocks):
        Mac[:] = 0.0
        for k in range(nst):
            propagate(St, Ci, nf, Mac, logw, lat.plaq, lat.pmaskw, lat.nbr_ptr, lat.nbr_idx, Csrc, V, J, ET, dt, nfint)
            lm = reconfigure(St, Ci, nf, Mac, logw)
            Eg.append(ET - lm / dt)
            Emix = (V - J) * nf.mean()
            Es.append(Emix)
            ET = 0.99 * ET + 0.01 * Emix
            M2[b, k] = (Mac * Mac).mean(0) - Mac.mean(0) ** 2
        if verbose and b % max(1, nblocks // 10) == 0:
            print(f"    block {b}: Emix~{np.mean(Es[-nst:]):.5f}", flush=True)
    return dict(Emix=np.array(Es), Egrowth=np.array(Eg), M2=M2, tau=dt * np.arange(1, nst + 1), N=N, dt=dt,
                final_nf=nf.copy())


def binned(x, nb_=20):
    x = np.asarray(x, float)
    n = len(x) // nb_ * nb_
    b = x[:n].reshape(nb_, -1).mean(1)
    return float(b.mean()), float(b.std(ddof=1) / np.sqrt(nb_))


def chi_fit(res, tmin_frac=0.4):
    """slope of the block-averaged <M^2>(tau) for tau >= tmin_frac*block; error from block scatter (jackknife)."""
    M2, tau = res["M2"], res["tau"]
    sel = tau >= tmin_frac * tau[-1]
    nb_, _, ns = M2.shape
    out = []
    for s in range(ns):
        full = np.polyfit(tau[sel], M2[:, sel, s].mean(0), 1)[0]
        jk = []
        for b in range(nb_):
            m = np.delete(M2[:, sel, s], b, axis=0).mean(0)
            jk.append(np.polyfit(tau[sel], m, 1)[0])
        jk = np.array(jk)
        err = np.sqrt((nb_ - 1) / nb_ * ((jk - jk.mean()) ** 2).sum())
        out.append((float(full), float(err)))
    return out
