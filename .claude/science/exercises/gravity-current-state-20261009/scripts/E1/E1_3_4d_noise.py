"""E1 (3+1) noise of the smeared BD operator on sprinkled causal diamonds (rho_k = 1).
 A: element-wise Var(b1), b1 = B 1 / P (P=(4/sqrt6) rho_k^{1/2}), vs the proper height tau
    of the element's past diamond (IR size) and eps; compare eps*S(tau) (first chaos).
 B: Gaussian-window averages (sd lam) of b1 at fixed window centre; Var over realizations
    vs lam; compare with the independent-element prediction.
"""
import numpy as np, time, sys
from math import sqrt, pi, log
from scipy import integrate
from bd_core import sprinkle4d, bd4d_weights, csr_apply

rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 44)
g4 = lambda s: np.exp(-s)*(1 - 9*s + 8*s*s - (4/3)*s**3)


def S4(T):
    def inner(tau):
        a = log(T/tau); return 4*pi*tau**3*(np.sinh(2*a)/4 - a/2)*g4(pi/24*tau**4)**2
    return integrate.quad(inner, 1e-12, T, limit=400)[0]


def tau_b(P): return np.sqrt(np.maximum(P[:, 0]**2 - (P[:, 1:]**2).sum(1), 0))


def partA(eps, T, nreal, ntg):
    print(f"\n== A: eps={eps} T={T} rho={1/eps:.0f} ==", flush=True)
    bins = [2.5, 3.5, 5.0, 7.0, 9.5, 12.5, 15.0]
    rec = [[] for _ in bins[:-1]]
    t0 = time.time()
    for r in range(nreal):
        P = sprinkle4d(1/eps, T, rng)
        tb = tau_b(P)
        cand = np.nonzero(tb >= bins[0])[0]
        tg = np.sort(rng.choice(cand, size=min(ntg, cand.size), replace=False))
        ip, ix, w = bd4d_weights(P, tg, eps)
        b1 = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
        gain = np.array([np.sum(w[ip[a]:ip[a+1]]**2) for a in range(len(tg))])
        for k in range(len(bins)-1):
            m = (tb[tg] >= bins[k]) & (tb[tg] < bins[k+1])
            for val, gg, tt in zip(b1[m], gain[m], tb[tg][m]):
                rec[k].append((val, gg, tt))
    print(f"   N~{len(P)}  [{time.time()-t0:.0f}s]")
    out = []
    for k in range(len(bins)-1):
        if len(rec[k]) < 20: continue
        a = np.array(rec[k]); tm = a[:, 2].mean()
        pred = eps*S4(tm)
        print(f"   tau in [{bins[k]},{bins[k+1]}) n={len(a):5d} <tau>={tm:5.2f}  <b1>={a[:,0].mean():+.3f}"
              f"  Var b1={a[:,0].var():8.3f}  eps*S(tau)={pred:8.3f}  <A^2>={a[:,1].mean():8.3f}", flush=True)
        out.append((tm, a[:, 0].var(), pred, a[:, 1].mean()))
    return out


def partB(eps, tc, lams, nreal):
    print(f"\n== B: eps={eps}, Gaussian window centred at (tc={tc},0,0,0), trunc 2.5 lam ==", flush=True)
    res = []
    for lam in lams:
        T = tc + 2.5*lam + 0.3
        t0 = time.time(); means = []; whites = []
        for r in range(nreal):
            P = sprinkle4d(1/eps, T, rng)
            dt = P[:, 0] - tc; rr = np.sqrt((P[:, 1:]**2).sum(1))
            sel = np.nonzero((np.abs(dt) < 2.5*lam) & (rr < 2.5*lam))[0]
            ip, ix, w = bd4d_weights(P, sel, eps)
            b1 = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
            wt = np.exp(-(dt[sel]**2 + rr[sel]**2)/(2*lam*lam))
            means.append((wt*b1).sum()/wt.sum())
            whites.append((wt**2*b1**2).sum()/wt.sum()**2)  # independent-element estimate
        means = np.array(means); sd = means.std(ddof=1); sdw = sqrt(np.mean(whites))
        print(f"   lam={lam:4.2f} T={T:5.2f} N~{len(P)} targets~{len(sel)}  <b_lam>={means.mean():+.4f}"
              f"  sd={sd:.4f} (+-{sd/sqrt(2*(nreal-1)):.4f})  indep-pred={sdw:.4f}  ratio={sd/sdw:.2f}"
              f"  sd*lam^2={sd*lam*lam:.4f}  [{time.time()-t0:.0f}s]", flush=True)
        res.append((lam, sd, sdw))
    return res


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "A"
    if which == "A":
        partA(0.2, 10.0, 6, 250)
        partA(0.1, 12.0, 3, 250)
        partA(0.05, 10.0, 2, 200)
    elif which == "A2":
        partA(0.025, 8.0, 2, 150)
        partA(0.1, 15.0, 1, 200)
    elif which == "B":
        partB(0.2, 6.0, [0.4, 0.6, 0.8, 1.0, 1.3], 40)
        partB(0.1, 6.0, [0.4, 0.6, 0.8, 1.0], 25)
