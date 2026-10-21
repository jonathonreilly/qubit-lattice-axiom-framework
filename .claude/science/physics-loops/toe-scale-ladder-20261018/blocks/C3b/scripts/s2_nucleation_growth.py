"""C3b s2 (candidate a): nucleation-growth formation (KJMA / Johnson-Mehl type), 2D torus.

Rate of a blank site: eps + g * 1{some neighbour formed}  (eps = nucleation, g = growth; lam_min = eps, lam_max = eps+g).
Content rule (q=2): majority of formed neighbours at formation time; tie or none -> uniform random colour.
Exact simulation: tau_x = min(N_x, t_first(x) + E_x), N ~ Exp(eps), E ~ Exp(g)  (memoryless growth stream started at
first neighbour formation; independent Poisson streams).  Variant 'seeded' (lam_min = 0): N_x = Exp(1) on iid seeds of
density p, N_x = inf elsewhere.

Observables (declared before running): colour C(r) along axes; chi_L = N * <m^2> (m = mean colour) at fixed eps for
three L; correlation scale xi(eps) defined as the first r with C(r) < C(0)/e (linear interpolation).
Criteria: LRO would show chi_L growing like L^d; no-LRO consistent if the log-log slope of chi_L vs L is
|slope| < 0.5 (i.e. far from d=2) -- declared before the run.  KJMA prediction (not a fit target): xi ~ eps^(-1/(d+1)) = eps^(-1/3).
"""
import numpy as np
import numba as nb
import heapq
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from c3b_common import check, total, nbr_table, axis_corr, mean_se, fit_loglog


@nb.njit(cache=True)
def kjma(N0, E, nbr, uc):
    Nn = N0.shape[0]
    tau = np.full(Nn, np.inf)
    tent = N0.copy()
    touched = np.zeros(Nn, np.bool_)
    formed = np.zeros(Nn, np.bool_)
    sig = np.zeros(Nn, np.int8)
    h = [(0.0, np.int64(0))]
    h.pop()
    for x in range(Nn):
        if np.isfinite(N0[x]):
            heapq.heappush(h, (N0[x], np.int64(x)))
    while len(h) > 0:
        t, x = heapq.heappop(h)
        if formed[x] or t > tent[x]:
            continue
        formed[x] = True
        tau[x] = t
        s = 0
        cnt = 0
        for j in range(nbr.shape[1]):
            y = nbr[x, j]
            if formed[y]:
                s += sig[y]
                cnt += 1
        if cnt == 0 or s == 0:
            sig[x] = 1 if uc[x] < 0.5 else -1
        else:
            sig[x] = 1 if s > 0 else -1
        for j in range(nbr.shape[1]):
            y = nbr[x, j]
            if not formed[y] and not touched[y]:
                touched[y] = True
                cand = t + E[y]
                if cand < tent[y]:
                    tent[y] = cand
                    heapq.heappush(h, (cand, np.int64(y)))
    return sig, tau


def run(L, eps, nsamp, rng, rmax, seeded_p=None):
    nbr = nbr_table((L, L))
    N = L * L
    Cs, chis, taus = [], [], []
    for s in range(nsamp):
        if seeded_p is None:
            N0 = rng.exponential(1.0 / eps, N)
        else:
            N0 = np.where(rng.random(N) < seeded_p, rng.exponential(1.0, N), np.inf)
        E = rng.exponential(1.0, N)
        sig, tau = kjma(N0, E, nbr, rng.random(N))
        assert np.all(np.isfinite(tau))
        f = sig.reshape(L, L)
        Cs.append(axis_corr(f, rmax))
        chis.append(N * f.mean() ** 2)
        taus.append(tau.mean())
    return np.array(Cs), np.array(chis), np.array(taus)


def xi_of(C):
    c0 = C[0]
    thr = c0 / np.e
    for r in range(1, len(C)):
        if C[r] < thr:
            return r - 1 + (C[r - 1] - thr) / (C[r - 1] - C[r])
    return np.nan


if __name__ == "__main__":
    rng = np.random.default_rng(1019)
    t0 = time.time()
    # cross-implementation sanity: eps -> inf makes the formation order iid-uniform, i.e. the iid-clock model of C3 A
    # with the same majority rule; compare C(1) with the independent sorted-order implementation depth_and_record.
    from c3b_common import depth_and_record
    Cq, chq, _ = run(64, 1e4, 40, rng, 4)
    nbr64 = nbr_table((64, 64))
    Ci = []
    for s_ in range(40):
        sg, _ = depth_and_record(rng.random(64 * 64), nbr64, rng.random(64 * 64), np.ones(64 * 64), 0.0)
        Ci.append(axis_corr(sg.reshape(64, 64), 4))
    Ci = np.array(Ci)
    m1, se1 = mean_se(Cq[:, 1]); m2, se2 = mean_se(Ci[:, 1])
    check("s2.0 eps->inf limit equals iid-clock model (two implementations), C(1) within 4 SE",
          abs(m1 - m2) < 4 * np.hypot(se1, se2), f"KJMA {m1:.4f}+-{se1:.4f} vs iid {m2:.4f}+-{se2:.4f}")

    eps_list = [1e-2, 3e-3, 1e-3, 3e-4, 1e-4]
    xis, xerr = [], []
    print("eps   L   nsamp  C(1)  xi(1/e)  <tau>")
    for eps in eps_list:
        scale = eps ** (-1 / 3)
        L = int(2 ** np.ceil(np.log2(24 * scale)))
        ns = max(8, int(3e6 / (L * L)))
        Cs, chis, taus = run(L, eps, ns, rng, min(L // 2, int(8 * scale) + 4))
        # bootstrap xi
        xb = []
        for b in range(200):
            ii = rng.integers(0, ns, ns)
            xb.append(xi_of(Cs[ii].mean(0)))
        xi = xi_of(Cs.mean(0))
        xis.append(xi)
        xerr.append(np.nanstd(xb))
        print(f"{eps:.0e} {L:5d} {ns:4d} {Cs.mean(0)[1]:.3f} {xi:7.3f}+-{np.nanstd(xb):.3f} {taus.mean():.2f}")
    xis = np.array(xis); xerr = np.array(xerr)
    sl, sse, chi2 = fit_loglog(np.array(eps_list), xis, xerr)
    print(f"fit xi ~ eps^a : a = {sl:.3f} +- {sse:.3f} (chi2/dof {chi2:.2f}); KJMA d=2 prediction -1/3")
    check("s2.1 xi(eps) exponent consistent with KJMA -1/3 within 4 SE or 0.05",
          abs(sl + 1 / 3) < max(4 * sse, 0.05), f"a={sl:.3f}+-{sse:.3f}")

    # FSS at fixed eps: chi_L = N <m^2>
    for eps in [1e-2, 1e-3]:
        scale = eps ** (-1 / 3)
        Ls = [int(2 ** np.ceil(np.log2(8 * scale))) * k for k in (1, 2, 4)]
        ch, che = [], []
        for L in Ls:
            ns = max(16, int(4e6 / (L * L)))
            _, chis, _ = run(L, eps, ns, rng, 2)
            m, se = mean_se(chis)
            ch.append(m); che.append(se)
            print(f"FSS eps={eps:.0e} L={L} nsamp={ns} chi_L={m:.2f}+-{se:.2f}  <m^2>={m/(L*L):.2e}")
        sl, sse, c2 = fit_loglog(np.array(Ls, float), np.array(ch), np.array(che))
        print(f"   slope dlog chi/dlog L = {sl:.3f} +- {sse:.3f}  (LRO would give 2)")
        check(f"s2.2 eps={eps:.0e}: chi_L bounded in L (|slope|<0.5, declared), no LRO", abs(sl) < 0.5,
              f"slope={sl:.3f}+-{sse:.3f}")

    # seeded lam_min = 0 variant (Theorem J): every site forms; colours decorrelate
    for p in [1e-2, 1e-3]:
        scale = p ** (-1 / 2)
        L = int(2 ** np.ceil(np.log2(16 * scale)))
        ns = max(8, int(2e6 / (L * L)))
        Cs, chis, taus = run(L, None, ns, rng, L // 2, seeded_p=p)
        C = Cs.mean(0); Cse = Cs.std(0, ddof=1) / np.sqrt(ns)
        r_far = int(6 * scale)
        print(f"seeded p={p:.0e} L={L} ns={ns}: xi={xi_of(C):.2f}, C({r_far})={C[r_far]:.4f}+-{Cse[r_far]:.4f}, C(L/2)={C[-1]:.4f}+-{Cse[-1]:.4f}")
        check(f"s2.3 seeded p={p:.0e} (lam_min=0): C(L/2) consistent with 0 (4 SE)", abs(C[-1]) < 4 * Cse[-1] + 1e-4)
    print(f"elapsed {time.time()-t0:.0f}s")
    total()
